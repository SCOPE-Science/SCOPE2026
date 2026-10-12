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

The proof in `RESULT.md` is universal and does not infer an infinite statement from finite data.

The attached `verify.py` independently factors every integer
\[
2\le n\le2{,}000{,}000
\]
with
\[
\Omega(n)\le3.
\]
It computes \(\sigma(n)\) and \(\varphi(n)\) directly from the prime factorization and tests
\[
\varphi(n)\mid\sigma(n)-n.
\]

The expected complete hit set in this finite range is
\[
\{2,6,10,12,44\}.
\]
The verifier also checks
\[
90=2\cdot3^2\cdot5,\qquad
\Omega(90)=4,\qquad
\frac{\sigma(90)-90}{\varphi(90)}=6.
\]

These computations are consistency checks only. Exhaustiveness for all \(n\) in the stated domain follows from the factorization-shape proof.
