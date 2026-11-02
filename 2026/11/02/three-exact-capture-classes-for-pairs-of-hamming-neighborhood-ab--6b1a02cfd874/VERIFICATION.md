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

# Reproduction and limitations

Run `python3 verify_two_ball_capture.py` with standard Python 3. It checks every energy shell at every center distance for dimensions 6 through 13 using two distinct prime fields, independently rebuilds Fourier restriction matrices for dimensions 6 through 9, and computes adjacency Krylov ranks for dimensions 6 and 7. The expected output is included in `verification_log.txt`.

The checks are finite arithmetic reproductions; the all-dimension result follows from the detailed affine-intersection proof in `RESULT.md`, not from extrapolation. No independent scientific audit has been performed. Positive detector rates, a finite homogeneous hypercube, and maximally mixed initialization are essential to the numerical capture-fraction formula. The general projection law is valid for any initial density matrix under the stated Hamiltonian model.
