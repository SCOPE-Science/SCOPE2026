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

# Verification of the two-support classification

Run `python3 verify_h5.py` with Python 3. The script implements the two independent prime-power cases of \(\sigma^{**}\), factors all \(n\le10^6\) with a smallest-prime-factor sieve, and tests integrality of \(H_5(n)\) exactly for all \(\omega(n)\le2\). It also checks the local non-power-of-two lemma for twelve odd primes and exponent \(2\) through \(100\).

Expected output:

`VERIFY_OK limit=1000000 support_hist=[1, 78734, 288726] qualifying=[1, 6, 45] odd_prime_exponent_tests=1188`

The mathematical verification is the unrestricted proof in RESULT.md: it checks every prime-support possibility and derives the power-of-two lemma without finite-exponent assumptions. Finite trials cannot establish an infinite classification; they are independently reproducible consistency checks. No external expert or independent audit has been performed.
