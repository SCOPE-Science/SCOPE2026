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

The standalone `verify.py` uses only Python's standard library. Running `python verify.py` completes two independent finite verification procedures. One enumerates all exact-step descendants directly and checks equality to the claimed closed form and reachability predicate on 2,550 seed-radius pairs, comparing 2,708,780 candidate targets. The other checks the existence of a valid inverse deletion retaining the embedding-and-run predicate on 84,490 admissible source-target pairs (target lengths up to ten). Expected successful terminal markers are `RC1_DESCENDANTS_PASS` and `RC1_INVERSE_LEMMA_PASS`.

All statements for unbounded seed lengths and steps are proved mathematically in `RESULT.md`; no finite test by itself proves the infinite assertions. No independent external audit or certification is asserted.
