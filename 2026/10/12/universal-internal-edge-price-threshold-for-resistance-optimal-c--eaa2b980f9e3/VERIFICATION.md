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

# Verification

Run `python3 check_bouquet.py` using Python 3 and only the standard library.

The script calculates exact grounded-Laplacian inverses for 217 rationally weighted clique-bouquet instances and verifies the exact Kirchhoff-index decomposition. It then checks 700 heterogeneous positive-price instances for budget normalization, the proposed objective, and derivative or endpoint optimality conditions. It also tests 2,100 randomly selected nonsymmetric feasible conductance vectors using a separate numerical inverse routine; these comparisons are diagnostics, not exhaustive optimization certificates.

A successful run reports `VERIFY_OK` and the counts. An observed run yielded:

`VERIFY_OK 217 exact Laplacian-inverse Kirchhoff identities; 700 heterogeneous optimal allocation/budget/stationarity checks; 805 retained and 936 deleted internal-edge cases; 2100 feasible nonsymmetric numerical comparisons`

The general assertion is proven by the electrical series law at a cut vertex, exact Laplacian modes on each weighted clique, single-variable minimization, and equality in Cauchy--Schwarz. Finite checks alone do not prove any infinite family, and machine floating-point comparisons do not certify exact inequalities outside the analytic proof. No independent audit has been performed.
