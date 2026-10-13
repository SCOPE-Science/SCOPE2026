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

The unrestricted theorem follows from the exact divisor-sum identity and the prime-support bounds in `RESULT.md`; the finite test below is corroborative.

Run `python verify.py 1000000` with Python 3 and its standard library. The program reconstructs \(\sigma(m)\) by summing divisors and \(\omega(m)\) by marking prime multiples, then compares every solution in \([1,1000000]\) with the parametric prime family. Its recorded output is:

```text
VERIFY_OK upper_bound= 1000000 checked_omega_le_two= 367461 observed= [15, 207, 19359] expected= [15, 207, 19359] large_witness= 36472996363223648799 large_q= 10460353199 composite_neighbor_factor=102461
```

For the large witness, the verifier uses exhaustive integer trial division to establish primality of \(10460353199\), checks the exact divisor-sum equality, and exhibits \(102461\mid(36472996363223648799-1)/2\). The primality check is over a single finite integer; it makes no assertion about primality for arbitrary exponents. The sieve bound is inclusive. The code is not a substitute for the proof's universal quantifiers.
