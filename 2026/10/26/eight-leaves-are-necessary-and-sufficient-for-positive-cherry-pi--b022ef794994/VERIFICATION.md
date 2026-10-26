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

The analytical proof uses the four edge-category transition law, moment recurrences, an exact first-order perturbation recurrence at the comb boundary, and two explicit positive-coefficient polynomial certificates. For each fixed finite leaf count the parameter functions are rational and analytic at the comb endpoint. Exact checks in `verify.py` compare the four-state Markov dynamics against the moment recurrences for seven rational parameters and all leaf counts through thirteen; they also verify the algebraic small-leaf certificates and 147 harmonic-response instances. The script uses SymPy and prints its own assertion count. No finite computation replaces the proof for all leaf counts and all admissible parameters. Historical priority and independent validation remain open.
