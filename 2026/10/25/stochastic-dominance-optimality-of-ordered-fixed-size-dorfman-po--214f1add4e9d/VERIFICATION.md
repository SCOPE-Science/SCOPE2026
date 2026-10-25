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
# Reproducibility and verification

`verification/verify.py` requires Python 3 and only its standard library. From the package root, run:

```text
python3 verification/verify.py > pooling-certificate.json
```

Parse both the resulting JSON and `verification/certificate.json` and check structural equality. This executable enumerates 2,478 partitions for fixed sizes and six exact rational profiles in each configuration; it compares 7,986 positive-pool-count upper-tail probabilities. For the six-person, two-person-pool case, it separately enumerates all independent underlying infection histories to cross-check the probability-generating-function approach (360 exact PMF comparisons). It checks 246 pairwise-variance extremal comparisons and stores two explicit rational counterexamples to any presumption that upper-tail improvement always lowers variance. The finite enumerations and printed results were recomputed from these packaged paths, using exact fractions; no floats or random samples are involved.

## Verified mathematical steps

The general statement relies on the analytical proof in `RESULT.md`: partial sums of largest pool log-negative probabilities, the finite transfer theorem for majorization, exact two-Bernoulli upper-tail identities, convolution preservation, strict exponential convexity for equality, and four-point signed-cross-derivative exchanges for the variance statement. Those steps quantify over every fixed positive pair of integers for which the given pooling design makes sense. The executable intentionally does **not** attempt an exhaustive infinite verification or independent literature certification.

## Limits

This verification assumes correct Python integer/Fraction operations and the supplied mathematical definitions. No empirical accuracy, dilution, correlated infections, unknown risks, adaptive pool choice or human bibliographic validation is asserted.
