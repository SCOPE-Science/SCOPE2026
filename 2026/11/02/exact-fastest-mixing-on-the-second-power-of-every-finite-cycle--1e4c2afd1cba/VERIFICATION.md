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
# Verification information

Run `python verify.py` with Python 3. If SciPy is available, the script also compares its explicit formula against a separately constructed linear program. Without SciPy, the exact small rational checks and all built-in numerical spectral checks still execute. The recorded run with SciPy installed reported `VERIFICATION_OK 1006259 assertions; exact n=5/6 and numerical n=6..1000, LP n=5..80`.

The exact rational boundary tests at \(n=5,6\) use `fractions.Fraction`. Other tests use standard floating-point trigonometry with explicit tolerances; they are not interval-arithmetic proofs or exhaustive checks over all dimensions. The universal mathematical justification is given by the Fourier/equioscillation argument and closed algebraic positivity factors in `RESULT.md`.

Independent audit has not been performed. No independent validation or external mathematical certification is asserted.
