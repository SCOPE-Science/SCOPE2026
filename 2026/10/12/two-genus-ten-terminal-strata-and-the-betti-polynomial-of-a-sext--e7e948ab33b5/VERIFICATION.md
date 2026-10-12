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

# Mathematical verification

The embedded standalone program `verify_sextic_quotient.py` was extracted from this record to a temporary execution path, run under Python, and produced `SEXTIC_QUOTIENT_EXACT_OK` with exit code zero. It checks the order-two transformation's defining-equation invariance in a symbolic sextic example, restriction to both eigenspace planes, the exact second-Veronese Hilbert-series coefficients and multiplicity \(4\), the top Chern number \(2610\), the genus-ten fixed-curve Euler characteristic \(-36\), the resulting fourth-cohomology trace \(-40\), and the quotient Betti number \(1283\).

Universal steps beyond computation are the projective eigenspace classification, smoothness-gradient argument, equivariant formal linearization in characteristic zero, generators/relations for the sign-invariant formal ring, Reid–Tai criterion, anticanonical residue-character computation, rational transfer and topological Lefschetz theorem. Their hypotheses and usage are stated in RESULT.md. The finite symbolic tests do not constitute a proof for every sextic. No independent audit has been performed.
