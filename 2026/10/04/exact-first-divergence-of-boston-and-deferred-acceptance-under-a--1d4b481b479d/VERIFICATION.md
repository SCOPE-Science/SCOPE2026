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
The embedded `verify_boston_da_common_priority_3x3.py` is a standard-library-only exact replay.

Boston is implemented twice: an ordinary application-round algorithm and an independent rank-by-rank irreversible-admission replay.

Deferred acceptance is also implemented twice: the ordinary proposal-and-holding algorithm and common-priority serial dictatorship.

The script verifies:
- all four \(2\times2\) profiles give identical Boston and deferred-acceptance outcomes;
- all \(216\) \(3\times3\) profiles are evaluated exactly;
- exactly \(24\) profiles diverge;
- the divergent set is exactly the set satisfying: students \(1\) and \(2\) share a first choice, and student \(3\)'s first choice is student \(2\)'s second choice;
- all \(24\) divergent outcomes are Pareto-incomparable;
- there are exactly four school-relabeling classes, each of orbit size \(6\);
- the two rank-vector patterns occur twelve times each.

Run:

`python3 verify_boston_da_common_priority_3x3.py`

The first output line must be:

`VERIFY_OK`

The computation is a finite replay of the analytic theorem; no larger-market statement is inferred from enumeration.
