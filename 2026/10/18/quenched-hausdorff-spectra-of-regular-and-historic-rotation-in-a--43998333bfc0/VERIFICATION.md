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

# Reproducible checks

The exact rational finite test lives in `verify_rotation_spectrum.py`. Running `python3 verify_rotation_spectrum.py` returns a `VERIFY_OK` line after checking all branch words for the listed environments, including 15,891 finite-word tests and three numerical pressure-normalization profiles. The script enumerates words, reconstructs initial points by inverse branches, follows the actual piecewise lifts, and compares integer lifts to an independently generated convolution count.

The mathematical theorem is not inferred from test counts. The proof requires the exact full-branch cocycle, a cylinder-count upper bound, uniformly frequency-regular environment control across concatenated blocks, a bounded independent-variable strong law, and a Euclidean Frostman measure argument. Boundary branch codes are countable and irrelevant to positive Hausdorff dimensions. No numerical approximation establishes the universal assertion. Independent external audit has not been performed.
