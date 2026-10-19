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

# Reproducibility and limits

Run `python verify.py` with Python 3 and no external dependencies. The program computes exactly, with `fractions.Fraction`, all vertices of the reduced spectral linear program for \(3\le n\le11\), checks optimality of the displayed branch for multiple \(\theta\) and \(t\), constructs full matrices and explicitly checks eigenvectors for \(3\le n\le8\), and tests the critical-price family and exact budget inversion. The verified output was:

`VERIFY_OK 12885 exact rational assertions; n=3..11; full LP vertices, eigenspaces, budget inversion`

This finite test does not certify all integers \(n\), and it does not claim to establish novelty. The proof in `RESULT.md` supplies the algebraic argument for all \(n\ge3\) and real parameters in the stated ranges. Only the stated symmetry-invariant minimizers are uniquely characterized; no unrestricted uniqueness claim is made.
