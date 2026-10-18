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

# Verification protocol

The exact claim is \(a(7)=19{,}027{,}139\), for distinct squarefree products of seven distinct primes. The following are deterministic proof checks, not random tests.

1. With C++17 available, compile and run `verify_exact.cpp` from the directory containing the embedded files. It generates the full seven-prime-product list up to \(19{,}120{,}000\) with an arithmetic sieve and performs a 3100-coin, bounded exact subset-sum calculation to \(40{,}000{,}000\).
2. Run `python3 verify_alternate.py` independently. It uses recursive increasing prime tuples and arbitrary-precision integer shifts rather than the sieve and 64-bit word shifts of the other checker.
3. Check that both print `VERIFY_OK`, with \(c_{3100}=19{,}111{,}638\), \(c_{3101}=19{,}114{,}095\), and largest missing finite subset sum \(19{,}027{,}139\).
4. Read the induction in `RESULT.md`. The computed interval has length \(20{,}972{,}861\), at least \(c_{3101}\), and Bertrand's postulate gives \(c_{j+1}<2c_j\) for every \(j\). This extends coverage without any further finite checks.
5. Confirm that \(c_{3100}>19{,}027{,}139\) and therefore no later coin can participate in a representation of the claimed missing integer.

The complete finite base is established only to the indicated finite bound. Its extension to the infinite set depends on the supplied mathematical proof. The checker execution is independently reproducible, but **no independent scientific audit has been performed**.
