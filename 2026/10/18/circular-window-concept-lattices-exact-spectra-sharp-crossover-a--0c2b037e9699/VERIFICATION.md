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

# Reproducibility checks

Run `python verify_circular_arc_concepts.py` with Python 3 and only its standard library.
The checker constructs each cyclic interval independently, builds every possible intersection, and separately generates the allowed circular binary words. It computes a state-transition trace, a cyclic-composition sum, and a recurrence for every parameter pair with \(2\le n\le11\). It also verifies strict monotonicity of concept counts and directly computes joins/meets to test modularity for all cases \(3\le n\le7\).

Observed results:

`VERIFY_OK parameter_pairs=55 independent_bit_patterns=36868 n=2..11 exact_intersections=PASS cyclic_runs=PASS transfer_trace=PASS composition=PASS recurrence=PASS fixed_n_strict_inverse=PASS`

`MODULARITY_OK cases=20 n=3..7 criterion=(arc_length=1 or complement_length=1)`

Limits: finite checks do not prove the all-parameter theorem, the fixed-defect asymptotic, or research priority. Those mathematical assertions use the accompanying proof and literature comparison. No independent external audit has been performed.
