---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---
# Verification record

The attached `check.py` uses only Python standard-library integer arithmetic. It enumerates Ehrhart values via exact finite transfer sums, recovers \(h^*\) with binomial inversion, and compares palindromicity against the classification for all \(2\le d\le10\), \(1\le s\le8\). The actual execution ended with `ALTERNATING_GORENSTEIN_CHECK_OK cases=72` and zero disagreements. It also prints eight representative \(h^*\)-vectors, among them \((d,s)=(4,3)\) with coefficients \((1,90,284,94,1)\).

The conceptual all-parameter verification is the facet-distance argument in `RESULT.md`: lower-coordinate facets force center \(c=\mathbf1\), while two true upper facets with unequal capacities force contradictory values of the same integer index. Explicit saturating points establish genuine facets for all parameter regimes. For the two positive families, translation and dilation produce reflexive polytopes with every primitive supporting hyperplane one unit from the origin. A finite computation alone would not establish the theorem.

Historical originality was compared against the recent primary paper's Theorem 1.9, Proposition 3.21, Corollary 3.24 and Question Q1, as well as the related older stable-set literature. Mathematical priority remains provisional; independent validation has not been performed.
