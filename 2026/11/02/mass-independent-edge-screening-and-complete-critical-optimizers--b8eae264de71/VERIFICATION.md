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

# Reproduction

Run `python3 verify.py` with Python 3, NumPy and SciPy. The program recomputes the path and critical-face conductances from the stated formulas, checks the exact flux and budget identities with rational arithmetic, and verifies many independent generalized eigenvalue instances. It also probes the strict threshold directions and solves a finite set of noncritical constrained optimization instances. It prints 2,000 exact-rational assertions, 8,190 numerical assertions and 24 successful numerical optimizations. All finite checks supplement rather than establish the universal proof in RESULT.md. No independent mathematical audit is claimed.
