# Equal sphere multiplicities in different degrees for two Petersen double covers

## Finding
Let \(G_k=\operatorname{GP}(10,k)\) be the generalized Petersen graph for \(k\in\{2,3\}\), and let \(\mathcal S(G)\) denote the induced-matching simplicial complex of a finite simple graph \(G\): its vertices are graph edges and its simplices are sets of edges forming an induced matching. Then there are integral homotopy equivalences
\[
\boxed{\mathcal S(G_2)\simeq\bigvee^{104}S^2,\qquad
\mathcal S(G_3)\simeq\bigvee^{104}S^3.}
\]
Here \(G_2\) is the dodecahedral graph and \(G_3\) is the Desargues graph. Both are twenty-vertex cubic graphs and double covers of the Petersen graph. Both have induced-matching number six and exactly 104 spheres in their homotopy decompositions, but **the spheres occur in different dimensions**. In particular, their reduced integral homology is concentrated in degree two and degree three, respectively, with group \(\mathbb Z^{104}\) in that degree. This is an integral homotopy classification, not just a field-homology computation.

## Assumptions and scope
For either \(k=2\) or \(k=3\), vertices are \(u_i,v_i\) for \(i\in\mathbb Z/10\mathbb Z\), with graph edges \(u_iu_{i+1}\), \(u_iv_i\), and \(v_iv_{i+k}\); all subscripts are modulo ten. For reproducibility, label \(u_i=i\) and \(v_i=i+10\), and sort the 30 graph edges as increasing unordered pairs of these integers. An induced matching is a set of edges whose endpoints induce exactly those edges and no additional graph edge. Consequently, two graph edges are forbidden in the same simplex when they share an endpoint **or** when a graph edge joins an endpoint of one to an endpoint of the other. Equivalently \(\mathcal S(G)=\operatorname{Ind}(L(G)^2)\), where \(L(G)\) is the line graph. All homotopy equivalences concern geometric realizations of these finite abstract simplicial complexes.

Each graph has a fixed-point-free involution \(u_i\leftrightarrow u_{i+5}\), \(v_i\leftrightarrow v_{i+5}\). The quotient of each involution is the generalized Petersen graph \(\operatorname{GP}(5,2)\), namely the Petersen graph; for \(k=3\), inner steps reduce to minus two modulo five. The standalone program verifies that every quotient edge has exactly two lifts. No claim is made about a uniform formula for all covers or all generalized Petersen graphs.

## Proof
**Finite face certificates.** Encode each simplex by a 30-bit mask relative to the graph-edge order above. Starting from the empty mask, append each graph edge only when its two endpoints are distinct from every previously selected endpoint and neither endpoint has a graph neighbor among the previously selected endpoints. This is an exhaustive hereditary enumeration because every permitted edge set has a unique increasing-edge insertion sequence. Independent subset enumeration forms all edge subsets of cardinality at most seven and tests all pairs for shared endpoints or cross-endpoint adjacency. The two methods agree exactly; the number of allowed seven-subsets is zero, which rules out every larger simplex by downward closure. The respective counts for face cardinalities zero through six, **including the empty face**, are
\[
(1,30,255,620,315,30,5)\quad\text{for }k=2,
\]
\[
(1,30,255,700,615,42,5)\quad\text{for }k=3.
\]
Thus both strong-matching numbers equal six. The augmented face sets have 1,256 and 1,648 elements.

**Explicit acyclic matchings.** Number the sorted graph edges from zero to 29. For reproducibility, the complete permutation of pivot indices for \(k=2\) is

`25,2,7,1,5,0,15,16,22,12,20,27,23,9,10,6,29,19,3,28,24,14,8,18,13,11,17,21,26,4`.

For \(k=3\) it is

`13,3,16,12,29,0,11,21,26,27,28,22,19,25,18,15,10,23,14,20,8,2,1,9,5,17,24,7,4,6`.

At each pivot \(j\), take each currently unpaired face \(s\) that does not contain \(j\) and whose extension \(s\cup\{j\}\) is still unpaired; pair the two and mark both unavailable at subsequent pivots. This gives precisely 576 pairs and 104 unmatched three-element faces for \(k=2\), and precisely 772 pairs and 104 unmatched four-element faces for \(k=3\). Each matching contains the empty face paired to a singleton. Discard that one pair, leaving its singleton as the unique critical zero-cell and preserving all other pairs. Hence the resulting ordinary face-poset matchings have precisely one critical zero-cell and 104 critical cells in dimension \(k\), with no other critical cells.

For completeness, acyclicity is not inferred merely from the toggle recipe. Orient every codimension-one incidence in the **augmented** face poset from lower to upper if matched, and from upper to lower if unmatched. A full Kahn topological sort of this directed graph consumes every face: 1,256 vertices and 3,840 incidences for \(k=2\), and 1,648 vertices and 5,340 incidences for \(k=3\). Thus both augmented matchings are acyclic. Deleting the empty face and its matched incidence leaves an acyclic matching on the nonempty face poset, since any directed cycle there would already have existed in the augmented directed Hasse graph. The numerical and directed-edge constructions are completely specified by the attached `verify.py`.

**Integral homotopy conclusion.** Forman's discrete Morse theorem gives a CW complex homotopy equivalent to \(\mathcal S(G_k)\) having exactly one zero-cell and 104 cells in dimension \(k\), and no others. Because \(k\ge2\), all higher-dimensional cells are attached to the unique zero-cell; each attaching sphere maps to a point. The CW complex is therefore \(\bigvee^{104}S^k\), proving both assertions integrally without assumptions about torsion or high-dimensional attaching maps.

## Verification
Run `python3 verify.py` with Python 3 and no nonstandard packages. It independently enumerates simplices in two ways, verifies the twofold Petersen covering description, constructs the complete matching pairs, tests **all** augmented face incidences for directed cycles, and independently computes all mod-two simplicial boundary ranks. The checked Betti vectors (degrees zero through five, ordinary unreduced degree zero) are respectively \((1,0,104,0,0,0)\) and \((1,0,0,104,0,0)\). The execution's complete exact printed output is included as `verification_output.txt` and ends with `VERIFY_OK`. The finite computations are exhaustive for these two graph complexes. The integral claim follows from the acyclic matching and the CW-cell argument, rather than from mod-two homology.

## Relationship to prior work
Joos, Rautenbach and Sasse (initial publicly accessible preprint 2013-12-04) investigate the sizes of induced matchings in subcubic graphs. Their theorems address extremal induced-matching cardinalities, not the topology of the simplicial complex whose faces are **all** induced matchings. The present theorem replaces an extremal number with a full integral homotopy invariant for a motivated pair of canonical cubic graphs.

The ordinary matching complexes of these same graphs have separately published integral wedge decompositions: five five-spheres and 117 six-spheres for the dodecahedral graph, and five five-spheres and 45 six-spheres for the Desargues graph. Those results concern \(\operatorname{Ind}(L(G))\), not the *proper subcomplex* \(\operatorname{Ind}(L(G)^2)\) studied here, and neither sphere decomposition implies the current one. A previously established strong-matching classification for the Heawood graph also involves a different incidence graph and does not determine either complex here. Database and textual comparisons did not identify the two present homotopy classifications. Negative bibliographic searches alone are not proofs of absolute novelty.

## Limitations
This theorem classifies exactly the indicated pair of finite graphs; it does not determine full automorphism representations, characterize all covers of the Petersen graph, or assert a stable family theorem. The pair provides a sharp contrast but does not show that arbitrary graph coverings control strong-matching homotopy degrees. Possible equivalent treatments in unindexed or inaccessible literature remain an originality risk. Independent external mathematical review has not been performed.

## References
- F. Joos, D. Rautenbach, T. Sasse, *Induced Matchings in Subcubic Graphs*, arXiv:1312.1110v1, first publicly posted 2013-12-04, https://arxiv.org/pdf/1312.1110 .
- *The dodecahedral matching complex is a wedge of five 5-spheres and 117 6-spheres*, published mathematical result dated 2026-10-11; its ordinary matching-complex statement and proof were inspected for scope.
- *The Desargues matching complex is a mixed-dimensional wedge of spheres*, published mathematical result dated 2026-10-11; its ordinary matching-complex statement and proof were inspected for scope.
- Waller, *Double covers of graphs*, published 2009; its dodecahedral antipodal Petersen-quotient background is not needed for the certificate, which verifies both quotients directly.
