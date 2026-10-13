# Sharp stochastic spanning-time dominance for the seven-point binary simplex code

## Finding
Let \(G\) be a full-row-rank binary \(3\times7\) generator matrix. A column-position read selects one of its seven positions uniformly, independently and with replacement. Define \(T_G\) as the first positive number of reads whose observed columns span \(\mathbb F_2^3\). For the binary simplex generator \(S\), which has each of the seven nonzero vectors of \(\mathbb F_2^3\) as a column exactly once, the following pointwise tail optimization holds for **every integer** \(t\ge3\):
\[
\Pr(T_G>t)\ge\Pr(T_S>t)=\frac{7\cdot3^t-14}{7^t}.
\]
Equality at any one \(t\ge3\) holds if and only if the seven columns are pairwise different and nonzero. This statement is invariant under a change of row basis and under column permutations. For \(t=0,1,2\), no matrix can be spanned by the first \(t\) samples, hence both tails are one.

The finite, sharp stability refinement is that for \(t=3,4,5,6\), respectively,
\[
\min_{G\not\sim S}7^t\bigl(\Pr(T_G>t)-\Pr(T_S>t)\bigr)
=(24,192,1080,5280)_t,
\]
where the notation means the four consecutive numbers at those four specified values of \(t\). For each value, equality holds precisely when the multiset of columns has six distinct nonzero points, one occurring twice and another missing; there are \(7\cdot6=42\) such multiplicity choices. The simplex failure numerators at these times are \(175,553,1687,5089\), respectively.

## Assumptions and scope
The ground field is exactly \(\mathbb F_2\). The length is seven and the column span has dimension three. Zero columns and repeated columns are allowed in \(G\). A read position is chosen uniformly from the seven physical positions; repeated columns therefore carry multiplicity. The stopping time has no truncation. The comparison applies to every integer observation deadline, rather than only the mean waiting time.

## Proof
Identify the nonzero vectors with the seven points of the Fano projective plane and write \(c_0,c_1,\ldots,c_7\) for the eight column multiplicities, where \(c_0\) is the number of zero columns and \(\sum_{i=0}^7 c_i=7\). Let \(\mathcal P\) denote the seven two-dimensional linear subspaces of \(\mathbb F_2^3\); each contains three nonzero vectors. Set
\[
m_P=c_0+\sum_{i\in P\setminus\{0\}}c_i,
\qquad \ell_i=c_0+c_i\quad(1\le i\le7).
\]
Every failing sequence of \(t\) reads spans a proper linear subspace. Inclusion–exclusion on the lattice of subspaces, whose Möbius coefficients below the whole three-space are \(1\) for planes, \(-2\) for one-dimensional subspaces, and \(8\) for the zero subspace, gives, for every integer \(t\ge1\),
\[
7^t\Pr(T_G>t)=\sum_{P\in\mathcal P}m_P^t-2\sum_{i=1}^7\ell_i^t+8c_0^t.\tag{1}
\]
For \(S\), \(c_0=0\), every \(c_i=1\), each \(m_P=3\), and each \(\ell_i=1\). Thus the claimed simplex formula is exact.

We next prove the key geometric dichotomy: if the multiset is not the seven distinct nonzero vectors, some plane has \(m_P\ge4\). Indeed, each nonzero vector lies in three of the seven Fano planes, whereas the zero vector lies in all seven. Consequently \(\sum_Pm_P=21+4c_0\). If \(c_0>0\), the average exceeds three. If \(c_0=0\) and all plane occupancies were at most three, they would all be exactly three. Writing \(B\) for the seven-by-seven plane-point incidence matrix, we would have \(Bc=3\mathbf 1\), \(B^\mathsf TB=2I+J\), and \(\sum_i c_i=7\). Multiplying by \(B^\mathsf T\) gives \(2c+7\mathbf1=9\mathbf1\), so \(c=\mathbf1\), contradiction.

For any nonsimplex matrix and any positive integer \(t\), the ordered sequences that use positions from one such occupied plane all fail, so \(7^t\Pr(T_G>t)\ge4^t\). At \(t=7\), \(4^7=16384>15309=7\cdot3^7\), and the inequality remains strict at all greater integer \(t\). This establishes strict stochastic dominance for every \(t\ge7\), without finite sampling assumptions.

For the remaining four values \(t=3,4,5,6\), the attached standalone certificate `verify.py` enumerates every multiset of seven vectors drawn from the eight binary three-vectors: there are \(\binom{14}{7}=3432\) such multisets, of which exactly \(2696\) span three dimensions. For each, it calculates the integer failure counts by two independent procedures: formula (1) and a dynamic program over all 16 vector subspaces. Both agree for \(t=1,\ldots,6\). The exhaustive comparison finds one simplex multiplicity vector and positive excess numerators for every one of the other \(2695\) full-rank vectors. The respective **sharp minima** are \(24,192,1080,5280\), each with precisely the 42 omitted-and-repeated nonzero-point minimizers described above. This establishes strictness at the four remaining deadlines and proves the stability refinement. The exhaustive enumeration is finite and complete for the explicitly bounded cases; it is not used to assert anything about arbitrarily large deadlines.

## Verification
Run `python3 verify.py` with Python 3 and its standard library. The program constructs the Fano incidences directly from binary dot products, constructs all 16 subspaces and their sample-update transitions, enumerates all \(3432\) multisets, filters the \(2696\) spanning multisets by independent XOR closure, and compares exact integer failure counts obtained by the two counting procedures for six deadlines. It checks the claimed minimizer counts and finishes with `VERIFY_OK`. All integer computations are exact. The analytic plane-occupancy argument, rather than the finite verifier, handles all \(t\ge7\).

## Relationship to prior work
Bertuzzo, Ravagnani, and Yaakobi study DNA retrieval coverage depth and minimum **expected** reads in their 2025 study and the 2026 extension. Kovačević's transitive-matroid theorem optimizes the probability that a given number of samples are independent; its three-sample specialization already covers the \(t=3\) ordering here, which is **not** offered as a standalone new assertion. The contribution is the **simultaneous all-deadline stochastic tail inequality** (particularly at \(t\ge4\)) and exact finite stability at four initial deadlines. Gross, Grunbaum, Bertuzzo, Yaakobi, and Ravagnani (October 2026) prove a general simplex optimality theorem for the expected stopping time; that result does not alone imply pointwise tail optimization. A separate October 2026 distributed-DNA-storage article provides a general distribution formula, but no covering tail-optimality theorem was verified in its accessible abstract. General distribution formulas do not by themselves prove the stated minimax inequality.

## Limitations
Only seven physical binary columns and rank three are optimized. The theorem does not assert analogous stochastic dominance for arbitrary lengths, dimensions, fields, nonuniform read distributions, errors, or multi-node storage. The first four strict finite-deadline comparisons depend on the complete exact finite certificate, supplied as source; its validity is not replaced by an unexamined output log. An equivalent unpublished or difficult-to-index prior theorem cannot be excluded. An apparently relevant October 2026 article could be inspected only at abstract level; this is a specific residual literature-comparison risk, not evidence of coverage or noncoverage of its full contents.

## References
- D. Bertuzzo, A. Ravagnani, and E. Yaakobi, *The Coverage Depth Problem in DNA Storage Over Small Alphabets*, arXiv:2507.20639v1 (first public July 28, 2025), https://arxiv.org/abs/2507.20639.
- D. Bertuzzo, A. Ravagnani, and E. Yaakobi, *The DNA Coverage Depth Problem: Duality, Weight Distributions, and Applications*, arXiv:2603.06489v1, https://arxiv.org/abs/2603.06489.
- M. Kovačević, *Maximum Probability of Independence in Transitive Matroids*, arXiv:2605.23291v1, https://arxiv.org/abs/2605.23291.
- E. Gross, B. Grunbaum, D. Bertuzzo, E. Yaakobi, and A. Ravagnani, *Optimal Codes for the Coverage Depth Problem and the Performance of Random Codes*, arXiv:2610.07370v1, https://arxiv.org/abs/2610.07370.
- Kong, Elishco, Wang, and Duman, *The Coverage Depth Problem in Distributed DNA Data Storage*, arXiv:2610.02931v1, https://arxiv.org/abs/2610.02931.
