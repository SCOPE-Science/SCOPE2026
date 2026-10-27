# Complete minimal-absent-factor spectrum for two-marker binary words

## Finding

Write a finite binary word with exactly two ones as \(w=0^a1\,0^b1\,0^c\), where \(a,b,c\in\mathbb Z_{\ge0}\). A **minimal absent factor** is a nonempty binary string absent as a *contiguous* factor of \(w\), while every proper contiguous factor occurs. Let \(\mathcal M(w)\) be their set and let \(m=\min(a,c)\), \(q=\max(a,c)\). Then the exact cardinality is

\[
|\mathcal M(w)|=\begin{cases}
b+2,&b\ge q,\\
m+3+\mathbf 1_{a\ne c},&b<m,\\
b+3,&m\le b<q.
\end{cases}
\]

For each \(n\ge6\), exactly one binary word of length \(n\) with two ones maximizes this cardinality: \(10^{n-2}1\), with exactly \(n\) minimal absent factors. The small-length equality exceptions are: at length \(2\), only \(11\); at length \(3\), all three words; at length \(4\), \(1001\) and \(0110\); at length \(5\), \(10001\), \(01100\), and \(00110\). In every case the maximum equals \(n\).

The whole fixed-weight-two mean is also explicit. If \(S_s=\sum_{a+b+c=s}|\mathcal M(0^a1\,0^b1\,0^c)|\), then

\[
\sum_{s\ge0}S_sz^s=
\frac{2+5z+2z^2+2z^3-4z^4}{(1-z)^2(1-z^2)(1-z^3)}.
\]

Consequently the mean over the \(\binom n2\) binary words of length \(n\) with exactly two ones is \((7/18)n+O(1)\).

## Assumptions and scope

All words are finite and noncircular, and factors must be contiguous; scattered subsequences and circular factors are expressly excluded. The alphabet is exactly \(\{0,1\}\), even when a particular string omits one of these letters. All three gaps are allowed to vanish. The counts are of *distinct* minimal absent strings, not occurrences, and \(n=a+b+c+2\ge2\). The generating series is formal over the integers and needs no analytic convergence hypothesis.

## Proof

For any string \(u\) of length at least two, \(u\in\mathcal M(w)\) precisely if \(u\) is absent but both its length-\((|u|-1)\) prefix and suffix occur: every other proper factor lies in one of these. Absent one-letter strings qualify automatically.

Put \(M=\max(a,b,c)\), \(L=\max(a,b)\), \(R=\max(b,c)\), and \(K=\min(L,R)=\max(b,\min(a,c))\). The following **complete disjoint description** of \(\mathcal M(w)\) follows by classifying a candidate by its number of ones:

1. There is exactly one zero-only string, \(0^{M+1}\).
2. The absent strings containing exactly one one are: \(0^{L+1}1\) when \(c>L\); \(10^{R+1}\) when \(a>R\); \(0^{b+1}1\,0^{b+1}\) when \(a>b\) and \(c>b\); and \(0^{a+1}1\,0^{c+1}\) when \(a<b\) and \(c<b\).
3. The absent strings containing exactly two ones are: \(10^k1\) for \(0\le k\le K\), \(k\ne b\); \(0^{a+1}1\,0^b1\) when \(a<b\le c\); and \(10^b1\,0^{c+1}\) when \(c<b\le a\).
4. The only possible three-one minimal absent string is \(10^b1\,0^b1\), which qualifies exactly when \(a\ge b\) and \(c\ge b\). No candidate with four ones qualifies, since its length-minus-one prefix still contains at least three ones, whereas \(w\) contains only two.

To prove completeness of item 2, a one-one-containing factor \(0^i1\,0^j\) is present exactly on the union of the down-closed rectangles \(0\le i\le a,0\le j\le b\) and \(0\le i\le b,0\le j\le c\). Its possible minimal missing lattice positions consist of the two axial boundary points and, only when the rectangles are incomparable, their unique inner corner. An axial point survives the absent-prefix/suffix test exactly when its required zero-only factor of length one less is present. This gives the two strict-maximum tests above, and the two possible inner corners give the remaining two conditions.

For item 3, every factor with two ones has the unique gap \(b\) between them. A missing core \(10^k1\) passes its proper-prefix and proper-suffix tests exactly for \(0\le k\le K\), \(k\ne b\). A candidate with any extra zeros outside the two ones must have middle gap \(b\); removing a first or final zero still leaves two ones, so only the immediately missing left or right boundary can be minimal. Checking the opposite proper factor gives exactly the two flank tests in item 3. For item 4, the proper prefix and suffix must each contain both ones of \(w\), forcing both intervening zero gaps to equal \(b\); the remaining exterior zero requirements are exactly \(a\ge b,c\ge b\). Each proposed string can also be checked directly against the same prefix/suffix criterion. These arguments cover the zero-gap and zero-length boundary cases.

Counting the disjoint classes above and splitting according to the ordering of \(a,b,c\) yields the displayed three-case law. More explicitly, when \(b\ge q\), the count is \(b+2\); when \(b<m\), it is \(m+3+\mathbf1_{a\ne c}\); and when \(m\le b<q\), it is \(b+3\). (The disjoint split accounts correctly for equality of two or all three gaps.)

The sharp maximum follows immediately. If \(b\ge q\), \(|\mathcal M|=b+2\le n\), with equality only if \(a=c=0\). If \(b<m\), put \(q=\max(a,c)\); then \(n-|\mathcal M|=q+b-1-\mathbf1_{a\ne c}\). Equality in this case requires \((m,q,b)=(1,1,0)\) or \((1,2,0)\), hence occurs only at lengths \(4\) or \(5\). If \(m\le b<q\), the difference is \(n-|\mathcal M|=m+q-1\); equality forces \((m,q,b)=(0,1,0)\), hence length \(3\). The remaining length-\(2\) boundary is immediate. Enumerating the equalities and their reversals gives the stated short-length list.

For the generating series, summing the eight disjoint contributions of the complete description uses only geometric sums, \(\sum_{j\ge0}z^j=(1-z)^{-1}\) and \(\sum_{j\ge0}jz^j=z(1-z)^{-2}\). For a fully explicit reduction, define

\[
E(z)=\frac1{(1-z)^2}\left(\frac z{1-z}-\frac{2z^2}{1-z^2}+\frac{z^3}{1-z^3}\right).
\]

Here \(E\) enumerates each event \(c>\max(a,b)\), \(a>\max(b,c)\), or \(b>\max(a,c)\) (the three events have equal generating series by permuting coordinates). The total of the constant term, core-gap count, two axial points, two inner-corner cases, two flanks, and three-one term is

\[
\begin{aligned}
F(z)={}&\frac1{(1-z)^3}
+\left[\frac z{(1-z)^4}+\frac{z^2}{(1-z)^2(1-z^2)(1-z^3)}\right]
+3E(z)\\
&+\frac{z^2}{(1-z)^2(1-z^3)}
+\frac1{(1-z)^2(1-z^3)}
+\frac{2z^2}{(1-z)(1-z^2)(1-z^3)}.
\end{aligned}
\]

Combining these rational terms gives the claimed formula for \(F(z)\). Since the numerator evaluates to \(7\) at \(z=1\) and \((1-z)^2(1-z^2)(1-z^3)\sim6(1-z)^4\), its coefficients satisfy \(S_s=(7/36)s^3+O(s^2)\). Divide by \(\binom{s+2}{2}\) to obtain the mean \((7/18)n+O(1)\), with \(n=s+2\).

## Verification

The standalone standard-library file `VERIFY.py` calculates the proposed full minimal-absent-factor *set* directly from the stated classification and compares it to an independently constructed set of actual factors and candidate minimal absences. It checks all \(11^3=1331\) gap triples with gaps at most \(10\), 200 additional fixed-seed larger-gap triples, 32 generating-series coefficients by a separate coefficient formula, and exact maxima for every \(6\le n\le89\). Run `python3 VERIFY.py`; the expected final line starts with `PASS:`. The infinite formulas above rest on the proof, not on these finite checks.

## Relationship to prior work

Barton, Heliou, Mouchard, and Pissis (2014, arXiv:1406.6341) give general linear-time minimal-absent-word extraction based on suffix arrays, including the proper-prefix/proper-suffix characterization. That algorithm makes the present finite strings computable but does not itself state the explicit gap formula, three-case classification, or aggregate rational series. Charalampopoulos, Crochemore, Fici, Mercas, and Pissis (2018, arXiv:1806.02718), Section 3, **already use the family** \(10^{n-2}1\) to demonstrate a linear number of minimal absent words, explicitly identifying \(n-2\) of them. Neither the witness family nor linear growth is claimed here as new. The added claims are the exact universal three-gap antictionary, its exact cardinality and finite-length extremal classification, and the weight-two mean law. The compared prior results do not imply these exact statements without additional analysis.

## Limitations

Only words with exactly two ones over a fixed binary alphabet are covered. This says nothing about arbitrary Hamming weights, circular or scattered factors, or optimal counts over *all* binary words. A general-purpose algorithm that enumerates minimal absent factors is not a structural proof of the closed formulas. Full priority against all historic, possibly unindexed results cannot be guaranteed; the strongest directly relevant inspected prior example already uses the same extremal word.

## References

1. C. Barton, A. Heliou, L. Mouchard, S. P. Pissis, *Linear-time Computation of Minimal Absent Words Using Suffix Array*, arXiv:1406.6341, first public preprint 2014-06-24. https://arxiv.org/abs/1406.6341.
2. P. Charalampopoulos, M. Crochemore, G. Fici, R. Mercas, S. P. Pissis, *Alignment-free sequence comparison using absent words*, arXiv:1806.02718, first public preprint 2018-06-07. https://arxiv.org/abs/1806.02718.
