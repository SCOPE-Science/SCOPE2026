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

# Verification and limits

Execute `python verify_matching_intervals.py` using Python 3 and its standard library. A successful execution produces:

`VERIFY_OK exhaustive_matching_sizes=2..7 exact_geometric_cases=12 uniform_spacing_identities=6`

The program generates every perfect matching with \(\(n=2,3,4,5,6,7\)\), merges actual geometric intervals to compute connected-component counts and union lengths, and independently computes the quantities in the finite covariance formula. Two positive spacing configurations are examined at each size, including a quadratic nonuniform profile. Exact fractions are used throughout; every individual and joint even-cut probability is checked against the matching-count formula, and the variance and the covariance match. Six further checks verify the uniform expected-spacing identity. These calculations apply to a finite set of matchings at each enumerated size; they do **not** prove the unbounded-\(n\) or arbitrary-distribution theorem.

The analytic argument in `RESULT.md` establishes all \(n\ge2\): parity locates possible missing gaps, nested-prefix matching counts give pairwise strictly positive cut correlations, and the weighted cut representation gives the strictly negative covariance. A random endpoint configuration must be independent of the matching and have integrable range for the unconditional assertion. If the endpoint law has atoms, the strict geometric inequality as stated need not apply; for \(\(n=1\)\) the covariance vanishes. No claim of external independent validation is made.
