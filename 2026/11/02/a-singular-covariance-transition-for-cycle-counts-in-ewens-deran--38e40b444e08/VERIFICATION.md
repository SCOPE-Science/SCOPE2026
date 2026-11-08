---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-04.md",
      "INDEPENDENT_AUDIT_2026-11-04.json"
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

Marking distinct r,s cycles in the weighted exponential formula gives E C_r=(theta/r)Z_(n-r)/Z_n and E(C_r C_s)=theta²/(rs) Z_(n-r-s)/Z_n, hence exact covariance (already known). For theta=1, Z_m=sum_{j<=m}(-1)^j/j!; alternating remainders yield strict alternating sign of Z_(u+r+s)Z_u-Z_(u+r)Z_(u+s) including u=0,1; factorial leading remainder gives (-1)^u e/[rs(u+1)!]. For fixed theta!=1, Z_m=e^-theta m^(theta-1)/Gamma(theta)(1+3theta(theta-1)/(2m)+O(m^-2)); mixed finite differences of log Z give -(theta-1)rs/n² and covariance theta²(1-theta)/n²+O(n^-3). Independent exact rational tests: 360 theta=1 parity checks plus 210 theta=3/2 eventual sign checks, not an all-parameter proof.

## originality

PASS

Best-of-knowledge PASS qualified for exceptional all-finite-size theta=1 parity sign and factorial scale versus nonunit n^-2 transition. Published Ewens-derangement factorial moments already imply the covariance identity (not claimed novel); inaccessible full original derangements paper may conceivably contain a sign theorem.

## value

PASS

The sign and magnitude of dependence between natural small-cycle statistics has a sharp singular change at uniform derangement weight. The exact all-size parity law and length-independent leading nonunit n^-2 term distinguish qualitative phases and furnish a useful asymptotic diagnostic beyond restating known factorial moments.

The dated certificate retains the supplied scientific assessment, sources and limitations.
