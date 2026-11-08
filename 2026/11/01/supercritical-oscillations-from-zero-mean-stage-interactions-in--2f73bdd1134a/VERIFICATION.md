---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-02.md",
      "INDEPENDENT_AUDIT_2026-11-02.json"
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

Read complete RESULT.md and symbolic verification source against pinned tree. Substitution establishes positive equilibrium E=(1,1,1,1) and 1^TM1=0. Exchange symmetry splits J into 2x2 J+ and J−, with p+(z)=z^2−tau z+u^2−4−2tau and p−(z)=z^2+(2d+2+w)z+4d+2w+u^2, tau=w−2d−2. For tau<0 p+ Hurwitz and p− always Hurwitz under u>2,d>u+2,w>0; for tau>0 tr J+>0. At tau=0 J+ has simple imaginary ±i sqrt(u^2−4), transverse crossing derivative 1/2, J− strictly left. The invariant species-symmetric plane is a center manifold; canonical scaling h=X,k=Y sqrt[(u+2)/(u−2)] makes frequency Omega, quadratic f,g. Recomputed standard planar Hopf quadratic derivative formula as l1=-du/[4(u+2)]<0; independent symbolic char-polynomial and exact l1 at u3,d6 return -9/10. Local Hopf, transverse stability and hyperbolic periodic-orbit persistence justify full 4D orbital attraction for sufficiently small positive tau, not global behavior. Stage-transfer d>0 keeps the positive orthant invariant at faces.

## originality

PASS

Best-of-knowledge PASS for the deterministic exact zero-aggregate four-dimensional Hopf threshold, canonical Lyapunov coefficient and full-system attracting branch; source literature gives stage gLV classes, random stability and numerical regimes, not this exact deterministic result.

## value

PASS

A concrete sharp nonlinear boundary in a natural finite-stage community class explains why vanishing aggregate stage interaction does not rule out persistent cycles. The exact Hopf coefficient is a structural counterexample/boundary for stage-aggregation intuition, and identifies robust positive full-system oscillations rather than simply an unstable equilibrium. Narrow deterministic example is independently motivated by this false inference.

The dated certificate retains the supplied scientific assessment, sources and limitations.
