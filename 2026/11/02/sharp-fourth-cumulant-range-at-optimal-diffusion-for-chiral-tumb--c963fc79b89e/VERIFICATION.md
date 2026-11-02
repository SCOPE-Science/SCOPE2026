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
# Verification and limitations

- Execute `python verify.py` using Python 3 with SymPy and mpmath. The embedded checker ran successfully on the stated exact examples.
- Symbolic equalities verify the principal-eigenvalue fourth-order coefficient and its optimum simplification.
- Exact rational laws (half-turn, symmetric quarter-turn and symmetric one-sixth-turn) verify the first and second angular Fourier modes, optimal rates and cumulants.
- Nine Fourier modes, independently diagonalized at high precision, reproduce the fourth-order Taylor coefficients within absolute error \(1.5\times10^{-6}\) at all three cases. These are finite spectral diagnostics, not a proof for arbitrary parameters.
- The analytic proof in RESULT.md establishes the infinite-time cumulant rate through the isolated eigenvalue of the tilted elliptic angular generator, then proves the sharp interval with an exact weighted measure inequality.
- The upper endpoint is not attained; it is approached by paired small-angle reorientations with increasing optimal rate. The theorem does not concern finite-time cumulant sign, nonsymmetric jumps, low chirality, correlated tumbles, or interactions.
- Independent scientific audit has not been performed.
