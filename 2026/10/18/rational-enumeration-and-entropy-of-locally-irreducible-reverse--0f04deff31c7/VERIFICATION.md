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

# Reproducibility and scope of verification

Run `python3 VERIFY.py` using Python 3 with only the standard library. The test prints accepted parameters and ends with `ALL_CHECKS_PASSED` if every comparison succeeds. The script implements a coefficient recurrence, an independently constructed automaton dynamic program, literal exhaustive word enumeration, and a positional-conjugacy test. It checks literal exhaustive lengths to \(16,8,6,5\) for alphabet sizes \(2,4,6,8\), respectively, and exact state dynamic programming to length \(35\) for each size. No random sampling is used.

The infinite theorem relies on the explicit marked-cluster proof in `RESULT.md` and the nonnegative-matrix argument. Finite checks alone cannot establish the recurrence for all lengths or exclude equivalent earlier literature. No external or independent audit has been performed.
