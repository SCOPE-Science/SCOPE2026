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
The universal proof is independent of finite enumeration.

For an outside element \(y\), the critical map is
\[
\delta_y:K\to K,
\qquad
\delta_y(a)=[a,y].
\]
Because \(K\) is abelian, this is a group endomorphism. Its kernel is \(C_K(y)=1\) by the Frobenius property, so \(\delta_y\) is bijective. Hence a nontrivial kernel commutator can never become trivial by repeated commutation with \(y\).

For an outside element \(x\) and nonidentity kernel element \(y\),
\[
[x,y]\in K\setminus\{1\},
\qquad
[x,{}_{2}y]=1,
\]
so the one-way arc to the kernel has exact depth \(2\).

The packaged checker `artifacts/verify.py` reconstructs six fixed-point-free semidirect products:
\[
C_3\rtimes C_2,
\quad C_5\rtimes C_4,
\quad C_7\rtimes C_3,
\quad C_9\rtimes C_2,
\quad C_5^2\rtimes C_4,
\quad C_7^2\rtimes C_6.
\]
It computes every ordered Engel relation by iterating commutators until the identity or a repeated state appears. It then independently checks the predicted block partition, exact depths, all strong components, condensation arcs, indegrees, outdegrees, and total arc counts.

The resulting arc totals are
\[
8,\ 102,\ 128,\ 128,\ 2502,\ 14996.
\]
The checker returns `VERIFY_OK`.

Finite computation is not used to infer the universal theorem.
