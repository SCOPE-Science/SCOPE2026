# Exactly two perfect six-bit codes for an adjacent-pair deletion

## Finding

For a binary word \(x=x_1x_2x_3x_4x_5x_6\), define its *exact adjacent-pair deletion shadow*
\[
D_2(x)=\{x_1\cdots x_{i-1}x_{i+2}\cdots x_6:1\le i\le5\},
\]
where repeated outputs are counted only once. A binary code \(C\subseteq\{0,1\}^6\) corrects one deletion of exactly two consecutive symbols if \(D_2(x)\cap D_2(z)=\varnothing\) for all distinct \(x,z\in C\).

**Theorem.** Such codes contain at most \(8\) words. Exactly two labeled codes achieve equality:
\[
\begin{aligned}
C_A={}&\{000000,001011,010101,011110,100001,101010,110100,111111\},\\
C_B={}&\{000000,000111,010010,010101,101010,101101,111000,111111\}.
\end{aligned}
\]
Here the six-digit strings are binary words, with leading zeros retained. Both codes are three-dimensional linear subspaces of \(\mathbb F_2^6\), and in each code the deletion shadows partition all \(16\) possible four-bit outputs. Both optima are fixed, as sets, by word reversal and global bit complementation.

## Assumptions and scope

The alphabet is \(\{0,1\}\), the word length is exactly \(6\), and a received word is formed by deleting positions \(i,i+1\) for some \(1\le i\le5\). The burst has exactly two deleted bits; its position is unknown, and there are no substitutions or insertions. A code is any unordered set of distinct input words; linearity is not assumed. “Labeled” means that the six coordinate positions retain their order; no quotient by symmetries is taken in the count of two.

## Proof

**Sharp upper bound.** Let \(T=\{y_1y_2y_3y_4\in\{0,1\}^4:y_2=y_4\}\), so \(\lvert T\rvert=8\). Among the three bits \(x_2,x_4,x_6\), some pair is equal. Deleting one of the three disjoint adjacent position pairs \((1,2),(3,4),(5,6)\) removes the *other* even-indexed bit, so that the two retained even-indexed bits become output positions \(2,4\) and agree. Therefore \(D_2(x)\cap T\neq\varnothing\) for every \(x\in\{0,1\}^6\). Distinct codewords have disjoint shadows, and hence disjoint nonempty intersections with \(T\). Thus \(\lvert C\rvert\le \lvert T\rvert=8\).

**Completeness of the equality census.** If \(\lvert C\rvert=8\), the eight nonempty disjoint sets \(D_2(x)\cap T\), for \(x\in C\), each consist of exactly one element and together exhaust \(T\). Write \(T=(0000,0010,0101,0111,1000,1010,1101,1111)\) in increasing binary order, and define \(B_t=\{x:D_2(x)\cap T=\{t\}\}\). Direct deletion of each of the \(64\) possible six-bit inputs gives this complete list of buckets:

| \(t\) | \(B_t\) |
|---|---|
| \(0000\) | \(000000,000001,000011,000100,010000\) |
| \(0010\) | \(001001,001011,001110,010010\) |
| \(0101\) | \(000101,010001,010100,010101,010110\) |
| \(0111\) | \(000111,011011,011100,011110\) |
| \(1000\) | \(100001,100011,100100,111000\) |
| \(1010\) | \(101001,101010,101011,101110,111010\) |
| \(1101\) | \(101101,110001,110100,110110\) |
| \(1111\) | \(101111,111011,111100,111110,111111\) |

For a fully specified finite enumeration, initialize \(F_0=\{(\varnothing,\varnothing)\}\). Given a pair \((S,U)\in F_j\), for each \(x\in B_{t_{j+1}}\) retain \((S\cup\{x\},U\cup D_2(x))\) in \(F_{j+1}\) precisely when \(U\cap D_2(x)=\varnothing\). No pruning or symmetry quotient is used. The sizes of \(F_0,F_1,\ldots,F_8\), in order, are
\[
1,\ 5,\ 13,\ 28,\ 17,\ 8,\ 11,\ 2,\ 2.
\]
The final two choices are exactly \(C_A,C_B\) above. This is exhaustive: any equality code must choose exactly one candidate in each bucket, and the recursion retains exactly the choices with disjoint shadows.

**Attainment, perfect packing, and structure.** Directly deleting consecutive pairs from the eight words of either displayed code yields pairwise disjoint shadows whose sizes, in sorted codeword order, are \(1,3,1,3,3,1,3,1\) for \(C_A\) and \(1,3,3,1,1,3,3,1\) for \(C_B\). Each sum is \(16\); disjointness therefore proves that the shadows partition all possible four-bit outputs. To check linearity, use three generating words \(001011,010101,100001\) for \(C_A\) and \(000111,010010,101010\) for \(C_B\); their eight binary sums reproduce the displayed sets. Reversing every word or complementing all six bits leaves each set unchanged, as can be checked directly.

## Verification

Run `python3 verify_buckets.py` and `python3 verify_dp.py` from the same directory as this file; both require only Python's standard library. The bucket verifier explicitly constructs all \(64\) shadows, checks the transversal property, evaluates the recurrence above and checks both concrete codes, linearity and symmetry. It outputs `BUCKETS_VERIFY_OK max=8 exact_labeled_optima=2 all_optima_linear=True` and the node counts \(1,5,13,28,17,8,11,2,2\). The independent dynamic-programming verifier processes the \(64\) source words by bitmasks over all \(2^{16}=65536\) occupancy states of the received-word universe, using exact integer counts of optimal partial packings. It outputs `DP_VERIFY_OK max= 8 exact_labeled_optima= 2 states= 65536`. Both were executed successfully from this package's own source files before the finding was reviewed.

## Relationship to prior work

The exact two-adjacent-deletion model, the insertion/deletion equivalence, and the fractional-transversal framework appear in Schoeny, Wachter-Zeh, Gabrys and Yaakobi, *Codes Correcting a Burst of Deletions or Insertions* (arXiv:1602.06820; first submitted 2016-02-22). Their Section IV, Theorem 4 gives the general bound \((2^{n-b+1}-2^b)/(n-2b+1)\), which specializes to \(28/3\) for length \(6\) and burst length \(2\), hence the integer upper bound \(9\); it does not yield the exact value \(8\) or classify equality. The present finite transversal and the equality census are different claims from that general estimate.

Cheng, Swart, Ferreira and Abdel-Ghaffar (ISIT 2014) treat constructions for three or more adjacent deletions, not this length-six two-deletion equality census. Levenshtein's 1967 work supplied early constructions for one or two adjacent losses and asymptotic bounds; existence or asymptotic size is not equivalent to an exhaustive classification of all labeled optima. The possibility of an older unlocated finite census is retained explicitly below.

## Limitations

The theorem is only for exactly two *consecutive* deletions at blocklength six. Neither optimal code corrects arbitrary two deletions; neither even corrects a single deletion: \(001011\) and \(010101\) both yield \(01011\) after one deletion, and \(010010\) and \(010101\) both yield \(01001\). No all-length extremal statement is made. The equality classification uses a finite exhaustive argument with independent exact-code verification, not an externally validated formal proof. Levenshtein's original 1967 article was not accessible in full for a direct line-by-line novelty comparison, so historical priority remains subject to that limited bibliographic risk.

## References

1. C. Schoeny, A. Wachter-Zeh, R. Gabrys, E. Yaakobi, *Codes Correcting a Burst of Deletions or Insertions*, arXiv:1602.06820v1 (submitted 2016-02-22), revised v2 2016-05-12, especially Sections II, III, IV, V and VIII. https://arxiv.org/abs/1602.06820
2. L. Cheng, T. G. Swart, H. C. Ferreira, K. A. S. Abdel-Ghaffar, *Codes for Correcting Three or More Adjacent Deletions or Insertions*, IEEE ISIT 2014, pp. 1246–1250.
3. V. I. Levenshtein, *Asymptotically optimum binary code with correction for losses of one or two adjacent bits*, Problems of Cybernetics 19 (1967), cited in Reference 10 of Schoeny et al. (2016).
