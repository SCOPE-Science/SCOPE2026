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

Run `python3 verification/check_border_density.py` with Python 3 and NumPy. The verifier implements the finite forbidden-pattern prefix automaton independently of the border-polynomial formula. It computes the dominant eigenvalue and left/right eigenvectors to estimate the limiting one-density from symbol-labelled transitions; it separately computes the border imbalance polynomial. It checks the predicted direction (including exact balance within numerical tolerance) for 348 balanced words of lengths four, six, eight and ten that satisfy the theorem's hypothesis, and for the explicitly mixed-sign word `100011110001`. The recorded standard output in `verification/checker_output.txt` must reproduce.

Mathematical proof obligations, not settled by computation: irreducibility of the graph apart from four known exceptions; strict Perron domination of algebraic conjugates; the algebraic-integer argument excluding rational positive powers; the exact marked-border generating function and its derivative at the simple Perron pole; and the word-family proper-border classification. These steps are written explicitly in RESULT.md and draw on the cited primary texts. The tests use floating-point spectral computations and are not a proof of any infinite assertion. No independent audit has been performed.
