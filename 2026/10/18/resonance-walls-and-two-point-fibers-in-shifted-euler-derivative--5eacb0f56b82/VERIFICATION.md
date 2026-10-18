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

# Reproducibility checks

Execute `python checks/verify.py` with Python 3 and NumPy. The program uses exact rational complex arithmetic for the Laurent-square identity, finite-degree reciprocal-conjugate equalities, the top harmonic, and a nonresonant detuning witness. It checks degrees 1 through 8 and carries out 48 numeric profile reconstructions from distinct, nonequispaced circle samples, using linear algebra to reconstruct the Fourier coefficients. The recorded output in `checks/output.txt` is the actual execution result and contains 105 exact checks, 48 reconstructions, a maximum coefficient error of approximately \(1.14\times 10^{-13}\), and `PASS`.

The general uniqueness and all resonance boundaries are proved analytically in `RESULT.md`. Finite tests are corroborating evidence only. No independent scientific audit or independent validation is claimed. The proof does not establish conditioning or sampling-cardinality optimality.
