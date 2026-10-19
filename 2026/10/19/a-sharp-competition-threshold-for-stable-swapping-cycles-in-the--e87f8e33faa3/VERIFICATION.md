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

# Verification and reproducibility

Run `python3 verify.py` with Python 3 and no external dependencies. The program checks exact-rational expressions for the trace, determinant and two Schur factorizations of the swap-reduced Jacobian. It independently reconstructs swapping dynamics, compares the matrix eigenvalues to the predicted strict stability interval across a finite parameter grid, and samples the monotonic scalar functions. The latest executed run printed `VERIFY_OK` with **13,062** checks.

The computation is neither an exhaustive infinite proof nor an independent audit. The proof in `RESULT.md` establishes the quantified existence, unique parametrization, Schur-equivalent wedge and coupling cutoff analytically. Values on neutral spectral boundaries are deliberately not labelled asymptotically stable. The source's approximate numerical transition is comparison literature, not a certificate.
