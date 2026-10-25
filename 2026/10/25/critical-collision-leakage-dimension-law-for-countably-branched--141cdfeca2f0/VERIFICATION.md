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

# Verification evidence and limits

The complete analytic proof is in `RESULT.md`. For every \(q>1\), \(0<\eta<1\), and \(s>1/q\), the critical finite/infinite weighted adjacency identity is \((Bv)_i-\lambda v_i=\sum_j r_j^s/(\lambda+r_j^s)-1\), where \(v_i=(\lambda+r_i^s)^{-1}\). At \(\lambda=1\) this yields the exact dimension root for the no-immediate-repeat survivor. The unrestricted and constrained roots are both bracketed inside \((1/q,1)\). As \(q\downarrow1\), both roots lie at distance \(o(q-1)\) below one; the two differentiable pressure functions have derivative asymptotic to \(-1/(q-1)\) on the intervening interval. Their respective deficits at the reference roots give the two stated limits.

`checker.py` runs with the Python 3 standard library. It tests the weighted adjacency identity in exact rational arithmetic, then approximates five cases using Euler–Maclaurin zeta sums and an alternating-series expansion. Its recorded output `checker_output.txt` ends with `NUMERICAL_DIAGNOSTICS_PASS`. The rational tests cover finitely many matrix sizes; floating-point tests are not interval-certified and cannot independently establish either infinite-dimensional or asymptotic conclusion.

No independent audit or external mathematical validation has been performed.
