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

Run `python checker.py` with a standard Python 3 installation. The script has no external dependencies and performs exact integer and `fractions.Fraction` arithmetic throughout. An actual execution completed with the output:

```
PASS: 954 exact assertions; 46224 uniform permutations enumerated; 24 patterns checked
```

The program independently enumerates every uniform permutation for lengths four through eight, calculates actual fixed-point/pattern joint moments, checks the sixteen reverse-complement polynomial groups (covering 24 patterns), and verifies Vandermonde endpoint-exclusion identities for sample sizes through 100. For every pattern it separately checks the proposed cubic polynomial identity at four distinct sample sizes. The proof establishes the degree-at-most-three bound, so these four values constitute an exact all-size polynomial identity certificate rather than an unproved extrapolation.

Additional sign tests cover the three patterns that achieve both covariance signs, and the sum of all 24 covariance polynomials is verified as zero in the tested sizes, as independently required because the total number of length-four windows is deterministic.

Limits: the enumeration alone does not prove all-size statements; the proof's conditional probability and polynomial degree arguments are essential. The checker does not establish novelty or independent mathematical certification. No external audit has been performed.
