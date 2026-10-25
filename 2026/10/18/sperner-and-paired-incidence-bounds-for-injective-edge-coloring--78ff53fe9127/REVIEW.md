# Independent mathematical audit

## correctness

PASS

An edge of S(G) incident at an original vertex corresponds to a directed arc u→v. The injective edge constraint is equivalent to forbidding repeated color on consecutive arcs u→v→w with three distinct original vertices. For an arbitrary proper q-vertex-colouring of G, map colors to q different equal-sized subsets of [t], t=L(q), and color u→v by any coordinate in A(u)\A(v); two consecutive directed arcs draw from disjoint coordinate differences. For S(K_n), duplicate every middle-layer word of length t−1 in a matched pair; pair arcs use color t, which cannot appear twice consecutively since matched edges are disjoint, and interpair arcs use the earlier differences. For the lower bound, each one-colour directed digraph without directed two-paths on three vertices is a union of oriented source/sink bipartite pieces and isolated reciprocated pairs, so its underlying graph is bipartite. Bipartition membership across t monochromatic subgraphs gives a proper 2^t vertex colouring of G. Hence ceil(log2 q)≤χ′inj≤L(q), and central binomial asymptotics give ratio→1 and half-loglog additive correction. All t≥2 and n bounds remain explicit; no exact finite optimum is claimed.

## originality

PASS

Bradshaw–Clow–Xu 2023 Proposition 2.5 supplies the same lower bound log₂χ(G), and their immediately following text supplies upper 2⌈log₂χ(G)⌉. Those are explicitly recognized as prior art. The claimed middle-layer construction replaces a factor-two leading upper coefficient by one for every G, and paired incidence doubles finite clique code capacity using a matching-only special colour. The full Bradshaw article was read, and the improvement does not follow from the stated factor-two result. Priyamvada–Panda 2023/2024 directly treats injective edge coloring of subdivisions and claims tight upper bounds; its full text could not be retrieved via lawful open-access routes or authenticated Oxford because VPN was disconnected. That is a substantive risk, not an automatic O failure nor grounds to declare the complete paper noncovering. No independently established dominating implication was found.

## value

PASS

The prior uniform one-subdivision bound lies between one and twice log₂χ(G), a genuine leading-order structural gap. An explicit antichain assignment proves the optimal leading coefficient one for every sequence of graphs with growing chromatic number, sharply connecting a standard edge-colouring invariant to Sperner coding. The distinct paired construction supplies further finite capacity using a matching-specific colour with a clear mathematical reason. It is a broadly quantified natural extremal bound, not just a modest gain at twelve vertices.

The dated certificate retains the supplied scientific assessment, sources and limitations.
