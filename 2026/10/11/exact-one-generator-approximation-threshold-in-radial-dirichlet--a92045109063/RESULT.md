# Exact one-generator approximation threshold in radial Dirichlet polydisk spaces

## Finding
Let \(d\ge s\ge1\), \(\beta\in\mathbb R\), and \(p_1,\ldots,p_s>0\) satisfy \(\sum_jp_j=1\). On the polydisk define
\[
t(z)=\sum_{j=1}^sp_jz_j,\qquad f(z)=1-t(z).
\]
For every integer \(N\ge0\), let \(E_N\) be the minimum of \(\|1-fP(t)\|_\beta\) over all univariate polynomials \(P\) of degree at most \(N\). Then
\[
E_N^2=\left(\sum_{n=0}^{N+1}\frac{1}{(n+1)^\beta V_n(p)}\right)^{-1},
\quad V_n(p)=\sum_{\substack{\nu_j\ge0\\\nu_1+\cdots+\nu_s=n}}
\binom{n}{\nu_1,\ldots,\nu_s}^{\!2}\prod_{j=1}^sp_j^{2\nu_j}.
\]
Set \(\gamma_s=(s+1)/2\) and \(C_p=(4\pi)^{-(s-1)/2}\prod_{j=1}^sp_j^{-1/2}\). The sharp large-degree asymptotics are
\[
E_N^2\sim
\begin{cases}
C_p(\gamma_s-\beta)N^{\beta-\gamma_s},&\beta<\gamma_s,\\
C_p/\log N,&\beta=\gamma_s.
\end{cases}
\]
For \(\beta>\gamma_s\), the squared error converges to the positive number
\[
E_\infty^2=\left(\sum_{n=0}^{\infty}\frac{1}{(n+1)^\beta V_n(p)}\right)^{-1}.
\]
Thus \(1\) can be approximated by multiples \((1-t)P(t)\) exactly when \(\beta\le(s+1)/2\). This is **not** a claim that all functions can be approximated using one generator.

In the symmetric bidisk case \(t=(z_1+z_2)/2\),
\[
V_n=4^{-n}\binom{2n}{n},\qquad C_p=\frac1{\sqrt\pi},\qquad \gamma_2=\frac32.
\]
Consequently, for \(3/2<\beta\le2\), restricted multiples fail to approximate \(1\), while unrestricted two-variable polynomial multiples succeed by the published cyclicity theorem [2]. The distinction exactly isolates an approximation barrier for one linear-form generator; it does not contradict full bidisk cyclicity.

## Assumptions and scope
The ambient radial Dirichlet-type Hilbert space is the completion of polynomials on \(\mathbb D^d\) for
\[
\left\|\sum_{\nu\in\mathbb N^d}a_\nu z^\nu\right\|_\beta^2
=\sum_{\nu\in\mathbb N^d}(|\nu|+1)^\beta|a_\nu|^2,
\qquad |\nu|=\sum_{j=1}^d\nu_j.
\]
The number \(s\) is the size of the strictly positive support of the normalized affine linear form; inactive coordinates do not enter \(t\). The weights \(p_j\) are fixed independently of \(N\), and need not be equal. Neither uniformity as some \(p_j\to0\) nor unrestricted cyclicity in higher dimensions is asserted.

## Proof
**Step 1: orthogonal homogeneous powers.** Since \(t^n\) is homogeneous of total degree \(n\), distinct \(t^n\) are orthogonal in the specified Hilbert space. By the multinomial formula,
\[
\|t^n\|_\beta^2=(n+1)^\beta V_n(p)=:w_n>0.
\]

**Step 2: exact finite-degree minimum.** Put \(R(t)=1-(1-t)P(t)\). If \(\deg P\le N\), then \(\deg R\le N+1\) and \(R(1)=1\). Conversely every polynomial \(R\) satisfying those two conditions has \(P(t)=(1-R(t))/(1-t)\) of degree at most \(N\). Writing \(R(t)=\sum_{n=0}^{N+1}r_nt^n\), its squared norm and interpolation constraint are
\[
\|R(t)\|_\beta^2=\sum_{n=0}^{N+1}w_n|r_n|^2,
\qquad\sum_{n=0}^{N+1}r_n=1.
\]
Weighted Cauchy–Schwarz gives the exact lower bound \(1/\sum_{n=0}^{N+1}w_n^{-1}\), attained uniquely by
\[
r_n=\frac{w_n^{-1}}{\sum_{j=0}^{N+1}w_j^{-1}},\qquad
P_N(t)=\frac{1-\sum_{n=0}^{N+1}r_nt^n}{1-t}.
\]
The numerator has a factor \(1-t\), so this is a genuine polynomial of degree at most \(N\).

**Step 3: the multinomial local limit.** By torus Parseval, if \(s\ge2\),
\[
V_n(p)=\frac1{(2\pi)^{s-1}}
\int_{[-\pi,\pi]^{s-1}}
\left|p_s+\sum_{j=1}^{s-1}p_je^{i\theta_j}\right|^{2n}d\theta.
\]
Strict positivity of every \(p_j\) ensures that the modulus is at most \(1\), with equality only when all phases agree, i.e. at the origin on the parameter torus. Near the origin,
\[
\log\left|p_s+\sum_{j<s}p_je^{i\theta_j}\right|^2
=-\theta^{\mathsf T}A\theta+O(|\theta|^4),
\qquad A=\operatorname{diag}(p_1,\ldots,p_{s-1})-vv^{\mathsf T},
\quad v=(p_1,\ldots,p_{s-1})^{\mathsf T}.
\]
The quadratic form is the variance of a random variable taking values \(\theta_1,\ldots,\theta_{s-1},0\) with probabilities \(p_1,\ldots,p_s\), so \(A\) is positive definite. The matrix determinant lemma gives \(\det A=\prod_{j=1}^sp_j\). Splitting the integral into a small neighborhood of the unique maximum and its compact complement, Gaussian rescaling and dominated convergence yield
\[
V_n(p)\sim\frac{1}{(2\pi)^{s-1}}
\frac{\pi^{(s-1)/2}}{\sqrt{\det A}}n^{-(s-1)/2}
=(4\pi)^{-(s-1)/2}\left(\prod_{j=1}^sp_j\right)^{-1/2}n^{-(s-1)/2}.
\]
For \(s=1\), \(t=z_1\), \(V_n=1\), and the same formula holds with the zero-dimensional determinant convention.

**Step 4: sharp transition and constants.** It follows that
\[
\frac1{w_n}\sim C_p^{-1}n^{(s-1)/2-\beta}
=C_p^{-1}n^{\gamma_s-\beta-1}.
\]
Integral comparison of positive series yields, when \(\beta<\gamma_s\),
\[
\sum_{n=0}^{N+1}w_n^{-1}\sim\frac{N^{\gamma_s-\beta}}{C_p(\gamma_s-\beta)},
\]
whereas at equality the partial sum is \(\sim C_p^{-1}\log N\), and above equality the complete sum converges. Substituting into Step 2 proves all cases. For the symmetric bidisk, Vandermonde's identity \(\sum_k\binom nk^2=\binom{2n}{n}\) proves the stated specialization. The distinction from unrestricted bidisk cyclicity follows from [2, Theorem 3.1], whose multiplier class includes **all** bivariate polynomials.

## Verification
The accompanying standalone script `verify_affine_generator.py` uses exact rational arithmetic to compare the finite minimization formula with its directly evaluated norm and verifies the weighted Euler–Lagrange equalities for several rational affine weights, including three active coordinates. It also checks Vandermonde's specialization through degree \(80\) and numerical Gaussian constants for two, three, and four active coordinates. Running `python verify_affine_generator.py` produces a PASS message and three asymptotic-ratio lines. These finitely many computations are checks of formulas, not proofs of the all-degree theorem; Steps 1–4 supply the proof.

## Relationship to prior work
Beslikas and Torkinejad Ziarati [1] study critical **unrestricted** cyclicity in the same radial total-degree spaces and note that the elementary radial-dilation approach fails to establish cyclicity of \(2-z_1-z_2\) above parameter \(3/2\). Their Lemma 3.8 averages a univariate function over **all** convex combinations \(uz_1+(1-u)z_2\) and has a different exact norm shift; it does not analyze a fixed affine average or the restricted ideal \((1-t)\mathbb C[t]\). Nailwal and Zalar [2] prove that \(2-z_1-z_2\) is cyclic for all parameters at most \(2\) when **both coordinate multipliers** are permitted, so their result and the restricted obstruction are compatible. The earlier product-weight bidisk analysis [3] and [4] concerns the distinct norm \(\sum_{k,l}(k+1)^\beta(l+1)^\beta|a_{kl}|^2\), not the radial total-degree norm or this restriction. The new quantitative distinction is precisely between one-generator and full-coordinate multiplier approximation, with the sharp support-size law and exact finite-degree errors.

## Limitations
The conclusion is limited to polynomial multipliers \(P(t)\). It is not a noncyclicity result for unrestricted two-variable multipliers. For fixed positive \(p_j\), the asymptotic constants are sharp; no uniform estimate across degenerating supports \(p_j\to0\) is asserted. The argument makes no claim about unrestricted polydisk cyclicity for \(d>2\), or about arbitrary nonlinear generators. No independently performed audit is claimed.

## References
[1] A. Beslikas and P. Torkinejad Ziarati, *Critical cyclicity in Dirichlet-type spaces on the bidisk*, arXiv:2609.09952, originally public September 9, 2026. §§1.4, 3.3, especially Lemma 3.8.

[2] R. Nailwal and A. Zalar, *Cyclic polynomials in Dirichlet-type spaces of the unit bidisk*, arXiv:2511.13441, originally public November 17, 2025. Theorem 3.1 and Corollary 3.3.

[3] C. Bénéteau, A. A. Condori, C. Liaw, D. Seco and A. A. Sola, *Cyclicity in Dirichlet-type spaces and extremal polynomials II: functions on the bidisk*, arXiv:1310.4094, 2013.

[4] C. Bénéteau, G. Knese, Ł. Kosiński, C. Liaw, D. Seco and A. Sola, *Cyclic polynomials in two variables*, arXiv:1408.3616, 2014.
