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

# Exact verification of the finite coextinction census

The two standalone artifacts in this package are `verify.py` and `certificate.json`. Run `python3 verify.py > regenerated.json` in an otherwise empty directory with Python 3 standard library; byte-compare `regenerated.json` with `certificate.json`. The verifier uses only exact integers, finite comprehensions, and permutations, with no network calls, randomness, or external packages.

The checker generates all distinct nonempty plant neighborhoods in every positive guild-size partition through eight total species; rejects empty, repeated pollinator neighborhoods or disconnected networks; canonicalizes by exhaustive pollinator permutations and sorted plant rows; computes every conditional viable-plant count signature by enumerating all pollinator subsets; and groups isomorphism classes by those signatures. Its result shows zero collisions through seven species and first collisions at eight. The independent witness check enumerates each deletion vector instead of using bit-mask subset iteration; it confirms the common signature, both degree multisets, disjointness under all role-preserving relabelings, and different four-cycle counts.

The complete certificate reports 57 admissible connected bi-twin-free network classes at guild sizes four and four, five signature-collision groups (six extra classes), and explicitly displays the shared histogram of the two selected witnesses. These facts are finite and exact. The separate algebraic arguments proving degree recovery for arbitrary network sizes and polynomial law equivalence are provided in `RESULT.md` and are not replaced by the finite enumeration.

Limitations: this checks the stated simple bipartite, guild-preserving, connected, twin-free model and only the claimed smallest finite range; it is not a test of ecological realism, empirical sampling precision, global graph uniqueness at greater orders, or independent scientific validation.
