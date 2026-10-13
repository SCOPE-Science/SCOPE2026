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

The proof is analytic and covers every finite dimension under the stated assumptions. The central algebraic checks are: conjugating the intertwining equation into the simple real eigenbasis; identifying every admissible metric with a positive diagonal weight; transferring the positive spectrum of \(\eta^{-1}\) to the scaled Gram matrix; and using the two vectors \(u_i\pm u_j\) to force the pairwise eigenvalue-ratio lower bound.

`artifacts/verify.py` is an independent finite replay of representative instances using only the Python standard library. It checks six two-dimensional overlaps, a broad family of nonoptimal metrics, ninety random higher-dimensional admissible metrics, the intertwining equation, the diagonal-Gram condition-number identity, and the pairwise lower bound. A successful run prints `VERIFY_OK two_dim_overlaps=6 general_trials=90`.

The finite replay is not an exhaustive proof. It does not test defective matrices, repeated spectra, indefinite metrics, or infinite-dimensional operators, all of which are outside the claim.
