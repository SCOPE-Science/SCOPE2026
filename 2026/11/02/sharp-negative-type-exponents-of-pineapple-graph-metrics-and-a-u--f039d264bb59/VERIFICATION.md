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

# Computational and analytical verification

The proof is symbolic and finite-dimensional for each pair of integers \(m\ge3,n\ge2\), with quantifiers over all such pairs. It uses no sample-to-infinite implication: the contrast decomposition, determinant sign, endpoint kernel and asymptotic expansion are given explicitly in `RESULT.md`.

The standalone `check_pineapple.py` uses breadth-first search on an independently generated graph adjacency list to compute the shortest-path metric. It constructs an orthonormal basis for the zero-sum subspace, diagonalizes the projected powered-distance matrix, compares both sides of the predicted threshold and checks the unique endpoint eigenvalue, a concrete equality load, and strict monotonicity on finite grids.

Execute from a directory containing the file with `python check_pineapple.py` using Python 3 and NumPy. In the completed replay the program printed `PASS 318 analytical comparison assertions`. The 318 finite checks are diagnostics, not an exhaustive proof over all graph sizes. Floating-point roundoff is controlled only by the explicit tolerances in the checker and is not used in any analytically decisive inference.

The first motivating public source used for the relevant literature window is Młotkowski–Obata's arXiv:1802.01214, posted 2018-02-04; no journal revision date is used as the earliest-public date. Independent mathematical verification and historical priority certification have not been performed.
