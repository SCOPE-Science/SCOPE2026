# An exact local-motif formula for one length-three palindromic duplication

## Finding

**Theorem (exact descendant count and its mean).** Fix an alphabet \(\Sigma\) of size \(q\ge2\), an integer \(n\ge3\), and a word \(w\in\Sigma^n\). For every \(0\le i\le n-3\), let \(P_i(w)\) be the word obtained by immediately appending the *reversal* of the length-three factor starting at \(i\) after that factor. Write \(\mathcal D_3(w)=\{P_i(w):0\le i\le n-3\}\); only outputs after **exactly one** insertion are counted.

For a finite word pattern \(u\), write \(\operatorname{occ}_u(w)\) for its contiguous occurrence count, allowing overlap. Set
\[
\begin{aligned}
C(w)&=\sum_{a\in\Sigma}\operatorname{occ}_{aaaa}(w),\\
T_3(w)&=\sum_{a\ne b}\operatorname{occ}_{abaaba}(w),\\
T_4(w)&=\sum_{a\ne b}\operatorname{occ}_{baaaaba}(w),\\
T_5(w)&=\sum_{a\ne b}\operatorname{occ}_{bbaabbab}(w).
\end{aligned}
\]
Then the exact formula, valid for every word and every such alphabet, is
\[
\boxed{|\mathcal D_3(w)|=n-2-C(w)-T_3(w)-T_4(w)-T_5(w).}
\]
For independent uniformly distributed letters \(W\in\Sigma^n\), define \(x_+=\max\{x,0\}\). Its expected exact-one sphere size is
\[
\boxed{\mathbb E|\mathcal D_3(W)|=n-2-\frac{n-3}{q^3}-(q-1)\left(\frac{(n-5)_+}{q^5}+\frac{(n-6)_+}{q^6}+\frac{(n-7)_+}{q^7}\right).}
\]
In particular, for \(n\ge8\), the coefficient of \(n\) is \(1-q^{-3}-q^{-4}+q^{-7}\).

## Assumptions and scope

There is no complement operation, no cyclic wraparound, and no restriction on letter multiplicity. The inserted copy has length exactly three and is placed directly after the copied block. All claims concern one application only. Lengths \(n=3,4,5,6,7\) are included, with absent patterns contributing zero. The at-most-one sphere in conventions that include the unchanged word has size \(1+|\mathcal D_3(w)|\), since insertion changes length.

## Proof

**Step 1 — collision equation.** For \(0\le i<j\le n-3\), put \(d=j-i\), \(U=w_iw_{i+1}w_{i+2}\), \(A=U^{\mathrm R}\), \(B=w_{i+3}\cdots w_{j+2}\) (length \(d\)), and \(V=w_jw_{j+1}w_{j+2}\). Cancellation of identical untouched prefixes and suffixes gives
\[
P_i(w)=P_j(w)\quad\Longleftrightarrow\quad AB=BV^{\mathrm R}.
\tag{1}
\]
This equation holds even when the copied factors overlap. At \(d=1\) it reads, in local letters \(x_0x_1x_2x_3\), \((x_2x_1x_0)x_3=x_3(x_3x_2x_1)\); at \(d=2\) it reads \((x_2x_1x_0)(x_3x_4)=(x_3x_4)(x_4x_3x_2)\). In both cases all involved symbols are equal. Conversely constant factors of length four give equal outputs at adjacent sites.

**Step 2 — periodic structure.** Suppose \(d\ge3\). Equation (1) forces \(B\) to be the length-\(d\) prefix of the infinite periodic sequence \(AAA\cdots\): compare the first \(d\) letters of both sides, then the last three. Moreover \(V\), which is the final three letters of \(B\), equals the left cyclic rotation of \(A\) by \(d\) modulo three. Comparing the final three letters in (1) therefore says that this rotation is palindromic. If \(A\) is constant, the whole local interval \(w_i\cdots w_{j+2}\) is constant.

If \(A\) is nonconstant, a length-three word admits a palindromic rotation if and only if exactly two symbols coincide. Exactly one of its three cyclic rotations is palindromic. For \(d\in\{3,4,5\}\), substitution into the periodic structure yields, respectively, precisely the local words
\[
abaaba,\qquad baaaaba,\qquad bbaabbab\qquad(a\ne b).
\tag{2}
\]
Conversely each word in (2) satisfies equation (1), so those patterns yield collisions between sites separated by three, four, and five respectively.

**Step 3 — classify consecutive equal outputs.** Partition all site indices into equivalence classes by the value of \(P_i(w)\), and order each class increasingly. Consider two consecutive indices \(i<j\) in one class. If their local interval is constant, every intervening adjacent pair also gives equal outputs, forcing \(j=i+1\); the interval then contributes one occurrence of \(aaaa\). If the interval is nonconstant, Step 1 rules out gaps one and two. If the gap \(d\ge6\), the periodic structure of Step 2 also yields \(P_i(w)=P_{j-3}(w)\): the shorter length-\(d-3\) periodic block has exactly the same palindromic terminal rotation. This contradicts consecutive membership. Hence \(d\in\{3,4,5\}\), giving a pattern in (2).

Conversely, every collision arising from a pattern in (2) joins *consecutive* indices of its equivalence class: a hypothetical intervening equal output would force either a gap one or two (and hence a constant local interval), or a smaller gap of three or four with a *different* residue modulo three, which would require a second palindromic cyclic rotation of the same nonconstant \(A\). Both possibilities are impossible. Each length-four constant pattern likewise joins consecutive equal indices. Consequently the four pattern counts enumerate, with no repetition, the successive edges of all equal-output classes.

**Step 4 — count and average.** A class with \(r\) indices contributes \(r-1\) such edges; summing over classes shows that the number of distinct outputs is the number \(n-2\) of positions minus the total number of edges. This proves the first boxed formula. For uniform independent letters, a fixed length-four window is constant with probability \(q^{-3}\). For each of the other three motifs, there are exactly \(q(q-1)\) admissible length-\(d+3\) blocks, so its probability is \((q-1)/q^{d+2}\). There are \((n-d-2)_+\) candidate windows. Linearity of expectation proves the second boxed identity without any independence assumption between overlapping windows. Finally, for \(n\ge8\), the slope simplifies using \((q-1)(q^2+q+1)=q^3-1\). \(\square\)

## Verification

The accompanying dependency-free `verify.py` computes each exact-one descendant directly, builds the equivalence classes of duplication sites independently, and checks their consecutive edges against the four motifs. It also enumerates uniform means as exact rational numbers. Exhaustive runs cover all alphabet words for \((q,n)\) with \(q=2,3,4,5\) and \(3\le n\le14,11,9,7\), respectively: 745,596 distinct words in total. Run `python3 verify.py` and expect `PALINDROMIC_LENGTH3_FORMULA_PASS`. This finite regression check corroborates, but does not replace, the infinite proof above.

## Relationship to prior work

Lenz, Wachter-Zeh, and Yaakobi (2017, arXiv:1707.00052, §§3.3 and Appendix 0.A) established equality criteria for two palindromic duplications, exact sphere sizes at lengths one and two, and a general upper bound at larger lengths. Their longer study (arXiv:1712.09345, Appendix B and §3) explicitly notes a length-three nonconstant collision, but still gives an upper bound rather than an exact length-three motif census. The present four-motif classification resolves that collision structure for every input and supplies the exact mean. Yohananov and Schwartz (arXiv:2312.00394) determine asymptotic coding capacity under arbitrarily many duplications, a different statistic and error regime. Sun and Ge (arXiv:2602.01151) primarily consider constructions and redundancy bounds, not this exact-one per-word motif formula. The presence of a general collision equation in the older work is acknowledged as a substantial technical precursor; independence or publication novelty is not claimed as established.

## Limitations

The theorem does not count two or more successive duplications, does not calculate maximum correcting-code cardinalities, and does not assert independence of overlapping collision events. A specialist may find an equivalent statement under a different terminology; the literature comparison is substantial but not logically exhaustive. All proof steps are elementary word combinatorics, with no external theorem used for correctness.

## References

1. Andreas Lenz, Antonia Wachter-Zeh, Eitan Yaakobi, *Bounds on Codes Correcting Tandem and Palindromic Duplications*, arXiv:1707.00052 (first posted 2017-06-30), https://arxiv.org/abs/1707.00052 . Relevant: §3.3 and Appendix 0.A.
2. Andreas Lenz, Antonia Wachter-Zeh, Eitan Yaakobi, *Duplication-Correcting Codes*, arXiv:1712.09345 (first posted 2017-12-24), https://arxiv.org/abs/1712.09345 . Relevant: palindromic spheres and Appendix B.
3. Lev Yohananov, Moshe Schwartz, *On the Coding Capacity of Reverse-Complement and Palindromic Duplication-Correcting Codes*, arXiv:2312.00394 (2023), https://arxiv.org/abs/2312.00394 .
4. Yubo Sun, Gennian Ge, *On the Palindromic/Reverse-Complement Duplication Correcting Codes*, arXiv:2602.01151 (2026), https://arxiv.org/abs/2602.01151 .
