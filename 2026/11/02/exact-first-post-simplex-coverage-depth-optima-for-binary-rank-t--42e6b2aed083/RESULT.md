# Exact first post-simplex coverage-depth optima for binary rank-three codes

## Finding
Let \(E_2(n,3)\) be the minimum expected number of independent uniform-with-replacement column draws needed to span \(\mathbb F_2^3\), minimized over all full-rank binary \(3\times n\) generator matrices. The exact first post-simplex replication window is

\[
\begin{array}{c|rrrrrr}
n&8&9&10&11&12&13\\\hline
E_2(n,3)&\frac{422}{105}&\frac{142}{35}&\frac{509}{126}&\frac{1439}{360}&\frac{615}{154}&\frac{7309}{1848}
\end{array}.
\]

There are precisely \(7,21,28,7,21,7\), respectively, optimizing nonzero-column multiplicity profiles on the seven specified nonzero vectors of \(\mathbb F_2^3\). All are equivalent under invertible row transformations, followed by column permutations.

In each optimum, all seven nonzero column types occur, each once or twice. Writing \(r=n-7\), exactly \(r\) types occur twice. For \(r=1,2,5,6\), every \(r\)-subset of the seven types gives an optimum. For \(r=3\), the three doubled types must be linearly independent (not a Fano line). For \(r=4\), the four doubled types must be a Fano four-cap (the complement of a Fano line). No other matrices are optimal.

## Assumptions and scope
All columns are sampled independently and uniformly from the \(n\) physical column positions, with replacement; duplicate columns therefore carry combined sampling probabilities. Recovery occurs at the first sample count for which the drawn columns span \(\mathbb F_2^3\). Codes are binary linear of rank exactly three. The classification is exhaustive only for \(8\le n\le13\); it does not assert a formula for larger lengths. The previously determined simplex case \(n=7\) and its multiples are not claimed here.

Identify each nonzero three-bit vector with its integer binary representation \(v\in\{1,\dots,7\}\); vector addition is bitwise exclusive-or. Write \(m_v\) for its column multiplicity. A Fano line is a three-set \(L=\{a,b,a\mathbin{\oplus}b\}\) with distinct nonzero vectors. The seven lines are
\[
\{1,2,3\},\{1,4,5\},\{1,6,7\},\{2,4,6\},\{2,5,7\},\{3,4,7\},\{3,5,6\}.
\]

## Proof
First, no optimal generator matrix contains a zero column: replacing such a column by any nonzero vector cannot delay recovery under a coupling that samples the same column indices, and strictly advances recovery with positive probability because the original nonzero columns already span dimension three. Therefore it suffices to study seven nonnegative multiplicities \(m_v\) with sum \(n\).

For a nonzero-column sampling distribution, let \(m(L)=\sum_{v\in L}m_v\). For every number \(t\ge0\) of draws, the event that the resulting span is proper is exactly the union of the seven planar (dimension-two) containment events. A span of dimension two belongs to one plane; a nonzero one-dimensional span lies in exactly three planes and one point; the zero span is in all seven planes and all seven points. Hence the exact subspace-lattice inclusion-exclusion identity gives
\[
\Pr(T>t)=\sum_L\left(\frac{m(L)}n\right)^t-2\sum_{v=1}^7\left(\frac{m_v}n\right)^t+8\,\mathbf1_{t=0}.
\]
For \(t=0\) this is \(7-14+8=1\), and for \(t>0\) the last term vanishes. Because the column types span exactly three dimensions, every line has \(m(L)<n\). Summing the geometric series over \(t\ge0\) proves
\[
E(m)=8+n\left(\sum_L\frac{1}{n-m(L)}-2\sum_{v=1}^7\frac{1}{n-m_v}\right).
\tag{1}
\]
Conversely, for rank-deficient profiles some line carries all columns and the expectation is infinite; those profiles are excluded from minimization.

Equation (1) reduces the problem to finitely many exact integer comparisons. Set \(D_n=\operatorname{lcm}(1,2,\ldots,n)\) and define
\[
Q_n(m)=\sum_L\frac{D_n}{n-m(L)}-2\sum_{v=1}^7\frac{D_n}{n-m_v}.
\tag{2}
\]
Every term in (2) is an integer, and minimizing (1) is equivalent to minimizing (2) among the weak seven-part compositions \(m_1+\cdots+m_7=n\). The accompanying complete enumerator implements this exact minimization without optimization software or floating-point arithmetic. Each profile is visited exactly once; rank-deficient profiles are excluded; every minimum is retained, not just one witness.

The exhaustive integer certificate yields the following table (\(N_n\) counts full-rank multiplicity profiles). The last column is the total number of minimizing profiles, including vector-label permutations preserving the Fano structure or not:

| \(n\) | \(N_n\) | Exact minimum of \(E(m)\) | Optimizing profiles |
|---:|---:|---:|---:|
|8|2702|\(422/105\)|7|
|9|4634|\(142/35\)|21|
|10|7560|\(509/126\)|28|
|11|11844|\(1439/360\)|7|
|12|17941|\(615/154\)|21|
|13|26411|\(7309/1848\)|7|

The verifier compares the **complete set** of minimizers against the independently defined Fano-subset families described in the Finding. Their cardinalities are \(\binom71,\binom72,\binom73-7,7,\binom75,\binom76\). In particular, the three- and four-element exceptions follow from Fano incidence, not merely their cardinality counts. Finally the automorphism group \(\mathrm{GL}(3,2)\) acts transitively on each of these optimizing families: on points, unordered pairs, noncollinear triples, complements of lines, complements of pairs, and complements of points. This proves the equivalence classification.

## Verification
Run \(\texttt{python3 verify.py}\) with Python 3 and its standard library. The code enumerates the complete domain and evaluates (2) as integer arithmetic with \(D_n\), compares every minimizing profile against its predicted Fano pattern, and independently evaluates expected recovery time by rational Markov recurrences on the finite lattice of vector subspaces. All 71,092 rank-three profiles across the six lengths are exhaustively compared; 240 additional independently generated profiles provide formula cross-checks. The file \(\texttt{verification_output.txt}\) records the actual run. The finite enumeration is a proof of the stated finite cases only, not of an unrestricted-length pattern.

## Relationship to prior work
Bertuzzo, Ravagnani, and Yaakobi (2025), Section III, obtained the simplex coverage expectation and explicitly checked the rank-three binary length-seven case. They did not provide the six subsequent length optima above. Their 2026 extension develops general expectation formulas. Gross, Grunbaum, Bertuzzo, Yaakobi, and Ravagnani (2026), Section IV, and independently Kong, Elishco, Wang, and Duman (2026), prove simplex optimality at the simplex parameters, which **already covers length seven**, including the appropriate uniform probability law, and also explains repeated-uniform sampling laws. Those results establish a universal continuous-distribution lower bound but do not furnish the discrete integer-constrained minimizers for lengths eight through thirteen. The present finding claims only those six new discrete optima and their exact equality structures.

## Limitations
No general closed-form optimum is established for every length, every dimension, or every alphabet. The proof uses an independently replayable exhaustive finite computation rather than a symbolic inequality valid for arbitrary lengths. The closest distributed-coverage primary source was not available as complete full text at examination; its abstract and scientific section-level excerpts establish simplex-parameter results but leave residual risk of an implicit intermediate-length computation. Independent mathematical/priority validation remains unperformed.

## References
1. M. Bertuzzo, A. Ravagnani, E. Yaakobi, *The Coverage Depth Problem in DNA Storage Over Small Alphabets* (first posted 2025-07-28), arXiv:2507.20639, https://arxiv.org/abs/2507.20639.
2. M. Bertuzzo, A. Ravagnani, E. Yaakobi, *The DNA Coverage Depth Problem: Duality, Weight Distributions, and Applications* (2026), arXiv:2603.06489, https://arxiv.org/abs/2603.06489.
3. R. Gross, Y. Grunbaum, M. Bertuzzo, E. Yaakobi, A. Ravagnani, *Optimal Codes for the Coverage Depth Problem and the Performance of Random Codes* (2026), arXiv:2610.07370, https://arxiv.org/abs/2610.07370.
4. X. Kong, O. Elishco, C. Wang, T. M. Duman, *The Coverage Depth Problem in Distributed DNA Data Storage* (2026), arXiv:2610.02931, https://arxiv.org/abs/2610.02931.
