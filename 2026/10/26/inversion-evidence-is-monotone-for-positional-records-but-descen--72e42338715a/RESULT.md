# Inversion evidence is monotone for positional records, but descent evidence first reverses at eight symbols

## Finding
For a uniformly random permutation \(\Pi\in S_n\), let \(I\) count inversions and \(D\) count ordinary descents. At position \(j\), the event \(R_j=1\) means that \(\Pi(j)\) exceeds all preceding values. For every \(n\ge2\) and \(2\le j\le n\), the conditional probability \(\Pr(R_j=1\mid I=k)\) is nonincreasing in the feasible inversion count \(k\). In contrast, conditioning on descents does not always have this monotonicity: among all orders \(2\le n\le8\), the first and sole adjacent increase occurs for \(n=8\), position \(j=5\), between five and six descents:

\[\Pr(R_5=1\mid D=5)=\frac{596}{4293}<\frac{35}{247}=\Pr(R_5=1\mid D=6).\]

The increase is exactly \(3043/1060371\). This sharp, finite boundary separates two natural permutation disorder statistics with respect to evidence about a fixed positional record.

## Assumptions and scope
Every permutation of \(\{1,\ldots,n\}\) is equally likely. Positions are one-indexed. An inversion is a pair of positions \(a<b\) with \(\Pi(a)>\Pi(b)\), while a descent is an adjacent inversion \(\Pi(a)>\Pi(a+1)\). The first position is automatically a record; the theorem concerns \(j\ge2\). A conditional probability is compared only where its conditioning event has positive probability. All adjacent descent levels \(d,d+1\) with \(0\le d<n-1\) are positive-probability events.

## Proof
**Inversion monotonicity.** For each position \(\ell\), let \(U_\ell=\#\{a<\ell:\Pi(a)>\Pi(\ell)\}\). Under the uniform permutation law these inversion-sequence variables are mutually independent, and \(U_\ell\) is uniform on \(\{0,\ldots,\ell-1\}\). This is a bijective permutation encoding: at the \(\ell\)-th insertion, the rank of the new value among the first \(\ell\) is uniformly distributed, and independent insertions produce every permutation exactly once. Consequently, \(I=\sum_{\ell=1}^n U_\ell\), while \(R_j=1\) exactly when \(U_j=0\).

Put \(S=\sum_{\ell\ne j} U_\ell\) and \(f(k)=\Pr(S=k)\), extending \(f\) by zero off its finite integer support. Convolution preserves nonnegative log-concavity with no internal zeros; each discrete uniform mass function has these properties, so \(f\) is log-concave on its support. Independence gives the exact identity

\[\Pr(R_j=1\mid I=k)=\frac{f(k)}{\sum_{t=0}^{j-1} f(k-t)}.\]

For each positive integer \(t\), log-concavity makes the ratio \(f(k-t)/f(k)\) nondecreasing in \(k\) whenever both entries are positive: factor the ratio into \(t\) successive terms \(f(s-1)/f(s)\), each nondecreasing in \(s\). At the support boundaries this ratio is interpreted as zero or infinity according to which term vanishes; the posterior formula has the corresponding limits. Hence \(1+\sum_{t=1}^{j-1} f(k-t)/f(k)\) is nondecreasing, and its reciprocal is nonincreasing. This proves the all-order statement. The endpoint case \(S\) degenerate is immediate from the displayed ratio.

**Sharp descent boundary.** For every permutation of sizes \(n=2,\ldots,8\), calculate its descent count and its indicator at each position. Let \(A_n(d)\) be the number of permutations with exactly \(d\) descents, and let \(B_{n,j}(d)\) count those also having a record at position \(j\). Then

\[\Pr(R_j=1\mid D=d)=\frac{B_{n,j}(d)}{A_n(d)},\]

and an adjacent increase occurs exactly if \(B_{n,j}(d+1)A_n(d)-B_{n,j}(d)A_n(d+1)>0\). Exact enumeration with the included standalone Python program checks this integer inequality for every \(2\le n\le8\), \(2\le j\le n\), and \(0\le d<n-2\). The program independently rederives all cells using subset dynamic programming, with states recording the used-value set, previous value, descents and the target record flag. Both methods agree on every count.

For \(n=8\), the full Eulerian total row \((A_8(d))_{d=0}^{7}\) is \((1,247,4293,15619,15619,4293,247,1)\). At \(j=5\), the marked row \((B_{8,5}(d))_{d=0}^{7}\) is \((1,100,1201,3336,2795,596,35,0)\). The sole positive difference is at \(d=5\): \(35\cdot4293-596\cdot247=3043>0\). All smaller orders have no positive difference. Since every object in a finite permutation set appears exactly once in each exhaustive enumeration and the independent subset recurrence agrees on all cells, this certifies the claimed sharp finite boundary.

## Verification
Run \(\texttt{python verify.py}\) using Python 3. The script has no nonstandard dependencies, enumerates all permutations through order eight (\(8!=40320\)), independently computes the same marked descent tables by a subset dynamic program, and asserts exact agreement. It checks that the complete list of adjacent conditional increases through order eight consists of the stated single instance and prints the exact fractions. This finite computation supports the finite boundary; the all-order inversion monotonicity is proved above, not inferred from enumeration.

## Relationship to prior work
Baril and Petrossian, *Equivalence classes of permutations modulo descents and left-to-right maxima* (2015), analyze equivalence classes defined by descents and records. Their full accessible text develops these equivalence relations and their enumerations, not fixed-position record posteriors conditioned on a prescribed total number of descents or the sharp order-eight monotonicity boundary. Classical Eulerian distributions supply \(A_n(d)\), but not by themselves the marked numerator \(B_{n,j}(d)\). Earlier work by Katzenbeisser treats the joint distribution of the total number of records with inversions; the present all-order statement concerns a **specified position**, while the descent counterexample concerns a different statistic. Later work of Jin treats joint Euler–Stirling distributions of aggregate statistics, but the local marked conditional comparison was not identified in the materials examined. These are implication comparisons, not claims of exhaustive historical priority.

## Limitations
The descent assertion proves a sharp first failure through order eight, not a classification for all larger orders. The theorem assumes uniform permutations; for Mallows permutations, conditioning on a fixed inversion count still yields the same conditional posterior, but no unrestricted nonuniform sampling theorem is claimed. The log-concavity argument establishes weak, not universal strict, monotonicity. A relevant earlier joint-record paper was not available in full text; precise historical priority remains subject to independent comparison. No independent scientific audit has been conducted.

## References
1. J.-L. Baril and A. Petrossian, *Equivalence classes of permutations modulo descents and left-to-right maxima*, Pure Mathematics and Applications 25 (2015), 19–29. DOI: 10.1515/puma-2015-0002. Author manuscript: https://jl.baril.u-bourgogne.fr/equivaldescentrevue.pdf. Author-hosted public copy documented by 2015-09-08.
2. W. Katzenbeisser, *On the joint distribution of the number of upper and lower records and the number of inversions in a random sequence*, Advances in Applied Probability 22 (1990), 957–960. DOI: 10.1017/S0001867800023211.
3. E. Y. Jin, *Symmetric generating functions and Euler–Stirling statistics on permutations*, arXiv:2210.08789 (2022), and Journal of Combinatorial Theory, Series A (2023).
