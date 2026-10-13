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

The attached `verify.py` constructs a prime-counting table by sieve and independently checks every integer
\[
2\le n\le2{,}000{,}000
\]
with
\[
\Omega(n)\le2.
\]
For each such integer it computes \(\sigma(n)\), \(\varphi(n)\), and \(\pi(\sigma(n))\) exactly.

It also reconstructs all finite exceptional cases left by the symbolic proof and compares them with `small_cases.csv`.

The expected and verified complete hit set is
\[
\{3,9,34\}.
\]

The finite sweep is a consistency check only. Exhaustiveness beyond its cutoff follows from the symbolic inequalities in `RESULT.md`.
