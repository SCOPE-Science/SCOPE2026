# Exact water-filling radii and sharp spherical roundness of Radon mean-section bodies of orthotopes

## Finding

Let \(d\ge3\) and \(Q=\prod_{i=1}^{d}[-\ell_i/2,\ell_i/2]\subset\mathbb R^d\), with every \(\ell_i>0\). Write \(a_i=\prod_{j\ne i}\ell_j\) for the area of either facet perpendicular to the \(i\)-th coordinate axis and put
\[
c_d=\frac{\Gamma((d-1)/2)}{\sqrt\pi\,\Gamma(d/2)}.
\]
Use the probability-normalized Grassmannian Radon mean-section operator \(\overline M_{d-1}\) specified below, and put \(L=\overline M_{d-1}Q\). Then
\[
h_L(u)=c_d\sum_{i=1}^{d}a_i\sqrt{1-u_i^2},\qquad u\in S^{d-1}.
\]
Let \(r(L)\) and \(R(L)\) be the radii of the largest Euclidean ball contained in \(L\) and the smallest Euclidean ball containing \(L\), respectively. They are attained with center at the origin. The exact inradius is
\[
r(L)=c_d\biggl(\sum_i a_i-\max_i a_i\biggr).
\]
There is one and only one \(\lambda>\min_i a_i\) satisfying
\[
\sum_{i=1}^{d}\left(1-\frac{a_i^2}{\lambda^2}\right)_+=1.
\]
For this \(\lambda\), the exact circumradius and **all** maximizing unit normals are given by
\[
R(L)=c_d\biggl(\sum_{a_i<\lambda}\frac{a_i^2}{\lambda}+\sum_{a_i\ge\lambda}a_i\biggr),
\qquad u_i^2=\left(1-\frac{a_i^2}{\lambda^2}\right)_+.
\]
Each nonzero coordinate of a maximizing normal admits either sign, independently. The radius ratio satisfies the **sharp rigidity inequality**
\[
\boxed{\frac{R(L)}{r(L)}\ge\sqrt{\frac{d}{d-1}},}
\]
with equality **if and only if \(Q\) is a cube**. More quantitatively, if \(\theta=\max_i a_i/\sum_i a_i\), then
\[
\frac{R(L)}{r(L)}\ge\sqrt{\frac{d}{d-1}}\frac{d-1}{d(1-\theta)}.
\]
In dimension three, sorting \(A\ge B\ge C>0\) among the three facet areas produces a genuine two-phase exact formula:
\[
\frac{R(L)}{c_3}=\begin{cases}
\sqrt{2(A^2+B^2+C^2)},&A^2\le B^2+C^2,\\
A+\sqrt{B^2+C^2},&A^2\ge B^2+C^2.
\end{cases}
\]
The branches agree to first order at the transition; for fixed \(B,C\), the second derivative with respect to \(A\) drops from \(1/(2\sqrt{B^2+C^2})\) to zero as the transition is crossed.

## Assumptions and scope

All statements concern Euclidean dimensions \(d\ge3\) and strictly positive finite side lengths. For a unit vector \(u\), define the Radon mean-section body's support function by
\[
h_{\overline M_{d-1}Q}(u)=\int_{\substack{H\in\mathrm{Gr}_{d-1,d}\\\mathrm{span}(u)\subset H}}\operatorname{vol}_{d-1}(Q\mid H)\,d\nu_u(H),
\]
where \(\nu_u\) is the unique rotation-invariant probability measure on the hyperplanes \(H\) containing \(\mathrm{span}(u)\), and \(Q\mid H\) means **orthogonal projection**, not intersection. This is the normalization of Brauner–Ortega-Moreno–Schuster (2026, Eq. 1.1); it is related to the even part of older mean-section operators up to constants, not identical to every convention in that older literature.

The radius assertions refer to Euclidean balls with **arbitrary allowed centers**, not just origin-centered balls. For an origin-symmetric convex body, averaging the centers of any inscribed or enclosing ball with its negative yields an origin-centered ball of the same radius, so this causes no loss.

## Proof

**1. Support function and normalization.** For any unit normal \(v\), Cauchy's brightness formula applied to the \(2d\) facets of \(Q\) gives
\[
\operatorname{vol}_{d-1}(Q\mid v^\perp)=\sum_{i=1}^d a_i|v_i|.
\]
For fixed \(u\), a Haar-random hyperplane through \(u\) has normal \(v\) uniformly distributed on the sphere of the \((d-1)\)-dimensional space \(u^\perp\). The orthogonal projection of \(e_i\) into that space has length \(\sqrt{1-u_i^2}\). For \(v\) uniformly distributed on \(S^{d-2}\) in that space, the elementary beta-integral identity is
\[
\mathbb E|v\cdot w|=\frac{\Gamma((d-1)/2)}{\sqrt\pi\,\Gamma(d/2)}\|w\|=c_d\|w\|.
\]
Linearity yields the stated support function. Each summand is the support function of \(a_ic_d(B_2^d\cap e_i^\perp)\), hence \(L\) is their Minkowski sum; in three dimensions this is a weighted orthogonal three-disc **discotope**, a body type already studied in earlier literature.

**2. Inradius.** Put \(t_i=u_i^2\). Then \(t\) ranges over the complete standard simplex \(\{t_i\ge0,\sum_i t_i=1\}\), and
\[
\frac{h_L(u)}{c_d}=f(t):=\sum_i a_i\sqrt{1-t_i}.
\]
Each term is concave in \(t_i\), so \(f\) is concave on the simplex. Writing any \(t\) as a convex combination of the simplex vertices, concavity gives \(f(t)\ge\min_j f(e_j)\). But \(f(e_j)=\sum_{i\ne j}a_i\); the least value occurs at a coordinate with maximal \(a_j\). The origin-centered inradius of any symmetric convex body is its minimum support value. The assertion follows.

**3. Circumradius and complete contact classification.** Because \(a_i>0\), the function \(f\) is strictly concave on the simplex; therefore its maximizing \(t\) is unique. At any positive \(t_i\), the Lagrange multiplier equation reads \(a_i/\sqrt{1-t_i}=\lambda\); for a vanishing \(t_i\), the complementary inequality is \(a_i\ge\lambda\). Thus every positive coordinate obeys \(t_i=1-a_i^2/\lambda^2\), the others vanish, and the simplex constraint is precisely the stated equation for \(\lambda\). Its left side is continuous, strictly increasing once \(\lambda>\min_i a_i\), tends to \(0\) as \(\lambda\downarrow\min_i a_i\), and tends to \(d>1\) as \(\lambda\to\infty\). Hence the solution is unique. Substitution in \(f\) gives the exact circumradius and all maximizing normals. In each phase, with active set \(I=\{i:a_i<\lambda\}\) of size \(m\ge2\), one may equivalently write
\[
\lambda^2=\frac{\sum_{i\in I}a_i^2}{m-1},
\]
subject to the checked inequalities \(a_i<\lambda\) for \(i\in I\), \(a_i\ge\lambda\) otherwise. This is a finite, exhaustive active-set formula in every dimension.

**4. Sharp roundness and rigidity.** Let \(S=\sum_i a_i\) and \(A=\max_i a_i\). At a body-diagonal direction \(u=(1,\ldots,1)/\sqrt d\), the support value equals \(c_d\sqrt{(d-1)/d}\,S\). Consequently
\[
\frac Rr\ge\sqrt{\frac{d-1}{d}}\frac{S}{S-A}
=\sqrt{\frac d{d-1}}\frac{d-1}{d(1-A/S)}.
\]
Since \(A/S\ge1/d\), this proves the two claimed inequalities. If equality holds in the uniform lower bound, then \(A/S=1/d\), so all \(a_i\) agree. Since \(a_i=(\prod_j\ell_j)/\ell_i\), all \(\ell_i\) must agree. Conversely, for a cube all \(a_i=a\); the strict-concavity maximum occurs at \(t_i=1/d\), with \(r=c_d(d-1)a\) and \(R=c_d\sqrt{d(d-1)}a\), proving sharpness.

**5. The three-dimensional transition.** If all three weights are active, the multiplier satisfies \(\lambda^2=(A^2+B^2+C^2)/2\); this phase is feasible exactly when \(A^2\le B^2+C^2\), and the maximum is \(\sqrt{2(A^2+B^2+C^2)}\). Otherwise only \(B,C\) are active, giving \(\lambda=\sqrt{B^2+C^2}\) and maximum \(A+\sqrt{B^2+C^2}\). Direct differentiation at \(A=\sqrt{B^2+C^2}\) gives the stated first-derivative agreement and the second-derivative jump.

## Verification

The accompanying `verify_mean_body.py` contains independently parameterized numerical checks of the beta-integral projection averaging, 500 constrained nonlinear maximizations in dimensions 3, 4, 5 and 8, 1,500 sampled direction/finite quadrature comparisons, the exact cube equality cases, and both sides of the three-dimensional phase boundary. Executing it with NumPy and SciPy printed:

`PASS: 500 independent constrained optimizations, 1500 random-direction/quadrature comparisons, equality and phase-boundary tests`

These finite diagnostics only test the implementation and formulas; they do not establish the universal claims, which follow from the preceding analytic proof.

## Relationship to prior work

Brauner, Ortega-Moreno, and Schuster (2026) supply the Radon-of-projection definition and prove general Aleksandrov–Fenchel inequalities for its intrinsic volumes. Their main results do not identify the all-dimensional Euclidean inradius, circumradius, maximizing-normal phases, or sharp orthotope roundness ratio evaluated here. Goodey, Kiderlen, and Weil (1998) study general section and projection mean operators under related but sometimes differently normalized conventions.

The Minkowski-sum-of-discs representation itself **is not new**: Gesmundo and Meroni (2021/2022) and Mathis and Meroni (2022/2023) explicitly analyze the three-dimensional sum of three mutually perpendicular discs, known as the *dice*. The claimed contribution is instead the exact **all-dimensional weighted-radius active-set classification** and **sharp cube-only Euclidean roundness extremality** for these specifically normalized Radon mean-section bodies. The cited prior studies focus on semialgebraic boundaries and fiber bodies, not the stated radius or extremal formulas. Similar-looking work on the convex **hull** of orthogonal discs concerns a different operation and does not imply these results.

## Limitations

This theorem concerns the normalized Radon mean-section body of positive rectangular boxes; it is not a statement about their actual central section shapes. It does not claim a similar sharp inequality for arbitrary convex bodies, rotated disc systems, arbitrary discotopes, or general mixed intrinsic volumes. The exact weighted three-dimensional dice as an object predates this calculation. Historical originality remains provisional because other classical convex-geometry sources may contain equivalent support-function optimizations. No independent mathematical audit has been performed.

## References

1. L. Brauner, O. Ortega-Moreno and F. E. Schuster, *Radon Transforms of Projection Functions and Aleksandrov–Fenchel Inequalities*, arXiv:2610.18268 (first public version, 13 October 2026), especially Eq. (1.1), Theorems 1–2. https://arxiv.org/abs/2610.18268
2. F. Gesmundo and C. Meroni, *The Geometry of Discotopes*, arXiv:2111.01241 (2021), *Le Matematiche* 77 (2022), 143–171, especially Sections 2 and 7. https://arxiv.org/abs/2111.01241
3. L. Mathis and C. Meroni, *Fiber Convex Bodies*, *Discrete & Computational Geometry* 70 (2023), 1451–1475, Sections 5.2–5.3. https://doi.org/10.1007/s00454-022-00451-3
4. P. Goodey, M. Kiderlen and W. Weil, *Section and Projection Means of Convex Bodies*, *Monatshefte für Mathematik* 126 (1998), 37–54. https://doi.org/10.1007/BF01312454
