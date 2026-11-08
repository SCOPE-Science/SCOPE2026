# Independent mathematical audit

## correctness

PASS

For W_(q,k)=(0..q−1)^k, 1<=m<=qk, an embedding of word u corresponds uniquely to block indices j_i in [0,k−1] with j_(i+1)−j_i>=1 if u_i>=u_(i+1), otherwise >=0. Inserting m+1 nonnegative slack variables summing k−1−d(u) gives E=binom(k+m−1−d(u),m) if d<=k−1, else zero. Cutting words into strictly increasing blocks and a double-counting generating-function transformation gives weak-descent frequency N_q(m,d)=sum_i (−1)^i binom(m+1,i) binom(q(d+1−i),m), generating function ((1+(1−t)x)^q−1)/(1−t(1+(1−t)x)^q). Bounded length-<=q increasing segments construct each d from floor((m−1)/q) to m−1. Strict binomial monotonicity gives all distinct positive multiplicities and their frequencies; normalization sum N_q E=binom(qk,m) follows from counting position subsets. Independent brute enumeration checked 13645 word/multiplicity comparisons over q2..4,k1..3,m<=6, including repeat letters and boundary cases.

## originality

PASS

Specific complete all-parameter histogram of positional embedding counts (and uniform deletion-output probabilities) for complete repeated alphabet permutation host; classical generalized-Eulerian numbers used without claiming their individual novelty. Flaxman–Harrow–Sorkin count distinct subsequences only (support), and Kosche et al absent subsequences; neither support result determines multiplicities. Word-binomial and P-partition literature remain real possible hidden prior specializations.

## value

PASS

Full output-probability spectrum under uniform-position deletion from a canonical periodic source is a natural and strictly finer invariant than output support. Complete exact frequencies and feasible range for every (q,k,m) can be used without a downstream theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
