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

# Reproducibility and limitations

The theorem is established by the four proof steps in `RESULT.md`: the semiprime reduction, the classical Bang–Zsigmondy primitive prime divisor theorem with its exceptions checked, injectivity plus the prime number theorem, and the standard exclusion of Carmichael semiprimes. For all primes \(p\ge5\), the primitivity order \(p-1\) divides \(q-1\), and the two base congruences then follow.

Run `python3 check.py` with Python 3 standard library only. Its reference output is `certificate_stdout.txt`. The certificate uses deterministic trial division for primality of each displayed example, modular multiplication to check multiplicative orders, a complete sieve for primes below \(100000\), and an exhaustive loop over all \(23313\) squarefree semiprimes not exceeding \(100000\). It verifies seven witness pairs, direct congruence-versus-reduced-congruence equivalence on this complete finite range, and the first sixteen OEIS A294169 entries. The count \(52\) in this finite range is corroborative only.

The code does not prove the infinite theorem or the external classical theorems. There is no independent mathematical audit or external certification. Historical coverage of potential prior proofs is incomplete.
