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
# Verification of the Delannoy gcd-density theorem

The standalone `verify.py` script uses only the Python standard library. It checks central Delannoy coefficients from both their binomial sum and their three-term recurrence, binomial Lucas factorization, the polynomial involution modulo each small odd prime, absence of adjacent zero digits, the guaranteed middle zero for primes \(3\pmod4\), and exact residue-count formulas for complete prime-power blocks of bounded size. Invoke `python3 verify.py`; successful completion prints `VERIFY_OK`.

These are finite corroborations. The infinite proof is the six-step derivation in `RESULT.md`, including the characteristic-prime ODE argument and the arbitrary-cutoff density estimate. The number of prime-power blocks checked is finite and does not certify the mathematical novelty or every possible index. Independent audit has not been performed.
