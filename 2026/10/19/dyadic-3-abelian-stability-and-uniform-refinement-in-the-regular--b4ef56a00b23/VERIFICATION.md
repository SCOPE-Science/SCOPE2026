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

The included `verify_paperfolding_3abelian.py` is a stand-alone Python 3 checker without external dependencies. Execute `python3 verify_paperfolding_3abelian.py` in the directory containing it.

The checker reconstructs all eight boundary states of the length-two paperfolding factors from explicit witnesses, applies the exact state recurrence, and computes the full one-, two-, and three-factor frequency signatures from a four-block formula. It verifies 12 coarse classes and the fine-class distribution of 32 at length sixteen and 36 from length thirty-two onward, including uniform three-way refinement of every coarse class. The 24-state stabilization gives an infinite mathematical proof; numerical sampling is not being used as an infinite certificate.

Additional checks generate 32,768 symbols by two independent descriptions, compare raw factor-frequency signatures with symbolic signatures for seven dyadic lengths, and verify the known count of distinct raw factors at those lengths. Both direct and symbolic counts are checked from the actual script. Direct tests cover dyadic lengths 16 through 1024, not all infinite positions; the proof of all positions is the exact recurrence and positional parametrization in the result.

The source comparisons do not establish exhaustive novelty, and no independent audit has been performed.
