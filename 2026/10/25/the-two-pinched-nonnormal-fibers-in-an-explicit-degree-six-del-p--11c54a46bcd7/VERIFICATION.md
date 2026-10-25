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
The exact checker `verify.py` checks the blowup-model local equation \(z^2-u^2v\), its Jacobian scheme support \(\{u=z=0\}\) in characteristic zero, the normalization substitution \(z=uw,v=w^2\), and the opposite-chart normalization transition \(u'=uw^2,w'=1/w\). It checks the double-cover ramification factors and both Euler calculations \(4-2+2=4\) and \(4+2+2=8\). The checker does not infer global normalization, nonnormality, finiteness, or geometric uniqueness from numerical sampling. Those are justified in `RESULT.md` by the proper quasi-finite finite birational morphism and explicit chart covering.

A smooth generic fiber is the blowup of a smooth quadric at two distinct points, hence has Euler characteristic \(6\). Over the two discriminant values the normalization is \(\mathbb F_2\) and the conductor identifies its negative section with a rational curve through a degree-two map. Additivity gives Euler characteristic \(4\) for each special fiber, independently cross-checked against the blowup Euler number of \(X\).

This is an internal self-review, not an independent audit or a machine-formal proof.
