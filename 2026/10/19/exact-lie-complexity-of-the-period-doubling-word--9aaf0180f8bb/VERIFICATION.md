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

# Finite verification and proof boundary

Run `python3 verify.py` with Python 3.8 or later. A successful execution prints four `PASS:` lines and a sample count table. The script checks the word generated both by iterating the substitution and by two-adic valuations, compares the complete observed factor sets for two prefix lengths, enumerates cyclic rotation classes at lengths 1 through 200, and checks the even-length class bijection against an independently assembled substitution image set.

The verifier was executed successfully, with all assertions satisfied. It does not certify that observing factors in a length-16384 prefix proves completeness of the infinite language. The infinite-length conclusion instead follows from the explicit parity, forbidden-factor, bijection, and base-case arguments in `RESULT.md`. Finite experiments cannot substitute for those arguments.

The references in `RESULT.md` support the literature comparison; searches and textual comparisons are described in `REVIEW.md` and `AUDIT.json`. The literature check cannot exclude unknown or unindexed equivalent treatments. No independent audit has been performed.
