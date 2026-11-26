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

With h=1−c>0 the update is exactly V-gradient ascent with mobility diag(h,1). In scaled coordinates the Hessian is a diagonal cosine term minus b cos(2π(y−x)) vvᵀ, with v=(√h,−1) and ||v||²=1+h; hence its bottom eigenvalue is globally bounded below by −L. At L=2, equality in this directional lower bound for nonzero gradient would require alignment with v and both individual cosines −1, forcing the half-integer diagonal, where the gradient actually vanishes. Taylor's integral along each nonzero step therefore gives strictly positive ascent even at equality. The zero-displacement equations reduce, for sin(t)≠0 and r=b/a, to sin(u)=−hr sin(t), cos(u)=r(1+h cos(t)), so the unit-circle constraint fixes cos(t)=(r⁻²−1−h²)/(2h). It gives exactly two extra solutions if this value is strictly between −1 and 1, with the stated thresholds, and neither endpoint adds a distinct solution. The sin(t)=0 branch gives exactly the four grid points. In L≤2 the actual increments are each smaller than one, so there are no extra winding torus fixed points. Strict ascent and compactness put the limit set in this finite stationary set. Vanishing steps prevent transitions between separated small neighborhoods, first on the torus and then among distinct integer lifts. Finally, in the −L direction of the Hessian at the diagonal half-integer, the derivative multiplies by 1−L; the quadratic potential change is L²(2−L)||v||²/2 times the squared perturbation. This proves sharpness for this potential, not necessity for global convergence. The verification note and supporting code were inspected, not executed; their finite diagnostics are not used as proof.

## originality

PASS

The supported distinct contribution is global real-lift convergence with strict weighted-potential ascent on the closed region, and exact sharpness for that potential. The model, local flip phenomena, and the general Taylor descent method are antecedents, not novelty claims. The exact priority of the auxiliary four/six stationary census is not separately certified against the unavailable same-family full texts; acceptance does not depend on that census being new in isolation.

## value

PASS

For a model studied for periodic bifurcations, synchronization and chaotic dynamics, a rigorously gradient-like region for every unwrapped initial condition is useful, particularly at the neutral flip where the ordinary strict step-size estimate stops. The result supplies a computable exact potential boundary, distinguishes that boundary from a claim about all supercritical dynamics, and explains how limiting fixed-point choices change with the coupling.

The dated certificate retains the supplied scientific assessment, sources and limitations.
