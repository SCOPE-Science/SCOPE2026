# Exact simple and subdirectly-irreducible loop spectra on temporal Hasse trees

## Finding

**Theorem (complete finite Hasse-tree loop classification).** Fix a finite nonempty poset \(P\) with \(n\) vertices such that its undirected Hasse graph is a tree. Write \(M=\operatorname{Min}(P)\) and \(m=|M|\). Each subset \(L\subseteq P\) determines a finite temporal transit and its dual temporal Heyting algebra \(A(P,L)\). For each \(r\in M\), let \(F_r\) be the set of upper endpoints \(v\) of covers \(u\prec v\) for which the unique tree path from \(r\) to \(u\) traverses \(v\) first (equivalently, the graph distance from \(r\) to \(v\) is smaller than that to \(u\)). Then:

1. The algebra \(A(P,L)\) is simple if and only if \(L\subseteq M\). Its exact loop-number enumerator is \(S_P(t)=(1+t)^m\).
2. The algebra \(A(P,L)\) is subdirectly irreducible if and only if \(L\cap F_r=\varnothing\) for at least one \(r\in M\). Its exact loop-number enumerator is
\[
I_P(t)=\sum_{\varnothing\ne E\subseteq M}(-1)^{|E|+1}(1+t)^{n-|\bigcup_{r\in E}F_r|}.
\]

These are exact classifications for all loop decorations of every Hasse-tree poset, including the one-vertex case. In particular, evaluating at \(t=1\) gives the numbers of simple and subdirectly-irreducible decorations; coefficient extraction counts decorations with a fixed number of loops.

## Assumptions and scope

A cover \(u\prec v\) means \(u<v\) with no element strictly between. The temporal transit on \(P\) has order \(\le\), forward relation \(R=(<)\cup\{(v,v):v\in L\}\), and backward relation \(R^{-1}\); the finite discrete order topology makes it a temporal Esakia space. The associated algebra \(A(P,L)\) is the algebra of its upsets with the temporal operations supplied by the established duality. The fixed poset \(P\) is not varied. Loop choices are distinct structures on that fixed carrier, even if an automorphism of \(P\) exchanges some choices; the displayed polynomials do not count automorphism orbits. A one-vertex poset has \(M=P\) and \(F_r=\varnothing\).

For a finite poset with arbitrary Hasse graph, define a directed graph \(D(P,L)\) by placing \(u\to v\) at every cover \(u\prec v\) and placing \(v\to u\) at that cover if and only if \(v\notin L\). We use the following cover-graph representation of the reachability relation \(Z\) in Alvarez's finite-transit characterisation:
\[
x\,Z\,y\quad\Longleftrightarrow\quad y\text{ is reachable from }x\text{ in }D(P,L).
\]

## Proof

**Cover representation.** The finite-transit step relation of Alvarez is \(x B w\) if and only if \(w\le x\) and the half-open order interval \((w,x]\) contains no looped point. The author defines \(Z\) as the reflexive transitive closure of \(B;\le\). For each cover \(u\prec v\), the upward arc \(u\to v\) is a step of \(B;\le\), since \(u B u\) and \(u\le v\). If \(v\notin L\), then \(v B u\), so the downward arc \(v\to u\) is also a step. Thus every \(D(P,L)\)-path is a \(Z\)-path. Conversely, if \(x B w\le y\), choose a saturated cover chain descending from \(x\) to \(w\). Each upper endpoint on the chain lies in \((w,x]\), hence is not looped and admits a downward arc. Then ascend along any saturated chain from \(w\) to \(y\). The concatenation is a directed \(D(P,L)\)-path. Closing under concatenation proves the representation for every finite poset, not only trees.

**Simplicity.** By the existing finite temporal-Heyting duality, \(A(P,L)\) is simple exactly when \(Z\) is connected in both directions between every pair. A directed graph whose underlying undirected graph is a tree is strongly connected only if every tree edge is available in both directions: otherwise the edge separating the two components after its removal prevents any directed return across its cut. The converse is immediate. Our orientation has a downward arc \(v\to u\) exactly if the upper endpoint \(v\) is not looped. Every nonminimal vertex is the upper endpoint of at least one cover. Hence all edges are bidirectional exactly when \(L\) consists only of minimal vertices. Each of the \(m\) minimal vertices may be looped independently. Their loop-number polynomial is \((1+t)^m\).

**Roots and the subdirectly-irreducible condition.** The existing finite duality says that \(A(P,L)\) is subdirectly irreducible exactly when some vertex reaches all vertices via \(Z\). If some vertex \(x\) reaches all, choose any minimal \(r\le x\). An upward cover chain gives a directed path from \(r\) to \(x\), so \(r\) also reaches all. Thus it suffices to test minimal roots.

Fix \(r\in M\). Because the Hasse graph is a tree, its unique simple undirected path from \(r\) to any vertex must be traversable in the directed graph if \(r\) reaches that vertex. Every step upward along \(\le\) is automatically traversable. A step downward at a cover \(u\prec v\) is traversable precisely when \(v\notin L\). The downward steps in all paths starting at \(r\) occur exactly at covers for which \(v\) is closer to \(r\) than \(u\); their upper endpoints form \(F_r\). It follows that \(r\) reaches all vertices if and only if \(L\cap F_r=\varnothing\), proving the structural criterion.

For each \(r\in M\), the admissible loop sets for which \(r\) is a universal root form the Boolean family \(\{L:L\subseteq P\setminus F_r\}\), with loop-weight polynomial \((1+t)^{n-|F_r|}\). The subdirectly-irreducible decorations form the union of these families. Finite inclusion-exclusion therefore gives exactly the stated formula for \(I_P(t)\), coefficient by coefficient.

## Verification

The standalone `checker.py` enumerates all labelled posets of sizes one through five (respectively \(1,3,19,219,4231\) posets), all their loop assignments, and the relevant tree cases (respectively \(1,2,12,128,2000\) labelled Hasse-tree posets). It independently compares reachability computed by the original \(B;\le\) relation against directed cover-graph reachability, checks simplicity by all-pairs reachability, checks the universal-root condition, and compares the two counts with the formulas above. The completed check prints `ALL_CHECKS_OK`. Exhaustive finite checks are supportive consistency tests, not proofs of the unrestricted theorem; the preceding reasoning proves the arbitrary finite case.

For a four-vertex Hasse path with covers \(a\prec d\), \(b\prec c\prec d\), the formula gives four simple and eight subdirectly-irreducible loop decorations. This shows that the two criteria genuinely distinguish different natural strata even among Hasse trees with two minimal vertices.

## Relationship to prior work

Alvarez introduced the finite temporal-transit relation \(B\), established the reachability relation \(Z\), and proved that simple finite temporal Heyting algebras correspond to \(Z\)-connected finite frames, while subdirectly-irreducible ones correspond to \(Z\)-rooted frames. Those foundational characterisations, the duality, and their algebraic consequences are prior work; this theorem does not claim them as new. The contribution here is the uniform local cover-graph representation and the **complete weighted loop-decorations classification for every Hasse-tree poset**, expressed by concrete forced vertex sets and an exact inclusion-exclusion polynomial.

Earlier classifications of looped ordinal sums of antichains concern a different poset family and already determine its simple/subdirectly-irreducible cases; the present theorem does not claim those cases as new. On a chain, the current formulas specialize to existing results. The general arbitrarily oriented Hasse-tree formula is not a corollary of the ordinal-sum classification without the independent tree-path argument.

## Limitations

The exact polynomial counts loop decorations on a fixed poset, not unlabelled frame isomorphism types and not arbitrary-poset congruence lattices. The finite Hasse-tree hypothesis is essential for the unique-path proof; the cover-graph reachability representation itself holds for all finite posets. Similar results could occur in older directed-tree reachability literature under different vocabulary. This result has been checked in the same mathematical review process, not independently audited or certified.

## References

1. D. Q. Alvarez, *A dual characterisation of simple and subdirectly-irreducible temporal Heyting algebras*, arXiv:2505.08014, first posted 2025-05-12. Journal version: *Algebra Universalis* 87, article 36 (2026), doi:10.1007/s00012-026-00939-6. Specifically, finite transit definitions and the finite \(Z\)-connected/\(Z\)-rooted dual characterisations.
2. D. Q. Alvarez, *The temporal Heyting calculus*, Master's thesis, University of Amsterdam (2024), cited for the preceding development of temporal Heyting semantics; no new theorem from that thesis is asserted here.
