# Seven rank-three theories of halved cubes and a sharp 64-vertex representative

## Finding
For each integer \(d\geq 1\), let \(H_d\) be the finite simple graph whose vertices are the even-cardinality subsets of \(\{1,\ldots,d\}\), with adjacency \(E(X,Y)\) exactly when \(|X\triangle Y|=2\). Let \(\equiv_3\) mean agreement on all first-order sentences of quantifier rank at most three in the language of adjacency and equality (no coordinate names and no counting quantifiers). Then

\[
H_d\equiv_3 H_e\quad\Longleftrightarrow\quad\min(d,7)=\min(e,7).
\]

Therefore precisely seven rank-three theories occur. Their least-dimensional representatives are \(H_1,H_2,H_3,H_4,H_5,H_6,H_7\), of respective orders \(1,2,4,8,16,32,64\). The largest order among these least-order representatives is 64, and no smaller member of this family represents the last class.

## Assumptions and scope
All dimensions are positive integers; every vertex is an even subset, including the empty subset. The sole nonlogical relation is symmetric, irreflexive adjacency. Formulas may use arbitrarily many variables and Boolean operations, but their maximum *nesting depth* of quantifiers is at most three. This is ordinary first-order logic, not first-order logic with counting or with a named coordinate system. The sharpness statement is relative to the family of halved cubes, not to arbitrary finite graphs.

## Proof
**1. Pair-extension profiles.** Given two vertices \(X,Y\), a third vertex \(Z\), distinct from both, has one of four adjacency signatures \((a,b)\in\{0,1\}^2\), where \(a=1\) means \(E(X,Z)\), and \(b=1\) means \(E(Y,Z)\). Write \(P_d(X,Y)\) for the set of signatures attained by such \(Z\). At quantifier rank one with the pair \((X,Y)\) named, the complete type is determined by \(X=Y\), by \(E(X,Y)\), and by \(P_d(X,Y)\): these data specify which quantifier-free configurations of the third vertex exist, including configurations where it equals either named vertex.

The transformations \(U\mapsto U\triangle X\) and coordinate permutations preserve the graph. Consequently it suffices to take \(X=\varnothing\) and \(Y=D\) with \(|D|=2t\), where \(0\leq t\leq\lfloor d/2\rfloor\). Put \(P_d(t)=P_d(\varnothing,D)\).

For \(t=0\), signature \((1,1)\) exists exactly when \(d\geq2\) (a two-element \(Z\)), and \((0,0)\) exactly when \(d\geq4\) (a four-element \(Z\)); the other two are impossible. For \(t\geq1\), the full existence table is:

| Signature | Exact condition for membership in \(P_d(t)\) |
| --- | --- |
| \((1,1)\) | \(t=1\) and \(d\geq3\), or \(t=2\) |
| \((1,0)\) and \((0,1)\) | \(t=1,d\geq4\), or \(t=2,d\geq5\), or \(t\geq3\) |
| \((0,0)\) | \(t=1,d\geq5\), or \(t=2,d\geq6\), or \(t=3,d\geq7\), or \(t\geq4\) |

Here \(d\geq2t\) is implicit. To prove the table, assume \(X=\varnothing\). Any neighbor \(Z\) of \(X\) has cardinality two. Its distance to \(D\) is \(2t+2-2|Z\cap D|\); thus a common neighbor exists only for \(t=1\) or \(t=2\). For \(t=1\), one element of \(D\) and one outside give \((1,1)\), requiring \(d\geq3\); for \(t=2\), any two inside \(D\) give \((1,1)\). For \((1,0)\), take a two-subset disjoint from \(D\) when \(t=1,d\geq4\), a two-subset meeting \(D\) once when \(t=2,d\geq5\), or any two-subset of \(D\) for \(t\geq3\). Symmetry gives \((0,1)\); the excluded smaller cases have no such two-subset.

For \((0,0)\), explicit four-element witnesses are: one point inside \(D\) and three outside for \(t=1,d\geq5\); two inside and two outside for \(t=2,d\geq6\); three inside and one outside for \(t=3,d\geq7\); and four inside \(D\) for \(t\geq4\). Each of these is at Hamming distance at least four from both \(X\) and \(Y\). Conversely, in the three excluded borderline cases, \((t,d)=(1,4),(2,5),(3,6)\), every other even subset is either of size two or at distance two from \(D\). The smaller cases are immediate. This proves the complete table for *every* dimension, without finite extrapolation.

**2. Stabilization.** For every \(d\geq7\), the table produces exactly these four types of ordered pairs:

| Relation between \(X,Y\) | Set \(P_d(X,Y)\) |
| --- | --- |
| \(X=Y\) | \(\{(1,1),(0,0)\}\) |
| \(E(X,Y)\) | \(\{(1,1),(1,0),(0,1),(0,0)\}\) |
| \(|X\triangle Y|=4\) | \(\{(1,1),(1,0),(0,1),(0,0)\}\) |
| \(|X\triangle Y|\geq6\) | \(\{(1,0),(0,1),(0,0)\}\) |

The two identical signature sets in the middle remain distinct pair types because one pair is adjacent and the other is not. Each of the four types is realized in *every* dimension at least seven. To play a three-round Ehrenfeucht–Fraïssé game between any \(H_d,H_e\) with \(d,e\geq7\), Duplicator responds to the first vertex arbitrarily (vertex transitivity). After the second vertex, Duplicator matches the complete ordered-pair rank-one type using the same four-type inventory. For the third move, the equalities with earlier vertices or the demanded pair of adjacency bits can be matched by the pair profile. This is a partial isomorphism of the three selected vertices, so Duplicator wins. Hence all dimensions at least seven are equivalent at rank three.

**3. Sharp separation.** Define \(A_{ab}(x,y,z)\) to mean that \(z\ne x,y\) and that the adjacency bits of \(z\) to \(x,y\) are \((a,b)\), respectively. For each threshold, the following first-order property has quantifier rank at most three and holds in \(H_d\) *if and only if* \(d\) is at least the displayed threshold:

| Threshold | Property |
| --- | --- |
| \(2\) | Two distinct vertices exist. |
| \(3\) | Three distinct vertices exist. |
| \(4\) | Two distinct nonadjacent vertices exist. |
| \(5\) | Some adjacent \(x,y\) admit a \(z\) with \(A_{00}(x,y,z)\). |
| \(6\) | Some distinct nonadjacent \(x,y\) admit a \(z\) with \(A_{00}(x,y,z)\). |
| \(7\) | Some distinct nonadjacent \(x,y\) have no \(z\) with \(A_{11}(x,y,z)\) but have a \(w\) with \(A_{00}(x,y,w)\). |

The last assertion uses the same two outer quantifiers and two separate depth-one subformulas, so its quantifier rank is three, not four. Each exact threshold follows from the pair-profile table, and the first two from the cardinality \(|V(H_d)|=2^{d-1}\). Because these six truth values form distinct increasing prefixes, all \(H_1,\ldots,H_7\) are pairwise rank-three inequivalent. Combined with stabilization this proves the theorem. The orders double with dimension, so 64 is the least available representative order for the stabilized class. \(\square\)

## Verification
Run `python3 verify.py` from the directory containing this result and the standalone program. The program constructs even-weight binary words, computes every rank-one ordered-pair type from all possible third vertices, forms rooted rank-two types, and forms unpointed rank-three types for dimensions one through nine. A second coordinate-orbit method checks dimensions one through thirteen, the six exact distinguishing predicates, and stability of all distance-at-least-six pair profiles. Expected final line: `VERIFY_OK`.

The finite tests do not prove stabilization in arbitrary dimension; that conclusion comes from the complete support-count table and the three-round game argument above.

## Relationship to prior work
Krotov (2008) works with the distance-two graph of a binary cube and the two halved-cube components, investigating perfect two-colorings (particularly in dimension 24), not finite-model-theoretic quantifier-rank classes. Chepoi, Labourel and Ratel (2017) study subgraph density and clique VC-dimension in halved cubes, again without the present bounded-rank classification. Wen and Huang (2021) study Terwilliger algebras of halved cubes and record their distance-regular combinatorics, but their representation-theoretic conclusions do not determine ordinary first-order rank-three equivalence. The present result instead uses the signs of existence in four two-point extension cells, including the distinctive six-dimensional antipodal exception. Ordinary rank-three logic becomes insensitive to all dimension growth from seven onward, despite the strictly increasing graph degree \(\binom d2\); this contrast explains why a bounded-rank invariant rather than exact intersection numbers is the appropriate target.

## Limitations
This theorem is confined to the pure adjacency/equality signature, ordinary first-order quantifier rank three, and the halved-cube family of positive dimensions. It does not assert indistinguishability in first-order counting logic, at quantifier rank four, with named coordinates, or among arbitrary graphs. The smallest representative bound is family-relative. The literature comparison is not a proof that every unindexed or inaccessible work omits an equivalent formulation.

## References
1. Denis S. Krotov, *On perfect colorings of the halved 24-cube*, arXiv:0803.0068, first posted 2008-03-02, https://arxiv.org/abs/0803.0068. See the introduction for the halved-cube graph construction and Sections 4–6 for the actual perfect-coloring questions.
2. Victor Chepoi, Arnaud Labourel, and Sébastien Ratel, *On density of subgraphs of halved cubes*, arXiv:1711.11414, first posted 2017-11-30, https://arxiv.org/abs/1711.11414. See the introduction and Sections 3–6 on 1,2-inclusion graphs and clique VC-dimension.
3. Chia-Yi Wen and Hau-Wen Huang, *The Terwilliger algebra of the halved cube*, arXiv:2109.02021, first posted 2021-09-05, https://arxiv.org/abs/2109.02021. See Definition 2.1 and the decomposition results.
