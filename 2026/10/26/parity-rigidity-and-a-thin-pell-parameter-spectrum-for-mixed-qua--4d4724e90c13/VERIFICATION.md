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

The proof of the parity classification is self-contained. It uses coprimality from the constant term, the exact valuation of the odd square plus one at the prime two, and integral conjugate-root descent on the odd-coordinate conic. The even-coordinate equivalence is exact completion of a square; reduction modulo eight gives the necessary parity and sufficiency. The parameter bound applies Chinese remainder counting and the standard reciprocal-prime estimate in the progression seven modulo eight. No finite check is substituted for these infinite steps.

Reproduction with Python 3 (standard library only): `python3 check.py`. The verified execution printed `VERIFY_OK bound 240 witnessed_parameters [3, 4, 5, 7, 11] odd_pairs 7 even_pairs 7 pell_converse_examples 11`.

Computational checks enumerate the finite coordinate square only; they do not certify a global enumeration, a best possible density bound, or originality against inaccessible material. Independent audit has not been performed.
