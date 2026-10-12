# Exact three-perfect-matching cover counts for bridgeless claw-free cubic graphs
## Finding
For a connected finite loopless bridgeless claw-free cubic multigraph \(G\), let \(\mathcal C_3(G)\) denote the set of unordered triples of perfect matchings whose union is \(E(G)\), and let \(c_3(X)\) denote the number of proper edge-colourings \(E(X)\to\{1,2,3\}\) with the three colours labelled.

Using the structural decomposition of bridgeless claw-free cubic graphs into \(K_4\), \(K_2^3\), rings of diamonds or 2-cycles, and type-(iii) graphs with a cubic core, the exact count is
\[
|\mathcal C_3(G)|=
\begin{cases}
1,&G\cong K_4\text{ or }G\cong K_2^3,\\
2^{q-1},&G\text{ is a ring of }q\ge2\text{ diamonds or 2-cycles},\\
2^q c_3(H)/6,&G\text{ is type (iii) with core }H,
\end{cases}
\]
where in the last line
\[
q=\sum_{e\in E(H)}\bigl(\ell(e)+r(e)\bigr)
\]
is the total number of diamond and 2-cycle units in all channels.

Consequently, a type-(iii) graph is coverable by three perfect matchings if and only if its core is 3-edge-colourable. If the core is simple and \(G\) is not coverable by three perfect matchings, then \(|V(G)|\ge30\); equality holds exactly for the graph obtained from the Petersen graph by replacing every vertex by a triangle and using no diamond or 2-cycle units.

## Assumptions and scope
Graphs are finite, connected, loopless, and may have parallel edges, matching the convention of the initiating paper. Cubic means degree three with multiplicity. A proper 3-edge-colouring assigns three labelled colours so that the three edges incident with every vertex receive distinct colours.

A diamond is \(K_4\) minus one edge, with the two degree-two vertices serving as terminals inside a channel. A 2-cycle is two parallel edges between two terminal vertices. In a type-(iii) graph, each core vertex is replaced by a triangle and each core edge is either left as a linking edge or replaced by a string of diamonds and 2-cycles. For a core edge \(e\), \(\ell(e)\) and \(r(e)\) count the two unit types.

The result concerns covers by exactly three perfect matchings. It does not decide whether a graph requiring more than three perfect matchings is coverable by four.

## Proof
First, in any cubic graph on \(n\) vertices, a perfect matching has \(n/2\) edges and the graph has \(3n/2\) edges. Thus three perfect matchings cover all edges if and only if they are pairwise edge-disjoint and partition \(E(G)\). Such a partition is the same object as a proper 3-edge-colouring after the three matchings are labelled. Therefore
\[
|\mathcal C_3(G)|=c_3(G)/6.
\]

The local transfer rules are exact.

For a triangle replacing a core vertex, prescribe the colours on its three external channel edges. A proper extension across the triangle exists if and only if those three external colours are pairwise distinct, and then the internal triangle colouring is unique: each internal edge receives the external colour at the opposite triangle vertex.

For a diamond, prescribe the colours on the two external linking edges at its terminals. A proper extension exists if and only if the two external colours agree. When they agree, the two remaining colours may be assigned to the two side edges at one terminal in either order, and the rest of the diamond is then forced. Hence there are exactly two extensions. The same statement holds for a 2-cycle: the two external colours must agree, and the two parallel edges may receive the remaining two colours in either order, again giving exactly two extensions.

It follows that every diamond or 2-cycle transports one edge colour unchanged from one end of its channel to the other and contributes an independent binary choice. Hence a channel with \(s\) units has exactly \(2^s\) extensions for each prescribed core-edge colour.

For a type-(iii) graph, contracting every replacement triangle conceptually recovers the core incidences. By the triangle rule, the three channel colours incident with every core vertex are pairwise distinct, so every proper 3-edge-colouring of \(G\) induces a proper 3-edge-colouring of \(H\). Conversely, every proper 3-edge-colouring of \(H\) extends uniquely over every replacement triangle and has exactly two independent extensions across every diamond or 2-cycle. Therefore
\[
c_3(G)=2^q c_3(H),
\]
and the asserted type-(iii) formula follows after division by six.

In a ring of \(q\ge2\) diamond or 2-cycle units, each unit forces the same colour on its two linking edges. Going around the ring therefore makes every linking edge carry one common colour, chosen in three ways, while every unit contributes an independent binary internal choice. Thus
\[
c_3(G)=3\cdot2^q
\quad\text{and hence}\quad
|\mathcal C_3(G)|=2^{q-1}.
\]
Finally, both \(K_4\) and \(K_2^3\) have exactly six labelled proper 3-edge-colourings, so each has one unordered three-perfect-matching cover.

For the cutoff, the initiating paper gives
\[
|V(G)|=3|V(H)|+4\sum_e\ell(e)+2\sum_e r(e).
\]
A classical census fact is that the Petersen graph is the smallest bridgeless simple cubic graph of chromatic index four; among the nineteen connected cubic graphs on ten vertices it is the only bridgeless one with chromatic index four. Therefore a simple bridgeless cubic core that is not 3-edge-colourable has at least ten vertices, with equality only for the Petersen graph. The displayed order formula now gives \(|V(G)|\ge30\), and equality forces a ten-vertex Petersen core together with no channel units.

## Verification
The analytic proof is local and does not depend on finite enumeration. The accompanying verifier independently enumerates all colour assignments for the triangle, diamond, and 2-cycle gadgets. It confirms that a triangle has one extension exactly for pairwise-distinct external colours, while a diamond or 2-cycle has two extensions exactly when its two external colours coincide.

As finite stress tests, the verifier counts six labelled 3-edge-colourings of \(K_4\), checks that a type-(iii) expansion of \(K_4\) containing one diamond and one 2-cycle has twenty-four labelled colourings, checks four small rings against \(3\cdot2^q\), and confirms that the Petersen graph has no proper 3-edge-colouring. It also constructs the thirty-vertex triangle truncation of the Petersen graph and checks cubicity. These computations support the local transfer argument but are not used as an infinite proof.

## Relationship to prior work
Zhou and Wang's 2026 preprint proves that every bridgeless claw-free cubic graph is coverable by five perfect matchings and develops the decomposition used here. Its Lemma 2.1 lists the three structural cases, and its Lemma 2.2 relates perfect matchings of a type-(iii) graph to parity subgraphs of the core. The paper explicitly observes that the exceptional graphs and rings are 3-edge-colourable, but its stated results concern five-cover existence and four-cover density rather than the exact number of three-perfect-matching covers.

Standard snark reductions note that contracting a triangle and reducing a 2-cycle preserve 3-edge-colourability, so the existence direction is related to familiar Tait-colouring reductions. The new statement tracked here is the exact multiplicity transfer through every diamond and 2-cycle, assembled with the Zhou--Wang decomposition into a closed count for all bridgeless claw-free cubic graphs and the resulting sharp simple-core order cutoff.

published-finding corpus searches for the exact transfer factor, three-perfect-matching-cover formulation, Petersen-truncation cutoff, Tait-colouring aliases, and triangle/diamond channel formulations returned no implication-equivalent result. The closest retrieved records concerned other colouring or Petersen-complex invariants and did not count proper 3-edge-colourings or three-perfect-matching covers of claw-free cubic graphs.

## Limitations
The cutoff statement is restricted to type-(iii) graphs whose core is simple; no claim is made here about the least obstruction when nonsimple cores are allowed. The theorem determines exactly the three-perfect-matching-cover layer, not the unresolved four-perfect-matching-cover problem. The originality assessment is necessarily literature-limited: older edge-colouring literature may contain the same multiplicative counting rule under Tait-colouring or graph-expansion terminology even though the targeted searches and inspected sources did not reveal it.

## References
1. H. Zhou and X. Wang, *Perfect matching covers of claw-free cubic graphs*, arXiv:2610.01137v1, first public 2026-10-01. https://arxiv.org/abs/2610.01137
2. D. A. Holton and J. Sheehan, *The Petersen Graph*, Cambridge University Press, 1993, Chapter 9, DOI: 10.1017/CBO9780511662058.010.
