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
# Reproducibility and verification

The embedded `VERIFY.py` can be executed with `python VERIFY.py`; it uses Python 3, `sympy`, and `mpmath` for exact and high-precision arithmetic. The complete proof is contained in `RESULT.md` and does not depend on samples or a numerical convergence extrapolation.

The script checks the exact Pell norm \(p^2-2q^2=2\) and alternating nonzero residues modulo three for nine terms, checks the Hermitian perturbation matrix and its exact characteristic polynomial \(x^3-6x\), and evaluates seven Gram matrices using 90-digit arithmetic. It checks that their extremal eigenvalues are positive, their ratios exceed one, and their scaled errors approach the coefficient \(4\pi/(3\sqrt3)\) in a quantitatively bounded way for the displayed terms.

Not directly computer-certified: the inverse-function/compactness lemma on the two-torus, the global all-bandwidth lower inequality, and the all-\(R\) denominator-selection argument. Those are proved analytically in the result. High-precision eigenvalues are consistency evidence only. No independent audit has been performed.
