# Independent mathematical audit

## correctness

PASS

Let C be the n original core vertices of W(G), each with private leaf v′. A paired-dominating set must contain every core vertex: otherwise v′ must be selected to dominate itself but has no selected neighbor for a perfect matching. Conversely every set containing all core vertices dominates. Such a set is uniquely C∪L′, with U=C\L. Each selected leaf forces its core partner into the perfect matching, so W(G)[C∪L′] admits a perfect matching exactly when G[U] does. Its cardinality is 2n-|U|, proving the entire paired-domination set polynomial. The weighted matching polynomial z^n M_G(z) counts perfect matchings of G[U], not merely supports; coefficientwise inequality follows from p_G(U)>=1_{p_G(U)>0}. Equality iff each induced subgraph has <=1 perfect matching. Two perfect matchings differ by alternating even cycles; every even cycle (even if not induced) supplies two matchings on its exact vertex subset. For a forest, permutation expansion of det(zI-iA) permits only fixed points and edge transpositions and equals M_F(z). The spectral, root-location, and minimum-degree consequences follow. Independently enumerated every core graph of order n<=4 and all selected subsets of their whiskered graphs; derived full polynomials and support-vs-multiplicity inequalities from separately coded perfect-matching recursion. C4 gives strict z^4 coefficient 1 against matching coefficient 2.

## originality

PASS

Dettlaff–Raczek–Yero Lemma 3.2 already relates a CORONA minimum paired-domination number to a maximum matching; it does not give the complete paired-domination polynomial, exact even-cycle equality criterion, or forest adjacency-spectrum determinant. Xu's survey states the paired-domination definition and original 1998 reference without the claimed enumerator. The 2016 abstract titled Introduction to Paired Domination Polynomial of a Graph is directly related, but full text was inaccessible: the abstract alone cannot support an assertion that the complete paper does not cover this theorem; retain this as a material priority risk. Published complete-multipartite and chain-graph paired-domination polynomials concern different graph families; there is no inspected reduction that makes the fully whiskered arbitrary-G all-cardinality identity a corollary.

## value

PASS

The paired-domination generating polynomial is a natural complete invariant that distinguishes the number of sets at every size, not only the preknown minimum. The matching-support map and sharp even-cycle obstruction yield a broad structural criterion for ALL core graphs. For forests, the determinant relation transports roots and adjacency-spectrum information into domination enumeration. These are motivated, reusable structural facts despite the elementary counting argument.

The dated certificate retains the supplied scientific assessment, sources and limitations.
