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
# Verification record

Run `python3 verify_catalan.py` with Python 3 and the standard library. It exhaustively constructs all ordered pairs of the \(2^{n-1}\) idempotent retractions for each \(1\le n\le10\), calculates both products as transformations, and checks the full list of product fibers against the Mersenne-gap formula. It independently enumerates all order-preserving regressive transformations up to \(n=8\) and verifies that the retractions are precisely the idempotents. It independently checks the closed binomial coefficient formula for every observed rank distribution and the total recurrence.

Observed total commuting-pair counts for \(n=1,\ldots,10\): `1,4,14,48,164,560,1912,6528,22288,76096`. Successful execution prints `VERIFY_OK` as the final line. The only requirement is a working Python 3 standard library.

The program verifies finitely many cases. The general conclusion is established by the combinatorial argument, not by extrapolation. No external mathematical audit has been performed.
