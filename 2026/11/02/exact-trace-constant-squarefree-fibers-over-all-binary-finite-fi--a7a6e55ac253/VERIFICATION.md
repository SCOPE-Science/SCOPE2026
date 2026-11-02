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

The source file `VERIFY.py` implements finite binary-field arithmetic in polynomial-basis form, Euclidean division and the squarefreeness criterion that a polynomial and its formal derivative be coprime. Exhaustive comparisons cover field sizes 2, 4, 8, 16 at degrees 2..10, 2..7, 2..5, 2..4 respectively. The standalone replay returned `VERIFY_OK cases= 22 fibers= 1034 polynomials= 115682 squarefree= 104570`. These are finite corroborative computations, not an infinite proof or independent audit. The character generating-function proof appears in RESULT.md.
