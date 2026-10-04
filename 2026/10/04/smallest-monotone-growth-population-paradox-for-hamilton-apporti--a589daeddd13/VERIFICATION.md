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
The embedded `verify_hamilton_population_boundary.py` gives an exact finite replay of the integer-minimality statement.

It implements Hamilton's largest-remainder rule in two ways: exact `Fraction` quotas and pure integer quotient/remainder arithmetic. The implementations are asserted equal on every census tested.

For three states and two seats, the program enumerates every pair of positive integer census vectors whose combined population is at most \(46\), keeps only pairs with componentwise nondecrease and strict Hamilton cutoffs, and tests every loser-gainer pair by exact cross-multiplication of growth factors. It verifies:
- no paradox below combined total \(46\);
- exactly six labeled pairs at total \(46\);
- a single orbit under all six state relabelings;
- canonical representative \((1,4,14)\to(4,5,18)\);
- allocations \((0,0,2)\to(0,1,1)\);
- loser growth \(9/7\) and gainer growth \(5/4\), with \(9/7>5/4\).

The analytic one-seat and two-state impossibility proofs are given in `RESULT.md`. The finite sweeps of those safe cases are only implementation consistency checks.

Run:

`python3 verify_hamilton_population_boundary.py`

The first line must be `VERIFY_OK`.
