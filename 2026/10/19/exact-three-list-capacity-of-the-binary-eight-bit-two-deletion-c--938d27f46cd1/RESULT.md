# Exact three-list capacity of the binary eight-bit two-deletion channel

## Finding
Let \(D_2(x)\) be the **set** of six-bit words obtainable by deleting exactly two coordinates from an eight-bit word \(x\), with repeated deletion outputs counted only once. Define
\[
A^{\mathrm{del}}_2(8,2;3)=\max\left\{|C|:\;C\subseteq\{0,1\}^{8},\quad
  |\{x\in C:y\in D_2(x)\}|\le 3\text{ for every }y\in\{0,1\}^{6}\right\}.
\]
Then
\[
\boxed{A^{\mathrm{del}}_2(8,2;3)=23.}
\]
Moreover, the natural fractional incidence-packing relaxation has exact optimum \(1082/45\); its rounded upper bound \(24\) is unattainable by an actual code. The exact integral optimum is \(23\).

## Assumptions and scope
The alphabet is exactly \(\{0,1\}\); transmitted words have length eight, and a received word consists of six **ordered** surviving bits after two arbitrary deletions. The list size is at most three distinct codewords for **each** possible output. Different embedding positions of one output in one codeword do not count as separate codewords. No claim is made about insertion list decoding, other lengths, other deletion orders, or asymptotic code rates.

## Proof
**Construction.** The following 23 distinct words form a code:

```text
00000000 00000001 00000111 00001000 00010111 00011111
00110001 00111101 01001010 01101010 01110000 01111111
10001100 10010011 10110101 10111100 11000010 11001110
11010011 11100000 11101111 11110100 11111111
```

Enumerating every six-position subset of each word, deduplicating the outputs within each word, and counting distinct sources for each of the 64 six-bit outputs shows that no output has more than three sources. The standalone `artifacts/verify_witness.py` implements this direct calculation without reference to the upper-bound search. This proves the lower bound \(23\).

**Exact weighted certificate.** Index the six-bit outputs lexicographically by integers \(0,\ldots,63\), and assign them the following integer weights, four rows of sixteen:

```text
99 36  4 36 16  0  0 63 16  0  0  0  4 17 32 36
 4  0  0 17  0  5 18  0  0 30 18  0 32  0 10 36
36 10  0 32  0 18 30  0  0 18  5  0 17  0  0  4
36 32 17  4  0  0  0 16 63  0  0 16 36  4 36 99
```

Write \(w_y\) for a weight and \(\mu_x=36\) for the all-zero and all-one eight-bit words, \(\mu_x=0\) otherwise. A direct enumeration of all 256 possible transmitted words verifies the **exact integer inequality**
\[
 s(x):=\sum_{y\in D_2(x)}w_y+\mu_x-135\geq0\qquad(x\in\{0,1\}^{8}).
\]
The weights sum to \(1058\), and \(\sum_x\mu_x=72\). Double counting the output incidences for any feasible code \(C\) gives
\[
135|C|\le\sum_{x\in C}\left(\sum_{y\in D_2(x)}w_y+\mu_x\right)
\le 3(1058)+72=3246.
\]
Hence \(|C|\le\lfloor3246/135\rfloor=24\). This inequality alone does **not** rule out 24. In fact, the fractional linear relaxation is **sharp** at \(3246/135=1082/45\): `artifacts/verify_witness.py` includes a sparse rational feasible fractional code with 48 nonzero word weights and common denominator \(35865\), summing exactly to \(862354/35865=1082/45\). It verifies all 64 relaxed output caps and each source upper bound \(0\le u_x\le1\). The integer problem therefore has a genuine fractional-integral gap.

**Sharp defect and exhaustive exclusion.** Suppose \(|C|=24\), and let \(m_y=|\{x\in C:y\in D_2(x)\}|\). Subtracting the preceding double count gives the identity
\[
6=\sum_{x\in C}s(x)+\sum_{x\notin C}\mu_x
 +\sum_{y\in\{0,1\}^{6}}w_y(3-m_y).
\]
All terms are nonnegative integers. Since each nonzero \(\mu_x\) equals \(36\), both constant words must lie in \(C\). Every selected word also has \(s(x)\le6\). Directly evaluating the 256 slacks gives exactly 54 words with slack zero, and among the words with positive slack at most six, four have slack two, four have slack three, twelve have slack four, and twelve have slack six. Every other word is excluded.

Let \(P\) be the subset of selected positive-slack words. Its total slack is at most six, and therefore it contains at most three words. There are precisely
\[
1+32+(6+16+48+6)+4=113
\]
possible choices of \(P\): the empty set, 32 singletons, 76 feasible pairs, and four triples of slack-two words. This is a complete finite partition of the potential 24-word codes. The other selected words must come from the 54 zero-slack words, including the two constant words.

For each of the 113 cases, `artifacts/verify_upper.cpp` searches all admissible zero-slack selections of cardinality \(24-|P|\). It maintains the 64 exact incidence caps \(m_y\le3\). If \(b=6-\sum_{x\in P}s(x)\) is the remaining defect budget, any output with \(w_y>b\) **must** be covered exactly three times: a remaining uncovered unit would alone exceed the budget. The verifier branches over every way to supply those mandatory occurrences, removes candidates when an output is already covered three times, and rejects when the minimum possible weighted residual deficit exceeds \(b\). If no mandatory row remains, it branches over both inclusion and exclusion of an arbitrary remaining candidate. Each branch is therefore either an exhaustive split or a deduction from a proved necessary condition. Every terminal 24-word candidate would be reported.

The exact integer verifier checks all 113 positive-slack cases and traverses 30,578 search nodes, with **no** feasible 24-word set. The search cutoff is larger than the observed node count and produces a nonzero status rather than a conclusion if reached. Therefore \(|C|\le23\), which together with the construction proves the theorem.

## Verification
From the directory containing this document, use:

```sh
python3 artifacts/verify_witness.py
c++ -O3 -std=c++17 artifacts/verify_upper.cpp -o verify_upper
./verify_upper
```

The first program recomputes deletion outputs by enumerating all 28 six-position subsets, verifies the 23-word construction, checks the 256 exact dual inequalities independently, and verifies the sparse rational feasible point proving the fractional optimum is exactly \(1082/45\). The second program reconstructs the output-incidence relation by a greedy subsequence test, verifies the integer dual, enumerates all 113 allowed slack-subsets, and runs the exhaustive upper-bound search. Recorded outputs are `WITNESS_OK`, `DUAL_OK`, and `INFEASIBLE_24_EXACT cases=113 total_sets=113 nodes=30578 tight=54 other=32`. These are finite computations, not extrapolation to other lengths.

## Relationship to prior work
Lin (2026) studies the same \(t\)-list adversarial deletion model and gives general asymptotic existence results and common-subsequence bounds; its theorems do not specify the maximum at \((n,k,t)=(8,2,3)\). Kiah, Wei, and Zeng (2026) obtain general constant-list rate bounds and a finite-length run-counting converse; substitution of \((q,n,k,L)=(2,8,2,3)\) into their Theorem 23 gives no bound below 106. The classical unique-decoding and two-list deletion code settings impose different incidence caps; their finite parameters do not imply this exact triple-list size. The present result is a single short-block exact determination by a weighted integer certificate and a complete obstruction search.

## Limitations
The last step of the upper bound uses an exhaustive finite computation; its reproducibility is provided as source code, not an independently audited formal proof. The fractional certificate by itself proves only the weaker bound \(24\). The result does not establish any neighboring code parameter, a uniform formula, or an asymptotic improvement. Prior unindexed finite tables or computational classifications could overlap the novelty claim.

## References
- A. D. Lin, *Lower Bounds for all List-Decodable Deletion Codes*, arXiv:2609.26650 (first posted September 22, 2026), https://arxiv.org/abs/2609.26650.
- H. M. Kiah, H. Wei, and R. Zeng, *Constant-List Insertion–Deletion Codes: New Bounds and an Improvement of Levenshtein's Lower Bound*, arXiv:2609.21395 (first posted September 18, 2026), https://arxiv.org/abs/2609.21395.
- V. Guruswami and J. Håstad, *Explicit Two-Deletion Codes with Redundancy Matching the Existential Bound*, arXiv:2007.10592 (2020), https://arxiv.org/abs/2007.10592.
