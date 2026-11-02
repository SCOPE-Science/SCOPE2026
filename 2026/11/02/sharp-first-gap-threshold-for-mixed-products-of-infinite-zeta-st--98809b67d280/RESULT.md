# Sharp first-gap threshold for mixed products of infinite zeta-star values

## Finding
For every integer \(q\ge2\), a canonical bounded gap of the upper-index-restricted infinite zeta-star set has a multiplicative ratio lying strictly between consecutive endpoint products:
\[
A_{q+2}<\frac{R_q}{L_q}<A_{q+1},\qquad
A_s=\prod_{n=2}^{\infty}(1-n^{-s})^{-1}.
\]
Consequently, for every integer \(p\ge q+2\), the mixed product \(D_qT_p\) is **not an interval**: it omits \((L_qA_p,R_q)\). The canonical gap closes as a *diameter obstruction* at exactly \(p=q+1\). No assertion is made about whether other gaps persist when \(p\le q+1\).

## Assumptions and scope
For a finite admissible index, write \(\zeta^\star(k_1,\ldots,k_r)=\sum_{n_1\ge\cdots\ge n_r\ge1}\prod_{i=1}^r n_i^{-k_i}\). The infinite-index correspondence \(\eta\), and its order and natural-gap descriptions, are those in Li--Yang (2026, arXiv:2610.29100), Section 2. The set \(D_q=\eta(\mathcal D_q)\) consists of the values for sequences with \(2\le k_1\le q\), \(1\le k_i\le q\) for \(i\ge2\), excluding the divergent sequence; \(T_p=\overline{\eta(\mathcal T_p)}\) has all entries at least \(p\), with closure in \(\mathbb R\). The integers \(p,q\) satisfy \(p,q\ge2\). The cited endpoint formulas give \(T_p\subset[1,A_p]\), with \(1,A_p\in T_p\), and \(A_s\) is strictly decreasing for integer \(s\ge2\).

Put \(F_m(q)=\prod_{n=2}^m(1-n^{-q})^{-1}\), with \(F_1(q)=1\). Define
\[
(L_q,R_q)=
\begin{cases}
(2\zeta(3),\,4\zeta(3)-2),&q=2,\\
\left(\zeta(2),\,\displaystyle\sum_{m=1}^{\infty}\frac{F_m(q)}{m^2}\right),&q\ge3.
\end{cases}
\]
The first case is the natural gap with prefix \((2)\) and split digit \(1\); the second has empty prefix and split digit \(2\), in the notation of the cited natural-gap construction. Both endpoints belong to \(D_q\) and the open interval contains no point of \(D_q\).

## Proof
**1. Identification of the gaps.** In Li--Yang (2026, arXiv:2610.29100), equations (2.4)--(2.7), a natural gap is \((\eta(P,i+1,\{1\}^{\infty}),\eta(P,i,\{q\}^{\infty}))\). For \(q\ge3\) choose empty \(P\) and \(i=2\). The first endpoint is \(\zeta^\star(2)=\zeta(2)\), and (2.4) gives the stated series for the second. For \(q=2\), choose \(P=(2)\), \(i=1\). Its left endpoint is \(\zeta^\star(2,1)=2\zeta(3)\). Since \(F_m(2)=2m/(m+1)\), the right endpoint equals
\[
2\sum_{n=1}^{\infty}\frac{H_{n+1}-1}{n^2}=4\zeta(3)-2,
\]
using \(\sum_{n\ge1}H_n/n^2=2\zeta(3)\) and \(\sum_{n\ge1}[n^2(n+1)]^{-1}=\zeta(2)-1\). These are the designated genuine open gaps.

**2. Lower endpoint-product inequality when \(q\ge3\).** Write \(Z=\zeta(2)\), \(t=2^{-q}\), and \(c=(Z-1)/Z\). Since \(F_m(q)\ge(1-t)^{-1}\) whenever \(m\ge2\),
\[
\frac{R_q}{L_q}\ge1+\frac{ct}{1-t}.
\]
The elementary bound \(Z>8/5\) gives \(c>3/8\). Set \(S_s=\sum_{n=2}^{\infty}n^{-s}\). For \(s=q+2\ge5\), sum--integral comparison yields
\[
S_s\le2^{-s}\left(1+\frac2{s-1}\right)\le\frac{3t}{8}.
\]
Expanding the Euler product into nonnegative monomials, the sum of complete homogeneous monomials of degree \(j\) is at most \(S_s^j\), so
\[
A_s\le(1-S_s)^{-1}\le(1-3t/8)^{-1}.
\]
Because \(0<t<1\) and \(c>3/8\),
\[
\frac{R_q}{L_q}>1+\frac{3t/8}{1-3t/8}\ge A_{q+2}.
\]
Indeed, \(Z>1+1/4+1/9+\int_4^{\infty}x^{-2}\,dx=29/18>8/5\).

**3. Upper endpoint-product inequality when \(q\ge3\).** Put \(S=S_q\), \(v_m=\sum_{n=2}^m n^{-q}\), and
\[
W_n=\frac{\sum_{m=n}^{\infty}m^{-2}}{Z}\quad(n\ge2).
\]
From the nonnegative product expansion, \(F_m(q)-1\le v_m/(1-S)\). Since \(\sum_{m=n}^{\infty}m^{-2}\le n^{-2}+n^{-1}\), the sequence \(n\sum_{m=n}^{\infty}m^{-2}\) is nonincreasing: the difference of the terms at \(n+1\) and \(n\) equals \(\sum_{m=n}^{\infty}m^{-2}-(n+1)/n^2\le0\). Therefore
\[
nW_n\le 2\frac{Z-1}{Z}<\frac{26}{33},
\]
where \(Z<33/20\): convexity of \(x^{-2}\) gives \(n^{-2}<\int_{n-1/2}^{n+1/2}x^{-2}\,dx\), hence the tail from index \(3\) is below \(\int_{5/2}^{\infty}x^{-2}\,dx=2/5\). Also for all \(q\ge3\),
\[
S\le S_3\le\frac18+\frac1{27}+\frac1{64}+\frac1{32}<\frac7{33}.
\]
Hence \(nW_n<1-S\). By interchanging absolutely convergent nonnegative sums,
\[
\begin{aligned}
\frac{R_q}{L_q}-1
&=\frac1Z\sum_{m\ge2}\frac{F_m(q)-1}{m^2}\\
&\le\frac1{1-S}\sum_{n\ge2}n^{-q}W_n
<\sum_{n\ge2}n^{-(q+1)}<A_{q+1}-1.
\end{aligned}
\]
This gives the second strict inequality.

**4. The exceptional small index \(q=2\).** The gap ratio is \(R_2/L_2=2-1/\zeta(3)\). The elementary bounds
\[
\frac76<\zeta(3)<\frac{91}{74}
\]
follow respectively from the first four terms and from \(1+1/8+1/27+\int_3^\infty x^{-3}\,dx\). The Euler product inequalities give
\[
A_4\le\frac{48}{43}<\frac87<\frac{R_2}{L_2}
<\frac{108}{91}\le A_3.
\]
For the first, use \(S_4\le5/48\); for the last, keep only the factors indexed by \(2\) and \(3\) in \(A_3\). Thus the strict threshold also holds at \(q=2\).

**5. Consequence for mixed products.** For \(p\ge q+2\), monotonicity gives \(A_p\le A_{q+2}<R_q/L_q\). Every \(x\in D_q\) lies in \((0,L_q]\cup[R_q,\infty)\), and every \(y\in T_p\) lies in \([1,A_p]\); therefore every product lies in \((0,L_qA_p]\cup[R_q,\infty)\). The interval \((L_qA_p,R_q)\) is omitted and nonempty. Since its endpoints are obtained from points in \(D_q\) and \(T_p\), the product has values on each side, proving it is not an interval. If \(p\le q+1\), then \(A_p\ge A_{q+1}>R_q/L_q\), so this particular diameter-obstruction interval is empty; this does *not* prove the product is an interval.

## Verification
The accompanying standalone script `number_theory_gap_verifier.py` checks seven exact rational inequalities used in the proof and numerically evaluates the strict bracketing for every \(2\le q\le30\), with no assumption of asymptotic completeness. Run `python3 number_theory_gap_verifier.py` using Python's standard library. The program's finite checks are corroboration only; the proof above establishes all cases and does not depend on its floating-point calculations.

## Relationship to prior work
Li and Yang (arXiv:2610.29100v1, 21 October 2026) classify **mixed sums** of upper-index and lower-index restricted sets; their equations (2.4)--(2.7) supply the natural gaps used here, and their introduction leaves **mixed products** for further study. Their additive gap criterion compares the gap length with \(A_p-1\), whereas the multiplicative obstruction requires the different inequality \(R_q/L_q>A_p\), which does not follow automatically. Li and Yang (arXiv:2603.26399v1, 27 March 2026) establish **self-products** \(D_qD_q\) and \(T_pT_p\); neither is the mixed product \(D_qT_p\). The present result gives one global negative parameter range and an exact threshold for one specified natural gap, not a complete mixed-product classification.

## Limitations
The theorem does not classify mixed products for \(p\le q+1\), does not assert that the specified gap is largest, and does not address gaps away from the designated natural gap. The derivation relies on the published infinite zeta-star correspondence and its natural-gap construction. Literature comparisons support but do not certify priority; independent review has not been performed.

## References
1. Jiangtao Li and Siyu Yang, *Mixed sums of infinite multiple zeta-star values with restricted indices*, arXiv:2610.29100v1 (first public 21 October 2026), especially Section 2 and Section 3. https://arxiv.org/abs/2610.29100
2. Jiangtao Li and Siyu Yang, *Arithmetic sums and products of infinite multiple zeta-star values*, arXiv:2603.26399v1 (first public 27 March 2026), especially Theorems 1.1--1.2. https://arxiv.org/abs/2603.26399
