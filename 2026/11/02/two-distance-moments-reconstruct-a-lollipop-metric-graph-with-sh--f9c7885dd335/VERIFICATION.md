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

# Verification of the distance-moment inverse

The included `verify.py` is independently executable using the Python 3 standard library:

```bash
python verify.py
```

Observed output:

```text
VERIFY_OK 22414 checks: exact identities, sharp inequalities, independent integration, seeded simulation
```

The script compares the two expanded moments against an independent three-case conditional construction at 199 exact rational parameters. It checks the exact contrast identity and range, all 7,260 pairs of a 121-point exact rational grid for injectivity and the quadratic inverse lower bound, numerical two-dimensional midpoint integration of the intrinsic shortest-path distance at nine parameters, a closed-form noncongruent mean-collision example, four seeded samples of 75,000 independent point pairs, and the small-loop quadratic differences for seven scales. The distance evaluator computes the shortest circular route and the route through the junction directly, not using the claimed moment formulas.

The proof in `RESULT.md`, not the finite grid, establishes the universal injectivity, all-positive-length quantifiers, exact mean fiber classification and optimal exponent. Quadrature and Monte Carlo tolerance checks are numerical corroboration, not infinite-domain certificates. Full-text comparisons and historical priority have residual access and search limitations, documented in `REVIEW.md` and `AUDIT.json`. No independent validation is asserted.
