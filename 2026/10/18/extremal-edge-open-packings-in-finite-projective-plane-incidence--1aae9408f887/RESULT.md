# Extremal edge-open packings in finite projective-plane incidence graphs

## Finding
Let \(\Pi\) be any finite projective plane of order \(q\ge3\), and let \(G_\Pi\) be its point-line incidence (Levi) graph. Write \(v=q^2+q+1\) for the number of points, equivalently lines, in \(\Pi\). Then
\[
\rho_e^o(G_\Pi)=q(q+1)=v-1.
\]
Moreover, there are **exactly \(2v\) distinct maximum edge-open packings**. They are all of the following forms:

* For a fixed line \(L\), select every incidence \((p,\ell)\) with \(p\in L\), \(\ell\ne L\), and \(p\in\ell\). This is a union of \(q+1\) induced \(q\)-edge stars centered at the points of \(L\).
* Dually, for a fixed point \(p\), select every incidence \((x,\ell)\) with \(\ell\ni p\), \(x\ne p\), and \(x\in\ell\). This is a union of \(q+1\) induced \(q\)-edge stars centered at the lines through \(p\).

The theorem is unconditional for every finite projective plane that exists, whether or not it is Desarguesian. The order-two Heawood case is not claimed as new here.

## Assumptions and scope
A projective plane of order \(q\) has \(v=q^2+q+1\) points and \(v\) lines; every line contains \(q+1\) points, every point lies on \(q+1\) lines, two distinct points have a unique joining line, and two distinct lines meet at a unique point. No field coordinatization is assumed. The graph \(G_\Pi\) has one vertex for every point and line, and edges are the incidences.

For any finite graph \(G\), an **edge-open packing** is a set \(B\subseteq E(G)\) such that no edge distinct from two selected edges joins an endpoint of the first to an endpoint of the second. Equivalently, the graph induced by all endpoints of \(B\) has components that are stars, and its edge set is precisely \(B\). The number \(\rho_e^o(G)\) is the maximum \(|B|\). A one-edge star may be oriented by either endpoint, without affecting \(B\).

## Proof
**Construction.** Fix a line \(L\). Every other line \(\ell\) meets \(L\) in a unique point \(p\). Select the edge from \(\ell\) to \(p\). Every line other than \(L\) is a leaf, every point of \(L\) is a center, and there are no incidences from a selected leaf to any other center. The \(q+1\) centers each have \(q\) leaves. This produces \(v-1=q(q+1)\) selected edges forming disjoint induced stars. Exchanging points and lines gives the second construction.

**Mixed-leaf bound.** Let \(B\) be an edge-open packing. Orient each induced star component around one center (arbitrarily for a one-edge star). Let \(X\) be the set of line vertices that occur as leaves of point-centered stars and \(Y\) the set of point vertices that occur as leaves of line-centered stars. Every selected edge has exactly one leaf, so
\[
|B|=|X|+|Y|.
\]
No point in \(Y\) is incident with a line in \(X\): such an incidence would join endpoints belonging to two different selected star components, contrary to the packing condition.

If both \(X\) and \(Y\) are nonempty, choose \(L\in X\) and \(y\in Y\). All points in \(Y\) lie outside \(L\), a set of \(q^2\) points. Let \(Z\) be the union of points outside \(L\) lying on lines of \(X\setminus\{L\}\). Each such line contributes \(q\) incidences to \(Z\). For any \(z\in Z\), the unique line \(yz\) cannot belong to \(X\), because it meets the forbidden point \(y\in Y\); hence \(z\) lies on at most \(q\) lines of \(X\setminus\{L\}\). Double counting gives
\[
q(|X|-1)\le q|Z|,\qquad |Y|\le q^2-|Z|,
\]
and therefore
\[
|B|\le q^2+1<q^2+q.
\]
Thus every maximum packing, by the construction, has all leaves on one side of the bipartition.

**Single-side bound and equality.** Suppose all leaves are line vertices, so \(Y=\varnothing\), \(|B|=|X|\), and the star centers form a nonempty set \(S\) of points. If \(|S|=1\), then \(|B|\le q+1<q(q+1)\). Otherwise choose distinct centers \(a,b\in S\). Their joining line \(L=ab\) cannot lie in \(X\). Indeed, if \(L\) were a leaf attached to one center, its incidence with the other center would connect two different selected stars. Consequently at least one of the \(v\) lines is not a leaf and \(|B|\le v-1\).

If \(|B|=v-1\), then \(L\) is the unique omitted line. The joining line of every other pair of centers must also be omitted, hence every center lies on \(L\). Each line \(\ell\ne L\), being a leaf, is attached to its only possible center on \(L\), namely \(\ell\cap L\). Every point of \(L\) lies on off-\(L\) lines, so all \(q+1\) points of \(L\) are centers, and every selected edge is exactly the prescribed construction from \(L\). The analogous argument with points and lines exchanged yields the dual construction when all leaves are point vertices.

**Counting.** There are \(v\) choices of the omitted line and \(v\) choices of the omitted point. The leaf sets distinguish the configurations within each type, and the two types have opposite leaf sides. Thus these \(2v\) constructions are all distinct, completing the proof.

## Verification
The standalone `verify.py` constructs \(\operatorname{PG}(2,q)\) from normalized nonzero vectors over the prime fields of orders \(q=2,3,5,7\). It checks the projective-plane incidence axioms, generates all \(2v\) stated constructions, checks their cardinalities, and tests every pair of selected edges directly against the packing definition. For \(q=2\) and \(q=3\), it additionally builds the edge-compatibility graph and exhaustively lists all maximal cliques, verifying that all maximum packings are exactly the geometric constructions.

Results: at \(q=2\), 28 maximal packings in total and 14 maximum packings of 6 edges; at \(q=3\), 3,094 maximal packings in total and 26 maximum packings of 12 edges. At \(q=5\) and \(q=7\), the explicit families contain 62 packings of 30 edges and 114 packings of 56 edges, respectively. The verifier reports `VERIFY_OK`. Finite enumerations are checks, **not** a substitute for the proof for arbitrary projective planes.

## Relationship to prior work
Chelladurai, Kalimuthu and Soundararajan introduced edge-open packing and proved a general degree bound, \(\rho_e^o(G)\le |E(G)|/\delta(G)\). For \(G_\Pi\), that bound is \(v\) rather than the sharp \(v-1\). Brešar and Samadi characterize equality in the general bound, but do not determine the precise next value or classify all maximizers for projective-plane incidence graphs. The complementary injective-edge-coloring literature primarily minimizes the number of color classes, whereas the present theorem determines the largest individual class and its complete equality structure. The order-two Heawood case lies outside the theorem and is not part of its novelty claim.

## Limitations
The theorem assumes the axioms of a finite projective plane of order \(q\ge3\); it does not assert existence for any particular order, enumerate nonisomorphic planes, or determine their injective chromatic indices. The 2, 3, 5, and 7 finite-field tests do not sample non-Desarguesian planes; the proof itself covers them. Searches and full-text comparisons reduce, but cannot eliminate, the possibility of an equivalent earlier result under alternative geometric or induced-star terminology. No independent mathematical audit is claimed.

## References
1. G. Chelladurai, K. Kalimuthu and S. Soundararajan, “Edge open packing sets in graphs,” *RAIRO—Operations Research* 56 (2022), 3765–3776, DOI: 10.1051/ro/2022171. Published online 2022-11-01. https://doi.org/10.1051/ro/2022171
2. B. Brešar and B. Samadi, “Edge open packing: complexity, algorithmic aspects, and bounds,” arXiv:2403.00750v1 (2024-03-01), especially Theorem 4.1. https://arxiv.org/abs/2403.00750
3. A. Kostochka, A. Raspaud and J. Xu, “Injective edge-coloring of graphs with given maximum degree,” arXiv:2010.00429v1 (2020-10-01), revised 2021. https://arxiv.org/abs/2010.00429
