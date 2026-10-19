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

# Finite verification protocol

Run `python3 verify.py` and `python3 verify_independent.py` alongside `certificates.json`. These are standalone standard-library Python programs; no scientific computation from another package is imported. Each generates all four finite regular-paperfolding prefixes directly from the odd-part rule.

For each prefix, `verify.py` loops over every substring length and every starting position, compares literal binary substrings, and ensures that the proposed attractor crosses at least one occurrence of every distinct factor. It independently finds all occurrences of each weighted certificate factor and adds its weight once to each position in the *union* of those occurrence spans. It checks the total weighted sum, denominator, and maximum position load. Expected terminal marker: `VERIFY_OK`.

`verify_independent.py` uses a different odd-part implementation and integer-bitset unions of substring occurrence intervals. It verifies all factors and separately recomputes load inequalities from the provided factor strings. Expected terminal marker: `INDEPENDENT_VERIFY_OK`.

Validated numerical rows are: prefix lengths `128,256,512,1024`, distinct factor totals `6479,25775,102767,410351`, attractor sizes `5,6,6,7`, weight sums `5,11,12,51`, denominators `1,2,2,8`, and maximal position loads `1,2,2,8`. These give exact lower bounds `5,6,6,7`. These finite checks are exhaustive under the declared definition; they do not establish any statement for untested word lengths or an asymptotic growth law. No independent external audit has been performed.
