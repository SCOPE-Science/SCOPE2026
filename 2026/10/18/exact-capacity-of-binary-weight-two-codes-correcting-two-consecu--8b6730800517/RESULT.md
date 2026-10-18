# Exact capacity of binary weight-two codes correcting two consecutive deletions

## Finding

For a binary block of length \(n\), write \(\mathcal B_2(w)\) for the set of words obtained by deleting **exactly two adjacent symbols**. Restrict all codewords to have Hamming weight two, and let \(M_{n,2}^{\mathrm{bd}}\) denote the largest cardinality of a code whose distinct members have disjoint \(\mathcal B_2\)-sets.

**Theorem.** For every integer \(n\ge3\),
\[
M_{n,2}^{\mathrm{bd}}=\left\lfloor\frac{3(n-1)}4\right\rfloor.
\]
For the boundary case \(n=2\), the optimum is \(M_{2,2}^{\mathrm{bd}}=1\).

Write a weight-two word as \([i,j]_n\), where its ones occupy zero-based positions \(0\le i<j<n\). The following code attains equality for every \(n\ge3\):
\[
\mathcal C_n=\{[0,1]_n\}\cup
\bigcup_{r\ge0}\{[4r+1,4r+3]_n,\ [4r+2,4r+4]_n,\ [4r+3,4r+6]_n\},
\]
where a pair is retained only if **both** of its coordinates lie in \(\{0,\ldots,n-1\}\).

## Assumptions and scope

The alphabet is exactly \(\{0,1\}\). The input length \(n\) is known, every input has exactly two ones, and the channel deletes **one contiguous block of two positions**; it does not delete two arbitrary nonadjacent positions. A code corrects this channel when its sets of *distinct* possible length-\(n-2\) outputs are pairwise disjoint. There is no restriction on computational complexity of decoding. No statement is made about variable-length bursts, multiple independent bursts, or other fixed weights.

## Proof

**Upper bound.** Fix \(n\ge3\) and put \(m=n-2\). Classify each codeword \([i,j]_n\) by the gap \(j-i\): adjacent (gap one), near (gap two), or far (gap at least three). Let their respective numbers in an arbitrary valid code be \(a,t,e\).

All adjacent pairs share the all-zero length-\(m\) descendant, obtained by deleting both ones; hence \(a\le1\). Every adjacent pair has at least one descendant of Hamming weight one (possible because \(n\ge3\)); each near pair has the unique weight-one descendant whose one is at position \(i\); and each far pair has **two distinct** weight-one descendants, whose ones are at positions \(i\) and \(j-2\). These statements follow directly by deleting a burst that contains one of the two ones but not the other. The length-\(m\) output alphabet has only \(m\) different weight-one words. As different codewords may not share any output,
\[
a+t+2e\le m.\tag{1}
\]

A second restriction concerns near pairs. For each \(0\le i\le m-3\), the two candidate codewords \([i,i+2]_n\) and \([i+2,i+4]_n\) have the *same weight-two descendant*: the pair of ones at output positions \((i,i+2)\). Indeed, delete the two zeros immediately after the second one in the first word, or the two zeros immediately before the first one in the second word. The inequalities on \(i\) guarantee all positions exist. Thus the allowed starts of near codewords form an independent set in the graph on vertices \(\{0,\ldots,m-1\}\) with edges joining vertices at distance two. This graph is exactly two disjoint paths of sizes \(\lceil m/2\rceil\) and \(\lfloor m/2\rfloor\). Its independence number is
\[
\alpha(m)=\left\lceil\frac{\lceil m/2\rceil}{2}\right\rceil+
\left\lceil\frac{\lfloor m/2\rfloor}{2}\right\rceil.
\]
Consequently \(t\le\alpha(m)\). Combining this with (1) and \(a\le1\),
\[
2|\mathcal C|=(a+t+2e)+(a+t)
\le m+\alpha(m)+1.
\]
An evaluation for the four residue classes of \(m\) modulo four gives
\[
|\mathcal C|\le\left\lfloor\frac{m+\alpha(m)+1}{2}\right\rfloor
=\left\lfloor\frac{3(m+1)}4\right\rfloor
=\left\lfloor\frac{3(n-1)}4\right\rfloor.\tag{2}
\]

**Achievability.** Use the explicit \(\mathcal C_n\) above. Only \([0,1]_n\) has adjacent ones, so only it can yield an all-zero output. A burst deleting exactly one one produces a weight-one word. For \([0,1]_n\), its surviving one can only be at output position \(0\); for the three families indexed by \(r\), the possible surviving-one positions are, respectively,
\[
\{4r+1\},\qquad\{4r+2\},\qquad\{4r+3,4r+4\}.
\]
These sets are mutually disjoint as \(r\) varies, including disjointness from \(\{0\}\).

It remains to rule out collisions between weight-two outputs, arising when the deleted burst comprises two zeros. A burst containing no ones must be wholly before the first one, strictly between the two ones, or wholly after the second. With the ordered pair of surviving-one positions reduced modulo four, the possibilities are:

| Source pair family | Possible output residue pairs modulo four |
| --- | --- |
| \([0,1]_n\) | \((0,1)\) |
| \([4r+1,4r+3]_n\) | \((3,1),(1,3)\) |
| \([4r+2,4r+4]_n\) | \((0,2),(2,0)\) |
| \([4r+3,4r+6]_n\) | \((1,0),(3,0),(3,2)\) |

A particular deletion option is absent when the relevant pair of zero positions lies outside the word; this only removes possible outputs. All eight residue patterns are distinct. Within any single family and residue pattern, output coordinates increase by four when \(r\) increases by one, so identical descendants cannot arise from different source words. Thus the entire construction has pairwise disjoint burst-deletion balls.

The code sizes for lengths \(n=3,4,5,6\) are \(1,2,3,3\), respectively. Each increase \(n\mapsto n+4\) admits precisely three additional candidate pairs from the displayed families. Hence \(|\mathcal C_n|=\lfloor3(n-1)/4\rfloor\) for every \(n\ge3\), matching (2). At \(n=2\), the unique weight-two input yields the singleton code. This completes the proof.

## Verification

The accompanying `checker.py` forms every actual length-two burst descendant from the bit positions, checks pairwise disjointness and the claimed size for every length from \(3\) through \(300\), and independently tests the near/far weight-one-output assertions and all prohibited near-pair overlaps through length \(34\). These finite checks serve as reproducibility checks; the all-length result is the preceding proof. Run with `python checker.py` from the extracted package directory.

## Relationship to prior work

Wang, Sima and Farnoud (ISIT 2021; a relevant public presentation on July 19, 2021) study codes correcting bursts of up to two deletions, and Wang and collaborators' 2022 expanded treatment gives general unrestricted-alphabet constructions. Schoeny, Wachter-Zeh, Gabrys and Yaakobi study unrestricted binary burst-deletion codes and bounds. Cullina, Kulkarni and Kiyavash give constant-weight graph methods for ordinary deletion channels. These frameworks motivate the precise restriction considered here; their inspected statements do not give the all-length exact optimum for **binary Hamming weight two and an exact adjacent two-deletion burst**. In particular, arbitrary single-deletion and arbitrary two-deletion channel constraints are different from the exact adjacent-two-deletion constraint. This is a statement-by-statement comparison, not a claim that searches can prove global novelty.

## Limitations

The theorem characterizes only weight-two binary codes under one exactly-two-position contiguous deletion. It does not characterize all optimal codes, decoder efficiency, other fixed weights, multiple burst events, or the variable-length-burst channel. Literature under different terminology, and any uninspected portions of related papers, remain originality risks. Neither a finite experiment nor the absence of an exact database match proves novelty.

## References

1. S. Wang, J. Sima, F. Farnoud, *Non-binary Codes for Correcting a Burst of at Most 2 Deletions*, IEEE ISIT (2021), pp. 2804–2809, DOI: `10.1109/ISIT45174.2021.9517917`. Presentation listed in https://2021.ieee-isit.org/TechnicalProgram.asp (July 19, 2021).
2. S. Wang, Y. Tang, J. Sima, R. Gabrys, F. Farnoud, *Non-binary Codes for Correcting a Burst of at Most t Deletions*, arXiv:2210.11818v1 (October 21, 2022), https://arxiv.org/abs/2210.11818.
3. C. Schoeny, A. Wachter-Zeh, R. Gabrys, E. Yaakobi, *Codes Correcting a Burst of Deletions or Insertions*, arXiv:1602.06820, https://arxiv.org/abs/1602.06820.
4. D. Cullina, A. A. Kulkarni, N. Kiyavash, *Two Approaches to the Construction of Deletion Correcting Codes: Weight Partitioning and Optimal Colorings*, arXiv:1211.4056, https://arxiv.org/abs/1211.4056.
