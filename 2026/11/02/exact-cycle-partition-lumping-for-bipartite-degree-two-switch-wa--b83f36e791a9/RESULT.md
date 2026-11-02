# Exact cycle-partition lumping for bipartite degree-two switch walks

## Finding
For every integer \(n\ge2\), consider all \(n\times n\) binary matrices with every row sum and column sum equal to \(2\). Choose independently and uniformly an unordered pair of distinct rows and an unordered pair of distinct columns. If the selected \(2\times2\) submatrix has one of the two permutation-matrix patterns, replace it by the other pattern; otherwise stay put. This is the standard rectangular switch walk, with an attempted rectangle at each step.

View a matrix as a simple bipartite \(2\)-regular graph, and let \(\lambda=(\lambda_1,\ldots,\lambda_h)\vdash n\) record its component cycles, where the corresponding bipartite cycle has length \(2\lambda_i\). Every part is at least \(2\). **The cycle-partition projection is an exact Markov chain (strongly lumpable) with the following complete transition counts**, independent of the particular labelled matrix:

1. For each unordered pair of *component occurrences* of sizes \(a,b\), exactly \(4ab\) rectangles merge them into a single part of size \(a+b\).
2. For each component occurrence of size \(k\) and each \(2\le a\le b\) with \(a+b=k\), exactly \(2k\) rectangles split it into \(a,b\) if \(a<b\), and exactly \(k\) if \(a=b\).
3. Exactly \(\sum_i\lambda_i(\lambda_i-2)\) legal rectangles retain the same cycle partition. All remaining rectangle attempts do nothing.

Multiply these counts by \(\binom n2^{-2}\) to obtain the corresponding one-step transition probabilities (and aggregate when several component occurrences lead to the same target partition). Thus the switch degree of any state of type \(\lambda\) is
\[
\deg(\lambda)=n(2n-5)+2m_2(\lambda),
\]
where \(m_2\) counts components that are four-cycles. The number of labelled matrices of type \(\lambda\) is
\[
N_n(\lambda)=\frac{(n!)^2}{\prod_{k\ge2}(2k)^{m_k(\lambda)}m_k(\lambda)!}.
\]
The unique stationary distribution of the type chain is proportional to \(\prod_{k\ge2}((2k)^{m_k}m_k!)^{-1}\), equivalently **Ewens sampling formula with parameter \(1/2\), conditioned to have no singleton parts**. The statement is exact at each finite \(n\); it is not an asymptotic assertion.

## Assumptions and scope
Every row and column is individually labelled; all matrices are simple binary matrices, not nonnegative integer tables with entries above one. Distinct components with equal lengths are treated as separate occurrences when counting moves. The cycle parts sum to the number \(n\) of vertices in either bipartition (half the total number of graph vertices). Only the checkerboard \(2\times2\) switch is allowed. Holding is part of the specified chain; replacing it by the degree-normalized nonlazy walk changes the stationary measure.

There are \(T_n=\binom n2^2\) equally likely rectangle choices. At \(n=2\) there is one matrix, no legal switches and the singleton stationary distribution. For \(n\ge3\) the full switch walk is irreducible by Ryser's classical connectivity theorem for binary matrices with fixed margins, and its cycle-partition quotient is also irreducible. The holding probability makes the specified walk aperiodic for all \(n\ge2\).

## Proof
**1. Classification of local switches.** Fix a component with \(k\) left vertices and \(k\) right vertices, hence a \(2k\)-cycle. Its edges split into the two alternating perfect matchings \(A\) and \(B\), each with \(k\) edges. For two edges chosen from distinct components the cross edges are absent; there are \((2a)(2b)=4ab\) choices, each merging exactly the two component cycles.

Within one component, choose edges from \(A\) or from \(B\). Two edges in the same alternating matching determine a legal switch exactly if their positions in the cyclic list are nonconsecutive. The switch cuts the cycle into two disjoint even cycles. If their half-lengths are unequal \(a<b\) with \(a+b=k\), there are \(k\) positions in each of \(A\) and \(B\), giving \(2k\) switches. If \(a=b\), each unordered pair is counted twice by cyclic starting position, yielding \(k/2\) pairs in each matching and \(k\) switches total. Four-cycles have no legal same-matching switches, as the shortest possible split requires both parts at least two.

An edge of \(A\) and an edge of \(B\) are disjoint exactly for \(k(k-2)\) pairs. In every such case the opposite corners are absent, so the switch is legal. Traversing the newly connected edges shows that it leaves one connected \(2k\)-cycle. Conversely, every pair of edges giving a legal switch belongs to one of these three cases: different components, the same alternating matching of one component, or different alternating matchings of one component. This proves the complete transition-count rules.

**2. Degree.** Summing the preceding rules gives, for \(k\ge3\), \(k(k-2)+k(k-3)=k(2k-5)\) within-component switches, while a component of half-length two has none. Adding \(4\sum_{i<j}\lambda_i\lambda_j\) cross-component switches and simplifying proves \(\deg(\lambda)=2n^2-5n+2m_2(\lambda)\). Every legal rectangle creates a distinct neighboring binary matrix, so this is also the switch-graph degree.

**3. Exact lumpability.** Each matrix of type \(\lambda\) has the same number of rectangle choices leading to each target partition \(\mu\), as specified above. Because all \(T_n\) rectangles are equiprobable, the conditional law of the next cycle type depends only on the present type. This proves strong lumpability for arbitrary initial distributions, rather than only for stationary starts.

**4. Multiplicities and stationarity.** On fixed sets of \(k\) labelled left and \(k\) labelled right vertices there are \(k!(k-1)!/2\) unoriented bipartite Hamiltonian cycles, including exactly one when \(k=2\). Choose and distribute disjoint labelled vertex sets of sizes \(\lambda_i\) on both sides, divide by multiplicity factorials for equal-size components, and multiply by these cycle counts. The cancellations yield the displayed \(N_n(\lambda)\).

Every allowable rectangle switch is a reversible involution, and each rectangle is chosen with probability \(1/T_n\). Hence the full finite chain is symmetric and uniform on binary matrices at stationarity; its cycle-type pushforward gives weights proportional to \(N_n(\lambda)\), i.e. the displayed Ewens\((1/2)\) law conditioned against singleton parts. Connectivity supplies uniqueness; alternatively merge all parts, then split to any target partition using positive prescribed counts.

For example, when \(n=6\), the type counts are \(43{,}200\) for \((6)\), \(16{,}200\) for \((2,4)\), \(7{,}200\) for \((3,3)\), and \(1{,}350\) for \((2,2,2)\). The nonzero off-diagonal rectangle counts are \((6)\to(2,4):12\), \((6)\to(3,3):6\), \((2,4)\to(6):32\), \((2,4)\to(2,2,2):4\), \((3,3)\to(6):36\), and \((2,2,2)\to(2,4):48\). Division by \(225\) gives their probabilities; the diagonal makes each row sum one. These rates obey detailed balance with the stated multiplicities.

## Verification
The supplied `verify_switch_cycletypes.py` exhaustively generates every labelled state for \(2\le n\le5\) by constrained row-pair recursion, builds every legal switch by replacing two edges, and independently computes cycle components and each transition target. The separate C++17 program `verify_switch_cycletypes.cpp` generates the matrices using bitmasks, tests all actual \(2\times2\) rectangles, computes connected components on the full bipartite vertex set, and exhaustively verifies the claimed transition rules for \(2\le n\le6\), including all \(67{,}950\) states at \(n=6\). Both also reproduce the closed formula for every partition's multiplicity. The computations test finite cases; the all-\(n\) theorem rests on the cycle argument above.

To reproduce, run `python3 verify_switch_cycletypes.py`, then `g++ -std=c++17 -O2 verify_switch_cycletypes.cpp -o verify_switch_cycletypes` and `./verify_switch_cycletypes` in a directory containing the two embedded source files. No external packages are needed.

## Relationship to prior work
Ryser's fixed-margin matrix interchange theorem (1957), as presented and proved in Miklós–Erdős–Soukup, already establishes connectivity; that is not claimed as novel. Miklós–Erdős–Soukup study the rectangular switch Markov chain on general bipartite degree sequences, proving rapid mixing for half-regular margins. Their chain definition and symmetry are the basis for our model, but these statements do not provide an exact partition-valued transition kernel in the degree-two case. Nester's 1994 enumeration of Eulerian orientations of complete bipartite graphs includes the known count of \(90\) matrices at \(n=4\); the general total-state counts are also recorded as OEIS A001499 and A008300. Neither the counts nor the uniform matrix stationary measure alone are claimed as new. The candidate contribution is the **complete cycle-type-specific merge/split/stay kernel and its strong-lumpability consequence**, not an enumeration of already tabulated matrices.

## Limitations
The partition process forgets labels and does not by itself give exact mixing times, spectral gaps, or label-level transition probabilities for individual matrices. It applies only to binary degree-two margins. The finite verification is exhaustive only through \(n=6\). A differently named special-case fragmentation–coagulation analysis in historical sampling literature could contain an equivalent projected kernel; the literature comparison cannot rule out every unindexed work. The review here is not an independent scholarly audit.

## References
1. M. R. Nester, *Eulerian Orientations and Circuits of Complete Bipartite Graphs*, Journal of Combinatorial Mathematics and Combinatorial Computing **16** (1994), 3–17. Public article: https://combinatorialpress.com/jcmcc-articles/volume-016/eulerian-orientations-and-circuits-of-complete-bipartite-graphs/ . Publicly dated 1994-10-31; relevant exact counts in Table 5.
2. I. Miklós, P. L. Erdős, L. Soukup, *Towards Random Uniform Sampling of Bipartite Graphs with given Degree Sequence*, Electronic Journal of Combinatorics **20** (2013), #P16; arXiv:1004.2612, first posted 2010-04-15. DOI:10.37236/3028. Relevant Definition 2.1, Theorem 2.2, Section 3.
3. R. Ryser, *Combinatorial properties of matrices of zeros and ones*, Canad. J. Math. **9** (1957), 371–377 (connectivity theorem, cited in Reference 2).
4. OEIS A001499, *Number of n × n matrices with exactly 2 ones in each row and column*, https://oeis.org/A001499; comparison sequence only, not a claim to new counts.
