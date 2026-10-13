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

Execute `python3 verify.py` with `COVARIANCE_MATRIX.json` beside the script. The checker reconstructs all overlap counts in the symmetric groups of orders 4, 5, 6 and 7; verifies the entire stored integer covariance matrix; checks the exact six-dimensional annihilating subspace; computes its modular rank and the 18-by-18 principal determinant residue 897856 (mod 1000003); and checks all 24-by-24 finite covariance entries for each permutation order 4, 5, 6 and 7 by direct exact enumeration. All computations use integers and standard Python only.

The finite matrix certificate proves the exact covariance rank/kernel because the modular minor cannot vanish as an integer. The finite exhaustive tests corroborate the full covariance formula, but the general Gaussian convergence is analytically justified by 3-dependence and Cramér–Wold, not by a finite test. Historical priority and any external or independent certification are not established by this program.
