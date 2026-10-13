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

# Reproduction and boundaries

Run `python3 verify_tail_vax.py` using Python 3.10 or later without dependencies. The checker uses exact integers and rational fractions to regenerate every labeled tree through seven vertices by Prüfer codes, canonicalizes to 24 unlabeled classes, computes the three-case probability polynomials, and supplies nonnegative coefficient certificates for all 23 parameter-independent classes. It reconstructs all seven witness vaccination choices at five rational transmission probabilities by explicitly summing every subset of surviving edges.

Successful execution yields:

`VERIFY_OK shape_counts={2: 1, 3: 1, 4: 2, 5: 3, 6: 6, 7: 11} exact_stable_shapes=23 exceptional_seven_shape=1 witness_reconstructions=35 crossover=3/5`

The exact identities and inequalities proved in RESULT.md, not numerical samples, justify the full parameter interval. The classification is proved only for trees of orders two through seven. A third-party independent mathematical audit has not been performed. Other published works might imply this specialized claim; the literature search and inspected primary texts were not exhaustive.
