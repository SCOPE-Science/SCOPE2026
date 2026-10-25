# The quadratic-determinant twist in Coxeter independence homology

## Finding
Let \(G\) be the 28-vertex Coxeter graph, modeled by the unordered pairs (duads) of \(\mathbb P^1(\mathbb F_7)\). Two disjoint duads \(\{a,b\}\) and \(\{c,d\}\) are adjacent when their cross-ratio is \(-1\); equivalently, \([a,c][b,d]+[a,d][b,c]=0\) in \(\mathbb F_7\), where brackets are determinants of homogeneous representatives.

The full automorphism group is \(\operatorname{PGL}_2(\mathbb F_7)\). Define its quadratic determinant character \(\varepsilon([A])=\left(\frac{\det A}{7}\right)\), which is well-defined on projective matrices. Let \(U\) be the seven-dimensional augmentation subrepresentation of the natural permutation module \(\mathbb Q[\mathbb P^1(\mathbb F_7)]\).

**Theorem.** The rational top reduced homology of the independence complex has the complete symmetry representation
\[
\widetilde H_6(\operatorname{Ind}(G);\mathbb Q)\cong\varepsilon\otimes U
\]
as a \(\operatorname{PGL}_2(\mathbb F_7)\)-module. Equivalently, for every \(g\), with \(f(g)\) its number of fixed points on the eight-point projective line,
\[
\operatorname{tr}\left(g\mid\widetilde H_6\right)=\varepsilon(g)(f(g)-1).
\]
This is a rationally irreducible seven-dimensional representation, with no fixed vectors under the full group. The underlying complex has independently verified homotopy type \(\bigvee^7 S^6\), and all other reduced integral homology vanishes. The nonequivariant homotopy type is prior knowledge, not the originality claim.

## Assumptions and scope
The graph is finite, simple, and loopless. Points of \(\mathbb P^1(\mathbb F_7)\) are the seven field elements together with infinity. For finite \(a\), use the homogeneous representative \((a,1)\); for infinity use \((1,0)\). The characteristic is exactly seven; the graph has exactly 28 vertices and 42 edges. Homology is simplicial and reduced. The module is asserted over \(\mathbb Q\); no classification of its integral equivariant lattice is asserted. A determinant character is independent of the scalar representative because rescaling a two-by-two matrix changes its determinant by a square.

## Proof
**Identification and symmetry.** The harmonic-duad adjacency formula is projectively invariant. The explicit isomorphism `ISO` in the verifier identifies it with the standard Coxeter graph consisting of the 28 noncollinear three-subsets of the seven Fano points, with disjointness adjacency. This check compares all 378 unordered pairs. The verifier enumerates all 336 projective matrices and verifies each is a graph automorphism. The classical order-336 automorphism-group statement identifies these with the full automorphism group [2].

**Homology concentration.** In the Fano-triple model, exhaustive recursive enumeration finds 196,009 independent subsets, counting the empty face. Process the 28 pivot vertices in the exact order `PIVOTS` supplied in the verifier. At each pivot, pair every still-unpaired face not containing that pivot with its pivot extension when both exist. This produces 98,001 pairs, including the empty face paired with one vertex, and precisely seven unpaired seven-element faces. The complete oriented Hasse diagram, reversing the matched incidences, has 196,009 vertices and admits a complete topological sorting. Thus this is an acyclic Forman matching. After deleting the augmented empty face and its matching incidence, the associated nonaugmented matching has one critical zero-cell and seven critical six-cells, no others. Discrete Morse theory gives \(\operatorname{Ind}(G)\simeq\bigvee^7S^6\), so the only nonzero reduced rational homology is in degree six and has dimension seven. The same conclusion follows integrally.

**Equivariant Lefschetz computation.** Fix a projective automorphism \(g\). Each invariant independent vertex subset is a union of vertex orbits of \(g\). An invariant simplex with \(k\) vertices partitioned into \(c\) such orbits contributes orientation sign \((-1)^{k-c}\). Its alternating chain contribution is therefore \((-1)^{c+1}\), including the augmentation contribution from the empty face. Consequently
\[
\operatorname{tr}\left(g\mid\widetilde H_6\right)
=-\sum_{S\,\text{invariant independent}}(-1)^{c_g(S)}.
\]
Discard each vertex orbit containing a graph edge. On the surviving orbits, form a conflict graph, with two orbits adjacent if any original graph edge joins them. The sum on the right is the independence polynomial of this quotient conflict graph evaluated at \(-1\). The supplied verifier evaluates it exactly, by deletion-neighborhood recurrence, for every one of the 336 projective transformations. For one representative of each of the eight projective cycle types, a separate face-by-face computation of the signed Lefschetz number checks the result without using that recurrence.

The resulting exhaustive class table lists, in order, the projective-point cycle type, the determinant character, the homology trace, and the number of matrices:

| Cycle type on eight points | \(\varepsilon\) | Trace | Count |
| --- | ---: | ---: | ---: |
| \(1^8\) | \(+1\) | \(7\) | 1 |
| \(1\,7\) | \(+1\) | \(0\) | 48 |
| \(1^2 3^2\) | \(+1\) | \(1\) | 56 |
| \(1^2 2^3\) | \(-1\) | \(-1\) | 28 |
| \(1^2 6\) | \(-1\) | \(-1\) | 56 |
| \(2^4\) | \(+1\) | \(-1\) | 21 |
| \(4^2\) | \(+1\) | \(-1\) | 42 |
| \(8\) | \(-1\) | \(1\) | 84 |

These counts sum to 336, and every row satisfies \(\operatorname{tr}(g)=\varepsilon(g)(f(g)-1)\). Since characteristic-zero representations of finite groups are semisimple and characters determine their isomorphism classes, this proves the displayed module isomorphism. The eight-point action is two-transitive, so its seven-dimensional augmentation module is irreducible; twisting by a one-dimensional character preserves irreducibility. The trace sum over all group elements is zero, so the multiplicity of the trivial representation is zero.

## Verification
Run `python3 verify_coxeter_character.py` using Python 3.9 or newer (standard library only). The included `verification_output.txt` is its captured output. The program checks both graph presentations, face vectors, the complete acyclic matching and oriented Hasse diagram, all 336 projective transformations and their adjacency preservation, the exact class table, eight independent face-by-face Lefschetz computations, and absence of full-group invariant homology. The central executable conclusion is `VERIFY_OK_COXETER_PGL_CHARACTER`.

## Relationship to prior work
Barmak [1] develops general methods for independence complexes of triangle-free graphs, including Kneser-related examples, but does not compute the Coxeter graph's full equivariant homology character. Godsil and Royle [2, Section 4.6] give a classical Coxeter graph construction and its order-336 automorphism symmetry, but no independence-complex homology module. An indexed 2026 computation [3] already identifies the nonequivariant wedge of seven six-spheres. That fact by itself supplies only the homology rank: it does not distinguish the ordinary augmentation character from its nontrivial quadratic twist. In particular, an eight-cycle has trace \(+1\) here, whereas the untwisted augmentation character gives \(-1\). Related Heawood and other graph-complex symmetry calculations involve different objects and representations.

## Limitations
The result classifies rational, not integral, equivariant homology. The finite exhaustive character certificate is exact for this graph, not a theorem about an infinite family of graphs. Identification with the full automorphism group uses the classical graph-theory result [2]; the action of the indicated 336 transformations is checked internally. Equivalently formulated or unindexed earlier equivariant computations may exist. This is not an independently audited result.

## References
[1] J. A. Barmak, *Star clusters in independence complexes of graphs*, arXiv:1007.0418v1, first posted 2010-07-02, https://arxiv.org/html/1007.0418v1.

[2] C. Godsil and G. Royle, *Algebraic Graph Theory*, Section 4.6, Springer, 2001 (classical Coxeter graph and automorphism group).

[3] *The Coxeter graph independence complex is a wedge of seven six-spheres*, published mathematical record, 2026-10-11, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-the-coxeter-graph-independence-complex-is-bigvee-7-s-6--8a1bdfa47e09.
