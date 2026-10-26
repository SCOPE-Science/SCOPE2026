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

# Verification procedure

Run `python verify.py` with Python 3. The program uses only the standard library and contains two logically separate finite corroborations: direct integer factorization and both divisor sums for all \(n\) between \(2\) and \(10^6\) with \(\Omega(n)\le4\), and a scan of the necessary congruence/divisibility reductions in the proposed three-prime equality for all primes \(r\le20000\). The first test covers \(737448\) integers. The second covers \(2262\) primes and sees only the composite terminal candidate \(q=25\) in the surviving odd-prime divisibility pattern.

Expected final message:

`VERIFY_OK: 737448 integers with Omega<=4 through 1000000; prime-root reduction through 2262 primes; unique positive equality values 20,45`

These finite checks do not prove the classification for unbounded prime factors. The universal proof is the modular and divisibility argument in RESULT.md; in particular \(t\mid\gcd(r-1,r^2+1)\mid2\) and the integrality restriction \(r-3\mid12\) force a complete universal elimination. No external proof certificate or independent audit is claimed.
