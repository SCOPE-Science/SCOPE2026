# Two-coloring flips in \(\operatorname{PG}(2,3)\): a sharp two-move Hamming detour

## Finding
Let \(\mathcal P\) be the thirteen points and \(\mathcal L\) the thirteen four-point lines of \(\operatorname{PG}(2,3)\). A labeled two-coloring \(\sigma:\mathcal P\to\{0,1\}\) is proper when neither color occupies an entire line. The flip graph \(\mathcal R\) has these proper colorings as vertices and joins two colorings that differ at precisely one point. Write \(h(\sigma,\tau)\) for their Hamming distance and \(d_{\mathcal R}(\sigma,\tau)\) for shortest-path distance.

**Exact metric theorem.** The graph \(\mathcal R\) is connected and, for every ordered pair of its proper labeled colorings,
\[
 d_{\mathcal R}(\sigma,\tau)\in\{h(\sigma,\tau),h(\sigma,\tau)+2\}.
\]
There are exactly \(52{,}416\) ordered pairs for which the second alternative holds (\(26{,}208\) unordered pairs); for each fixed coloring exactly \(112\) target colorings require the extra two flips. The bound is sharp. There are \(468\) colorings, \(702\) edges, and every vertex has three neighbors; the radius and diameter are both \(13\). The exact ordered-pair counts are \(166{,}608\) at distance \(h\) and \(52{,}416\) at distance \(h+2\), including \(468\) diagonal pairs in the first count.

The **claim of contribution is the exact Hamming-sensitive recoloring metric and detour distribution** for this naturally embedded coloring space. The known geometry of size-six blocking sets, ordinary abstract cubic-graph parameters, and existence of proper two-colorings are not claimed as new.

## Assumptions and scope
The plane is the unique Desarguesian projective plane \(\operatorname{PG}(2,3)\). Colors are labeled: exchanging both color labels generally gives a different vertex. A move flips exactly one point and must maintain nonmonochromaticity on *every* line. Distances are ordinary unweighted graph distances, with no external vertices or temporary improper colorings allowed. No assertion is made for projective planes of another order or for more than two colors.

For an explicit reproducible model, choose the thirteen normalized nonzero vectors \(p\in\mathbf F_3^3\), where the first nonzero coordinate equals \(1\); points are these vectors and lines are the sets \(L_u=\{p:u\cdot p=0\}\) indexed by similarly normalized nonzero vectors \(u\). Fix lexicographic point order and represent a coloring by an integer \(s\) in \([0,8191]\), whose \(i\)-th binary digit records color \(1\) at the \(i\)-th point. If \(\ell\) is the four-bit line mask, then \(s\) is proper exactly when
\[
0<\operatorname{popcount}(s\mathbin{\&}\ell)<4\qquad\text{for all thirteen lines }\ell.
\]
Here the bitwise operator is merely part of the executable finite model.

## Proof
**(1) Completeness of the coloring enumeration.** Every labeled coloring of thirteen points occurs exactly once among the \(2^{13}=8192\) masks. The displayed thirteen conjunctions test precisely the proper-coloring definition. The supplied verifier constructs the plane in two different coordinate models: homogeneous dot-product incidences and affine lines plus a line at infinity; it checks identical line masks and identical proper-coloring sets. Complete enumeration yields \(468\) valid masks, with exactly \(234\) of weight six and \(234\) of weight seven. Independently, the \(\binom{13}{3}-13\binom43=234\) triples of pairwise nonconcurrent lines give \(234\) distinct six-point vertexless triangles, precisely the six-point color classes in the enumeration. These known static structures are used to check the finite domain; they are not the new metric claim.

**(2) Exhaustion of the allowed flips.** For each enumerated mask \(s\), the program tests all thirteen masks \(s\oplus2^i\) against the full proper-coloring set. This is exactly the adjacency rule, without a search heuristic. An independent adjacency construction compares every unordered pair of valid words and selects Hamming distance one. Both adjacency lists coincide. There are \(468\) vertices, every vertex has degree three, and therefore \(468\cdot3/2=702\) edges.

**(3) Exactness of distances and the theorem.** For each of the \(468\) sources, a breadth-first search traverses the entire finite graph. In an unweighted graph, breadth-first search assigns the length of a shortest path: by induction on the visited layer it discovers each vertex in the least possible number of edges. All \(468\) vertices are reached from every source. For each target, the code independently computes \(h\) as the population count of the bitwise XOR of the source and target masks. Every legal flip changes one bit, so \(d\ge h\); parity of the number of flips in each coordinate forces \(d-h\) to be even. The full matrix enumeration verifies that its only values are \(0\) and \(2\), with respective ordered-pair counts \(166{,}608\) and \(52{,}416\). Every row has \(356\) entries of the first type and \(112\) of the second. In particular, some positive fraction of pairs requires an extra two moves, proving sharpness. All source eccentricities equal \(13\), proving the radius and diameter claim. Every finite quantifier in the theorem is covered by this explicit exhaustive verification.

## Verification
Run the bundled `check_coloring.py` with a standard Python 3 interpreter, using no third-party packages. The bundled `check_output.txt` is the actual terminal result; the verifier runs again from the embedded files. It asserts: agreement of both incidence constructions and both proper-coloring tests; exhaustive vertexless-triangle correspondence; equality of two independent adjacency constructions; all-source reachability; exact shortest-path, Hamming, detour and distance-shell statistics. The expected output includes `exact_full_enumeration=PASS`, `detour_two_per_coloring=112`, and `radius=13 diameter=13`.

## Relationship to prior work
Gravin and Karpov (2011) give the standard proper-hypergraph-coloring definition and general existence results, but do not analyze reconfiguration of this projective plane. Kiss, Marcugini and Pambianco (2008) classify small-order semiovals and specifically discuss six-point configurations in \(\operatorname{PG}(2,3)\), so their static geometry is prior work, not novelty here. Conder and Nedela catalog the cubic symmetric graph F468, having order \(468\), girth \(12\), and diameter \(13\); the matching abstract-graph parameters constitute a major overlap warning. An explicit isomorphism between our coloring graph and F468 was neither established nor needed. Even if they are isomorphic, abstract isomorphism invariants do not determine the chosen thirteen-coordinate Hamming metric or its sharp two-step detour counts. Anastos and Frieze (2020) investigate connectivity for random-hypergraph coloring spaces; their stated random-family results do not specialize to this fixed projective-plane instance.

## Limitations
This is a finite exact result, not an asymptotic or uniform statement. The metric facts are computationally exhaustive and reproducible, rather than a closed-form conceptual characterization of which particular pairs require a detour. No graph-isomorphism classification is claimed. A previously unindexed realization of F468 or an unpublished finite coloring enumeration could already contain the coordinate-sensitive distances; this remains an originality risk. The full text of Anastos–Frieze (2020) was not accessible during comparison; its available theorem statement concerns random hypergraphs and does not by itself imply the present fixed-instance metric.

## References
1. N. Gravin and D. Karpov, *On proper colorings of hypergraphs*, arXiv:1111.1558v1, first public 2011-11-07. https://arxiv.org/abs/1111.1558
2. Gy. Kiss, S. Marcugini and F. Pambianco, *Semiovals in projective planes of small order*, ACCT2008, pp. 151–154. https://www.researchgate.net/publication/228983042_Semiovals_in_projective_planes_of_small_order
3. M. Conder and R. Nedela, *A more detailed classification of symmetric cubic graphs*, especially F468 in the appendix. https://www.math.auckland.ac.nz/~conder/preprints/symmcubictypes.pdf
4. M. Anastos and A. Frieze, *On the connectivity of proper colorings of random graphs and hypergraphs*, Random Structures & Algorithms **56** (2020), 988–997. https://doi.org/10.1002/rsa.20912
