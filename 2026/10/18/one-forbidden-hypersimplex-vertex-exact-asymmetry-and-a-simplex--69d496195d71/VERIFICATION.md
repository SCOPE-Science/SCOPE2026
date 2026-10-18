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
# Verification of one-forbidden-basis Minkowski asymmetry

The universal claim is proved by the halfspace and reflection argument in `RESULT.md`. The attached `verify.py` is a standalone, standard-library Python 3 checker; run `python verify.py` alongside this file. The observed run reported:

```
PASS: 36 integer profiles, 48164 polytope vertices, 212798 exact reflected-vertex tests, 10 positive-dimensional center loci
```

For each integer pair from \(3\) through \(8\) in both rank and corank, it enumerates all admissible basis indicators, constructs the purported extreme Minkowski centers and their average, checks their rescaled constraints, and verifies every reflected vertex against the actual defining halfspaces using `fractions.Fraction`. It checks the four lower-bound barriers and the predicted simplex dimensions. An additional independently formulated numerical linear program in the full rescaled coordinate variables, not symmetry-reduced, matched the exact formula for the 64 profiles \(3\le k,\ell\le10\).

**Limits.** These are finite checks, not a proof for all integers. Exact minimization, center completeness, and the universal facet description follow from the proof in `RESULT.md`. Floating-point linear programming corroborates and does not certify exactness. No independent external audit has been performed.
