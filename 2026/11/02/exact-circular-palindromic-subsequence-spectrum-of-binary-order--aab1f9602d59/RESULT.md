# Exact circular palindromic-subsequence spectrum of binary order-five de Bruijn cycles

## Finding

Let \(\mathcal{B}_5\) be the set of binary de Bruijn cycles of order \(5\), identified up to cyclic rotation. For a linear word \(u\), let \(\lambda(u)\) denote the maximum length of a palindromic **scattered subsequence** of \(u\). For \(W\in\mathcal{B}_5\), let \(W^{[r]}\), \(0\le r<32\), be its linear representative starting at the \(r\)-th circular position, and set

\[
\Lambda(W)=\max_{0\le r<32}\lambda(W^{[r]}),\qquad
\delta(W)=\min_{0\le r<32}\lambda(W^{[r]}).
\]

**Theorem (complete finite classification).** There are exactly \(2048\) cycles in \(\mathcal{B}_5\). Every one of them has a linear representative with a palindromic scattered subsequence of length at least \(25\), and the bound is sharp: exactly \(76\) cycles have \(\Lambda(W)=25\). The complete distribution of best-root lengths is

| \(\Lambda(W)\) | Number of cycles |
|---:|---:|
| 25 | 76 |
| 26 | 114 |
| 27 | 1380 |
| 28 | 286 |
| 29 | 192 |

Across all \(65536=2048\cdot32\) rooted traversals \((W,r)\), the complete distribution of \(\lambda(W^{[r]})\) is

| LPS length | Number of rooted traversals |
|---:|---:|
| 19 | 40 |
| 20 | 224 |
| 21 | 2662 |
| 22 | 3656 |
| 23 | 16140 |
| 24 | 9804 |
| 25 | 18934 |
| 26 | 6808 |
| 27 | 6060 |
| 28 | 1008 |
| 29 | 200 |

For completeness, the distribution of the worst-root value is

| \(\delta(W)\) | Number of cycles |
|---:|---:|
| 19 | 40 |
| 20 | 212 |
| 21 | 1080 |
| 22 | 456 |
| 23 | 260 |

The joint \((\delta,\Lambda)\) table, including all \(22\) supported entries and no others, is present in `summary.json`. Thus a word of this family needs at most \(7\) deletions to become a palindrome **after an optimal choice of cyclic starting position**, and some members need exactly \(7\). At an arbitrarily fixed starting position, as many as \(13\) deletions can be necessary. These are deletion-to-palindrome counts, not contiguous-palindrome lengths.

## Assumptions and scope

A binary de Bruijn cycle of order \(5\) is a circular binary word of length \(32\) in which every binary factor of length \(5\) appears exactly once, allowing wraparound. Two cycles differing only by cyclic rotation represent the same element of \(\mathcal{B}_5\); reversal and complement are **not** factored out. A rooted traversal chooses one of the \(32\) labeled circular positions, retaining all \(32\) symbols without wraparound in the subsequence. A scattered subsequence is formed by deleting any positions while preserving the order of the remaining positions. Palindromicity compares the remaining word with its reversal. Every de Bruijn cycle in scope is primitive, so all \(32\) starting positions are distinct as linear words.

## Proof

**1. Complete feedback parametrization.** Identify each binary length-\(5\) window with an integer state \(s\) between \(0\) and \(31\), with oldest bit most significant. From state \(s\), a left shift followed by feedback bit \(f(s)\) gives

\[
T_f(s)=(2s\bmod 32)+f(s).
\]

In a de Bruijn cycle every state occurs exactly once and every state has a unique successor, so the induced map \(T_f\) must be a permutation with one orbit of length \(32\). The two states with the same low four bits, \(u\) and \(u+16\), have the same shifted four-bit suffix. For their successors to be distinct, necessarily \(f(u+16)=1-f(u)\) for each \(0\le u<16\). Conversely, any table obeying those equations makes \(T_f\) a permutation; it is a de Bruijn cycle exactly when its orbit from the unique zero state has length \(32\). Thus all possibilities arise by choosing the \(16\) bits \(f(0),\ldots,f(15)\) independently. The checker examines **all** \(65536\) choices, not a sample. For every accepted one, reading the most significant bit of each successive state from state zero produces the uniquely normalized circular word containing the window `00000` at its starting state. This establishes exhaustiveness and prevents rotational duplicates.

**2. Exact palindromic-subsequence computation.** For a linear binary word \(u=u_0\cdots u_{31}\), let \(L(i,j)\) be the maximum length of a palindromic scattered subsequence of the inclusive interval \(u_i\cdots u_j\), with \(L(i,j)=0\) for \(i>j\). The standard optimal-substructure recurrence is

\[
L(i,j)=\begin{cases}
1,&i=j,\\
2+L(i+1,j-1),&i<j\ \text{and }u_i=u_j,\\
\max\{L(i+1,j),L(i,j-1)\},&i<j\ \text{and }u_i\ne u_j.
\end{cases}
\]

When endpoints match, they may be chosen together without shortening an optimum; when they differ, an optimal palindrome excludes at least one endpoint. Induction on interval length proves the recurrence. Its value \(L(0,31)\) is exactly \(\lambda(u)\). The checker applies it to every one of the \(32\) rotations of each accepted cycle and accumulates the displayed distributions. Every possible state table and root is accounted for by the finite loops, so the resulting census proves the theorem rather than inferring it from a sample.

**3. Independent exhaustive controls.** The checker separately enumerates Euler tours in the directed binary de Bruijn graph with \(16\) length-\(4\) vertices and \(32\) length-\(5\) edges. Every Euler tour can be rotated to start with the unique `00000` edge. Depth-first enumeration with this edge fixed yields exactly \(2048\) canonical cycles, precisely equal to those from the feedback tables. It independently evaluates each rooted LPS length as the longest common-subsequence length of \(u\) and \(u^R\), using a rowwise two-string dynamic program, and checks exact equality with the interval calculation for all \(65536\) roots. The LPS/LCS-reversal identity is recalled in [3, Section 1]. Both enumeration and numeric checks execute in the supplied, standalone `checker.py` and its expected output assertions; machine-readable all-entry counts are in `summary.json`.

**4. Sharp examples.** The canonical cycle `00000100101011010001111101110011` has \(\Lambda=25\), proving the minimax lower bound cannot be raised. The canonical cycle `00000100101100011111011100110101` has \(\Lambda=29\), proving the upper extremum is attained. The checker verifies the order-five property and every cyclic root for these examples as part of the exhaustive computation.

## Verification

Run `python3 checker.py` in a directory containing the supplied `checker.py`. It writes `summary.json` and prints `VERIFY_OK 2048 65536`, followed by all rooted, best-root, worst-root, joint and optimal-root counts. The code independently generates the same \(2048\) cycles by feedback permutations and Euler tours, checks that all \(32\) length-\(5\) circular windows are distinct, compares two dynamic programs for every root, and asserts all stated margins. Its sorted canonical cycle-list SHA-256 is `e8b5746482780303fec542789b123a2d51a892f460137bb9f8a96c85fec30421`. The exact `summary.json` output is included as an additional artifact. The finite argument and exhaustive loop bounds, not merely the printed log, are the proof of the numerical classifications.

## Relationship to prior work

Cooper and Heitsch [1] analyze skew and Fibonacci-type breakpoints in the lexicographically least binary de Bruijn sequence, not palindromic scattered subsequences of the complete cycle family. Chowdhury et al. [2] study algorithms for the longest **common** palindromic subsequence of two given words, not the distribution over all circular roots of de Bruijn sequences. Müllner and Ryzhikov [3] investigate longest palindromic scattered subsequences in arbitrary circular words, including the conjectured general \(2/3\) guarantee, but do not specialize to de Bruijn cycles or enumerate the order-five distribution. OEIS A318916 [4] gives the minimum optimal-root LPS across **all** binary circular words of length \(32\) as \(24\), not the sharper \(25\) within the de Bruijn subfamily, nor the distributions here. Results about **contiguous** palindromic factors are not equivalent to the scattered-subsequence statistic: a long scattered palindrome need not occur contiguously.

## Limitations

The complete tables and the sharp length-\(25\) guarantee apply only to binary order-five de Bruijn cycles. They do not establish an asymptotic or higher-order formula, or a general bound for all binary circular words. Enumeration is exhaustive for the explicitly defined finite domain but is not an independent external mathematical audit. The literature comparisons support a best-knowledge originality assessment, not an absolute historical priority claim; exact unpublished or unindexed tables remain a residual risk.

## References

1. Joshua Cooper and Christine E. Heitsch, *Generalized Fibonacci recurrences and the lex-least De Bruijn sequence*, arXiv:1003.5939, first public 2010-03-30. https://arxiv.org/abs/1003.5939
2. Shihabur Rahman Chowdhury, Md. Mahbubul Hasan, Sumaiya Iqbal, and M. Sohel Rahman, *Computing a Longest Common Palindromic Subsequence*, arXiv:1110.5296, first public 2011-10-24. https://arxiv.org/abs/1110.5296
3. Clemens Müllner and Andrew Ryzhikov, *Palindromic Subsequences in Finite Words*, arXiv:1901.07502, first public 2019-01-22, Sections 1–3. https://arxiv.org/html/1901.07502v1
4. Jeffrey Shallit and contributors, *OEIS A318916: Minimum longest palindromic subsequence among binary circular words*, initial entry September 2018, https://oeis.org/A318916
