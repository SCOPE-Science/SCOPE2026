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
The result is an analytical theorem, not an infinite assertion inferred from finite experiments. The derivative identity \(K'(v)=v/p(v)\) follows exactly from the completed square and the logarithmic/arctangent primitive. The passage-time expression is obtained by integrating the original-time velocity equation twice around each regular energy circle. Its asymptotic proof uses the integrable first two moments of \(F(t)\), not a numerical extrapolation.

The standalone script `tools/check_period.py` checks the symbolic Taylor series, the algebraic substitutions for both large-amplitude moment coefficients, the large-amplitude velocity skew and the identity behind positivity of \(C_{\alpha,\kappa}\). Requirements: Python 3 with SymPy; run `python tools/check_period.py`. The script verifies algebra and does not replace the dominated convergence proof.

A direct original-time quadrature for \(\alpha=0\), \(\kappa=1\) at amplitudes \(A=10,20\) agrees with the coefficient \(C_{0,1}=\log 2\) to the indicated asymptotic order. These finite numerical samples are neither the proof nor a certified bound at arbitrarily large amplitudes.

Limitations: fixed \(\Delta>0\), \(\kappa>0\); no claim on degenerate boundaries, parameter-uniform remainder, or the number of interior critical periods. The local Taylor coefficient is established prior work. No independent audit has been performed.
