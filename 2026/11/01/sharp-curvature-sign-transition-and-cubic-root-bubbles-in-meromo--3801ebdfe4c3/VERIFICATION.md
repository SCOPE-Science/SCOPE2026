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

# Verification and limits

The Laurent monomial norms and generating function were derived directly. With \(x=|z|^2\), the metric coefficient is \(g=2/(1-x)^2+c/(1+cx)^2\), and the Gaussian curvature convention is \(-2g^{-1}[(\log g)'(x)+x(\log g)''(x)]\). The attached `checker.py` uses exact symbolic rational arithmetic to compare this expression with the polynomial expression in the proof, verifies the limiting curvature at the puncture and the kernel numerator identity, and checks rational examples on both sides of the sign threshold. Run with `python checker.py` in an environment with SymPy available.

The global one-zero result rests on the positivity of every nonconstant coefficient of the explicit polynomial, not numerical root enumeration. The transition exponents follow from Taylor expansion and a locally uniform rescaling limit plus monotonicity. A finite checker can confirm algebra but does not independently establish historical priority, infinite-dimensional Hilbert-space completeness, or asymptotics. Independent audit has not been performed.
