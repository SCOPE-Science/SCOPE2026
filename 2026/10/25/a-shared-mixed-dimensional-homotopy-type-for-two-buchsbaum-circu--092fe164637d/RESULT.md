# A shared mixed-dimensional homotopy type for two Buchsbaum circulant independence complexes

## Finding

Let \(C_{16}(S)\) be the simple graph with vertex set \(\mathbb Z/16\mathbb Z\), where distinct vertices are adjacent when their cyclic difference belongs to \(S\) or \(-S\). Define
\[
G_1=C_{16}(1,2,3,8),\qquad G_2=C_{16}(1,4,7,8).
\]
Both of the **nonisomorphic** graphs have ordinary independence complexes with the same integral homotopy type:
\[
\operatorname{Ind}(G_1)\simeq\operatorname{Ind}(G_2)\simeq S^1\vee\bigvee^{16} S^2.
\]
Consequently, in either case the reduced integral homology is \(\mathbb Z\) in degree one, \(\mathbb Z^{16}\) in degree two, and zero in all other degrees. The result strengthens the previously published classification of these two complexes as Buchsbaum but not Cohen–Macaulay.

## Assumptions and scope

The independence complex of a finite simple graph has one vertex for each graph vertex and a face for every independent vertex set. The symbols \(C_{16}(1,2,3,8)\) and \(C_{16}(1,4,7,8)\) use the undirected circulant convention; the antipodal difference \(8\) gives one neighbor per vertex. All homology groups are integral unless a coefficient field is specified. The assertion is about these two particular natural members of the published sixteen-vertex well-covered circulant list, not an infinite family.

## Proof

For each step set enumerate all \(2^{16}\) subsets by integer bit masks and retain precisely the nonempty independent sets. Both resulting complexes have face vector \((f_0,f_1,f_2)=(16,64,64)\), and no higher faces.

Construct a discrete vector field by visiting graph vertices in the specified order and, at each vertex \(v\), pairing every as-yet-unpaired face \(\sigma\) not containing \(v\) with the as-yet-unpaired face \(\sigma\cup\{v\}\), whenever both exist. The orders are
\[
(5,7,2,12,9,1,4,11,13,3,6,14,8,10,15,0)
\]
for \(G_1\), and
\[
(2,3,11,10,8,1,5,4,7,15,9,12,6,13,14,0)
\]
for \(G_2\). In each case there are exactly \(63\) pairwise disjoint matched face–coface pairs, leaving exactly one critical vertex, one critical edge, and sixteen critical triangles. The complete directed Hasse graph, oriented from higher- to lower-dimensional cells except at matched incidences, has \(144\) vertices and \(320\) arrows. A full topological sort visits all \(144\) cells, proving that the matching is acyclic. Forman's discrete Morse theorem thus gives a CW complex with one cell in dimension zero, one in dimension one, and sixteen in dimension two.

It remains to determine the attaching degrees of these two-cells, which a Morse cell count alone does not provide. Contract a spanning tree of the original one-skeleton. This gives \(49\) oriented edge generators (since \(64-16+1=49\)). The \(64\) oriented triangle boundaries form an integral \(49\times64\) presentation matrix with entries \(0,1,-1\). The standalone integer verifier performs unimodular row and column operations and obtains exactly \(48\) unit Smith pivots and a zero residual matrix in both cases. Hence \(H_1\cong\mathbb Z\) without torsion.

In the Morse CW model, the one-skeleton is a circle. Every two-cell is attached by a map \(S^1\to S^1\) of some integral degree. If any degree were nonzero, \(H_1\) of the whole space would be a finite cyclic group, contrary to the established \(H_1\cong\mathbb Z\). Thus all sixteen degrees are zero. Maps \(S^1\to S^1\) of degree zero are nullhomotopic. All two-cells attach trivially, proving the asserted homotopy equivalence.

The two base graphs are nonisomorphic: counting common neighbors at the ends of each graph edge gives distributions \(\{0:8,2:16,3:16,4:16\}\) for \(G_1\) and \(\{2:48,6:8\}\) for \(G_2\). This graph-isomorphism invariant also proves that the independence complexes are nonisomorphic as abstract simplicial complexes (their one-skeleta recover the complementary graphs).

## Verification

Run `python3 verify.py` from the unpacked package. This standalone Python-standard-library program constructs all faces, checks the two stated toggle orders, validates disjointness and incidence of all \(63\) matched pairs, topologically sorts every directed Hasse incidence, and performs integer row and column elimination of the signed boundary presentation to obtain \(48\) unit factors and a zero remainder. It also checks the two different graph-invariant distributions. Expected output is in `VERIFIER_OUTPUT.txt`. No finite sampling or non-exhaustive enumeration is used.

## Relationship to prior work

Earl, Vander Meulen, and Van Tuyl, arXiv:1505.02837v1 (first public 2015-05-11), Table 1, explicitly list both \(C_{16}(1,2,3,8)\) and \(C_{16}(1,4,7,8)\) as \(B\) (Buchsbaum but not Cohen–Macaulay), and both as one-well-covered. The full inspected paper studies vertex decomposability, shellability, and Cohen–Macaulay/Buchsbaum properties; it does not give the claimed complete homotopy type or the sixteen two-sphere multiplicity for this pair. The cycle-power result of Adamaszek cited there covers independence complexes of cycle powers; neither seven-regular graph here is a cycle power on sixteen vertices (cycle-power degrees are even below the complete graph). Adding the antipodal matching to a cycle power changes the underlying complex and is not covered by the stated pure cycle-power theorem. Mousivand's subsequent Serre-condition paper, arXiv:1512.08141, studies ring-theoretic properties; its accessible abstract does not provide the asserted homotopy classification, but its full text was not inspected.

## Limitations

Only the two explicitly named sixteen-vertex circulants are classified; no statement is made about other Buchsbaum circulants. The proof determines the homotopy type but not a preferred equivariant decomposition under dihedral symmetries. The closest primary paper was inspected in full; the Serre-condition follow-up was accessible here only by abstract. The novelty assessment therefore retains a non-exhaustive indexing risk. The computation is fully reproducible, but no independent scientific audit has been performed.

## References

1. J. Earl, K. N. Vander Meulen, A. Van Tuyl, *Independence complexes of well-covered circulant graphs*, arXiv:1505.02837v1, first public 2015-05-11, especially Table 1 and Sections 5–8; subsequently *Experimental Mathematics* 25 (2016), 441–451, DOI:10.1080/10586458.2015.1091753.
2. M. Adamaszek, *Splittings of independence complexes and the powers of cycles*, *Journal of Combinatorial Theory, Series A* 119 (2012), 1031–1047; cited as reference [1] in the primary circulant paper.
3. A. Mousivand, *Circulant S2 graphs*, arXiv:1512.08141, first public 2015-12-26; abstract inspected.
4. R. Forman, *Morse theory for cell complexes*, *Advances in Mathematics* 134 (1998), 90–145 (discrete Morse background).
