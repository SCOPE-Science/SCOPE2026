---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
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

For the exact normalized two-species Ricker map, eliminate prey through x(y)=1+r^{-1}log(1-b(1-exp(-y-cy²))) and reduce strictly positive fixed points to R q(y)=1 on x(y)>0, R=beta*b. G(s)=s[r+log(1-bs)] has G′′=-b(2-bs)/(1-bs)^2<0 and G′′′=-b²(3-bs)/(1-bs)^3<0. On initial G′>0 interval P=-G′′/G′ is strictly increasing, while Q=s′′/(s′)^2=e^{y+cy²}(2c/(1+2cy)^2-1) has Q′=-e^u[((1+2cy)^2-c)^2+7c²]/(1+2cy)^3<0; independently reproduced all three derivative identities symbolically. Thus T=G(s(y)) has curvature changing at most once from + to -, and W=yT′-T, W′=yT′′, yields strict decrease of q when c<=1/2+b/r and exactly one nondegenerate peak otherwise. The endpoint limits q(0+)=1 and q(right end)=0 prove the entire R=beta*b regime table, including R=1 and the tangent at 1/qmax. The published example has two positive roots, but numerical samples do not prove this infinite-parameter theorem.

## originality

PASS

Best-of-knowledge new statement/implication after source-specific primary comparison and targeted published-record searches; residual priority and access risks are itemized below.

## value

PASS

A global sharp equilibrium census and nondegenerate fold for the precise Ricker/refuge/cooperative-hunting map settle an explicit geometric gap in the original same-model Proposition 3.2. Distinguishes beta*b=1 and threshold c=1/2+b/r without imposing r<2, which matters for interpreting bistability and possible positive stationary states. It does not assert dynamical attraction or persistence.

The dated certificate retains the supplied scientific assessment, sources and limitations.
