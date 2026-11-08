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

PASS: For delta>0,r>0 and h(u)=u^2 e^-u on u>=0 (0 otherwise), Q=h(t)+r h(t-delta). On 0<t<delta derivative=t(2-t)e^-t. After the second pulse x=t-delta,k=r exp(delta), derivative has sign of P=-(1+k)x^2+2(1+k-delta)x+delta(2-delta), with discriminant 4[k^2+(2-delta^2)k+1]. For delta>2, two additional simple positive roots occur iff k>(delta^2-2+delta sqrt(delta^2-4))/2, giving exact two-peak iff r>R(delta); boundary double-root is a shoulder, not second max. For delta<=2 one strict max including delta=2 equality. Log differentiation gives R prime/R=-1+2/sqrt(delta^2-4), hence strict rise to 2sqrt2, fall thereafter, and a genuine bimodal–unimodal–bimodal interval of fixed r between exp(-2) and peak. Independently reconstructed derivative polynomial, root criterion, phase examples delta=2.01/3/5 for r=1/5 using exact rational and high precision calculations; general proof is analytic.

## originality

PASS

PASS, best of knowledge and limited to the exact three-stage common-kernel shifted-pulse specialization. Dosla 2009 provides substantial general two-mixture modality theory including gamma examples; the inspected full text applies as a conceptual predecessor, but its gamma specializations use common origin and differing rates/shapes and do not contain this translated identical Erlang-3 explicit threshold and nonmonotone lag phase. Hydrology papers concern gamma pulse stochastic streamflow or different advection models. A general mixture criterion may yield the new formulas after an elementary computation; residual priority risk explicit.

## value

PASS

PASS: Count of hydrograph peaks under two separated positive inputs is an immediate, physically motivated shape invariant of a canonical three-reservoir linear response. The exact entire (delay,volume ratio) phase diagram, all equality shoulders and unusual two–one–two reentrance are meaningful mathematical predictions, not just a single fitted example or an arbitrary numeric slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
