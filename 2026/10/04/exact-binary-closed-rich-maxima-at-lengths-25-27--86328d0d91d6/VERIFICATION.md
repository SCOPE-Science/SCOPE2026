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

Compile and run `verify.c` with a C11 compiler, for example:

`cc -O3 -std=c11 verify.c -o verify && ./verify`

The program first evaluates the closed predicate for every binary word of every length through \(27\). It then computes the exact number of distinct closed factors for every binary word by the append-one-symbol suffix recurrence proved in `RESULT.md`. It checks the published extremal sequence through length \(24\) before checking the new maxima at lengths \(25\), \(26\), and \(27\). Finally it enumerates every maximizer and tests all candidate periods from the defining equalities.

Successful replay prints exactly:

`VERIFY_OK source_table_1_24=matched n25=109 count25=56 p25=8:56 n26=117 count26=128 p26=8:56,9:72 n27=126 count27=72 p27=9:72`

This is a finite exhaustive certificate for the three stated lengths. No extrapolation to larger \(n\) is claimed. The correctness of the global maxima depends on the recurrence proof plus enumeration of every binary word, not on heuristic search or sampling.
