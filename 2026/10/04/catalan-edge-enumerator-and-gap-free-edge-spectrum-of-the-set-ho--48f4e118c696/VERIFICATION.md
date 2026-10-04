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

The bundled checker uses two independent finite routes.

First, it recursively generates every plane full binary tree with \(n\) leaves. Leaves are numbered by in-order position. For each tree it computes root-to-leaf bit paths and evaluates \(C(x;y,z)\) using longest-common-prefix depth; for every increasing triple \(i<j<k\), it declares an \(M_3\) edge exactly when \(j,k\) have a deeper common prefix than \(i,j\). This is the finite tree form of the source's rule \(E(i,j,k)\iff C(i;j,k)\).

Second, independently of that triple scan, the checker computes the root-split statistic
\[
e(T)=e(L)+e(R)+|L|\binom{|R|}{2}
\]
and builds the polynomial recurrence
\[
P_n(q)=\sum_{i=1}^{n-1}q^{i\binom{n-i}{2}}P_i(q)P_{n-i}(q).
\]
It compares the two coefficient tables exactly through ten leaves.

The checker also verifies that the total number of generated trees is \(C_{n-1}\), tests coefficient palindromy through ten leaves, confirms
\[
P_4(q)=1+q+q^2+q^3+q^4,
\]
confirms that \(P_5\) has every exponent from \(0\) through \(10\) except \(5\), and verifies complete support for \(6\le n\le10\). The all-\(n\) support theorem beyond this finite range is proved by the interval induction in `RESULT.md`.

As an additional check that different tree types do not accidentally collapse to the same unlabelled hypergraph in small orders, the script canonically relabels every generated \(3\)-hypergraph under all vertex permutations through six vertices and recovers exactly \(C_{n-1}\) isomorphism classes.

Replay command:

`python3 artifacts/verify.py`

Observed output:

```
age_counts_n1_to_10 [1, 1, 2, 5, 14, 42, 132, 429, 1430, 4862]
P4 [(0, 1), (1, 1), (2, 1), (3, 1), (4, 1)]
P5 [(0, 1), (1, 1), (2, 1), (3, 2), (4, 2), (6, 2), (7, 2), (8, 1), (9, 1), (10, 1)]
P6_support (0, 20, 21)
injective_orbits_n1_to_8 [1, 2, 12, 120, 1680, 30240, 665280, 17297280]
VERIFY_OK
```

The script checks the finite combinatorial core. The identification of all finite hypergraph isomorphism types with plane-tree types uses the primary source's homogeneity, automorphism-group equality, and set-homogeneity and is established deductively in `RESULT.md`.
