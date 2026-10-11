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
The arbitrary-positive-weight proof is given in `RESULT.md`.

Critical checks:
- the generic minimum-enclosing certificate is center-in-convex-hull of contact points plus containment;
- for base-only contacts, equal squared distances imply \(c_i=(b_i^2-\mu)/(2b_i)\);
- positive base weights are \(\frac12(1-\mu/b_i^2)\), forcing a sorted tail and fixing \(\mu\);
- the apex squared-distance excess is exactly \(\kappa_B-\mu\);
- if the apex is active, equal apex/base distances give \(b_i^2-2b_ic_i=K\);
- the apex weight and \(K\) satisfy the two displayed linear equations, whose solution is \(t_p,K_p\);
- active-base positivity and inactive-base containment are respectively strict and weak versions of \(b_i^2+2at_pb_i>K_p\);
- monotonicity in \(b_i\) forces a tail support;
- the positive contact weights sum to \(1\), so the weighted parallel-axis identity proves global optimality and center uniqueness.

`verify.py` uses exact rational arithmetic on deterministic integer-weight families in dimensions \(2\) through \(7\). It compares the closed tail formula with an independent generic enumeration of every possible contact subset, solving the contact barycentric equations from scratch and checking containment. The finite enumeration is corroborative only and does not assess originality.
