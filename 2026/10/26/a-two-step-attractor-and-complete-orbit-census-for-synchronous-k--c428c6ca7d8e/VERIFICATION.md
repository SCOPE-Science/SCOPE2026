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

The accompanying `check_biclique.py` requires Python 3 and no nonstandard dependencies. Execute `python3 check_biclique.py`; the original run printed `PASS: exact orbit/entry/basin census for 301 parameter triples, a,b<=7.` and `PASS: F^4=F^2 for every enumerated state and parameter.` For each pair of part sizes 1–7 and each threshold up to the largest part size plus one, all labelled bit vectors are traversed. Each next state is recomputed by checking the number of disagreeing neighbours for each vertex, not by the binomial counting formula. The checker compares the fixed, primitive period-two, entry-time and (when relevant) uniform-basin counts with the proposed closed formulas.

These finite computations are **not** a proof for unbounded part sizes. The noncomputational certificate is the exhaustive low/middle/high transition lemma, plus the nine pair-class implications and exact disjoint class counts in `RESULT.md`. The general theorem includes the equality-to-threshold update convention and the cases where some vertices have degree less than the threshold. No machine proof assistant or independent audit is claimed.
