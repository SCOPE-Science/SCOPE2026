# Scientific review: vertex-perturbation stability for triangle strength

## Correctness

**PASS.** The definitions fix the semiperimeter and signed orientation unambiguously, including degenerate configurations. Elliptic coordinates make the one-apex gradient exactly rational. The inequality reduces to positivity of three explicit polynomials; the potentially sign-indefinite first two have a complete exact-rational Bernstein certificate on the bounded interval and positive shifted coefficients on the entire unbounded tail. The zero-area and coincident-vertex boundaries are handled before integration along apex paths. Symbolic differentiation verifies the lower witness. The executable checker reproduces the critical finite computations.

## Originality

**PASS within the inspected literature, with residual priority risk.** Anosova--Kurlin (arXiv:2602.17630, Theorem 2.8(b)) derive a much larger constant for arbitrary perturbations. Kurlin (arXiv:2303.13486, Theorem 4.2) establishes earlier qualitative and quantitatively weaker global stability. Their inspected proofs do not yield the vertexwise constant \(3/32\), the exact near-sharp witness, or the derived \(9/32\) all-vertex coefficient. No directly matching result was found under alternative terms such as Heron-invariant, triangle strength, and semiperimeter-normalized squared area; this is not a claim of exhaustive historical priority. The closest generic barycentric Lipschitz-free interpolation estimates study different functions and do not imply this bound.

## Mathematical value

**PASS.** The originating work explicitly motivates a scalar Lipschitz descriptor for noisy geometric point clouds and needs quantitative robustness. An exact rational global certificate tightens the published triangular coefficient from \(2\sqrt3\) to \(9/32\) for independent three-vertex perturbations, a factor greater than twelve, while the canonical one-vertex coefficient is bracketed within \(0.4\%\) of optimal. These are usable uniform numerical stability guarantees, valid through degeneracy, rather than a change of normalization or a point-sampled improvement.

## Sources and limitations

Primary scientific sources: Anosova--Kurlin, arXiv:2602.17630 (2026), Sections 2--3; Kurlin, arXiv:2303.13486 (2023), Section 4 and Theorem 4.2. Residual risks: unindexed sharp-constant literature; optimal one-vertex value and sharp simultaneous three-vertex value are unproved. The attached checker verifies exact finite algebra, not independent peer review.

Self-review: passed. Independent audit: not yet performed.
