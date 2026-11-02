# Scientific review

## Correctness — PASS

**Claim and quantifiers.** For every pair of nonnegative integers \(m,n\), the formal bivariate exponential generating function determines the induced-forest polynomial of the labeled rook graph \(K_m\square K_n\), with empty-shore terms treated as singleton components. For every \(2\leq m\leq n\), the claimed degree and leading coefficients cover the balanced and unbalanced cases separately.

**Proof reconstruction.** The map from a rook cell to an edge of \(K_{m,n}\) is a graph isomorphism onto the line graph. A line graph is acyclic exactly when the original graph is a disjoint union of paths and isolated vertices: vertices of degree three create triangles and cycles remain cycles. For each alternating path component, factorial labeling and reversal produce the two exact connected-component weights. The exponential formula is applicable to a set of labeled components and counts every permitted edge set once. Extremal forests meet the degree bound on the smaller shore; the square case forces an alternating Hamiltonian path, whereas the rectangular case suppresses every smaller-shore vertex to produce a unique labeled path forest. The displayed binomial sum follows by exact coefficient extraction from the path-component exponential generating function. Every step is algebraic or bijective and works for the asserted infinite parameter range.

**Checks and limitations.** Native rook-adjacency union-find enumerations, a separate labeled-component recursion, and exact rational expansion of the proposed exponential generating function agree on all tested coefficients. The standalone script checks 14 parameter pairs and eight generating-function expansions; it is finite corroboration and is not used as an infinite certificate.

## Originality — PASS, with residual literature uncertainty

The closest first-hand source is Barton–Brown–Pike, *Acyclic polynomials of graphs*, arXiv:2011.01735, first public November 3, 2020. Its open-access full text defines exactly the vertex-induced-forest polynomial and studies roots, general properties, and selected graph families. Its lexicographic-product result is not a Cartesian-product identity and does not imply the two-parameter rook polynomial. The paper's direct terminology creates the substantive motivation and permits direct comparison of definitions. The older decycling literature treats minima; the rook-graph minimum cardinality appears in existing invariant tables, and it is explicitly not claimed as novel here.

Alternate descriptions were searched: induced-forest or forest polynomial of rook/Hamming graphs, line-graph acyclicity, bipartite linear-forest enumerators, feedback-vertex-set multiplicities, and existing graph-polynomial formulae. None of the inspected sources states this whole coefficient enumeration or its leading-coefficient count. Searches can miss differently indexed work; a general published formula for bipartite labeled linear forests would subsume the present identity. This is the explicit remaining publication-priority risk, not proof of absolute novelty.

## Mathematical value — PASS

The acyclic polynomial is a natural invariant motivated by induced-forest optimization and feedback vertex sets. The result determines **every** induced-forest coefficient for all rectangle dimensions, not merely the already known maximum cardinality. Its extremal coefficients count **all minimum feedback vertex sets**, with a structural transition between the balanced Hamiltonian-path case and the unbalanced right-shore path-forest case. The precise factorial and binomial multiplicities can inform enumeration, sampling, and extremal studies of these line graphs. The complete two-parameter classification, rational bivariate exponential form, and phase-dependent optimum multiplicities constitute a motivated exact counting result rather than an arbitrary finite example or routine repetition of a known scalar minimum.

## Closest sources and residual risks

Barton–Brown–Pike (2020/2022) provides the same graph-polynomial definition but not the rook-graph coefficients; Bau–Beineke (2002/2007) concerns scalar decycling bounds and other Cartesian products; the MathWorld feedback-vertex-set table already gives the rook minimum. The ordinary matching polynomial was historically also called an acyclic polynomial; it is a different invariant and does not cover the present claim. Publication-priority comparison remains limited to discoverable and materially inspected sources. No independent mathematical validation has been performed.

Self-review: passed. Independent audit: not yet performed.
