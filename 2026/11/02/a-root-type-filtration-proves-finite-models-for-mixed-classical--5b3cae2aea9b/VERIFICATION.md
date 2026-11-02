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

Run `python3 checker.py` in a Python 3 environment; the checker uses only standard-library modules. The expected exact final line is `ALL_CHECKS_OK randomized_models=250 formula_model_cases=5000 root_local_truth_lemmas=all`.

The checker generates 250 finite mixed models, including nontrivial intuitionistic posets, independent outer accessibilities, and persistent valuations. It evaluates sampled formulas and all their subformulas in the original and filtered models, checks every filtered local point, and checks the declared size bounds. The package includes the exact source file executed. This bounded test does not validate arbitrary infinite inputs, whose correctness is supplied by the mathematical proof in `RESULT.md`.

The bound is sufficient rather than optimal. The complexity corollary depends on the previously published completeness correspondence. No external or independent audit has been performed.
