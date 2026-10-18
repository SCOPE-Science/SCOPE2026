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

Run `python3 verify.py` with the Python 3 standard library. It uses exact `fractions.Fraction` calculations and independent enumeration of allowed-edge priority orders for three \(n=3\) substrates. The executed program printed `PASS 31 exact checks, including three independent edge-order enumerations`.

The computation verifies the one-forbidden-edge identity for all \(2\le n\le8\), calculates exact success/failure probabilities for three natural degree-bounded defect patterns in this range, and cross-checks the Markov chain against direct priority permutations. Only finitely many cases are tested; these checks do not certify the asymptotic bound. The infinite-family claim is supported instead by the survival-product estimates and biclique error argument in RESULT.md. No separate external validation or independent audit has been performed.
