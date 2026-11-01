# Integral multipath topology and coordinate-symmetry character of the oriented Boolean four-cube

## Finding

Let \(B_4\) be the Boolean lattice of all subsets of \(\{1,2,3,4\}\), and orient every Hasse edge upward, from a subset to a subset obtained by adding one element. For this 16-vertex, 32-arc directed graph \(D\), let \(X(D)\) denote the multipath complex: its vertices are directed arcs, and a set of arcs is a simplex exactly when its spanning subgraph is a disjoint union of directed paths and isolated vertices. Then, integrally,

\[
 X(D)\simeq\bigvee^{225}S^7.
\]

The coordinate-permutation group \(S_4\) preserves \(X(D)\). On \(\widetilde H_7(X(D);\mathbb Q)\), the character in the conjugacy-class order \((1^4),(2,1^2),(2^2),(3,1),(4)\) is

\[
 (225,1,1,0,1).
\]

As a rational \(S_4\)-representation, with irreducibles indexed by integer partitions, this is

\[
 10V_{(4)}\oplus9V_{(1^4)}\oplus28V_{(3,1)}
 \oplus28V_{(2,1,1)}\oplus19V_{(2,2)}.
\]

In particular, its coordinate-permutation invariant subspace has dimension \(10\). All other reduced integral homology groups vanish.

## Assumptions and scope

The directed graph is the **upward** Hasse diagram, not the bidirected cube, an arbitrary acyclic orientation, or the underlying undirected graph. Its vertices are the \(16\) subsets of a four-element set. There is precisely one arc \(A\to B\) when \(A\subset B\) and \(|B|=|A|+1\). The complex is the ordinary arc-subset multipath complex; it is not the path homology of the directed graph. The homotopy equivalence is nonequivariant, while the representation assertion concerns rational reduced homology under coordinate permutations only. The proof does not assert an equivariant wedge decomposition.

## Proof

**1. Admissibility and exact rank decomposition.** Every directed edge increases subset cardinality, so a directed cycle cannot occur. A chosen arc set is therefore a multipath if and only if each lattice vertex is the tail of at most one chosen arc and the head of at most one chosen arc. Split the directed edges into four disjoint rank layers \(E_k\), comprising the edges from rank \(k\) to rank \(k+1\), for \(0\leq k\leq3\). Each tail constraint belongs to exactly one rank layer and each head constraint also belongs to exactly one rank layer. Thus distinct rank layers impose no mutual restrictions, even where their directed paths concatenate at a lattice vertex. Consequently there is an isomorphism **of simplicial complexes**

\[
 X(D)=K_0*K_1*K_2*K_3,
\]

where \(K_k\) is the matching complex of the bipartite inclusion graph between ranks \(k\) and \(k+1\), and \(*\) denotes simplicial join. This argument also establishes the analogous rank-layer isomorphism for any upward-oriented Boolean lattice; the explicit topology below is restricted to four coordinates.

**2. Four factors.** The bottom and top inclusion graphs are four-edge stars. Their matching complexes are four discrete points, hence each is homotopy equivalent to \(\bigvee^3 S^0\). The rank-one-to-rank-two inclusion graph has the four singleton subsets on one side and the six two-element subsets on the other, with incidence by containment. It is precisely the graph obtained by subdividing each edge of \(K_4\) once. Complementing subsets identifies the rank-two-to-rank-three graph with this same incidence graph, equivariantly under \(S_4\).

Write \(Y\) for the matching complex of this subdivided tetrahedral graph. Its simplices, including the empty simplex, have face-enumerator

\[
 1+12t+48t^2+72t^3+30t^4.
\]

There are \(162\) nonempty faces. An explicit lexicographic pivot matching on the complete nonempty simplicial face poset pairs \(156\) of them into \(78\) pairs. It leaves one critical vertex and exactly five critical triangles, with no other critical faces. The supplied checker reconstructs every face, every pair, and all \(432\) Hasse incidences, and proves that reversing the paired incidences makes a directed acyclic graph. Forman's discrete Morse theorem therefore yields

\[
 Y\simeq\bigvee^5 S^2.
\]

For reproducibility, enumerate the twelve inclusion edges in increasing lexicographic order of source and target, enumerate all admissible face bitmasks, and visit pivot indices successively. For each pivot, pair an unremoved face lacking the pivot with its pivot extension if both remain. Omit the pair involving the empty face from the ordinary, nonaugmented matching. The remaining \(78\) pairs and the six critical faces are stored in `morse_certificate.json`; `verify_boolean_cube_multipath.py` regenerates and checks them. The same algorithm independently checks the complementary middle factor.

**3. Integral homotopy.** Taking joins of the four factor homotopy types gives \(3\cdot5\cdot5\cdot3=225\) sphere summands. Their dimension is \(0+2+2+0+3=7\), since each join adds one dimension. This proves the integral homotopy equivalence. In particular it proves torsion-freeness without relying on modular boundary calculations.

**4. Coordinate symmetry.** The \(S_4\)-action preserves each rank layer. On the reduced zero-dimensional homology of the four-point factors it is the three-dimensional standard representation \(V\) with character \(\chi_V(g)=\#\operatorname{Fix}_{\{1,2,3,4\}}(g)-1\). Let \(W=\widetilde H_2(Y;\mathbb Q)\). For each permutation, the trace of its action on \(W\) is computed exactly as the reduced simplicial Lefschetz number

\[
 \chi_W(g)=-1+\sum_{\substack{\varnothing\neq F\in Y\\gF=F}}
 (-1)^{|F|-1}\operatorname{sgn}(g|_F).
\]

Here the sign is the sign of the permutation of the selected directed-edge vertices in the fixed face. The complete \(163\)-face computation gives \(\chi_W=(5,-1,1,2,1)\) in the stated class order. Complementation identifies the two middle modules as \(S_4\)-representations. Since the rank factors are individually invariant, the equivariant reduced join Künneth formula gives

\[
 \widetilde H_7(X(D);\mathbb Q)\cong V\otimes W\otimes W\otimes V.
\]

In particular \(\chi=(\chi_V\chi_W)^2=(225,1,1,0,1)\). Inner products with the five rational irreducible characters of \(S_4\), using class sizes \((1,6,3,8,6)\), give the displayed multiplicities \((10,9,28,28,19)\). Their dimension sum is \(10+9+84+84+38=225\), agreeing with the topological calculation.

## Verification

Run `python3 verify_boolean_cube_multipath.py` in a directory containing the accompanying `morse_certificate.json`. The checker uses the standard library only and exits nonzero on any violated assertion. Its recorded full output is in `verification_output.txt`.

Besides the two exact acyclic-Morse certificates and independent mod-two boundary ranks \((11,37,30)\) in each middle factor, an independent dynamic-programming enumeration using only indegree/outdegree constraints on all \(32\) arcs computes the full rank-oriented four-cube face polynomial

\[
 1+32t+448t^2+3600t^3+18300t^4+61104t^5+
 134592t^6+190944t^7+164484t^8+76320t^9+14400t^{10}.
\]

There are \(664224\) nonempty faces. This polynomial agrees coefficient-by-coefficient with \((1+4t)^2(1+12t+48t^2+72t^3+30t^4)^2\). The checker evaluates all \(24\) coordinate permutations, both middle-factor Lefschetz characters and the complete irreducible character decomposition. It therefore verifies more than an Euler-characteristic check. Exact finite combinatorial computations are used only on the explicitly specified 32-arc graph, not as a substitute for the rank-join proof.

## Relationship to prior work

Caputi, Collari and Di Trani developed path posets and their simplicial interpretation; Caputi, Collari, Di Trani and Smith established general dynamical-module join decompositions and computed multipath homotopy types for paths, polygons, certain two-row grids and transitive tournaments. Those results motivate the rank decomposition, but their inspected statements do not supply the homotopy type of the four-dimensional Boolean-lattice Hasse digraph or its coordinate-symmetry character. In particular, the two-row grid results concern products of a linear digraph with a directed edge, not the fourfold Cartesian product of directed edges.

The middle factor is also the ordinary matching complex of the once-subdivided tetrahedral graph, so matching-complex literature is an important potential alternative source of this calculation. The explicit five-sphere calculation, its embedding in the Boolean-rank join, and the full \(S_4\)-character form the claim here. No originality is asserted for the general notion of multipath complex, the general join theorem, or the abstract representation-theoretic trace formula.

## Limitations

The statement classifies the upward orientation in dimension exactly four. It does not determine the analogous middle-rank matching complexes in five or more Boolean coordinates, nor the multipath homotopy type for arbitrary orientations. Only the subgroup of coordinate permutations is represented; orientation-reversing cube symmetries are excluded. The full complex is nine-dimensional as a simplicial complex although its homotopy is concentrated in dimension seven. A mathematically equivalent calculation not captured by the inspected literature remains possible; novelty is a best-knowledge assessment rather than a proof of absence from every publication.

## References

1. Luigi Caputi, Carlo Collari and Sabino Di Trani, *Combinatorial and Topological Aspects of Path Posets, and Multipath Cohomology*, first public preprint 2021-10-21, arXiv:2110.11206, especially Sections 2 and 6. https://arxiv.org/abs/2110.11206
2. Luigi Caputi, Carlo Collari, Sabino Di Trani and Jason P. Smith, *On the homotopy type of multipath complexes*, first public preprint 2022-08-09, arXiv:2208.04656, especially Theorem 4.11, Lemma 4.8 and Section 4.3. https://arxiv.org/abs/2208.04656
