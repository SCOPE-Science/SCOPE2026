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

# Exact verification protocol
Execute `python3 verify.py` with a standard Python 3 installation. It uses only standard-library `fractions`, `itertools`, `math`, and `random`. The enumerator visits every nonnegative seven-tuple summing to each of the six blocklengths and evaluates the finite-expectation criterion by integer arithmetic after clearing denominators. For each length it verifies both the optimal rational expectation and **the exact set** of minimizers, including the Fano line/cap restrictions.

The independent Markov check solves rational one-step equations for expected waiting times in every binary subspace, then compares all optimal profiles and 240 additional profiles against the subspace-lattice formula. Failure of any check raises `AssertionError`; a success marker is printed only after all tests finish. Read `verification_output.txt` for the recorded actual execution. These checks certify the stated finite cases conditional on correct execution of the supplied open code; they are not an external mathematical audit and they do not extend the result to arbitrary lengths. Scientific novelty remains subject to literature coverage risks described in the review.
