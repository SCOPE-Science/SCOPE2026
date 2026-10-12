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

The attached `verify.py` enumerates every prime square and every squarefree semiprime
\[
pq\le2{,}000{,}000
\]
with
\[
p<q.
\]

For each squarefree semiprime it checks three predicates independently:

\[
\sigma(pq)-\varphi(pq)\mid\sigma(pq)+\varphi(pq),
\]

\[
p+q\mid p^2-1,
\]

and the quotient-fiber identity
\[
(p-k)(q-k)=k^2-1.
\]

It asserts that the predicates agree in every tested case and separately confirms that no tested prime square satisfies the original divisibility.

The finite replay is corroborative only. The infinite statement follows from the exact algebraic reduction and exhaustive factorization-shape split.
