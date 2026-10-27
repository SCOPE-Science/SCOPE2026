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

# Reproducibility and mathematical boundaries

Run `python3 check.py` with a standard Python 3 interpreter and no external packages. It enumerates every perfect matching of cyclic side labels for each integer between two and seven, constructs the face permutation directly, computes orientable genus from its cycles and counts cyclically adjacent pairs. It checks each cell of the genus-by-short-chord distribution against the inclusion--exclusion coefficient obtained from the deletion formula, as well as exact means and parity covariance. The checker printed `PASS 125 exact assertions` from the delivered source.

The genus-preserving deletion and cycle-edge count supply the all-order proof. The joint Gaussian/Poisson claim depends on the cited Chmutov--Pittel genus limit and a uniform factorial-moment bound, not on enumerating finitely many matchings. Neither historical uniqueness nor any independent audit is certified by these checks.
