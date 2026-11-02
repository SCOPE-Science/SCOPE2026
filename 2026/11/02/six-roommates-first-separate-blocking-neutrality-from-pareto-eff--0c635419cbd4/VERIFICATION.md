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

Reproduce with `python3 verify_bn.py` using standard Python 3. The program independently enumerates all \(1296\) strict four-agent preference profiles and all feasible pairings, and constructs complete dominance relations for the two six-agent profiles before and after the indicated adjacent swap.

The recorded complete census for four agents has exactly \(48\) unsolvable labeled profiles, each with three distinct singleton blocker sets and all three matchings both blocking-neutral and Pareto optimal. The initial six-agent profile has nine Pareto-optimal and nine blocking-neutral pairings; the final six-agent profile has nine Pareto-optimal and six blocking-neutral pairings. The verifier asserts exact matching identities, not just counts, and prints all fifteen six-agent pairings and blocker sets. Its successful terminal line is `ALL ASSERTIONS PASSED`.

This is a finite exhaustive check for the four-person universe and exact verification of the specified six-person witnesses; it is not an enumeration of all six-person preference profiles. The universal four-person step also uses the published classification of unsolvable profiles, and the analytic six-person proof is given in `RESULT.md`. Independent scientific audit has not been performed.
