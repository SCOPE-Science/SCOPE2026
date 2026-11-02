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

# Reproducibility and limits

The standalone `verify_floquet.py` was executed with Python and SymPy and produced `PASS: 12 symbolic exact identities, 999 exact Jury checks, 64 independent nonlinear derivative comparisons`. The exact identities cover the full matrix product \(M_sM_{4/5}^2\), its trace, determinant, scalar Schur tests, the precise \(s=7/64\) boundary, the initialized-line transversality expression, and the exact \(s=1/10\) eigenvalues. A separately implemented nonlinear APG2 map confirms the claimed derivative asymptotics at sampled parameters and small amplitudes.

The universal statements require, and are supplied by, the algebraic proof and classical local stable-manifold theorem in `RESULT.md`. The finite tests alone are not infinite proofs. The constrained projection is inactive near zero, but it can affect trajectories after a neighborhood exit; no statement about later global dynamics follows. No independent mathematical audit has been performed.
