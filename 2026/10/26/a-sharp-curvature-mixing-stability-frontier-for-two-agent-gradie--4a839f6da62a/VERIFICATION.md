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

# Reproducibility and evidence

Run `python VERIFY.py` with SymPy and NumPy installed. The bundled `CHECKS.txt` contains the output from executing that exact script.

The script checks symbolically: the characteristic polynomial of the exact reduced matrix, \(p(1)=(1-\lambda)^2\), \(-p(-1)=1+\lambda^2-2\lambda d^2\), the remaining strict Schur quantity \(J\), the cyclicity determinant \(\lambda-1\), and reconstruction of all transformed state updates directly from the original two-agent equations. It additionally checks selected numerical eigenvalue radii on either side of the transition.

Proof beyond automation: the classical cubic Schur reduction is reconstructed explicitly in RESULT.md; its inequalities are reduced to a single quadratic in \(u=d^2\); positivity at both ends and strict decrease for negative \(\lambda\) classify every admissible parameter. The unit-circle factorization establishes equality failure. The finite numerical diagnostics do not prove the universal theorem.

Scientific limits and literature-access caveats are stated in RESULT.md and REVIEW.md. No external independent audit or independent validation has been performed.
