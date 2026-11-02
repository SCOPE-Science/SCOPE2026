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
# Reproduction and limits

The embedded checker uses symbolic exact rational simplification to reconstruct the spectral projectors and the exact coefficient identities, then expands the optimum-placement comparison at \(n=7\) to an explicit degree-13 polynomial with all positive coefficients. Exact evaluations at \(n=5\) and \(n=6\) certify the remaining cases. Further shifted-positive symbolic certificates cover the fixed-rate statement at \(n\ge8\).

Full-graph tests construct the vertices and hopping adjacency independently of the closed formulas for \(n=5,6,7,8,9\). Each of the two absorber geometries has a five-dimensional Krylov space, and all three positive loss rates \(\kappa=0.37,1.4,5.8\) agree numerically with the exact integrated-survival formula, yielding 30 physical-graph Lyapunov comparisons. These numerical checks do not substitute for the general symbolic proof.

Run `python check_triangular.py` using the dependencies in `requirements.txt`. See `PLACEMENT_CERTIFICATE.json` for exact integer sign data. Only conditional means on the absorbing subspace are finite, because the complementary dark population remains unabsorbed. No independent scientific audit or laboratory validation has been performed.
