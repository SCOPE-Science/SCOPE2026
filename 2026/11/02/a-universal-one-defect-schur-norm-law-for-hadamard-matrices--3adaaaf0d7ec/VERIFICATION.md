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

# Verification scope

The analytic proof rests on a normalized Hadamard block decomposition and matching Schur-multiplier lower and upper witnesses. The lower witness is a real orthogonal polar factor of a weighted sign matrix. The upper witness is a strictly positive Gram matrix with constant diagonal and an exact matrix-inverse identity. These are algebraic equalities for arbitrary existing Hadamard orders, not extrapolations from numerical tests.

The included `verify_hadamard.py` uses NumPy to construct Sylvester orders 4, 8, 16, 32 and independently Paley orders 12, 20, checks Hadamard orthogonality and the exact constant, verifies the witness and certificate with double-precision tolerances, and compares many perturbed weighted nuclear norms. The checker also compares exact closed-form identities over integer orders 4 through 200. Successful replay: 521 supplementary assertions. Reproduction: `OPENBLAS_NUM_THREADS=1 python verify_hadamard.py` (Python 3 with NumPy).

The checks do not constitute formal symbolic verification or exhaust all Hadamard matrices or all inputs. Historical priority against all published literature is not independently certified. The previously published order-four specialization is expressly excluded from the novel part.
