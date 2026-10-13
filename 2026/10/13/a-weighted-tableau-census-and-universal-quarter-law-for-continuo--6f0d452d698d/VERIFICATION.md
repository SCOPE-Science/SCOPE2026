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

# Verification of the stated finite-chain enumeration

Run `python3 artifacts/verify.py` (Python standard library only). The verified standalone program enumerates every binary relation for chain pairs \((r,m)\) with \(1\le r,m\le4\), testing **74,954** relations in total. One check computes openness of both raw modal operators at each possible upward-open threshold, with the empty and total subsets included; another computes monotonicity of row minima and maxima. These independently implemented conditions agree for every relation.

The exhaustive run finds 3,958 two-sided continuous relations and 960 with either all rows empty or all rows consecutive intervals. For every examined pair these numbers equal the exact weighted multichain and hook-content counts. The self-relation totals for chain sizes one through five computed by transfer recursion are 2, 7, 80, 2855, and 374660; size five is not a brute-force enumeration of all \(2^{25}\) relations. For fixed target sizes three through six, the program checks the exact rational dominant-pole constants against the weighted count at source size 80.

This code verifies finite instances only. Correctness for all positive \(r,m\) relies on the endpoint equivalence, independent row-choice count, tableau bijection, and dominant-pole proof supplied in `RESULT.md`. No independent external audit, formal proof assistant, or claimed infinite enumeration is involved.
