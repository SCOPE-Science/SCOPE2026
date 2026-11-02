# Three-regime cooperative-binding thresholds for remote fractional Dirichlet impurities

## Finding

Let \(L\) be the Dirichlet discrete Laplacian on \(\ell^2(\mathbb N)\), \((Lf)_n=2f_n-f_{n-1}-f_{n+1}\), with \(f_0=0\). Fix \(0<\alpha<3/2\), \(k\geq2\), distinct real positions \(0<x_1<\cdots<x_k\), and positive strengths \(w_1,\ldots,w_k\). For all sufficiently large positive integers \(R\), set \(m_i(R)=\lfloor Rx_i\rfloor\) and
\[
V_R=\sum_{i=1}^k w_i\langle e_{m_i(R)},\cdot\rangle e_{m_i(R)},\qquad
c_R=\sup\{c\geq0:L^\alpha-cV_R\geq0\}.
\]
All operator inequalities are quadratic-form inequalities on \(\ell^2(\mathbb N)\). Write \(W=\operatorname{diag}(w_1,\ldots,w_k)\). Define the finite Green matrix
\[
G_R(i,j)=\frac2\pi\int_0^\pi
\frac{\sin(m_i(R)\theta)\sin(m_j(R)\theta)}{(2-2\cos\theta)^\alpha}\,d\theta.
\]
Then \(c_R=\lambda_{\max}(W^{1/2}G_RW^{1/2})^{-1}\) exactly. The following three limits are sharp:

**(i) Short-range regime, \(0<\alpha<1/2\):**
\[
\lim_{R\to\infty}c_R=
\frac1{C_\alpha\max_iw_i},\qquad
C_\alpha=\frac{4^{-\alpha}}\pi B(1/2-\alpha,1/2).
\]
Here \(G_R\to C_\alpha I_k\) entrywise.

**(ii) Logarithmic borderline, \(\alpha=1/2\):**
\[
\lim_{R\to\infty}(\log R)c_R=\frac{\pi}{\max_iw_i},
\qquad \frac{G_R}{\log R}\longrightarrow\frac1\pi I_k.
\]
More precisely, whenever \(i\ne j\),
\[
\lim_{R\to\infty}G_R(i,j)=
\frac1\pi\log\frac{x_i+x_j}{|x_i-x_j|},
\qquad G_R(i,i)=\frac{\log R}\pi+O(1).
\]

**(iii) Collective regime, \(1/2<\alpha<3/2\):** put \(\beta=2\alpha-1\in(0,2)\) and
\[
K_\alpha(x,y)=\frac{(x+y)^\beta-|x-y|^\beta}
{2\Gamma(1+\beta)\sin(\pi\beta/2)}.
\]
Then \(R^{1-2\alpha}G_R(i,j)\to K_\alpha(x_i,x_j)\), with strictly positive-definite limit matrix, and
\[
\boxed{\displaystyle
\lim_{R\to\infty}R^{2\alpha-1}c_R=
\frac1{\lambda_{\max}\bigl(W^{1/2}[K_\alpha(x_i,x_j)]_{i,j=1}^kW^{1/2}\bigr)}.}
\]
Every off-diagonal entry of this limit matrix is strictly positive. Hence its largest eigenvalue is *strictly larger* than its largest diagonal entry when \(k\ge2\): the joint binding threshold is strictly below the best separate-impurity threshold at leading order.

For two sites, let \(t_1,t_2>0\) and choose individual couplings \(t_iR^{1-2\alpha}\). If \(t_iK_\alpha(x_i,x_i)<1\) for each \(i\) and
\[
\bigl(1-t_1K_\alpha(x_1,x_1)\bigr)
\bigl(1-t_2K_\alpha(x_2,x_2)\bigr)
<t_1t_2K_\alpha(x_1,x_2)^2,
\]
then, for every sufficiently large \(R\), *neither isolated impurity binds* but the *combined pair has a negative eigenvalue*. Such choices of positive \(t_1,t_2\) exist for every \(1/2<\alpha<3/2\) and any two distinct positive positions. Conversely, reversing this strict inequality preserves nonnegativity of the combined pair for all sufficiently large \(R\), provided each individual diagonal inequality remains strict.

## Assumptions and scope

The power \(L^\alpha\) is defined by the functional calculus of the **Dirichlet half-line Jacobi matrix** \(L\). This is not the same as first taking a full-line fractional Laplacian and then compressing to the half-line. The \(x_i\) and \(w_i\) are fixed as \(R\to\infty\); \(k\) is fixed and finite. The source model uses complex \(\ell^2\), but the self-adjoint Green matrices are real symmetric. The condition \(\alpha<3/2\) ensures finiteness of every zero-energy Green entry, and \(\alpha>0\) makes \(L^\alpha\) well defined as a bounded nonnegative operator. The floor operation does not alter the limits because \(m_i(R)/R\to x_i\).

## Proof

**Step 1: Exact finite-rank reduction.** The unitary sine transform maps \(L\) to multiplication by \(2-2\cos\theta\) on \(L^2((0,\pi),d\theta)\), with transformed basis vector \(e_m\) equal to \(\sqrt{2/\pi}\sin(m\theta)\). Thus
\[
G_R(i,j)=\langle L^{-\alpha/2}e_{m_i},L^{-\alpha/2}e_{m_j}\rangle.
\]
For fixed \(m,n\), integrability near zero follows from \(\sin(m\theta)\sin(n\theta)=O(\theta^2)\), so \(\alpha<3/2\) suffices. The map \(A_R:\mathbb C^k\to\ell^2\), \(A_Rz=\sum_i\sqrt{w_i}z_i L^{-\alpha/2}e_{m_i}\), is bounded, and \(A_R^*A_R=W^{1/2}G_RW^{1/2}\). In quadratic-form sense,
\[
L^\alpha-cV_R=L^{\alpha/2}(I-cA_RA_R^*)L^{\alpha/2}.
\]
The range of \(L^{\alpha/2}\) is dense because \(L\) is injective. Positivity therefore holds precisely for \(c\|A_R\|^2\le1\). This proves the exact formula for \(c_R\). For \(c>c_R\), a negative quadratic-form witness exists, and the compact perturbation of \(L^\alpha\), whose essential spectrum begins at zero, has a negative eigenvalue.

**Step 2: \(0<\alpha<1/2\).** Write
\[
G_R(i,j)=\frac1\pi\int_0^\pi\frac{\cos((m_i-m_j)\theta)-\cos((m_i+m_j)\theta)}{(2-2\cos\theta)^\alpha}\,d\theta.
\]
The denominator's negative power is integrable exactly when \(\alpha<1/2\). Because the \(x_i\) are positive and distinct, the Riemann–Lebesgue lemma kills both cosine terms off diagonal, and kills the oscillatory cosine on diagonal. The remaining diagonal integral is
\[
\frac1\pi\int_0^\pi(2-2\cos\theta)^{-\alpha}d\theta
=\frac{4^{-\alpha}}\pi B(1/2-\alpha,1/2).
\]
Finite-dimensional spectral continuity gives the stated coupling limit.

**Step 3: \(\alpha=1/2\).** Near \(\theta=0\), \((2-2\cos\theta)^{-1/2}=\theta^{-1}+h(\theta)\), where \(h\in L^1(0,\pi)\). The diagonal singular term obeys
\[
\int_0^\pi\frac{1-\cos(2m\theta)}\theta\,d\theta
=\log m+O(1),
\]
while all off-diagonal oscillations of \(h\) vanish by the Riemann–Lebesgue lemma. For \(i\ne j\), the singular terms have the finite limit
\[
\lim_{R\to\infty}\int_0^\pi
\frac{\cos((m_i-m_j)\theta)-\cos((m_i+m_j)\theta)}\theta\,d\theta
=\log\frac{x_i+x_j}{|x_i-x_j|}.
\]
This follows from \(\int_0^\infty(\cos(au)-\cos(bu))du/u=\log(b/a)\) for \(a,b>0\), or from the cosine integral and the fact that both frequencies diverge. Dividing by \(\log R\) and using spectral continuity yields the borderline limit.

**Step 4: \(1/2<\alpha<3/2\).** Substitute \(u=R\theta\) in the Green integral. The rescaled integrand is
\[
R^{1-2\alpha}G_R(i,j)=\frac2\pi\int_0^{\pi R}
\frac{\sin((m_i/R)u)\sin((m_j/R)u)}
{\bigl[R^2(2-2\cos(u/R))\bigr]^\alpha}\,du.
\]
For \(0<u<\pi R\), the denominator is bounded below by a positive constant times \(u^{2\alpha}\); for fixed positions the numerator is bounded by \(C\min\{u^2,1\}\). This is integrable on \((0,\infty)\) exactly in the stated interval. Dominated convergence therefore gives
\[
\frac2\pi\int_0^\infty\frac{\sin(x_i u)\sin(x_j u)}{u^{2\alpha}}du.
\]
Writing \(\beta=2\alpha-1\) and using the standard elementary cosine-difference integral
\[
\int_0^\infty\frac{1-\cos(tu)}{u^{1+\beta}}\,du
=\frac{\pi t^\beta}{2\Gamma(1+\beta)\sin(\pi\beta/2)},
\quad 0<\beta<2,
\]
gives exactly \(K_\alpha(x_i,x_j)\). Its integral Gram representation proves positive definiteness: a linear combination of \(\sin(x_i u)\) that vanishes almost everywhere must have all coefficients zero because the frequencies \(x_i\) are distinct and positive. Its explicit closed form proves strictly positive off-diagonal entries. Spectral continuity gives the claimed coupling constant.

**Step 5: Strict collective binding.** For \(k\ge2\), any principal two-by-two submatrix of the positive-entry matrix \(W^{1/2}KW^{1/2}\) has largest eigenvalue strictly above either diagonal entry. The full matrix has largest eigenvalue at least that of the submatrix, so its largest eigenvalue strictly exceeds the largest diagonal entry (choose a pair including an index of maximal diagonal entry). For two impurities, the limiting Birman–Schwinger matrix with individual rescaled strengths \(t_1,t_2\) has diagonal \(t_iK_{ii}\) and off-diagonal \(\sqrt{t_1t_2}K_{12}\). Under two strict diagonal bounds, it has an eigenvalue above one exactly when \((1-t_1K_{11})(1-t_2K_{22})<t_1t_2K_{12}^2\). A strict spectral gap persists for all sufficiently large \(R\). To exhibit admissible pairs, write \(\rho=K_{12}/\sqrt{K_{11}K_{22}}\in(0,1)\) and choose \(t_i=s/K_{ii}\) with \((1+\rho)^{-1}<s<1\); the limiting matrix has eigenvalues \(s(1\pm\rho)\). This proves the claimed cooperative-binding window and completes the proof.

## Verification

The accompanying standalone program `CHECKER.py` evaluates finite Green matrices using exact gamma/digamma identities for the sine integral, tests independent quadrature cases and the three rescaling laws, checks the exact \(\alpha=1\) Dirichlet Green kernel, verifies two-site coupling inequalities and reproduces a cooperative-binding example. It requires Python 3, `mpmath`, and `numpy`. Run `python CHECKER.py` from the directory containing this document. The program checks finite cases only; the preceding integral arguments prove all asymptotic and universal assertions.

## Relationship to prior work

Gerhat, Krejčiřík and Štampach (2023, arXiv:2307.09919) prove subcriticality of \(L^\alpha\) exactly for \(0<\alpha<3/2\), derive the sine Green integral, and analyze localized perturbations (including a critical bilaplacian regime). Their general Green bounds and Hardy estimates supply the starting framework. The present claim does **not** present the individual-site threshold, the source sine transform, or the Birman–Schwinger principle as new. Rather, it determines the exact **joint** leading coupling threshold for any fixed number of sites moving apart proportionally to their distance from the boundary, exhibits the \(\alpha=1/2\) interaction transition with an explicit logarithmic off-diagonal limit, and gives a sharp cooperative-binding criterion valid throughout \(1/2<\alpha<3/2\).

The continuum expression is an odd-sine fractional Green/covariance kernel. Standard Fourier analysis implies its general form, but its appearance as the sharp joint binding threshold of these discrete operators requires the rescaled Green-matrix and finite-rank spectral limits. Other fractional Laplacian boundary constructions, especially compression of the full-line fractional power, are not assumed equivalent. Related literature on continuum point interactions, threshold resolvents and Hardy weights addresses overlapping methods or objects; priority for an equivalent unlocated formulation cannot be excluded.

## Limitations

The result concerns finite fixed \(k\), positive fixed weights, distinct positive macroscopic positions and spectral powers of the half-line Dirichlet discrete Laplacian. It neither determines the full spectrum or negative eigenvalue energies nor establishes a uniform joint limit as \(k\) increases. At exact limiting critical equality the leading asymptotics do not determine the sign of the finite-\(R\) perturbation. The global critical range \(\alpha\ge3/2\) is outside the theorem. Historical priority for equivalent formulations remains provisional.

## References

1. B. Gerhat, D. Krejčiřík and F. Štampach, *Criticality transition for positive powers of the discrete Laplacian on the half line*, arXiv:2307.09919 (initial public version July 19, 2023). https://arxiv.org/abs/2307.09919
2. F. Štampach and J. Waclawek, *Optimal fractional discrete Hardy inequalities on the half-line*, arXiv:2608.26936 (2026). Different half-line fractional realization; used for construction comparison. https://arxiv.org/abs/2608.26936
3. M. Reed and B. Simon, *Methods of Modern Mathematical Physics, IV: Analysis of Operators*, Academic Press (1978), standard Birman–Schwinger principle and compact perturbation framework.
