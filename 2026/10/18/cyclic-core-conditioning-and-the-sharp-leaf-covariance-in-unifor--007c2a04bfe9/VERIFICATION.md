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

# Reproducibility checks

Run `python3 verify.py` with a standard Python 3 interpreter. The script enumerates all mappings of sizes 2 through 6, obtains cyclic vertices by following each forward orbit and terminals by counting values with no preimage, and compares the resulting exact rational counts against the conditional probabilities, core laws and factorial moments. It also verifies the exact negative covariance and checks the scaled covariance numerically at three larger sizes. The script prints the number of passed assertions.

These are finite checks. The unrestricted conditional law follows from the rooted-forest deletion count. The strict sign follows from conditional mean monotonicity, and the asymptotic follows from a moment-controlled Rayleigh expansion. A numerical convergence check is not a proof of an infinite asymptotic. Independent scientific audit has not been performed.
