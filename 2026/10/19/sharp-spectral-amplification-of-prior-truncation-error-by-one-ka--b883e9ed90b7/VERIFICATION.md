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

Run `python verify_covariance.py` with Python 3, NumPy and SymPy. The verifier symbolically checks the two-mode posterior subtraction, rank-one factorization and exact amplification identities; performs rational arithmetic on a nontrivial positive-noise witness; and checks PSD order, sharp upper bounds, convergence to the supremum and the aligned-sensor bound across dimensions two through seven.

The tests consist of 385 deterministic assertions. They support but do not certify the general proof, which follows from the variational characterization of Gaussian conditioning, a spectral upper bound, and an explicit limiting one-sensor construction. The supremum requires a limiting sensor family; the verifier never treats finite sampling as a proof of universal sharpness. Independent audit is not performed.
