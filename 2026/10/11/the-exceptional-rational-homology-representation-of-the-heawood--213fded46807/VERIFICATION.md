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

# Reproducible finite checks

Invoke `python3 verify.py` and `python3 crosscheck.py` from the extracted package directory. The programs use only the Python standard library and encode independent finite definitions of the Fano incidence graph and its binary linear action.

The first program exhaustively checks all 16,384 subsets, the independent-set size counts, the six mod-two signed-chain boundary ranks, all 168 invertible matrices, both actions on the fourteen vertices, cycle-polynomial coefficients for each order, and the resulting character norms. Successful execution prints `VERIFY_OK`, the coefficient table, ranks and trace distribution.

The second program uses row-based matrix enumeration and directly oriented simplicial traces, rather than the cycle polynomial, and independently computes all mod-three signed-boundary ranks. Successful execution prints `CROSSCHECK_OK`, mod-three ranks and character distributions. Its result matches the first verifier.

The finite checks prove the finite character table and boundary-rank statements for the specified fourteen-vertex complex. The Hopf trace argument and the representation decomposition are mathematical steps stated in `RESULT.md`; a finite program alone is not an automatic proof of any unbounded graph-family statement. No integral equivariant homology-lattice or equivariant homotopy classification is claimed. External independent audit was not performed.
