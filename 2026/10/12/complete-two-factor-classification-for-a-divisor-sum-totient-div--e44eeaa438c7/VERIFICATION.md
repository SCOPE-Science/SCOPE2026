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

The universal proof is symbolic and appears in `RESULT.md`.

The attached `verify.py` independently checks every integer
\[
2\le n\le5{,}000{,}000
\]
with
\[
\Omega(n)=2.
\]
For each such integer it computes \(\sigma(n)\) and \(\varphi(n)\) from its prime factorization and compares the direct condition
\[
\sigma(n)\mid n\varphi(n)
\]
with the theorem's criterion.

The verifier also checks directly that every tested odd-prime branch satisfies
\[
q=p^2-p-1
\]
and that the quotient equals
\[
q(p-2).
\]
Prime squares are tested separately and none is admitted.

These finite checks corroborate the formulas and case boundary handling. They are not used to infer the unbounded classification.
