# Exact momentum and relaxation frontiers for randomized multi-reflection Douglas–Rachford on identity systems

## Finding

Consider the randomized multi-reflection Douglas–Rachford iteration with raw heavy-ball momentum, as defined below, on \(A=I_m\), with \(m\ge2\) and \(r\ge1\) independently sampled coordinate-hyperplane reflections per outer iteration. Fix \(0<\alpha<1\), momentum \(\beta\ge0\), and deterministic \(x^1=x^0\ne b\). Write
\[
q_{m,r}=\frac{1-(1-2/m)^r}{2},\qquad
\beta_{\mathrm c}(\alpha,m,r)
=\frac{\sqrt{\alpha^2(1-2q_{m,r})^2+4(1-\alpha)}-\alpha(1-2q_{m,r})}{2}.
\]
Then \(0<\beta_{\mathrm c}<1\), and **the complete mean-square classification** is:

* For \(0\le\beta<\beta_{\mathrm c}\), \(\mathbb E\|x^k-b\|_2^2\) decays exponentially.
* At \(\beta=\beta_{\mathrm c}\), \(\mathbb E\|x^k-b\|_2^2\) converges to a finite **strictly positive** limit.
* For \(\beta_{\mathrm c}<\beta<1\), \(\mathbb E\|x^k-b\|_2^2\) grows exponentially, although \(\mathbb E(x^k-b)\to0\) exponentially.
* For \(\beta\ge1\), mean-square convergence also fails.

For \(m=2\) the critical momentum is \(\sqrt{1-\alpha}\), **independently of the reflection count**. For every \(m>2\) it increases strictly with \(r\) and approaches \(\sqrt{1-\alpha}\).

There is also an exact **local acceleration transition**. Let \(\rho(\beta)\) denote the spectral radius of the single-coordinate second-moment operator, which determines the asymptotic mean-square factor. At zero momentum, put
\[
\mu=1-2\alpha q_{m,r},\qquad v=1-4\alpha(1-\alpha)q_{m,r}.
\]
Then \(\rho(0)=v\) and
\[
\rho'(0)=\frac{4\alpha q_{m,r}(1-2\alpha q_{m,r})(2\alpha-1)}{v}.
\]
Consequently sufficiently small positive momentum strictly **improves** the mean-square factor when \(0<\alpha<1/2\), but strictly **worsens** it when \(1/2<\alpha<1\). At \(\alpha=1/2\), the first derivative vanishes but \(\rho''(0)=2q_{m,r}/(1-q_{m,r})>0\): small momentum worsens the factor quadratically. This transition holds for every admissible dimension and reflection count.

For instance, \(m=2\), \(\alpha=1/2\) gives the exact ceiling \(\beta<1/\sqrt2=0.7071067811\ldots\). The general sufficient condition in Han–Su–Xie's Theorem 4.1 specializes to the much narrower \(\beta<(\sqrt3-1)/4=0.1830127018\ldots\). **That particular unrelaxed one-reflection threshold was already accessible from related exact Kaczmarz analysis**; the new claim is the full relaxed, multiple-reflection frontier together with its local-rate sign transition, not priority for this special case.

## Assumptions and scope

Fix integers \(m\ge2\), \(r\ge1\), and \(b\in\mathbb R^m\). The linear equations are \(I_m x=b\); their coordinate hyperplanes are \(C_i=\{x:x_i=b_i\}\). A reflection about \(C_i\) is \(R_i(x)=x-2(x_i-b_i)e_i\). At each outer step \(k\ge1\), independently sample \(J_{k,1},\ldots,J_{k,r}\) uniformly from \(\{1,\ldots,m\}\); all samples are independent across outer steps and within each step. Define
\[
z_k=R_{J_{k,r}}\cdots R_{J_{k,1}}(x^k),\qquad
x^{k+1}=(1-\alpha)x^k+\alpha z_k+\beta(x^k-x^{k-1}).
\]
Assume \(x^0=x^1\) is deterministic, \(0<\alpha<1\), \(\beta\ge0\), and exact real arithmetic. No conclusion is asserted for dependent row selections, nonidentity matrices, inconsistent systems, adaptive momentum, or floating-point implementations.

## Proof

**1. Reflection parity and exact coefficient law.** Fix a coordinate \(i\). Its sign is reversed once for each sampled occurrence of index \(i\). Each of the \(r\) draws hits that coordinate with probability \(1/m\). Thus the odd-parity probability is
\[
q:=\Pr\bigl\{\operatorname{Binomial}(r,1/m)\text{ is odd}\bigr\}
=\frac{1-(1-2/m)^r}{2}\in(0,1/2].
\]
Let \(t_k=(x^k-b)_i\). Independently for each outer step, its update is
\[
t_{k+1}=(a_k+\beta)t_k-\beta t_{k-1},\quad
\Pr\{a_k=1\}=1-q,\quad \Pr\{a_k=1-2\alpha\}=q.
\]
Although distinct coordinate coefficients within an outer step may be correlated, each coordinate's coefficient sequence is independent over steps, and \(\mathbb E\|x^k-b\|_2^2=\sum_i\mathbb E t_{k,i}^2\). Thus the scalar classification suffices for every deterministic nonzero vector.

**2. Positive second-moment operator.** Denote \(\mu=\mathbb Ea_k=1-2\alpha q\), \(v=\mathbb Ea_k^2=1-4\alpha(1-\alpha)q\), and \(\sigma^2=v-\mu^2=4\alpha^2q(1-q)>0\). For \(s_k=\mathbb E t_k^2\) and \(u_k=\mathbb E(t_kt_{k-1})\), independence gives the exact recurrence
\[
\begin{pmatrix}s_{k+1}\\u_{k+1}\\s_k\end{pmatrix}
=M\begin{pmatrix}s_k\\u_k\\s_{k-1}\end{pmatrix},\quad
M=\begin{pmatrix}
v+2\beta\mu+\beta^2&-2\beta(\mu+\beta)&\beta^2\\
\mu+\beta&-\beta&0\\1&0&0
\end{pmatrix}.
\]
Direct expansion, reproduced in `verify.py`, yields
\[
\det(I-M)=4\alpha q\bigl(1-\alpha-\beta^2+\alpha\beta(2q-1)\bigr).
\]
A sign of this determinant alone would not establish sufficiency; the next argument supplies the complete spectral and boundary classification.

**3. Exact mean-square stability criterion.** For \(0\le\beta<1\) the mean recurrence matrix
\[
B=\begin{pmatrix}\mu+\beta&-\beta\\1&0\end{pmatrix}
\]
is Schur stable by the quadratic Jury conditions \(1-\mu>0\), \(1+\mu+2\beta>0\), and \(1-\beta>0\). Put \(g_j=e_1^\mathsf{T}B^je_1\). The discrete Lyapunov equation \(W=BWB^\mathsf{T}+e_1e_1^\mathsf{T}\) yields the exact impulse energy
\[
G:=\sum_{j\ge0}g_j^2
=\frac{1+\beta}{(1-\beta)(1-\mu)(1+\mu+2\beta)}.
\]
Write the random scalar coefficient as \(a_k=\mu+\eta_k\), with independent centered \(\eta_k\) of variance \(\sigma^2\). Variation of constants, followed by expectation, gives for every \(n\ge1\)
\[
s_n=d_n^2+\sigma^2\sum_{j=1}^{n-1}g_{n-1-j}^2s_j,
\qquad d_n=e_1^\mathsf{T}B^{n-1}(t_1,t_0)^\mathsf{T}.
\]
The cross terms vanish by the martingale-difference property of \(\eta_jt_j\). The kernel is nonnegative. Its total mass is \(\sigma^2G\), and
\[
\sigma^2G<1\quad\Longleftrightarrow\quad
1-\alpha-\beta^2+\alpha\beta(2q-1)>0.
\]
If the inequality is strict, \(B\) is Schur stable and a slightly exponentially weighted version of the kernel still has mass below one. The renewal equation therefore gives exponential decay of \(s_n\).

If the kernel mass equals or exceeds one, let \(t\in(0,1]\) be the unique solution of \(\sigma^2 t\sum_{j\ge0}g_j^2t^j=1\); equality corresponds to \(t=1\). Multiplying the preceding recurrence by \(t^{n-1}\) gives a renewal equation with probability weights \(\sigma^2t^{j+1}g_j^2\). These have finite mean and span one because \(g_0=1\) and \(g_1=\mu+\beta>0\). The forcing \(t^{n-1}d_n^2\) is summable and not identically zero when \(t_0=t_1\ne0\). The elementary arithmetic renewal theorem consequently gives
\[
t^{n-1}s_n\longrightarrow
\frac{\sum_{n\ge1}t^{n-1}d_n^2}
{\sigma^2\sum_{j\ge0}(j+1)t^{j+1}g_j^2}>0.
\]
Thus at the boundary the second moment approaches a positive limit, and strictly beyond it (while \(\beta<1\)) it grows exponentially. For \(\beta\ge1\), the deterministic mean recurrence matrix has roots of modulus at least one; the nonzero synchronized initial state is not a decaying mode. Jensen's inequality then rules out mean-square convergence. Solving the strict quadratic inequality in \(\beta\ge0\) gives precisely the stated \(\beta_{\mathrm c}\).

**4. Reflection count, example, and local rate.** When \(m=2\), \(q=1/2\) at every positive \(r\). When \(m>2\), \(q\) increases strictly to \(1/2\), and implicit differentiation of the threshold equation gives \(d\beta_{\mathrm c}/dq=2\alpha\beta_{\mathrm c}/(2\beta_{\mathrm c}+\alpha(1-2q))>0\).

For \(\beta=0\), the nonzero eigenvalue of \(M\) is \(v\in(0,1)\), hence it is a simple isolated spectral-radius eigenvalue. Differentiating \(\det(\lambda I-M)=0\) at \((\lambda,\beta)=(v,0)\) gives the displayed \(\rho'(0)\). At \(\alpha=1/2\), a second differentiation gives \(\rho''(0)=2q/(1-q)>0\). Since \(1-2\alpha q>0\), the sign of the first derivative is exactly the sign of \(2\alpha-1\), completing the local-rate classification.

## Verification

Run `python verify.py` with NumPy and SymPy installed (versions need only support the standard matrix, polynomial, and eigenvalue operations). The file checks the exact Lyapunov identity, determinant factorization, momentum threshold, and first and second spectral-radius derivatives; it independently enumerates reflection parity, compares direct finite-step scenario enumeration with the covariance recurrence, and samples stability margins across dimensions, reflection counts, and relaxation parameters. The recorded run passed 1,007 deterministic assertions. The finite checks do **not** prove the infinite-time result; that depends on the preceding Lyapunov/renewal analysis.

## Relationship to prior work

Han, Su and Xie introduced the randomized \(r\)-sets Douglas–Rachford method and its heavy-ball extension. Their Algorithm 2 fixes the iteration considered here, and Theorem 4.1 supplies a sufficient mean-square condition in terms of two aggregate constants; the inspected proof uses upper bounds on mixed momentum terms. The present exact identity-system frontier and its relaxation-dependent local acceleration transition are not stated in that theorem or its proof. Their Theorem 3.1 and Remark 7.4 already give an equality case for the **momentum-free** expected-error bound, so no novelty is claimed for that known fact.

Existing stochastic Kaczmarz momentum and covariance analyses cover aspects of the same mathematical mechanism. In particular, a prior exact frontier for smoothed-momentum Kaczmarz subsumes the \(r=1\), \(\alpha=1/2\) unrelaxed specialization of the present threshold. The asserted additional result is the complete dependence on arbitrary \(\alpha\in(0,1)\), all reflection counts and dimensions, and the sign change of local mean-square acceleration. Generic covariance and discrete Lyapunov theory provide the proof machinery but do not themselves report this combined method-specific frontier. Equivalent formulations elsewhere remain a literature risk.

## Limitations

The test matrix has condition number one. These sharp formulas are not asserted to hold for general row geometries or nonuniform sampling. Reflection count is the number of inner reflections, **not** a cost-normalized convergence comparison. For large momentum in the unstable region, signed means can converge while second moments do not; that does not imply almost-sure divergence. Neither a global optimal momentum nor global monotonicity of the mean-square factor is claimed: the acceleration comparison is rigorously local at zero momentum. All results presume independent row draws, constant parameters, no perturbation noise, and exact arithmetic.

## References

1. D. Han, Y. Su, and J. Xie, *Randomized Douglas–Rachford Methods for Linear Systems: Improved Accuracy and Efficiency*, arXiv:2207.04291, originally public 2022-07-09; SIAM Journal on Optimization 34 (2024), 1045–1070. https://arxiv.org/abs/2207.04291 ; https://doi.org/10.1137/23M1567503 .
2. R. Bollapragada, T. Chen, and R. Ward, *On the fast convergence of minibatch heavy ball momentum*, arXiv:2206.07553, originally public 2022-06-15; IMA Journal of Numerical Analysis, published online 2024-08-08. https://arxiv.org/abs/2206.07553 .
3. A. Agaskar, C. Wang, and Y. Lu, *Randomized Kaczmarz algorithms: Exact MSE analysis and optimal sampling probabilities*, GlobalSIP 2014, pp. 389–393. https://dash.harvard.edu/entities/publication/73120379-2750-6bd4-e053-0100007fdf3b .
