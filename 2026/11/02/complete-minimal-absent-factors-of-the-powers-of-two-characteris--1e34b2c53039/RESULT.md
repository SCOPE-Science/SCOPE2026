# Complete minimal absent factors of the powers-of-two characteristic word

## Finding

Let \(c=c_0c_1\cdots\) be the binary word defined by \(c_n=1\) exactly when \(n=2^j-1\) for some integer \(j\geq0\), with zero-based indexing. A finite binary word is a *factor* if it occurs contiguously in \(c\), and is a *minimal absent factor* if it is absent but every proper contiguous factor occurs.

For each integer \(g\geq1\), put
\[
H_g=1\,0^{g-1}1,\quad \lambda_g=\begin{cases}0&g=1,\\g/2-1&g\geq2\text{ and }g\text{ is a power of two}.
\end{cases}
\]
For powers of two \(g\), write \(L_g=0^{\lambda_g+1}H_g\) and \(R_g=H_g0^{2g}\). Then the *entire* minimal-absent-factor set is
\[
\boxed{\mathcal M(c)=\{111\}\ \cup\ \{H_g:g\geq1,\ g\text{ is not a power of two}\}\ \cup\ \{L_g,R_g:g\text{ is a power of two}\}.}
\]
In particular, every member except \(111\) has precisely two ones. Its exact length-generating series is
\[
\boxed{F(z)=\sum_{v\in\mathcal M(c)}z^{|v|}=\frac{z^2}{1-z}-\sum_{j\geq0}z^{2^j+1}+2z^3+2\sum_{j\geq0}z^{3\cdot2^j+1}.}
\]
The coefficient at length \(n\geq2\) is
\[
\mathbf1_{n-1\text{ is not a power of two}}+2\mathbf1_{n=3}+2\mathbf1_{n-1=3\cdot2^j\text{ for some }j\geq0}.
\]
There are no minimal absent factors of lengths \(1\), \(2\), \(5\), or \(2^j+1\) for \(j\geq3\), while the lengths \(3\cdot2^j+1\) have precisely three.

## Assumptions and scope

The alphabet is exactly \(\{0,1\}\). Factor means contiguous substring, **not** a scattered subsequence. The word is right-infinite and begins with \(11\); a prefix-end marker is not added. The formula concerns its full infinite factor language, not the minimal absent factors of an arbitrary finite prefix. Integer powers of two include \(1\). The special value \(\lambda_1=0\) records the left endpoint of \(c\).

## Proof

**Gap lemma.** The one-positions are \(2^j-1\) for \(j\geq0\), so the successive gaps between ones are \(1,2,4,8,\ldots\), each occurring once. If two successive ones have distance \(g=2^j\), the source factor \(H_g\) occurs exactly once, with its first one at index \(g-1\). The number of consecutive zeros immediately preceding its first one equals \(\lambda_g\), and the number immediately following its second one is \(2g-1\). All factors with at most one one occur, since the neighboring zero gaps around ones become arbitrarily long. Pure-zero factors also occur at every length.

**Every listed word is minimal absent.** If \(g\) is not a power of two, the factor \(H_g\) is absent by the gap lemma. Removing either end leaves a factor with one one, hence both maximal proper factors occur. If \(g\) is a power of two, \(L_g\) is absent because the unique \(H_g\) has only \(\lambda_g\) preceding zeros. Removing its first zero gives \(0^{\lambda_g}H_g\), which occurs; removing its last one gives a factor with one one, which also occurs. Likewise \(R_g\) is absent because \(H_g\) has only \(2g-1\) following zeros; removing its last zero gives an occurring factor, while removing its first one leaves a factor with one one. Finally \(111\) is absent, whereas both of its length-two proper factors equal \(11\), which occurs at the beginning. Factoriality means it suffices to verify the two maximal proper factors.

**The list is complete.** Take any binary word \(u\) containing none of the displayed words as a factor. If it has at most one one, it occurs. Otherwise, let \(g_1,\ldots,g_t\) be the positive distances between consecutive ones in \(u\), and let \(a,b\) be its numbers of zeros preceding its first one and following its last one. Every \(g_i\) must be a power of two: otherwise \(H_{g_i}\) occurs inside \(u\). The absence of \(L_{g_1}\) and \(R_{g_t}\) forces \(a\leq\lambda_{g_1}\) and \(b\leq2g_t-1\).

For any consecutive gaps \(d=g_i\) and \(e=g_{i+1}\), both powers of two, we prove \(e=2d\). If \(e>2d\), the region after the pair at distance \(d\) contains at least \(2d\) zeros, giving the forbidden \(R_d\). If \(e<2d\) and \(e\geq2\), power-of-two divisibility implies \(d\geq e\), and the \(d-1\) zeros immediately before the middle one contain at least \(e/2\) zeros, giving the forbidden \(L_e\). If \(e=1<2d\), then \(d=1\) produces \(111\), whereas \(d\geq2\) produces \(011=L_1\). Each case contradicts avoidance. Hence every later gap doubles the preceding one.

Thus the ones of \(u\) have precisely the same gap sequence as the uniquely placed consecutive ones of \(c\) starting with gap \(g_1\). Their surrounding zero runs accommodate \(a\) and \(b\) by the bounds above. Consequently \(u\) occurs. Every absent word therefore contains a displayed absent factor; if it is minimal absent, it equals one of them. This proves the classification.

**Length census.** The non-power gaps contribute one word at length \(g+1\), except when \(g\) is a power of two. The exceptional \(111\) and \(L_1\) both have length three. For \(g=2^j\), the right-boundary word \(R_g\) has length \(3\cdot2^j+1\); for \(j\geq1\), the left-boundary word \(L_{2^j}\) has length \(3\cdot2^{j-1}+1\). Summing these disjoint families produces the generating series and coefficient formula.

## Verification

The bundled `verify.py` constructs a finite prefix of length \(2^{15}\). It compares, at every length through \(40\), the predicted minimal-absent-word set against the direct difference of observed factor sets, independently enumerates all binary words through length \(12\) for membership-versus-avoidance checks, and compares the coefficient formula against the explicit family enumeration. Execute `python3 verify.py`; its successful output begins with `VERIFY_OK`. These finite checks test the proof and implementation but do **not** prove the infinite classification.

## Relationship to prior work

Ayad, Badkobeh, Fici, Héliou and Pissis study antidictionary computation for finite texts and give the standard factorial-language definition. Inenaga, Mieno, Arimura, Funakoshi and Fujishige relate minimal absent words of finite strings to compact DAWGs and extended bispecial factors. Neither inspected work specifies the infinite powers-of-two characteristic word or the formula above. This result instead characterizes every forbidden factor of an explicit nonrecurrent automatic word and gives its exact length distribution.

## Limitations

This is a classification of the infinite factor language only. It does not give a finite-prefix MAW count, occurrence frequencies, or a universal bound for general automatic words. Equivalent presentations in unindexed literature remain possible; no independent audit has been performed.

## References

- L. A. K. Ayad, G. Badkobeh, G. Fici, A. Héliou and S. P. Pissis, *Constructing Antidictionaries of Long Texts in Output-Sensitive Space*, Theory of Computing Systems 65 (2021), 777–797. Published online December 14, 2020. https://doi.org/10.1007/s00224-020-10018-5
- S. Inenaga, T. Mieno, H. Arimura, M. Funakoshi and Y. Fujishige, *Computing Minimal Absent Words and Extended Bispecial Factors with CDAWG Space*, arXiv:2402.18090, first posted February 28, 2024. https://arxiv.org/abs/2402.18090
