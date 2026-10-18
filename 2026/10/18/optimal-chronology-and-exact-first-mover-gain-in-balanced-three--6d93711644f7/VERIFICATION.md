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

Run `python check.py` (Python 3.9+, standard library only). The program independently evaluates all active unordered triples for every vertex; it does not substitute the reduced two-class vector field into the full-system integrator. Tested class sizes: 2, 3 and 5; reinforcement strengths: 0.4, 1.3, 3 and 5; half-window lengths: 0.2 and 0.6. Each case checks edge-degree counts, agreement with the scalar autonomous gap equation, the exact final mean for A-first and B-first, the strict interior bound for interleaving, and convergence after both snapshots are activated. Three additional small-time tests assess the proved quadratic coefficient.

On extraction and execution, all cases passed. The numerical tests are finite evidence against transcription/normalization errors, **not** a proof of the all-schedule optimization, uniqueness up to null sets, or asymptotic statements. Those follow from the independent analytical reduction and strict integral rearrangement in `RESULT.md`. The model is deterministic and restricted to equitable incidence and within-community homogeneous initial opinions. No independent scientific validation was performed.
