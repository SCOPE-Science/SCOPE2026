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

The standard-library code `verify_chebyshev_a.py` was executed and returned `VERIFY_OK`. It checks exact genus-one binary-quartic \(j\)-values \(1728,8000,1728\), two cleared-denominator quotient identities, and Hasse–Witt matrices for the smooth plane quartic over the prime fields with \(p=3,5,7,11,13,17,19,23,29,31,37,41,43,47,53\). Every computed rank equals \(3-a\) with \(a\) determined by the prime residue class modulo eight.

The all-primes proof is the degree-two quotient decomposition and the elliptic CM inertness criterion, not extrapolation from finite-prime tests. The standalone program is exact but does not independently certify the general Ciani isogeny theorem or Deuring's theorem. The full text of one earlier same-family maximality paper could not be inspected, so that specific literature-overlap risk remains.
