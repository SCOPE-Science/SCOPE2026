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

The source file `verify.py` uses only the Python standard library and exact rational arithmetic. Execute `python3 verify.py` from the extracted artifact directory. It exhaustively enumerates remaining-edge orientations of the fair tournament for every marked outdegree at orders 3 through 7, reconstructing cyclic triples directly from edge directions. It checks the three conditional cumulants and all exceptional sign cases, and separately evaluates exact algebraic derivative inequalities over a finite range as a diagnostic. The general theorem is proved symbolically in RESULT.md; enumeration and bounded parameter checks are not certificates for infinitely many orders.
