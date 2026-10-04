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

Run `python3 verify.py`. A successful replay prints class-size vectors for \(p=3,5,7,11\), confirms direct two-consecutive-deletion covering for every syndrome at \(p=3,5,7\), and ends with `VERIFY_OK`.

The program checks, for every binary pattern in the tested primes, that syndrome parity equals Hamming-weight parity and that one cyclic right rotation changes the syndrome modulo \(p\) by the cyclic transition count. It then computes ternary class sizes from the exact lift weight \(2^{p-\operatorname{wt}(b)}\) and compares them to the claimed closed form.

For \(p=3,5,7\), the program separately enumerates all ternary length-\(p\) words, forms every code class from its parity-pattern syndrome, deletes every possible consecutive pair, and verifies coverage of all ternary length-\(p-2\) words.

These finite checks do not prove the infinite statement. The all-prime cardinality result is proved symbolically by the rotation-orbit argument in `RESULT.md`; the all-prime covering property is the ternary specialization of the cited source theorem.
