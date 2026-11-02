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

# Finite reproducibility and proof limits

Run `python3 verify_cayley_open.py` with Python 3. The program is pure standard-library Python; no special computer algebra dependency or network access is needed. The included `verify_cayley_open.out` is the exact execution output. The program checks all 24 permutations of four labels, independent normalization/branch fixed-point counts, and all five cycle classes; split point enumerations over four prime fields; and independent arithmetic enumeration of all five degree-four étale algebras over the field of three elements. Both final lines indicate successful completion.

The general theorem is not deduced from those finite tests: its all-field validity is established by the geometric inversion, exhaustive five-conjugacy-class argument, and extension-of-scalars Frobenius action described in `RESULT.md`. The explicit rational zeta functions are derived algebraically from the periodic point-count coefficients. Characteristic two is excluded. No external scientific audit or independent validation is claimed.
