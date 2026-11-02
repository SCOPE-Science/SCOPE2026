# Exact capacity and rigidity of weight-three binary cross-bifix-free codes

## Finding

For every integer \(n\ge4\), the maximum size \(M_n\) of a cross-bifix-free family of binary length-\(n\) words, all having Hamming weight exactly three, is

\[
M_n=\begin{cases}
\frac{3m(m-1)}2,&n=3m,\\
\frac{m(3m-1)}2,&n=3m+1,\\
\frac{m(3m+1)}2,&n=3m+2.
\end{cases}
\]

There is also a complete labeled classification of maximizers. For integers \(n\ge4\) and \(a\ge2\), set

\[
\mathcal F_{n,a}=\bigl\{w\in\{0,1\}^n:\operatorname{supp}(w)=\{i,j,n\},\quad a\le i<j\le n-1,\quad j\ge n+1-a\bigr\},
\]

where positions are indexed from one. All maxima are precisely these families with \(a=m\) or \(m+1\) when \(n=3m\), and \(a=m+1\) in the other two residue classes, together with the reversals of those families (reverse every word). Distinct displayed choices give distinct codebooks. Thus there are exactly four labeled maximizers when \(3\mid n\), and exactly two otherwise.

## Assumptions and scope

A family \(\mathcal C\subseteq\{0,1\}^n\) is *cross-bifix-free* (also called *non-overlapping*) if, for all \(x,y\in\mathcal C\), including \(x=y\), and every integer \(1\le\ell<n\), the length-\(\ell\) prefix of \(x\) differs from the length-\(\ell\) suffix of \(y\). The codewords are distinct, uniformly length \(n\), and have exactly three ones. Words are labeled by their absolute coordinate positions; no quotient by permutations or cyclic shifts is taken. Only simultaneous reversal is a named symmetry. No claims are made about optimum unrestricted-composition code sizes or coding distance.

## Proof

**1. Endpoint orientation.** For any codeword, the first bit differs from its last bit; otherwise a proper prefix and suffix of length one coincide. If the family had words of both endpoint orientations, the first bit of one would equal the last bit of the other. Hence all words share the same orientation. Reversing every word if necessary, suppose the first position is zero and the last is one. Then every word has exactly two interior ones in positions \(2\le i<j\le n-1\), so identify the word with its ordered pair \((i,j)\).

**2. Exact cross-bifix criterion.** For a nonempty family \(\mathcal C\) in this orientation define

\[
a=\min_{(i,j)\in\mathcal C}i,\qquad b=\min_{(i,j)\in\mathcal C}j.
\]

We show

\[
\mathcal C\text{ is cross-bifix-free}\quad\Longleftrightarrow\quad a+b>n.
\]

If \(a+b\le n\), choose a word \(x\) with its first interior one at position \(a\) and a word \(y\) with its second interior one at position \(b\). The prefix of \(x\) of length \(a\) is \(0^{a-1}1\). Since the second interior one of \(y\) is at or before position \(n-a\), the suffix of \(y\) of length \(a\) is also \(0^{a-1}1\). Their equality contradicts the required condition.

Conversely suppose \(a+b>n\). Any proper prefix that matches a suffix must end in one, because every suffix ends in one. Such a proper prefix terminates at either the first or the second interior one. For a prefix ending at position \(i_x\), it contains exactly one one. But for every \(y\in\mathcal C\), its suffix of length \(i_x\) contains its second interior one and its final one: indeed \(j_y\ge b>n-a\ge n-i_x\). For a prefix ending at position \(j_x\), it contains exactly two ones. The corresponding suffix of any \(y\) contains *three* ones because \(i_y\ge a>n-b\ge n-j_x\). In both cases, counts disagree. All other prefixes end in zero and cannot match a suffix. This proves sufficiency, including self-overlaps.

**3. Threshold capacity.** For any valid family with minimum first interior position \(a\), its minimum second interior position satisfies \(b\ge n+1-a\). Therefore it is contained in the full threshold family \(\mathcal F_{n,a}\). Conversely the minimum positions in every nonempty \(\mathcal F_{n,a}\) with \(2\le a\le\lfloor n/2\rfloor\) satisfy the criterion, so that family is valid. Counting first interior positions at each allowable second interior position gives

\[
|\mathcal F_{n,a}|=\sum_{j=n+1-a}^{n-1}(j-a)=\frac{(a-1)(2n-3a)}2,\qquad 2\le a\le\lfloor n/2\rfloor.
\]

For \(a>\lfloor n/2\rfloor\), a valid family is a strict subset of \(\mathcal F_{n,\lfloor n/2\rfloor}\) (the latter also contains words whose first interior one occurs earlier). It cannot maximize cardinality. Thus the optimum is the maximum of this displayed quadratic over the indicated integer interval.

**4. Maximizers and rigidity.** The concave quadratic has real vertex \(a=(2n+3)/6=n/3+1/2\). If \(n=3m\), the two adjacent integers \(m\) and \(m+1\) tie, and if \(n=3m+1\) or \(3m+2\) the unique integer maximizer is \(m+1\). These indices are in the allowed interval for the stated domain, except that the unneeded \(m\) when \(n=4,5\) is outside the candidate list. Direct substitution yields the three formulas. A family attaining the bound must contain every eligible pair in its containing threshold family; omitting any word strictly decreases its size. Therefore the named threshold families are all the oriented maximizers, and reversing them gives the remaining orientation. The two orientations are disjoint, and the tied threshold families for \(3\mid n\) differ, proving the enumeration of all labeled maxima.

## Verification

The accompanying `verify.py` is standalone Python using only the standard library. Execute `python3 verify.py`. It directly tests all ordered pairs against literal prefix/suffix matches, checks the exact two-index criterion for every pair of oriented words at lengths \(4\) through \(21\), checks every constructed threshold family through length \(30\), and enumerates every subset of admissible oriented codewords at lengths \(4\) through \(9\). It confirms optimal sizes \(1,2,3,5,7,9\) for these six lengths, with \(1,1,2,1,1,2\) oriented maximum families, respectively. The verifier tests finite instances only; the unrestricted-length assertion relies on the proof above.

## Relationship to prior work

Cross-bifix-free or non-overlapping word families and their unrestricted size are extensively studied. Wang and Wang's generating-function analysis of \(q\)-ary non-overlapping codes (arXiv:2108.06934, first posted 2021-08-16) studies general constructions, while Qin, Chen and Luo's non-expandability work (arXiv:2309.08915, first posted 2023-09-16) analyzes expansion properties of specific families. Wang and Wang's later study (arXiv:2402.18896, first posted 2024-02-29) treats variable-length code capacity. The present finding imposes *exactly three ones in every fixed-length binary codeword* and determines both the optimum and every labeled maximizer, rather than unrestricted code size or maximality under addition of words. It is not asserted that the first two general works contain no implicit derivation of the theorem.

## Limitations

The method directly uses the fact that a weight-three word with fixed endpoint orientation has precisely two interior ones. It neither solves the analogous fixed-weight-four problem nor the unrestricted binary non-overlapping coding problem. No external independent scientific validation was performed. A differently named or poorly indexed formulation of this special constant-weight optimum may exist; novelty is assessed relative to the inspected primary material, not guaranteed by unsuccessful search.

## References

1. Wang and Wang, *Q-ary non-overlapping codes: a generating function approach*, arXiv:2108.06934, https://arxiv.org/abs/2108.06934 (initial public posting 2021-08-16).
2. Qin, Chen and Luo, *On non-expandable cross-bifix-free codes*, arXiv:2309.08915, https://arxiv.org/abs/2309.08915 (initial public posting 2023-09-16).
3. Wang and Wang, *On the maximum size of variable-length non-overlapping codes*, arXiv:2402.18896, https://arxiv.org/abs/2402.18896 (initial public posting 2024-02-29).
4. Chee, Kiah, Purkayastha and Wang, *Cross-bifix-free codes within a constant factor of optimality*, arXiv:1209.0236, https://arxiv.org/abs/1209.0236 (general background, not the dating source).
