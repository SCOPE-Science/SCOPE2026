# Independent mathematical audit

## correctness

PASS

The team split is equivalent to total vertex labels such that each edge's assigned color matches a label at one endpoint. A satisfying split supplies partial labels, completed arbitrarily because the alphabet is nonempty; conversely each edge can be assigned to a matching endpoint. Constant labels on each side solve the two-color case. In a tree or unicyclic component orient edges to have at most one incoming edge at each vertex; each vertex then labels its one incoming edge. For necessity, take a spanning tree plus two non-tree edges in a component with at least two cycles, and prune leaves. This gives a connected core of minimum degree two with E=V+1. The sum of degree excesses above two is two. Suppressing degree-two paths leaves either one degree-four vertex with two loops, or two degree-three vertices with either three joining edges or one joining edge and a loop at each end. On undoing suppression these are exactly the figure-eight, theta and joined disjoint cycles. For each subcubic core, König's bipartite edge-coloring theorem supplies a proper three-coloring; each vertex can then cover at most one edge, fewer total than required. In the figure-eight, give the two incidences of each cycle at the shared vertex the same color, distinct across cycles. Alternate the two other colors along each remaining path, so each noncentral vertex sees distinct colors. Every cycle must use the shared vertex to cover an edge, but no single label can cover edges of both cycles. Extending the falsifying coloring preserves failure. Checking E≤V for each connected component takes linear time and includes isolated vertices. The checker was inspected, not run. It stops at the first falsifier on each nonrobust support, so it correctly tests the universal condition but the wording that it tests every coloring even on those supports is too strong.

## originality

PASS

The uncolored pseudoforest criterion and the same formula on a single given team are prior. Fröhlich–Kolaitis–Meier also already give three-color witnesses on a particular family of chorded even cycles. Their results, combined with proper edge coloring, account for the unbounded-palette implication and the subcubic obstructions. The distinct supported result is the sharp palette threshold for arbitrary finite bipartite supports: a three-color obstruction also exists on every figure-eight, where degree four prevents a proper three-edge-coloring, and two colors are always coverable. The closest matched catalogue record gives an exact three-color census and deletion distances on K_{2,n}, not the arbitrary-support threshold. Its same-day date gives no order or priority determination.

## value

PASS

For an established dependence formula whose individual-team model checking has already been studied, asking whether an unlabeled support guarantees all teams work is a distinct, naturally motivated question. The sharp jump from universal acceptance at two colors to a linear-time structural classification at three identifies the least usable counterexample alphabet, including the only bicyclic core not covered by the direct proper-edge-coloring argument.

The dated certificate retains the supplied scientific assessment, sources and limitations.
