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

# Reproducibility and verification

Run `python3 verify.py` with Python 3 and its standard library from the directory containing this document. A successful run prints `VERIFY_OK` followed by the count of enumerated labeled trees and selected numerical constants. Observed output: `VERIFY_OK trees_checked= 18247 delta= 0.162751579441755 path_limit= 0.415643841780765 large_n_path= 0.415159263498 large_n_star_per_n= 0.162516293177`.

The program independently calculates edge-pair counts from explicit root vectors for all labeled trees of orders 3 through 7, checks the sharp degree-count boundaries, compares bivariate absolute Gaussian integrals against deterministic angular quadrature, and compares analytic width moments against independently simulated normalized Gaussian directions for four trees and one cyclic graph. It also numerically checks the limiting expressions for a tree of order 1001. Randomized checks are seeded for reproducibility and use explicit finite tolerances.

The proof in `RESULT.md` supplies the exact all-order argument: support-function additivity, Gaussian radial separation, the exact pair integral, and elementary tree-degree extremization. Neither stochastic simulations nor finite enumeration verify originality or turn a finite test into a proof over all orders. Independent audit has not been performed.
