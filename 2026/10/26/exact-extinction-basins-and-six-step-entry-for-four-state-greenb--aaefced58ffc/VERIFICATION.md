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

The finite-support proof checks each of 225 possible ordered nonempty support pairs and determines every cycle and its distance to entry. The separately implemented labelled-state transition was exhaustively simulated for all shore sizes from one through four, covering 115,600 configurations. The checker confirms exact basin and period counts on each graph, the entire 80-row first-entry coefficient table, 36 weighted-support calculations on sizes up to six, and the balanced extinction identity through size 30.

To reproduce with Python 3 standard library only, place `gh4_biclique_verify.py` beside `gh4_biclique_depth_table.csv` and execute `python gh4_biclique_verify.py`. The output must terminate with `GH4_BICLIQUE_CERTIFICATE_OK: 225 exact support pairs, 115600 independent full-site states, 36 weighted counts.` An archived run is included as `gh4_biclique_verify.out`.

The finite enumeration is exhaustive only for the 225-state support factor. The proof that this factor controls arbitrary biclique sizes is the mathematical lifting and recurrent-support argument in RESULT.md; exhaustive small-graph simulation is a separate cross-check, not a substitute for this infinite-family argument. Scientific novelty is a best-knowledge literature comparison, not a completeness guarantee. Independent audit: not performed.
