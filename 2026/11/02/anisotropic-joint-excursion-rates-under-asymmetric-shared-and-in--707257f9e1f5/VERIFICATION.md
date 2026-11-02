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

## Reproducibility

Use Python 3 and run `python3 verify_shared_reset_tails.py` from the directory containing this document and the included verifier. It uses only the Python standard library. The supplied checker printed:

`PASSED: 7784 exact rational/numerical consistency assertions`

The program checks stationary generator identities and exact marginal transforms with rational arithmetic, positivity-compatible mixture transforms, 2,100 random parameter tuples against independently minimized infimal-convolution costs, 1,600 fixed-marginal monotonicity comparisons, 750 symmetric benchmarks, and finite uniform-batch source-transform specializations. A deterministic seed makes the numerical comparisons reproducible.

## Scope of verification

The theorem's all-parameter result, full large-deviation limit, branch boundaries and strict monotonicity follow from the proof in `RESULT.md`. A finite checker does not prove asymptotic limits or global originality. Critical premises independently assessed in the proof are: existence of a two-sided stationary realization, the three-type Fourier balance equation, the positive-mixture representation, the exponential-age Gaussian large-deviation rate, infimal-convolution minimization, and strict nesting of support domains.

The model's rates are assumed strictly positive, the marginal reset rates are held fixed only during the monotonic comparison, and the genuine asymmetric novelty scope assumes unequal individual reset rates. No independent external review was performed.
