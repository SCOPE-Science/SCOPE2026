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

Run `python3 checker.py` using Python 3 and the standard library. It needs no input data or network access.

The script checks all palindromic factors by direct cyclic enumeration against the structural inventory for 8,000 labeled triples of zero gaps, verifies the exact bivariate distribution through 50 zeros, and separately enumerates rotation orbits of all length-3 through length-17 binary words containing exactly three ones. It raises an assertion on disagreement and prints `PASS` summaries otherwise.

The proof of the general formula is symbolic: a four-way partition by the number of ones in a palindrome, followed by a partition of sorted gap configurations and geometric-series summation. The limit theorem uses equidistribution of nonnegative integer triples on a simplex. Finite experiments do not substitute for these arguments and do not establish historical priority. No independent audit has been performed.
