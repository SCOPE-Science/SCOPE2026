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

# Verification procedure and limits

Run `python two_ring_quadratic_verifier.py` from the directory containing the extracted package. Requirements: Python 3, SymPy, and NumPy.

The checker constructs exact Hermitian measurement rows for \(r=1/2\), \(s=1\), \(\phi=0\), \(\psi=\pi/4\), verifies rank eight and the one-dimensional diagonal kernel, and tests rank loss in two forbidden parameter configurations. It checks explicit non-equivalent signal ambiguities, the three Fourier-demixing formulas, a two-radius complex linear solve, an angular real linear solve across 1,500 seeded examples, and the two predicted angular singular values. The executable prints `VERIFY_OK` upon completion.

The general theorem, exact necessity and the seven-measurement lower bound are proved algebraically in RESULT.md, not inferred from finitely many examples. No external or independent audit has been carried out. The 2026 contextual source was not accessible in complete text; this limits the historical-priority assessment, not the elementary rank calculations.
