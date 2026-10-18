# Scientific review of the ellipsoidal section-profile rank-one deficit

## Correctness — PASS

The claim is for centered, positive-definite three-dimensional ellipsoids, measured on the common inradius-normalized offset interval with spherical/uniform probability weights. The affine section-Jacobian formula gives the exact rank-two profile. Two explicit \(2\times2\) Gram matrices have squared-singular-value sum \(S\) and product \(4D/45\), so the best rank-one relative error is their smaller eigenvalue divided by the sum. Cauchy–Schwarz supplies both positivity and equality only for balls. Uniform perturbation of the three angular moments and exact spherical quartic moments yield the coefficient \(1/24\). The two axial moment recurrences are elementary one-dimensional integrals, and their endpoint asymptotics establish the opposite degeneration limits. The standalone geometry/recurrence checker was actually executed with `VERIFY_OK`; the infinite conclusions rest on the analytical proof, not tests. No external certificate or independent mathematical validation is asserted.

## Originality — PASS (qualified historical priority)

The full relevant 2026 source, Fish–Ryabogin–Sun–Yaskin, arXiv:2610.10229 (Theorem 4.2), classifies bodies with **exact finite-rank local separability**. Its statement and proof neither define nor compute a normalized **best rank-one approximation** and do not give the near-ball Frobenius coefficient or the prolate/oblate divergence of extreme regimes. The earlier Yaskin–Zawalski arXiv:2306.17127 Theorem 2.2 is also about structural classification under exact separability of related integrals. The fully read available RESULT.md of the closest published ellipsoid recoverability, finite-section-moment, and Archimedean linearized-section results concerns injectivity, parameter recovery, or angular kernel, not this deficit. Actual semantic research-index queries for rank one, near-ball coefficient, and prolate/oblate tails identified none with a statement implying the full theorem. The singular-value principle is classical and is not claimed as new. These comparisons support a best-knowledge originality PASS, not a proof of historical priority: unindexed prior work might treat the same optimal approximation with different normalization or terminology.

## Mathematical value — PASS

The 2026 paper naturally raises the quantitative question of how far exactly separable ellipsoidal section profiles lie from a single separated factor. The result identifies the exact optimal compression error, a sharp local quadratic detection law with an invariant anisotropy coefficient, and a substantive counterexample to unrestricted global stability: arbitrarily flattened ellipsoids have arbitrarily small relative error despite growing axis ratio. The asymmetric prolate/oblate degeneration is not an arbitrary finite table or merely a renaming of singular-value theory; it is a geometric boundary of a natural stability conjecture and is directly relevant to interpreting low-rank tomographic data. The answer depends on using the maximal common inradius interval; other data-weighting conventions require separate analysis.

## Scope and remaining risks

The only claimed result is the formula and local/global consequences for centered \(\mathbb R^3\) ellipsoids in the specified common-offset metric. No general convex-body inverse theorem, high-dimensional analog, finite-sample estimate, or independent audit is claimed. The original literature was compared by mathematical implication, including stronger-looking finiteness and uniqueness statements, but an unknown equivalent historical least-squares formula remains possible.

Self-review: passed. Independent audit: not yet performed.
