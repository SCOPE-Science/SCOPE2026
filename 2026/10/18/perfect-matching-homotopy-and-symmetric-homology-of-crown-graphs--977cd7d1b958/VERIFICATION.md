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

# Finite verification

The standalone standard-library script `verify_crown.py` reconstructs all perfect-matching facets of each crown graph with four through seven pairs, generates every subface, then constructs the advertised acyclic matchings by the fixed ordered vertex toggles. Every nonempty Hasse cover is oriented and tested for a directed cycle using a full topological sort. For the largest case, the test handles 61,984 nonempty faces and 298,788 incidences, leaving one critical vertex and 2,175 critical four-cells. Smaller cases similarly leave the critical vectors specified in RESULT.md.

A separate inclusion-exclusion computation verifies the complete face vector against an exact counting formula for each cardinality. At seven pairs, two independent sign evaluations (cycles versus inversions on each fixed oriented simplex) agree for every one of the thirty group classes. Class sizes sum to 5,040, and the character averages give one-dimensional invariant subspaces for both the diagonal symmetric group and the full group.

`crown_verification.json` records the complete exact output. Run `python3 verify_crown.py` without network access. The proof is bounded to the four explicitly enumerated values; finite testing is not promoted to an infinite-family homotopy theorem.
