# Sharp six-read reconstruction and equality-pair census for two length-two burst deletions

## Finding
Fix an integer alphabet size \(q\ge3\). For a word \(x\in\{0,1,\ldots,q-1\}^{6}\), let \(D(x)\) denote the **set of distinct** length-two outputs produced by performing exactly two successive deletions, each deleting two adjacent symbols in the *current* word. The maximum pairwise intersection over distinct inputs is
\[
\max_{x\ne y}|D(x)\cap D(y)|=5.
\]
Moreover, the exact number \(T(q)\) of **unordered, labeled-alphabet** pairs \(\{x,y\}\) of distinct length-six inputs with intersection size five is
\[
T(q)=\frac{210(q)_3+582(q)_4+363(q)_5+71(q)_6+4(q)_7}{2},
\qquad (q)_k=q(q-1)\cdots(q-k+1),
\]
where \((q)_k=0\) for \(k>q\). Thus \(T(3)=630\), \(T(4)=9504\), \(T(5)=63000\), and \(T(6)=273600\). As \(q\to\infty\), \(T(q)=2q^{7}+O(q^{6})\), so the proportion of unordered distinct-input pairs attaining the worst overlap is \(4q^{-5}+O(q^{-6})\).

Equivalently, six *distinct* channel outputs suffice to identify any input that could have produced all six; five do not suffice in general. The binary case is deliberately excluded from the displayed formula: its maximum is four.

## Assumptions and scope
The alphabet is labeled and has exactly \(q\) symbols, not necessarily a field. Inputs are ordered words of exactly six symbols. Both deletion operations have burst length exactly two; the second burst acts after the first, on the shortened word. Outputs are deduplicated before intersections are taken. The pair census counts unordered sets of two *distinct* input words, without quotienting by alphabet permutations or other equivalences. There is no restriction on which symbols may appear in the inputs.

## Proof
**Reduction to six ordered symbol pairs.** Exhausting the five positions of the first two-symbol deletion and the three positions of the second deletion shows that the original-coordinate survivor pairs are precisely
\[
(1,2),\ (1,4),\ (1,6),\ (3,4),\ (3,6),\ (5,6).
\]
Consequently, with \(x=(a,b,c,d,e,f)\),
\[
D(x)=\{(a,b),(a,d),(a,f),(c,d),(c,f),(e,f)\}.
\]
Every ball has at most six distinct outputs. If it has six, then its three distinct first components are \(a,c,e\), with respective outdegrees \(3,2,1\), and its three distinct second components are \(b,d,f\), with respective indegrees \(1,2,3\). These are degrees in the *ordered-pair relation*, so the conclusion remains valid when a first-component symbol also appears as a second-component symbol. Thus the six-output set determines \(a,b,c,d,e,f\) uniquely. In particular, two distinct inputs cannot share six outputs.

**Sharpness.** The distinct words \(x=(0,0,1,0,2,1)\) and \(y=(0,1,1,0,2,1)\), admissible for every \(q\ge3\), satisfy
\[
D(x)=D(y)=\{(0,0),(0,1),(1,0),(1,1),(2,1)\},
\]
so they share five outputs. Together with the upper bound, this proves the extremal intersection statement.

**Exact equality census.** Concatenate an ordered pair \((x,y)\) into a twelve-position word. Identify two positions exactly when they carry the same symbol. Every equality pattern has a unique *restricted-growth* encoding \((r_1,\dots,r_{12})\), with \(r_1=0\) and \(0\le r_i\le1+\max_{j<i}r_j\). If the pattern uses precisely \(k\) different labels, it has exactly \((q)_k\) realizations over the actual alphabet. These realizations preserve the set-intersection cardinality, because only symbol equality matters. The patterns for \(x=y\) are discarded.

The included exhaustive symbolic-pattern enumerator visits all \(B_{12}=4{,}213{,}597\) restricted-growth encodings and computes both balls as sets of ordered pairs; only patterns with exactly five shared outputs are counted. The resulting numbers of ordered-center equality patterns by number \(k\) of distinct symbols are

| \(k\) | both balls size five | one size five, the other six | both size six | total |
|---:|---:|---:|---:|---:|
| 3 | 72 | 96 | 42 | 210 |
| 4 | 72 | 288 | 222 | 582 |
| 5 | 12 | 144 | 207 | 363 |
| 6 | 0 | 16 | 55 | 71 |
| 7 | 0 | 0 | 4 | 4 |

All other symbol counts contribute zero. Since swapping two distinct inputs interchanges their order and has no fixed points, division by two yields the displayed formula for unordered pairs. This finite symbolic enumeration proves the formula for **every** alphabet size, rather than extrapolating from a list of small values.

## Verification
`verify_rgs.cpp` independently derives the six survivor-coordinate pairs by two sequential deletions. It then enumerates every restricted-growth partition of twelve positions; its assertions check the complete coefficient table, \(B_{12}=4{,}213{,}597\), and that no distinct equality pattern has six common outputs. Compile using `g++ -O2 -std=c++17 verify_rgs.cpp -o verify_rgs`; execute `./verify_rgs`.

`verify_direct.py` separately constructs deletion balls by applying actual substring deletions, never using the survivor-pair formula or restricted-growth partitions. Its complete finite-alphabet enumerations for \(q=2,3,4,5\) reproduce maximum overlaps \(4,5,5,5\) and all corresponding pair counts for \(q\ge3\). Run `python3 verify_direct.py`. The two programs are standalone and depend only on a standard C++17 compiler and Python 3 standard library, respectively.

## Relationship to prior work
Schoeny, Wachter-Zeh, Gabrys, and Yaakobi (first publicly available on 2016-02-22) study burst-deletion error-correcting codes and provide the foundational fixed-burst channel. Sun, Xi, and Ge (2023) determine pair-ball intersections for **one** burst. Lan, Sun, Yu, and Ge (arXiv:2504.20460, 2025), particularly Section IV.B and Theorem IV.16, determine the maximum intersection for **multiple** bursts in the **binary** deletion case and obtain general alphabet ball-size formulas and a general-alphabet *lower construction*. At these parameters the latter construction already provides the lower overlap of five for \(q\ge3\); that lower bound is not claimed as new. Neither those reported results nor the compared sources provide this nonbinary sharp upper bound or the all-alphabet equality-pair polynomial.

## Limitations
This result concerns exactly two bursts of length two on length-six inputs. It does not prove a formula for larger blocklengths, other burst lengths, or additional bursts. The equality polynomial relies on a finite, fully enumerated family of equality patterns; its correctness depends on the supplied deterministic code and the stated proof of the symbolic reduction. No independent external audit has been performed. An obscure or unindexed earlier enumeration of these specific equality cases cannot be ruled out solely by literature searches.

## References
- C. Schoeny, A. Wachter-Zeh, R. Gabrys, and E. Yaakobi, *Codes Correcting a Burst of Deletions or Insertions*, arXiv:1602.06820 (first version 2016-02-22). https://arxiv.org/abs/1602.06820
- Y. Sun, Y. Xi, and G. Ge, *Sequence Reconstruction Under Single-Burst-Insertion/Deletion/Edit Channel*, IEEE Transactions on Information Theory 69 (2023), 4466–4483. https://doi.org/10.1109/TIT.2023.3250459
- Z. Lan, Y. Sun, W. Yu, and G. Ge, *Sequence Reconstruction under Channels with Multiple Bursts of Insertions or Deletions*, arXiv:2504.20460 (2025), especially Section IV.B, Lemma IV.19, and Theorem IV.16. https://arxiv.org/abs/2504.20460
