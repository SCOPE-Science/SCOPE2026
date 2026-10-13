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

The proof in `RESULT.md` is universal.

The attached `verify.py` independently factors every integer
\[
2\le n\le2{,}000{,}000
\]
with
\[
\Omega(n)\le2.
\]
It computes \(\sigma(n)\) and \(\varphi(n)\) exactly from the factorization and tests
\[
\varphi(n)\mid n\sigma(n).
\]

It asserts that the complete hit set in that finite range is exactly
\[
\{2,3,4,6,10,14,15,21,26,35,39,55,155,203\}.
\]

The computation is corroborative only. The absence of larger low-multiplicity solutions follows from the symbolic prime/prime-square/semiprime proof, not from the cutoff.
