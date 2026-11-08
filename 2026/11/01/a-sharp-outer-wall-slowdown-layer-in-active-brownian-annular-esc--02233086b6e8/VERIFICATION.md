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

For D,D_rot>0, any fixed 0<α<1 and uniform heading, the backward generator gives Hβ A=h and (sBβ')'=−(sA)'/2 with Dirichlet conditions. Writing A=(h−wβ)/β, Hβ wβ=0 with wβ boundary h, yields exact Cβ=−(2Lβ)^−1∫wβ. Independent Bessel endpoint asymptotics give Cβ=−S/(2L)β^−3/2+O(β^-2), A'(1)=−h(1)β^-1/2+O(β^-1), and β^{5/2}Bβ(1−y/β)→Sy/(2L)+h(1)y²/4 locally with derivative. Algebra with α=e^-t gives S=(1+α)(sinh(t)−t)/(2t)>0 and h(1)<0; hence strict sign change and simple root y*=−2S/(Lh(1)). One independent two-boundary ODE numerical check was run at α∈{0.25,0.6}, β∈{80,640} using a separate implementation. It corroborates coefficient signs; uniform infinite-β follows from analytic proof, not finite checks.

## originality

PASS

Qualified originality PASS for the sharp, sign-changing β^-1 outer-wall susceptibility layer in a two-absorber annulus; derived O(Pe²) mean is not supplied by prior O(Pe) annulus result. Earlier work provides the PDE and Bessel tools, so no general first-passage novelty is asserted.

## value

PASS

Sharp wall-scale sign reversal is a physically motivated boundary phenomenon: the standard fast-rotation effective diffusion predicts decreased mean exit time at fixed interior points, yet the exact weak-propulsion susceptibility increases arbitrarily close to the outer absorber. Explicit β^-1 scale and local root separate this from the β^-1/2 angular resolvent layer; this is not a mere parameter substitution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
