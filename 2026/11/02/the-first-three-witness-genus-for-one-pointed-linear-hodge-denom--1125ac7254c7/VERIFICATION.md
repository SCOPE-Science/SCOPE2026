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

# Mathematical verification

The standalone `verify.py` requires only Python 3 standard-library `fractions`, `math`, and `itertools`. From the same directory as `certificate.json`, run `python3 verify.py` and check for the initial line beginning `VERIFY_OK`.

The checker derives all \(H_{g,i}\) for \(1\le g\le10\) from two algebraically independent finite algorithms: one computes Bernoulli numbers by recurrence and exponentiates the logarithmic series, while the other directly inverts the sine series and interpolates in the exponent. The rational output arrays must match exactly. Independent Minkowski prime-exponent calculation checks the full least common multiple. Enumeration of all nonempty index subsets in each genus identifies every minimum size and independently verifies explicit witness sets. The genus-ten prime-support lower bound is separately checked by exact integer valuations.

`certificate.json` records the complete reduced-denominator arrays in these ten genera and all eleven exact rational coefficients at genus ten. All tested identities are finite exact arithmetic equalities, not probabilistic samples or floating-point assertions. This certificate does not supply information about genera above ten or historical publication priority. No independent audit has been performed.
