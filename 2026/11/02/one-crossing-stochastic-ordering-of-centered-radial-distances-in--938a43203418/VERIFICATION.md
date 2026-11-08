---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-05.md",
      "INDEPENDENT_AUDIT_2026-11-05.json"
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

For area-one regular k-gons, rho_k=(k tan(pi/k))^-1/2 rises with k, R_k=rho_k sec(pi/k) falls, and k rho_k rises. On overlap (rho_m,R_m) h(t)=n acos(rho_n/t)-m acos(rho_m/t) decreases strictly from positive to negative, giving exactly one density crossing. Outside overlap density differences retain the stated signs. Thus F_m-F_n increases then decreases, strictly positive on (rho_n,R_n), TV equals Kolmogorov at the crossing, W1 is mean-radius difference. The radial-sector integration yields an elementary M(k) with sec/tan/log. Independently numerically checked six widely separated pairs including (4,6) t=.567729021647736, TV=.053443541641648. Finite checks corroborate the all-pairs analytic proof.

## originality

PASS

Known central radial CDF for individual regular polygons is prior (Khalid-Durrani 2012; Dacey 1965) and Fraenkel polygon-to-disk comparisons are prior. All n<m stochastic ordering and unique pairwise density crossing with exact TV/W1 were not in the inspected relevant primary arguments. Best-of-knowledge qualified for older facility-location literature.

## value

PASS

Uniform-point radial distributions are natural geometric/probabilistic invariants. Universal pairwise first-order stochastic dominance and sharp total-variation equality give stronger structural information than mean ordering or convergence to disk.

The dated certificate retains the supplied scientific assessment, sources and limitations.
