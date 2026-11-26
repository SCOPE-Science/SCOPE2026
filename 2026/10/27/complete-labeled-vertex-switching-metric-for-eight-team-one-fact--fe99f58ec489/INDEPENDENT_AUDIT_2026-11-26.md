# Independent mathematical audit

## correctness

PASS

For anchors a,b, each other vertex is incident to two distinct factor nodes, and each non-anchor factor has one a-edge and one b-edge. Contracting factors gives the cycle components of z -> the partner of b in the factor containing az. Swapping a and b on one such cycle leaves one edge at both anchors in each affected factor and leaves all other vertices properly matched. It is an involution and preserves the cycle partition, so the excluded connected case cannot become an allowed reverse move. Full state canonicalization must retain vertex labels and erase only factor labels. My exact independent replay fixed the round order by the partner of vertex 0, used pairing recursion in each round, generated switches by permutation cycles, deduplicated targets, and obtained 6,240 states, 66,360 edges and the stated degree and cycle-signature counts. A separate alternating-cycle test identified exactly the 960 degree-14 states as perfect. Adjacent transpositions generate all of S_8, act by graph automorphisms and gave the same six orbit sizes; sparse unweighted shortest paths from each representative visited all states and reproduced all six distance vectors. Weighting representatives by orbit sizes gives eccentricity 5 for 5,790 states and 6 for 450, hence radius 5 and diameter 6 (private replay /workspace/branches/replay/switch.py and switch.txt). The matching checker was inspected; the coloring checker's VERIFY_OK does not by itself assert the printed profiles, but the matching computation and independent replay verify the full table.

## originality

PASS

Supported for the exact fixed-label single-component switch graph, with the historical move, class census and quotient data credited separately. The 960/14 comparison is between perfect states' lack of factor moves and their nonzero fixed-label vertex-switch degrees, not a new definition or a quotient claim.

## value

PASS

K8 is the small complete-graph case singled out by the established switch literature with a perfect class separated under factor switches. Fixing labels answers the different scheduling/reconfiguration question of how many actual moves are needed without renaming teams. The result proves all concrete schedules communicate within six moves, exactly quantifies access out of every otherwise factor-switch-frozen state, and identifies which labeled orbits attain the worst case. The six-class quotient does not determine this behavior.

The dated certificate retains the supplied scientific assessment, sources and limitations.
