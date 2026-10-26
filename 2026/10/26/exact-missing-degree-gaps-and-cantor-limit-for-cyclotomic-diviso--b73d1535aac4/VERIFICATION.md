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
# Verification of the cyclotomic degree-gap theorem

The `verify.py` script computes all cyclotomic factor degrees independently as \(\varphi(d)\), for every positive divisor \(d\) of \(N=2^ap^b\), and builds their subset sums via an integer-bitset algorithm. It compares the resulting full attainable degree set with the formula from the theorem, checks \(N-d\) complement symmetry, verifies the complete regime, and in the incomplete regime checks all distinct-degree counts, missing counts and entire gap histograms.

Run with `python3 verify.py`. The recorded successful check is `VERIFY_OK: 77 independent totient-subset enumerations; exact gap multisets and completeness regimes`.

Scope: \(1\le a\le4\), \(1\le b\le3\), odd primes among \(3,5,7,11,13,17,19\), and \(N\le20{,}000\). This is an independent finite computational consistency test, **not** a proof of the theorem for arbitrary parameters. The general argument appears in `RESULT.md`; the Cantor dimensional conclusion is proved by a separated-cylinder mass estimate, not by the numerical script. Independent mathematical audit remains unperformed.
