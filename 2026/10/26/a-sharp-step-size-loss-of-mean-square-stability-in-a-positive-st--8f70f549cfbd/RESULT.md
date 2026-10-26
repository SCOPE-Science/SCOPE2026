# A sharp step-size loss of mean-square stability in a positive stochastic heat splitter

## Finding
Consider the noise-first, heat-second Lie–Trotter scheme of Bréhier, Cohen and Ulander for the one-dimensional stochastic heat equation with multiplicative Itô space-time white noise. On the smallest Dirichlet grid with two interior nodes, take the linear coefficient \(g(v)=\sigma v\), \(\sigma\geq0\), the mesh width \(h=1/3\), and any time step \(\tau>0\). Define the dimensionless time step \(x=\tau/h^2\), noise intensity \(\zeta=\sigma^2 h\), and
\[
\mathcal F(x)=\frac1x\log\left(\frac{2+y+y^2}{y(1+y+2y^2)}\right),\qquad y=e^{-2x}.
\]
For every nonzero deterministic nonnegative initial vector, the expected squared Euclidean norm after \(k\) full steps is asymptotic to a positive constant times \(\lambda_+(x,\zeta)^k\). It tends exponentially to zero if \(\zeta<\mathcal F(x)\), tends to a finite strictly positive limit if \(\zeta=\mathcal F(x)\), and grows exponentially if \(\zeta>\mathcal F(x)\). The threshold \(\mathcal F\) is strictly decreasing, with limits
\[
\lim_{x\downarrow0}\mathcal F(x)=3,\qquad \lim_{x\to\infty}\mathcal F(x)=2.
\]
Consequently, \(\zeta\leq2\) gives exponential mean-square decay for **every** positive step size; \(2<\zeta<3\) gives a unique sharp step-size boundary, below which mean-square decay holds and above which mean-square growth holds; and \(\zeta\geq3\) gives growth for every positive step size. At the boundary, there is neither decay to zero nor unbounded growth of the second moment.

Nevertheless the same method preserves componentwise nonnegativity and converges exponentially almost surely to zero **for every** \(\sigma\geq0\) and \(\tau>0\): for each \(0<\gamma<x\), almost surely its \(k\)-th iterate has \(\ell^1\)-norm at most \(e^{-\gamma k}\) for all sufficiently large \(k\). This pathwise assertion holds for arbitrary deterministic initial vectors, with the nonnegative version being positivity preserving.

In particular, with \(\sigma^2=15/2\) and \(h=1/3\), changing \(\tau\) from \((\log 2)/9\) to \((\log 4)/9\) changes exponential mean-square decay into exponential mean-square growth, although both steps are positivity preserving and almost-surely exponentially decaying. Both regimes are demonstrated by exact inequalities, not simulation.

## Assumptions and scope
The spatial domain is \([0,1]\) with homogeneous Dirichlet boundary conditions and grid points \(0,1/3,2/3,1\). The two interior values form a column \(U_k\in\mathbb R^2\). The spatial second-difference matrix is
\[
L_h=h^{-2}\begin{pmatrix}-2&1\\1&-2\end{pmatrix}.
\]
Every update uses independent standard real Gaussians \(Z_{k,1},Z_{k,2}\), independent across sites and time steps. The scheme is, exactly,
\[
U_{k+1}=B(x)D_kU_k,\quad B(x)=e^{\tau L_h},\quad
D_k=\operatorname{diag}\left(e^{\sqrt{\zeta x}Z_{k,1}-\zeta x/2},e^{\sqrt{\zeta x}Z_{k,2}-\zeta x/2}\right).
\]
This is the parabolic-Anderson specialization \(g(v)=\sigma v\) of the published noise-first, heat-second integrator. We study long-time iteration at fixed \(h\) and \(\tau\), not refinement at a fixed physical horizon. The mean-square classification assumes a deterministic vector in \(\mathbb R^2_{\geq0}\setminus\{0\}\); the almost-sure bound requires only a deterministic finite vector.

## Proof
**1. Exact heat matrix and noise moments.** The symmetric and antisymmetric eigenvalues of \(L_h\) are \(-h^{-2}\) and \(-3h^{-2}\). Therefore
\[
B(x)=\begin{pmatrix}p&q\\q&p\end{pmatrix},\quad
p=\frac{e^{-x}+e^{-3x}}2,\quad q=\frac{e^{-x}-e^{-3x}}2.
\]
For \(x>0\), \(p,q>0\), and every row and column of \(B\) sums to \(e^{-x}\). If \(d_{k,i}\) denotes a diagonal entry of \(D_k\), independence and elementary lognormal moments give
\[
\mathbb E d_{k,i}=1,\quad \mathbb E d_{k,i}^2=m=e^{\zeta x},\quad \mathbb E(d_{k,1}d_{k,2})=1.
\]

**2. Closed second-moment recursion.** Put \(X_k=\mathbb E(U_kU_k^{\mathsf T})\),
\(s_k=(X_{k,11}+X_{k,22})/2\), and \(t_k=X_{k,12}\). Conditioning on \(U_k\) and applying the moments above gives
\[
X_{k+1}=B\begin{pmatrix}mX_{k,11}&X_{k,12}\\X_{k,12}&mX_{k,22}\end{pmatrix}B.
\]
Writing
\[
u=p^2+q^2=\frac{e^{-2x}+e^{-6x}}2,\qquad
v=2pq=\frac{e^{-2x}-e^{-6x}}2>0,
\]
one obtains the **exact** two-dimensional recursion
\[
\begin{pmatrix}s_{k+1}\\t_{k+1}\end{pmatrix}
=K(x,m)\begin{pmatrix}s_k\\t_k\end{pmatrix},\qquad
K(x,m)=\begin{pmatrix}mu&v\\mv&u\end{pmatrix}.
\]
The expected squared Euclidean norm is precisely \(2s_k\), whether or not the two componentwise second moments are equal. The positive matrix \(K\) has eigenvalues
\[
\lambda_\pm=\frac{u(m+1)\pm\sqrt{u^2(m-1)^2+4mv^2}}2.
\]
For every nonzero nonnegative \(U_0\), \(s_0>0\) and \(t_0\geq0\), so Perron–Frobenius gives \(s_k\sim C\lambda_+^k\) for some \(C>0\), including at the threshold. The remaining eigenvalue satisfies \(0<\lambda_-<u<1\), because the off-diagonal entries of \(K\) are strictly positive and its determinant is \(m e^{-8x}>0\).

**3. Exact stability boundary.** At \(m=1\), \(\lambda_+=e^{-2x}<1\). Increasing \(m\geq1\) strictly increases the Perron eigenvalue, and it becomes arbitrarily large. Since \(u^2-v^2=e^{-8x}\), the unique crossing \(\lambda_+=1\) satisfies
\[
0=\det(I-K)=1-u-m(u-e^{-8x}),\qquad
m_*(x)=\frac{1-u}{u-e^{-8x}}.
\]
Set \(y=e^{-2x}\in(0,1)\). Canceling the strictly positive factor \(1-y\) yields
\[
m_*(x)=\frac{2+y+y^2}{y(1+y+2y^2)}.
\]
The denominator is positive and \(m_*>1\). Since \(m=e^{\zeta x}\), the sign of \(\lambda_+-1\) is exactly the sign of \(\zeta-\mathcal F(x)\). This proves the trichotomy for fixed \(x\).

**4. Strictly decreasing threshold and its sharp limits.** Write
\[
\mathcal F(x)=2+\frac{g(x)}x,\quad
g(x)=\log\left(\frac{2+y+y^2}{1+y+2y^2}\right),\quad y=e^{-2x}.
\]
Here \(g(0)=0\) by continuity, \(g'(0)=1\), and \(g(x)\to\log2\) as \(x\to\infty\). A direct differentiation, with \(y=e^{-2x}\), gives
\[
g''(x)=
\frac{8y(y-1)(y+1)(y^4+12y^3+10y^2+12y+1)}
{(y^2+y+2)^2(2y^2+y+1)^2}<0.
\]
Thus \(g\) is strictly concave on \((0,\infty)\), and \(g(x)/x\) is strictly decreasing because \(g(0)=0\). Its endpoint limits are \(1\) and \(0\), proving the strict monotonicity and the limits \(3\) and \(2\) for \(\mathcal F\). Continuity and strict monotonicity give the claimed unique crossover for \(2<\zeta<3\), and the two outer regimes follow from the strict inequalities \(2<\mathcal F(x)<3\) for every \(x>0\).

**5. Almost-sure decay independent of the noise strength.** The entries of \(B\) and \(D_k\) are nonnegative, so positive initial vectors remain positive. For any deterministic or adapted \(U_k\) independent of the next noise, componentwise absolute values and the column sums of \(B\) give
\[
\|B D_k U_k\|_1\leq e^{-x}\sum_{i=1}^2 d_{k,i}|U_{k,i}|.
\]
Taking conditional expectation and iterating yields
\[
\mathbb E\|U_k\|_1\leq e^{-xk}\|U_0\|_1.
\]
For every \(\gamma\in(0,x)\), Markov's inequality shows
\[
\Pr\{\|U_k\|_1>e^{-\gamma k}\}
\leq\|U_0\|_1e^{-(x-\gamma)k}.
\]
This is summable. The first Borel–Cantelli lemma proves the claimed almost-sure eventual bound without any restriction on \(\sigma\). It does not imply convergence of the second moments.

**6. Comparison to the actual spatially semidiscrete Itô equation.** Before time splitting, the two-site equation is
\[
\mathrm dU=L_hU\,\mathrm dt+\frac\sigma{\sqrt h}\operatorname{diag}(U)\,\mathrm dW,
\]
with independent Wiener coordinates. The symmetric second-moment variables solve the deterministic system
\[
\frac{\mathrm d}{\mathrm dt}\begin{pmatrix}s\\t\end{pmatrix}
=\frac1{h^2}\begin{pmatrix}\zeta-4&2\\2&-4\end{pmatrix}
\begin{pmatrix}s\\t\end{pmatrix}.
\]
Its leading eigenvalue equals \((\zeta-8+\sqrt{\zeta^2+16})/(2h^2)\), which is negative exactly when \(\zeta<3\). Thus, for \(2<\zeta<3\), the time splitting **creates** mean-square instability at sufficiently large time steps even though the underlying two-site semidiscrete Itô equation is exponentially mean-square stable.

**7. Exact finite-step witness.** Take \(h=1/3\), \(\sigma^2=15/2\), hence \(\zeta=5/2\), and \(U_0=(1,1)^\mathsf T\). If \(\tau=(\log2)/9\), then \(x=\log2\), \(y=1/4\), and
\[
m=4\sqrt2<\frac{74}{11}=m_*(x),
\]
so there is exponential mean-square decay. If instead \(\tau=(\log4)/9\), then \(x=\log4\), \(y=1/16\), and
\[
m=32>\frac{4232}{137}=m_*(x),
\]
so there is exponential mean-square growth. The first strict inequality follows after squaring positive sides; the second is an integer comparison.

## Verification
The standalone `check.py` recomputes the moment map independently from matrix multiplication; verifies the exact cutoff, its factorization, and the strictly negative second derivative by symbolic algebra; checks the two exact step-size examples; and compares independent full second-moment propagation with the reduced recursion over rational parameters and multiple deterministic inputs. It passed 1,526 deterministic assertions in the recorded execution. These finite checks corroborate, but do not replace, the preceding proof for all admissible parameters.

## Relationship to prior work
Bréhier, Cohen and Ulander introduced this positivity-preserving noise-first, heat-second splitting method and proved finite-horizon positivity, moment estimates under a CFL condition, and strong convergence. Their equation (15) in the 2024 published paper contains exactly the update specialized here; their stated theorems do not classify fixed-grid, infinite-time mean-square stability or provide the two-node sharp threshold. Lang, Petersson and Thalhammer prove general tensor-operator/spectral-radius criteria for mean-square stability of stochastic numerical approximations. Such criteria provide the abstract eigenvalue test used here, but their examined schemes are Euler–Maruyama/Milstein with rational propagators and they do not give the exact noise-versus-step curve or its strict monotonicity for this lognormal Lie–Trotter update. Chen, Dang and Hong study weak intermittency and Lyapunov-index preservation for a **periodic-boundary** stochastic heat equation and a different, \(\theta\)-time-discrete family; those results neither imply this Dirichlet Lie–Trotter phase curve nor contradict the example. Yang, Yang and Zhang study numerical positivity and almost-sure stability for a split-step backward-Euler method with finite-dimensional noise, a different numerical map; full-text comparison was unavailable. Yang and Hu's 2025 implicit/spectral analysis concerns correlated spatial noise and different discretizations. The long-known distinction between almost-sure and mean-square stochastic stability is not claimed as novel; the claimed specific contribution is the sharp step-size frontier and its strict drift between the thresholds \(3\) and \(2\) **for the published splitting update**.

## Limitations
The complete classification is for two interior Dirichlet nodes, linear multiplicative independent Gaussian noise, exact heat exponentiation, and fixed-step repeated iteration. It does not claim a corresponding frontier for finer grids, nonlinear \(g\), spatially correlated noise, reversed splitting, or a coupled continuum limit. The borderline second moment approaches a nonzero constant only for nonzero deterministic nonnegative data; the pathwise bound is independent of that sign restriction. Literature searches cannot establish absolute publication priority, and an inaccessible earlier source on a different splitting algorithm remains a residual comparison risk. No independent scientific audit has been performed.

## References
1. C.-E. Bréhier, D. Cohen and J. Ulander, *Analysis of a positivity-preserving splitting scheme for some semilinear stochastic heat equations*, ESAIM: M2AN **58** (2024), 1317–1346, DOI: 10.1051/m2an/2024032. Earliest public preprint: arXiv:2302.08858, 2023-02-17. Published full text: https://research.chalmers.se/publication/542281/file/542281_Fulltext.pdf.
2. C. Chen, T. Dang and J. Hong, *Weak intermittency of stochastic heat equation under discretizations*, Journal of Differential Equations **333** (2022), 268–301, DOI: 10.1016/j.jde.2022.06.009. Author-hosted full text: https://lsec.cc.ac.cn/~chenchch/.
3. A. Lang, A. Petersson and A. Thalhammer, *Mean-square stability analysis of approximations of stochastic differential equations in infinite dimensions*, BIT Numerical Mathematics **57** (2017), 963–990, DOI: 10.1007/s10543-017-0684-7. Open full text: https://link.springer.com/article/10.1007/s10543-017-0684-7.
4. X. Yang, Z. Yang and C. Zhang, *Stochastic heat equation: Numerical positivity and almost surely exponential stability*, Computers & Mathematics with Applications **119** (2022), 312–318, DOI: 10.1016/j.camwa.2022.05.031.
5. X. Yang and Y. Hu, *Long Time Stability and Numerical Stability of Implicit Schemes for Stochastic Heat Equations*, SIAM J. Numer. Anal. **63** (2025), 396–421, DOI: 10.1137/24M1636691.
