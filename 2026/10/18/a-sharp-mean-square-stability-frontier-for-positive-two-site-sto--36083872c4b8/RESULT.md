# A sharp mean-square stability frontier for positive two-site stochastic heat splitting

## Finding

A positivity-preserving Lie–Trotter exponential discretization of a two-site stochastic heat equation has an exact noise–time-step mean-square stability frontier. Let \(a>b>0\), \(h>0\), and \(\sigma\ge0\). Define independent Gaussian increments \(\Delta B_{n,1},\Delta B_{n,2}\sim N(0,h)\), independent also between time steps, and
\[
X_{n+1}=S_hD_{n,h}X_n,\qquad
S_h=e^{-ah}\begin{pmatrix}\cosh(bh)&\sinh(bh)\\\sinh(bh)&\cosh(bh)\end{pmatrix},\quad
D_{n,h}=\operatorname{diag}(e^{\sigma\Delta B_{n,1}-\sigma^2h/2},e^{\sigma\Delta B_{n,2}-\sigma^2h/2}).
\]
For every deterministic initial vector \(X_0\), the mean square \(\mathbb E\|X_n\|_2^2\) converges to zero as \(n\to\infty\) if and only if
\[
\sigma^2<\Gamma_{a,b}(h):=\frac1h\log\!\left(\frac{e^{2ah}-\cosh(2bh)}{\cosh(2bh)-e^{-2ah}}\right),
\]
where the quantifier in the reverse direction is that **all** deterministic initials decay: at or above the threshold there exist nonzero deterministic initials whose mean square does not decay. In fact, for \(\sigma>0\), **every** nonzero deterministic initial has a positive nondecaying limiting Perron component at equality, and exponentially growing mean square above it.

The exact worst-case asymptotic second-moment factor per step is
\[
R(h,\sigma)=\frac{e^{-2ah}}2\left[(v+1)c+\sqrt{(v+1)^2c^2-4v}\right],\qquad v=e^{\sigma^2h},\quad c=\cosh(2bh).
\]
The threshold interpolates between two *different* sharp frontiers:
\[
\lim_{h\downarrow0}\Gamma_{a,b}(h)=2\left(a-\frac{b^2}{a}\right),\qquad
\lim_{h\to\infty}\Gamma_{a,b}(h)=2(a-b).
\]
In particular, if \(2(a-b)<\sigma^2<2(a-b^2/a)\), the semidiscrete stochastic differential equation is exponentially mean-square stable, and its positivity-preserving split discretization is stable for sufficiently small steps but mean-square unstable for sufficiently large steps. At every step size and every realization, the numerical update preserves coordinatewise nonnegativity.

## Assumptions and scope

This is a two-degree-of-freedom semidiscrete heat model with symmetric strictly substochastic negative generator \(-A\), where \(A=\begin{pmatrix}a&-b\\-b&a\end{pmatrix}\), \(0<b<a\). It is compatible, for example, with a symmetric two-interior-node one-dimensional mass-lumped Dirichlet finite-element Laplacian (the uniform mesh yields \(a=2b\)). Each nodal component is driven by its own independent Brownian motion with equal linear multiplicative coefficient. The update first solves exactly the diagonal geometric-Brownian subsystem and then exactly the deterministic heat subsystem. No claim is made for general finite-element meshes, nonlinear noise, stochastic forcing shared across sites, or switched step sizes.

Mean-square asymptotic stability means \(\mathbb E\|X_n\|_2^2\to0\) for every deterministic initial; strict exponential mean-square stability uses a geometric decay rate uniform over initials. At the critical boundary \(R=1\), nonzero mean-square modes persist, so convergence is not asserted. The limit \(h\downarrow0\) is at fixed \(a,b,\sigma\); the limit \(h\to\infty\) is a parameter diagnostic, not a convergence statement for finite-horizon accuracy.

## Proof

Write \(v=\mathbb E[e^{2\sigma\Delta B-\sigma^2h}]=e^{\sigma^2h}\) and \(\mathbb E[e^{\sigma\Delta B-\sigma^2h/2}]=1\). Thus the covariance \(C_n=\mathbb E[X_nX_n^\mathsf T]\) evolves by the exact deterministic linear map
\[
C_{n+1}=S_h\bigl(C_n\circ\begin{pmatrix}v&1\\1&v\end{pmatrix}\bigr)S_h^\mathsf T,
\]
where \(\circ\) is Hadamard multiplication. Set \(u=(C_{11}+C_{22})/2\), \(w=C_{12}\), and \(d=(C_{11}-C_{22})/2\). The symmetric sector obeys
\[
\binom{u_{n+1}}{w_{n+1}}=e^{-2ah}
\begin{pmatrix}v\cosh(2bh)&\sinh(2bh)\\v\sinh(2bh)&\cosh(2bh)\end{pmatrix}
\binom{u_n}{w_n},
\]
while \(d_{n+1}=e^{-2ah}v d_n\). The displayed symmetric matrix is strictly positive. Its characteristic polynomial before the factor \(e^{-2ah}\) is \(\lambda^2-(v+1)c\lambda+v\); its larger eigenvalue therefore gives \(R(h,\sigma)\). Since \(c>1\), the larger root strictly exceeds \(v\); hence the antisymmetric mode is strictly dominated and \(R\) is the full covariance spectral radius.

The positive symmetric matrix is strictly increasing entrywise in \(v\) on its first column. Its Perron root is therefore strictly increasing in \(v\ge1\). At \(v=1\) its Perron root is \(e^{2bh}\), so \(R=e^{-2(a-b)h}<1\). As \(v\to\infty\), the radius diverges. Consequently precisely one \(v_*(h)>1\) makes \(R=1\). Writing \(q=e^{2ah}\), the root equation at \(\lambda=q\) is \(q^2-(v+1)cq+v=0\), hence
\[
v_* =\frac{q(q-c)}{qc-1}>1.
\]
The numerator and denominator are strictly positive as \(q>e^{2bh}>c>1\); \(v_*>1\) also follows from strict monotonicity. Taking its logarithm gives the claimed exact frontier.

For every deterministic initial, \(C_0=X_0X_0^\mathsf T\) is positive semidefinite, and the linear covariance map has spectral radius \(R\). If \(R<1\), its powers converge exponentially to zero. For \(\sigma>0\) and \(X_0\ne0\), the covariance after one step is positive definite: indeed, the expectation of \(D X_0X_0^\mathsf T D\) has determinant \((v^2-1)(X_{0,1}X_{0,2})^2\) when both coordinates are nonzero, and for a one-coordinate initial it initially remains rank one. In the latter case the strictly positive heat matrix makes both coordinates nonzero after one step, and the following independent stochastic step makes the covariance positive definite. For a positive-definite covariance, its symmetric sector satisfies \(u>|w|\). The strictly positive Perron left eigenvector has a strictly positive pairing with this sector (the left eigenvector's \(w\)-to-\(u\) weight is strictly below one when \(v>1\)); thus \(R\ge1\) yields nondecay for any nonzero initial. Alternatively, nondecay for at least one initial already follows by taking \(X_0=(1,1)^\mathsf T\), which gives a strictly positive covariance sector. At \(\sigma=0\), stability follows directly from \(\rho(S_h)=e^{-(a-b)h}<1\).

For the small-step asymptotic, expand \(q=1+2ah+2a^2h^2+O(h^3)\) and \(c=1+2b^2h^2+O(h^4)\) in \(v_*=q(q-c)/(qc-1)\). The quotient is \(1+2(a-b^2/a)h+O(h^2)\); taking \(h^{-1}\log\) proves the first limit. For the large-step limit, \(q\gg c\sim e^{2bh}/2\), so \(v_*\sim q/c\sim2e^{2(a-b)h}\); taking logarithms proves the second limit. The original continuous-time semidiscrete SDE has covariance-sector drift matrix \(\begin{pmatrix}-2a+\sigma^2&2b\\2b&-2a\end{pmatrix}\). Its largest eigenvalue is negative precisely when \(\sigma^2<2(a-b^2/a)\) (trace negative and determinant positive). The gap between this critical noise and the large-step critical noise is \(2b(1-b/a)>0\). Therefore the claimed interval of noise intensities produces stable small steps and unstable large steps.

## Verification

The accompanying standalone `verify.py` computes both the covariance transfer matrix and its closed-form Perron root, checks the exact threshold equation, tests stability on both sides for several positive parameter sets, and confirms the two limiting laws. It passed 185 deterministic comparisons. Finite checks corroborate but do not replace the exact covariance computation and eigenvalue proof.

## Relationship to prior work

Hearder, Le Bris and Djurdjevac (2026, arXiv:2602.16508v1) introduce the positive mass-lumped finite-element Lie–Trotter algorithm, prove positivity and give finite-horizon moment and convergence estimates. Bréhier, Cohen and Ulander (2024) establish positivity and finite-time approximation for a finite-difference splitting scheme for a stochastic heat equation. The present calculation does not claim either discretization or lognormal-moment methods are new. It isolates a sharp *infinite-horizon* mean-square noise/step frontier on the minimal coupled two-site model, together with an explicit interval in which pathwise positivity and continuous mean-square stability coexist with large-step numerical mean-square instability. This precise statement is not implied by a finite-horizon stability bound, a scalar independent-site test equation, an almost-sure exponent, or a first-order finite-time convergence theorem.

## Limitations

The proof requires two symmetric coupled sites, equal and independent multiplicative Gaussian noises, exact matrix exponentials, constant step size and a strictly dissipative generator. The result is not a characterization for arbitrary meshes, larger spatial stencils, correlated noise, nonlinear coefficients, or all positivity-preserving splittings. Mean-square instability is not the same as almost-sure instability. Relevant related literature on long-time stability of *different implicit stochastic-heat discretizations* was identified but not fully read; a specialized, previously published equivalent two-site exact threshold remains a residual bibliographic possibility. Independent validation has not been performed.

## References

1. O. Hearder, C. Le Bris, and A. Djurdjevac, *A Fully Discrete Nonnegativity-Preserving FEM for a Stochastic Heat Equation*, arXiv:2602.16508v1 (first public release 2026-02-18). https://arxiv.org/abs/2602.16508
2. C.-E. Bréhier, D. Cohen, and J. Ulander, *Analysis of a positivity-preserving splitting scheme for some semilinear stochastic heat equations*, 2024. Open full text: https://research.chalmers.se/publication/542281/file/542281_Fulltext.pdf
3. X. Yang, Z. Yang, and C. Zhang, *Stochastic heat equation: numerical positivity and almost surely exponential stability*, Computers & Mathematics with Applications (2022), DOI:10.1016/j.camwa.2022.05.031 (bibliographic/title-and-abstract comparison only).
