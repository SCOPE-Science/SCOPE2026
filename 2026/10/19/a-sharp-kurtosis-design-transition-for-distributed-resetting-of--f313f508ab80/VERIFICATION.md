---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

The backward age of the last reset is exponential, gives the unique stationary state, and bounds its fourth moment. In units of v/kappa for position and 1/kappa for time, the mixed balances are (1+q+g)E[XS]=1 and (3+q+g)E[X^3S]=3V, since the new sign has zero mean and is independent of reset position, even for asymmetric centered reset laws. Consequently V=(2/(q+g+1)+qx)/(q+2) and F=(12V/(q+g+3)+qy)/(q+4), where x,y are the scaled reset moments. At fixed x, variance is positive and Jensen gives y>=x^2, with equality exactly for equally weighted endpoints (point mass at zero for x=0). Writing V0=2/[(q+2)(q+g+1)] and s=1/V produces the strictly convex quadratic A+Bs+AV0^2s^2 on 0<s<=1/V0, with A=(q+2)^2/[q(q+4)] and B=12/[(q+4)(q+g+3)]-2AV0. With Delta=3-(q-1)(q+g), B has sign -Delta. For Delta>0, its vertex is interior: V_star/V0=(q+2)(q+g+3)/(2 Delta)=1+3q(q+g+1)/(2 Delta), giving x_star=3/Delta and the stated completed-square minimum. For Delta<=0, every positive s gives a value strictly above A, including at equality Delta=0. Only s tending to zero realizes the limit. Fixed-x three-point mixtures realize every larger value when x>0, and Delta=(2q_c+g-1)(q_c-q)-(q_c-q)^2 gives the claimed divergence. Frozen verify.py was inspected, not executed; several reset-balance residuals reuse the tested formulas, while the regenerative sampler is a separate finite diagnostic. No part of the proof needs those checks or a numerical certificate.

## originality

PASS

Pass applies to the global kurtosis optimization (including attainment and its critical boundary), not to the arbitrary-reset moment hierarchy. No inspected prior result covers the optimization or its threshold; the hierarchy is a starting point and does not by itself decide which admissible distributions attain the quotient minimum.

## value

PASS

This is a physically interpretable sharp design boundary, not just a forward calculation of kurtosis: for every allowed trap and switching/reset scale it determines whether finite optimal reset positions exist, identifies the unique admissible law when they do, and quantifies its loss at the threshold. The full range explains what can be achieved beyond the optimum. No claim is made about individual tail probabilities, different reset protocols, or support-constrained designs.

The dated certificate retains the supplied scientific assessment, sources and limitations.
