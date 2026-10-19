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

The standalone `verify.py` uses the Python standard library only. Execute `python3 verify.py` in the directory containing this file and `verify.py`. It constructs the exact integer-scaled weighted Laplacian and an exact prime-field row basis for the Kalman Krylov matrix. It compares the resulting ranks with the closed formula in all 2,645 cases with \(4\le n\le48\), across five rational conductance choices per chord. It separately constructs the exceptional eigenvector with rational coordinates and checks \(Lx=4x\) and \(x_0=0\).

The script must print `PASS: 2645 finite-field Krylov-rank checks and exact rational resonance eigenvectors; n=4..48.`. A prime-field rank equals a rigorous lower bound on characteristic-zero rank, not necessarily an equality absent further information. Here the exhibited eigenvectors give the complementary upper bounds for the tested instances, and the analytic proof supplies the global result. No finite run is presented as an exhaustive proof for all cycle sizes or arbitrary real conductances.

There has been no independent audit or independent validation.
