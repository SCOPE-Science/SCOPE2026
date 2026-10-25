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

# Verification

The analytic checks are the synchronous-Poisson \(W_1\) contraction, exchangeable degree-two generator closure, strict Metzler Perron eigenvalue necessity/sufficiency for finite invariant second moment, direct solution of the centered stationary equations, and differentiation/Taylor expansion of closed-form expressions. The threshold equalities include \(\varphi=0\) and all critical boundary values, where the second moment is infinite.

Execute `python3 VERIFY.py` with Python 3.9 or later. It uses the Python standard library only and deterministically checks the two independent (raw/centered) moment formulations, 2-by-2 determinant, covariance lock, zero-exchange independent reset case, sample means, and numerical Perron boundaries. The stored output in `VERIFY_OUTPUT.txt` reports 57,501 successful assertions. Finite checks alone do not prove the infinite-time claims. No external independent audit has been performed.
