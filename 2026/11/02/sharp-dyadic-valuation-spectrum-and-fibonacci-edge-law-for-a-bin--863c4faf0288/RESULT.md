# Sharp dyadic valuation spectrum and Fibonacci edge law for a binomial-parity sum

## Finding
For each integer \(n\geq0\), let
\[
T(n)=\sum_{k=0}^{n}\left[\binom{6k}{n+3k}\binom nk\pmod 2\right],
\]
where the bracket is the integer \(0\) or \(1\) equal to the parity of the product. Thus the sum is taken **after** reducing each product separately modulo \(2\). The sequence has strictly positive values. For an integer \(r\geq0\), define
\[
M_r=\max_{0\leq n<2^r}\nu_2(T(n)),\qquad
A_r=\#\{0\leq n<2^r:\nu_2(T(n))=M_r\}.
\]
Then the exact valuation spectrum and its maximum are
\[
\{\nu_2(T(n)):0\leq n<2^r\}=\{0,1,\ldots,\lfloor(r+1)/4\rfloor\},
\qquad M_r=\left\lfloor\frac{r+1}{4}\right\rfloor.
\]
Write \(r+1=4a+s\), where \(a\geq0\) and \(0\leq s\leq3\). With \(Q(y)=1-y-y^2\), the number of maximizers is **exactly**
\[
A_r=[y^a]\begin{cases}
Q(y)^{-1},&s=0,\\
Q(y)^{-2},&s=1,\\
Q(y)^{-2}+Q(y)^{-3},&s=2,\\
Q(y)^{-2}+2Q(y)^{-3}+Q(y)^{-4},&s=3.
\end{cases}
\]
In particular, using \(F_0=0\) and \(F_1=1\), one has \(A_{4a-1}=F_{a+1}\) for each \(a\geq1\).

There is also a complete structural characterization: write \(n\) in exactly \(r\) binary digits, permitting initial zeros, and append one final zero. A number \(n\) is a maximizer precisely when the resulting word has a tokenization using only `0`, `10`, `110`, `1110`, and `11111110`, in which the total token deficit is \(s\). The respective deficits are \(1,2,3,0,0\). The natural tokenization (a lone zero or a maximal run of ones together with its terminating zero) is unique.

More generally, let \(D_r(n)=r+1-4\nu_2(T(n))\). For each fixed integer \(d\geq0\), the length generating function
\[
E_d(x)=\sum_{r\geq0}x^{r+1}\#\{0\leq n<2^r:D_r(n)=d\}
\]
is rational, with reduced denominator dividing \((1-x^4-x^8)^{d+1}\). Thus all fixed-distance-from-the-upper-edge counting sequences satisfy explicit constant-coefficient recurrences.

## Assumptions and scope
All integers and valuations are ordinary, and \(\nu_2(t)\) is the exponent of \(2\) in a positive integer \(t\). The binomial coefficient \(\binom ab\) is zero unless \(0\leq b\leq a\) and both indices are nonnegative integers. We include \(n=0\), with \(T(0)=1\), and include \(r=0\) so that the dyadic interval consists of \(\{0\}\). The variables \(x,y\) and the deficit-marking variable \(u\) are formal indeterminates; every rational expression is expanded at zero. There are no unstated large-parameter hypotheses.

## Proof
**1. Previously established run-length identity.** Rampersad and Wiebe (2023 preprint; 2024 published Theorem 14) prove that \(T(n)\) is the run-length transform of the sequence
\[
S(0),S(1),S(2),S(3),\ldots=1,1,1,2,1,3,1,4,\ldots.
\]
Consequently, if the maximal binary one-run lengths of \(n\) are \(\ell_1,\ldots,\ell_h\),
\[
T(n)=\prod_{j=1}^{h}S(\ell_j),\quad
S(2m)=1\ (m\geq1),\quad S(2m-1)=m\ (m\geq1).
\]
For \(n=0\) the empty product equals \(1\). This run-length identity is cited as an established premise, not reproved or claimed as new.

**2. Unique deficit tokenization.** Represent \(n\) using exactly \(r\) bits including leading zeros, and add a trailing zero. Every resulting word is uniquely decomposed left-to-right into the tokens `0` and \(1^{\ell}0\), \(\ell\geq1\). A `0` token has length \(1\) and zero valuation contribution. A \(1^{\ell}0\) token has length \(\ell+1\) and contributes \(\nu_2(S(\ell))\). Define the token deficit by its length minus four times its valuation contribution. The deficits are
\[
\delta(0)=1,\qquad
\delta(1^{\ell}0)=\ell+1-4\nu_2(S(\ell)).
\]
When \(\ell=2m\geq2\), the latter is \(2m+1\geq3\). When \(\ell=2m-1\), it is \(2m-4\nu_2(m)\). If \(b=\nu_2(m)\), then \(m\geq2^b\geq2b\); equality in \(m=2b\) occurs only at \(m=2,4\). Thus every deficit is nonnegative, and the only zero-deficit tokens are `1110` and `11111110`, of lengths \(4\) and \(8\). The only tokens with positive deficit below \(4\) are `0`, `10`, and `110`, with deficits \(1,2,3\), respectively; all other tokens have deficit at least \(4\).

The total word length is \(r+1\), so additivity of the valuation gives the exact equality
\[
D_r(n)=r+1-4\nu_2(T(n))=\sum_{\text{tokens}}\delta(\text{token})\geq0.
\]
Since \(D_r(n)\equiv r+1\pmod4\), the smallest possible deficit is at least \(s\) when \(r+1=4a+s\). It equals \(s\): concatenate \(a\) copies of `1110` and \(s\) copies of `0`, then remove the last zero to obtain a binary word of length \(r\). Hence \(M_r=a\). To achieve every smaller valuation \(j\in\{0,\ldots,a\}\), concatenate \(j\) copies of `1110` followed by \(r+1-4j\) zero tokens. This establishes the claimed spectrum and boundary cases.

**3. Complete maximizers and their exact count.** A word attains \(M_r\) if and only if its deficit is \(s<4\). Such a word can contain only the five tokens stated in the finding, proving the characterization. Introduce \(u\) to mark total deficit. Modulo \(u^4\), the generating function for all token sequences is
\[
H(x,u)\equiv\frac{1}{1-x^4-x^8-xu-x^2u^2-x^3u^3}\pmod{u^4}.
\]
The empty sequence contributes only length zero and does not affect any \(r+1\geq1\). Put \(y=x^4\), \(z=xu\), and \(Q(y)=1-y-y^2\). The necessary coefficient is that of \(y^a z^s\) in
\[
\frac1{Q(y)-z-z^2-z^3}=\sum_{h\geq0}\frac{(z+z^2+z^3)^h}{Q(y)^{h+1}}.
\]
For \(s=0,1,2,3\), the coefficients of \(z^s\) are respectively \(Q^{-1}\), \(Q^{-2}\), \(Q^{-2}+Q^{-3}\), and \(Q^{-2}+2Q^{-3}+Q^{-4}\). This is the asserted formula for \(A_r\). The standard Fibonacci generating series \(Q^{-1}=\sum_{a\geq0}F_{a+1}y^a\) proves the special Fibonacci identity.

**4. Fixed-deficit rationality.** The exact, not truncated, bivariate generating function for nonempty token sequences is
\[
H(x,u)-1=
\frac{1}{1-x-\sum_{\ell\geq1}x^{\ell+1}u^{\ell+1-4\nu_2(S(\ell))}}-1.
\]
For each fixed deficit \(d\), only finitely many one-run lengths have deficit at most \(d\). Indeed for odd length \(2m-1\), the deficit \(2m-4\nu_2(m)\) tends to infinity with \(m\), because \(\nu_2(m)\leq\log_2m\); for even lengths the deficit equals length plus one. Separate the two zero-deficit terms \(x^4,x^8\) from the denominator. Writing the remaining positive-deficit contribution as \(B(x,u)\), the identity
\[
H(x,u)=\sum_{j\geq0}\frac{B(x,u)^j}{(1-x^4-x^8)^{j+1}}
\]
holds formally. Since every monomial of \(B\) has \(u\)-degree at least \(1\), only indices \(0\leq j\leq d\) can contribute to \([u^d]\); and for any fixed \(d\), the contributing coefficients of \(B\) are polynomials in \(x\). Multiplying by \((1-x^4-x^8)^{d+1}\) therefore clears every denominator, yielding the stated rationality and divisor bound. Subtracting the empty sequence only changes the \(d=0\) numerator, not the bound.

## Verification
The accompanying standalone `verify.py` implements exact independent finite checks using Lucas's parity criterion for binomial coefficients, a direct binary one-run valuation, and independent dynamic programming. On execution it reports `VERIFY_OK` after 4096 direct binomial-sum comparisons, 2000 token-deficit tests, 121 distribution recurrences, and 262143 independent brute-force dyadic evaluations through \(r=17\). No floating-point arithmetic is involved. The proof above covers all \(n\) and \(r\) and does not infer an infinite statement from these finite checks. To reproduce, run `python3 verify.py` from the extracted standalone package directory.

## Relationship to prior work
The run-length identity in Step 1 is a previously published theorem: Rampersad–Wiebe, arXiv:2309.04012 (first posted September 7, 2023), published in *Integers* 24 (2024), Theorem 14. Their Section 6 computes **average values** of selected run-length transforms, not the exact dyadic maximum, its full extremizer language, the sharp valuation spectrum, or the fixed-deficit rational recurrences. Kropf–Wagner (2017), *On q-Quasiadditive and q-Quasimultiplicative Functions*, establish general block factorization and limit theorems for a wide class of digit-based functions. Those general statements do not provide the five-token classification or the coefficient formulas here without further specialization and proof. This contribution is the quantitative arithmetic edge classification built on the known transform identity; it does not assert that the transform identity itself is new.

## Limitations
The result concerns exactly this parity sum, the prime \(2\), and initial intervals bounded by powers of \(2\). It does not determine odd-prime valuations, maxima on arbitrary non-dyadic intervals, or a distributional limit in the center of the valuation range. The coefficient formulas give an exact and reproducible answer, but mathematical priority remains subject to unindexed or implicit specializations of earlier general digit-statistic results. There has been no independent scientific audit.

## References
1. Narad Rampersad and Max Wiebe, *Sums of products of binomial coefficients mod 2 and 2-regular sequences*, arXiv:2309.04012v1, first posted 2023-09-07; *Integers* 24 (2024), paper A73, Theorem 14, DOI: 10.5281/zenodo.13331528. https://arxiv.org/abs/2309.04012 ; https://math.colgate.edu/~integers/y73/y73.pdf
2. Sara Kropf and Stephan Wagner, *On q-Quasiadditive and q-Quasimultiplicative Functions*, *Electronic Journal of Combinatorics* 24(1) (2017), #P1.60, DOI: 10.37236/6373. https://www.combinatorics.org/ojs/index.php/eljc/article/download/v24i1p60/pdf/
