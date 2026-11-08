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

For every a,b>=1, count-chain next states are independent binomial/monochrome given current majority signs. The two-step sign channel fixes strict signs and preserves a tie with probability q_a q_b<=1/4; two eventual strict signs are independent fair resolutions of initial ties. It follows there are just two monochromatic fixed points and one opposing period-two class. Conditioning one update by pure/mixed/tied probabilities yields the three given PGF equations and X,Y,Z expectations. G(q_a,q_b) is increasing; decreasing even central-binomial probabilities reduce global sharp 79/27 to nine explicit finite even pairs, attained only K_(2,6) with both parts tied. Fresh exact rational Bellman checks for 36 size pairs verified transient equations; those finite checks supplement the all-size argument.

## originality

PASS

Random-majority under independently fair synchronous tie coins is an existing studied model. Zehmakan previously derived C4=K2,2 random-cycle outcome statistics, a covered boundary case, but his general exponential stabilization and even-cycle results do not give the all-biclique exact distribution or 79/27 global maximum. Deterministic tie-resolution majority is a different Markov kernel.

## value

PASS

Exact probabilities, full finite-time law through rational PGFs, and a sharp universal expected absorption time for all nontrivial complete bipartite networks are natural stochastic-dynamics observables; precise attainment at K2,6 is a structural bound, not a routine reformulation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
