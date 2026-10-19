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

Run `python verify.py` with Python 3 and NumPy. The program constructs the additive fields for orders \(2,3,4,5,7,8,9,11\), evaluates the window over each coordinate cross, and counts all time-frequency ambiguity entries with a numerical zero tolerance of \(10^{-8}\). It checks the stated closed-form flat and optimal rank expressions. For every even-characteristic field it independently checks every predicted kernel label against the explicit trace criterion. For \(q\in\{2,3,4\}\), it also constructs the dense projector Gram matrix and compares its numerical rank to the independent ambiguity count.

`verification_output.txt` records the program's successful stdout. The finite checks do not constitute a proof for arbitrary prime powers; the algebraic proof in `RESULT.md` supplies that proof. The code does not test nonlinear phase retrieval, unrelated windows, or all potentially equivalent published results.
