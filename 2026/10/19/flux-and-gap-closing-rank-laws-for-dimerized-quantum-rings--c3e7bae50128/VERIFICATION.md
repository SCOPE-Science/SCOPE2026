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
# Finite verification and proof boundaries

Run `python verify.py` from this directory with NumPy installed. The code assembles 250 direct finite Hermitian matrices (orders 4 through 22), groups their numerical eigenvalues into distinct spectral projectors, and independently reconstructs the same projectors by two-band Bloch eigenvectors, checking entrywise averages, row sums, positivity, and the claimed ranks. Tested hoppings are `(1,1)`, `(1,2)`, `(2,1)`, `(2,3)` and `(3,3)` with fluxes `0`, `pi`, `0.37`, `1.7`, `4.6`, at each integer cell count from 2 to 11.

Observed output: `VERIFY_OK spectral_profiles= 250 matrix_entries= 50500 orders=2..11 max_entry_discrepancy= 7.772e-16`.

These are finite numerical tests and cannot establish the infinite family of ranks or discover all exact near-degeneracies. That unrestricted conclusion relies on the analytic cosine-collision equivalence, Fourier-frequency rank proof, and exact zero-mode Schur-square correction in `RESULT.md`. Numerical eigengap grouping uses tolerance `1e-8` and is not a certified exact arithmetic calculation.
