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

# Verification details

Execute `python checker.py` after installing `requirements.txt` with mpmath and sympy. The reproducible output is recorded in `check_output.txt`. The script checks twelve independent Gamma-moment integrations, six analytic eta-derivative/odd-zeta speed identities and nearby numerical zeros on both sides of each parameter threshold, and exact symbolic Eulerian polynomial root counts through \(m=6\). All assertions passed in the packaged run. The finite cases are illustrations, not certificates of the infinite theorem; completeness relies on the uniform polylogarithm expansion and holomorphic perturbation argument in `RESULT.md`. No independent audit has occurred.
