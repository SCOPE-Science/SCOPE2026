---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-31.md",
      "INDEPENDENT_AUDIT_2026-10-31.json"
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

For lambda(t)=A/(t+a)+B/(t+b) the exact derivative of the apparent elasticity E=-t lambda’/lambda decomposes into two positive component saturation terms and a negative mixture-weight-change term. Minimizing the positive terms relative to pi(1-pi) gives a single quadratic y^2-(r-1)y+r<0, with r=sqrt(b/a), hence the sharp threshold b/a>(3+2sqrt2)^2=17+12sqrt2. At critical contrast the only stationary contact is horizontal and not a reversal; above contrast choosing A/B=sqrt(a/b) makes E’ negative at t=sqrt(ab) but positive near both endpoints. Exact symbolic differentiation independently reproduced all five coefficients of the quartic numerator, which has at most two positive zeros by Descartes’ rule, and the exact witness E’(10)=-41/4840 for a=1,b=100,A=1/10,B=1. Finite symbolic checks supplement the all-positive-parameter analytic proof.

## originality

PASS

The modified Omori law, magnitude-dependent offsets, ETAS branching sums and detection-induced apparent rates are established in earlier seismology. Shcherbakov–Turcotte–Rundle (2004) gives a magnitude-dependent c for a generalized single component; Helmstetter–Sornette (2001) studies an endogenous branching cascade. Neither inspected statement entails the universal two-coeval-simple-pole amplitude threshold or at-most-two-turning theorem. The mathematical equivalent is a sharp logarithmic-elasticity theorem for positive two-pole Stieltjes mixtures, which remains a genuine alternative-priority risk; best-of-knowledge PASS.

## value

PASS

Different characteristic times are natural in aftershock rate models. The exact minimal two-component threshold quantifies when summation alone can mimic rise–fall–rise changing apparent decay exponent, without changing either intrinsic exponent; the universal two-turning bound is a substantive structural classification with an explicit rational witness. It is not claimed to identify earthquake mechanisms or noisy-catalog detectability.

The dated certificate retains the supplied scientific assessment, sources and limitations.
