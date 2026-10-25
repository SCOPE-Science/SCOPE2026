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

The recursive `verify.py` computes exact rank-four first-order types, preserving equality and repeated choices; its calculation on all rung counts 3 through 16 in both closure modes establishes the finite bridge. Additional rung counts 17 through 24 test, but do not prove, the infinite range. The independent `direct_game.py` uses literal Spoiler-versus-Duplicator quantification over choices in both graphs, checking distinction at rung 8 and equivalence at rung 9. Output files record the successful local executions. The proof for all larger sizes is the radius-two column-window argument in `RESULT.md`; no finite experiment substitutes for that lemma. Cross-check the layer-twist definition when reproducing results.
