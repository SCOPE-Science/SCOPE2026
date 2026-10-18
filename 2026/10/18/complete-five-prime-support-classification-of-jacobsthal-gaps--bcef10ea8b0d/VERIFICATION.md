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

The standalone `verify.py` uses only the Python 3 standard library. It exhaustively checks all residue tuples for each subset of \(\{3,5,7\}\), verifies the sharp lower and upper finite-cover thresholds, and verifies an eleven-position obstruction in every case. The maximal tuple count in a case is \(105\).

It also computes every reduced residue modulo the product for eight representative radicals (one per claimed value) and obtains successive coprime gaps exactly, including the wraparound gap. A successful execution prints `JACOBSTHAL_FIVE_SUPPORT_EXACT_OK small_supports=8 residue_tuples=192 full_periods=8`.

The mathematical reduction by the Chinese remainder theorem and singleton coverage for primes at least eleven proves why this finite exhaustion controls every odd five-prime support. The doubling identity and direct odd-four-factor argument cover even supports. Sampled gcd-period checks alone do not prove the infinite theorem.

Independent audit: not performed. No independent validation or certification is asserted.
