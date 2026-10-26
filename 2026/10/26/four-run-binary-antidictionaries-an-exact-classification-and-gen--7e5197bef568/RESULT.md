# Four-run binary antidictionaries: an exact classification and generating spectrum

## Finding

Fix the binary alphabet \(\{0,1\}\). For every quadruple of **positive integers** \(a,b,c,d\), put
\[
T_{a,b,c,d}=0^a1^b0^c1^d.
\]
A *minimal absent factor* (MAF), also called a minimal absent word, is a nonempty binary word that does not occur contiguously in \(T_{a,b,c,d}\), although every proper contiguous factor does. Denote the set by \(\mathcal A(T)\).

**Theorem (complete four-run classification).** The complete, disjoint description of \(\mathcal A(T_{a,b,c,d})\) is given in the table below. Every condition not stated in a row is just \(a,b,c,d\ge1\). An interval of integer indices with no members contributes the empty family.

| Family of absent factors | Occurrence condition |
|:--|:--|
| \(0^{\max(a,c)+1}\); \(1^{\max(b,d)+1}\) | Always (two words) |
| \(0 1^j 0\), \(1\le j<b\) | Always |
| \(1 0^j 1\), \(1\le j<c\) | Always |
| \(1 0^{c+1}\) | \(a>c\) |
| \(1^{b+1}0\) | \(d>b\) |
| \(0^{a+1}1^{d+1}\) | \(a<c\) and \(b>d\) |
| \(0^{c+1}1^{b+1}\) | \(a>c\) and \(d>b\) |
| \(0^{a+1}1^b0\) | \(c>a\) and \(d\ge b\) |
| \(10^c1^{d+1}\) | \(a\ge c\) and \(b>d\) |
| \(10^c1^b0\) | \(a\ge c\) and \(d\ge b\) |

In particular, with \(\mathbf 1_P\) denoting the indicator of proposition \(P\),
\[
\boxed{\ |\mathcal A(T_{a,b,c,d})|=b+c+
\bigl(1+\mathbf 1_{a>c}\bigr)\bigl(1+\mathbf 1_{d>b}\bigr).\ }
\]
Thus the correction to \(b+c\) takes exactly the values \(1,2,4\); it is multiplicative in two opposite boundary comparisons.

There is also a complete rational bivariate generating function for the joint distribution of word length and number of minimal absent factors. In the ring of formal power series, let
\[
F_0(z,u)=\frac{uz^2}{(1-uz)(1-uz^2)},\qquad
F_1(z,u)=\frac{uz^3}{(1-z)(1-uz^2)}.
\]
Then
\[
\boxed{\ \sum_{a,b,c,d\ge1}z^{a+b+c+d}u^{|\mathcal A(T_{a,b,c,d})|}
=uF_0(z,u)^2+2u^2F_0(z,u)F_1(z,u)+u^4F_1(z,u)^2.\ }
\]
Consequently, among all binary words of length \(n\) having exactly four nonempty constant runs, the maximum number of minimal absent factors is
\[
\boxed{\ n\ \text{if }n=6,\quad n-1\ \text{for every }n\ge4\text{ with }n\ne6.\ }
\]
The exceptional maximum at length \(6\) is attained, up to exchanging the binary alphabet symbols, only by \(001011\), corresponding to \((a,b,c,d)=(2,1,1,2)\).

## Assumptions and scope

The factor relation is **contiguous**, not scattered. The ambient alphabet is exactly binary; the words are linear, not circular, and all four run lengths are positive integers. Words with a different number of runs or a larger alphabet are not asserted to satisfy the formula. Reversing the word and/or exchanging the two letters does not affect its number of minimal absent factors; hence the normal form with first letter \(0\) covers all binary words with exactly four runs.

We adopt the usual convention that the empty word is a factor of every word. Because both binary symbols occur in \(T_{a,b,c,d}\), its minimal absent factors all have length at least two. For any binary word \(x\) of length at least two, minimal absence is equivalent to the conjunction
\[
x\notin \operatorname{Fact}(T),\qquad
x[1..|x|-1]\in\operatorname{Fact}(T),\qquad
x[2..|x|]\in\operatorname{Fact}(T).
\]
The first and second proper overlapping factors in this display are obtained by deleting the last and first letters, respectively; all shorter proper factors are factors of one of them.

## Proof

**Step 1: structural factor rectangles.** The factors with exactly two runs have the following exponent domains:
\[
\begin{array}{c|l}
\text{shape} & \text{possible exponent pairs}\\\hline
0^i1^j&([1,a]\times[1,b])\cup([1,c]\times[1,d])\\
1^i0^j&[1,b]\times[1,c].
\end{array}
\]
For factors with three runs, only the first triple of runs can produce \(0^i1^j0^k\); its domain is \(1\le i\le a\), \(j=b\), \(1\le k\le c\). Similarly, only the final triple can produce \(1^i0^j1^k\), with \(1\le i\le b\), \(j=c\), \(1\le k\le d\). Any four-run factor necessarily has the form \(0^i1^b0^c1^j\) with \(1\le i\le a\), \(1\le j\le d\). There are no factors with at least five runs, and no factor of shape \(1^i0^j1^k0^\ell\).

**Step 2: candidates with one or two runs.** In one run, the two minimal forbidden powers are exactly \(0^{\max(a,c)+1}\) and \(1^{\max(b,d)+1}\). For two runs \(0^i1^j\), apply the displayed union of two downward-closed rectangles and the condition that deleting either terminal letter must yield a factor. If the rectangles have incomparable maxima, there is exactly one minimal point outside both: \((a+1,d+1)\) when \(a<c,b>d\), or \((c+1,b+1)\) when \(a>c,d>b\). When the maxima are comparable, there is none. The shape \(1^i0^j\) has one occurrence rectangle; the only possible minimal absent factors are \(10^{c+1}\), if the first run of zeros is longer than the third, and \(1^{b+1}0\), if the last run of ones is longer than the second. These four possibilities exhaust the two-run table entries.

**Step 3: candidates with three runs.** Consider \(x=0^i1^j0^k\). The first and last deletions must both occur as factors. If \(j<b\), neither a three-run factor with middle exponent \(j\) nor an extension of one exists in \(T\); both deletions can be factors only when \(i=k=1\). Precisely \(01^j0\), \(1\le j<b\), result. If \(j=b\), every word with \(i\le a,k\le c\) occurs. Of the remaining possibilities, the only one surviving both deletion tests is \(0^{a+1}1^b0\), requiring \(c>a,d\ge b\). If \(j>b\), the final deletion cannot be a factor because no occurrence of \(1^j0\) exists with \(j>b\). Thus these are all the \(010\)-shaped minimal absent factors.

The analogous analysis for \(x=1^i0^j1^k\) yields the family \(10^j1\) for \(1\le j<c\), and the sole boundary word \(10^c1^{d+1}\) if \(a\ge c,b>d\). No other three-run candidates pass both deletion tests. Notice that the two boundary cases involve the *other* occurrence of a two-run factor, an interaction that does not appear in the interior bridge families.

**Step 4: candidates with four or more runs.** If a minimal absent word had at least six runs, at least one of its first- or last-letter deletions would still have five runs and thus could not be a factor. A five-run candidate would need both first and last runs to be singletons; then at least one deletion has shape \(1010\), which is not a factor. For the four-run shape \(0101\), testing the two deletions against the four-run factor rectangle in Step 1 shows that both deletions being present forces the original word to be present too. The only remaining shape is \(1010\), which never occurs. Its two deletions can both occur only if its first and last runs are singletons and its inner run lengths are exactly \(c\) and \(b\), respectively. This gives \(10^c1^b0\), requiring \(c\le a\) and \(b\le d\). This completes the exhaustive table, including its disjointness (by shape, exponents and distinct strict inequalities).

**Step 5: simplify the count.** The always-present rows contribute \(2+(b-1)+(c-1)=b+c\). The remaining seven indicator contributions reduce, by a four-case split on the truth values of \(a>c\) and \(d>b\), to \(1,2,2,4\), respectively. These are exactly \((1+\mathbf1_{a>c})(1+\mathbf1_{d>b})\), proving the displayed count.

**Step 6: generating function.** Let \(F_q(z,u)\) count ordered positive pairs \((a,c)\), giving weight \(z^{a+c}u^c\), with \(q=\mathbf1_{a>c}\). Summation of geometric series gives
\[
F_0(z,u)=\sum_{c\ge1}\sum_{a=1}^c z^{a+c}u^c
=\frac{uz^2}{(1-uz)(1-uz^2)},\quad
F_1(z,u)=\sum_{c\ge1}\sum_{a>c}z^{a+c}u^c
=\frac{uz^3}{(1-z)(1-uz^2)}.
\]
The pair \((d,b)\) has exactly the same distributions with \(r=\mathbf1_{d>b}\), and its weight is \(z^{d+b}u^b\). For \((q,r)=(0,0),(0,1),(1,0),(1,1)\), the additional number of missing factors is \(1,2,2,4\). Multiplying the two independent pair generating functions and adding the four cases gives the stated rational bivariate series.

**Step 7: sharp maximum.** Write \(n=a+b+c+d\). The count is \(n-a-d+1\), \(n-a-d+2\), or \(n-a-d+4\) according as neither, exactly one, or both inequalities \(a>c,d>b\) hold. Neither requires only \(a,d\ge1\), giving at most \(n-1\); one requires \(a+d\ge3\), also giving at most \(n-1\). Both require \(a,d\ge2\), giving at most \(n\), with equality only for \(a=d=2,c=b=1\), hence \(n=6\). In every other both-inequalities case, \(a+d\ge5\), giving at most \(n-1\). Finally, \(a=d=1\) and any positive \(b,c\) with \(b+c=n-2\) attain \(n-1\), proving sharpness for every \(n\ge4\), except that the unique six-letter exception attains \(n\).

## Verification

The file `verify.py` implements the minimal-absence definition independently by enumerating factors and checking both one-letter deletions. It also implements the theorem's explicit family list. Execution with ordinary Python 3 gives:

```
VERIFY_OK: exact minimal-absent sets on 4096 parameter quadruples; sharp maxima at 18 lengths; full bivariate counts through length 17
```

Here all \(1\le a,b,c,d\le8\) are checked for **set equality**, not only numerical cardinality. The separately tested maxima cover lengths \(4\) through \(21\). The power-series check compares full \((n,k)\) multiplicities through length \(17\). These finite checks detect common indexing/boundary mistakes but are **not** evidence for the infinite quantifiers; the proof in Steps 1–7 establishes them.

## Relationship to prior work

Akagi, Okabe, Mieno, Nakashima and Inenaga, *Minimal Absent Words on Run-Length Encoded Strings* (arXiv:2202.13591, first available 2022-02-28), give general classifications and compressed enumeration algorithms for minimal absent words of arbitrary run-length encoded strings. In particular, their Lemma 3 shows that three-run bridge-type missing words can be arbitrarily numerous at fixed RLE size, and their Theorem 1 gives a general output-sensitive enumerator. The present theorem does **not** claim to improve that algorithm: it supplies a fully symbolic four-run binary antidictionary, its multiplicative boundary law, a bivariate enumeration, and a sharp length extremum. These formulas do not follow as a stated parameterized corollary of their asymptotic bounds or algorithm without a separate structural calculation.

Inenaga, Mieno, Arimura, Funakoshi and Fujishige, *Computing Minimal Absent Words and Extended Bispecial Factors with CDAWG Space* (arXiv:2402.18090, 2024), address general compressed enumeration and extended bispecial factors. A full-text comparison was not possible here; the accessible abstract establishes only the algorithmic subject, not absence of an equivalent exact family formula. Targeted search did not reveal an already-stated classification, but absence from a search is not proof of priority.

## Limitations

The result is specific to four binary runs and exact contiguous minimal absence; it is not an enumeration of scattered absent subsequences. The factor-list proof does not extend automatically to five or more runs. It does not establish priority against every unindexed or inaccessible manuscript. In particular, a potentially relevant 2024 compressed-automaton paper could not be fully inspected.

## References

1. T. Akagi, K. Okabe, T. Mieno, Y. Nakashima, S. Inenaga, *Minimal Absent Words on Run-Length Encoded Strings*, arXiv:2202.13591 (initial submission 2022-02-28); CPM 2022, DOI: 10.4230/LIPIcs.CPM.2022.27. https://arxiv.org/abs/2202.13591
2. S. Inenaga, T. Mieno, H. Arimura, M. Funakoshi, Y. Fujishige, *Computing Minimal Absent Words and Extended Bispecial Factors with CDAWG Space*, arXiv:2402.18090 (initial submission 2024-02-28). https://arxiv.org/abs/2402.18090
