---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-18.md",
      "INDEPENDENT_AUDIT_2026-10-18.json"
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

Using P(A)=[1+cos(2theta)cos alpha]/2 and P(AB)=[1+cos(2theta)(cos alpha+cos beta)+cos alpha cos beta+sin(2theta)sin alpha sin beta]/4, substitute the source I3322 polynomial and M_A=P(A1)-1. Independent SymPy Taylor series in t=sqrt(theta) directly returned Q theta^2,theta^3,theta^4 coefficients 4/3,-25/9,-1/9 and M_A=-theta^2+(1/3)theta^4, then series division gave eta 3/7+25theta/49+562theta^2/1029. Independent symbolic expansion in the general six-parameter scaling produced q4=-(a^2 f^2+8af+6b^2-8b+6d^2+8d+4u^2)/16, equal to the displayed sum-of-squares form q4=4/3-(af+4)^2/16-3(b-2/3)^2/8-3(d+2/3)^2/8-u^2/4, with no c in leading order. Loss leading coefficient is 1+u^2/4; therefore q4/(1+u^2/4)<=4/3 with equality iff four conditions hold. Analyticity of trig expressions and theta>0 ensure the expansions and strict positive Q for sufficiently small theta. No claim of arbitrary-scaling optimality.

## originality

PASS

Best-of-knowledge PASS. An equivalent prior theorem must provide these same asymmetric qubit loss settings/limit or directly imply exact asymptotic coefficients and scaling-class equality conditions. Approximate numerical optimization does not constitute this exact analytic theorem. The two prior papers establish the optimization context, not this exact rational constructive limit or limited sharpness proof. The new theorem does not imply the stronger conjectural global lower bound. Residual priority/access caveats explicitly included; no search absence alone is interpreted as novelty.

## value

PASS

Supplies explicit analytic qubit settings and an exact rational constructive efficiency boundary where the original landmark asymmetric Bell loophole work had a numerical ~43% optimization, plus a sharp algebraic classification inside a motivated weak-entanglement scaling. Provides a concrete reproducible benchmark and clarifies its relation to later qudit construction, without overclaiming global qubit optimality.

The dated certificate retains the supplied scientific assessment, sources and limitations.
