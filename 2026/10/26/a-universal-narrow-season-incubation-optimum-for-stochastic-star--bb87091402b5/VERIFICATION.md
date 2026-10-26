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

# Verification of the single-window optimum

Execute `python verify.py` from a directory containing the supplied script. The program requires only Python's standard library. It separately numerically solves the forward equations of the finite Markov epidemic, rather than reusing the conditioning formula for that comparison. It checks four tail-utility thresholds at four positive incubation rates, derivative signs around each numerical optimum, strict improvement over the immediately infectious limit, and approach to the analytic short-window value. It prints `CHECK_OK` only if all assertions succeed.

The proof is in `RESULT.md`: the central correctness certificate is the exact representation \(F_U'=B-A\), the strict increase of \(A/B\) from below to above one, and the limiting probability-measure argument. The numerical code is finite and has quadrature and Runge–Kutta truncation error; it is corroborating evidence rather than an exhaustive or formal verification of the continuum theorem. Rates \(\beta,\gamma\) must be positive and the pulse must satisfy \(0<a<b\). Independent validation has not been performed.
