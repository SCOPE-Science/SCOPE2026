# Sharp random-mesh positivity step and an adjacent-spacing extreme-value law

## Finding

Let \(n\ge2\). Sort \(n-1\) independent uniform points in \((0,1)\), append endpoints \(0,1\), and write the \(n\) positive cell lengths as \(H_0,\ldots,H_{n-1}\). Discretize the one-dimensional homogeneous Dirichlet heat equation using continuous piecewise-affine finite elements, nodal mass lumping, and unmodified forward Euler. Let \(\tau_n^*\) be the largest step for which **every nonnegative interior nodal state** is mapped to a nonnegative state in one step. Then, pathwise,

\[
\tau_n^*=\frac12\min_{0\le i\le n-2}H_iH_{i+1}.
\]

Under the random-node model, the sharp weak limit is

\[
2n^3\log n\,\tau_n^*\ \Rightarrow\ \operatorname{Exp}(1)
\qquad(n\to\infty).
\]

For every fixed \(n\ge2\) and \(q>0\), the inverse threshold has the exact integrability classification

\[
\mathbb E[(\tau_n^*)^{-q}]<\infty\quad\Longleftrightarrow\quad 0<q<1.
\]

For comparison, the equally spaced \(n\)-cell mesh has \(\tau_n^*=1/(2n^2)\). The random mesh has a typical positivity step of order \(1/(n^3\log n)\), much smaller than the uniform-mesh order; its reciprocal has infinite mean for every finite \(n\).

## Assumptions and scope

The heat problem is \(\partial_tu=\partial_{xx}u\) on \((0,1)\), with zero Dirichlet data, and \(n\ge2\) cells. The random mesh is specifically the ordered sample of \(n-1\) *independent* \(\operatorname{Uniform}(0,1)\) interior points. The finite-element method uses continuous \(P_1\) hat functions, exact stiffness integrals, lumped mass obtained by summing each row of the exact mass matrix, and exact-arithmetic forward Euler of the homogeneous semidiscrete equation. The mesh is frozen in time. Positivity means entrywise preservation of the cone of all nonnegative vectors, not merely positivity for a chosen initial condition. It is not the spectral stability limit, and it does not impose a uniform mesh regularity bound.

## Proof

**Step 1: sharp deterministic positivity criterion.** Let \(x_0=0<x_1<\cdots<x_{n-1}<x_n=1\) and \(H_i=x_{i+1}-x_i\). Number interior nodes \(j=1,\ldots,n-1\). The lumped mass is diagonal, and stiffness is tridiagonal, with

\[
M_{jj}=\frac{H_{j-1}+H_j}{2},\qquad
K_{jj}=\frac1{H_{j-1}}+\frac1{H_j},\qquad
K_{j,j+1}=-\frac1{H_j}.
\]

The remaining off-diagonal stiffness entries are zero except their symmetric companions. A forward Euler step has matrix \(P_\tau=I-\tau M^{-1}K\). Its off-diagonal entries are nonnegative for every \(\tau\ge0\). Its \(j\)-th diagonal entry is nonnegative precisely if

\[
\tau\le\frac{M_{jj}}{K_{jj}}=\frac{H_{j-1}H_j}{2}.
\]

A matrix preserves every nonnegative vector if and only if all its entries are nonnegative (test the coordinate unit vectors for necessity). This proves the asserted pathwise cutoff, including equality and the case \(n=2\). Below the cutoff each row sum lies in \([0,1]\) because the stiffness row sums are nonnegative after imposing zero boundary data; hence the step also satisfies the discrete maximum bound. At any strictly larger step one diagonal becomes negative, giving an explicit nonnegative coordinate-unit initial state whose next iterate has a negative component.

**Step 2: exact spacing representation.** If \(E_0,\ldots,E_{n-1}\) are independent unit-rate exponential random variables and \(S_n=\sum_{i=0}^{n-1}E_i\), the gap vector has the Dirichlet\((1,\ldots,1)\) law and admits the representation \(H_i=E_i/S_n\). Therefore

\[
\tau_n^*=\frac{Z_n}{2S_n^2},\qquad
Z_n:=\min_{0\le i\le n-2}E_iE_{i+1}.
\]

**Step 3: the adjacent-product extreme.** For independent unit exponentials \(X,Y\), let \(p(t)=\Pr(XY<t)\). Conditioning on \(X\) gives

\[
p(t)=\int_0^\infty e^{-x}(1-e^{-t/x})\,dx
=t\log(1/t)+O(t)\quad(t\downarrow0).
\]

The stated remainder follows by splitting the integral over \((0,t)\), \([t,1]\), and \((1,\infty)\); on the middle interval use \(1-e^{-t/x}=t/x+O(t^2/x^2)\), and \(e^{-x}=1+O(x)\). For three independent exponentials, the probability of two neighboring products both being small is

\[
\begin{aligned}
&\Pr(X_1X_2<t,\ X_2X_3<t)\\
&=\int_0^\infty e^{-y}(1-e^{-t/y})^2\,dy\le 2t,
\end{aligned}
\]

since the integrals over \((0,t)\) and \([t,\infty)\) are bounded by \(t\) and \(t^2\int_t^\infty y^{-2}dy=t\). Products with index separation at least two are independent.

Fix \(z>0\) and put \(t_n=z/(n\log n)\), so \(p(t_n)\sim z/n\). Write \(A_i=\{E_iE_{i+1}<t_n\}\). Choose an integer block length \(b_n=\lfloor\sqrt{\log n}\rfloor\), group the event indices into blocks of \(b_n\) consecutive indices and omit one index between blocks. The groups depend on disjoint sets of exponentials and are therefore independent. For any one block, Bonferroni's inequalities imply

\[
\Pr\left(\bigcup_{i\ \mathrm{in\ block}}A_i\right)
=b_n p(t_n)+O\bigl(b_n^2p(t_n)^2+b_n t_n\bigr).
\]

Here adjacent pairs contribute at most \(2t_n\) and nonadjacent pairs contribute \(p(t_n)^2\). There are asymptotically \(n/b_n\) blocks, so their total approximation error is \(O(nb_np(t_n)^2+nt_n)=o(1)\), and the probability of any omitted event is \(O(np(t_n)/b_n+b_np(t_n))=o(1)\). Independence of the retained blocks now yields

\[
\Pr(Z_n>z/(n\log n))\longrightarrow e^{-z}.
\]

Therefore \(n\log n\,Z_n\Rightarrow\operatorname{Exp}(1)\). By the strong law \(S_n/n\to1\) almost surely. Substitution into the representation in Step 2 and Slutsky's theorem give the asserted limit with constant exactly \(2\).

**Step 4: inverse-moment threshold.** For \(0<q<1\) and any adjacent pair of Dirichlet gaps, beta-integral evaluation gives

\[
\mathbb E[(H_iH_{i+1})^{-q}]
=\frac{\Gamma(n)\Gamma(1-q)^2}{\Gamma(n-2q)}<\infty.
\]

Since the maximum of finitely many nonnegative quantities is at most their sum,
\( (\tau_n^*)^{-q}=2^q\max_i(H_iH_{i+1})^{-q}\) is integrable. When \(q\ge1\), a single Dirichlet gap has a nonintegrable reciprocal \(q\)-moment; because \(H_{i+1}\le1\), \((H_iH_{i+1})^{-q}\ge H_i^{-q}\), and so the reciprocal threshold has infinite \(q\)-moment. This proves the sharp classification.

## Verification

The accompanying standalone Python verifier uses exact rational arithmetic to assemble the \(P_\tau\) matrix on 200 deterministic positive meshes with \(2\) through \(9\) cells. Across 800 matrix/step tests it checks that entrywise nonnegativity is equivalent to \(\tau\le\tfrac12\min_iH_iH_{i+1}\), including equality and just-above-threshold witnesses; it also checks row sums in the positive regime. Seeded Monte Carlo calculations at three mesh sizes check the scale \(n\log n\min_iE_iE_{i+1}\) as a diagnostic, **not** as proof of convergence or of a finite-sample exponential law. Run with `python3 verify.py`; Python's standard library suffices.

## Relationship to prior work

Abdulle and Garegnani (2021) propose random perturbations of finite-element meshes to quantify error for elliptic problems; their analyzed perturbation construction is different from an unrestricted uniform-order-statistic mesh, and their paper does not derive this parabolic explicit-step extreme-value law. Li, Yang and Zhou (2020) develop mass-lumped maximum-principle methods using exponential integration and cut-off; this does not give the positivity threshold distribution for the **unmodified** forward Euler method on independent random knots. Chatzipantelidis, Horváth and Thomée (2015) analyze classical heat-equation finite-element positivity. The deterministic local sign criterion is elementary and is **not** asserted to be a new positivity principle; the claim of added content is its exact combination with the one-dependent adjacent-product extreme, the \(n^3\log n\) distributional scale, and the reciprocal-moment cutoff in this specified random-mesh model.

## Limitations

The random knots are independent uniform points, which create highly non-quasi-uniform meshes. Results do **not** transfer directly to bounded shape-regular mesh perturbations, graded deterministic meshes, random physical coefficients, resampled time-dependent grids, non-lumped mass matrices, higher dimensions or higher-order time integrators. The exponential law is asymptotic and may converge slowly due to logarithmic corrections; no finite-\(n\) exponential distribution or spectral-stability threshold is claimed. The proof uses real exact arithmetic and does not control rounding or conditioning. The classical positivity literature may contain stronger statements about the **deterministic** step bound; publication-priority assessment of the new random-mesh limit is not independent.

## References

1. A. Abdulle and G. Garegnani, *A probabilistic finite element method based on random meshes: Error estimators and Bayesian inverse problems* (2021), arXiv:2103.06204, first public 2021-03-10, https://arxiv.org/abs/2103.06204.
2. B. Li, J. Yang and Z. Zhou, *Arbitrarily high-order exponential cut-off methods for preserving maximum principle of parabolic equations* (2020), arXiv:2010.08789, https://arxiv.org/abs/2010.08789.
3. P. Chatzipantelidis, Z. Horváth and V. Thomée, *On Preservation of Positivity in Some Finite Element Methods for the Heat Equation*, Comput. Methods Appl. Math. **15** (2015), 417–437, doi:10.1515/cmam-2015-0018.
