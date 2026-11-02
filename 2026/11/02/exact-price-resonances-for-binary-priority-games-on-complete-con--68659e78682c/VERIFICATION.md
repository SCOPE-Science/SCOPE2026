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

The proof in `RESULT.md` is analytical and holds for every integer \(n\ge2\) and every real price \(c>0\). In particular, it establishes the best-response inequalities from the stated utility, the adjacent gain identity, the forced alternating suffix following a switch, the two allowed prefix-length expressions and the candidate count.

A separate exhaustive checker, `verify.py`, computes unilateral utility differences directly from service-order comparisons rather than calling the analytical best-response characterization. For \(2\le n\le11\), it scans positive half-integer prices through one step beyond the all-zero threshold and checks complete equality of directly enumerated and analytically predicted equilibrium sets. It also checks the gain identity across all binary profiles for \(2\le n\le9\).

Executed with Python 3 standard library only:

`VERIFY_OK game_instances=150 scanned_profiles=90104 exact_gain_identites=8192`

This is finite corroboration, not an infinite certificate. The uniqueness of the two candidate profiles and the absence of noninteger-price equilibria follow from the algebraic proof, not from enumeration. Mixed equilibria and models outside the stated assumptions are not assessed. No independent audit has been performed.
