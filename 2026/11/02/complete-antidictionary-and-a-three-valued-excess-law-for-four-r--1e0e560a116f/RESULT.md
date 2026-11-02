# Complete antidictionary and a three-valued excess law for four-run binary words

## Finding

Let \(a,b,c,d\) be arbitrary positive integers and put \(W=0^a1^b0^c1^d\), with alphabet exactly \(\{0,1\}\). A *minimal absent word* is a nonempty binary word absent as a contiguous factor of \(W\), every proper contiguous factor of which occurs in \(W\). The complete set \(\mathcal A(W)\) consists of the following ten disjoint families (empty conditional families are omitted):

1. The two unary words \(0^{\max(a,c)+1}\) and \(1^{\max(b,d)+1}\).
2. \(01^t0\), for each integer \(1\le t<b\).
3. \(10^t1\), for each integer \(1\le t<c\).
4. \(1^{b+1}0\), precisely when \(b<d\).
5. \(10^{c+1}\), precisely when \(c<a\).
6. \(0^{\min(a,c)+1}1^{\min(b,d)+1}\), precisely when \((a-c)(b-d)<0\).
7. \(0^{a+1}1^b0\), precisely when \(a<c\) and \(b\le d\).
8. \(10^c1^{d+1}\), precisely when \(c\le a\) and \(d<b\).
9. \(10^c1^b0\), precisely when \(c\le a\) and \(b\le d\).

Here the unary pair is one family, so the displayed numbering identifies nine grouped cases. Every word in the list is distinct from every other word in the list; each condition is necessary and sufficient. Consequently the *full length spectrum* is the polynomial
\[
\begin{aligned}
H_{a,b,c,d}(z)={}&z^{\max(a,c)+1}+z^{\max(b,d)+1}
 +\sum_{t=1}^{b-1}z^{t+2}+\sum_{t=1}^{c-1}z^{t+2}\\
&+\mathbf 1_{b<d}z^{b+2}+\mathbf 1_{c<a}z^{c+2}
+\mathbf 1_{(a-c)(b-d)<0}z^{\min(a,c)+\min(b,d)+2}\\
&+\mathbf 1_{a<c,\,b\le d}z^{a+b+2}
+\mathbf 1_{c\le a,\,d<b}z^{c+d+2}
+\mathbf 1_{c\le a,\,b\le d}z^{b+c+2}.
\end{aligned}
\]
In particular, the number \(M(W)=H_{a,b,c,d}(1)\) follows a sharp *three-valued excess law*:
\[
\boxed{
M(W)=b+c+\begin{cases}
4,&a>c\text{ and }b<d,\\
1,&a\le c\text{ and }b\ge d,\\
2,&\text{otherwise}.
\end{cases}}
\]
Thus the excess above the sum of the two interior run lengths is never three, even though all values one, two, and four occur. For example, the tuples \((a,b,c,d)=(2,2,2,2),(1,2,3,4),(2,1,1,2)\) realize the three cases.

## Assumptions and scope

The assertion is for four *nonempty* maximal alternating runs, with starting symbol zero and ending symbol one. Complementing all bits gives the identical formulas for words that start with one. The alphabet is restricted to the two symbols that occur; a larger ambient alphabet would add absent single-letter words. Substrings are contiguous and are not scattered subsequences. \(H_{a,b,c,d}(z)\) counts *distinct word values* (not occurrences); the coefficient of \(z^\ell\) is the number of minimal absent words of length \(\ell\). All inequalities refer to integers and include equality exactly as written.

## Proof

**The local criterion.** Let \(u\) be a binary word of length at least two. Then \(u\) is minimal absent exactly when \(u\) is absent and its prefix and suffix of length \(|u|-1\) both occur. Indeed, any shorter contiguous factor belongs to at least one of those two proper factors. Both letters appear in \(W\), so no length-one word is absent. We shall apply this criterion repeatedly.

**Factors by run type.** Every nonconstant factor has one of the following run patterns. A factor with one change from zero to one, \(0^i1^j\), occurs exactly when \((i\le a,\,j\le b)\) or \((i\le c,\,j\le d)\). A factor \(1^i0^j\) occurs exactly when \(i\le b\) and \(j\le c\). A factor with two changes \(0^i1^j0^h\) occurs exactly when \(i\le a,\,j=b,\,h\le c\); a factor \(1^i0^j1^h\) occurs exactly when \(i\le b,\,j=c,\,h\le d\). A factor with three changes is necessarily \(0^i1^b0^c1^h\) with \(i\le a,\,h\le d\). No factor has more than three changes. These equivalences follow by checking which entire middle runs a contiguous factor must cross.

**No changes.** Among unary words, exactly the two listed run-overflow words have occurring length-one-shorter factors and are absent.

**One change.** For \(1^i0^j\), the occurrence region is the rectangle \(1\le i\le b,\,1\le j\le c\). Its only possible minimally excluded points are \((b+1,1)\) and \((1,c+1)\): in the first case deleting the last letter leaves an occurring factor, while deleting the first leaves the unary \(1^{b+1}\), which occurs exactly if \(d>b\). In the second case the unary \(0^{c+1}\) occurs exactly if \(a>c\). There is no mixed-corner candidate because at a point outside both bounds the prefix or suffix is already absent. This proves families 4 and 5.

For \(0^i1^j\), the occurrence region is the union of the two lower-left rectangles with opposite corners \((a,b)\) and \((c,d)\). No point with \(i=1\) or \(j=1\) is minimally excluded, because the necessary unary proper factor imposes the corresponding largest run bound. For \(i,j\ge2\), deletion of either endpoint reduces respectively \(i\) or \(j\) by one. If the rectangles are nested, there is no minimally excluded point of this kind. If their corners are incomparable, there is exactly one, \((i,j)=(\min(a,c)+1,\min(b,d)+1)\). It is inside the bounding unary limits, and the two decremented points fall into the two different rectangles. This proves family 6.

**Two changes.** Consider \(0^i1^j0^h\). If \(j<b\), this is absent, and both proper length-one-shorter factors occur only when the first and last runs are singletons: the word is \(01^j0\), giving family 2. If \(j>b\), its suffix \(1^j0^h\), or the corresponding shortened version when \(i>1\), cannot occur, so it is not minimal absent. For \(j=b\), occurrence requires \(i\le a\) and \(h\le c\). The prefix-suffix criterion excludes \(h>c\); the only way to be minimally absent is \(h=1\) and \(i=a+1\). The shorter suffix then occurs at the first \(010\) boundaries, while the shorter prefix must occur at the second \(01\) boundary. This is possible exactly if \(a<c\) and \(b\le d\), proving family 7. Reversing the word and complementing the letters sends the parameter quadruple to \((d,c,b,a)\) and converts this argument to the type \(1^i0^j1^h\). It gives family 3 for \(j<c\) and the additional word \(10^c1^{d+1}\) exactly when \(c\le a\), \(d<b\), giving family 8.

**Three changes.** A word beginning with zero has the form \(0^i1^j0^h1^r\). The occurring shortened prefix forces the first \(01\) and \(10\) transitions to cross the complete \(1^b\) run, unless it retains the final \(1\) run; either way combining the shortened prefix and suffix forces \(j=b\), \(h=c\), \(i\le a\), and \(r\le d\). Consequently the whole word occurs and is not absent. A word beginning with one has the form \(1^i0^j1^h0^r\) and cannot occur as a factor at all. If either end run has length more than one, one of its proper prefix and suffix still has three changes starting with one, so also cannot occur. Thus necessarily \(i=r=1\). The prefix \(10^j1^h\) occurs if and only if \(j=c\), \(h\le d\); the suffix \(0^j1^h0\) occurs if and only if \(h=b\), \(j\le a\). They coexist exactly when \(j=c\le a\), \(h=b\le d\). This gives family 9, \(10^c1^b0\).

**Four or more changes.** If a minimal absent word has at least four changes, deleting either endpoint must leave a factor with at most three changes. Hence there must be exactly four changes and both end runs must have length one. But then one of the shortened prefix or suffix starts with one and has three changes, and such a factor cannot occur in \(W\), a contradiction.

These cases exhaust all binary run patterns and establish both necessity and sufficiency of the list. Different listed families have different run patterns or exponents; families 2 and 3 have two changes with strictly short middle runs, whereas families 7 and 8 have the full relevant middle run. Thus the families are pairwise disjoint. Taking lengths proves the polynomial.

**Excess law.** The two unary words and the two short-middle families contribute \(2+(b-1)+(c-1)=b+c\). The six conditional singletons contribute, respectively, the indicators
\[
\mathbf 1_{b<d}+\mathbf 1_{c<a}+\mathbf 1_{(a-c)(b-d)<0}
+\mathbf 1_{a<c,b\le d}+\mathbf 1_{c\le a,d<b}
+\mathbf 1_{c\le a,b\le d}.
\]
Partitioning by the three comparisons \(a<c,a=c,a>c\) and the three comparisons \(b<d,b=d,b>d\), the nine resulting excesses, in that row and column order, are
\[
\begin{pmatrix}2&1&1\\2&1&1\\4&2&2\end{pmatrix}.
\]
This is precisely the stated three-valued law. The three example tuples establish attainment. \(\square\)

## Verification

Run `python3 verify.py` with Python 3. The verifier constructs the proposed factor families separately from a literal exhaustive predicate: it lists every contiguous factor of each host, generates every possible one-letter left/right extension of every factor (including the empty factor), and selects precisely those absent words whose two length-one-shorter factors occur. It checks all \(8^4=4096\) positive parameter quadruples with each exponent in \(\{1,\ldots,8\}\), together with 120 reproducibly sampled larger quadruples with exponents up to 30. It checks disjointness, individual words, length histograms, the count formula, and all nine inequality-regions. Expected output:

`VERIFY_OK exhaustive_quadruples=4096 verified_maws=45328 total_maw_lengths=257664 larger_quadruples=120 comparison_regions=9 offset_values=[1, 2, 4]`

This is finite corroboration, not a proof for unbounded exponents; the preceding case analysis supplies the proof.

## Relationship to prior work

Akagi, Okabe, Mieno, Nakashima, and Inenaga (2022, arXiv:2202.13591) classify general minimal absent words on run-length encoded strings into five types and give an output-sensitive algorithm using storage linear in the number of runs. That algorithm can in principle enumerate the words here, but their stated theorems do not provide this four-run parameter classification, its exact length generating polynomial, or the sharp one/two/four excess law. In particular, this result claims no new general enumeration algorithm or compression bound.

Akagi et al. (2021, arXiv:2105.08496) and Mieno et al. (2019, arXiv:1909.02804) study how absent words and minimal unique factors change in a sliding window, proving general worst-case bounds and algorithms rather than formulas for the present fixed four-run family. A classification of minimal unique factors does not itself characterize absent factors: unique factors occur once, whereas minimal absent factors occur zero times and require only occurrence of their proper factors.

## Limitations

The result applies only to binary words with exactly four alternating nonempty runs, not arbitrary run-length encoded words or larger alphabets. The formula is not a claim about minimal absent *subsequences*. The overlap assessment is based on the published sources and searches described above; an equivalent unlocated special-case result cannot be ruled out. The original general run-length algorithm remains stronger as an algorithmic tool for unrestricted inputs. No independent mathematical audit has been performed.

## References

- Tooru Akagi, Kouta Okabe, Takuya Mieno, Yuto Nakashima, and Shunsuke Inenaga, *Minimal Absent Words on Run-Length Encoded Strings*, arXiv:2202.13591, first public February 28, 2022; CPM 2022, LIPIcs 223, Article 27. https://arxiv.org/abs/2202.13591
- Tooru Akagi, Yuki Kuhara, Takuya Mieno, Yuto Nakashima, Shunsuke Inenaga, Hideo Bannai, and Masayuki Takeda, *Combinatorics of Minimal Absent Words for a Sliding Window*, arXiv:2105.08496, first public May 18, 2021. https://arxiv.org/abs/2105.08496
- Takuya Mieno, Yuki Kuhara, Tooru Akagi, Yuta Fujishige, Yuto Nakashima, Shunsuke Inenaga, Hideo Bannai, and Masayuki Takeda, *Minimal Unique Substrings and Minimal Absent Words in a Sliding Window*, arXiv:1909.02804, first public September 6, 2019. https://arxiv.org/abs/1909.02804
