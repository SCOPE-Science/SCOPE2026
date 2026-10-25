# Odd-cycle-source Hom complexes of high-girth graphs recover two consecutive cycle counts

## Finding

Let \(g\ge5\) be odd and \(H\) a finite undirected loopless simple graph with girth at least \(g\) (girth infinity is permitted). For every positive integer \(j\), write \(c_j(H)\) for the number of distinct unoriented simple \(j\)-cycles in \(H\), identifying cyclic rotations and reversals. Set \(m=g+2\). Then

\[\operatorname{Hom}(C_m,H)\simeq\left(\bigsqcup_{2c_g(H)} S^1\right)\sqcup\left(\bigsqcup_{2m c_m(H)}\{\mathrm{point}\}\right).\]

More precisely, the isolated points are exactly the injective homomorphisms onto \(m\)-cycles. The other components are indexed by an unoriented \(g\)-cycle together with a choice of its two orientations. Each such component simplicially collapses onto the standard polygon in \(\operatorname{Hom}(C_m,C_g)\) with exactly \(gm\) vertices. Hence \(\beta_0=2c_g(H)+2m c_m(H)\), \(\beta_1=2c_g(H)\), and \(\beta_i=0\) for \(i\ge2\), all over \(\mathbb Z\); the complex is empty if both specified cycle counts vanish.

## Assumptions and scope

The source is the cyclic graph on \(m\) indexed vertices, rather than a directed cycle. The standard polyhedral graph-Hom complex has vertices the graph homomorphisms \(f:C_m\to H\) and faces the tuples \((A_0,\ldots,A_{m-1})\) of nonempty vertex sets with \(A_i\times A_{i+1}\subseteq E(H)\) (indices modulo \(m\)); each face is a product of simplices. We treat disconnected target graphs componentwise. No edges with repeated endpoints or multiple edges are allowed. Both the girth condition and oddness are used; no assertion concerns larger odd source lengths.

## Proof

**Closed-walk reduction.** Let \(W=(v_0,v_1,\ldots,v_m=v_0)\) be a graph homomorphism regarded as a closed walk. Successively delete an immediate reversal \((a,b,a)\), shortening the walk by two edges. A nonempty reduced closed walk cannot have length below \(g\): otherwise a repeated-vertex decomposition contains a simple cycle of length below \(g\). Reduction preserves oddness, so the terminal length is \(g\) or \(m=g+2\). The reduced walk in either case is a simple cycle: if a reduced closed walk of length at most \(g+2\) repeats an interior vertex, splitting at that repetition produces two positive closed subwalks. After removal of any backtracks, their total length forces either a simple cycle of length below \(g\) or two cycles of total length at least \(2g>g+2\). Thus the original walk is either an injective traversal of a simple \(m\)-cycle or a traversal of a simple \(g\)-cycle with one inserted immediate reversal. In the latter case, the cyclically reduced oriented \(g\)-cycle is uniquely determined; two adjacent possible erasures of a zigzag give the same cyclically reduced oriented cycle.

**Isolation of long cycles and rigidity of cells.** In a simple graph with no triangle or quadrilateral, two distinct vertices have at most one common neighbor. For an injective \(m\)-cycle walk, changing a single source coordinate would require a second common neighbor of its two target neighbors. Those two target neighbors already have the old intermediate vertex, hence a change would make a quadrilateral. All such walks are isolated Hom vertices. There are \(2m\) indexed directed traversals for every unoriented simple \(m\)-cycle.

For all other walks, there is exactly one reversal and thus one reduced oriented \(g\)-cycle. A nontrivial Hom cell can have only one variable source coordinate: two nonadjacent variable coordinates would produce two disjoint immediate reversals and reduce an odd closed walk to length \(m-4=g-2\), impossible by girth; two adjacent variables would entail a complete bipartite \(K_{2,2}\) subgraph, also impossible. Consequently, every nontrivial cell is a simplex supported at one coordinate. Changing its value preserves the reduced oriented \(g\)-cycle, so different oriented \(g\)-cycles cannot lie in the same Hom component.

**Collapse onto the cycle source/target subcomplex.** Fix a reduced oriented \(g\)-cycle \(Q\subseteq H\). At the unique reversal of a walk with core \(Q\), the neighbors in the source walk of the reversal apex both map to one vertex \(a\in Q\). Holding all other coordinates fixed gives a maximal simplex whose vertices are the allowed replacements from \(N_H(a)\). Exactly two of those replacements, the predecessor and successor of \(a\) on \(Q\), belong to the subcomplex \(\operatorname{Hom}(C_m,Q)\). Every other replacement is outside \(Q\). Such an outside neighbor belongs to only one vertex of \(Q\): attachment to two would produce a cycle of length at most \((g-1)/2+2<g\). Hence each off-cycle walk occurs in just this simplex and no other maximal simplex. Each simplex with off-cycle vertices therefore admits an elementary simplicial collapse relative to its edge joining the two cycle neighbors. Collapsing all these distinct free attachments leaves precisely the oriented-core component of \(\operatorname{Hom}(C_m,Q)\).

**The residual polygon.** A length-\(g+2\) closed walk into the cycle \(C_g\) must have winding number \(+1\) or \(-1\). For a given winding sign it has exactly one step against that sign. There are \(m\) choices for the step and \(g\) choices for an initial target vertex, giving \(gm\) vertices. Every vertex has two allowable single-coordinate recolorings; these move the unique contrary step by one position. Moving the step all the way around changes the initial value by two modulo \(g\). Because \(g\) is odd, this move visits every initial value, proving that the resulting 2-regular complex is one cycle on \(gm\) vertices. There are two winding signs, hence two disjoint circles per unoriented simple \(g\)-cycle.

Combining the long-cycle isolated vertices and the short-cycle polygons proves the classification. The collapses show integral torsion-freeness and exclude higher homology.

## Verification

The accompanying `checks/hom_cycle_verifier.py` uses only the Python standard library. Run `python checks/hom_cycle_verifier.py`; it enumerates every closed-walk homomorphism and every single-coordinate cell, checks absence of simultaneous independent coordinate variation, constructs connected components and checks their Euler characteristics against cycle counts. Tested cases include the Petersen graph (24 circles, no isolates), a pentagon joined to a heptagon by a bridge (two circles, fourteen isolates), a pentagon and heptagon sharing one vertex (two circles, fourteen isolates), and cycle and branch examples. The finite checks support, but do not replace, the argument for all \(g\) and \(H\).

## Relationship to prior work

Čukić–Kozlov determine the Hom complexes between two cycle graphs, including the two length-\(g(g+2)\) winding polygons for \(\operatorname{Hom}(C_{g+2},C_g)\); those polygons are a known ingredient and are not presented as new. Matsushita's Theorem 5.8 and Corollary 5.9 determine that a component with nonbipartite source and square-free target is homotopy equivalent to a point or a circle, but do not give the global cycle-count formula above. Fujii–Kimura–Nozaki give a more general componentwise algorithm for square-free codomains; the full manuscript was not accessible during comparison. The precise global count and explicit high-girth collapse are the asserted refinement, not the qualitative point/circle dichotomy.

## Limitations

The result requires the source to be precisely two longer than an odd girth lower bound and does not treat source odd lengths beyond this first one-reversal regime. It does not establish that this exact global formula is absent from inaccessible or unindexed literature, and it is not an independently audited result. Full-text inspection of Fujii–Kimura–Nozaki was unavailable; this is a material originality risk. Finite tests are not universal proof.

## References

- S. Čukić and D. Kozlov, *The homotopy type of complexes of graph homomorphisms between cycles*, Discrete & Computational Geometry 36 (2006), arXiv:math/0408015. https://arxiv.org/abs/math/0408015
- T. Matsushita, *Hom complexes of graphs whose codomains are square-free*, Journal of Combinatorial Theory B 178 (2026), 267–293, first public 2024-12-26, arXiv:2412.19144. https://arxiv.org/abs/2412.19144
- S. Fujii, K. Kimura, and Y. Nozaki, *Homotopy types of Hom complexes of graph homomorphisms whose codomains are square-free*, European Journal of Combinatorics 131 (2026), first public 2024-12-26, arXiv:2412.19039. https://arxiv.org/abs/2412.19039
