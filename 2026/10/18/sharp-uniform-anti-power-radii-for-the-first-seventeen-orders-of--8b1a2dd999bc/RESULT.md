# Sharp uniform anti-power radii for the first seventeen orders of the regular paperfolding word

## Finding

For the zero-indexed regular binary paperfolding word \(f=f_0f_1\cdots\) defined below, let \(R_f(k)\) be the least integer \(M\) such that **at every position** \(i\ge0\), some block length \(1\le m\le M\) makes the consecutive blocks
\[
 f_i\cdots f_{i+m-1},\ f_{i+m}\cdots f_{i+2m-1},\ \ldots,\ f_{i+(k-1)m}\cdots f_{i+km-1}
\]
pairwise distinct. The exact initial spectrum is
\[
\boxed{
R_f(k)=
\begin{cases}
2,&k=2,\\
5,&k=3,\\
6,&k=4,\\
7,&5\le k\le8,\\
9,&9\le k\le16,\\
15,&k=17.
\end{cases}}
\]
In particular, the uniform radius is exactly nine at order sixteen, but jumps to fifteen at order seventeen. The monotonicity proved below implies \(R_f(k)\ge15\) for every \(k\ge17\) whenever its radius is finite (and the inequality holds in the extended sense otherwise).

## Assumptions and scope

The binary sequence is specified by \(f_0=0\) and, for all \(t\ge0\),
\[
 f_{2t}=t\bmod2\quad(t\ge1),\qquad f_{2t+1}=f_t.
\]
Equivalently, \(f_i=1\) precisely when the odd part of \(i+1\) is congruent to \(3\pmod4\). Its beginning is `00100110001101100010011100110110`.

An order-\(k\) anti-power is a word of length \(km\) split into \(k\) *adjacent*, *equal-length*, *pairwise unequal* blocks. Equality of blocks is literal, not up to rotation, complementation, or Parikh vector. The radius is a worst-starting-position bound, rather than the smallest anti-power *anywhere* or the shortest anti-power starting at position zero. The theorem makes exact assertions for integer orders \(2\le k\le17\) only.

## Proof

**Lemma 1 (monotonicity).** For every infinite word and any \(k\ge2\), its uniform radius for order \(k\) does not exceed that for order \(k+1\), in the extended nonnegative integers. Indeed, the first \(k\) blocks of a \((k+1)\)-anti-power form a \(k\)-anti-power of the same block length at the same position. Thus an upper bound valid at all positions for order \(k+1\) is also valid for order \(k\).

**Lemma 2 (finite complete factor test).** Suppose the first \(N\) symbols of an infinite word contain exactly \(p(L)\) different factors of length \(L\), where \(p(L)\) is the known total number of length-\(L\) factors of the infinite word. Then this finite factor set equals the complete infinite factor set. For a fixed order \(k\) and candidate radius \(r\), set \(L=kr\). If every word in this complete set contains an order-\(k\) anti-power in its prefix of length \(km\) for some \(1\le m\le r\), then \(R_f(k)\le r\). If one of these factors contains no such anti-power for \(1\le m<r\), then \(R_f(k)\ge r\). Both assertions are direct: length-\(L\) factors encode all necessary symbols for every possible tested \(m\).

**Factor-count input.** Allouche's factor-complexity theorem gives \(p_f(4)=12\) and \(p_f(L)=4L\) for \(L\ge7\), for *every* paperfolding word. The specified \(f\) is the regular paperfolding word, as follows either from the odd-part characterization or its Toeplitz construction. Thus this published infinite theorem, together with a finite cardinality equality, certifies that the factor sets used below are exhaustive across **all** possible starting positions, not merely positions in a sampled prefix.

**Eight finite anchor tests.** Generate precisely the first \(2048\) symbols of \(f\), form all \(2048-L+1\) indexed factors of length \(L\), and retain distinct factors. For each anchor pair \((k,r)\), test every \(m\in\{1,\ldots,r\}\) for pairwise distinct adjacent blocks. The complete finite outcome is:

| \(k\) | \(r\) | \(L=kr\) | Distinct length-\(L\) factors | Factors avoiding every block length \(m<r\) | One witness position |
|---:|---:|---:|---:|---:|---:|
| 2 | 2 | 4 | 12 | 6 | 7 |
| 3 | 5 | 15 | 60 | 1 | 86 |
| 4 | 6 | 24 | 96 | 1 | 3 |
| 5 | 7 | 35 | 140 | 3 | 20 |
| 8 | 7 | 56 | 224 | 32 | 15 |
| 9 | 9 | 81 | 324 | 10 | 100 |
| 16 | 9 | 144 | 576 | 258 | 31 |
| 17 | 15 | 255 | 1020 | 4 | 552 |

For **every** factor at every row, at least one tested block length \(m\le r\) produces an anti-power; the indicated positive number of obstructing factors shows \(m<r\) does not always suffice. The table's factor counts match the known exact full complexities, so Lemma 2 gives \(R_f(k)=r\) for all eight anchors. The `verify.py` package checks every indicated value, independently generates the word through two definitions, independently enumerates the factor sets through byte slicing and binary rolling values, outputs concrete witness factors, and verifies the actual block inequalities. It does not assume the desired radius in any lower-bound check.

Finally Lemma 1 sandwiches \(R_f(6)\) and \(R_f(7)\) between \(R_f(5)=R_f(8)=7\), and sandwiches all \(R_f(k)\) with \(10\le k\le15\) between \(R_f(9)=R_f(16)=9\). All entries of the displayed formula follow. The transition at seventeen is sharp because the row at sixteen has universal bound nine, whereas a certified length-\(255\) factor at seventeen forbids *every* block length up to fourteen.

## Verification

Run `python3 verify.py` in a directory containing `verify.py`. It requires only the Python 3 standard library, no network and no other data files. The verifier tests two independent formulas for the first \(2048\) paperfolding digits; two different factor-enumeration representations for each tested length; the published complexity value at each length; all upper-bound possibilities on the entire complete set; and an explicit lower-bound obstruction for each row. It prints the eight rows with obstruction counts, explicit binary witnesses, and a final `VERIFY_OK` marker. The computation is a finite exhaustive proof *conditional only on* the independently published infinite factor-count theorem, not a claim that running \(2048\) positions constitutes an infinite search.

## Relationship to prior work

Fici, Restivo, Silva and Zamboni introduced anti-powers and proved that in a uniformly recurrent aperiodic word every position begins an anti-power of every order. Their result is qualitative: it does not give the exact uniform worst-position block-length radius for the regular paperfolding word. Allouche's published paperfolding factor-count theorem supplies the full-factor certificate needed here, but does not discuss anti-powers. Fici, Postic and Silva prove existence of *abelian* anti-powers in paperfolding words, with existence quantified over starting positions; their result neither determines nor implies a literal all-start radius. Berger and Defant prove an \(O(k)\) uniform block-length bound for certain uniformly morphic words, a different quantitative level from the exact values established here. Published exact Fibonacci-word radii concern a different infinite language and cannot transfer these values to paperfolding by changing names.

## Limitations

This is an exact, computer-assisted finite classification for \(2\le k\le17\), together with the elementary monotonic consequence for larger orders; **no formula or finite upper bound at orders \(k\ge18\) is claimed**. The finite program verifies the required bounded combinatorics, while completeness of its factor sets invokes Allouche's theorem. The result does not extend automatically to arbitrary generalized paperfolding sequences with different folding instructions. Related or unindexed earlier classifications could exist; no independent scientific audit has been performed.

## References

1. J.-P. Allouche, *The Number of Factors in a Paperfolding Sequence*, Bulletin of the Australian Mathematical Society **46** (1992), 23–32, DOI: `10.1017/S0004972700011655` (Theorem, Section 5).
2. G. Fici, A. Restivo, M. Silva, L. Q. Zamboni, *Anti-Powers in Infinite Words*, arXiv:`1606.02868`, first publicly submitted 2016-06-09 (Theorem 6, Corollary 7 and Section 5).
3. G. Fici, M. Postic, M. Silva, *Abelian AntiPowers in Infinite Words*, arXiv:`1810.12275` (Section 3, Theorems 6 and 8).
4. A. Berger, C. Defant, *On Anti-Powers in Aperiodic Recurrent Words*, arXiv:`1902.01291` (Theorem 5).
