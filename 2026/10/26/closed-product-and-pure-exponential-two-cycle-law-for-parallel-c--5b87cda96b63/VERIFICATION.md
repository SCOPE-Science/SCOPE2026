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

# Reproducible checks
Run `python3 verify.py` using Python 3.10 or newer and compare output with `verification_output.txt`. The script independently checks the closed product against the exact two-branch nonlinear recursion through height four, constructs every edge subset through height three and simulates each corresponding chip configuration to verify its primitive two-cycle, then enumerates all bounded chip states for heights one and two. These finite computations do not establish the claimed theorem for arbitrary height; the infinite proof is in `RESULT.md`. The truncation at 70 terms of the rapidly convergent series only supports the reported numerical approximations, not the symbolic limit.
