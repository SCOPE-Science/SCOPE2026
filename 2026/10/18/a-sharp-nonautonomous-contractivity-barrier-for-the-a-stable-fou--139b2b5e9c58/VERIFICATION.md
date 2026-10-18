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

Run `python verify.py` with Python 3 and SymPy available. The program reconstructs all coefficients with rational arithmetic and computes the original method's scalar affine-decay stage matrix inverse. It checks the stage determinant, both unit-circle-crossing factorizations, derivative of the crossing cubic, isolating signs at parameters \(24\) and \(25\), exact output at \(25\), and the large-damping asymptotic. It derives the Gaussian tableau independently through exact Lagrange integration, checks all nine symplectic/algebraic-stability identities, and proves equality of both autonomous rational stability functions to the \([3/3]\) Padé approximant.

The actual execution completed successfully with output beginning `PASS: exact nIRK4 table, stage determinant, sharp scalar frontier` and reported \(a_*=24.42686781215640\), \(R_{\mathrm{var}}(25)=-346/329\). Finite rational-parameter checks and finite-precision Gaussian checks are not exhaustive. The mathematical proof of all-parameter stage invertibility, root uniqueness, sharp nonexpansivity and Gaussian contractivity appears in RESULT.md. No external or independent audit is claimed.
