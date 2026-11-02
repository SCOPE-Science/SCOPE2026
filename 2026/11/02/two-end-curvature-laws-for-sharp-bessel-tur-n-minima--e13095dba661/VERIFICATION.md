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

# Verification record

The analytical argument is in `RESULT.md`. The critical nonstandard step is differentiated large-order turning-point asymptotics: the proof uses the complete Olver expansion for Bessel functions near the turning point, its complex-order extension, and Cauchy derivative estimates on the remainder. This is more than a numerical Airy limit. The small-order coefficient is deduced from the exact Bessel order derivative, Wronskian and stationarity identity.

Execute `python CHECK.py` with Python, SciPy and mpmath available. The script checks three nodal indices at small order, computes the Airy constants for three intervals, and checks large-order convergence. It is explicitly supplementary: finitely many floating-point evaluations do not prove signs for all real orders or all indices.

No proof-assistant certificate and no independent external audit are claimed. The analytically established statement does not decide uniqueness of an inflection point.
