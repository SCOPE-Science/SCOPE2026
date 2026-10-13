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

The displayed groupoid has exact-depth value sets
\[
D_1=\{0,a,b\},\qquad D_2=\{0,a\},\qquad D_3=\{0\}.
\]
Thus every term of depth at least \(3\) vanishes. Also
\[
G^2=\{0,a,b\},\qquad (G^2)^2=\{0,a\},
\]
so the obstruction to \(3\)-supernilpotency is nonzero.

For the lower bound, if \(u,v\in H^2\) and \(uv=w\neq0\) in a \(3\)-nilpotent groupoid with zero, depth-\(3\) vanishing makes \(w\) a two-sided annihilator. Hence \(u,v\neq w\). If \(u\neq v\), four distinct elements are present. If \(u=v\) in an algebra of size at most \(3\), any product representing \(u\) must use \(u\) twice, forcing both \(u^2=u\) and \(u^2=w\), a contradiction.

`check_minimal.py` exhaustively checks all \(81\) labeled three-element groupoids with zero and confirms that none separates \(3\)-nilpotency from \(3\)-supernilpotency. It also checks the four-element example and terminates with `CHECK_OK`.

The finite computation is a cross-check, not a substitute for the symbolic proof. No claim is made for \(n\ge4\).
