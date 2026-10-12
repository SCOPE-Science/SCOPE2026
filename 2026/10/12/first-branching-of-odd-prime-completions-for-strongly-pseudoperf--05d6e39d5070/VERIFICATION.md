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

The file `artifacts/verify.py` reconstructs all finite claims using integer arithmetic, exact reciprocal divisor pairing, deterministic primality sieving and bit operations.

The first algorithm enumerates all \(2^{a+1}-1\) nonempty binary masks for each \(1\le a\le9\) and derives every possible odd-prime completion from the binary-reversal fraction. The second independently scans all primes below \(2^{a+1}\) and expands the actual divisor-pair subset-sum polynomial by exact integer bitset dynamic programming. Both algorithms return the same nine prime sets.

Explicit witnesses for \(2^9\cdot23\) and \(2^9\cdot179\) are checked for unique divisors, reciprocal closure, correct sum \(2N\), and their distinct omission counts. The check is exhaustive within the rigorously bounded finite range; no result for \(a>9\) is inferred.
