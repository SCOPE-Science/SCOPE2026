# Triangular mod-two systoles across the six equivelar double-tori
## Finding
Let \(K_1,\ldots,K_6\) be the six lexicographically listed 12-vertex orientable equivelar triangulations of Euler characteristic \(-2\) in the Lutz surface data set, in its displayed order. For every \(i\), every three-edge simple cycle in \(K_i\) is either a triangular face or is nonzero in \(H_1(K_i;\mathbf F_2)\). Consequently the simple mod-two homology \(1\)-systole has edge length \(3\) for all six triangulations, and the numbers of unoriented systolic cycles are respectively \(20,24,24,24,18,18\). Grouping these shortest cycles by their nonzero mod-two homology class gives, respectively, the multiplicity multisets \(\{4,4,4,4,2,2\}\), \(\{4,4,4,4,4,4\}\), \(\{4,4,4,4,4,4\}\), \(\{4,4,4,4,4,4\}\), \(\{4,4,2,2,2,2,1,1\}\), and \(\{4,4,4,1,1,1,1,1,1\}\). Thus every nonfacial triangle in this complete equivelar genus-two family is nonseparating, while the shortest-class multiplicity profile varies across the family.

## Assumptions and scope
The complexes \(K_1,\ldots,K_6\) are defined by the six facet lists in Frank H. Lutz's file `equi_surfaces_lex_n12_p3_q7_o1_g2.txt`; the order in this result is exactly the order of that file. Each list has \(12\) vertices and \(28\) triangular facets. The verifier reconstructs \(42\) edges, checks that every edge belongs to exactly two facets, checks that every vertex has degree \(7\), and checks that every vertex link is a connected seven-cycle. Thus each listed complex is a closed combinatorial surface with face vector \((12,42,28)\) and Euler characteristic \(-2\).

Datta and Upadhyay prove that there are exactly six orientable degree-regular combinatorial \(2\)-manifolds of Euler characteristic \(-2\), equivalently exactly six orientable equivelar polyhedral maps in this parameter range. Sulanke and Lutz independently record the same count in their lexicographic enumeration. The claim concerns these six exact labeled representatives and mod-two simplicial homology.

A simple three-edge cycle means a cycle on three distinct vertices whose three edges are present. A cycle is called systolic here when its class in \(H_1(-;\mathbf F_2)\) is nonzero and its number of edges is minimum among simple cycles with nonzero class. Multiplicities count unoriented vertex triples, and two systolic cycles are grouped together precisely when their difference is a mod-two boundary.

## Proof
For any one of the six complexes, form the simplicial boundary maps over \(\mathbf F_2\). The verifier obtains \(\operatorname{rank}\partial_1=11\) and \(\operatorname{rank}\partial_2=27\). Since there are \(42\) edges,
\[
\dim H_1(K_i;\mathbf F_2)=42-11-27=4.
\]

Next enumerate every three-element vertex set whose three edges are present. The total numbers of such graph triangles are \(48,52,52,52,46,46\). Exactly \(28\) in each complex are facets, so the numbers of nonfacial three-cycles are
\[
20,24,24,24,18,18.
\]
For each nonfacial three-cycle, its edge vector is reduced against an exact row basis of \(\operatorname{im}\partial_2\). Every reduction is nonzero. Conversely, every facial triangle is itself a column of \(\partial_2\), hence has zero homology class. This proves that every graph triangle is either a face or a nonzero mod-two homology cycle.

There is no simple cycle with fewer than three edges in a simple graph, so the homology \(1\)-systole is exactly \(3\). To classify the minimizers by homology class without choosing coordinates on \(H_1\), the verifier declares two cycle vectors \(c,d\) equivalent exactly when \(c+d\in\operatorname{im}\partial_2\). Exhaustive grouping gives the six multiplicity multisets stated in the finding.

Finally, on a closed orientable surface a simple closed curve is separating exactly when its mod-two homology class vanishes. Therefore every nonfacial triangular cycle found here is nonseparating.

## Verification
Run `python verify.py`. The expected final line is:

`VERIFY_OK f=12,42,28 H1_F2_dim=4 missing3=20,24,24,24,18,18 class_mults=4+4+4+4+2+2;4+4+4+4+4+4;4+4+4+4+4+4;4+4+4+4+4+4;4+4+2+2+2+2+1+1;4+4+4+1+1+1+1+1+1 all_missing3_nonzero=yes`

The script uses only exact integer and bit-vector operations. It reconstructs all faces from the six published facet lists, checks manifold links and incidence, computes both boundary ranks, enumerates every vertex triple, verifies each nonfacial triangular boundary is outside \(\operatorname{im}\partial_2\), and groups all minimizers by exact boundary equivalence. No sampling, numerical approximation, or unproved classification of cycles enters the finite computation.

## Relationship to prior work
Datta and Upadhyay classify the exact family of six orientable degree-regular double-torus triangulations and determine their symmetry properties. Sulanke and Lutz's independent enumeration confirms that the orientable equivelar parameter pair \((n,q)=(12,7)\) with Euler characteristic \(-2\) has exactly six examples, and the Lutz surface data provide the six complete facet lists used here. These sources establish the objects and the completeness of the family, but the inspected statements do not provide the mod-two homology status of every nonfacial triangle, the six exact systolic counts, or the homology-class multiplicity spectra.

Focused searches for the exact family, nonfacial three-cycles, nonseparating triangles, mod-two systoles, the count vector \((20,24,24,24,18,18)\), and the class-multiplicity profiles did not locate a covering statement. The closest broader literature on maps of genus two concerns classification, symmetry, face width, or vertex-transitive maps rather than this complete shortest-cycle homology census.

## Limitations
The result is specific to the six 12-vertex orientable equivelar triangulations of Euler characteristic \(-2\). It classifies simple three-edge representatives in mod-two first homology; it does not classify longer systolic representatives, integral homology classes, geodesic lengths in a geometric realization, or triangulations outside this complete equivelar family. Search failure is not treated as a proof of novelty. A residual literature risk is that an unindexed computational table or a detailed treatment of genus-two vertex-transitive maps may contain part of the same finite census.

## References
1. B. Datta and A. K. Upadhyay, *Degree-regular triangulations of the double-torus*, arXiv:math/0508106v1 (5 August 2005); Forum Mathematicum 18 (2006), 1011--1025.
2. T. Sulanke and F. H. Lutz, *Isomorphism-free lexicographic enumeration of triangulated surfaces and 3-manifolds*, arXiv:math/0610022v1 (30 September 2006).
3. F. H. Lutz, `equi_surfaces_lex_n12_p3_q7_o1_g2.txt`, exact facet lists for the six orientable equivelar genus-two triangulations.
4. J. Karabáš and R. Nedela, *Archimedean solids of genus two*, Electronic Notes in Discrete Mathematics 28 (2007), 331--339.
