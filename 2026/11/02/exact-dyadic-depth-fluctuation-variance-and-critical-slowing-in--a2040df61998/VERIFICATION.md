---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-04.md",
      "INDEPENDENT_AUDIT_2026-11-04.json"
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

Conditional uniformity within dyadic bands under both maps and full band history induces the Markov level transition: k>=1 to k-1 with p and k+1 with q; from k=0, q to 1 and p reinject geometric J with Pr(J=j)=2^-j-1. Stationary PGF Pi(z)=d/((2-z)(p-qz)) yields mean p/d, Var=(1+7d²)/(4d²) and third moment. Check quadratic h(k)=k(k-1)/(2d) solves (I-P)h=k-p/d, including reinjection at k=0 using E[J(J-1)]=2. Martingale decomposition and geometric Foster drift establish stationary CLT; sigma²=2E[gh]-E[g²] reduces to displayed rational expression. At p=1 renewal to level0 remains ergodic, sigma²=6; at p=1/2 excluded because no stationary ac law. Independent SymPy identities checked PGF, boundary/interior Poisson equations, exact variance and critical scales (finite matrix numerics not necessary for infinite proof).

## originality

PASS

The Pelikan map and its dyadic Markov representation are known. The assessed contribution is an additive-time CLT for unbounded depth with exact Green-Kubo variance and a fourth-order critical divergence, not a relabelling of stationary level density or one-time variance.

## value

PASS

The rational Green-Kubo variance and precise d^-4 critical divergence identify a physically and mathematically natural time-additive observable. The contrast with d^-2 instantaneous variance provides a nontrivial quantitative critical-slowing law, not merely a routine CLT existence theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
