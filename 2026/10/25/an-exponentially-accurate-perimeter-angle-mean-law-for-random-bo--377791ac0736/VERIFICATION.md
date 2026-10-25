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

# Reproducibility notes

Run `python3 verify.py` with a standard Python 3 interpreter. No third-party modules, network access, downloads, or external datasets are required. The script checks independently computed convex-hull areas, the exact corner decomposition on its eligible domain, finite-sample means against the explicit binomial-void formula, rescaled variances, and independent exponential-product moments. It prints the finite checks that passed.

Analytical checks consist of: supporting-line and disjoint-corner-triangle geometry on the all-edges-occupied event; two-dimensional integration of the binomial void probability; exponentially small failure probability for empty edges; joint convergence of finite disjoint shrinking boundary intervals to independent exponential waiting times; uniform all-order moment bounds; and the elementary exponential-integral identity for the Laplace transform. None of those universal steps is inferred from numerical output.

The claim is limited to fixed positive-edge-length convex polygons and independent uniform boundary points. Simulation tolerances are finite-sample sanity checks, not rigorous numerical error bounds for the infinite limit. Independent mathematical audit has not been performed.
