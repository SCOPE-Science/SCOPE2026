# Four-round logical invisibility of projective-plane incidence graphs

## Finding
Let \(\Pi\) and \(\Pi'\) be **any** finite projective planes of orders at least \(2\), including non-Desarguesian planes. Write \(L(\Pi)\) for the **uncoloured** simple bipartite graph whose vertices are the points and lines of \(\Pi\), adjacent precisely when incident. In the first-order language containing only graph adjacency and equality,
\[
L(\Pi)\equiv_4 L(\Pi').
\]
This uniform four-round invisibility is sharp for the Fano plane \(\mathrm{PG}(2,2)\) and the ternary plane \(\mathrm{PG}(2,3)\): their Levi graphs are rank-four equivalent but **not** rank-five equivalent. If the point and line sorts are named by unary predicates, the same two planes are equivalent through rank three but are distinguishable at rank four. Thus retaining the geometric sorts advances the first distinguishing rank of this pair by exactly one.

Here \(A\equiv_r B\) means agreement on every first-order sentence of quantifier rank at most \(r\), without a restriction on the number of free-variable occurrences or formula length. The assertion is not about counting logic, higher-order logic, or arbitrary bipartite graphs.

## Assumptions and scope
A finite projective plane of order \(q\ge2\) has \(q^2+q+1\) points and the same number of lines. Every point is on \(q+1\) lines and every line contains \(q+1\) points; distinct points lie on exactly one common line, and distinct lines meet at exactly one common point. Its Levi graph is loopless, bipartite, regular of degree \(q+1\), and has \(2(q^2+q+1)\) vertices. The proof uses only these axioms and their point-line duals.

Let \(\tau_r^G(v_1,\ldots,v_k)\) denote the depth-\(r\) one-point-extension type of an ordered vertex tuple. Define \(\tau_0\) as the complete equality/adjacency diagram. Recursively define
\[
\tau_{r+1}^G(\bar v)=\Bigl(\tau_0^G(\bar v),\,\{\tau_r^G(\bar v,w):w\in V(G)\}\Bigr).
\]
Types are compared up to a common canonical naming across structures; the braces denote a **set**, not a multiset. Standard Ehrenfeucht–Fraïssé semantics imply that two empty tuples have the same depth-\(r\) type precisely when their graphs are \(\equiv_r\). A repeated vertex in an extension is allowed, and its equality data is retained.

## Proof
**1. Universal one-step profiles of triples.** In an uncoloured Levi graph, the depth-one type of every ordered triple is determined by one of the following \(24\) geometric profiles, independent of plane order.

* If all three positions coincide, there is one profile.
* If exactly two positions coincide, there are three choices of the repeated-position pair and three kinds of the remaining distinct pair: adjacent, nonadjacent on the same side, or nonadjacent on opposite sides. This gives nine profiles.
* If all three vertices are distinct on one bipartition side, there are two profiles: the corresponding three points are collinear, or the three lines concurrent, versus not. Duality identifies the point and line descriptions at this logical depth.
* If all three vertices are distinct and occupy both sides, there is one position for the minority-side vertex (three choices), and its incidence vector to the other two vertices has any of the four values \((0,0),(0,1),(1,0),(1,1)\). These give twelve profiles.

To verify the assertion rather than only count configurations, take three distinct vertices all on the same side. If they share a common opposite-side neighbor, their only possible adjacency masks for a fresh fourth vertex are: no adjacency, adjacency to a specified single vertex, or adjacency to all three. In particular, a fresh vertex adjacent to exactly two of the three does **not** exist. If they do not share such a neighbor, the possible masks are: none, any specified singleton, or any specified pair; adjacency to all three is impossible. The singleton masks in the nonconcurrent case occur because each point has \(q+1\) lines, only two of which join it to the other chosen points, leaving \(q-1\ge1\). The concurrent/collinear case also leaves \(q\ge2\) singly incident alternatives. The zero mask is realized by an additional vertex on the already chosen side.

For a mixed triple, by point-line duality write its two same-side vertices as distinct points \(x,y\) and its other vertex as a line \(\ell\). A fresh point can have mask \(\varnothing\) or \(\{\ell\}\); both occur because \(\ell\) contains at least three points and there are points off \(\ell\). A fresh line can have masks \(\varnothing\), \(\{x\}\), \(\{y\}\), and, **if and only if** \(\ell\ne xy\), \(\{x,y\}\), where \(xy\) is the unique line through both points. Each singleton option has at least \(q-1\) witnesses after excluding \(\ell\). The zero option has at least \(q(q-1)-1\ge1\) witnesses: there are \(q(q-1)\) lines through neither point. The line \(xy\) gives the two-point mask when it is not already named. Equality extensions are handled separately by the complete atomic diagram. Every listed mask is attainable at \(q=2\), and the inequalities show attainability for all \(q\ge2\).

These profile labels really distinguish different depth-one types: equality and existing adjacency recover the repeated/mixed patterns, a common-neighbor query recognizes same-side pairs, and a fourth common neighbor distinguishes collinear/concurrent triples from noncollinear/nonconcurrent ones. Thus there are exactly \(1+9+2+12=24\) profiles, realized in every finite projective plane of order at least two.

**2. Universal two-step profiles of pairs.** For an ordered pair \((x,y)\), the depth-two type depends only on which of four cases holds: \(x=y\), adjacent, distinct nonadjacent vertices on the same side, or distinct nonadjacent vertices on opposite sides. Indeed, the depth-one triple extensions are precisely the available profiles from part 1. For two distinct same-side vertices, an added same-side vertex may be collinear/concurrent with them or not (both are possible). A fresh opposite-side vertex may be incident to both, exactly either one, or neither. The unique joining line/intersection supplies the first option; \(q\ge2\) and the \(q(q-1)\) vertices missing both ensure the remaining options. For an opposite-side point–line pair, a fresh point may lie on or off the line, and a fresh line may pass through or miss the point. All these alternatives exist independently of whether the selected point lies on the selected line. Repetitions are always available. Consequently the **sets** of the 24 available extension profiles depend only on the stated pair case, not on the plane. They are distinct because adjacency/equality distinguishes two cases and existence of a common neighbor distinguishes the two nonadjacent cases.

**3. Root type.** Every vertex has a copy of each of the four depth-two pair-extension kinds: itself, an adjacent vertex, a different vertex on the same side, and a nonincident vertex on the other side. Hence all single vertices in all the graphs have the same depth-three type. The empty tuple therefore has one common depth-four type, proving the universal equivalence.

**4. Sharpness and the effect of naming sorts.** The rank-five graph sentence stating that some vertex has **four distinct neighbors**, namely
\[
\exists v\,\exists w_1\,\exists w_2\,\exists w_3\,\exists w_4\,
\Bigl(\bigwedge_{i<j}w_i\ne w_j\;\land\;\bigwedge_{i=1}^{4}E(v,w_i)\Bigr),
\]
is false in the degree-three Fano Levi graph and true in the degree-four Levi graph of \(\mathrm{PG}(2,3)\). The first distinguishing rank of this pair in the uncoloured language is therefore exactly five.

In the expanded language with unary predicates \(P\) (point) and \(Q\) (line), the two planes are indistinguishable through rank three: the same extension-profile argument for **ordered pairs with named sides** gives universal depth-one pair profiles, then universal singleton and empty-tuple types. But the following depth-four sentence separates them:
\[
\begin{aligned}
\exists \ell_1\exists \ell_2\exists \ell_3\;[&\bigwedge_{i=1}^{3}Q(\ell_i)\land\bigwedge_{i<j}\ell_i\ne\ell_j\\
&\land\exists p\bigl(P(p)\land\bigwedge_{i=1}^{3}E(p,\ell_i)\bigr)\\
&\land\exists z\bigl(P(z)\land\bigwedge_{i=1}^{3}\neg E(z,\ell_i)\bigr)].
\end{aligned}
\]
It asks for three concurrent lines with a point off their union. In a projective plane of order \(q\), three distinct lines through one point cover \(1+3q\) points, leaving exactly \(q(q-2)\) points off their union. Thus this sentence is false for \(q=2\) and true for every \(q\ge3\) for which a plane exists. Its quantifier rank is four because the quantifiers for \(p\) and \(z\) occur in separate conjuncts.

## Verification
A standalone Python 3 program, `verify_incidence_rank.py`, constructs the Levi graphs for \(\mathrm{PG}(2,2)\) and \(\mathrm{PG}(2,3)\) from normalized nonzero vectors in three-dimensional prime-field space. It recursively computes exact finite first-order rank types, comparing tuples across the two graphs using the **set** of one-point extension types. The accompanying `rank_checks.json` records agreement of uncoloured rank-four root types, the exact counts \(24,4,1,1\) for tuple lengths three through zero, a direct bijection between the 24 geometric triple profiles and rank-one triple types, sorted rank-three agreement, and sorted rank-four disagreement. Degree checks corroborate the rank-five witness.

The finite computations check two examples, **not** all projective planes. Universality, including the non-Desarguesian case, follows from the symbolic incidence-axiom case analysis above. The program uses no external dependencies and reproduces its output with `python verify_incidence_rank.py`.

## Relationship to prior work
The paper by De Winter, Lazebnik and Verstraëte (2008) defines Levi graphs of projective planes and investigates their extremal cycle counts; its main conclusion does not imply any Ehrenfeucht–Fraïssé equivalence. Pikhurko and Verbitsky (2010, revised 2013) provide the general framework for first-order graph logical depth and Ehrenfeucht games, but not this incidence-family rank-four comparison. The finding concerns **qualitative first-order expressibility**, not a cycle count, metric invariant, graph homology, or projective-plane classification. The graph-theoretic order is not recovered at quantifier rank four even though regular degrees differ.

## Limitations
The proof does not classify rank-five or higher theories across all projective planes and does not claim any counting-logic equivalence. The comparison of the two named-sort structures is restricted to the specific Fano/ternary pair for sharpness; more ranks or more plane orders are not classified. An equivalent rank-four argument could exist in unindexed teaching material or older geometry/model-theory literature despite the targeted checks described in the accompanying review. Independent validation has not been performed.

## References
1. S. De Winter, F. Lazebnik, and J. Verstraëte, “An Extremal Characterization of Projective Planes,” *Electronic Journal of Combinatorics* 15 (2008), R143. DOI: 10.37236/867. Public date: 2008-11-30. Full text: https://www.combinatorics.org/ojs/index.php/eljc/article/download/v15i1r143/pdf/.
2. O. Pikhurko and O. Verbitsky, “Logical Complexity of Graphs: A Survey,” arXiv:1003.4865 (first posted 2010-03-25; version 4 dated 2013-04-29), especially Section 3 (Ehrenfeucht games). https://arxiv.org/abs/1003.4865.
