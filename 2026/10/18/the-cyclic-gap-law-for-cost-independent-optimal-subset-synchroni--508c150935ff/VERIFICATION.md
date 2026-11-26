---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

For nonsingletons put K=(n-1)alpha+beta and attach K(n-g)-alpha u to a directed gap of length g ending at u. A loss of one in g costs at least beta even with the largest possible advantage in u. Thus the unique minimizing gap has maximum g and then maximum u. Rotation preserves lengths and subtracts alpha from any contribution whose endpoint does not wrap; a wrapping endpoint instead increases the contribution by (n-1)alpha. Equality in the rotation inequality occurs exactly when the winner does not wrap. If n-1 is absent, b does nothing. If present, the incoming gap gains one and ends at 0, subtracting beta from its contribution, while the outgoing gap is removed if 0 is occupied and otherwise shortens with unchanged endpoint. No other contribution improves. Thus b is an equality move exactly when the winner ends at n-1; for the exceptional collapse {0,n-1} the potential is directly beta and the same conclusion holds, including n=2. Iterating gives a lower bound on every word. The equality path rotates the winner to n-1, grows it by one, and then repeats a^(n-1)b: the winner is now strictly longer than all remaining gaps and ends at 0. Full length is reached after n-G contractions. Positive costs exclude any post-synchronization suffix, so equality at every move forces precisely the displayed word. The letter counts, formula and ordered-input linear-time calculation follow. A singleton needs only the empty word.

## originality

PASS

Credit substantial overlap: Eppstein already solves the unweighted arbitrary-subset optimization algorithmically, Cardoso already uses growing a largest gap and the n-1 rotation blocks, and the same-day pair record explicitly has the entire weighted two-state result. The later all-subset circular-gap record gives the exact unit-cost answer and witness by a closely related potential. The supported increment is the strict Bellman policy, hence one unique word minimizing every positive letter-cost objective for all subsets, not the gap-growth construction, pair theorem, or full-state length in isolation.

## value

PASS

For the canonical cyclic synchronizing family this identifies an exact deterministic policy for every occupied-state configuration and rules out any rotation/contraction cost trade-off or ties at positive weights. The pointwise all-subset statement is materially stronger than a worst-case bound by cardinality or computing an optimum separately for each set and cost pair. It gives a linear scan and compressed word rather than a search over intervals or state subsets. The value resides in the uniform strict policy and separate letter counts, not in recomputing the classical full-state length or restating the pair law.

The dated certificate retains the supplied scientific assessment, sources and limitations.
