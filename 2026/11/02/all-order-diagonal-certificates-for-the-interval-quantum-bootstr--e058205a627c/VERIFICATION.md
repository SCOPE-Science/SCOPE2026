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

The packaged `verify.py` is a standalone SymPy program. Run from the same extracted directory with `python3 verify.py` after installing the dependency recorded in `requirements.txt`.

It checks equality of the formal rational diagonal obtained from the Schrödinger equation and the product formula for orders one through six, verifies the source's explicit low-order diagonal examples, computes exact physical Legendre weighted derivative norms for orders zero through four and levels zero through seven, and tests negative rational diagonal witnesses in the first six pole gaps. Its exact finite tests provide regression diagnostics, not an infinite-order proof.

The arbitrary-order proof is contained in `RESULT.md`: the weighted-derivative integral identity, formal rational-moment interpolation, parity removal of odd-step resonances, and one-negative-diagonal sign argument. An independent audit has not been performed. No experimental script is treated as a substitute for the all-order proof.
