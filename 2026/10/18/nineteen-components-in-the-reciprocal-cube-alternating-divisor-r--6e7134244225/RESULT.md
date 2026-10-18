# Nineteen components in the reciprocal-cube alternating divisor range

## Finding

For every positive integer \(n\), let \(s_{-3}\) be the multiplicative arithmetic function specified at prime powers by
\[
s_{-3}(p^e)=\sum_{j=0}^{e}(-p^{-3})^j,\qquad e\ge 0.
\]
Its range has an exact nineteen-component closure:
\[
\boxed{\ \overline{\{s_{-3}(n):n\ge1\}}=\bigcup_{i=1}^{19}[T a_i,b_i]\ },\qquad
T=\prod_{p\ge11}(1-p^{-3})=
\frac{1}{\zeta(3)\prod_{p\in\{2,3,5,7\}}(1-p^{-3})}.
\]
The intervals are pairwise disjoint, and their exact rational coefficients are as follows. The displayed table is in increasing order; no endpoints are estimated or rounded in its assertions.

| Component | Exact left endpoint | Exact right endpoint |
|---:|---:|---:|
| 1 | \(T\cdot \frac{15314}{18375}\) | \(\frac{25426807}{30375000}\) |
| 2 | \(T\cdot \frac{247}{294}\) | \(\frac{4921}{5832}\) |
| 3 | \(T\cdot \frac{99541}{117600}\) | \(\frac{13357}{15552}\) |
| 4 | \(T\cdot \frac{5301}{6125}\) | \(\frac{1818375807}{2100875000}\) |
| 5 | \(T\cdot \frac{217}{250}\) | \(\frac{108507}{125000}\) |
| 6 | \(T\cdot \frac{171}{196}\) | \(\frac{117307}{134456}\) |
| 7 | \(T\cdot \frac{7}{8}\) | \(\frac{7}{8}\) |
| 8 | \(T\cdot \frac{68913}{78400}\) | \(\frac{6620706313287}{7529536000000}\) |
| 9 | \(T\cdot \frac{302157}{343000}\) | \(\frac{56439141}{64000000}\) |
| 10 | \(T\cdot \frac{1767}{2000}\) | \(\frac{883557}{1000000}\) |
| 11 | \(T\cdot \frac{11115}{12544}\) | \(\frac{427114787}{481890304}\) |
| 12 | \(T\cdot \frac{9747}{10976}\) | \(\frac{3641}{4096}\) |
| 13 | \(T\cdot \frac{57}{64}\) | \(\frac{57}{64}\) |
| 14 | \(T\cdot \frac{122512}{128625}\) | \(\frac{3632401}{3796875}\) |
| 15 | \(T\cdot \frac{988}{1029}\) | \(\frac{703}{729}\) |
| 16 | \(T\cdot \frac{42408}{42875}\) | \(\frac{1818375807}{1838265625}\) |
| 17 | \(T\cdot \frac{124}{125}\) | \(\frac{15501}{15625}\) |
| 18 | \(T\cdot \frac{342}{343}\) | \(\frac{117307}{117649}\) |
| 19 | \(T\cdot 1\) | \(1\) |


There are therefore exactly eighteen nonempty complementary gaps between these components, including the particularly large gap between the thirteenth and fourteenth components.

## Assumptions and scope

The assertion holds unconditionally for the function \(s_{-3}\) on all positive integers. Only multiplicativity, elementary rational inequalities, Euler's product identity for \(\zeta(3)\), the standard subsum-interval lemma, and the unconditional prime-in-a-short-interval theorem of Nagura are invoked. The theorem does not concern arbitrary real exponents, nor the unrelated unitary divisor function.

## Proof

**1. The prime tail is an interval.** For primes \(p\ge11\), define \(u_p=-\log(1-p^{-3})>0\), and define \(T=\prod_{p\ge11}(1-p^{-3})\). The series \(\sum_{p\ge11}u_p\) converges. We claim that for every prime \(p\ge11\),
\[
 u_p\le \sum_{q>p}u_q.
\]
Indeed, this is equivalent to \(\prod_{q>p}(1-q^{-3})\le1-p^{-3}\). For the five primes \(p=11,13,17,19,23\), this is certified directly by the following exact rational finite-product inequalities, where the primes \(q\) used respectively are
\[
\begin{array}{c|l}
p & q\\\hline
11&13,17,19\\
13&17,19,23,29\\
17&19,23\\
19&23,29,31\\
23&29,31,37
\end{array}
\]
and in every row \(\prod_q(1-q^{-3})\le1-p^{-3}\). These are exact tests in the accompanying verifier. For primes \(p\ge29\), Nagura's prime-interval theorem yields three successive primes \(q_j>p\) with \(q_j<(6/5)^j p\), for \(j=1,2,3\). Put \(t=p^{-3}\) and \(c_j=(5/6)^{3j}\). Writing \(S_1=\sum c_j\) and \(S_2=\sum_{i<j}c_ic_j\), exact rational arithmetic confirms \(S_1>1\) and \(S_1-1>S_2/29^3\). Consequently
\[
\prod_{q>p}(1-q^{-3})\le\prod_{j=1}^{3}(1-c_jt)
\le1-S_1t+S_2t^2\le1-t.
\]
The elementary subsum-interval lemma states that if nonnegative summable terms satisfy each term being no larger than the sum of its successors, then their subsums fill the entire interval from zero to the total sum. Applying it to \(u_p\), then exponentiating negatively, shows that the closure of products \(\prod_{p\in F}(1-p^{-3})\), over finite sets of primes \(F\subseteq\{11,13,\dots\}\), is exactly \([T,1]\). Since all factors \(s_{-3}(p^e)\) for \(e\ge0\) lie in \([1-p^{-3},1]\), the closure of **all** contributions from primes \(p\ge11\), allowing arbitrary exponents, is also exactly \([T,1]\).

**2. Every small-prime exponent reduces to finite choices.** Write \(f_p(e)=\sum_{j=0}^{e}(-p^{-3})^j\). For \(p=3,5,7\), every exponent \(e\ge1\) satisfies \(f_p(1)\le f_p(e)\le f_p(2)\). Direct exact inequalities give \(T f_p(2)\le f_p(1)\) for each such \(p\), so the two intervals \([Tf_p(1),f_p(1)]\) and \([Tf_p(2),f_p(2)]\) overlap and cover \([Tf_p(1),f_p(2)]\). Thus, when the tail may range over \([T,1]\), all these exponents can be replaced by \(e=1\) or \(e=2\). We also retain \(e=0\).

For \(p=2\), every \(e\ge3\) satisfies \(f_2(3)\le f_2(e)\le f_2(4)\), and exact arithmetic gives \(T f_2(4)\le f_2(3)\). Hence exponents \(0,1,2,3,4\) suffice. The interval-replacement argument remains valid after multiplying by any fixed positive contributions of the other three small primes; iterating gives
\[
\overline{s_{-3}(\mathbb N)}
=\bigcup_{\substack{e_2\in\{0,1,2,3,4\}\\ e_3,e_5,e_7\in\{0,1,2\}}}
\left[T\prod_{p\in\{2,3,5,7\}}f_p(e_p),\ \prod_{p\in\{2,3,5,7\}}f_p(e_p)\right].
\]
The reverse inclusion follows because each small-prime choice is attainable and each number in the tail interval is a limit of squarefree tail products. Thus this identity is an **equality** of closures, not merely an outer bound.

**3. Rigorous finite interval union.** There are exactly \(5\cdot3^3=135\) rational products on the right. Sort these rationals exactly. To decide whether consecutive intervals overlap, an explicit rational enclosure of \(T\) suffices: put \(Q=10^{18}\), \(N=100000\), and
\[
B=\sum_{k=1}^{N}\left\lfloor\frac{Q}{k^3}\right\rfloor,
\qquad Z_-=B/Q,\quad Z_+=(B+N)/Q+\frac{1}{2N^2}.
\]
Term-by-term flooring and the integral tail bound establish \(Z_-\le\zeta(3)\le Z_+\). Writing \(K=\prod_{p\in\{2,3,5,7\}}(1-p^{-3})^{-1}\), set \(T_-=K/Z_+\), \(T_+=K/Z_-\). The exact verifier certifies
\[
\frac{656250000000000000000}{657439264820957127821}\le T\le
\frac{4593750000000000000000}{4602074853554892044747}.
\]
Every proposed overlap \(T a\le b\) is proved by the stronger inequality \(T_+a\le b\); every proposed separation \(T a>b\) is proved by \(T_-a>b\). After enumerating and merging all 135 intervals in increasing rational order, the exact program outputs nineteen groups whose endpoints are precisely those in the table. The **smallest certified separation** is greater than \(0.0000326\), and the **smallest certified overlap** at a joined transition exceeds \(0.0002716\); hence the rational enclosure resolves all comparisons with a strict margin. Finally, each group is a closed interval and neighboring groups are strictly separated, yielding exactly nineteen connected components. \(\square\)

## Verification

Run `python3 verify.py` using Python 3 with its standard library only. The script independently reconstructs all 135 rational local products, the finite exceptional-prime certificates, Nagura-regime rational inequality, small-prime interval reductions, rational \(\zeta(3)\) enclosure, and all nineteen component boundaries. It prints `VERIFY_OK` only if all exact assertions pass, then prints each exact endpoint and its corresponding small-prime exponent vectors. The proof of the infinite tail uses Nagura's theorem and the proved subsum lemma, not extrapolation from an experiment. In the packaged execution, the checker produced `VERIFY_OK`, `distinct_finite_local_products 135`, and `components 19`.

## Relationship to prior work

Colin Defant's 2015 study introduced this exact alternating divisor function, determined its connectedness threshold \(\eta_A\approx1.9011618\), and explicitly asked for the parameters whose range closures have exactly a prescribed number of intervals. This theorem addresses that question at \(r=3\) with an exact component count and all endpoints. A separately published calculation for \(r=2\) determines two intervals but does not imply the \(r=3\) count; the unitary-divisor component question uses different Euler factors. The tail-filling step follows a familiar subsum method, while the 135-product rational classification at this parameter and its 18 certified gaps provide the new determination.

## Limitations

No general formula for the number of components as a function of real \(r\) follows. The discovery of an equivalent earlier calculation in unindexed literature would affect the originality assessment. The finite certificate is rigorous only together with the analytic prime-tail argument; enumeration by itself does not establish the infinite theorem. Independent verification has not been carried out.

## References

1. Colin Defant, *On Ranges of Variants of the Divisor Functions that are Dense*, arXiv:1507.01128 (first posted July 4, 2015), https://arxiv.org/abs/1507.01128 . In particular, the final open problem.
2. Jitsuro Nagura, *On the Interval Containing At Least One Prime Number*, Proceedings of the Japan Academy 28 (1952), 177–181, https://doi.org/10.3792/pja/1195570997 .
3. *Exactly two closure components for the alternating divisor range at parameter two*, published mathematical result (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-exactly-two-closure-components-for-the-alternating-divisor-range--f19c7ab30430 .
