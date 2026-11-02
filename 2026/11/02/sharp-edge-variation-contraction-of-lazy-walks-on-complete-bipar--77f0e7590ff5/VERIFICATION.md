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

# Reproduction and limits

Run `python verify_bipartite.py` using Python 3 with the standard library. It independently evaluates the graph-neighbor averaging map and every undirected edge difference using `fractions.Fraction`.

Successful execution produced:

- 31,468 exact direct checks of nonconstant binary signals for part sizes \(2\le p,q\le5\) and nine or fewer rational holding parameters per size profile;
- 2,536 exact comparisons of direct graph variation with the separately implemented cut-count formula;
- 1,200 additional direct inequalities on random real-valued rational profiles;
- 814 exact equality/extremizer comparisons for bipartition sizes \(2\le p,q\le14\).

No floating-point comparisons, timeouts, or external mathematical libraries are involved in the reported run. These finite tests do **not** certify the universal claim; the proof uses a coarea identity, a sharp integer cut-size inequality and two exhaustive absolute-value sign cases. In particular, the script's random generator is seeded for repeatability, but no probabilistic statement is asserted.

The independent scientific audit is not performed. The possibility of equivalent older results under another terminology is a priority limitation, not a proof defect or a claim of certified novelty.
