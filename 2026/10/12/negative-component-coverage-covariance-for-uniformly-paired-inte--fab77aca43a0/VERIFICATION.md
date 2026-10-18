---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
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

Cut representation K=1+sum Z_j, V=range-sum g_(2j) Z_j holds for every perfect matching. Internal matching probabilities q_(n,j)=C(n,j)/C(2n,2j) and nested-cut P(Z_i=Z_j=1)=q_(n,j)q_(j,i) imply strictly positive cut covariance because q_(a+1,b)/q_(a,b)<1. Conditional mixed covariance is negative for all positive gaps; independent location randomness preserves sign; IID uniform spacings give Cov(K,V)=-(b-a)Var(K)/(2n+1). Separate merged-interval exact rational enumeration of all matchings for n=2..5: counts 3,15,105,945 with strictly negative covariance (-10/9,-364/75,-13296/1225,-345356/19845) on unequal gaps. Proof handles all n>=2, n=1 zero.

## originality

PASS

Acan and Flajolet–Noy define components by crossing intersection graph, Young by runs of adjacent short chords; nested intervals can share a real union component without being connected in the crossing graph. None of their checked component models directly calculates length-weighted line-union covariance. Substantive best-of-knowledge originality, not merely absence of identical wording.

## value

PASS

All-geometry negative correlation between natural topological component count and geometric covered length is a genuine dependence law, with exact coefficients and uniform-spacing variance identity. This is stronger than sampling a single interval distribution and usable as a benchmark for random pairing coverage.

The dated certificate retains the supplied scientific assessment, sources and limitations.
