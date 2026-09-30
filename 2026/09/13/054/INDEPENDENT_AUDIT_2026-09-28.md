# Independent Audit — 2026/09/13/054

Audit date: 2026-09-28 (UTC)
Audited tree: `570665708e7909fe1d794559bb2e8c590aed59a3`

## Disposition

**PASSED** — Passed: interval-certified Voronoi/deep-hole bounds prove the normalized covering-radius increase and appear original and scientifically useful.

## Correctness

**PASS**. The certificate logic checks. The rank-3 m=16 computation obtains a rigorous Gram-matrix lower eigenvalue bound by interval LDL, uses a valid a-priori covering-radius bound to confine all Voronoi-relevant vectors, and evaluates every nonsingular triple of candidate facets with exact integer linear algebra followed by interval solves; the resulting maximum gives μ16≤1.25675225. For m=32 the interval-LDL sphere decoder exhausts every integer point within squared radius 4.84 around the stated half-integral hole and certifies none exists, giving μ32≥2.20. The normalized numerical comparison is then immediate. The full-unit identification for these real 2-power cyclotomic fields is consistent with class number one and Sinnott's cyclotomic-unit index theorem, and the reported regulators agree with the cited LMFDB fields.

## Originality

**PASS**. The searched literature provides general upper bounds for logarithmic unit-lattice covering radii, but no exact or certified two-sided values for these two maximal real cyclotomic fields and no normalized comparison μ(Λ32)/√7>μ(Λ16)/√3. Regulator tables do not determine covering radius, and one-sided general bounds cannot imply the submitted separation.

## Scientific value

**PASS**. This is a natural exact comparison along the 2-power cyclotomic tower, supported by independently checkable Voronoi and deep-hole certificates and a nontrivial separation gap. It is a reusable benchmark for logarithmic unit-lattice geometry rather than an arbitrary parameter lookup.

## Evidence and limitations

Repository files were read from the exact assigned/current tree and GitHub was used only as evidence. The following literature comparisons were inspected from lawful open-access sources:
- https://doi.org/10.1016/j.disc.2023.113665 — de Araujo: general upper bound for covering radius of logarithmic cyclotomic lattices; does not give this pairwise two-sided comparison.
- https://arxiv.org/abs/2507.20544 — Punch: improved general upper bound; no exact Q(zeta_16)^+/Q(zeta_32)^+ comparison.
- https://www.lmfdb.org/NumberField/4.4.14641.1 — regulator/field cross-check for degree-4 field.
- https://www.lmfdb.org/NumberField/8.8.4294967296.1 — regulator/field cross-check for degree-8 field.

No claim is made that the m=32 lower bound is sharp; only the certified 2.20 lower bound is required for the comparison.
