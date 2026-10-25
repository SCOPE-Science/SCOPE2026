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

# Verification performed

The included `verify_contextual_k1.py` enumerates **all source words** of lengths from 1 to 12 for two symbols, from 1 to 9 for three symbols, from 1 to 7 for four symbols, and from 1 to 6 for five symbols. For each word it independently applies the deletion rule to original run-leading positions and compares the entire resulting image set with the exact characterization. It also compares every output-length histogram to the displayed binomial sum.

There are 34 distinct tested (alphabet size, input length) parameter pairs, totaling 79,087 source words. The recorded standard-Python execution terminated with `VERIFY_OK`. The analytic infinite proof is independent of these finite tests. The capacity and central limit theorem depend on the explicit rational generating function, its unique strictly dominant analytic pole near the probability-generating-function argument 1, and a Taylor expansion of its logarithm.

To replay from these standalone files, use `python3 verify_contextual_k1.py`; the only imports are standard-library modules. No external datasets, network services, or other-row files are required.

# Limitations

No independent scientific audit has been performed. The computational check is finite. Thresholds greater than one, intermediate deletion probabilities, and distributions induced by random input rather than uniform distinct outputs are outside the theorem's scope.
