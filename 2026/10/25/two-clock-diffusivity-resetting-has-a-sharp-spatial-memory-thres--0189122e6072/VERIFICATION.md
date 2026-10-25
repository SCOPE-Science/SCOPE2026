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

The exact symbolic checker is `verification/checker.py`; run it with Python 3 and SymPy. The recorded output in `verification/checker_output.txt` was produced by executing that checker with its actual program text.

Generator identities: stationarity of medium-square, medium fourth power, position square, position fourth power, medium–position mixed fourth power, and two-coordinate mixed squares. Independent check: the medium-square stationary autocovariance equals \(20\Lambda^4 a^{-2}e^{-a|t|}\). Conditional on the independent exponential time since the last position reset, a two-fold integral yields \(\mathbb E Z_t^2=M\). These agree with the Markov generator's mixed moments.

Time-lag check: the exact ODE \(K'(t)+bK(t)=2He^{-at}\), initial condition \(K(0)=V\), and its repeated-rate \(a=b\) limit were symbolically verified. Conditional Gaussian fourth moments separate the self-covariance contribution \(2Me^{-bt}\) from the cross-covariance. For all strictly positive parameters, the integral kernel implies strict positivity and increasing cross-to-self ratio. The \(a>b\) rational limit was derived algebraically from the finite integral. The checker also performed 72 positive-parameter/lag comparisons, which are numerical supplements, not proof of all-parameter claims.

This verification concerns only the exact two-clock model. It does not prove independent scholarly priority, a finite-sample statistical estimator, a uniform-in-time law of large numbers, or analogous claims for general waiting-time distributions.
