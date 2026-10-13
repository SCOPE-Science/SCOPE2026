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

The proof is the three-case counting argument in `RESULT.md`. Independently, run `python3 verify_double_stars.py` (Python 3, standard library only). The program tests each \(1\le m,n\le4\) and reports exact counts for zero, one, and two initially coloured centres. The bundled `verification_output.txt` records the outputs; all sixteen comparisons passed. This is a finite check, not an infinite certificate. No external audit has been performed.
