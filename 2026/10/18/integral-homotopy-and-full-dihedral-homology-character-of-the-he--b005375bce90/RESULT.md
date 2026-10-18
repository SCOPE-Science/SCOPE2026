# Integral homotopy and full dihedral homology character of the Herschel matching complex

## Finding

Let \(H\) be the Herschel graph, realized with the explicit eleven-vertex edge set below, and let \(\mathcal M(H)\) denote its ordinary matching complex: simplices are nonempty sets of pairwise vertex-disjoint edges of \(H\), together with the empty face. There is an integral homotopy equivalence
\[
\mathcal M(H)\simeq\bigvee^{12}S^3.
\]
The natural action of its full automorphism group \(\operatorname{Aut}(H)\cong S_3\times C_2\) on the only nonzero reduced rational homology is
\[
\widetilde H_3(\mathcal M(H);\mathbb Q)
\cong (\mathbf1\boxtimes\mathbf1)\oplus
(\operatorname{sgn}\boxtimes\varepsilon)\oplus
2(V\boxtimes\mathbf1)\oplus3(V\boxtimes\varepsilon),
\]
where \(V\) is the two-dimensional standard representation of \(S_3\) and \(\varepsilon\) is the nontrivial one-dimensional character of \(C_2\). In particular, the full-symmetry fixed subspace is one-dimensional. No assertion is made here about an integral direct-sum decomposition of the automorphism module.

## Assumptions and scope

The vertices of \(H\) are labeled `0` through `10` and its edges, written as unordered vertex pairs, are exactly

```text
(0,3) (0,4) (0,7) (0,8)
(1,3) (1,4) (1,5) (1,6)
(2,5) (2,6) (2,7) (2,8)
(3,9) (4,10) (5,9) (6,10) (7,9) (8,10)
```

Vertices `0,1,2` have degree four; all other vertices have degree three. For every pair of vertices in `0,1,2` there are exactly two common neighbors, one adjacent to `9` and the other to `10`. This is the standard bipartite eleven-vertex, eighteen-edge Herschel graph (the smallest non-Hamiltonian polyhedral graph). The matching complex is the independence complex of its line graph, **not** the independence complex of the original graph. Coefficients are integral unless \(\mathbb Q\) is expressly specified. Graph automorphisms act on oriented simplices by the signs of their induced edge permutations.

## Proof

**1. Complete matching-complex face enumeration.** Index the eighteen listed edges in increasing lexicographic order from `0` to `17`. Encode a face by a length-eighteen bit mask. A mask is admitted precisely when no two selected edges share an endpoint. Exhausting every mask from `0` through `262143` produces exactly `752` faces including the empty face, with nonempty face vector
\[
(f_0,f_1,f_2,f_3,f_4)=(18,111,280,270,72).
\]
The verifier constructs this set from the displayed graph, without importing a face database.

**2. Integral homotopy certificate.** Apply elementary face-poset toggles sequentially at edge indices

```text
6,11,1,0,16,12,7,2,13,15,17,14,4,10,3,8,5,9
```

At each index \(i\), pair every still-unpaired nonempty matching \(\sigma\) not containing \(i\) with \(\sigma\cup\{i\}\), whenever that second matching is also still unpaired. Exactly `369` pairs are obtained. The unmatched faces consist of one vertex and twelve three-simplices. The verifier checks **every** one of the `2502` codimension-one incidences between nonempty faces: incidences in the proposed matching are oriented from lower to upper face, and every other incidence is oriented from upper to lower face. A complete topological traversal of this oriented Hasse diagram visits all `751` nonempty faces, proving the orientation is acyclic. Thus the matching is an acyclic discrete-Morse matching, not merely a count of critical cells. Forman's discrete Morse theorem yields a CW model with one zero-cell and twelve three-cells and no cells in any other dimension. Every three-cell attaches to the single zero-cell, so this model is a wedge of twelve three-spheres. It is an integral homotopy statement; no reduction of coefficients is used.

**3. The full graph automorphism group.** The three degree-four vertices may be permuted arbitrarily. The two degree-three vertices `9,10`, uniquely characterized by having no degree-four neighbors, may be exchanged simultaneously with the two members of every common-neighbor pair of degree-four vertices. These choices extend uniquely to automorphisms, giving an embedded \(S_3\times C_2\) of order twelve. Conversely, every automorphism preserves the degree-four set, the distinguished two vertices `9,10`, and their incident pairs, so there are no further automorphisms.

**4. Signed character and irreducible decomposition.** For any automorphism \(g\), let \(F\) run over all nonempty matching-complex faces fixed setwise by \(g\), and let \(\operatorname{sgn}(g|F)\) be the sign of the permutation of their vertices (edges of \(H\)). The reduced simplicial Lefschetz number is
\[
\widetilde L(g)=-1+\sum_{gF=F}(-1)^{\dim F}\operatorname{sgn}(g|F).
\]
Since reduced homology is concentrated in degree three, \(\operatorname{tr}(g|\widetilde H_3)=-\widetilde L(g)\). The exhaustive signed fixed-face enumeration gives the following class traces, in order identity/transposition/three-cycle in \(S_3\), first without then with the \(C_2\)-flip:
\[
(12,\ 0,\ -3;\ -2,\ 2,\ 1).
\]
Using the three irreducible characters \((1,1,1)\), \((1,-1,1)\), and \((2,0,-1)\) of \(S_3\) and both signs on \(C_2\), ordinary character inner products yield multiplicities \((1,0)\) for the trivial \(S_3\) character, \((0,1)\) for its sign character, and \((2,3)\) for its standard character, with the pairs ordered by even/odd \(C_2\)-parity. Their weighted dimensions sum to twelve. This proves the asserted rational representation and fixed-subspace dimension.

## Verification

The accompanying standalone `verify.py` implements the complete graph and face enumeration, the toggling matching, the full Hasse-diagram acyclicity check, construction of all twelve graph automorphisms, signed Lefschetz traces and rational character inner products. Execute `python3 verify.py` using Python's standard library. The successful run prints `VERIFY_OK_HERSCHEL_MATCHING_COMPLEX_DIHEDRAL_HOMOLOGY` and all intermediate counts and character multiplicities. The verifier is finite and exhaustive for **this one explicit graph**; the mathematical transition from an acyclic matching to integral homotopy follows from the standard discrete-Morse theorem. Neither code execution nor self-review constitutes independent external certification.

## Relationship to prior work

The Herschel graph is the canonical smallest-edge non-Hamiltonian polyhedral graph; a public construction and its order-twelve symmetry are described by Lawson-Perfect (2013). Jonsson (2012) analyzes matching-complex homology of complete graphs through exact sequences, not the ordinary matching complex of this proper eighteen-edge Herschel graph. Bayer, Goeckner and Jelić Milutinović (2019) classify matching complexes with a homology-manifold condition; that classification does not supply the asserted Herschel homotopy or representation. Bayer, Jelić Milutinović and Vega (2024) prove results for **outerplanar** graph matching complexes; this three-connected nonouterplanar graph falls outside that hypothesis. The previously published result for the ordinary independence complex \(\operatorname{Ind}(H)\) does not determine \(\mathcal M(H)=\operatorname{Ind}(L(H))\). Searches of published mathematical findings found similar statements for the Goldner–Harary, Heawood and other graphs but not the same Herschel matching complex. The contribution is the exact integral homotopy type together with the full twelve-element rational symmetry character.

## Limitations

The rational isotypic decomposition is proved, but no integral decomposition into direct summands of group lattices is asserted. This theorem concerns a single, explicitly specified graph and does not classify arbitrary non-Hamiltonian polyhedral graphs. A chapter-length treatment of matching complexes in Jonsson's monograph could be inspected only at abstract level; unindexed or inaccessible literature may contain equivalent calculations. Absence of indexed matches does not prove absolute publication priority. Independent mathematical review has not been performed.

## References

1. Christian Lawson-Perfect, “An enneahedron for Herschel,” *The Aperiodical*, posted 2013-10-01, https://aperiodical.com/2013/10/an-enneahedron-for-herschel/ .
2. Jakob Jonsson, “Exact Sequences for the Homology of the Matching Complex,” arXiv:1203.5641, first submitted 2012-03-26, https://arxiv.org/abs/1203.5641 .
3. Margaret Bayer, Bennet Goeckner and Marija Jelić Milutinović, “Manifold Matching Complexes,” arXiv:1906.03328, https://arxiv.org/abs/1906.03328 .
4. Margaret Bayer, Marija Jelić Milutinović and Lejla Vega, “Matching Complexes of Outerplanar Graphs,” arXiv:2411.04601, https://arxiv.org/abs/2411.04601 .
5. Robin Forman, “Morse theory for cell complexes,” *Advances in Mathematics* **134** (1998), 90–145, doi:10.1006/aima.1997.1650 .
