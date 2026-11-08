---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-05.md",
      "INDEPENDENT_AUDIT_2026-11-05.json"
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

Stationary two-state transition has nonconstant eigenvalue rho, hence P(all selected zero)=u product(u+p rho^gap). Enumerating all 15 labeled set partitions reduces to 4-pool, optimized 3+1, optimized 2+2 and singletons; 2+1+1 is dominated by 2+2 or all singletons according as u*A2 crosses 1/2. For rho<0, gap-two maximizes each factor and 2b-a-c=-p*rho*(1-rho)^2>0; positive-rho 2+2 is dominated by the 4-pool or singletons (including rho=0 boundary). Exact rational witnesses verify each negative-rho open phase; for a single h-pool n>=2h-1, the factor maximum is uniquely gap2 for negative rho and gap1 for positive rho. Independent script exhaustively enumerated 15 partitions at rational feasible points, which supplements but does not replace this continuous proof.

## originality

PASS

Best-knowledge originality belongs to the exhaustive four-site Markov partition/negative-correlation geometry and the one-pool h-gap result. The classical Dorfman objective and correlated-testing efficiency formulas were explicitly not counted as new.

## value

PASS

A motivated exact combinatorial screening optimization: negative serial correlation can make noncontiguous parity pools optimal even when adjacent pools seem natural, and the four qualitative regimes have sharp parameter boundaries and attainable open phases. This is stronger and scientifically different from merely reporting a finite candidate minimum.

The dated certificate retains the supplied scientific assessment, sources and limitations.
