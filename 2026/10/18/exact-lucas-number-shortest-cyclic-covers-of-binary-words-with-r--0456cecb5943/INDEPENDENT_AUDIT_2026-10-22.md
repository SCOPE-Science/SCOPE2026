# Independent mathematical audit

## correctness

PASS

For k>=3, the required length-k words are precisely binary words avoiding 000 and 111. In the de Bruijn graph on length-(k-1) vertices, vertices beginning unequal and ending equal have one more incoming than outgoing required edge; the complementary class has the opposite imbalance. For a deficit v, its first equal adjacent pair at position t(v) proves every path in the unrestricted host graph to any surplus has length at least t(v). Subtracting required edges from any cyclic cover leaves a nonnegative flow whose source-to-sink path decomposition gives the lower bound sum t(v). The explicit map from each deficit to a surplus using its first/last equal pair is bijective, realizes each lower bound with a run-two path, and balances the multigraph. Strong connectivity yields an Eulerian cycle. Counting admissible suffixes gives overhead 2(F_(k-1)-1), hence total length 2L_k-2. The inspected verifier checks the construction and finite small cases; the infinite statement follows from the proof, not those tests.

## originality

PASS

The full Moreno–Matamala arXiv paper was inspected through its restricted-language definitions and Section 3. It studies exact-once de Bruijn cycles in restricted languages and the conditions for a greedy minimal walk to be Eulerian. The present required-edge graph is unbalanced for k>=4, so no exact-once restricted de Bruijn cycle exists; the claim instead minimizes a repeat-allowing cover and proves the extra multiplicity cost. The full Chen–Sima–Milenkovic paper's Kautz section was inspected: it defines Kautz cycles and studies orthogonal collections, not shortest repeat-allowing hosts. Resultary's nearest hits were unrelated Fibonacci/word problems. A 2004 conference version and the 2008 universal-cycle paper remain incompletely inspected, but inaccessible plausible literature alone does not fail O; the specific comparison remains a residual risk.

## value

PASS

The exact minimum periodic test length for all binary windows avoiding both constant triples is a natural constrained-coding invariant. The required graph is unbalanced, so repeat overhead is nontrivial; the first/last-equal-pair bijection gives a simultaneous optimal path assignment and a forbidden-free host, with a closed Lucas formula and limiting relative overhead. This is not a known-table recomputation or arbitrary parameter slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
