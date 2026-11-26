# Independent mathematical audit

## correctness

PASS

Below order four the type multiplicities are impossible. At order four both colors have size two. Each mover must have positive utility after a profitable swap, so both stayers gain the other swap vertex as a same-color neighbor. Each had at most one same-color neighbor before, so neither stayers nor movers can lose satisfaction. For order five an independent structural check gives the full classification. Write A={i,a}, B={j,b,c} and swap i and j. Profitability of A forces edge ja, so the A stayer a cannot lose satisfaction. The B stayer that loses satisfaction, say b, must have jb present and ib absent. Profitability of B requires a positive new numerator, so ic is present. Write p=1{ij is an edge}, s=|N(j)∩{b,c}|≥1. If ia were present, B's new utility would be 1/(2+p) and its old utility s/(1+p+s), at least as large. Thus ia is absent. Now b is the only possible loser: c cannot lose a same-type neighbor overall and the movers strictly improve. There can be no gains in the headcount. To keep a unsatisfied requires both ab and ac. B reaches utility 1/(1+p) at i, hence must already have been satisfied, requiring s≥1+p. If p=1 this forces s=2 and contradicts strict improvement, so p=0. A starts at zero and reaches 1/(1+s); to remain unsatisfied requires s=2. These force all edges except bc, which is optional. Conversely both choices of bc give a loss: b goes from (1+1{bc})/(2+1{bc}) to 1{bc}/(2+1{bc}), c's utility is unchanged, and the movers gain from 0 to 1/3 and from 2/3 to 1. The six-edge and seven-edge graphs are thus both attained and nonisomorphic. The frozen six-edge vectors also give H:2→1, utility sum 3/2→2 and the claimed threshold interval. A separately written complete census checked all labeled graphs, colorings and unlike swaps using integer inequalities and permutation isomorphism. It found 38 and 728 labeled connected graphs, 6 and 21 connected classes, and respectively 0 and 2 positive classes at orders four and five. This exhausts only these finite orders. The frozen certificate was inspected, not executed; its replay entry point is python3 verify.py in the frozen package.

## originality

PASS

The distinct claim supported by the comparison is the exact first order and the two connected topologies for loss of the external half-satisfied headcount under strictly fraction-improving bilateral swaps. The closest model papers use the same incentives but different aggregates, or related aggregates with a different move rule. No equivalent one-swap minimum or dominating classification was verified in the targeted comparisons. This does not establish global priority.

## value

PASS

The half-satisfied headcount is a natural assessment distinct from both individual preferences and aggregate utility. The result gives a sharp negative answer to its one-move monotonicity, including a witness where total utility actually rises. The order five cutoff is forced by the property rather than chosen arbitrarily, and the full minimal topology classification supplies reproducible minimal test graphs for work on segregation and swap dynamics. Larger-order or other-tolerance theorems are not needed for this finite claim to be useful.

The dated certificate retains the supplied scientific assessment, sources and limitations.
