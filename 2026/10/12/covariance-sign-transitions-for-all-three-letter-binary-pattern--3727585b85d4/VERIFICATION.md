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

`verify.py` independently derives the exact covariance rational functions by a first-pattern absorption model and by a separate finite Markov reward model that tracks both occurrence flags. It compares all sixteen complement-orbit representatives symbolically, all twenty-eight distinct unordered pairs at three exact rational coin biases, validates positive-denominator factor identities, and applies exact Sturm counting to the sixteen numerator sign polynomials. It checks that the polynomials have no multiple roots or boundary zeros.

Run `python verify.py` after installing `requirements.txt`. The observed output was:

```
VERIFY_OK pair_orbits=16 all_pairs=28 symbolic_cross_checks=16 rational_cross_checks=84 representative_interior_zeros=13 sturm_certificates=16
```

The root counts and covariance identities use exact symbolic operations. The decimals in RESULT.md are nonbinding approximations; numerical probing or finite sample enumeration is not used as a proof. The scope does not extend to word lengths other than three, dependence between tosses, or degenerate bias endpoints. General joint waiting-time generating functions are established in earlier literature; independent originality and mathematical audit remain unperformed.
