# A projective-plane summand in the scale-two Čech nerve of the Clebsch graph

## Finding

Let \(C\) be the five-regular Clebsch graph (the folded five-cube), and let \(\mathcal N(C,2)\) be the intrinsic graph Čech nerve of closed radius-one metric balls centered at its vertices. Then
\[
\mathcal N(C,2)\simeq \mathbb{RP}^{2}\vee\bigvee^{55}S^{2}.
\]
In particular, its fundamental group is \(\mathbb Z/2\), and its reduced integral homology is \(\mathbb Z/2\) in degree one, \(\mathbb Z^{55}\) in degree two, and zero otherwise. The complex is pure of dimension five and is not shellable.

## Assumptions and scope

Identify the vertex set with \(V=\mathbb F_2^4\), represented by integer masks from zero through fifteen. Join two vertices \(a,b\) exactly when their bitwise difference belongs to \(\{1,2,4,8,15\}\). This is the standard folded five-dimensional hypercube: quotient the five-dimensional cube by antipodal identification, and choose the representative with last coordinate zero. The edges of the geometric realization have unit length, and distances use its shortest-path metric. The closed balls defining \(\mathcal N(C,2)\) have radius \(2/2=1\). No statement is made about other folded hypercubes or scales.

The graph is strongly regular with parameters \((16,5,0,2)\), as follows directly by counting common neighbors in the displayed Cayley presentation; these parameters and the folded-cube identity are independently checked by the supplied verifier.

## Proof

**Step 1: Exact nerve.** By the even-integer-scale characterization of graph Čech nerves (Adams–Shukla–Singh, Lemma 2.2), the facets are the closed one-neighborhoods
\[
F_v=\{v,v\oplus1,v\oplus2,v\oplus4,v\oplus8,v\oplus15\},\qquad v\in\mathbb F_2^4.
\]
Equivalently, every simplex is a subset of some \(F_v\). These sixteen distinct facets all have six vertices. Exhaustively taking their subfaces gives the face vector in dimensions zero through five
\[
(16,120,320,240,96,16),
\]
consisting of 808 nonempty simplices. The empty face is included solely in the augmented-chain and directed-Hasse checks.

**Step 2: Explicit acyclic matching.** Encode every face by its sixteen-bit characteristic mask. Starting with all 809 faces, for each vertex label \(v=0,1,\ldots,15\) in that order, traverse currently unmatched face masks in increasing numerical order. Whenever \(v\) is absent from a face \(\sigma\) and \(\sigma\cup\{v\}\) remains unmatched, pair these two faces and remove both from further consideration. The successive numbers of pairs are
\[
(172,88,57,48,2,2,4,0,0,1,2,0,0,0,0,0).
\]
There are exactly 376 pairs. The first is \((\varnothing,\{0\})\). In the augmented face poset, direct each cover relation from its higher to its lower face, reversing the direction exactly for matched incidences. A complete traversal of all 2,752 directed cover incidences gives an acyclic graph: Kahn's topological sorting removes all 809 vertices. This is a finite, exhaustive acyclicity certificate, not a heuristic. Discarding the augmented pair leaves an ordinary acyclic matching with 375 pairs, one critical vertex, one critical edge \(\{1,6\}\), and 56 critical triangles, and no critical cells in higher dimensions.

**Step 3: Integral Morse differential and attaching maps.** Give each simplex its increasing-label orientation. For a matched edge \(e\) and triangle \(t\) with \(e\) the lower member, the signed gradient-path reduction replaces \(e\) by the negative of the other two oriented boundary edges of \(t\), divided by the unit incidence coefficient. Edges matched down to a vertex project to zero. Applying this recursion to the 56 critical triangles yields exactly 44 zero incidence coefficients, six coefficients \(+2\), and six coefficients \(-2\) against the single critical edge. Separate integral unit-pivot chain cancellation of all matched pairs reproduces the identical full coefficient vector, with critical triangles ordered by their bit masks. Both algorithms are written out in `verify.py`; they compute with exact integers and check the intermediate pair pivots.

Forman's discrete Morse theorem therefore yields a CW complex with one zero-cell, one one-cell, and 56 two-cells attached to the resulting circle with winding degrees in \(\{0,+2,-2\}\), with at least one degree of absolute value two and no other nonzero degrees. Attach one degree-two cell first; the resulting two-skeleton is \(\mathbb{RP}^2\). Every remaining attaching loop has degree zero or \(\pm2\), hence is null-homotopic after the first degree-two cell has been attached. Attaching the remaining 55 two-cells adds a wedge of 55 two-spheres. This proves the stated integral homotopy equivalence, rather than merely a homology calculation.

The displayed homology and fundamental group follow. A pure shellable five-dimensional simplicial complex has reduced homology concentrated in degree five and torsion-free; nontrivial first-homology torsion therefore rules out shellability here.

## Verification

Run `python3 verify.py` with Python 3 and only its standard library. The program constructs the graph and all 809 augmented faces from the five generators, checks strong regularity, enumerates and verifies every matching pair and Hasse arrow, and derives the exact integral Morse boundary by two distinct methods. It prints `VERIFY_OK` on success. Direct finite-field simplicial boundary-rank calculations in dimensions one through five yield \((15,104,160,80,16)\) over \(\mathbb F_2\) and \((15,105,160,80,16)\) over \(\mathbb F_3\); these independently confirm the two-torsion detected integrally.

All finite checks are exhaustive over the explicitly defined sixteen-vertex graph. The topological identification uses the stated discrete-Morse and CW attaching-map arguments, not an inference from finite-field ranks.

## Relationship to prior work

Adams, Shukla and Singh formulate intrinsic graph Čech nerves, establish their even-scale neighborhood characterization, and classify the scale-two complexes of ordinary hypercubes as wedges of two-spheres. The folded five-cube is not an ordinary hypercube; that theorem does not cover its closed-neighborhood nerve. The appearance of \(\mathbb{RP}^2\) therefore contrasts with the torsion-free unfurled family.

Previte develops the more general distance-neighborhood construction and studies cycles, trees, one-point unions, and examples including the Petersen graph; her results do not determine this Clebsch complex. Matsushita proves general equivalences involving closed-neighborhood complexes, graph fundamental groups, canonical double coverings, and Alexander duality, and treats rook graphs as an example; those statements do not determine the unsuspended Clebsch nerve's integral homotopy type. The ordinary open-neighborhood and independence or matching complexes are different objects, so their calculations do not determine this nerve merely by similarity of graph or name.

## Limitations

The theorem concerns the one explicitly specified finite graph and scale. It does not assert a formula for all folded hypercubes or classify the entire persistence filtration. The finite verification is supplied to make the discrete-Morse and integer computation fully replayable; a proof of correctness must also use the topological implications explained above. The literature comparison cannot rule out an unindexed equivalent computation.

## References

1. Henry Adams, Samir Shukla and Anurag Singh, *Čech complexes of hypercube graphs*, arXiv:2212.05871 (first public 2022-12-12), especially Lemma 2.2 and Theorem 4.1. https://arxiv.org/abs/2212.05871
2. Takahiro Matsushita, *Closed neighborhood complexes of graphs*, arXiv:2511.12608 (2025), especially Theorems 1.2, 1.4, 1.5 and Example 3.5. https://arxiv.org/abs/2511.12608
3. Corrine Previte, *The D-Neighborhood Complex of a Graph*, Colorado State University dissertation (2014), Definition 12 and §3.2. https://doi.org/10.25675/3.018305
4. *Clebsch Graph*, Wolfram MathWorld, for the standard folded-cube and strongly regular identifications. https://mathworld.wolfram.com/ClebschGraph.html
