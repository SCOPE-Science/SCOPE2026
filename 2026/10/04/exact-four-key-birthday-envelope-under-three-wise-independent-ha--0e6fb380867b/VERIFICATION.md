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
# Verification

The proof is analytic. The standalone checker uses exact rational arithmetic. It verifies the symbolic endpoint laws for every integer \(q\) from \(4\) through \(5000\). For \(4\le q\le10\), it enumerates all \(q^4\) assignments, uniformizes each endpoint law within occupancy types, and checks every concrete three-coordinate marginal against \(1/q^3\). It also checks exact convex mixtures of the endpoint laws.

Replay result:

`VERIFY_OK symbolic_checks=4997 exact_assignment_checks=14 triple_tables_checked=23912 mixture_checks=485`

Finite replay does not prove the universal interval; the inequalities in `RESULT.md` do. Originality was assessed by statement-level comparison with the cited sources and the closest indexed occupancy result. Independent audit has not been performed.
