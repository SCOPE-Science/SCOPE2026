# The scale-three Čech nerve of the ternary projective-plane incidence graph

## Finding
Let \(G\) be the point–line incidence graph of \(\operatorname{PG}(2,3)\), with its unit-length geometric realization. Write \(\mathcal N(G,r)\) for the simplicial nerve of the 26 closed metric balls of radius \(r/2\) centered at graph vertices, with intersections permitted in edge interiors. At the first threshold beyond girth-six graph recovery,
\[
\mathcal N(G,3)\simeq\bigvee^{324}S^2.
\]
Thus \(\widetilde H_2(\mathcal N(G,3);\mathbb Z)\cong\mathbb Z^{324}\), all other reduced integral homology vanishes, and the fundamental group is trivial.

## Assumptions and scope
Represent the 13 points of \(\operatorname{PG}(2,3)\) by nonzero triples over \(\mathbb F_3\), normalized so the first nonzero coordinate is one, and represent its 13 lines by nonzero dual triples under the same normalization. A point \(p\) and a line \(\ell\) are adjacent in \(G\) exactly when their dot product is zero in \(\mathbb F_3\). There are 26 vertices and 52 edges; each vertex has four neighbors. This specifies the Desarguesian projective plane of order three rather than an arbitrary incidence structure.

The scale parameter is exactly \(r=3\), so balls have geometric radius \(3/2\). The Čech nerve is not the Vietoris–Rips clique complex and is not the nerve of balls intersected only with the discrete graph vertex set. Its primary classification is topological; no formula for other prime powers or other scales is asserted.

## Proof
**1. Complete finite description.** For a unit-edge graph at odd integer threshold three, each maximal Čech simplex occurs among the unions
\[
F_{u v}=(\{u\}\cup N_G(u))\cup(\{v\}\cup N_G(v)),\qquad uv\in E(G).
\]
Indeed an intersection of radius-\(3/2\) balls has a point in the interior of some edge or at a vertex; moving to that edge's midpoint preserves all incident vertex centers at distance at most \(3/2\), and a vertex intersection is covered by some adjacent-edge midpoint. For the midpoint of \(uv\), the centers at distance at most \(3/2\) are exactly \(F_{uv}\). This is also the standard odd-threshold graph Čech facet lemma of Adams–Shukla–Singh.

Enumerate all normalized homogeneous triples and use the dot-product incidence rule. The 52 incidence edges produce 52 distinct sets \(F_{uv}\) of cardinality eight; none contains another. Enumerating every nonempty subface gives the exhaustive face vector
\[
(f_0,\ldots,f_7)=(26,325,2132,3250,2834,1456,416,52)
\]
with 10,491 nonempty faces. Every vertex pair belongs to some facet, so the one-skeleton is the complete graph on 26 vertices.

**2. Exact simplicial collapse.** On the complete set of face bitmasks, compute for each face its complete set of immediate (one-vertex-larger) cofaces. Repeatedly select an active face having exactly one such coface, preferring largest face dimension and then smallest numerical bitmask. Delete the face and its unique coface only when the latter has no active immediate coface; update all incidences after each deletion. This is a completely specified deterministic elementary simplicial-collapse algorithm, included in `check_pg23_cech.py`. The exhaustive algorithm has exactly 4,875 legal free-face pairs and leaves the two-dimensional subcomplex with face vector
\[
(26,208,507).
\]
Every step is a homotopy equivalence. The complete code checks codimension one, uniqueness, maximality and closure, not just an outcome log.

**3. Triviality of the fundamental group.** Use the complete original one-skeleton and root a spanning star at vertex zero. The 25 star edges are the maximal tree, leaving exactly \(\binom{25}{2}=300\) chord generators in the standard triangle-presentation of the fundamental group. Each triangular face through vertex zero kills its chord. For any further triangle on vertices all distinct from zero, its boundary relation implies that if two of its three chords are already trivial, then the third is trivial. Iterating this valid implication across *all* 2,132 triangular faces kills all 300 chord generators. The executable verifier checks this exact closure process. It follows that the original nerve, and hence its collapsed two-complex, is simply connected.

**4. Integral homotopy type.** The collapsed two-complex has Euler characteristic \(26-208+507=325\). It is connected and simply connected, and it has no cells above dimension two. Consequently its reduced second integral homology is free of rank \(325-1=324\), with all other reduced homology zero. By the Hurewicz theorem, a map from a wedge of 324 two-spheres can be chosen to induce an isomorphism on second homology; it is then a homology equivalence of simply connected CW complexes, and Whitehead's theorem makes it a homotopy equivalence. This proves the claimed wedge type integrally, not just modulo a prime.

## Verification
Run `python3 check_pg23_cech.py` with Python 3 and its standard library. It performs the full projective normalization and incidence-axiom checks; lists all Čech facets and all 10,491 simplices; checks the 4,875 free pairs; checks all 300 fundamental-group relations are killed by a finite triangle-propagation certificate; and independently computes mod-two ranks \(25\) and \(183\) for the first two boundary maps of the collapsed complex. This gives \(507-183=324\) two-dimensional mod-two classes, independently corroborating the integral argument. Successful execution prints `VERIFY_OK`.

## Relationship to prior work
Adams, Shukla and Singh introduce the intrinsic metric-graph Čech convention and the odd-scale facet rule; their explicit homotopy results concern hypercube graphs, not projective-plane incidence graphs. Biswas (first public September 26, 2026) studies finite-subset Čech complexes under symmetric-difference metrics and Boolean-order restrictions; the objects and filtration are different, and neither his stated results nor his conjectural higher-radius extension implies the claim here.

Published work on the Heawood graph—the order-two projective-plane incidence graph—identifies 48 two-spheres at scale three. A separate published theorem treats **scale four** for every finite projective plane, obtaining \(q^6\) four-spheres. Both results were inspected in full and do not determine the order-three plane's scale-three homotopy type. Results for the Desargues and Pappus graphs concern different configurations; published projective-plane scale-two **Vietoris–Rips** results concern a different nerve construction. A published result for the ternary **nonincidence** graph studies a Lovász neighborhood complex, not the present incidence graph's metric Čech nerve.

## Limitations
The result is an exhaustive finite theorem for the unique projective plane of order three. It makes no assertion for higher plane orders, non-Desarguesian planes, scale-four Čech nerves, persistence maps, or equivariant homotopy. The structural step uses a standard graph Čech facet lemma, while the finite collapse and fundamental-group certificates can be checked from the embedded standalone script. Existing database and literature searches do not logically exclude unindexed or differently named equivalent work. No independent audit has been performed.

## References
1. H. Adams, S. Shukla, A. Singh, *Čech complexes of hypercube graphs*, arXiv:2212.05871 (first public December 12, 2022), especially Lemma 2.2 and its odd-scale graph nerve description.
2. A. Biswas, *Čech complexes for finite sets*, arXiv:2609.32786v1 (first public September 26, 2026), especially its finite-set Čech construction and high-radius questions.
3. *Complete intrinsic graph Čech persistence of the Heawood graph*, published topology result (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-complete-intrinsic-graph-ech-persistence-of-the-heawood-graph--a334f7f20b6f .
4. *Scale-four graph Čech nerves of finite projective planes*, published topology result (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-scale-four-graph-ech-nerves-of-finite-projective-planes--2cc10caab711 .
5. *Scale-three Čech nerve of the Desargues graph is a wedge of 49 two-spheres*, published topology result (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-scale-three-ech-nerve-of-the-desargues-graph-is-a-wedge-of-49-tw--eac77c714390 .
6. *Scale-two Vietoris–Rips complexes of finite projective-plane incidence graphs*, published topology result (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-scale-two-vietoris-rips-complexes-of-finite-projective-plane-inc--c3740b96b3c3 .
