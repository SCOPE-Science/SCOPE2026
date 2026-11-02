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

# Exact independent arithmetic checks

The file `VERIFY.py` requires only Python's standard library. Run `python VERIFY.py` in the directory containing this verification file. It independently generates Euler-totient values by a sieve and compares the **complete sets** of positive preimages with the theorem's conditional formulas for every odd prime at most 2000. It separately checks that no enumerated fiber is a singleton. The verifier exhausts the tested fibers using the proven bound \(n<6\varphi(n)\) for these values; it does not truncate at an arbitrary experimental cutoff.

Observed output:

```text
VERIFY_OK primes=302 q_max=2000 independent_totient_sieve=yes cardinality_histogram=[(0, 158), (2, 33), (3, 52), (4, 40), (6, 17), (9, 1), (10, 1)] checked_preimages=503 enlarged_boundary=yes
```

The comparison establishes exact agreement only within the tested finite range. The proof in `RESULT.md`, not this enumeration, establishes the theorem for every odd prime. Historical priority and independent mathematical audit remain unverified.
