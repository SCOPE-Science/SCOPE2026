# Antipodal isotropic spherical means: a sharp bound and cube–cross-polytope duality

## Finding
Let \(d\ge2\) and let \(\mu\) be an antipodally symmetric Borel probability on the unit sphere \(S^{d-1}\subset\mathbb R^d\), with the isotropy normalization \(\int vv^\top\,d\mu(v)=I_d/d\). For \(x\in S^{d-1}\), set
\[
 F_\mu(x)=\int_{S^{d-1}}\arccos(\langle x,v\rangle)^2\,d\mu(v),
 \qquad B_d=\frac{\pi^2}{4}+\arcsin^2\!\left(\frac1{\sqrt d}\right).
\]
Then the universal inequality and fourth-moment stability refinement are
\[
 F_\mu(x)\ge B_d+\frac13\left[\int_{S^{d-1}}\langle x,v\rangle^4\,d\mu(v)-\frac1{d^2}\right]\ge B_d.
\]
Equality \(F_\mu(x)=B_d\) holds precisely when \(|\langle x,v\rangle|=1/\sqrt d\) for \(\mu\)-almost every \(v\). Thus equality is an exact equiangular-incidence condition on the direction \(x\).

Let \(\mu_C\) be uniform on the \(2^d\) normalized cube vertices \(C_d=\{(\varepsilon_1,\ldots,\varepsilon_d)/\sqrt d:\varepsilon_i\in\{-1,1\}\}\); let \(\mu_X\) be uniform on the \(2d\) cross-polytope vertices \(X_d=\{\pm e_i:1\le i\le d\}\). Both are antipodal isotropic measures. Their **complete** global minimizer sets and minimum values are
\[
 \operatorname*{argmin}_{x\in S^{d-1}}F_{\mu_C}(x)=X_d,\qquad
 \operatorname*{argmin}_{x\in S^{d-1}}F_{\mu_X}(x)=C_d,
\]
\[
 \min_xF_{\mu_C}(x)=\min_xF_{\mu_X}(x)=B_d.
\]
There are no exceptional dimensions or additional minimizers. Quantitatively, for every \(x\in S^{d-1}\),
\[
 F_{\mu_C}(x)-B_d\ge\frac{2}{3d^2}\left(1-\sum_{i=1}^d x_i^4\right),
 \qquad
 F_{\mu_X}(x)-B_d\ge\frac1{3d}\sum_{i=1}^d\left(x_i^2-\frac1d\right)^2.
\]
The displayed stability coefficients are valid universal constants; no claim of optimal coefficients is made.

## Assumptions and scope
Distances are **intrinsic angular geodesic distances on the unit round sphere in radians**, not ambient Euclidean chord distances or paths on the boundaries of solid polyhedra. The measures may be discrete or continuous. Antipodal symmetry means \(\mu(A)=\mu(-A)\) for all measurable \(A\). Isotropy has total mass one, hence second moment exactly \(I_d/d\). The cube and cross-polytope are regarded as *sets of directions on the same round sphere* with equal point mass; all minimizations range over the entire sphere. In dimension two the two configurations are squares rotated by a quarter of the angular spacing.

## Proof
**Antipodal reduction.** For \(t\in[-1,1]\), \(\arccos t=\pi/2-\arcsin t\) and \(\arccos(-t)=\pi/2+\arcsin t\). Therefore antipodal averaging gives
\[
 F_\mu(x)=\frac{\pi^2}{4}+\int\arcsin^2(\langle x,v\rangle)\,d\mu(v)
 =\frac{\pi^2}{4}+\mathbb E\,\phi(Z),
\]
where \(V\sim\mu\), \(Z=\langle x,V\rangle^2\in[0,1]\), and \(\phi(s)=\arcsin^2\sqrt s\).

**Strong scalar convexity.** Direct differentiation on \((0,1)\) yields
\[
 2s(1-s)\phi''(s)+(1-2s)\phi'(s)=1.
\]
The analytic solution at zero with \(\phi(0)=0\) has \(\phi(s)=\sum_{n\ge1}a_ns^n\), \(a_1=1\), and
\[
 a_{n+1}=\frac{2n^2}{(n+1)(2n+1)}a_n\qquad(n\ge1).
\]
In particular \(a_n>0\) and \(a_2=1/3\). Hence \(\phi''(s)\ge2/3\) on \([0,1)\), and \(\phi\) is strictly convex on \([0,1]\) (continuous at the endpoint). This also gives the pointwise supporting-line inequality
\[
 \phi(s)\ge\phi(m)+\phi'(m)(s-m)+\frac13(s-m)^2\quad(0\le s\le1,\ 0<m<1),
\]
by integration and endpoint continuity. Since \(\mathbb EZ=x^\top(I_d/d)x=1/d\), taking expectations at \(m=1/d\) proves the refined universal bound. Its fourth-moment bracket is exactly \(\operatorname{Var}(Z)\ge0\). Strict convexity implies equality with the baseline \(B_d\) if and only if \(Z=1/d\) almost surely.

**Cube vertex measure.** For independent uniform signs \(\varepsilon_i\in\{-1,1\}\), \(\langle x,V\rangle=d^{-1/2}\sum_i x_i\varepsilon_i\). Expanding the fourth power and using cancellation of odd sign products gives
\[
 \mathbb E\langle x,V\rangle^4=\frac{3-2\sum_i x_i^4}{d^2},\qquad
 \operatorname{Var}(Z)=\frac{2}{d^2}\left(1-\sum_i x_i^4\right).
\]
For a unit vector, \(\sum_i x_i^4\le(\sum_i x_i^2)^2=1\), with equality only if exactly one coordinate has absolute value one. Thus \(Z\) is constant precisely at the \(2d\) signed coordinate axes. The universal bound is attained there (each cube vertex makes the same absolute scalar product), which proves the exact argmin and its stability inequality.

**Cross-polytope vertex measure.** The random direction \(V\) chooses \(i\) uniformly in \(\{1,\ldots,d\}\), and then chooses \(\pm e_i\) with equal probability. Thus \(Z=x_i^2\), and
\[
 \operatorname{Var}(Z)=\frac1d\sum_i\left(x_i^2-\frac1d\right)^2.
\]
This vanishes if and only if \(x_i^2=1/d\) for every coordinate, namely \(x\in C_d\); each such point attains the baseline. This proves the second exact argmin statement and bound. The two minimizer sets are mutually dual in the literal cube/cross-polytope sense, but no duality for arbitrary antipodal isotropic sets is asserted.

## Verification
An accompanying standalone standard-library script, `verify.py`, independently enumerates both vertex sets in dimensions two through eight, tests their predicted minima, verifies the cube fourth-moment identity on seeded random unit vectors, and checks both quantitative inequalities at sampled points. It passed 2,114 numerical checks. These tests only supplement the exact all-dimensional algebra above; they are not used as infinite-dimensional or global optimization certificates. The proof of the scalar power-series recurrence is given explicitly rather than inferred from sampling.

## Relationship to prior work
The intrinsic Fréchet mean on spheres is an established nonconvex geometric optimization problem. Hotz and Huckemann (arXiv:1108.2141, publicly available 2011-08-10) analyze intrinsic means on the circle, including nonuniqueness. Eichfelder, Hotz, and Wieditz (arXiv:1802.09243) provide a global branch-and-bound method for spherical Fréchet means and numerical examples with multiple minimizers; their inspected paper does not state the present dimension-uniform antipodal isotropic bound or the complete dual cube/cross-polytope minimizer sets. Roychowdhury (arXiv:2601.03333) studies spherical quantization and cluster means, mostly on \(S^2\); its inspected statements do not imply these exact all-dimensional one-center minimizers. This result is not a claim of a new definition of intrinsic mean or of an improved general-purpose algorithm.

## Limitations
The geometric conclusion applies to antipodally symmetric **isotropic** direction distributions; removing either hypothesis is not covered. Stability constants are not asserted sharp. Full independent historical priority review has not been performed, and undiscovered equivalent formulations in earlier work on spherical potentials remain a residual novelty risk. No numerical test substitutes for the analytic global proof. No independent validation is claimed.

## References
1. T. Hotz and S. Huckemann, *Intrinsic Means on the Circle: Uniqueness, Locus and Asymptotics*, arXiv:1108.2141, initial public preprint 2011-08-10. https://arxiv.org/abs/1108.2141
2. G. Eichfelder, T. Hotz, and J. Wieditz, *An algorithm for computing Fréchet means on the sphere*, arXiv:1802.09243, initial public preprint 2018-02-26. https://arxiv.org/abs/1802.09243
3. M. Roychowdhury, *Optimal Quantization of Finite Uniform Data on the Sphere*, arXiv:2601.03333, initial public preprint 2026-01. https://arxiv.org/abs/2601.03333
