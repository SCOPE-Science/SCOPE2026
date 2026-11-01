# Sharp length-32 cutoff for ternary \(9/10\)-synchronization strings

## Finding
Let \(\Sigma\) be an alphabet with at most three symbols. For nonempty consecutive factors \(X=S[i:j]\) and \(Y=S[j:k]\), put \(L=|X|+|Y|\) and let \(\operatorname{LCS}(X,Y)\) denote the longest common subsequence length. A finite word is a strict \(9/10\)-synchronization string precisely when
\[
20\operatorname{LCS}(X,Y)<9L
\]
for every \(0\le i<j<k\le |S|\), where indices are zero-based and slices are half-open.

**Theorem.** Over three letters, such a word of length \(n\) exists if and only if \(1\le n\le32\). Every word of length \(33\) already has adjacent factors satisfying the *strict opposite* inequality
\[
20\operatorname{LCS}(X,Y)>9L.
\]
One explicit strict witness at the sharp attainable length is the word `01020120212012101201020120212012`. More generally, arbitrary-length ternary \(\varepsilon\)-synchronization strings can exist only for \(\varepsilon>9/10\).

## Assumptions and scope
The alphabet is a set of at most three abstract labels, and arbitrary relabeling of the alphabet leaves the condition invariant. The insertion–deletion edit distance is
\[\operatorname{ED}_{\mathrm{ID}}(X,Y)=|X|+|Y|-2\operatorname{LCS}(X,Y).\]
Hence the defining strict synchronization inequality \(\operatorname{ED}_{\mathrm{ID}}(X,Y)>(1-\varepsilon)(|X|+|Y|)\) is equivalent to \(2\operatorname{LCS}(X,Y)<\varepsilon(|X|+|Y|)\). The theorem uses all pairs of adjacent nonempty factors, including unequal-length factors. This is different from testing only equal-length adjacent factors.

## Proof
**Canonical representatives.** Relabel the first symbol to `0`. When scanning left to right, each newly encountered symbol receives the next unused digit. A canonical word is therefore a restricted-growth word over `0`,`1`,`2`: from a prefix whose largest digit is \(m\), the next digit can be any integer from \(0\) through \(\min(2,m+1)\). Every ternary word has exactly one such representative, and all longest-common-subsequence values are invariant under its global relabeling.

**Prefix recurrence.** Let \(A_n\) be the set of canonical words of length \(n\) obeying the *weak* requirement
\[
20\operatorname{LCS}(S[i:j],S[j:k])\le9(k-i)
\quad\text{for every }0\le i<j<k\le n.
\]
Initialize \(A_1=\{0\}\). Obtain \(A_{n+1}\) by appending each allowed next digit to each word of \(A_n\), retaining it exactly if all newly completed adjacent pairs with right endpoint \(n+1\) pass the inequality. The previously completed pairs pass automatically, so this recurrence examines every canonical admissible word exactly once, without heuristic pruning.

**Exact finite exhaustion.** The attached `verify_exact.py` implements the recurrence with integer arithmetic and ordinary dynamic-programming LCS. It obtains \(|A_{32}|=10\) and \(|A_{33}|=0\). Its `exact_certificate.json` lists every one of the ten length-\(32\) canonical survivors and every one of their thirty possible length-\(33\) extensions, together with an explicit failing split \((i,j,33)\) and its LCS length. An independent bit-parallel LCS implementation in `verify_independent.py` recomputes all cardinalities for lengths \(1\) through \(33\) and obtains identical counts. No floating-point comparison occurs in either test.

Every ternary length-\(33\) word has a canonical representative. Were that representative weakly admissible, the recurrence would include it in \(A_{33}\), contradicting the certified empty level. Thus every such word has a pair with strict inequality \(20\operatorname{LCS}>9L\). Every longer word contains a length-\(33\) prefix and inherits the same obstruction.

**Sharpness.** For `01020120212012101201020120212012`, the exhaustive integer test over all adjacent nonempty factors and all right endpoints gives a minimum value of \(9L-20\operatorname{LCS}(X,Y)\) equal to \(1\), which is strictly positive. Every prefix of the witness therefore satisfies the strict condition. This proves existence for all lengths \(1\) through \(32\), completing the iff assertion.

## Verification
From the directory containing the four named artifacts, run `python3 verify_exact.py > exact_certificate.json` and `python3 verify_independent.py > independent_output.json`. Compare `canonical_counts` in the resulting JSON files and check that the level-\(33\) count is zero, that the level-\(32\) survivor list has ten entries, and that all thirty listed extensions carry valid strict-violation witnesses. The independent checker also directly checks the explicit strict length-\(32\) word. No random sampling, numerical tolerances, computational timeout or infinite experimental extrapolation is involved. The mathematical reduction from all words to the finite search tree is given above.

## Relationship to prior work
Xu, Fu, Qiao and Tao (first posted September 3, 2026) proved ternary synchronization strings exist for all lengths when \(\varepsilon>226/227\), and state that the optimal ternary parameter remains open. This result goes in the opposite direction: it is a finite obstruction at \(\varepsilon=9/10\), not a competing construction.

Camungol and Rampersad (arXiv 2013, published 2016) studied the LCS similarity of **equal-length** adjacent blocks. Their Table 1 reports a ternary unavoidability threshold below approximately \(0.888\), while the putative attainable side below approximately \(0.901\) is labeled conjectural. Their conditions differ from the all-unequal-length synchronization definition used here, and neither their lower threshold nor the newer construction establishes this exact length-\(32\)/\(33\) transition. Existing bounds and the exact obstruction are not interchangeable.

## Limitations
The result does not determine the optimal ternary parameter for arbitrarily long words, nor exhibit an infinite ternary string for any parameter near the new necessary bound. The sharp length cutoff is only asserted for the specific strict \(9/10\) condition. The finite exhaustive step is independently implemented and is reproducible, but not independently audited by an external mathematician. Coverage by an earlier unindexed exhaustive obstruction remains a priority risk.

## References
1. H. Xu, S. Fu, Y. Qiao, and D. Tao, *Synchronization Strings over the Optimal Alphabet*, arXiv:2609.04122, initially posted September 3, 2026, https://arxiv.org/abs/2609.04122.
2. S. Camungol and N. Rampersad, *Avoiding approximate repetitions with respect to the longest common subsequence distance*, arXiv:1308.1620, initially posted August 7, 2013; *Involve* 9 (2016), 657–666, https://arxiv.org/abs/1308.1620.
