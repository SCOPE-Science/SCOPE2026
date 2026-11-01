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

For a fixed successful-edge subgraph and one-generation infectivity, the infected generations are the directed source-distance layers, including the seed at t=0. If original peak=1, deleting the unique vertex at distance h disconnects every originally later layer, so no increase. If peak>=2 and a deletion raises it, a new layer of at least three people is needed. Layers 1 and 2 cannot gain new vertices because direct seed arcs persist and any new layer-2 vertex already lay at original distance 2. Thus a new layer of size >=3 must lie at distance>=3; it requires >=6 surviving vertices (seed, two intermediates, three targets), plus vaccinated vertex, hence n>=7. The explicit seven-vertex directed arcs (0,1),(0,2),(1,3),(2,4),(3,4),(3,5),(3,6), seed 0, vaccination 2 yield peaks 2 and 3 and final sizes 7 and 6. An INDEPENDENT complete census of all 2^7=128 contact-realization masks matches the k-by-delta table and exactly gives E[delta]=p^2(p^5-2p^4+3p^3-1), with unique root in (0,1) from derivative p^2(5p^2-8p+9)>0. Independently 32420 directed small-network checks corroborate but do not prove the universal n<=6 theorem.

## originality

PASS

Qualified PASS: the published vaccination monotonicity result concerns individual eventual infection probability, not maximum synchronous generation width. Epidemic-percolation network theory identifies deletion and paths, but its cited results do not give the sharp seven-vertex peak-amplification cutoff or the witness-specific exact polynomial. A generic BFS-width theorem under vertex deletion is the primary unresolved equivalent-formulation risk.

## value

PASS

The minimum population size for a counterintuitive intervention effect is a natural sharp extremal invariant of a simple exact epidemic model; the constructive witness plus exact probability threshold show how peak load can rise while infections fall. This is an independently useful boundary for interpreting network timing, without claiming clinical generality.

The dated certificate retains the supplied scientific assessment, sources and limitations.
