# Mixed-dimensional two-independence homotopy of the triangular graphs \(T_5,T_6,T_7\)

## Finding

For \(n\in\{5,6,7\}\), let \(T_n=L(K_n)=J(n,2)\) have as vertices the two-element subsets of \([n]\), adjacent when they intersect. Let \(X_n=\operatorname{Ind}_2(T_n)\) be the simplicial complex of sets of these vertices whose induced graph components have at most two vertices. Then, as integral homotopy equivalences,

\[
X_5\simeq\bigvee^{6}S^1,\qquad
X_6\simeq\bigvee^{24}S^2\vee\bigvee^{10}S^3,\qquad
X_7\simeq\bigvee^{400}S^3.
\]

In particular the first case in this three-term range permitting two vertex-disjoint selected two-edge paths has nonzero **integral homology in two adjacent positive degrees**, while the next case has homology concentrated in one degree. The exact middle classification is more than a field-homology or Euler-characteristic calculation.

## Assumptions and scope

Graphs are finite, simple and undirected, and \(n\) ranges **only** over \(5,6,7\). The vertices of \(T_n\) are the edges of the complete graph \(K_n\); a face of \(X_n\) is a set of such edges in which each chosen edge meets at most one other chosen edge. Equivalently, the selected-edge subgraph of \(K_n\) is a disjoint union of isolated edges and two-edge paths, with isolated original vertices ignored. This is a \(P_3\)-devoid complex on \(T_n\): a prohibited \(P_3\) need not be induced. The parameter is \(2\), not the ordinary matching complex \(\operatorname{Ind}_1(T_n)\), and not the two-matching complex allowing vertex degree two within arbitrarily long paths.

Order the \(\binom n2\) edges of \(K_n\) lexicographically, starting with the pair \((0,1)\). Encode each nonempty face as a bitmask in that order. Every computation below is exact and finite.

## Proof

**Step 1 (exhaustive face sets).** Test every nonzero bitmask below \(2^{\binom n2}\). The primary membership test checks that every chosen edge has at most one neighbor among the other chosen edges in \(T_n\). An independent membership test computes the connected components among chosen edges and checks that each contains at most two elements. Both agree on every bitmask. The \(f\)-vectors, indexed by dimensions beginning at zero, are

\[
(f_0,f_1,f_2)(X_5)=(10,45,30),
\quad(f_0,f_1,f_2,f_3)(X_6)=(15,105,195,90),
\]
\[
(f_0,f_1,f_2,f_3)(X_7)=(21,210,735,945).
\]

Checking each valid face against all possible one-vertex extensions gives exactly 30 facets of dimension two for \(X_5\), 15 facets of dimension two and 90 of dimension three for \(X_6\), and 945 facets of dimension three for \(X_7\). The 15 lower-dimensional facets of \(X_6\) are the perfect matchings in \(K_6\); the 90 maximal four-edge faces are partitions into two two-edge paths. Thus the middle complex is nonpure, while the next is pure.

**Step 2 (explicit acyclic matching).** Initially mark all nonempty faces unmatched. For each coordinate \(i=0,1,\ldots,\binom n2-1\), in increasing numerical order of faces, match any still-unmatched face \(\sigma\) not containing coordinate \(i\) to \(\sigma\cup\{i\}\) if the latter is still unmatched; delete both from the unmatched set. This completely specifies every matching pair. For independent validation, orient the entire nonempty-face Hasse diagram downwards except for matched incidences, which are reversed. A topological sort visits **every** face, proving acyclicity rather than assuming it from the matching construction. The resulting totals are:

| Complex | Nonempty faces | Hasse incidences | Matched pairs | Critical cells by dimension |
| --- | ---: | ---: | ---: | --- |
| \(X_5\) | 85 | 180 | 39 | one in dimension 0, six in dimension 1 |
| \(X_6\) | 405 | 1,155 | 185 | one in dimension 0, 24 in dimension 2, ten in dimension 3 |
| \(X_7\) | 1,911 | 6,405 | 747 | one in dimension 0, eight in dimension 2, 408 in dimension 3 |

**Step 3 (integral Morse boundaries).** Every simplex is oriented by ascending coordinate order. The critical integral boundary maps are calculated by the signed recursive gradient-path substitution on the matched pairs. Independently, the code performs an exact integer Schur-complement cancellation of every matched pair, with each pivot checked to be \(\pm1\). The two resulting critical boundary maps agree entry-by-entry. For \(X_5\) and \(X_6\) all remaining boundary maps are zero. Thus the Morse CW complex for \(X_5\) is a wedge of six circles; for \(X_6\) it consists of one vertex, 24 two-cells attached at that vertex, and ten three-cells with zero boundary degrees. Because the Hurewicz map \(\pi_2(\bigvee^{24}S^2)\to H_2(\bigvee^{24}S^2;\mathbb Z)\) is an isomorphism, each three-cell attaches nullhomotopically. This proves the stated *integral homotopy*, not just homology, of \(X_6\).

For \(X_7\), the exact critical boundary \(C_3\to C_2\) has size \(8\times408\), 528 nonzero integer entries and exactly 202 nonzero columns. The columns with zero-based positions

`[9,14,15,17,26,37,38,72]`

form this displayed minor in the ordered critical bases:

```text
-1  0  0  1  1  0  0  0
 1  0  0  0  0  0  0  0
 0  0  1  0  0  0  0  0
 0  1  1  1  0  1  1  1
 0 -1 -1 -1 -1 -1 -1 -1
 0  0  0  0  0  1  0  0
 0  0  0  0  0  0  1  0
 0  0  0  0  0  0  0  1
```

Its **integer determinant is \(-1\)**. Thus the attaching-degree homomorphism is split-surjective over \(\mathbb Z\). Since \(\pi_2(\bigvee^8 S^2)\cong\mathbb Z^8\), unimodular row and column transformations can be realized by homotopy equivalences of wedges of two-spheres. Eight three-cells consequently cancel the eight two-cells up to homotopy, leaving 400 free three-cells. Therefore \(X_7\simeq\bigvee^{400}S^3\).

## Verification

Run `python3 verify.py` with Python 3.10 or newer and no external packages. The program exhaustively enumerates all ambient subsets for each of the three complete graphs, tests two equivalent face predicates independently, reconstructs the face-poset matching, checks all Hasse incidences for directed acyclicity, reconstructs the **integer** critical boundary by two independent elimination algorithms, and evaluates the displayed determinant using fraction-free integer arithmetic. Its deterministic expected output is embedded in `verified_output.txt`; successful execution ends with `ALL_CHECKS_PASS`. The exact code, not an unverified log, constitutes the checkable finite certificate.

## Relationship to prior work

Taylan introduced graph path-devoid complexes and acyclic matching-tree methods and classified path-, forest- and cycle-based examples, but not the \(P_3\)-devoid complexes of triangular line graphs here. Deshpande and Singh developed higher-independence homotopy classifications for complete multipartite graphs, fully whiskered graphs, paths, cycles and perfect arity trees; none of these graph families contains \(T_5,T_6,T_7\). The ordinary matching complex \(\operatorname{Ind}(T_n)\) and published neighborhood- or cut-complex calculations on triangular graphs use different face conditions; their conclusions do not imply the displayed mixed-dimensional result. The equivalence between the path-devoid and higher-independence formulations is acknowledged, not treated as novelty. Searches did not identify a previously published classification with the same objects and parameters, but unindexed equivalent results remain possible.

## Limitations

These proofs cover only \(n=5,6,7\). They do not give a recurrence or general homotopy classification for larger triangular graphs. They do not calculate full symmetric-group actions, cup products for other families, or the homotopy type of arbitrary \(r\)-independence complexes. The scientific and novelty assessment has not received independent verification; absence of a retrieved source cannot establish absolute publication priority.

## References

- Demet Taylan, *Matching trees for simplicial complexes and homotopy type of devoid complexes of graphs*, arXiv:1501.06754v1, first posted 2015-01-27, https://arxiv.org/abs/1501.06754 .
- Priyavrat Deshpande and Anurag Singh, *Higher Independence Complexes of graphs and their homotopy types*, arXiv:2001.05448, first posted 2020-01-15, https://arxiv.org/abs/2001.05448 .
- *Triangular Graph*, MathWorld, for the standard identifications \(T_n=L(K_n)=J(n,2)\), https://mathworld.wolfram.com/TriangularGraph.html .
