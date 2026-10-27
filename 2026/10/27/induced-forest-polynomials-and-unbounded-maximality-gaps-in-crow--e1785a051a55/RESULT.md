# Induced-forest polynomials and unbounded maximality gaps in crown graphs

## Finding

For every integer \(n\ge3\), write \(\operatorname{Cr}_n=K_{n,n}-M_n\) for the crown graph with parts \(A=\{a_1,\ldots,a_n\}\) and \(B=\{b_1,\ldots,b_n\}\), in which \(a_i b_j\) is an edge if and only if \(i\ne j\). A set \(S\subseteq V(\operatorname{Cr}_n)\) is an **induced-forest set** if the subgraph induced by \(S\) has no cycle, and is **inclusion-maximal** if no proper superset is an induced-forest set. Set

\[
\Phi_n(z)=\sum_{S:\,\operatorname{Cr}_n[S]\text{ acyclic}}z^{|S|},\qquad
\Psi_n(z)=\sum_{S:\,S\text{ maximal induced forest}}z^{|S|}.
\]

**Theorem.** The full induced-forest polynomial is

\[
\boxed{\begin{aligned}
\Phi_n(z)={}&2(1+z)^n-1+2nz\big((1+z)^n-1\big)-n^2z^2\\
&+\binom n2(2n-3)z^4+n(n-1)(n-2)z^5.
\end{aligned}}
\]

The inclusion-maximal induced-forest polynomial is

\[
\boxed{\Psi_n(z)=\begin{cases}
6z^5,&n=3,\\
2nz^{n+1}+n(n-1)(n-2)z^5,&n\ge4.
\end{cases}}
\]

In particular, the crown graph is well-\(f\)-covered (all inclusion-maximal induced forests have the maximum possible order) exactly when \(n\in\{3,4\}\). For every \(n\ge5\), inclusion-maximal forests have precisely the two cardinalities \(5\) and \(n+1\), with the indicated multiplicities; hence the difference between largest and smallest cardinalities is \(n-4\), which grows without bound. Equivalently, the inclusion-minimal feedback-vertex-set polynomial is \(z^{2n}\Psi_n(z^{-1})\), giving cardinalities \(n-1\) and \(2n-5\) for \(n\ge5\).

## Assumptions and scope

Graphs are finite, undirected, simple, with labeled vertices. The deleted edges \(a_i b_i\), for \(1\le i\le n\), form a perfect matching. The parameter range is exactly \(n\ge3\); \(n=2\) is excluded because the graph then consists of two independent edges. Every coefficient counts actual vertex subsets, without identifying configurations under graph automorphisms.

For an induced set \(S\), put \(I=\{i:a_i\in S\}\), \(J=\{j:b_j\in S\}\), and \(a=|I|\), \(b=|J|\). The classification is as follows:

1. \(a\le1\) or \(b\le1\);
2. \(a=b=2\) and \(|I\cap J|\ge1\);
3. \((a,b)=(2,3)\) and \(I\subset J\), or \((a,b)=(3,2)\) and \(J\subset I\).

These three cases are disjoint and exhaust the induced forests. For \(n\ge4\), the inclusion-maximal sets are exactly (i) one full bipartition class together with one vertex of the opposite class, and (ii) the sets in case 3. For \(n=3\), only case 3 gives inclusion-maximal sets.

## Proof

**Step 1: acyclic induced-subgraph classification.** The induced subgraph on \(S\) has

\[
|E(\operatorname{Cr}_n[S])|=ab-|I\cap J|.
\]

If \(a\le1\) or \(b\le1\), this graph is a star and isolated vertices (possibly empty), so it is acyclic. If \(a\ge3\) and \(b\ge3\), then \(|I\cap J|\le\min(a,b)\), so its edge count is at least \(ab-\min(a,b)\ge a+b\). A forest on \(a+b\) vertices has at most \(a+b-1\) edges, proving that this regime is cyclic.

If \(a=2\) and \(b\ge4\), there are at least \(2b-2\ge b+2\) edges on \(b+2\) vertices, again forcing a cycle. The symmetric case is identical. For \((a,b)=(2,3)\), acyclicity requires \(|I\cap J|=2\), because otherwise there are at least five edges on five vertices. If \(I\subset J\), the induced graph is a path of length four: the unique unmatched index in \(J\) supplies a vertex adjacent to both selected \(A\)-vertices, while the other two \(B\)-vertices have degree one. The \((3,2)\) case is symmetric. Finally, for \(a=b=2\), no deleted edge within the selection gives a four-cycle, whereas at least one deleted edge leaves at most three edges on four vertices, hence a forest. This proves the three-case characterization for all \(n\ge3\).

**Step 2: enumerate all forests.** Subsets with one side empty contribute \(2(1+z)^n-1\). Those with \(a=1\) and \(b\ge1\) contribute \(nz((1+z)^n-1)\); the other orientation with \(b=1\) and \(a\ge2\) contributes \(nz((1+z)^n-1-nz)\), avoiding double-counting pairs with \(a=b=1\). For \(a=b=2\), select \(I\) freely and select \(J\) among all two-subsets meeting \(I\):

\[
\binom n2\!\left(\binom n2-\binom{n-2}{2}\right)=\binom n2(2n-3).
\]

For \((a,b)=(2,3)\) there are \(\binom n2(n-2)\) configurations; the reverse orientation has the same count, giving \(n(n-1)(n-2)\). Summing the disjoint cases proves the formula for \(\Phi_n\).

**Step 3: inclusion-maximality.** Any forest with one side empty can be extended by a vertex on the other side. Any forest with \(a=1\) and \(b<n\) can be extended by an omitted \(B\)-vertex; the symmetric statement holds. A forest with \(a=b=2\) can always be extended: if \(|I\cap J|=1\), adjoin the missing member of \(I\) to \(J\); if \(|I\cap J|=2\), adjoin an index outside \(I\) to \(J\), possible because \(n\ge3\). The resulting \((2,3)\) forest remains acyclic.

Every \((2,3)\) forest with \(I\subset J\) is maximal: adjoining another \(B\)-vertex enters the cyclic \((2,b)\) regime with \(b\ge4\), and adjoining another \(A\)-vertex enters the cyclic \((a,b)\) regime with both sizes at least three. Symmetrically, every \((3,2)\) forest is maximal. A forest of the form \(\{a_i\}\cup B\) can be extended when \(n=3\), because adjoining another \(A\)-vertex produces a \((2,3)\) forest; it is maximal for \(n\ge4\), because any such addition produces a cyclic \((2,n)\) induced graph. The symmetric statement holds. Therefore the two full-side families contribute \(2nz^{n+1}\) for \(n\ge4\); the \((2,3)\) families contribute \(n(n-1)(n-2)z^5\) for all \(n\ge3\). This proves \(\Psi_n\).

For \(n=3\) all maximal configurations have size five. For \(n=4\) both displayed terms have degree five. For every \(n\ge5\) the two positive coefficients have distinct degrees five and \(n+1\). This proves the well-\(f\)-covered classification and the unbounded gap.

## Verification

The standalone file `verify.py` constructs every crown graph directly from adjacency pairs and checks induced acyclicity by a disjoint-set cycle detector for all \(2^{2n}\) subsets, for each \(3\le n\le8\). It separately identifies inclusion-maximal acyclic sets by checking each omitted vertex, and compares complete coefficient dictionaries to both formulas. The standalone finite computation inspected 87,360 subsets; all cases matched, including the coincidences at \(n=3\) and \(n=4\). Run `python3 verify.py` from a directory containing this source. This is a finite consistency check; the proof above establishes the universal quantification.

## Relationship to prior work

Jafarpour-Golzari (2021) introduced well-\(f\)-covered graphs and determined several classes of graphs with uniform maximal induced-forest size, including complete bipartite graphs. The present result concerns a different family obtained by deleting an entire perfect matching from a balanced complete bipartite graph. That edge deletion changes the inclusion-maximal forest spectrum: the uniform-order property survives only at the first two connected crown orders. The same author's subsequent work on lexicographic products (2021) studies a different graph operation. The theorem above supplies the full cardinality enumerator as well as the maximal-set classification, rather than only the minimum feedback-vertex-set size or a well-\(f\)-covered decision. The induced-forest polynomial also encodes the counts of *all* feedback vertex sets through complementing selected vertices.

## Limitations

The proof applies to crowns with a complete deleted matching and \(n\ge3\); it does not classify arbitrary partial-matching deletions or unbalanced bipartite graphs. The exhaustive program checks only \(3\le n\le8\), not the infinite domain. Priority checks covered accessible and indexed material; lack of a discovered equivalent source is not a proof of absolute novelty. Independent scientific audit has not been performed.

## References

- R. Jafarpour-Golzari, *Graphs whose all maximal induced forests are of the same order*, arXiv:2105.14339, first publicly posted 29 May 2021. https://arxiv.org/abs/2105.14339
- R. Jafarpour-Golzari, *On well-f-coveredness of lexicographic product of graphs*, arXiv:2108.09146, first publicly posted 20 August 2021. https://arxiv.org/abs/2108.09146
