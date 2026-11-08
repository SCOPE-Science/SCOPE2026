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

For all n>=2 and real 0<=t<=n, reconstruct vertices of [0,1]^n with sum<=t: binary weights j<=m and m ones plus a single fractional delta, then maximize strictly convex squared-distance envelope at symmetric center. For 2m<n, the two quadratic branches meet at c=delta/2 and are minimized at m/n and (m+delta)/n respectively, so c=median(m/n,delta/2,(m+delta)/n); for 2m>=n the unique center is 1/2 with R^2=n/4. Contact orbits and plateau delta<=2m/n follow from strict inequalities in the envelope. Independent Fraction arithmetic rebuilt vertex inequalities and contact convex-hull orbit means for 272 (n,t) samples, including n=8,m=2 branch values; samples corroborate but do not prove the all-dimensional result. Singleton t=0, integer caps, transition ties and t=n checked conceptually.

## originality

PASS

The new contribution is the specified exact mathematical fact and not any already known nonequivariant/underlying special case; see each implication comparison and full-material primary inspections. The inspected candidates do not imply the new claim as stated. Historical priority is provisional and risks are explicit.

## value

PASS

Boundary contact theorem and radius formula are motivated as an exact Euclidean circumball classification for the canonical uniformly clipped hypercube, including noninteger parameters; the positive-length radius plateaus and fractional contact transition are nontrivial geometry not implied by integer uniform-matroid cases. Natural applications include precise covering-radius benchmarks of knapsack sections, though no broad application theorem is asserted.

The dated certificate retains the supplied scientific assessment, sources and limitations.
