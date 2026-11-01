# Two-term near-optimal inradius law for Haar central cross-polytope sections

## Finding
For every **fixed** integer \(d\ge 2\), put \(q=d-1\) and let \(B_1^d=\{x\in\mathbb R^d:\sum_{i=1}^d|x_i|\le1\}\). Choose \(U\) uniformly on the Euclidean unit sphere \(S^{d-1}\). Write \(r_d(U)\) for the intrinsic Euclidean inradius of the central hyperplane section \(B_1^d\cap U^\perp\). Then, as \(\varepsilon\downarrow0\),

\[
\Pr\left\{r_d(U)>q^{-1/2}-\varepsilon\right\}
= C_d\varepsilon^q\bigl(1+K_d\varepsilon+O_d(\varepsilon^2)\bigr),
\]

where the explicit constants are

\[
C_d=\frac{d\,2^q\Gamma(d/2)\,q^{3q/2}}{\pi^{d/2}\,q!},\qquad
K_d=\frac{q^{3/2}(q^2+2q+3)}{2(q+1)}.
\]

In dimension three this states

\[
\Pr\left\{r_3(U)>1/\sqrt2-\varepsilon\right\}
=\frac{24}{\pi}\varepsilon^2\left(1+\frac{11\sqrt2}{3}\varepsilon+O(\varepsilon^2)\right).
\]

The deterministic identity behind the law is

\[
r_d(U)=\left(d-\min_{\sigma\in\{-1,1\}^{d}}(\sigma\cdot U)^2\right)^{-1/2}.
\]

The global maximum \(q^{-1/2}\) was previously available as a general Euclidean-section inradius bound; neither that maximum nor the coordinate-section example is a novelty claim. The contribution here is the explicitly normalized two-term **Haar extreme tail** and its signed-partition interpretation.

## Assumptions and scope
The body is the unit \(\ell_1\)-ball, the section is a through-origin hyperplane, and orientation has normalized Haar surface measure. The inradius is computed using the induced Euclidean metric on the hyperplane; its center is the origin because the section is centrally symmetric. Dimension \(d\) remains fixed while \(\varepsilon\) tends to zero. No uniform-in-dimension error assertion or higher-codimension section theorem is made. The inequality in the probability is strict, but its level-set boundary has Haar measure zero.

## Proof
**1. Exact signed-partition formula.** The radius of the largest centered ball in a symmetric convex section \(E=B_1^d\cap U^\perp\) is

\[
r_d(U)^{-1}=\max_{x\in U^\perp,\ \|x\|_2=1}\|x\|_1.
\]

Since \(\|x\|_1=\max_{\sigma\in\{-1,1\}^d}\sigma\cdot x\), interchange two finite/compact maxima and project each sign vector orthogonally to \(U^\perp\):

\[
r_d(U)^{-1}=\max_\sigma\|\sigma-(\sigma\cdot U)U\|_2
=\sqrt{d-\min_\sigma(\sigma\cdot U)^2}.
\]

Let \(m(U)=\min_\sigma|\sigma\cdot U|\). Averaging \((\sigma\cdot U)^2\) over uniformly random signs gives \(1\), so \(m(U)\le1\). If \(m(U)=1\), every signed sum has absolute value one. As the variance of their squares equals \(4\sum_{i<j}U_i^2U_j^2\), this forces precisely one nonzero coordinate in \(U\). Thus the only maximizing normals are the \(2d\) vectors \(\pm e_i\), and the maximal inradius is \(q^{-1/2}\). This extremal bound is recognized as earlier knowledge, not claimed here.

**2. Reduce rare orientations to axial charts.** Compactness of \(S^{d-1}\) and uniqueness of these maximizers imply that for sufficiently small \(\varepsilon>0\), all the event's orientations belong to disjoint spherical neighborhoods of the \(2d\) axes. Near \(e_1\), write

\[
U=\bigl(\sqrt{1-\|u\|_2^2},u_1,\ldots,u_q\bigr),\qquad u\in\mathbb R^q.
\]

Shrinking the chart so that \(\sum_i|u_i|<\sqrt{1-\|u\|_2^2}\), minimization over signs gives exactly

\[
m(U)=\sqrt{1-\|u\|_2^2}-\sum_{i=1}^{q}|u_i|.
\]

Define

\[
\delta_\varepsilon=1-\sqrt{d-(q^{-1/2}-\varepsilon)^{-2}}.
\]

Since the square root is positive in the range considered, the exceedance event in this chart is precisely

\[
\sum_i|u_i|+1-\sqrt{1-\|u\|_2^2}<\delta_\varepsilon.
\]

A Taylor expansion with fixed \(q\) yields

\[
\delta_\varepsilon=q^{3/2}\varepsilon+\tfrac12q^2(q+3)\varepsilon^2+O_q(\varepsilon^3).
\]

**3. Universal local spherical volume.** The exact surface element in this graph chart is \((1-\|u\|_2^2)^{-1/2}\,du\). For small \(\delta>0\), define

\[
I_q(\delta)=\int_{\sum_i|u_i|+1-\sqrt{1-\|u\|_2^2}<\delta}
\frac{du}{\sqrt{1-\|u\|_2^2}}.
\]

Write \(u_i=\rho t_i\) in each orthant with \(t_i\ge0\) and \(\sum_i t_i=1\). The radial upper limit solves

\[
\rho+\frac{\rho^2}{2}\sum_i t_i^2+O_q(\rho^4)=\delta,
\quad\text{so}\quad
\rho_{\max}=\delta-\tfrac12\delta^2\sum_i t_i^2+O_q(\delta^3),
\]

uniformly on the compact simplex. The spherical Jacobian is \(1+O_q(\rho^2)\), so it produces no relative first-order correction. Under the uniform Dirichlet law on that simplex, \(\mathbb E\sum_i t_i^2=2/(q+1)\). Integrating the radial factor \(\rho^{q-1}\) gives

\[
I_q(\delta)=\frac{2^q\delta^q}{q!}\left(1-\frac{q}{q+1}\delta+O_q(\delta^2)\right).
\]

This computation holds also for \(q=1\), where the simplex reduces to a point.

**4. Normalize and expand.** All axial charts contribute identically. Because the sphere area is \(2\pi^{d/2}/\Gamma(d/2)\),

\[
\Pr\{r_d(U)>q^{-1/2}-\varepsilon\}
=\frac{2d\,I_q(\delta_\varepsilon)}{2\pi^{d/2}/\Gamma(d/2)}.
\]

Substituting the Taylor series and collecting the relative \(\varepsilon\) coefficient gives

\[
\frac{q\,q^2(q+3)}{2q^{3/2}}-\frac{q^{5/2}}{q+1}
=\frac{q^{3/2}(q^2+2q+3)}{2(q+1)},
\]

which proves the stated constants and the \(O_d(\varepsilon^2)\) relative remainder.

## Verification
Standalone `inradius_verifier.py` enumerates all sign choices and compares exact discrepancies against a vectorized calculation for 800,000 random directions each in dimensions two through five. It confirms the analytic extremal bound and tests exact sign evaluation, without purporting to prove an infinite statement. `local_integral_check.py` evaluates the exact local spherical-chart integral by scrambled Sobol sampling and checks the leading and next-order expansions for dimensions two through five at three small deficits each. The analytic proof above, not the numerical samples, establishes the theorem. Run with Python 3, NumPy, and SciPy (dependencies noted in `requirements.txt`).

## Relationship to prior work
Donoho and Tanner (first publicly available 2008-07-23) provide a classical random-polytope framework involving hypercubes and their polar cross-polytope context, but study projected face counts rather than intrinsic Haar section-inradius tails. Szarek and Wolff (2024, Theorem 2.1(ii) and Remark 2.2(b)) establish the universal \(1/\sqrt{k}\) inradius upper bound for \(k\)-dimensional Euclidean sections of \(\ell_1\)-balls, with coordinate-subspace attainment. Hence the present theorem *does not* claim the upper bound itself. The new comparison object is the exact fixed-dimension asymptotic probability of approaching that bound at codimension one, including both coefficients and the sign-partition formula. Related published results on random cross-polytope *section diameter*, random octahedral *projection inradius*, and random cube section combinatorics treat different geometric functionals and do not supply the displayed law.

## Limitations
The result is a fixed-dimensional local tail, not the full inradius distribution, not uniform as dimension grows, and not an assertion about random affine (noncentral) cuts or sections of arbitrary convex bodies. A comprehensive historical-priority determination, particularly against older metric-entropy and integral-geometric literature, is still outstanding; the source inspections and searches made here cannot establish uniqueness of discovery. Independent expert review has not been performed.

## References
1. D. L. Donoho and J. Tanner, *Counting the Faces of Randomly-Projected Hypercubes and Orthants, with Applications*, arXiv:0807.3590, first public version 2008-07-23. https://arxiv.org/abs/0807.3590
2. S. J. Szarek and P. Wolff, *Radii of Euclidean Sections of \(\ell_p\)-Balls*, arXiv:2410.15118, initial preprint 2024, Theorem 2.1(ii) and Remark 2.2(b). https://arxiv.org/abs/2410.15118
