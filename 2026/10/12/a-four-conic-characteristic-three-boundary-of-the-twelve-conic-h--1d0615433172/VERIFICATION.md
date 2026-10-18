---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-16.md",
      "INDEPENDENT_AUDIT_2026-10-16.json"
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

In the fixed Z[ω,t]/(ω²+ω+1) cyclotomic source model, reduction at char3 sends ω↦1. Direct substitution into all twelve published conic forms gives nine copies of D=x²+y²+z²+(t+1)(xy+xz+yz), with the three remaining components A=xy−tz², B=xz−ty², C=yz−tx²; product is −D⁹ABC. When char(k)=3 and t≠0,1 the Hessian determinants are (−t,−t,−t,1−t³), all nonzero, so the reduced support is four distinct smooth conics. Independently expanded at P=[t:1:1], z=1, x=t+u,y=1+v: A=u+tv+uv, B=u+tv−tv², D=(t−1)(u+tv)+u²+v²+(t+1)uv. On B, u=−tv+tv² makes A=tv³; D vanishes to exact order 2 there and on A because (t−1)²≠0. Hence pairwise intersections (A,B),(A,D),(B,D) at P have multiplicities (3,2,2), and coordinate permutations give two others. The three coordinate vertices are transverse nodes. Each pair of distinct conics already uses total Bézout intersection 4 across identified points, exhausting all geometric intersections, not extrapolating finite-field checks. Delta=3·1+3·7=24; arithmetic genus 21 equals δ−4+1. All six singular points have coordinates in the field containing t; the claim concerns reduced support, not nonreduced scheme. Critical exact symbolic identities independently corroborated from actual package paths.

## originality

PASS

The original Chilean 12-conic configuration paper explicitly works in characteristic ≠2,3; Dimca–Pokora–Sticlaru §5 lists complex cyclotomic forms and §6 degenerations in λ over characteristic zero. Neither treats the arithmetic specialization ω=1 at residual characteristic 3 or gives the resulting four-conic support and (3,2,2) local contacts. Coefficientwise source reduction is new geometric work, not simply changing the parameter λ; Resultary and targeted literature searches did not find a dominating all-t characteristic-three classification. Negative result not exhaustive priority certification.

## value

PASS

The excluded small characteristic is structurally natural: the cyclotomic third roots coalesce, collapsing nine of twelve distinct complex components. A complete singular-support and local-intersection classification is valuable for arithmetic degenerations of Halphen/Hesse conic configurations and for distinguishing reduced geometry from nonreduced specialization. Exact all-parameter structure is not a mere isolated arithmetic spot check.

The dated certificate retains the supplied scientific assessment, sources and limitations.
