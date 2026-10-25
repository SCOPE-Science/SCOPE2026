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

# Verification of weighted edge projection formulas

Run `python3 weighted_edge_checker.py` with a standard Python 3 interpreter. The checker constructs vertex–edge incidence matrices for five balanced complete bipartite graph orders, with six strictly positive rational square-root conductances each, deletes one vertex coordinate, inverts the resulting weighted reduced Laplacian by exact rational Gauss–Jordan elimination, and compares every projector matrix entry against the analytical rank-one formulas. It checks 38,124 matrix entries, symmetric matrix entries, exceptional column norm identities, and exact uniform-weight endpoint norms. The output was:

`WEIGHTED_BIPARTITE_CERTIFICATE_OK matrix_entries=38124 dimensions=5 weights=6 asymptotic_parameters=71`

A further 71 integer graph orders were used to check the evaluated radical optimizers numerically. These tests **cannot** prove the theorem for all orders or all real conductances; that proof is the rank-one identity, Rayleigh maximization, and uniform ordinary-column bound in `RESULT.md`. The script is complete, standalone and uses no network or third-party dependencies. No independent mathematical audit or external verification is claimed.
