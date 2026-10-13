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

# Verification and limits

The proof in `RESULT.md` is symbolic and unrestricted: it explicitly covers \(\varphi(n)=1\), odd \(n\), and all finite subsets of Fermat primes. For even inputs, the integer identity \(a-1+T=2^{2-T}P\), with odd \(P\), forces \(T\le2\), leaving just \(32,80,192\). The candidates are checked by direct evaluation of \(D(2^e)=e2^{e-1}\).

Run `python verify_totient_dyadic.py` from the package directory. The standard-library script computes the totient by an integer sieve, then the arithmetic derivative using exact prime-power factoring from a smallest-prime-factor sieve. It tests all \(n\) with \(1\le n\le10^6\) whose totients have no odd prime factor. Its recorded output is:

`VERIFY_OK limit=1000000 prime_power_totient_candidates=208 solutions=[32, 80, 192] near_exceptions=[31,81,112,176,244]`

The computation is finite and supplies no independent proof of the universal statement. No verification external to the documented self-review has been performed; no external certification is claimed. Originality comparisons cannot exclude undiscovered or unindexed older statements.
