---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-02.md",
      "INDEPENDENT_AUDIT_2026-11-02.json"
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

For d≥4 and positive half-edges a_i, the full boundary surface-area distribution picks facet-normal coordinate I=i with probability 1/(a_i T), T=Σ 1/a_i; conditional tangential coordinates are independent uniform and normal coordinate is ±a_i. From this mixture E X_i²=(a_i²+2a_i/T)/3 and E X_i⁴=(a_i⁴+4a_i³/T)/5. For independent centered X,Y, the fourth-distance identity and diagonal covariance give κ=E D⁴/(E D²)²=1+(7E/5+28C/5-2R²+4B/T²)/(B+2R)² with B=Σa_i²,E=Σa_i⁴,R=Σa_i/T,C=Σa_i³/T. Independent rational summation of all 16 ordered facet-normal pairs for a=(1,2,3,4) yielded 48211/32670, exactly matching the invariant formula. Cauchy E≥B²/d, C≥R², and BT−dΣa_i=Σ_{i<j}(a_i+a_j)(a_i−a_j)²/(a_i a_j)≥0 imply κ≥κ_d=1+1/d+2(d−1)/(5(d+2)²), with cube the unique equality case. The residual E−B²/d gives global stability ≥2d²/[5(d+2)²]Σ(a_i²/B−1/d)²; symmetric cube perturbations show the square-root inverse exponent optimal. The numerator of 12/5−κ decomposes into nonnegative B²−E, BR−C, and R²−B/T² terms (strict for positive d≥2); slender a_1→∞ reaches the unattained supremum. Connected shape space gives every intermediate κ. SymPy independently verified exact positive formula for κ_d−κ_{d+1}; the argument covers all integer d≥4, not only tested dimensions.

## originality

PASS

Best-of-knowledge originality judgment for the exact scoped final claim, after mathematical prior-work implication comparison. Forward distance-moment formulas and 3D face-pair results are credited; the all-d≥4 surface-uniform shape extremum/stability/feasibility claim is not covered by accessible statements.

## value

PASS

This is the complete sharp normalized fourth-distance moment range for a natural surface-uniform sampling model across all d≥4, with a rigid cube optimizer, explicit inverse-anisotropy stability, sharp square-root exponent and a dimension-feasibility law. Those geometric optimization and inverse conclusions exceed isolated cube or facet-integral computations and can be used to benchmark geometric probability models.

The dated certificate retains the supplied scientific assessment, sources and limitations.
