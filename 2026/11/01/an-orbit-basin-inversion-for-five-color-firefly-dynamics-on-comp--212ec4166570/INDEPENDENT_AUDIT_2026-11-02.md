# Independent mathematical audit

## correctness

PASS

Any vertex’s color update depends only on its own color and whether blink color 2 appears in the opposite shore, yielding a deterministic factor on (2⁵−1)²=961 pairs of occupied color supports, independent of a,b. Within a shore equal colors never separate; support sizes cannot grow, hence periodic support cycles induce bijective color permutations. After q support steps the monodromy has order L, so a labelled microstate on that cycle has exact least period qL, and first periodic-entry time equals the support entry depth. Independent reimplementation of all 961 mask transitions, cycle search, color-permutation monodromy, and transients reproduced exactly 16 support cycles, 49 recurrent supports, seven cycle types of least period 5, seven of 6, two of 18; maximum entry depth 25 at support pair (1,31). The exact independent basin-six coefficient matrix is [[0,0,0,0,0],[0,30,28,5,0],[0,28,20,12,1],[0,5,12,3,1],[0,0,1,1,0]], and the six supports entering 18-cycles are already periodic. Summing the finite support factors with A_j(n)=number of surjections onto j colors yields all closed N_p and B_p formulas. Leading support-size terms yield N18∼12^n/3, N6∼9^n/3, N5∼(2/5)10^n, whereas almost every initial configuration has full support on each shore, depth exactly 8 and period 5. The finite enumeration is mathematically exhaustive for the proved 961-state factor; microscopic finite examples are auxiliary.

## originality

PASS

Lyu’s original firefly model and tree synchronization theorems do not include a complete orbit/basin census on all K_{a,b}. A related published complete-tripartite period-18 construction requires three nonempty shores and may share a special numeric factor; it does not determine bipartite period-5/6 cycles, 961-state basin coefficients or max transient 25. Related Resultary automata entries cover different update rules. Claim is qualified original after checking actual implications.

## value

PASS

The finite quotient is exact for an infinite natural graph family, and determines genuine orbit counts, basin sizes and sharp universal entry time; the asymptotic reversal between uniform choice of a periodic orbit and of an initial condition is a substantive new dynamical phenomenon, not simply a computed small graph.

The dated certificate retains the supplied scientific assessment, sources and limitations.
