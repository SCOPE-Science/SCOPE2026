# Four-round logical collapse of finite thick generalized hexagons and octagons

## Finding

**Theorem (sharp quadrangle-to-hexagon rank threshold).** Let \(\mathcal H\) and \(\mathcal H'\) be arbitrary finite thick generalized polygons whose gonality is either six or eight, allowing different gonalities and different order parameters. In the one-sorted relational language consisting of equality, unary point and line predicates, and symmetric point–line incidence, they satisfy precisely the same first-order sentences of quantifier rank at most four:

\[
\mathcal H\equiv_4\mathcal H'.
\]

More precisely, every such structure realizes exactly **fourteen** quantifier-rank-two types of ordered pairs, two quantifier-rank-three types of singletons, and one quantifier-rank-four type of the empty tuple. The fourteen ordered-pair types are completely determined by the two sorts and the following truncated incidence-graph distances:

* For two vertices of the same sort: equality, distance two, distance four, or distance at least six.
* For a point and a line, in either order: distance one, distance three, or distance at least five.

**Sharp boundary.** Every finite thick generalized quadrangle \(\mathcal Q\) satisfies \(\mathcal Q\equiv_3\mathcal H\), while \(\mathcal Q\not\equiv_4\mathcal H\). Thus four is exactly the first quantifier rank at which the quadrangle and higher-gonality families can be distinguished. The theorem makes no assertion of rank-five equivalence between hexagons and octagons.

## Assumptions and scope

A generalized \(d\)-gon has a finite connected bipartite incidence graph \(G\), with point and line sides, diameter \(d\) and girth \(2d\). Thickness means every vertex has degree at least three. In a finite thick generalized polygon, line degrees are \(s+1\) and point degrees are \(t+1\), for integers \(s,t\ge2\). Both sorts are named. Incidence is a binary relation connecting opposite sorts; no adjacency, distance, collinearity, constants, or coordinate functions are added as independent symbols.

Quantifier rank counts **nesting depth**, not the total number of quantifiers across conjunctions. Equivalence \(\equiv_r\) is equivalence under every first-order sentence of quantifier rank at most \(r\), or, equivalently, a winning duplicator strategy in the \(r\)-round Ehrenfeucht–Fraïssé game. Repeated selections and arbitrary alternation are permitted.

For \(d\in\{6,8\}\), every vertex has vertices at graph distances zero through six, along a geodesic to an opposite vertex. Shortest paths of length at most five are unique, since the graph has girth at least twelve. There are no four-, six-, eight-, or ten-cycles.

## Proof

**Step 1 (rank-one types of triples).** Fix at most three selected vertices. Their quantifier-free diagram records equality, the unary sorts, and incidence. To determine their entire rank-one type, one must additionally decide which atomic diagrams can be realized by one fourth vertex. A fresh fourth vertex can be adjacent to any specified subset of the selected vertices only if all vertices in that subset have the opposite sort. A common neighbor of two distinct selected vertices exists precisely when they have graph distance two; it is then unique because there is no four-cycle. A common neighbor of three distinct selected vertices exists precisely when they share a center. If all three pairwise distances are two, they must share their center: otherwise the three length-two connections would form a six-cycle. No vertex can be adjacent to both endpoints of an already adjacent pair, because the graph is bipartite.

A fresh vertex adjacent to exactly one prescribed selected vertex is available: the selected vertex has at least three neighbors, while the other two parameters exclude at most two neighbors. A fresh vertex adjacent to none is available on each side. To justify this last assertion uniformly, the cardinality of the point side of a generalized hexagon of order \((s,t)\) is \((s+1)(1+st+s^2t^2)\), and the cardinality of its line side is the dual expression; octagons have strictly larger corresponding expressions. The vertices on a fixed side within distance at most two of at most three parameters occupy at most three radius-two neighborhoods, each bounded by \(1+(s+1)t\) on the line side or \(1+(t+1)s\) on the point side, with the appropriate smaller opposite-sort radius. Already the hexagon formula exceeds these bounds for \(s,t\ge2\). Thus an unrelated fresh vertex exists on each side. Equality to a selected vertex is entirely encoded by the selected diagram.

Consequently a triple's **complete rank-one type** is determined by equality, sorts, incidences, and which same-sort pairs have distance two. The argument holds for every finite thick hexagon and octagon, without homogeneity assumptions.

**Step 2 (rank-two types of pairs).** Fix an ordered pair \((u,v)\). Its rank-two type is determined by its atomic diagram and the set of rank-one triple types realized by \((u,v,w)\) as \(w\) ranges over the graph. By Step 1, the only extra tests on the third vertex are whether it equals an endpoint, is incident to an endpoint, or is distance two from an endpoint.

The existence of a vertex simultaneously within these two-edge neighborhoods depends only on whether the endpoint distance is zero, one, two, three, or four. If the endpoints are at distance at most four, a shortest path gives every admissible simultaneous proximity pattern; if they are farther than four, no third vertex can lie within distance two of both. The other patterns, in which the third vertex lies near only one endpoint or neither, are supplied by branches away from the unique short geodesic (minimum degree three and girth at least twelve), and by the remote-vertex bound of Step 1. For distance two, the third vertex may also belong to the same three-point star through the unique common center; this pattern occurs for every degree at least three. Every one of these choices works independently of \(s,t\).

It follows that ordered-pair rank-two types depend only on the displayed truncated distances. Conversely the categories are distinct: equality and incidence are atomic; distance two is witnessed by one common-neighbor quantifier; distance three by a length-three path with two nested quantifiers; and distance at most four for same-sort vertices by choosing a midpoint and asking, in two parallel rank-one existential subformulas, that it have a common neighbor with each endpoint. These yield exactly four categories per same-sort orientation and three per opposite-sort orientation, hence \(2\cdot4+2\cdot3=14\) types.

**Step 3 (singletons and sentences).** For any fixed point, and separately any fixed line, a geodesic of length at least six supplies representatives of every permissible pair-distance category. Thus the set of rank-two types of pairs \((u,v)\), as \(v\) varies, is exactly the same for every fixed \(u\) of a given sort, in every thick hexagon and octagon. By the recursive definition of finite-rank types, there is exactly one rank-three singleton type for points and one for lines. Since both sorts occur in every structure, the set of rank-three singleton types is identical throughout the family; therefore all empty-tuples have the same rank-four type. This proves the first assertion.

**Step 4 (the exact quadrangle boundary).** For any finite thick generalized quadrangle, hexagon, or octagon, a rank-one pair type depends only on equality, sorts, incidence, and the existence of a common neighbor. Every root on each side has a same-sort vertex at distance two, another same-sort vertex farther away, an incident opposite-sort vertex, and a nonincident opposite-sort vertex. Hence every such root realizes the same spectrum of rank-one pair types, giving rank-three sentence equivalence of quadrangles with the higher-gonality structures.

To separate at rank four, let \(\Psi\) be the following rank-four sentence (with \(I\) the symmetric incidence relation):

\[
\begin{aligned}
\exists p\,\exists\ell\,[\;&P(p)\land L(\ell)\land\neg I(p,\ell)\\
&\land\neg\exists m\,\exists q\,(L(m)\land P(q)\\
&\qquad\land I(p,m)\land I(q,m)\land I(q,\ell))\,].
\end{aligned}
\]

It says that some nonincident point–line pair has no incidence path of length three. A generalized quadrangle has diameter four, so every nonincident point–line pair has distance exactly three, and \(\Psi\) is false. Every thick generalized hexagon or octagon contains opposite-sort pairs at distance five, so \(\Psi\) is true. Consequently quadrangles first separate at rank four, as asserted.

## Verification

The attached `verify_local_profiles.py` independently builds the Fano plane's point–line incidence graph, enumerates its 133 simple cycles of lengths six, eight and ten, and constructs two cyclic covers with respectively 2,954 and 3,122 vertices. Nonzero voltage on every such base cycle gives both covers girth at least twelve; the program checks degree three and graph connectivity. It computes the **literal** rank-one triple extension diagrams, not merely distances, by bitset intersection over all fourth vertices. For representative endpoint pairs across both sorts and graph distances through ten, the resulting rank-two pair signatures collapse into exactly fourteen distance-profile types; the two unrelated covers agree on all fourteen. A separately constructed symplectic quadrangle of order \((2,2)\) has the same rank-three singleton types as both covers. Running `python3 verify_local_profiles.py` prints `VERIFY_OK`.

These finite covers are **not asserted** to be generalized hexagons or octagons, and finite testing is **not** a proof of the universal theorem. They test the nonstandard short-distance extension lemma against independent actual incidence structures. The proof above, especially Steps 1–3, establishes the infinitely quantified statements.

## Relationship to prior work

Exoo and Jajcay's *Dynamic Cage Survey* describes the incidence-graph diameter, girth, and degree conditions for generalized polygons and the classical hexagon examples. Bamberg, Glasby, Popiel, Praeger, and Schneider study finite generalized hexagons and octagons under point-primitive group actions, and explicitly develop their incidence-graph geometry and point counts. Neither work establishes quantifier-rank-four equivalence in the named-sort first-order language. Earlier bounded-depth results for projective planes or generalized quadrangles do not imply hexagon–octagon equivalence: they concern different families, and the quadrangle case is in fact separated by \(\Psi\).

The new result uses the high-girth incidence geometry to identify an exact and uniform finite-rank type spectrum, independently of polygon gonality six versus eight and independently of the two degree parameters.

## Limitations

No equivalence at rank five or higher is claimed for hexagons and octagons; no classification of arbitrary bipartite graphs, thin generalized polygons, infinite generalized polygons, structures with extra constants or coordinate operations, or geometries with named automorphisms is claimed. The argument concerns ordinary first-order quantifier rank and does not apply without modification to counting quantifiers or infinitary logic. The finite verifier is a consistency and boundary check, not an independent certification of the proof. Literature searches may miss unindexed equivalent results.

## References

1. G. Exoo and R. Jajcay, *Dynamic Cage Survey*, Electronic Journal of Combinatorics, Dynamic Surveys DS16, first published 2008-09-29, DOI 10.37236/37. Official record: https://www.combinatorics.org/ojs/index.php/eljc/article/view/DS16 ; full-text 2013 version: https://www.combinatorics.org/files/Surveys/ds16/ds16v3-2013.pdf .
2. J. Bamberg, S. P. Glasby, T. Popiel, C. E. Praeger, and C. Schneider, *Point-primitive generalised hexagons and octagons*, arXiv:1410.3423v1, first posted 2014-10-09, https://arxiv.org/abs/1410.3423 .
3. W. Feit and G. Higman, *The nonexistence of certain generalized polygons*, Journal of Algebra 1 (1964), 114–131. (Background classification; exact first-public date not used.)
