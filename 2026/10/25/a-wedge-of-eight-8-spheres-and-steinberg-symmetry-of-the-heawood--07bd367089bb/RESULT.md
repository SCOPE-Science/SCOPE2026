# A wedge of eight 8-spheres and Steinberg symmetry of the Heawood induced-forest complex

## Finding

Let \(H\) be the point–line incidence graph of the Fano projective plane. Its *induced-forest complex* is the finite simplicial complex
\[
\mathcal F(H)=\{A\subseteq V(H): H[A]\text{ has no cycle}\}.
\]
There is an integral homotopy equivalence
\[
\mathcal F(H)\simeq\bigvee^{8}S^8.
\]
Moreover, for the point–line-preserving group \(G=\mathrm{GL}_3(\mathbb F_2)\) of order 168, there is an isomorphism of rational \(G\)-representations
\[
\widetilde H_8(\mathcal F(H);\mathbb Q)
\cong_{\mathbb Q G}H_1(H;\mathbb Q)
\cong_{\mathbb Q G}\operatorname{St}_3(\mathbb F_2).
\]
This eight-dimensional representation is irreducible over \(\mathbb C\), hence also irreducible over \(\mathbb Q\). The multiplicities of its character values on the 168 group elements are respectively \((-1,56)\), \((0,63)\), \((1,48)\), and \((8,1)\). It has no \(G\)-fixed vector.

## Assumptions and scope

Use the Fano plane whose seven lines are \(\{t,t+1,t+3\}\) modulo seven, for \(t=0,\ldots,6\). Give points labels 0 through 6 and give the lexicographically sorted lines labels 7 through 13. Join a point to a line precisely when it lies on that line. These rules specify all 14 vertices and 21 edges. Each pair of points lies on exactly one line, so the incidence graph is connected. The complex consists of all vertex *subsets*, not edge subsets. This distinction matters: matching, independence, cut, and Vietoris–Rips complexes of the same graph have different face predicates. The homotopy statement is nonequivariant and integral; the module statement concerns only the specified 168-element subgroup, not the full 336-element graph automorphism group. The result does not assert an integral module isomorphism or an equivariant homotopy equivalence.

## Proof

**Face enumeration.** For each of the \(2^{14}=16{,}384\) vertex subsets, decide whether the induced graph is acyclic. Two independently implemented tests agree on every subset: an incremental union–find test rejects the first edge that completes a cycle; alternatively, breadth-first component counting verifies \(|E(H[A])|=|A|-c(H[A])\). Exactly 12,792 masks qualify, including the empty face. In dimensions -1 through nine their face numbers are
\[
(1,14,91,364,1001,2002,2975,3208,2254,812,70).
\]
The complex is nonpure, with 70 nine-dimensional faces; no purity or shellability assumption is used.

**Explicit discrete-Morse reduction.** Regard each face as its fourteen-bit mask. Starting with all 12,792 faces unmatched, repeatedly choose a vertex maximizing the number of currently unmatched pairs \((A,A\cup\{v\})\) with \(v\notin A\) and both masks unmatched; resolve ties by the smallest vertex and remove all these disjoint pairs. The chosen pivots and their pair counts are exactly
\[
(0,5832),(10,294),(3,138),(11,64),(2,26),(13,22),(5,14),(6,1),(9,1).
\]
There are 6,392 pairs, leaving exactly eight unpaired faces, each with nine vertices (dimension eight). To certify acyclicity, orient every codimension-one Hasse incidence upward if it is matched and downward otherwise. There are exactly 81,648 such incidences, and a topological sort visits all 12,792 faces: the directed graph has no cycle. This is a *complete* check, not a sample or a numerical homology guess.

The augmented matching pairs the empty face with a singleton; delete that pair to obtain an ordinary acyclic matching with one critical vertex and exactly eight critical eight-cells. Forman's discrete Morse theorem gives a CW model with only those cells. As each higher cell attaches to the single point, its attaching map is constant, and the CW space is a wedge of eight eight-spheres. This proves the asserted integral homotopy type, including the absence of torsion or other reduced homology.

**Equivariant rational homology.** Identify the seven nonzero vectors of \(\mathbb F_2^3\) with Fano points by the ordered labels \((1,2,4,3,6,7,5)\); lines become two-dimensional subspaces. Enumerate \(G=\mathrm{GL}_3(\mathbb F_2)\) by the images of its three basis vectors, obtaining exactly \(7\cdot6\cdot4=168\) distinct graph automorphisms preserving points and lines.

For each \(g\in G\), compute the trace on reduced simplicial homology by the signed simplicial Lefschetz identity
\[
\chi_{\mathcal F}(g)=-1+\sum_{\substack{\varnothing\ne A\in\mathcal F(H)\\gA=A}}(-1)^{|A|-1}\operatorname{sgn}(g|_A).
\]
Since reduced homology is concentrated in degree eight, this is exactly the degree-eight homology character. Separately the incidence graph \(H\) is the one-dimensional spherical Tits building for \(\mathrm{GL}_3(\mathbb F_2)\). It is connected and its first Betti number is \(21-14+1=8\). The chain exact sequence gives its first-homology character
\[
\chi_{H_1(H)}(g)=\#\{\text{edges fixed by }g\}-\#\{\text{vertices fixed by }g\}+1.
\]
Because \(G\) preserves the bipartition, an invariant edge is fixed individually at both endpoints and no edge orientation sign occurs. The two independently computed traces agree for **every one** of the 168 group elements. Their value distribution is \(\{8:1,1:48,-1:56,0:63\}\). Thus their complex and rational characters coincide, so semisimplicity in characteristic zero implies the two rational representations are isomorphic. The building's first homology is the Steinberg representation by definition.

Finally, \(\sum_{g\in G}\chi(g)^2=168=|G|\), so the complex character has irreducible norm one; and \(\sum_{g\in G}\chi(g)=0\), so no trivial constituent occurs. The Fano point–line action and all character assertions are checked by the executable verifier.

## Verification

The accompanying self-contained Python 3 file `heawood_induced_forest_verify.py` needs only the standard library. Run `python3 heawood_induced_forest_verify.py`. Its checks are assertions, and successful output terminates in `VERIFY_OK`. The accompanying `heawood_induced_forest_verify_output.txt` records the expected stdout. The code reproduces both forest predicates, the complete Morse pairing and acyclicity, all 168 symmetries, all signed Lefschetz traces, their agreement with the building's first-homology character, the irreducible norm and invariant-space calculation. The finite exhaustive computation is a proof of this specifically defined finite complex, not a claim about arbitrary graphs.

## Relationship to prior work

Taylan's 2015 treatment of forbidden-induced-subgraph (devoid) complexes establishes the general setting and matching techniques; it does not give the specific Fano incidence graph classification. Carnero Bravo's 2023 forest-filtration paper explicitly defines \(\mathcal F_\infty(G)\) as the induced-acyclic-vertex complex and obtains results for several graph families. Its inspected accessible full text does not determine the Heawood case or its character. The Fano incidence graph and its 168-element collineation group are classical. Independently, the 8-dimensional first homology of its Tits building is the classical Steinberg module. The present statement is the *new comparison* identifying the forest complex's integral homotopy type and its rational symmetry representation with that module. Known results for matching, independence and cut complexes of the same graph concern different simplicial complexes and do not imply this calculation.

## Limitations

The result is restricted to the explicit fourteen-vertex Fano incidence graph and its point–line-preserving subgroup. Its proof uses exhaustive exact finite computations; it provides no uniform theorem for arbitrary finite projective planes. Equality of rational group characters does not give a canonical or integral module isomorphism. Similar unindexed computations could exist; the accessible literature comparison is not a proof of absolute novelty. Independent mathematical validation has not been performed.

## References

- D. Taylan, *Matching trees for simplicial complexes and homotopy type of devoid complexes of graphs*, arXiv:1501.06754v1, first submitted 2015-01-27, https://arxiv.org/abs/1501.06754.
- A. Carnero Bravo, *The Forest Filtration of a Graph*, arXiv:2307.13271v1, first submitted 2023-07-25, https://arxiv.org/abs/2307.13271.
- J. C. Baez, *Heawood Graph*, AMS Visual Insight, 2015-08-01, https://blogs.ams.org/visualinsight/2015/08/01/heawood-graph/.
- G. Z. Arone and W. G. Dwyer, *Partition Complexes, Tits Buildings and Symmetric Products*, Proc. London Math. Soc. 82 (2001), 229–256, doi:10.1112/S0024611500012715.
- R. Forman, *Morse theory for cell complexes*, Adv. Math. 134 (1998), 90–145, doi:10.1006/aima.1997.1650.
