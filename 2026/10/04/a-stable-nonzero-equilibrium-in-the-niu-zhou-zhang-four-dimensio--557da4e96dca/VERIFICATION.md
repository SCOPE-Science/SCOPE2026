---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-04.md",
      "INDEPENDENT_AUDIT_2026-10-04.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

Solving the printed equilibrium equations exactly gives y=-fx, z=b+cf=856/25, x=(b+cf)/(a(f+1))=428/1445, y=-5136/7225 and w=(fx^2+dz)/e=1432077728/18792225. Exact substitution vanishes. Expanding det(lambda I-J) at this point gives the primitive positive-coefficient quartic printed in the package. The nontrivial Routh–Hurwitz determinants recompute exactly as Delta_2=1850867402738339250 and Delta_3=23033184284619159659128251000, both positive; therefore every eigenvalue has negative real part. The approximate roots are consistent but unnecessary.

## originality

PASS

The exact open-access primary paper was inspected and states the opposite result: for the same E2 it prints eigenvalues -24.1106,-12.4377,-4.1019,+0.0501 and declares both equilibria unstable. Fresh Resultary search returns the submitted record itself plus corrections for other unrelated four-dimensional flows, but no prior correction of this Niu–Zhou–Zhang equilibrium. Thus the exact Hurwitz sign correction is not a corollary of the source and remains original to best knowledge.

## value

PASS

Changing the nonzero equilibrium from unstable to asymptotically stable changes the qualitative phase portrait at the parameter vector used as the pseudorandom generator: it creates an open steady-state basin that must coexist with any chaotic invariant set. This is a substantive dynamical correction with direct initialization/interpretation relevance.

The dated certificate retains the supplied scientific assessment, sources and limitations.
