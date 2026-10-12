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

# Verification

Run `python3 verify.py` with the included standalone file. It uses only the Python standard library, with no network access or imported packages. It enumerates exactly one upper triangular matrix per scalar coset, computes the commutator operator over each requested prime field, tests composition-idempotence entrywise, computes its actual vector-space rank by modular Gaussian elimination, and compares every rank multiplicity to the theorem's predicted polynomial.

The program checks the following \((n,p)\) pairs: \((2,2)\), \((2,3)\), \((2,5)\), \((3,2)\), \((3,3)\), \((3,5)\), \((4,2)\), \((4,3)\), and \((5,2)\). Successful completion prints `VERIFY_OK`. Exhaustive enumeration is limited to these nine finite-prime-field instances; the proof in `RESULT.md` establishes all dimensions and all field characteristics including extension fields. The independent-audit channel has not been performed.
