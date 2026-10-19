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

# Reproducibility

Run `python3 verify_five_tone.py` from the directory containing the embedded files. The checker requires Python 3 standard library only. It verifies the exact rational polynomial identity
\(1-4s+8s^3=(2s-1)(4s^2+2s-1)\), compares the direct five-Gaussian-mode formula with the hyperbolic factorization, checks all four predicted zeros in representative scales from all three open regimes, and checks zero first derivatives with nonzero second derivatives at both collision scales. Its completed run reported 2,109 supplemental comparisons and the transition values 0.33214123513398 and 0.43232515622947.

These finite floating-point checks confirm internal consistency but do not prove absence of zeros on an infinite domain, completeness, exact multiplicities, or historical novelty. Those conclusions rely on the analytic quartic argument, positivity at \(\cosh w=\pm1\), and the inverse-cosh classification in RESULT.md. Independent validation has not been performed.
