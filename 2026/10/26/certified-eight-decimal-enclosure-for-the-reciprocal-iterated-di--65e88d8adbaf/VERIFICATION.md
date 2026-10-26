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

# Reproducibility and scope of verification

Run `python3 verify.py` using only the Python 3 standard library. The program implements an odd-only sieve, exact integer fixed-point probability updates with scale \(10^{40}\), and independent rational checks on a three-prime truncated toy model.

The outputs `CONTRIBUTION`, `CEILING_CONTRIBUTION`, and `REPRESENTED_MASS` are the exact integers \(A\), \(B\), and \(M\) in RESULT.md. The program constructs the exact rational endpoints \(A/Q-1/10^8-1/(3\cdot1000^3)\) and \((B+Q-M)/Q\), compares them to the announced decimal bounds by integer cross-multiplication, and prints `VERIFY_OK` only if all checks succeed.

A successful run produces 536 retained low-prime states, 5,761,287 processed primes above 1000, seven states in an independent exact rational toy comparison, and `VERIFY_OK rational_tiny=PASS exact_integer_interval=PASS prime_tail=PASS`.

The analytic comparison with the infinite constant depends on the elementary independent-prime valuation model, monotonicity of the divisor-count function under divisibility, and integral bounds for omitted large-prime events. The finite checks are not an independent proof of Campbell's asymptotic or of bibliographic novelty. Independent audit has not been performed.
