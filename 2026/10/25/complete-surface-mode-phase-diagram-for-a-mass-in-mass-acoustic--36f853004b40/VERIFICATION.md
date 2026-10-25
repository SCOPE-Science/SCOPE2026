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

The standalone `check_surface_modes.py` is self-contained given Python 3 with NumPy, SciPy and SymPy. Run `OPENBLAS_NUM_THREADS=1 python check_surface_modes.py`. It separately forms finite mass/stiffness matrices and compares their mass-normalized eigenvalues and surface-mode envelopes to the scalar secular roots for 40 distinct parameter sets, including threshold-separated one- and two-mode regimes. The run passed three symbolic identities, 40 finite-chain spectral comparisons, 40 predicted surface eigenmode matches and three quadratic edge-law tests.

The exhaustive infinite result is **analytical**, not computational: the bulk recurrence has exactly one decaying Bloch solution in each forbidden frequency interval, the free-end condition gives the secular function, its derivative is strictly positive away from poles, and interval endpoint signs provide necessity and sufficiency. Exactly at each threshold the candidate has nondecaying Bloch factor of modulus one, so it is not a point eigenvector. At the internal-resonator pole there is no nontrivial mode. Finite eigensolvers do not certify that spectral completeness statement.

No third-party independent audit has been performed.
