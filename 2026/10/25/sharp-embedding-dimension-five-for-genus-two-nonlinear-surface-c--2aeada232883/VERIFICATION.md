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

# Mathematical verification

The exact proof is in `RESULT.md`. The coefficient identity follows from substituting \(y_U=t y_W/(1-t^{-2}y_W)\); it is an identity of formal series. The cancellation \(PS-QR\) has coefficient zero in order five and \(-z\) in order six. At the Weierstrass point, \(t^{3}z=x^{6}/f_{5}(x)=x+O(1)\), which makes the prescribed jets regular on the second chart. Recursive extension follows from the vanishing of \(H^{1}(C,\mathcal O_C(qp))\) for \(q\ge3\), not from computations.

Run `python3 verify.py` to reproduce the deterministic checks of the transition exponents, exact cancellation, and normal-form monomial generation through weight 100. Finite monomial enumeration is supplementary; the semigroup-generation argument applies to all degrees, and the complete-filtered-algebra lifting theorem supplies the infinite step.

The independently evaluated mathematical audit channel is not present. Historical priority, especially possible implicit coverage in the original 1962 construction, remains uncertain.
