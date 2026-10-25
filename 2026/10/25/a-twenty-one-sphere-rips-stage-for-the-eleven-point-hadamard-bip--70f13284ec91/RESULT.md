# A twenty-one-sphere Rips stage for the eleven-point Hadamard biplane

## Finding

Let \(P=\mathbb Z/11\mathbb Z\), \(D=\{1,3,4,5,9\}\), and let the eleven blocks be \(B_j=j+D\), for \(j\in P\). Write \(G\) for the bipartite incidence graph on points \(p_i\) and blocks \(b_j\), with an edge \(p_i b_j\) exactly when \(i\in B_j\), and use the integer-valued shortest-path metric. Write \(K_r=\operatorname{VR}_{\le r}(V(G))\). The complete integral homotopy filtration at integer scales is

\[
K_0\simeq\bigvee^{21}S^0,\qquad
K_1\simeq\bigvee^{34}S^1,\qquad
K_2\simeq\bigvee^{21}S^3,\qquad
K_r\simeq *\quad(r\ge3).
\]

Consequently the complete positive-dimensional integral persistence barcode consists of thirty-four degree-one intervals \([1,2)\) and twenty-one degree-three intervals \([2,3)\). There are twenty-one reduced degree-zero intervals \([0,1)\); all positive-dimensional reduced integral homology groups are free.

Under simultaneous translation \(p_i\mapsto p_{i+t}\), \(b_j\mapsto b_{j+t}\), the cyclic group \(C_{11}\) acts on the two nontrivial homology groups with rational decompositions

\[
\widetilde H_1(K_1;\mathbb Q)\cong4\mathbf 1\oplus3\mathbb Q(\zeta_{11}),\qquad
\widetilde H_3(K_2;\mathbb Q)\cong\mathbf 1\oplus2\mathbb Q(\zeta_{11}).
\]

Here \(\mathbb Q(\zeta_{11})\) denotes the unique nontrivial irreducible rational representation of \(C_{11}\), of dimension ten. No assertion is made about an integral module splitting.

## Assumptions and scope

All simplices are ordinary abstract simplices, and the Rips convention is inclusive diameter at most the scale. Point labels and block labels occupy two disjoint copies of \(\mathbb Z/11\mathbb Z\). The difference set \(D\) has exactly two ordered representations of each nonzero residue as a difference of its elements, so the eleven translates form a symmetric \(2\)-\((11,5,2)\) design. Every two points share two incident blocks, and every two blocks share two points. Consequently graph distances are two between distinct vertices in either part, one between incident point-block vertices, and three between nonincident point-block vertices.

The theorem is specific to this canonical eleven-point biplane and its specified cyclic automorphisms. It does not assert the same wedge decomposition for other biplanes.

## Proof

**Step 1: a general incidence suspension reduction.** For a bipartite incidence relation between finite point set \(P\) and block set \(\mathcal B\), suppose its connected incidence graph has distances exactly two within either part and distance three between nonincident opposite-part vertices. Its inclusive scale-two Rips complex \(K\) consists of subsets with arbitrary point and block parts subject only to the requirement that every chosen point belongs to every chosen block. Write \(\Delta_P\subset K\) for the full point simplex. Let \(U\) be the union of the closed vertex stars \(\operatorname{st}_K(b)\) over all block vertices \(b\). Every nonempty intersection of these stars is the star of their common block-vertex simplex, because all block vertices form a clique and membership in each star means all selected point vertices are incident with the corresponding block. Thus all intersections are nonempty and contractible; their nerve is the full block simplex, and the finite nerve lemma makes \(U\) contractible. The union \(\Delta_P\cup U\) equals \(K\). Their intersection is the *block complex* \(L\), whose faces are precisely the nonempty sets of points contained in some block. As the inclusions of finite subcomplexes are cofibrations, the ordinary homotopy pushout of the two contractible complexes is homotopy equivalent to the unreduced suspension \(\Sigma|L|\). Hence \(|K|\simeq\Sigma|L|\). This reduction concerns ordinary homotopy types, not a claimed equivariant suspension equivalence.

**Step 2: the eleven-point block complex.** The eleven sets \(B_j\) are its facets, each with five points; any two facets intersect in exactly two points. Its \(f\)-vector in dimensions zero through four is \((11,55,110,55,11)\). Every triangle belongs to exactly one block, because two blocks cannot share three points. Within each four-simplex, collapse one free three-face together with that simplex, and then collapse each of the four remaining three-faces with an available free two-face. These collapses can be made independently across blocks (distinct block simplices share only edges). The resulting simplicial complex is two-dimensional with \(f\)-vector \((11,55,66)\); the package contains a deterministic list of the fifty-five actual elementary pairs.

**Step 3: simple connectivity.** Use the ten edges \(\{0,i\}\), \(1\le i\le10\), as a spanning tree of the complete eleven-vertex one-skeleton. Its usual edge-path fundamental-group presentation has forty-five generators, one for each remaining edge, and one triangular relator for each filled triangle. Every generator can be eliminated using a relator whose other two edge labels have already been eliminated: thirty in the first pass and fifteen in the second. The attached certificate lists all forty-five triangles and their eliminated edges in a valid sequence. Since all relators are primitive length-three edge-loop relators, these operations are legitimate Tietze eliminations, proving \(\pi_1(L)=1\).

**Step 4: homotopy type and integral homology.** Elementary collapses retain homotopy type, so \(L\) is homotopy equivalent to a simply connected two-dimensional finite CW complex. Its reduced Euler characteristic is \(11-55+110-55+11-1=21\). Therefore \(H_2(L;\mathbb Z)\cong\mathbb Z^{21}\), all other reduced integral homology vanishes, and by Hurewicz and the simply connected homology form of Whitehead's theorem \(L\simeq\bigvee^{21}S^2\). Suspending gives \(K_2\simeq\bigvee^{21}S^3\). The scale-one complex is the graph itself; since it has twenty-two vertices and fifty-five edges and is connected, its cycle rank is \(55-22+1=34\). At scale three, every pair of vertices is joined and the Rips complex is a full simplex. These facts give the stated integral barcode.

**Step 5: cyclic homology characters.** For \(t\ne0\), translation by \(t\) is an eleven-cycle separately on points and blocks. At scale one it fixes no graph vertex or graph edge setwise, so its ordinary Lefschetz number is zero. Connectedness gives trace \(1\) on \(H_0\), hence trace \(1\) on \(H_1\). At scale two, the only nonempty invariant simplices are the full eleven-point simplex and the full eleven-block simplex. Both have dimension ten, and an eleven-cycle has orientation sign \(+1\). Including the augmented empty simplex, the reduced Lefschetz number is \(-1+1+1=1\). Homology is concentrated in degree three, hence the trace on reduced \(H_3\) is \(-1\). The identity traces are respectively \(34\) and \(21\). Every rational \(C_{11}\)-module is a sum of the trivial representation and the degree-ten cyclotomic representation; solving the identity and nonidentity trace equations yields \((4,3)\) and \((1,2)\) copies respectively.

## Verification

Run `python3 verify_biplane11.py CERTIFICATE.json` using Python 3 with no third-party dependencies. It independently regenerates the incidence design, the fifty-five actual free-face pairs, the forty-five triangle-relator eliminations, all 4,776 nonempty scale-two Rips simplices, boundary ranks over \(\mathbb F_2\), and all eleven signed cyclic Lefschetz values. It compares the two explicit finite certificates to the stored data. The proof of the general suspension reduction is mathematical, not inferred from finite tests. The exact collapse and generator-elimination certificates prove the finite nonstandard steps, while the mod-two ranks provide a separate check.

## Relationship to prior work

Feng and Nukala (first arXiv version February 28, 2023) determine scale-two Rips homotopy types for classes of finite subset metrics, especially Hamming-type/Kneser settings; the eleven-point biplane incidence metric is a different object. Virk (June 10, 2019) develops a functorial Rips–nerve/Dowker framework but does not calculate this block design. Alavi, Daneshkhah and Praeger (April 9, 2020) identify the unique \(2\)-\((11,5,2)\) biplane and its design automorphisms, but do not give its incidence Rips homotopy or homology characters. Published results on finite projective-plane incidence Rips complexes concern designs with pair multiplicity one, rather than two; the already determined Kummer biplane block complex is a sixteen-point, not an eleven-point, instance. The general complement-graph/independence-complex identification is acknowledged and does not itself determine the twenty-one-sphere type or its cyclic character.

## Limitations

This is an exact result for a single canonical symmetric design, not a classification of all biplanes and not a classification of representations under its full automorphism group. Only rational \(C_{11}\)-module decompositions are claimed, although the underlying integral homology groups are determined. The absence of an indexed equivalent statement does not prove priority; independent mathematical review has not been performed.

## References

1. Z. Feng and N. C. P. Nukala, *On Vietoris–Rips Complexes of Finite Metric Spaces with Scale 2*, arXiv:2302.14664, initially public 2023-02-28. https://arxiv.org/abs/2302.14664
2. S. H. Alavi, A. Daneshkhah and C. E. Praeger, *Symmetries of Biplanes*, arXiv:2004.04535, initially public 2020-04-09. https://arxiv.org/abs/2004.04535
3. Ž. Virk, *Rips Complexes as Nerves and a Functorial Dowker-Nerve Diagram*, arXiv:1906.04028, initially public 2019-06-10. https://arxiv.org/abs/1906.04028
