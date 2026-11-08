---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-06.md",
      "INDEPENDENT_AUDIT_2026-11-06.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

For every positive orthogonal box, the random half-perimeter of its orthogonal planar shadow is sum a_i sqrt(1-U_i^2). Symmetric spherical moments give m1=(pi/4)p1, m2=alpha p1^2+(2/3-alpha)p2, m3=beta p1^3+3(5pi/32-beta)p1p2+(2beta-9pi/32)p3. Since E(X1-X2)^2>0, alpha<2/3; Cauchy–Schwarz plus E product(1-U_i^2)=4/21 gives 2beta<=4/sqrt21<9pi/32. Thus invert all three p_k and Newton cubic to recover unordered positive sides, including multiplicities. An explicit distinct pair of shapes with same p1,p2 and a local circle establish sharpness. Independent sphere integration yielded alpha≈0.59321360684 beta≈0.42181219067, negative third coefficient ≈−0.03994855, and cross-checked near-exact inversion; quadrature error is not proof.

## originality

PASS

Best-of-knowledge statement-and-implication comparison finds a distinguishable addition to the inspected primary works, with explicit partial-access risks and no claim of exhaustive novelty. First two orthotope shadow perimeter moments determine p1,p2 only and leave a circle of positive side triples; the third independent coefficient determines p3 and hence all roots of the Newton cubic, so prior first-two formulas do not imply uniqueness.

## value

PASS

Minimal exact moment tomography for a natural three-parameter convex-body family using orientation-unlabeled shadow perimeter is a genuine identifiability boundary; first two moments provably fail and the third always restores uniqueness.

The dated certificate retains the supplied scientific assessment, sources and limitations.
