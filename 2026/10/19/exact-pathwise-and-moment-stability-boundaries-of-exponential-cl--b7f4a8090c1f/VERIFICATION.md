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

The standalone numerical file `verify.py` was run with Python and the `mpmath` dependency in `requirements.txt`. It executed 39 high-precision quadrature, exponential-integral, first- and second-absolute-moment identity, threshold-sign and moment-cutoff checks; its complete terminal output is embedded in `verification_output.txt`. The special-function threshold was independently found by solving \(\operatorname{Ei}(z)=0\); the computed positive zero is \(0.37250741078136663446\ldots\), whose reciprocal is \(2.68451035082070765\ldots\). At \(\xi=1.2\), the independently calculated moment cutoff is \(p_*(1.2)=1.45320882793830844\ldots\).

The mathematical proof additionally uses analytical integration, iid strong law, law of the iterated logarithm, Borel--Cantelli and strict convexity of the log moment-generating function. Finite numerical checks cannot establish infinite-time almost-sure claims, uniqueness for all real parameters or historical originality. No independent mathematical audit has been performed.
