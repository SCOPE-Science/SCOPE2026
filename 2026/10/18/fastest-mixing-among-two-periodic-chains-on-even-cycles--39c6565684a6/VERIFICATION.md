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

The complete proof is the Fourier-block and scalar-inequality argument in `RESULT.md`.

To reproduce the checks, run `python verify.py` with Python 3, SymPy and NumPy. The program verifies four exact symbolic identities, an exact rational four-state defective optimal witness, and 2275 grid instances for graph orders 4, 6, 8, 10 and 12. It terminates with:

`VERIFY_OK symbolic_identities=4 defective_four_cycle=1 finite_parameter_checks=2275`

The exact symbolic identities are not an automated proof assistant certification. Grid comparisons are neither exhaustive over the real parameter region nor evidence for all even graph sizes. Mathematical conclusions for arbitrary real parameters follow from the stated universal algebraic inequality and Fourier argument.
