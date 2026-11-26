# Independent mathematical audit

## correctness

PASS

An ideal has a selected vertex set A and an edge set B⊆K(A). If F=K(A)∖B, the minimal complement consists of the vertices outside A and the edges F; its ideal has vertex set (V∖A)∪supp(F) and edge set F. To check eventual return to full vertex sets, write C=V∖A and T=supp(F). If each vertex in A lies in T, the next state is full. If C and T are nonempty and completion is still needed, the next missing edges include every C–T edge, so the second state is full. For T empty the first image is (C,∅), followed by a full state unless |C|=1; in that case (A,∅) is followed by a full state using n≥3. From a full state, an isolated vertex yields a complementary full state with a universal vertex. Full graphs with neither type are paired with their complements, and the complete graph belongs to the unique length-3 orbit. For a nonempty proper universal set X, the residual graph H on Y=V∖X has no universals and |Y|≥2. Reapplying the recurrence gives exact lengths 6 when H has no isolates, 8 when it has isolates and edges, 5 when H is empty and |X|=1, and 8 when H is empty and |X|≥2. In the eight-cycle with nonempty H, the full states four steps apart have different universal sets (X and the isolates of H); in the empty case they switch X and Y. Thus no period-four collapse occurs. Each six- or eight-cycle has two full states with universals; each five-cycle has one. Inclusion–exclusion for graphs without isolates, together with complementation and incompatibility of isolated and universal vertices, yields the stated a_m and b_m and the full census. The 3-, 5- and 8-cycles exist for n≥4, giving order 120; for n=3 only lengths 3 and 5 occur. A spanning cycle on n≥4 vertices has neither isolates nor universals, and the same construction on n−1≥4 vertices supplies the six-cycle. A fresh finite check used the minimal-complement definition directly, enumerating each ideal and following successors. Its complete counts for n=3,4,5,6 in the order (2,3,5,6,8) were (0,1,3,0,0), (9,1,4,0,9), (256,1,5,45,80), and (11065,1,6,1671,985), respectively.

## originality

PASS

The prior literature supplies the classical action, its toggle and antichain formulations, and the graph-incidence poset definition. The strongest indexed related exact results concern other families, with an exact n=3 overlap with the standard example. No inspected statement covers the remaining complete-graph incidence family, its uniform bound or its census. This comparison is limited to the inspected sources and does not certify historical priority.

## value

PASS

This is a natural Boolean rank selection and a complete exact invariant of its classical rowmotion. The uniform orbit bound of eight, despite the rapidly increasing set of ideals, exposes a structural restriction through the full-singleton return mechanism. The result gives exact multiplicities and resolves all exceptional sizes, not just a small-instance table or a constant-order estimate.

The dated certificate retains the supplied scientific assessment, sources and limitations.
