# Divisor-rooted permutation fixed spaces of graph discrete Morse complexes

## Finding

Let \(n\geq 2\), let \(\mathfrak M(K_n)\) be the ordinary Chari–Joswig discrete Morse matching complex of the complete graph on \(n\) labeled vertices, and let \(\sigma\in S_n\) act by relabeling graph vertices. Write \(m_d\) for the number of cycles of length \(d\) in \(\sigma\), and set \(c=\sum_{d\ge1}m_d\). Call the cycle type **divisor-rooted** if one occurring cycle length \(d_0\) divides every occurring cycle length. For each occurring length \(d\), define

\[
S_d=\sum_{\substack{e\mid d\\1\le e<d}}e m_e,\qquad
Q_\sigma(z)=\prod_{d:m_d>0}(1+S_dz)(1+(S_d+d m_d)z)^{m_d-1}.
\]

**Theorem.** If \(c=1\), the geometric fixed space \(|\mathfrak M(K_n)|^{\langle\sigma\rangle}\) is empty. If \(c\ge2\) and the cycle type is divisor-rooted, this fixed space has a canonical triangulation of pure dimension \(c-2\) that is shellable, and its complete integral homotopy type is

\[
\boxed{|\mathfrak M(K_n)|^{\langle\sigma\rangle}\simeq
\bigvee^{\,B_\sigma}S^{c-2},\quad
B_\sigma=\left|\prod_{d:m_d>0}(1-S_d)(1-S_d-dm_d)^{m_d-1}\right|.}
\]

A zero wedge multiplicity means a contractible space. More precisely, the face-number generating polynomial of the canonical fixed-space triangulation (including the empty face) is exactly \(Q_\sigma(z)\). Thus all reduced integral homology is free and confined to degree \(c-2\), with rank \(B_\sigma\); the homotopy statement is stronger than the Euler-characteristic formula.

The class is not limited to chains of divisors or involutions. For cycle types \((2,4,6)\), \((2,4,8)\), and \((2,2,2,4)\), the fixed spaces are respectively \(S^1\), \(\bigvee^5S^1\), and \(\bigvee^{125}S^2\). The first type contains the incomparable lengths four and six. In contrast, a cycle type such as \((2,3)\) is not divisor-rooted, and its fixed space is empty despite having two permutation cycles; the divisor-rooted hypothesis is therefore substantive.

## Assumptions and scope

The ordinary discrete Morse matching complex is used, **not** the strong discrete Morse complex. A vertex of \(\mathfrak M(K_n)\) is an oriented incidence pair \((v,\{v,w\})\), written \(v\to w\). A face is a set of such arrows with at most one outgoing arrow at each original graph vertex and no directed cycle. Its geometric realization is equipped with the actual simplicial relabeling action, and the fixed set consists of points fixed by every power of \(\sigma\), not merely invariant simplices as an abstract collection.

The theorem assumes only that one cycle length divides every other cycle length, with no restriction on the multiplicities and no total-order assumption among the remaining lengths. Its shellability and homotopy conclusions for more general cycle types are not asserted. The space for \(c=1\) is the empty geometric realization of a complex containing only the empty face. The convention \(S^0\) is the two-point sphere, so a wedge of one zero-sphere is two points.

## Proof

**1. Triangulating the geometric fixed space.** Write \(C_1,\ldots,C_c\) for the vertex cycles of \(\sigma\), of lengths \(a_1,\ldots,a_c\). The action on the vertices (directed arrows) of \(\mathfrak M(K_n)\) partitions them into cyclic orbits. A point in the realization is fixed exactly when its barycentric weights are constant on each vertex orbit. Such a point can occur only on a simplex containing every vertex of each chosen orbit. Taking each admissible orbit's barycenter as a new vertex therefore yields a canonical simplicial triangulation \(Y_\sigma\) of the actual fixed space. Its faces are exactly sets of arrow orbits whose unions form directed forests on the original \(n\) vertices.

**2. Admissible arrow orbits.** Consider arrows with sources on \(C_i\) (length \(a_i\)) and targets on \(C_j\) (length \(a_j\)). If an arrow orbit forms part of a face, the entire source cycle must map equivariantly to a single target cycle. Its existence requires \(a_j\mid a_i\): otherwise the source vertices have multiple outgoing arrows. If \(i=j\), the equivariant target map is a cyclic shift of \(C_i\) and creates a directed cycle, so it is forbidden. If \(i\ne j\) and \(a_j\mid a_i\), precisely \(a_j\) distinct equivariant maps exist, determined by the target of one chosen source vertex. Each is an admissible arrow orbit. Hence the quotient has, for each ordered pair of distinct cycles, exactly \(a_j\) parallel arrows \(i\to j\) when \(a_j\mid a_i\), and none otherwise.

**3. Forest equivalence.** Two chosen arrow orbits cannot use the same source cycle because that would violate the one-outgoing-arrow rule. The directed graph on cycle indices consequently has at most one outgoing arrow per index. A directed cycle among chosen original arrows projects to a closed directed walk, hence a directed cycle, among the cycle indices. Conversely a directed cycle among cycle indices forces divisibility of lengths around the cycle, and thus all its lengths are equal. Each corresponding equivariant map is a bijection of cyclic sets, and the composite around the quotient cycle is a finite cyclic permutation. Repeating the walk therefore closes a directed cycle in the original graph. This proves that faces of \(Y_\sigma\) are exactly the directed forests of the weighted quotient multidigraph in Step 2. In particular, the weights count genuinely different simplex vertices, rather than algebraic multiplicities added after the fact.

**4. Purity and shellability.** Reverse every quotient arrow, thereby changing the convention from at most one outgoing to at most one incoming. Let \(D\) be the underlying simple directed graph after forgetting the parallel-arrow labels. A cycle index of length \(d_0\) is a complete source of \(D\), since \(d_0\) divides every other cycle length and there is an arrow from the distinguished index to every other index. The complete-source shellability theorem of Kozlov, in the explicit form reviewed by Jojić [3, Section 2], applies to the directed-forest complex \(\Delta(D)\). Every forest can extend to a spanning directed tree, hence its facets have precisely \(c-1\) arrows. Restoring the parallel arrows is exactly the positive-integer **simplicial expansion** of \(\Delta(D)\): each arrow is independently replaced by one of its allowed labels, never selecting two replacements of the same arrow. Moradi and Khosh-Ahang [4, Definition 2.1 and Theorem 2.12] prove that expansion preserves shellability. It also preserves facet cardinalities. Thus \(Y_\sigma\) is pure shellable of dimension \(c-2\). For \(c=1\), Step 2 gives no admissible arrow orbit and hence an empty geometric fixed set.

**5. Exact face polynomial.** Orient quotient edges toward their targets as in Step 2 and form the weighted row-outgoing Laplacian \(L\): its off-diagonal entry \(L_{ij}\) is \(-a_j\) if \(i\ne j\) and \(a_j\mid a_i\), and zero otherwise; diagonal entries are the sums of outgoing weights. The directed matrix–forest theorem [5] identifies the generating polynomial of weighted directed forests with \(\det(I+zL)\). The same quotient and Laplacian appear in the pre-existing equivariant face-character calculation [6]; here we use the determinant as an enumerative input, not as a homotopy theorem. Order the permutation cycles by their lengths. Since arrows only point to same-size or divisor-size cycles, \(I+zL\) is block triangular. Its block for the \(m_d\) cycles of length \(d\) is

\[
(1+z(S_d+d m_d))I_{m_d}-zd J_{m_d},
\]

where \(J_{m_d}\) is the all-ones matrix. On the constant vector this block has eigenvalue \(1+S_dz\), and on its codimension-one sum-zero subspace the eigenvalue is \(1+(S_d+dm_d)z\). Multiplying proves \(\det(I+zL)=Q_\sigma(z)\), as asserted. No matrix inversion or nonzero-determinant hypothesis is used.

**6. Integral homotopy type.** A finite pure shellable complex of dimension \(c-2\) is homotopy equivalent to a wedge of \((c-2)\)-spheres. The alternating face sum is \(Q_\sigma(-1)\), so its reduced Euler characteristic equals \(-Q_\sigma(-1)\). For such a wedge, the reduced Euler characteristic is \((-1)^{c-2}\) times the number of spheres. This determines the nonnegative integer multiplicity as \(|Q_\sigma(-1)|=B_\sigma\), completing the proof with integral (not merely rational) homotopy and homology conclusions.

## Verification

The included standalone, standard-library program `verify.py` constructs the **original** vertex permutation and all directed-edge orbits, without assuming the quotient description. It checks each admissible orbit, compares all valid unions with directed forests on quotient indices, enumerates every face of the small resulting simplicial complexes, and independently computes mod-two simplicial boundary ranks. It compares the resulting face vectors and reduced Betti numbers with the theorem for fourteen divisor-rooted cycle types, including the non-chain \((2,4,6)\), the rank-five circle bouquet \((2,4,8)\), and a rank-125 two-sphere bouquet \((2,2,2,4)\). The observed final line is `VERIFY_OK 14 cases` when executed as `python3 verify.py`. These finite computations do not establish shellability for arbitrary parameters: the unrestricted proof is Steps 1–6.

## Relationship to prior work

Knudson and Owens–White [1] distinguish ordinary versus strong discrete Morse matching complexes and discuss the complete-graph case, but their homotopy theorems concern the strong version and they do not compute geometric fixed spaces under arbitrary vertex permutations. Deshpande and Sawant [2] investigate shellability of directed-forest-related complexes, with primary focus on directed linear forests, but do not classify these cyclic fixed spaces. The general complete-source shellability theorem [3], expansion-shellability theorem [4], and matrix–forest theorem [5] are explicitly used as earlier ingredients. The published equivariant matrix–forest calculation [6] already establishes the orbit-divisibility enumeration and the complete-graph face-character determinant; in particular, it implies the displayed Euler-characteristic factor. **The claimed new result is the actual geometric fixed-space shellability and integral homotopy classification for the entire divisor-rooted class, not the quotient or determinant formula in isolation.** Existing involution-specific cases form a proper subfamily of the present theorem. Because the classification combines several known ingredients, its originality relative to unindexed combinations remains a genuine residual risk.

## Limitations

The divisor-rooted hypothesis is sufficient, not claimed necessary, for shellability. The result classifies the fixed space of the *single cyclic subgroup* generated by \(\sigma\); it does not classify intersections of fixed spaces of arbitrary subgroups, the full equivariant homotopy type, or geometric fixed spaces for non-divisor-rooted cycle types. The integral homology statement does not identify a preferred integral basis or the action of centralizer symmetries on it. The formula for face numbers follows from the prior determinant reduction; the new homotopy deduction depends on the shellability and expansion theorems. Unindexed equivalent arguments may exist. No independent mathematical audit has been performed.

## References

[1] K. Knudson and A. Owens–White, *Complexes of strong discrete Morse matchings*, arXiv:2609.06844v1, first posted 2026-09-06; especially the introduction and Section 10. https://arxiv.org/pdf/2609.06844

[2] P. Deshpande and R. Sawant, *Vertex decomposable complexes of directed forests, conflict graphs and chordality*, arXiv:2602.14936v1, first posted 2026-02-16. https://arxiv.org/pdf/2602.14936

[3] D. Jojić, *Shellability of complexes of directed trees*, arXiv:1109.4475v2 (2012), especially Section 2 citing Kozlov's complete-source theorem. https://arxiv.org/pdf/1109.4475

[4] S. Moradi and F. Khosh-Ahang, *Expansion of a simplicial complex*, arXiv:1601.00456 (2016), Definition 2.1 and Theorem 2.12. https://arxiv.org/abs/1601.00456

[5] P. Chebotarev and E. Shamis, *Matrix-Forest Theorems*, arXiv:math/0602575v2, directed matrix–forest theorem. https://arxiv.org/pdf/math/0602575

[6] *Equivariant matrix–forest character formula for graph Morse complexes*, published mathematical result (2026), especially the orbit-divisibility classification and complete-graph factorization. https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-equivariant-matrix-forest-character-formula-for-graph-morse-comp--0f531889a464
