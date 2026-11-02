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

## Reproducibility

Run `python3 artifacts/verify.py` with Python 3 and no external packages. Expected final line: `FIREFLY_BICLIQUE_EXACT_VERIFY_OK`. The verifier constructs the 49 support-state dynamics, checks 64 algebraic parameter pairs, and directly simulates 174,051 labelled full configurations across 25 biclique sizes. The canonical 49 support classifications are in `artifacts/support_pairs.csv`; the exact recorded execution is in `artifacts/verification_output.txt`.

The finite checks are not a substitute for the all-size proof. Infinite validity rests on the exact support quotient, the fully enumerated 49 support pairs, bijectivity of the recurrent support maps, and surjection counting. Independent audit has not been performed.
