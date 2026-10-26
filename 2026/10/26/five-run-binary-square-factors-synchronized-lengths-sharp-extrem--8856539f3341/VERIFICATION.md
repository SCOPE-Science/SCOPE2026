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

# Verification of mathematical claims

Running the included Python 3 file `verify.py` independently constructs the entire distinct-square set from contiguous substrings and compares it with the four-class closed form for all 3,125 tuples with positive run lengths at most five. It checks the two stated rational generating-function coefficient sequences, extremal counts and equality witnesses for every word length from five through 26, plus witnesses for lengths up to 159.

Observed output:

`VERIFY_OK complete_distinct_square_sets=3125 enumerated_length_histograms=22 sharp_witness_lengths=5..159`

The universal factor classification is proved by the transition count of a repeated root and the forced embedding across source run boundaries. The sharp extrema are derived by inequalities on the five run lengths. The rational functions follow from a positive-integer lattice-point parameterization, and the probability limits from their poles and simplex convergence. These analytic steps, not test coverage alone, support the infinite claims.

**Limits.** Finite verification cannot prove the infinite formulas; exact algebraic arguments appear in `RESULT.md`. Published literature overlap remains incompletely resolved for a related 2014 proceedings paper whose full text was unavailable. No independent audit has been performed.
