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
2\le n\le3{,}000{,}000
\]
with
\[
\Omega(n)\le3.
\]
It computes the exact factorization, \(\sigma(n)\), and \(\varphi(n)\), then tests
\[
n\mid\varphi(n)\sigma(n).
\]

The theorem predicate is checked independently from the direct divisibility:
\[
n=6,
\qquad
n=18,
\]
or
\[
n=p^2(p^2+p+1)
\]
with both factors prime.

The verified hit set is
\[
\{6,18,28,117,775,88723,2896363\}.
\]

The finite replay is corroborative only. Exhaustiveness follows from the factorization-shape proof.
