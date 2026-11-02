---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Reproducibility and boundaries

Run `python3 verify.py` using Python 3 with its standard library only. This constructs the triangular graphs from original pair-intersection adjacency, enumerates all minimum-cardinality candidates at \(n=4,7\), checks every vertex's open neighborhood, constructs both exchange and slide graphs by testing all replacements, and checks component counts, valencies and edge totals. For \(n=10,13,16\), it directly verifies open-neighborhood domination of a canonical configuration and independently enumerates its valid replacement neighbors.

Actual execution produced `EXHAUSTIVE_OK 4 12`, `EXHAUSTIVE_OK 7 630`, `CANONICAL_OK 10`, `CANONICAL_OK 13`, `CANONICAL_OK 16`, and `VERIFY_OK`. For \(n=4\), the exchange and slide graphs have respectively \(36\) and \(24\) edges; for \(n=7\), respectively \(3780\) and \(2520\). No probabilistic steps or external packages are used. These finite checks do not assert exhaustive verification for all orders, nor an independent mathematical audit.
