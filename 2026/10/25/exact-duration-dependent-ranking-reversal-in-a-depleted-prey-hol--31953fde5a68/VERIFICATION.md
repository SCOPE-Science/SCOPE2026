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

The analytic proof in RESULT.md uses integrated survivor equations, a necessary-and-sufficient equality criterion, continuous sign classification, and a strictly increasing universal threshold; no finite tests are promoted to continuum proof.

Reproduction: run `python3 verify.py` with Python 3.9+ and no third-party packages. The fixed-seed program checks 700 parameter quadruples of strict tradeoffs; for each it independently inverts the exact survivor equations at the predicted equality stock and at points on either side, tests 1,400 strict comparisons, and checks the threshold value and near-zero series. Numeric bisection and finite sampling test arithmetic implementation only; they cannot establish global novelty or mathematical correctness for all real parameters.

Source access limits: Rosenbaum–Rall (2018) relevant full-text sections were available in HTML. Older Rogers (1972) and Oaten–Murdoch (1975) were available only at abstract/metadata level; an institutional full-text retrieval was not available. The primary comparison therefore retains explicit originality risk. Independent audit: not performed.
