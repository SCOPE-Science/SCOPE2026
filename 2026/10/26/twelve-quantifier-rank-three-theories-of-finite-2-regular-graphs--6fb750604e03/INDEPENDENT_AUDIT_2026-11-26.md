# Independent mathematical audit

## correctness

PASS

For a named ordered pair x,y, equality and adjacency together with the realized adjacency patterns of a third distinct vertex are the full one-round extension data (repeated choices are forced). Taking first the set of pair data at each root and then the set of rooted types gives precisely three-round equivalence. Independently, for every graph of order at least 7, a third distinct vertex with pattern (0,0) always exists: the union of x,y and their neighbors has size at most 6. For distinct x,y and j common neighbors, the (1,1) pattern occurs iff j>0, and both exclusive patterns occur iff 2-E(x,y)-j>0. At every root there is a nonadjacent second vertex with j=0 (use another component, or distance 3 in the sole cycle), and the root's adjacent type and possible extra nonadjacent type are determined by whether its component is C3, C4, or C_n with n>=5. Thus the set of rooted types is determined by the nonempty set of these three categories. All seven sets occur with order at least 7; in that range I is true (sum of floor(n/2) at least order/3), while D and U are false. The only smaller nonempty graphs are C3, C4, C5, C6, and two C3s, giving five different signatures, each with D true. Here 'exactly one/two triangles' in the table describes the entire graph in those rows. T,Q,F are respectively the three category tests, and all six formulas have rank at most three. This proves correctness even without the cycle citation or enumeration. I inspected checker.py, game_crosscheck.py and enumeration.txt without executing the packaged scripts. Independent replay: python3 /workspace/replay_rank_three.py constructs full atomic triple diagrams including repetitions and computes both partitions on all 1023 reduced cases; it matches the twelve populations in enumeration.txt. The replay checks the finite cases only; the rooted-type argument above handles arbitrary sizes.

## originality

PASS

Best-of-knowledge pass for the evaluated rank-three equivalence classes and explicit signature on all nonempty finite undirected 2-regular graphs, not for the connected-cycle cutoff, the EF recurrence, or disjoint-sum composition. Neither the finer unrestricted-depth finite-variable classification nor the directed rank-three catalogue determines this exact quotient as a stated or immediate specialization.

## value

PASS

The rank-three boundary is natural: it detects triangle, true square-twin and longer-cycle common-neighbor behavior yet collapses arbitrarily many and long components. The result gives the complete expressive-power quotient, says exactly where small size still matters, and lets a researcher decide indistinguishability or exhibit a separating formula for any pair of finite 2-factors without playing a game on those inputs. This is more than extending the connected cutoff by a parameter substitution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
