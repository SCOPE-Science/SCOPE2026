# Complete rooted palindromic-length spectrum of binary order-five de Bruijn cycles

## Finding

Let \(\mathcal B_5\) be the set of binary de Bruijn cycles of order five, modulo cyclic rotation. Each cycle has length \(32\) and contains each binary word of length five exactly once as a cyclic factor. For a nonempty *linear* word \(u\), let \(\operatorname{PL}(u)\) be the least number of nonempty palindromes whose concatenation is \(u\). For \(B\in\mathcal B_5\) and \(0\le c<32\), let \(B^{(c)}\) be the linear rotation starting at cut \(c\).

**Theorem (exhaustive order-five classification).** Over all \(2048\) cycles and all \(32\) cuts of each, the number of pairs \((B,c)\) having the indicated palindromic length is exactly:

| \(\operatorname{PL}(B^{(c)})\) | Rooted pairs |
| ---: | ---: |
| 4 | 384 |
| 5 | 3554 |
| 6 | 18266 |
| 7 | 29118 |
| 8 | 12138 |
| 9 | 2030 |
| 10 | 46 |
| **Total** | **65536** |

There are no other possible values. Moreover, putting \(m(B)=\min_c\operatorname{PL}(B^{(c)})\) and \(M(B)=\max_c\operatorname{PL}(B^{(c)})\), the complete distribution of ordered pairs \((m(B),M(B))\) is:

| \(m(B)\) | \(M(B)\) | Cycles |
| ---: | ---: | ---: |
| 4 | 7 | 48 |
| 5 | 7 | 120 |
| 5 | 8 | 350 |
| 5 | 9 | 64 |
| 6 | 7 | 118 |
| 6 | 8 | 742 |
| 6 | 9 | 74 |
| 6 | 10 | 8 |
| 7 | 8 | 254 |
| 7 | 9 | 154 |
| 7 | 10 | 8 |
| 8 | 9 | 92 |
| 8 | 10 | 14 |
| 9 | 10 | 2 |
| **Total** | | **2048** |

In particular, **every** order-five cycle has cuts of *different* palindromic lengths. The best cut always uses at most nine palindromes; exactly two cycles require nine even at their best cut. With their unique `00000` occurrence used as the start, those two cycles are:

```
00000110100111110110001010111001
00000100111010100011011111001011
```

They are equivalent under binary complementation followed by cyclic rotation; each has 29 cuts of palindromic length nine and three of length ten. The globally shortest and longest rooted lengths are exactly four and ten.

## Assumptions and scope

The alphabet is the labeled binary alphabet `0`,`1`. A palindrome is a nonempty contiguous factor equal to its reversal. The palindrome factors in a partition need not be distinct; all cuts of a cycle are counted individually, but the cycle itself is counted only once modulo rotation. No reversal or complementation quotient is imposed on the \(2048\) cycles. The claimed census is **only** for de Bruijn order five; no formula for higher orders is asserted. All counts are exact integers.

## Proof

This is a complete *finite exhaustive proof* supported by the included executable `verify.py`, not an inference from random samples.

**1. A bijective, complete search space.** Consider the binary de Bruijn directed graph whose 16 vertices are four-bit words and whose 32 labeled edges are five-bit words. An edge \(e\in\{0,\ldots,31\}\) runs from the vertex \(\lfloor e/2\rfloor\) to \(e\bmod16\). An order-five de Bruijn cycle is exactly an Eulerian edge tour of this graph. Its cyclic five-bit factor `00000` occurs exactly once, so place that edge first (edge 0); this is a canonical rooting of every rotation class. The `euler_cycles` search begins with edge 0 and, at each subsequent step, tries both unused edges leaving the current vertex; a completed path is accepted if it closes at the initial vertex. Every Eulerian tour with this canonical first edge is explored, and no two yield the same labeled cycle.

**2. Independent enumeration.** At each four-bit vertex, the two incoming five-bit edges must be bijectively matched to its two outgoing edges in a directed Euler tour. There are precisely two such local matchings. The `switch_cycles` enumeration checks all \(2^{16}=65536\) choices, follows their induced edge permutation from edge 0, and accepts exactly the choices giving one 32-cycle. This enumerates the same objects by a different global parameterization. The two sets of 32-symbol words are asserted equal and have size 2048. Every accepted word is also checked to have all 32 five-bit cyclic factors distinct.

**3. Exact minimization over palindrome partitions.** For each root word \(u\) of length \(32\), define \(P_u(0)=0\), and for \(1\le j\le32\) set

\[
P_u(j)=1+\min_{0\le i<j,\ u[i:j]\text{ is a palindrome}}P_u(i).
\]

This recurrence is exact: the final nonempty palindrome in any partition occupies some interval \([i,j)\), and appending that palindrome to an optimal partition of \(u[:i]\) realizes every candidate. There is at least one candidate because a single letter is a palindrome. Thus \(P_u(32)=\operatorname{PL}(u)\). The script evaluates the recurrence by literal substring reversal and also independently by expanding around all odd/even palindrome centers, updating the same prefix optimum from each detected palindrome occurrence. Center order is increasing, so all prefix optima needed by an interval are already finalized. The two methods are asserted equal on **every one** of the 65536 rooted words.

**4. Exhaustive tally and arithmetic certificates.** The verifier traverses the 2048 canonical cycles, evaluates all 32 cuts of each with both algorithms, tallies the first table, takes the minimum and maximum of each cycle's 32 values to tally the second table, and checks the stated two exceptional cycles and their cut multiplicities. Every entry in both tables is compared with an independently declared exact integer constant. Their column totals are separately checked as 65536 and 2048. The program terminates with `VERIFY_OK` only if all these tests pass. Since steps 1--3 exhaust the full finite domain and compute the relevant optimum exactly, this proves both tables and their corollaries.

## Verification

Run `python3 verify.py` using Python 3 and the standard library. The final packaged script was executed and produced:

```
VERIFY_OK binary_debruijn_order5_cycles=2048 rooted_words=65536 independent_cycle_generators=2 independent_palindrome_parsers=2 root_spectrum=4:384,5:3554,6:18266,7:29118,8:12138,9:2030,10:46 exceptional_min9_cycles=2 minmax_cells=14
```

No external data files, solvers, randomized seeds or third-party libraries are required. This verifies an exhaustive finite theorem; it does not imply an unrestricted-order result.

## Relationship to prior work

The de Bruijn Eulerian-cycle correspondence and the general notion of palindrome partitions are classical. Anisiu, Anisiu and Kása (2006; public arXiv version 2010) use de Bruijn words to generate all palindromes of a given length, and study the **number of palindromic factors**, not minimum-partition statistics of the 2048 order-five cycles. Ravsky (2003; public arXiv version 2010) finds the maximum palindromic length over **all** binary words of a fixed length and studies their average; his general formula gives 12 as the all-binary length-32 maximum and does not imply either conditional table. Frid, Puzynina and Zamboni (2012) study unbounded palindromic length of infinite-word factors rather than the all-cycle finite census. Bannai and collaborators (2015) analyze **diverse** palindromic factorization, a different constraint. Harju, Huova and Zamboni (2013) investigate the minimum number of palindromic *relations* generating a word, which is not the concatenation measure used here.

In the accessible related historical claims, the order-five de Bruijn BWT-run, longest-palindromic-factor, and LZ76-parsing spectra concern different invariants. Even knowing a word's longest circular palindrome does not determine its shortest palindromic partition of each linear cut. No equivalence to those claims was identified. The originality assessment is limited to inspected literature and records; it is not a priority certification.

## Limitations

The theorem is a finite exhaustive classification at order five, not a universal bound on all binary de Bruijn orders. Its correctness depends on executing or independently inspecting the included exhaustive checker and on the accompanying graph and dynamic-programming completeness arguments. The script has two independently structured enumerators and two palindrome algorithms, but an external audit has not been performed. An earlier unindexed or differently formulated equivalent census remains possible. The number of palindromic factors is a combinatorial length statistic; no compression-bit-rate conclusion is asserted.

## References

1. M.-C. Anisiu, V. Anisiu and Z. Kása, *Properties of palindromes in finite words*, Pure Mathematics and Applications 17 (2006), 183–195; arXiv:1002.2723, initial posting 2010-02-13. https://arxiv.org/abs/1002.2723
2. A. Ravsky, *On the Palindromic Decomposition of Binary Words*, Journal of Automata, Languages and Combinatorics 8 (2003), 75–83; arXiv:1004.1278, initial posting 2010-04-08. https://arxiv.org/abs/1004.1278
3. A. E. Frid, S. Puzynina and L. Q. Zamboni, *On minimal factorizations of words as products of palindromes*, arXiv:1210.6179, initially posted 2012-10-23. https://arxiv.org/abs/1210.6179
4. T. Harju, M. Huova and L. Q. Zamboni, *On Generating Binary Words Palindromically*, arXiv:1309.1886, initial posting 2013-09-07. https://arxiv.org/abs/1309.1886
5. H. Bannai et al., *Diverse Palindromic Factorization is NP-Complete*, arXiv:1503.04045, initial posting 2015-03-13. https://arxiv.org/abs/1503.04045
