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

# Exact verification of the incidence-variance classification

The standalone file `verify.py` uses Python 3 standard-library `fractions.Fraction`, `itertools`, and `math.comb`. Executing `python3 verify.py` from the package directory returned:

```text
VERIFY_OK smaller_shape_pairs_tested=15 small_communities_34=42 small_communities_43=42 minimal_pair_orbits=4
```

The program enumerates each nonempty species-site subset mask, requires every site to be occupied, removes row permutations by sorting, and removes site permutations by explicit canonical minimization. It checks all same-occupancy-profile pairs. For each community and sample depth, it separately computes richness moments by directly enumerating site subsets and by summing exact indicator covariance probabilities; the two routes agree at every tested state. The raw multiset counts are \(168\) for the \(3\)-site, \(4\)-species case and \(400\) for the \(4\)-site, \(3\)-species case. Each yields \(42\) classes after relabeling. The program also checks all admissible smaller total-size dimension pairs, but the mathematical no-go proof does not rely solely on that finite confirmation.

This is a complete finite verification of the four pair-orbits and their exact rational variances. It does not exhaust systems with more than seven total vertices and provides no empirical estimate or external validation. Independent audit: not performed.
