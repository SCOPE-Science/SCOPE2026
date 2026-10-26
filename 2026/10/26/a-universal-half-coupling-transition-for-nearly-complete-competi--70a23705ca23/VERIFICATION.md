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

The symbolic/rational checker in `verify.py` was executed from its packaged file contents. It returned: `exact model identities: 150`, `difference identities: 9`, `numerical winner tests: 12`, `PASS`.

The exact checks validate the positive subcritical equilibrium, the critical stationary simplex, and pair-only invasion rates for finite integer sizes. Nine symbolic difference identities were checked with SymPy. Numerical integrations with SciPy illustrate selection from positive pair-balanced starting populations. None is a certificate for arbitrary population sizes, and no independent scientific audit has been conducted. Proof of every all-size statement is in `RESULT.md`.
