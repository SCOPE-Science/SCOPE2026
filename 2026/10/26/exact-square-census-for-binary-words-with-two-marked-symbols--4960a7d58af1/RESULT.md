# Exact square census for binary words with two marked symbols

## Finding

For all integers \(a,b,c\ge 0\), consider the finite binary word
\[
w=0^a1\,0^b1\,0^c,
\]
and let \(D(w)\) denote the number of **distinct nonempty ordinary square factors** \(uu\), where \(u\) is a nonempty contiguous word. Two occurrences of the same square count once. Write \(m=a+b+c\), \(M=\max\{a,b,c\}\), and \([x]_+=\max\{x,0\}\). Then
\[
\boxed{D(w)=\left\lfloor\frac{M}{2}\right\rfloor
 + [1+\min\{a,b,c,a+c-b\}]_+.}
\tag{1}
\]

Let \(S_m\) be the sum of \(D(w)\) over all \(\binom{m+2}{2}\) words with exactly two ones and \(m\) zeros. The **all-length square census** is
\[
\boxed{\sum_{m\ge0} S_m z^m
=\frac{\frac{3z^2}{1-z^2}-\frac{3z^4}{1-z^4}+\frac{z^6}{1-z^6}}{(1-z)^3}
 +\frac{1}{(1-z)^2(1-z^2)^2}.}
\tag{2}
\]
The coefficients \(S_m\) for \(0\le m\le10\) are \(1,2,8,17,32,50,79,115,163,218,289\). The mean among uniformly sampled words of this fixed composition satisfies
\[
\frac{S_m}{\binom{m+2}{2}}=\frac{7}{18}m+O(1).
\tag{3}
\]

Both extremes are sharp at **every** length. For \(m\ge1\),
\[
\boxed{\min_w D(w)=\left\lfloor\frac{m+2}{4}\right\rfloor,\qquad
\max_w D(w)=\left\lfloor\frac{m}{2}\right\rfloor+1.}
\tag{4}
\]
For \(m=0\), the only word is \(11\), with \(D(11)=1\). Furthermore, let \(E_m\) be the **number of words attaining the maximum** in (4), with \(E_0=1\). If \(m\ge0\) is even, then
\[
\boxed{E_m=2\left(\left\lfloor\frac m3\right\rfloor+1\right)-\mathbf1_{3\mid m}.}
\tag{5}
\]
If \(m\ge1\) is odd, then
\[
\boxed{E_m=2\left(\left\lfloor\frac m3\right\rfloor+1\right)-\mathbf1_{3\mid m}
+4\left(\left\lfloor\frac{m-2}{3}\right\rfloor+1\right)
-\mathbf1_{m\equiv2\ (\mathrm{mod}\ 3)}.}
\tag{6}
\]
Here \(\mathbf1\) denotes an indicator. Thus the equality-family cardinalities form an explicit mod-six quasipolynomial, not merely an asymptotically sharp construction.

## Assumptions and scope

The alphabet is exactly \(\{0,1\}\). Factors are linear, contiguous, and equality of square factors means equality as binary strings, not equality of occurrence positions. Squares of empty roots are excluded. A square is **ordinary** (two identical halves), not merely Abelian (two anagram halves) and not a shuffle square. Every length under consideration has exactly two ones, including adjacent ones, and no supplementary conditions on the three zero gaps. There are no claims for words with three or more ones.

## Proof

**Classification of all squares.** A square factor has an even number of ones, since its two halves are equal. As the whole word has two ones, a square factor has either zero or two ones. The zero-one-count squares are precisely the strings \(0^{2j}\), \(1\le j\le\lfloor M/2\rfloor\), giving the first term of (1).

A square factor with both ones has a root with exactly one one, hence a uniquely determined shape \(0^u1\,0^v\) for \(u,v\ge0\). Its square equals \(0^u1\,0^{u+v}1\,0^v\). It is a factor of \(w\) precisely when \(u+v=b\), \(u\le a\), and \(v\le c\). Equivalently, \(u\) is an integer in
\[
\max\{0,b-c\}\le u\le\min\{a,b\}.
\]
Different choices of \(u\) give different square strings. Its cardinality is
\[
T(a,b,c)=\left[1+\min\{a,b\}-\max\{0,b-c\}\right]_+
=[1+\min\{a,b,c,a+c-b\}]_+,
\]
where the second identity follows by separately considering \(b\le c\) and \(b>c\). This proves (1), including all boundary cases.

**Aggregate generating function.** Since \(\lfloor M/2\rfloor=\sum_{j\ge1}\mathbf1_{M\ge2j}\), the all-zero-square contribution summed over triples of nonnegative gaps has generating function
\[
\frac{1}{(1-z)^3}\sum_{j\ge1}(3z^{2j}-3z^{4j}+z^{6j}),
\]
by inclusion-exclusion over the three possible gaps of size at least \(2j\). Summing the geometric series gives the first summand of (2). To count every pair \((w,\text{two-one square factor})\), write \(b=u+v\), \(a=u+r\), \(c=v+s\), with \(u,v,r,s\ge0\). Then \(m=2u+2v+r+s\), so the generating function is \((1-z^2)^{-2}(1-z)^{-2}\), the second summand. This proves (2). Near \(z=1\), the first summand has leading singular part \(\frac{11}{12}(1-z)^{-4}\) and the second \(\frac14(1-z)^{-4}\). All other poles have smaller order, so \(S_m=\frac7{36}m^3+O(m^2)\). Since \(\binom{m+2}{2}=m^2/2+O(m)\), (3) follows.

**Maximum.** If \(T=0\), (1) is at most \(\lfloor m/2\rfloor\). Otherwise set \(t=T-1=\min\{a,b,c,a+c-b\}\ge0\). If \(M=a\) or \(M=c\), the other two gaps are at least \(t\); if \(M=b\), then \(a+c\ge b+t\ge2t\). In every case \(M+2t\le m\). Hence \(D(w)=\lfloor M/2\rfloor+t+1\le\lfloor m/2\rfloor+1\). Equality is achieved at \((a,b,c)=(m,0,0)\), proving the maximum in (4).

**Minimum.** For any \(m\ge1\), let \(M=\max(a,b,c)\). If \(M>m/2\), (1) gives \(D(w)\ge\lfloor M/2\rfloor\ge\lfloor(m+2)/4\rfloor\). If \(M\le m/2\), each of \(a,b,c,a+c-b\) is at least \(m-2M\), so (1) gives \(D(w)\ge\lfloor M/2\rfloor+m-2M+1\). This lower bound decreases as the integer \(M\) increases and, at \(M=\lfloor m/2\rfloor\), is at least \(\lfloor(m+2)/4\rfloor\). For sharpness take \(b=\lfloor m/2\rfloor+1\), \(a=m-b\), \(c=0\). Then \(b>a+c\), the two-one-square term vanishes, and \(D(w)=\lfloor b/2\rfloor=\lfloor(m+2)/4\rfloor\). The case \(m=0\) follows directly from (1).

**Exact number of maximizers.** For \(T>0\), retain \(t=T-1\) and write the slack \(s=m-(M+2t)\ge0\). Equality in the maximum means \(s=0\) when \(m\) is even, and \(s\in\{0,1\}\) when \(m\) is odd. If \(s=0\), the triples are exactly
\[
(M,t,t),\quad(t,t,M),\qquad M=m-2t\ge t,
\]
with one duplicate when \(M=t\). This produces \(2(\lfloor m/3\rfloor+1)-\mathbf1_{3\mid m}\) words. If \(m\) is odd and \(s=1\), the triples are exactly
\[
(M,t,t+1),\ (M,t+1,t),\ (t,t+1,M),\ (t+1,t,M),
\quad M=m-2t-1\ge t+1,
\]
with exactly one duplicate when \(M=t+1\), equivalent to \(m=3t+2\). Indeed, if the middle gap is a largest gap, the condition \(t\le a+c-b\) forces \(b=t+1\), already included in these lists. The admissible values are \(0\le t\le\lfloor(m-2)/3\rfloor\). Counting proves (5)–(6), including \(m=1\) where the latter range is empty.

## Verification

The standalone script `scripts/check_square_census.py` enumerates actual square strings independently of (1). It checks all \(2600\) two-one binary words with \(0\le m\le23\). It then checks a total of \(302621\) zero-gap triples for \(0\le m\le120\) against independently computed aggregate coefficients, extrema, and (5)–(6). It verifies both sharpness constructions for an additional 500 lengths. It uses Python's exact integer arithmetic without outside libraries. These finite checks corroborate, but are not substituted for, the all-length arguments above.

## Relationship to prior work

Fraenkel and Simpson developed the distinct-square counting problem and proved a general linear upper bound. Jonoska, Manea and Seki formulated the strengthened bound sensitive to the minority-letter multiplicity and, in their 2014 presentation, confirmed the \(2\le k\le9\) cases; in particular their \(k=2\) result already yields \(D(w)\le\lfloor(m+2)/2\rfloor\) for words with two ones and sufficiently many zeros. Li later established the bound for general \(k\). **The upper bound by itself is not claimed as new.** What (1)–(6) add is the full per-word ordinary-square count, the exact all-length sum and asymptotic mean, the sharp minimum, and the count of *all* words attaining the sharp maximum. The general bounds do not imply these enumerations.

A related 2026 study by Fazekas, Mammoliti, Mercaş, and Simpson gives minima for distinct **Abelian** squares in exactly-two-marker words, including a different pair-count condition. Ordinary squares impose literal equality of halves and are strictly more restrictive; their individual and extremal enumerations cannot be inferred by replacing Abelian squares with ordinary squares in that result.

## Limitations

No assertion is made about squares in higher-weight words, Abelian or shuffle squares, or the entire distribution of \(D(w)\) (beyond its first moment and extremal count). The complete proceedings article of Jonoska–Manea–Seki was not available for full-text comparison; its author presentation was examined for the relevant statements. Thus priority is conditional on the accessible primary literature and record searches; the absence of a detected statement is not a proof of novelty. The finding has not received an independent audit.

## References

1. A. S. Fraenkel and J. Simpson, *How Many Squares Can a String Contain?*, Journal of Combinatorial Theory A 82 (1998), 112–120. DOI: `10.1006/jcta.1997.2843`.
2. N. Jonoska, F. Manea and S. Seki, *A Stronger Square Conjecture on Binary Words*, SOFSEM 2014, LNCS 8327, 339–350. DOI: `10.1007/978-3-319-04298-5_30`. Author presentation dated 2014-01-27: `https://users.ics.aalto.fi/sseki/presen/20140127_SOFSEM2014.pdf`.
3. S. Li, *An Upper Bound of the Number of Distinct Powers in Binary Words*, first preprint 2022-09-14, `arXiv:2209.06891`.
4. S. Z. Fazekas, A. Mammoliti, R. Mercaş and J. Simpson, *Binary Words Containing Few Abelian Squares*, first preprint 2026-04-25, `arXiv:2604.23188`.
