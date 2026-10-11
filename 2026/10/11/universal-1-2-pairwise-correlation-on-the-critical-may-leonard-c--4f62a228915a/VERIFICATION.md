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
# Verification notes

The analytic proof was replayed from the stated differential equations and hypotheses. The checks are:

1. On \(\alpha+\beta=2\), summing the three equations gives \(\dot u=u(1-u)\) for \(u=x+y+z\).
2. Invariance of \(\log u\) and \(u\) gives \(\mathbb E[u]=\mathbb E[u^2]=1\), hence \(u=1\) almost surely.
3. Coordinate-wise generator testing gives zero conditional mean of each per-capita growth rate. On \(u=1\), the first one factors as \((\alpha-1)(z-y)\), with cyclic analogues. Under \(\alpha\ne1\), the conditional equal-sharing laws follow.
4. The conditional laws imply equal coordinate means and equal second moments; direct simplification gives each pairwise covariance as minus one half of the common variance.
5. If the common variance vanishes, all three coordinates are almost surely \(1/3\); otherwise each Pearson correlation is exactly \(-1/2\).

The bundled `verify.py` checks the factorization and covariance algebra and produces `ALGEBRA_OK`. It does not attempt to certify measure-theoretic invariance, literature coverage, or any infinite computation.

Limits checked explicitly: compact support lies strictly inside the positive octant; \(\alpha+\beta=2\); \(\alpha\ne1\). No boundary, stochastic, spatial, or delayed extension is asserted.
