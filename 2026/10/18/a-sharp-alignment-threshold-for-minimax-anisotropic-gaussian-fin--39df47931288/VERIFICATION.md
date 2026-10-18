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

The attached `reproduce.py` uses Python 3 and NumPy and checks exact two-step second-moment identities, formula-based optimal covariance ratios against dense scalar grids, operator-Jensen symmetrization inequalities on randomly generated positive-definite examples, and one-step Gaussian simulations. Run with `python reproduce.py` after installing NumPy. The randomized diagnostic seeds are fixed and the source is self-contained.

Proof of the global minimax theorem is mathematical, from Gaussian Wick identities, the variational convexity of inversion, orthogonal group averaging, and exact minimization of positive-linear-plus-inverse-linear scalar expressions. The positive coefficient of the leading moment mode analytically proves the stability threshold. Numerical finite comparisons neither establish originality nor replace these arguments. Historical published results were compared on claim implications, with residual bibliographic uncertainty where complete full text was not accessible. No external audit or independent validation was performed.
