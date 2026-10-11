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

The proof has two logically independent parts. First, evaluating the nonnegative polynomial at \(\theta=\pi\) and \(\theta=4\pi/5\) gives the exact universal upper bound \(a\le\sqrt5/2\). Second, the candidate at equality is proved globally nonnegative after the substitution \(x=\cos\theta\) by the exact factorization
\[
(x+1)(x-r)^2R(x),\qquad r=-\frac{1+\sqrt5}{4}.
\]
The derivative of \(R\) has negative leading coefficient and discriminant
\[
\frac{32}{25}(1063-477\sqrt5)<0,
\]
while \(R(1)>0\), hence \(R>0\) on \([-1,1]\).

`verify_exact.py` checks the coefficient identities, the Chebyshev factorization, the derivative discriminant, and the exact integer comparisons used for sign determination. No finite grid, numerical optimizer, or timeout is used to establish the universal theorem. The computation does not address other frequency supports or sampled cyclic problems.
