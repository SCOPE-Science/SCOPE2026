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

The analytic check has four steps: the Pauli channel maps a Bell state to the Bell-basis probability vector \((1-p,p/3,p/3,p/3)\); the Bell-diagonal formula gives \(E_R=1-H_2(p)\) for \(0<p<1/2\); Bell-diagonal additivity gives \(nE_R\) for \(n\) copies; and LOCC monotonicity plus the admissible identity LOCC map gives equality for the post-channel supremum.

`verify.py` reproduces the numerical evaluation at \(p=0.2\) and checks the strict inequality between the identity value and an exponentially damped candidate ceiling. Floating-point output is not used to justify the symbolic inequalities.

Limits: this verification addresses global relative entropy of entanglement under trace-preserving LOCC-after-channel maps. It does not analyze a distinct constrained distillation task that prescribes a smaller output space, target fidelity, success event, or rate normalization.
