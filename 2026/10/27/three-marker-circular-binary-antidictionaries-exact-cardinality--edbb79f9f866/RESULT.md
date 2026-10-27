# Three-marker circular binary antidictionaries: exact cardinality and extremizers

## Finding

Let \(w\) be any circular binary word containing exactly three occurrences of \(1\). Write its three cyclic zero-gap lengths as nonnegative integers \(a,b,c\), so a linearization is \(1 0^a1 0^b1 0^c\). Let \(\mathcal F(w)\) be the set of *all finite factors of the bi-infinite periodic repetition* of \(w\), allowing factors longer than one circuit. A minimal absent word is a binary word not in \(\mathcal F(w)\) whose every proper factor belongs to \(\mathcal F(w)\). Denote their set by \(\mathcal M(w)\).

Put \(M=\max\{a,b,c\}\), and let \(d=|\{a,b,c\}|\) be the number of distinct zero-gap lengths. Then, with no primitivity assumption and allowing zero gaps,

\[
|\mathcal M(w)|=
\begin{cases}
M+1,&d=1,\\
M+3,&d=2,\\
M+4,&d=3.
\end{cases}
\]

This is an exact count of **distinct** minimal absent contiguous words, not of their occurrences. In particular, if \(n=|w|\ge4\), its maximum over all circular binary words of length \(n\) and weight three is exactly \(n\). The maximizing cyclic gap multisets are precisely \(\{0,0,n-3\}\), and also \(\{0,1,n-4\}\) when \(n\ge6\). The minimum is \(\lfloor(n-3)/3\rfloor+1\) when \(3\mid(n-3)\), and \(\lfloor(n-3)/3\rfloor+4\) otherwise. At \(n=3\) the sole word is \(111\) and has one minimal absent word, namely \(0\).

The count depends only on the longest gap and the number of distinct gaps, suppressing all other numerical gap information. A stronger ingredient of the proof explicitly classifies every bispecial factor.

## Assumptions and scope

The alphabet is exactly \(\{0,1\}\). An empty zero gap is permitted, so consecutive ones may occur. The circular word has exactly three ones, regardless of whether its marked length is the least period. The factor language is the periodic-factor language, not the truncated language of factors of length at most \(|w|\). The two circular definitions are distinct in general; the periodic version is standard in the minimal-absent-word literature. Factor, left-special, right-special, and minimal-absent counts refer to **different words**, never to multiple occurrences.

For a factor \(u\), let \(L(u)=\{t\in\{0,1\}:tu\in\mathcal F(w)\}\) and \(R(u)=\{t\in\{0,1\}:ut\in\mathcal F(w)\}\). A factor is *bispecial* if both sets have two elements. The empty word is counted as a factor and is bispecial whenever both letters occur. Write \(Z_j=0^j\), including \(Z_0=\varepsilon\).

## Proof

**1. A binary periodic-antidictionary counting identity.** Suppose a periodic binary word contains both symbols. Write \(C(k)\) for the number of its distinct length-\(k\) factors, with \(C(0)=1\), and \(B(k)\) for its number of bispecial factors of length \(k\). For a length-\(k\) factor \(u\), set \(\ell(u)=|L(u)|\), \(r(u)=|R(u)|\), and let \(e(u)\) count its occurring two-sided extensions \(xuy\), for \(x,y\in\{0,1\}\).

A candidate \(xuy\) is minimally absent if and only if both \(xu\) and \(uy\) occur while \(xuy\) does not. Consequently the number \(m(k+2)\) of length-\(k+2\) minimal absent words is

\[
m(k+2)=\sum_{|u|=k}\bigl(\ell(u)r(u)-e(u)\bigr).
\]

Since \(\ell(u),r(u)\in\{1,2\}\), we have
\(\ell(u)r(u)=\ell(u)+r(u)-1+(\ell(u)-1)(r(u)-1)\), where the final product is one precisely for bispecial \(u\). Moreover \(\sum_{|u|=k}\ell(u)=\sum_{|u|=k}r(u)=C(k+1)\), and \(\sum_{|u|=k}e(u)=C(k+2)\). Hence

\[
m(k+2)=2C(k+1)-C(k)-C(k+2)+B(k).
\]

The complexity of a periodic word eventually stabilizes at its least period; it has no length-one absent words because both symbols occur. Summing over \(k\ge0\) telescopes the complexity terms to \(C(1)-C(0)=1\). Thus

\[
|\mathcal M(w)|=1+\sum_{k\ge0}B(k). \tag{1}
\]

This identity is only used as an elementary counting tool; the content of the result is the complete bispecial-factor classification below.

**2. The zero-only bispecial factors.** Assume \(M\ge1\). Exactly the words \(Z_0,Z_1,\ldots,Z_{M-1}\) among zero-only factors are bispecial. For \(0\le j<M\), a gap of length \(M\) provides occurrences of \(Z_j\) both at a zero-run boundary and strictly inside that gap, giving both left and both right extensions. The factor \(Z_M\) cannot extend by \(0\), and longer zero words do not occur. Hence there are exactly \(M\) zero-only bispecial factors.

**3. A factor with one occurrence of \(1\).** After a cyclic rotation and, if necessary, a reversal, we may suppose \(0\le a\le b\le c=M\): the dihedral permutations of three gap positions exhaust all permutations. At each marked occurrence of \(1\), record the preceding and following complete zero-gap lengths \((P,Q)\). In cyclic order these three contexts are
\((a,b),(b,c),(c,a)\), with multiplicity.

A word \(Z_p1Z_q\) occurs in a context exactly when \(P\ge p\) and \(Q\ge q\). Its left extension is \(1\) when \(P=p\) and \(0\) when \(P>p\); its right extension is \(1\) when \(Q=q\) and \(0\) when \(Q>q\). It is therefore bispecial precisely if, among its eligible contexts, both equality and strict inequality occur in each coordinate. Checking the three displayed pairs gives the **complete** one-marker list:

| Gap order | One-marker bispecial factors |
| --- | --- |
| \(a=b=c\) | none |
| \(a=b<c\) | \(Z_a1Z_a\) |
| \(a<b=c\) | \(Z_a1Z_a\) |
| \(a<b<c\) | \(Z_a1Z_a,\ Z_a1Z_b,\ Z_b1Z_a\) |

For example, in the distinct case the admissible threshold pairs are exactly \((p,q)=(a,a),(a,b),(b,a)\). Thresholds outside this list either do not occur or leave at most one of the two required extension letters on one side.

**4. Factors with two or more occurrences of \(1\).** Any factor with exactly two ones has the form \(Z_p1Z_t1Z_q\), with \(t\in\{a,b,c\}\). Such a factor is eligible at precisely the occurrences of the cyclic gap \(t\). If all gaps are distinct, \(t\) determines a unique marked context, so no such factor can be bispecial. If two gaps have the same length, the repeated value is the only possible \(t\). The two occurrences have preceding and following outer-gap lengths of either \((a,c)\) and \((c,a)\) when \(a=b<c\), or \((a,b)\) and \((b,a)\) when \(a<b=c\). The equality/inequality criterion from Step 3 then forces \(p=q=a\), giving precisely

\[
\begin{array}{ll}
Z_a1Z_a1Z_a,& a=b<c,\\
Z_a1Z_b1Z_a,& a<b=c.
\end{array}
\]

If all gaps are equal, the periodic word has least period \(M+1\), and every factor containing a one has fixed left and right extensions. Finally, when the three gaps are not all equal, any factor containing three or more ones includes two complete consecutive zero gaps. The ordered pair of two consecutive gaps determines a unique cyclic phase among three gap positions: if any two such ordered pairs coincided, all three gap lengths would be equal. Thus the factor has one marked occurrence phase and cannot be bispecial. This also excludes longer bispecial factors.

Combining Steps 2–4 gives the complete list: \(M\) zero-only bispecial factors, plus respectively \(0,2,3\) distinct one-containing bispecial factors according as \(d=1,2,3\). Equation (1) proves the displayed three-case formula for \(M\ge1\). If \(M=0\), then \(w=111\), whose sole minimal absent word is \(0\); the same \(M+1\) formula holds.

**5. Fixed-length extrema.** Put \(S=n-3=a+b+c\). For \(S>0\), if exactly two gap lengths differ, the bound \(M+3\le S+3=n\) is attained precisely for \(\{a,b,c\}=\{0,0,S\}\). For pairwise distinct gaps, \(M+4\le S+3=n\), with equality only when the two smaller gaps sum to one: the multiset is \(\{0,1,S-1\}\), possible exactly when \(S\ge3\). The all-equal case has strictly fewer. For the minimum, if \(3\mid S\), the equal triple gives \(S/3+1\) and all unequal triples are larger; otherwise \(M\ge\lceil S/3\rceil\), every unequal triple contributes at least three extra terms, and balanced triples with two equal gaps attain \(\lceil S/3\rceil+3=\lfloor S/3\rfloor+4\). This establishes all extremal assertions.

## Verification

Run the standalone finite checker using `python3 verify.py`. It builds the periodic factor sets from first principles, enumerates minimal absent words by checking their maximal proper prefix and suffix, and independently computes the bispecial factors by four single-letter extension tests. It compares **sets** of bispecial factors with the explicit classification, not just their sizes, and checks the formula on all \(1000\) ordered triples \((a,b,c)\in\{0,\ldots,9\}^3\), whose largest word length is \(30\). It also checks fixed-length extrema and their maximizing gap multisets for lengths \(3\) through \(33\). The expected program output contains two `PASS` lines. These finite checks do not replace the proof for unbounded gaps.

A representative distinct-gap example is \((a,b,c)=(1,2,3)\). Its seven minimal absent words are \(11\), \(0000\), \(10101\), \(000100\), \(001001\), \(100101\), and \(101000\), consistent with \(M+4=7\).

## Relationship to prior work

Crochemore, Fici, Mercaş and Pissis established algorithmic comparison of circular words through minimal absent words, including the periodic-factor-language convention and algorithms for their computation. Their result supplies the motivating invariant, not an exact cardinality formula conditional on three one-markers and gap multiplicities. Fici, Restivo and Rizzo developed structural results for circular minimal forbidden factors, with general cardinality bounds, reconstruction, and explicit circular Fibonacci antidictionaries. A general upper bound of the word length does **not** imply this theorem's exact three-case cardinality, complete bispecial-factor list, or sharp weight-three extremizer classification. The weight-three class and the dependence only on \(M\) and \(d\) are specific to the present argument. Later work by Ota and Manada studies reconstruction from circular substrings and minimal absent words; its abstract addresses reconstruction thresholds rather than this distribution.

## Limitations

The result assumes exactly three occurrences of \(1\), the binary alphabet, and the periodic convention for circular factors. It makes no claim for arbitrary marker number, for a truncated circular factor language, or about frequency-weighted absent words. The finite checker covers bounded gaps only. The related later reconstruction article was inspected at abstract level; its downloadable full PDF was not accessible in the current check, leaving a residual literature priority risk. No independent audit has been performed.

## References

1. Maxime Crochemore, Gabriele Fici, Robert Mercaş, Solon P. Pissis, *Linear-Time Sequence Comparison Using Minimal Absent Words & Applications*, arXiv:1506.04917, first publicly posted 2015-06-16, https://arxiv.org/html/1506.04917v2 (especially Section 4).
2. Gabriele Fici, Antonio Restivo, Laura Rizzo, *Minimal Forbidden Factors of Circular Words*, arXiv:1707.04450, first publicly posted 2017-07-14, https://arxiv.org/html/1707.04450v3 (especially Sections 3–4).
3. Takahiro Ota and Akiko Manada, *A Reconstruction of Circular Binary String Using Substrings and Minimal Absent Words*, IEICE Transactions E107.A (2024), 409–416, DOI: 10.1587/transfun.2023TAP0015. The accessible abstract was inspected; the full article was not verified.
