---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-07.md",
      "INDEPENDENT_AUDIT_2026-11-07.json"
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

For a planar SPD eigenbasis orbit A_theta=R_theta diag(1,epsilon)R_theta^T, a single fixed projective-isotropic probe has relative squared Frobenius error E_theta=[cos^2(phi-theta)+epsilon^2 sin^2(phi-theta)]^-1. For 1<=x<epsilon^-2, the set of phi passing all theta on the arc has projective length (2 arccos(sqrt((1/x-eps^2)/(1-eps^2)))-Theta)_+; hence exact CDF (q_epsilon(x)-Theta/pi)_+, atom min(Theta/pi,1) at the worst value. Integration over projective angles gives E Z_Theta=Theta/(pi epsilon^2)+2/(pi epsilon) arctan(tan((pi-Theta)/2)/epsilon) when Theta<=pi and epsilon^-2 beyond. Independent preassigned probes on K blocks multiply independent probabilities; AM-GM gives equal-part optimum (q-t/K)_+^K. Strict negativity of f"(k) and Lambert-W root establish unique continuous optimizer and integer neighbors, with the t->infinity law. Independent angular quadrature, mean integral and optimization checks corroborated and treat Theta=0,pi boundaries.

## originality

PASS

Kressner and Lam investigate reused random dimension reduction for parameter-dependent matrices but their uniform estimates in the inspected theorem require oversampling and are not the exact one-probe planar worst-parameter distribution/atom. Halko-Martinsson-Tropp and Epperly-Webber bound or characterize fixed-matrix errors, not this joint shared-probe arc law or independent-refresh optimum.

## value

PASS

This exact model isolates a real uniform-in-parameter instability of reusing a Gaussian sketch: mean factor of order epsilon^-2 for fixed positive angular sweep versus epsilon^-1 at a single parameter. Optimal nonadaptive refresh density quantifies a practically motivated tradeoff, even though dimension two and one probe are restrictive.

The dated certificate retains the supplied scientific assessment, sources and limitations.
