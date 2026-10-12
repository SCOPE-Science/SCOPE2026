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

The attached `verify.py` independently factors every composite integer
\[
4\le n\le1{,}000{,}000
\]
with
\[
\Omega(n)\le3.
\]
It computes \(\sigma(n)\) and \(\varphi(n)\) from the prime factorization and tests
\[
n-\varphi(n)\mid\sigma(n)-n.
\]

The verifier asserts that the only hit is
\[
12.
\]
It separately checks
\[
56=2^3\cdot7,
\qquad
\Omega(56)=4,
\qquad
\frac{\sigma(56)-56}{56-\varphi(56)}=2.
\]

The finite computation is corroborative only. Exhaustiveness follows from the symbolic factorization-shape proof.
