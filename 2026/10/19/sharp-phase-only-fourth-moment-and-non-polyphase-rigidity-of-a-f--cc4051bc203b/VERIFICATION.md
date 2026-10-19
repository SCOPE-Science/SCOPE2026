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
The standalone `checker.py` is a standard-library Python script that recomputes the 13 cross-difference autocorrelations, compares with the closed fourth-moment identity for 300 deterministic pseudorandom phase choices, verifies 60 independent Fourier averages on six nonaliased product groups, checks the algebraic two-component minimum in three ways and exhaustively verifies the q-phase minima for q = 1, 2, 3, 4, 6. The test program reported `PASS: 368 independent autocorrelation, discrete Fourier, optimizer, and phase-alphabet checks`.

The global inequalities and exact projective phase classifications follow from the displayed analytic deficit identity, not from numerical tests. No higher phase alphabets are claimed to have an exact optimal value; the proof only rules out attaining the continuous optimum. No independent mathematical audit has been performed.
