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

# Verification notes

The complete analytic proof is in `RESULT.md`. Running `python3 verify_period3.py` (Python 3 standard library only) reproduced: `PASS: 4912 nonzero rational weight triples, exact variance identities, sharp-envelope and linear-stability numerical diagnostics, eight boundary checks.` The calculated optimal coefficient was approximately `0.040440114519881`.

The checker uses rational arithmetic for input moments and floating-point bisection for the positive cubic root; it is a finite consistency test, not an exhaustive or independently certified proof. The uniform case, the change of support at normalized variance one half, and the degeneration to a single edge are addressed algebraically in the proof. No external audit or independent scientific validation has been performed.
