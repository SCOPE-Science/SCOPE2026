# Exact longest-Lyndon-subsequence deficiency and its limiting law for four-run binary words

## Finding

Order the binary alphabet by \(0<1\). For every quadruple of positive integers \(a,b,c,d\), let
\[
w=0^a1^b0^c1^d,\qquad n=a+b+c+d.
\]
Write \(\ell(w)\) for the maximum length of a **scattered subsequence** of \(w\) that is a Lyndon word. The exact number of symbols that must be deleted to obtain a longest Lyndon subsequence is
\[
\boxed{D(w):=n-\ell(w)=\min\!\left\{b,\max\!\left(0,c-a+\mathbf{1}_{\{b\ge d\}}\right)\right\}.}
\]
In particular, \(w\) itself is Lyndon precisely when \(a>c\), or when \(a=c\) and \(b<d\). For every \(n\ge4\), among four-run words of length \(n\) beginning in zero, the sharp maximum deletion deficiency is
\[
\boxed{\max D(w)=\left\lfloor\frac{n-2}{2}\right\rfloor.}
\]

Let \(H_{n,k}\) be the number of positive quadruples summing to \(n\) with \(D(w)=k\). Then the entire fixed-length distribution is encoded by the following rational bivariate generating function (formal in \(z\), with \(y\) marking deletion deficiency):
\[
\boxed{\begin{aligned}
\sum_{n\ge4}\sum_{k\ge0}H_{n,k}z^ny^k
={}&\frac{z^4}{(1-z)^4}\\
&+(y-1)\left[
\frac{z^4}{(1-z)^3(1-z^2)(1-yz^2)}
-\frac{z^5}{(1-z)(1-z^2)^2(1-yz^3)}\right].
\end{aligned}}
\]
Equivalently, for every integer \(k\ge1\), the number with deficiency at least \(k\) has generating function
\[
\boxed{\sum_{n\ge4}\#\{(a,b,c,d):a+b+c+d=n,\ D(w)\ge k\}z^n
=\frac{z^{2k+2}}{(1-z)^3(1-z^2)}-
\frac{z^{3k+2}}{(1-z)(1-z^2)^2}.}
\]

If \(W_n\) is selected uniformly among the \(\binom{n-1}{3}\) four-run words of this form, then
\[
\frac{\ell(W_n)}n\ \xrightarrow{\mathrm d}\ X,
\]
where \(X\) has a point mass \(\Pr(X=1)=1/2\) and continuous density
\[
\boxed{f_X(x)=3(2x-1)^2,\qquad \tfrac12<x<1.}
\]
In particular, \(\mathbb E[\ell(W_n)]=\frac{15}{16}n+O(1)\). This distribution is *not* the distribution of longest Lyndon contiguous factors.

## Assumptions and scope

A subsequence is obtained by deleting any subset of positions without changing the order of the remaining positions; the retained positions need not be consecutive. A nonempty word is Lyndon when it is strictly lexicographically smaller than every nonempty proper suffix. The binary alphabet is ordered \(0<1\). All four run lengths are strictly positive. The count \(H_{n,k}\) treats different run-length quadruples as different words, not different occurrences of the same subsequence. Words beginning in one, other alphabets, empty runs, and cyclicly indexed words are outside the stated theorem.

## Proof

**1. Structural Lyndon criterion.** Every binary Lyndon word of length exceeding one starts in zero and ends in one: starting in one or ending in zero gives a strictly smaller proper suffix, unless the word is unary, in which case only length one is Lyndon. Consequently a nontrivial Lyndon subsequence of \(w\) has either two or four nonempty alternating runs. Every two-run word \(0^i1^j\), for \(i,j\ge1\), is Lyndon. A four-run word
\[
0^i1^j0^k1^l\quad (i,j,k,l\ge1)
\]
is Lyndon exactly when \(i>k\), or when \(i=k\) and \(j<l\). Indeed, all suffixes beginning in one are lexicographically larger, suffixes starting inside a zero run are larger than the suffix starting at the beginning of that run, and comparison with \(0^k1^l\) gives exactly the displayed criterion. This also settles equality cases, because a proper suffix that is a prefix of the whole word is smaller.

**2. Exact maximization.** The longest possible two-run subsequence has length
\[
M_2=a+d+\max\{b,c\}=n-\min\{b,c\}.
\]
Its two realizations retain the first zeros and both one runs (deleting the middle zeros), or both zero runs and the last ones (deleting the first ones). Four-run Lyndon subsequences must retain positive amounts from each of the four original runs, and obey the criterion of Step 1.

If \(a>c\), the whole word is Lyndon. If \(a=c\) and \(b<d\), the whole word is also Lyndon. If \(a=c\) and \(b\ge d\), the whole word is not Lyndon, while deleting one middle zero (when \(a\ge2\)) or the entire one-symbol middle zero run (when \(a=1\)) yields a Lyndon subsequence of length \(n-1\).

Suppose \(a<c\) and \(b<d\). In the four-run case, \(i=k\) forces deletion of at least \(c-a\) middle zeros, while \(i>k\) forces at least \(c-a+1\) deletions. Keeping \(i=k=a\) and \(j=b<d=l\) attains cost \(c-a\). A two-run subsequence has deletion cost at least \(\min\{b,c\}\), and deleting the first one run costs exactly \(b\). Thus the optimum cost is \(\min\{b,c-a\}\).

Suppose \(a<c\) and \(b\ge d\). Any four-run Lyndon subsequence with \(i>k\) loses at least \(c-a+1\) middle zeros. With \(i=k\), the condition \(j<l\le d\) forces at least one further deletion from the first one run, on top of at least \(c-a\) deleted zeros. Thus every four-run solution costs at least \(c-a+1\). When \(a\ge2\), retaining \(i=a\), \(k=a-1\), and all ones attains this cost. When \(a=1\), \(c-a+1=c\), and the two-run solution suffices. As \(c-a+1\le c\), the optimum deletion cost is \(\min\{b,c-a+1\}\). All four cases combine to give the asserted closed formula.

**3. Sharp deficiency.** If \(D(w)\ge k\ge1\), then \(b\ge k\) and \(c\ge a+k-1\), so
\[
n=a+b+c+d\ge 2k+2.
\]
Hence \(D(w)\le\lfloor(n-2)/2\rfloor\). For \(k=\lfloor(n-2)/2\rfloor\), the positive quadruple \((a,b,c,d)=(1,k,n-k-2,1)\) attains \(D=k\), proving sharpness for every \(n\ge4\).

**4. Exact distribution.** Fix \(k\ge1\). On \(b<d\), the condition \(D(w)\ge k\) is equivalent to \(b\ge k\), \(c\ge a+k\). Summing the independent pairs of run lengths gives
\[
\sum_{\substack{a,b,c,d\ge1\\b<d,\ D\ge k}}z^{a+b+c+d}
=\frac{z^{3k+3}}{(1-z)^2(1-z^2)^2}.
\]
On \(b\ge d\), the condition is equivalent to \(b\ge k\), \(c\ge a+k-1\), yielding
\[
\sum_{\substack{a,b,c,d\ge1\\b\ge d,\ D\ge k}}z^{a+b+c+d}
=\frac{z^{2k+2}}{(1-z)^3(1-z^2)}-
\frac{z^{3k+2}}{(1-z)^2(1-z^2)^2}.
\]
Their sum is the claimed tail generating function. For any nonnegative integer deficiency, the identity
\[
y^D=1+(y-1)\sum_{k=1}^D y^{k-1}
\]
and two geometric-series sums prove the stated rational bivariate generating function. Differentiation at \(y=1\) gives the exact first-moment generating function
\[
\sum_{a,b,c,d\ge1}D(w)z^{a+b+c+d}
=\frac{z^4}{(1-z)^3(1-z^2)^2}
-\frac{z^5}{(1-z)(1-z^2)^2(1-z^3)}.
\]
Its coefficient of \(z^n\) is \(n^4/96+O(n^3)\), while \(\binom{n-1}{3}=n^3/6+O(n^2)\), proving \(\mathbb E[D(W_n)]=n/16+O(1)\).

**5. Limiting distribution.** The rescaled positive composition of \(n\) converges to the uniform Dirichlet distribution \((A,B,C,E)\) on the simplex of four nonnegative coordinates summing to one. The indicator in Step 2 contributes at most one, hence
\[
D(W_n)/n\xrightarrow{\mathrm d}Y=\min\{B,(C-A)_+\}.
\]
For \(0\le t\le1/2\), the simplex constraints \(B>t\) and \(C>A+t\) give, by the change of variables \(B=t+u\), \(C=A+t+v\),
\[
\Pr(Y>t)=6\int_{\substack{A,u,v\ge0\\2A+u+v\le1-2t}}dA\,du\,dv
=\frac12(1-2t)^3.
\]
For \(t>1/2\) this probability is zero. The discontinuity at \(t=0\) gives \(\Pr(Y=0)=1/2\); on \((0,1/2)\) its density is \(3(1-2t)^2\). Since \(X=1-Y\), the claimed atom and density follow, with mean \(15/16\).

## Verification

Run `python3 verify.py` with Python 3 and its standard library. This independently enumerates every distinct subsequence of each word for all \(625\) parameter quadruples with entries in \(\{1,\ldots,5\}\), checks the Lyndon suffix definition directly, and compares the exact maximum against the formula. It separately enumerates all \(91{,}390\) positive four-part compositions with total lengths from \(4\) to \(40\), checking the complete deficiency histogram against coefficients of the rational tail generating function and checking every sharp extremum in that range. These are finite checks; the preceding five proof steps establish the unbounded claims.

## Relationship to prior work

Bannai, I, Kociumaka, Köppl, and Puglisi introduced a polynomial-time general algorithm for longest Lyndon subsequences, initially publicly posted on 2022-01-18 and expanded in the open-access 2023 Algorithmica paper. The original 2022 preprint and the complete expanded open-access article (introduction, Section 4 on longest Lyndon subsequences, Section 5 on common subsequences, and conclusions) were compared against the precise present theorem. Its algorithms cover arbitrary strings computationally, but it neither states this four-run deletion formula nor derives the rational fixed-length distribution or the Dirichlet limiting law. It treats a unique-character special case, which cannot encompass positive four-run binary inputs with repeated letters. These observations are statements about inspected material, not a claim that computation for the family was previously impossible.

Hirakawa, Nakashima, Inenaga, and Takeda (2021) study counts of Lyndon subsequences (maximal/expected total count and expected distinct count), not the **length of a longest** Lyndon subsequence of a specified four-run word; their complete five-section public preprint was inspected. Urabe et al. (2018) study longest **contiguous** Lyndon substrings under edits, a distinct invariant. General Lyndon-factor enumeration for four-run binary words counts contiguous factors, whereas this theorem concerns the maximum length of an arbitrarily scattered Lyndon subsequence. No equivalence to those factor statements is used or asserted. The remaining possibility of an unindexed equivalent specialization has not been eliminated.

## Limitations

This is a result for positive binary four-run words beginning in zero under the order \(0<1\). It does not classify all alphabets, all run counts, or the number of distinct maximizing subsequences. The limiting law is for uniformly selected positive compositions, not independently sampled binary letters. Verification code checks finitely many cases and is not a certificate for all lengths. Originality assessment is based on identified published sources and indexed records; it is not an absolute proof of priority. Independent audit has not been performed.

## References

1. H. Bannai, T. I, T. Kociumaka, D. Köppl, S. J. Puglisi, *Computing Longest (Common) Lyndon Subsequences*, arXiv:2201.06773, first version dated 2022-01-18, https://arxiv.org/abs/2201.06773.
2. H. Bannai, T. I, T. Kociumaka, D. Köppl, S. J. Puglisi, *Computing Longest Lyndon Subsequences and Longest Common Lyndon Subsequences*, Algorithmica 86 (2024), 735–756, open-access article published online 2023-05-06, https://doi.org/10.1007/s00453-023-01125-z.
3. Y. Urabe, Y. Nakashima, S. Inenaga, H. Bannai, M. Takeda, *Longest Lyndon Substring After Edit*, CPM 2018, LIPIcs 105, Article 19, https://doi.org/10.4230/LIPIcs.CPM.2018.19.

4. R. Hirakawa, Y. Nakashima, S. Inenaga, M. Takeda, *Counting Lyndon Subsequences*, arXiv:2106.01190, publicly posted 2021-06-02, https://arxiv.org/abs/2106.01190.
