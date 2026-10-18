---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-16.md",
      "INDEPENDENT_AUDIT_2026-10-16.json"
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

For any law on [0,1] with mean 1/2 and variance v, CDF F has ∫F=1/2 and ∫tF=3/8-v/2, including possible atoms; independence gives E min(X1,X2)=∫(1-F)²=∫F². Minimizing ∫F² under two affine moment constraints and 0≤F≤1 is solved by the clipped affine L meeting constraints: if H=F-F*, then ∫HL=0 and H(F*-L)≥0 pointwise, so objective difference is ∫H²+2∫H(F*-L)≥0, uniquely. In low variance v≤1/12 the solution is uniform on [1/2-sqrt(3v),1/2+sqrt(3v)] with value 1/2-sqrt(v/3); for higher variance it has two endpoint masses alpha=3v-1/4 and uniform density beta=1-2alpha, with value 7/16-3v/2+3v². Independent symbolic integrations verified exact moments and both objective values. The transformed independent triangular bonds have threshold tau=2sin(pi/18); the sharp every-law strictly-supercritical guarantee is precisely v<3(1/2-tau)²=0.06995520928... . Equality is critical, above it a subcritical optimizing witness exists; no conclusion about every high-variance law.

## originality

PASS

Best-of-knowledge PASS for exact hard-support all-laws phase diagram and sharp lattice robustness threshold, carefully crediting the minimum rule and first-regime classical Gini inequality. Full Cerone finite-interval paper was inaccessible through authorized means and remains the principal nontrivial originality risk; this alone does not defeat O.

## value

PASS

Input singlet-conversion probabilities are physically constrained to [0,1], so a worst-case swapping-protocol bound without specifying an input distribution is natural. The support-induced unique optimizer phase change at v=1/12 is not captured by unrestricted Gini/variance bounds; its exact classification yields a sharp and experimentally interpretable robustness threshold for independent double-bond-to-triangular swapping.

The dated certificate retains the supplied scientific assessment, sources and limitations.
