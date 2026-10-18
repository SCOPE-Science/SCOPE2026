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

Directly reconstructed conditional moments of z=x-s C x_{k-D}; the explicit positive quadratic V=(1+ps)x²-2psxy+p vartheta s²(1+ps)y² has exact conditional drift s[vartheta(s+p s²)-2]x². For p>0, determinant p s²[vartheta(1+ps)²-p]>0; summable E[x_k²] gives sufficiency, while nondecreasing positive E[V] rules out convergence at and above equality. At p=0 the unused lag coordinate drops out; independent symbolic polynomial check agrees. Two-point curvature (.5,1.5), p=.5, s=1.2 gives lhs 2.4, versus 1.5 without lag and 1.92 without variability. Verification is a consistency check, not the proof.

## originality

PASS

The contribution is the coupled sharp p-vartheta stability boundary and exact mixed-noise synergy, not the generic second-moment lift, the no-lag SGD bound s<2/vartheta, or fixed-coefficient random delay stability. Inspected earlier stochastic-delay and stochastic-gradient references address different combinations. Priority against unindexed older stochastic feedback recurrences is not absolute.

## value

PASS

A complete necessary-and-sufficient threshold for a natural minimal model of asynchronous, heterogeneous interpolating SGD distinguishes two individually stable mechanisms that jointly destabilize. Explicit energy and exact strict boundary can be reused in analyzing step-size choice and limits of naive separately sufficient criteria.

The dated certificate retains the supplied scientific assessment, sources and limitations.
