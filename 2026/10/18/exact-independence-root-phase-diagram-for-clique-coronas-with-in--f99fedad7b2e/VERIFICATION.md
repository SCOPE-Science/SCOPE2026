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

# Verification and limits

**Reproducibility.** Execute `python3 verify_threshold.py` using a standard Python 3 interpreter. The script has no third-party dependencies. It enumerates 108748 labelled vertex subsets across small corona graphs and compares coefficients with the derived polynomial. It also computes 940 exact-rational Routh tables at nonsingular real parameters for the scalar factor and compares their right-half-plane counts with the exact crossing formula; no cases from that grid were omitted as singular. Further checks verify three explicit small-degree critical parameters and the dimension-six factorization at an imaginary-root boundary.

**What the checks do not prove.** Finite enumeration or finitely many Routh cases do not establish a statement for every \(k\) and \(r\). The mathematical proof identifies all boundary crossings and shows their one-sided direction, while constant degree and bounded root trajectories rule out unnoticed changes in the root count. Exact coordinates of nonboundary complex zeros are not claimed.

**Validation status.** The present review is not an independent mathematical audit. Independent audit: not performed.
