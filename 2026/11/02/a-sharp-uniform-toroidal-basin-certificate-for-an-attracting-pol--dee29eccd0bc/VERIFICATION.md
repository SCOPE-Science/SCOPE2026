---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-03.md",
      "INDEPENDENT_AUDIT_2026-11-03.json"
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

The edge values P(4-delta,(4+delta)/10)=delta(25delta-11), P(4+delta,(4-delta)/10)=delta(25delta+11) show all four Nagumo signs. The only equilibrium in the box is (4,2/5) (q=1 outside); trace J=-344 mu-1, det J=600 mu. Divergence=-1-2mu E, E>=36957/625, so Bendixson and Poincare-Bendixson yield full convergence to the unique sink. At delta>11/25 the upper-left qdot<0. An independently recomputed exact polynomial check agrees. The primary 3D source writes mu_orig/21 for the coefficient; unrestricted positive mu makes this a harmless reparametrization, not identical original parameter notation.

## originality

PASS

The source 2026 cyclic-field paper provides the underlying circular periodic orbit and its local attraction; the assessed addition is a positive-volume, mu-uniform explicit basin tube and sharp cutoff within a defined nullcline-balanced rectangle family. The primary Theorem 1 does not itself assert such a rectangle. Full-document priority remains qualified, including other trapping-region methods.

## value

PASS

The motivating unusual attracting polynomial-field circle has local stability without an explicit nonlocal attraction region. The sharp 11/25 balanced, physically interpretable full-azimuth tube is a substantive natural family-wise certificate, not a general claim about the entire basin.

The dated certificate retains the supplied scientific assessment, sources and limitations.
