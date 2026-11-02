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

# Verification of the finite-path absorber identity

The exact all-dimension proof appears in `RESULT.md`. It relies on strict spectral stability and entrywise substitution into the Lyapunov equation, including finite-chain endpoints and the parity off-diagonals. No empirical finite-size check substitutes for these steps.

## Reproducible check

With Python 3, NumPy, SciPy, and SymPy installed, execute `python verify.py` in the extracted package directory. The implementation constructs the claimed kernel independently, builds the finite-chain generator, compares the kernel with a numerical Lyapunov solve, checks positive definiteness and localized-source optimization, and performs symbolic rational identity checks for lengths from \(2\) through \(8\).

The performed run printed exactly:

```
PASS: 1267 deterministic numerical and finite-size symbolic consistency checks
```

The accompanying `verification_output.txt` records that outcome. It is a finite analytical-consistency test, not an exhaustive infinite-\(N\) certificate. Exact symbolic entries are checked at fixed dimensions; arbitrary length is covered by the explicit commutator identity in the proof.

## Scope of evidence

The theorem assumes strictly positive hopping and loss, uniform finite open boundary conditions, and only one absorbing channel. The proof shows every eigenmode decays and hence all initial states are eventually absorbed. No independent mathematics or priority audit was undertaken.
