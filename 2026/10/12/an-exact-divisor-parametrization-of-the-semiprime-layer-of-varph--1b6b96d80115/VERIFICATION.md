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

The theorem in `RESULT.md` is universal; finite computation is used only as a consistency check.

The attached `verify.py` examines every integer
\[
2\le n\le2{,}000{,}000
\]
with
\[
\Omega(n)=2.
\]
It computes \(\varphi(n)\) exactly and compares the direct predicate
\[
\varphi(n)\mid n^2-1
\]
with the theorem's normalized criterion.

For each odd squarefree semiprime hit, it checks
\[
g\mid a+b,\qquad
h=\frac{g(a+b)+1}{ab}\in\mathbb Z_{>0},
\]
the identity
\[
(ha-g)(hb-g)=g^2+h,
\]
the finite bound
\[
h\le\left\lfloor\frac{3g+1}{2}\right\rfloor,
\]
and the prime-size bound
\[
q\le\frac{p^2+1}{2}.
\]
It also verifies that prime squares and even semiprimes are never accepted.

These checks do not establish the unbounded theorem; the infinite statement follows from the exact algebraic equivalences in the proof.
