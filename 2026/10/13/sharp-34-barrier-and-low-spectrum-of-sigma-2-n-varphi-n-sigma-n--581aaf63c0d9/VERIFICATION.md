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

The proof in `RESULT.md` is unrestricted.

The attached `verify.py` checks every integer
\[
2\le n\le2{,}000{,}000.
\]
It computes the exact factorization, \(\sigma(n)\), \(\sigma_2(n)\), \(\varphi(n)\), and
\[
H(n)=\sigma_2(n)+\varphi(n)\sigma(n)-2n^2.
\]

It asserts that every value below \(34\) occurs only on primes, squarefree semiprimes, or
\[
4,\ 8,\ 9,\ 25,
\]
with respective exceptional values
\[
3,\ 17,\ 7,\ 21.
\]
It also asserts that the boundary fiber is exactly
\[
H^{-1}(34)=\{12\}.
\]

The finite replay is corroborative only. Exhaustiveness beyond the cutoff follows from the symbolic formulas and recursion in `RESULT.md`.
