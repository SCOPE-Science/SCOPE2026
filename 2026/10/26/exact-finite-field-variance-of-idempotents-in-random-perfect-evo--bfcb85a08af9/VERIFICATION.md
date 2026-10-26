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
# Reproducible checks

Run the standalone `verify.py` with Python 3. It enumerates all square matrices in ten cases, rejects singular matrices by exact finite-field row reduction, counts nonzero solutions of the idempotent equation, and calculates the mean and variance as `fractions.Fraction` values before comparing with the theorem. The test set includes the characteristic-two field extension \(\mathbb F_4\) and the excluded one-dimensional boundary.

Verified cases: \((q,n)=(2,1),(3,1),(2,2),(3,2),(4,2),(5,2),(7,2),(2,3),(3,3),(2,4)\). Representative empirical variances are \(5/6\) at \((3,2)\), \(13/15\) at \((5,2)\), \(23/26\) at \((3,3)\), and \(1\) at \((4,2)\). The script prints `VERIFY_OK` after all assertions.

The enumerations are finite consistency tests. The general proof does not rely on them. No independent mathematical audit has been performed.
