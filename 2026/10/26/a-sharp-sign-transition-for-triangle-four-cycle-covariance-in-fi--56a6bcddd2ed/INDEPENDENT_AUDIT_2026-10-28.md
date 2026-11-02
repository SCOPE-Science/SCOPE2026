# Independent mathematical audit

## correctness

PASS

For uniform G(n,m) with M=binom(n,2), a fixed j-edge event has probability h_j=(m)_j/(M)_j (interpreted as zero if j>m). Fix a non-induced unoriented 4-cycle. Exactly 4 triangles share 2 cycle edges, exactly 4(n−4) share 1, and the remainder share 0; the exact covariance is 3 binom(n,4){binom(n,3)(h_7−h_3h_4)+4(n−4)(h_6−h_7)+4(h_5−h_7)}. For n=4 the h7 terms cancel before evaluation. Independently factorized it symbolically to the claimed rational expression 4(m)_4(M−m)(M−m−1)[m(n²−2n−7)−4(n²−n−4)]/[(n+1)²(n+2)(n+3)(M−5)(M−4)(M−2)²]; denominators positive n>=4. The sign changes at tau_n=4(n²−n−4)/(n²−2n−7), giving the stated exceptional small-n ranges, zero at (5,8), and a universal m=4 negative to m=5 positive transition for n>=9. Independently exhaustively enumerated all 64+1024+32768=33856 labeled simple graphs for n=4,5,6 and every m-layer using separately generated triangle/cycle masks; all exact covariance values match. These finite checks supplement the exact combinatorial proof.

## originality

PASS

Best-of-knowledge PASS with a clearly delimited priority risk: the elementary overlap method for mixed subgraph moments is classical, but inspected papers on triangle tails, subcritical graph-class statistics, prescribed subgraph avoidance and univariate local limits do not furnish the all-n, all-m factored triangle/C4 covariance or full integer sign boundary. A broad classical motif moment formula might imply this with additional algebra; searches are not novelty proof.

## value

PASS

Conditional dependence of two canonical motifs in the fixed-edge random-graph null model changes sign, unlike nonnegative covariance from shared edges in independent-edge G(n,p). The exact threshold (especially m=4 versus 5 for all n>=9) and complete finite boundary make a natural, reusable mixed-invariant classification, not an arbitrary small instance or restatement of marginal motif statistics.

The dated certificate retains the supplied scientific assessment, sources and limitations.
