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

The proof has three independently checkable components.

1. **Rank-one classification.** Every nonzero singular element of \(M_2(\mathbb F_q)\) has a unique image line and kernel line. For each ordered pair of lines there are exactly \(q-1\) matrices, differing by nonzero scalar.

2. **Adjacency reduction.** For types \((L,K)\) and \((L',K')\),
\[
AB=0\iff L'=K,
\qquad
BA=0\iff L=K'.
\]
This is the only graph-theoretic input used by the general proof.

3. **Lower-bound accounting.** Any support that dominates all absent projective types contains the rectangle \(X\times Y\). The coordinate deficits force at least
\[
|X||Y|+m-|X|-|Y|
=
m-1+(|X|-1)(|Y|-1)
\]
represented types. Equality below \(m=q+1\) leaves an isolated selected off-diagonal type. When \(q>2\), that fiber has another scalar multiple outside the dominating set, giving the contradiction.

The standalone verifier additionally reconstructs the actual matrix graphs over \(\mathbb F_2\) and \(\mathbb F_3\), exhaustively searches their dominating sets through the proved optimum, and checks the projective support mechanism for \(q\in\{2,3,4,5\}\).

Exact output:

```text
VERIFY_OK
actual_q2_vertices=9 gamma=2
actual_q3_vertices=32 gamma=4
projective_support_checks=q2,q3,q4,q5
theorem_values=q2:2,q3:4,q4:5,q5:6
```

The finite computations are corroborative only; the arbitrary-prime-power theorem is proved symbolically.
