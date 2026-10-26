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

# Reproducibility and proof boundary
The supplied source file `verify_opposite_subseq.py` requires Python 3 and only standard-library modules. Run `python3 verify_opposite_subseq.py`. It returns `VERIFY_OK parameter_pairs 100 word_checks 73719` if all assertions hold. For every pair of thresholds from one through ten, the program builds the reachable greedy-product automaton, compares its states against the explicit four-region classification, and executes a final/nonfinal partition-refinement minimization. For nine parameter pairs, it checks all binary words of lengths zero through twelve using an independently written direct subsequence predicate. The checks are finite and do not establish an infinite-parametric theorem by themselves. The all-parameter proof consists of the complete reachability witness/exclusion argument and the exhaustive four-case right-quotient threshold argument in RESULT.md. An independent audit has not been performed.
