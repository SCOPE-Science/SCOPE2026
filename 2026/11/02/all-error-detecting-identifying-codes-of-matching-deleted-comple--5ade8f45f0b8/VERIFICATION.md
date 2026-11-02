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

Use Python 3.9 or later. Execute `python3 verify.py` in the directory containing the supplied standalone verifier; no third-party dependencies or downloaded resources are needed.

Observed output:

`VERIFY_OK: 155 full exhaustive parameter cases; 32 larger witness families`

The script separately creates the actual closed neighborhoods in each matching-deleted biclique, tests every vertex for at least two selected closed neighbors, and tests every distinct vertex pair for at least two selected vertices in one directed neighborhood difference. For 155 triples with \(2\le a,b\le7\), \(a+b\le13\) and \(0\le t\le\min(a,b)\), it examines every candidate sensor subset. The expected coefficients come from a separately programmed formula. For 32 additional instances, with deleted matching sizes up to 50, it checks the cardinalities, uniqueness and actual sensor validity of all constructed code classes.

The brute-force portion is finite. It is not an infinite theorem certificate; the structural proof in `RESULT.md` supplies that argument. The verifier tests the specified false-negative detection condition and not alternative models of fault tolerance. The source file was executed in the provided form.
