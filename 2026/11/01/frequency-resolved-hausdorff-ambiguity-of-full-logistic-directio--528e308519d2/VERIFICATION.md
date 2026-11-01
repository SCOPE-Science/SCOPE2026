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

# Reproducibility and proof limits

With Python 3 and no third-party dependencies, run `python3 verify_direction_fiber.py` from the directory holding the file. The checker uses `fractions.Fraction` to compare the length-1 through length-10 sign-word probabilities against the three-cell Markov chain, enumerate the two inverse-return paths for each gap length from 2 through 16, reconstruct inverse cylinders for several multi-gap schedules, and check equal lengths and disjoint interiors. The executed output was:

```
PASS exact_markov_word_checks 2046
PASS first_return_two_branches k=2..16; disjoint equal cylinders
PASS multi_return_equal_cylinder_lengths and counts
PASS stationary_mean=1/3 stationary_down_frequency=1/3
PASS sign_entropy=(2/3)log(2), typical_fiber_dimension=1/3
PASS finite_checks_total 2234
```

The displayed exact results concern finitely many finite words. The proof in `RESULT.md` supplies the infinite extrapolation via an exact path classification, Frostman bound, ergodicity, and local bi-Lipschitz conjugacy. The program does not certify originality, reach the entire infinite domain computationally, or perform independent validation. No Lean/external expert certificate is asserted.
