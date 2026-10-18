---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
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

For the specified symmetric two-mutualist one-substrate Monod system, total mass obeys a linear dissipative bound and the log biomass ratio satisfies d/dt log(x1/x2)=f(S,x2)-f(S,x1), opposite in sign to x1-x2. This rules out nonsymmetric interior periodic orbits and forces equal biomasses at positive equilibria. On x1=x2=x, solving f(S,x)=d yields a strictly convex scalar feed S_in=H(x) with one nondegenerate minimum and 0,1,2 equilibria. The antisymmetric Jacobian eigenvalue is -u where u=xf_x in (0,d); symmetric trace=-D-v+u, determinant=dv-Du, v=2xf_S. Positive determinant and trace>=0 would force (d-D)u>dD, impossible if d<=2D. Thus upper branch stable and no spectral Hopf for d<=2D. For each d>2D an explicit one-parameter positive Monod family has positive determinant, zero trace and nonzero trace derivative, proving spectral Hopf feasibility. At exact (D,d,Sin,K,L,m)=(1,5,11,3/5,19,160) the anti eigenvalue is -19/4, planar pair ±i sqrt(14); an independently reconstructed cubic Hopf normal form gives l1=-40879/532480<0 and transversal stable positive cycles for K<3/5 near threshold with m=100(1+K). Dulac factor 1/(x f) in the symmetric plane gives strictly negative weighted divergence for d<=D, excluding all positive nonconstant periodic orbits. No assertion of absence of large cycles for D<d<=2D.

## originality

PASS

The initiating Mtar–Fekih-Salem model and generic equilibrium Routh–Hurwitz criteria are prior science, including d=D mortality-free special case. Exact common-removal d>2D feasibility threshold, symmetric-ratio global obstruction, parameter-uniform crossing construction and certified nondegenerate rational Hopf example were not found as stated in the primary source sections inspected. Those generic criteria imply some local algebra after specialization but do not immediately deliver the all-parameter sharpness and cycle witness without the new argument. Risk: a more general Hopf feasibility theorem may implicitly imply part of the claim.

## value

PASS

Separates three mathematically distinct regimes—global nonoscillation at d<=D, local Hopf impossibility at d<=2D and constructive Hopf feasibility above 2D—and supplies an exact supercritical stable-cycle witness. This resolves a genuine interpretation gap in a motivated chemostat model rather than merely substituting equal parameters.

The dated certificate retains the supplied scientific assessment, sources and limitations.
