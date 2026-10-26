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

# Reproducible checks and limitations

Run `python3 verify.py` using an ordinary Python 3 interpreter; no third-party packages are required. The companion `VERIFICATION.txt` records the output from the exact packaged checker.

The checker reconstructs every two-support vector \(X_{i,j}\), optionally adds the all-\((k-1)\) vector, checks distinctness, and enumerates **all** receiver multisets of size \(k\) for each test. It checks \(54\) construction parameter/length cases, covering \(1,563\) receiver vectors in total. Separately it enumerates every possible subset of the ternary length-3 and length-4 multiset simplices for \(k=L=2\); optimum sizes are \(7\) and \(6\).

These finite tests verify an implementation and small instances. The universal theorem follows from the symbolic heavy-coordinate incidence bound and explicit cyclic construction, not from finite sampling or from a timeout. There is no claim of independent scientific audit, proof-assistant verification, or completeness of the literature search.
