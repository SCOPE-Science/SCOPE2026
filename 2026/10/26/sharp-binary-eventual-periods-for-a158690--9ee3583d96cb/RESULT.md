# Sharp binary eventual periods for A158690

## Finding
Let \(a(n)\), for \(n\ge0\), be defined by the formal exponential generating function
\[
\sum_{n\ge0}a(n)\frac{t^n}{n!}
=1+\sum_{m\ge1}\prod_{j=1}^{m}\bigl(1-e^{-(2j-1)t}\bigr).
\]
For each integer \(r\ge4\), the **least eventual period** of \(a(n)\) modulo \(2^r\) is exactly
\[
\boxed{P_r=2^{r-3}}.
\]
The remaining dyadic moduli have least eventual periods \(P_1=1\), \(P_2=P_3=2\). More precisely, for every integer \(k\ge0\) and every even integer \(n\ge k+5\),
\[
\boxed{\nu_2\bigl(a(n+2^{k+1})-a(n)\bigr)=k+4}.
\]
Here an eventual period \(T\ge1\) modulo \(2^r\) means that \(a(n+T)\equiv a(n)\pmod{2^r}\) for all sufficiently large integer \(n\). All assertions concern this single integer sequence, not every sequence expressible as \(G(e^t-1)\).

## Assumptions and scope
All generating functions are formal over the rationals. The defining products have order at least their number of factors, so every coefficient is a finite sum and the integers \(a(n)\) are well defined. The coefficient representation below uses an integral series \(H(y)\in\mathbb Z[[y]]\); its integrality follows directly because \((1+y)^{-d}\in\mathbb Z[[y]]\) for positive integer \(d\). The period statement has no unstated analytic or asymptotic hypotheses. The explicit bound \(n\ge r\) suffices for the periodicity claim when \(r\ge4\); it is not asserted to be the minimal preperiod.

## Proof
**1. Integral power-sum expansion.** Write \(H(y)=\sum_{m\ge0}c_my^m\), where
\[
H(y)=1+\sum_{m\ge1}\prod_{j=1}^m\bigl(1-(1+y)^{-(2j-1)}\bigr)\in\mathbb Z[[y]].
\]
Substituting \(y=e^t-1\) recovers the defining exponential generating function. The Stirling identity gives, for \(n\ge1\),
\[
a(n)=\sum_{m=0}^{n}c_m\,m!\,S(n,m),\qquad
m!S(n,m)=\sum_{j=0}^{m}(-1)^{m-j}\binom mj j^n.
\]
Fix \(r\ge4\). Choose an integer \(M\) with \(2^{\max(r,5)}\mid M!\), and define the integers
\[
w_j=\sum_{m=j}^{M-1}(-1)^{m-j}\binom mjc_m\quad(0\le j<M).
\]
For every \(n\ge1\), factorial divisibility yields
\[
 a(n)\equiv\sum_{j=1}^{M-1}w_jj^n\pmod{2^{\max(r,5)}}.\tag{1}
\]
No convergence of the right-hand side as \(M\to\infty\) is invoked.

**2. A base coefficient determines the decisive parity.** For odd positive \(j\) put \(\beta_j=(j^2-1)/8\in\mathbb Z\), and set
\[
B=\sum_{\substack{1\le j<M\\j\ \mathrm{odd}}}w_j\beta_j.
\]
Subtract equation (1) at \(n=6\) and \(n=8\), reducing modulo \(32\). For even \(j\), \(j^6(j^2-1)\equiv0\pmod{32}\); for odd \(j\), \(j^6\equiv1\pmod4\). Therefore
\[
a(8)-a(6)\equiv8B\pmod{32}.\tag{2}
\]
Direct finite expansion of the defining generating function gives
\[
a(6)=1431665,\qquad a(8)=6646603073.
\]
The difference is \(16\pmod{32}\), so the crucial invariant is
\[
\boxed{B\equiv2\pmod4}.\tag{3}
\]
The computation is independently reproducible via the finite subset-sum formula: for each positive \(n\),
\[
a(n)=\sum_{m=1}^n\ \sum_{S\subseteq\{1,3,\ldots,2m-1\}}
 (-1)^{|S|+n}\left(\sum_{d\in S}d\right)^n.
\]

**3. Improved upper period.** For \(r\ge4\), put \(T=2^{r-3}\). For odd \(j\), the binomial theorem applied to \(j^2=1+8\beta_j\) gives
\[
j^T-1\equiv2^{r-1}\beta_j\pmod{2^r}.\tag{4}
\]
Indeed, for \(r=4\) this is an equality with \(T=2\), while for \(r\ge5\) all terms of binomial degree at least two have valuation at least \(r\). If \(n\ge r\), then \(j^n\equiv0\pmod{2^r}\) for every even \(j\). Consequently (1), (3), and (4) give
\[
a(n+T)-a(n)\equiv2^{r-1}\sum_{j\ \mathrm{odd}}w_jj^n\beta_j
\equiv2^{r-1}B\equiv0\pmod{2^r},\quad n\ge r.
\]
The middle congruence uses \(j^n\equiv1\pmod2\) for odd \(j\).

**4. Every shorter period fails.** For \(r\ge5\), let \(U=T/2=2^{r-4}\). Expanding \((1+8\beta_j)^{2^{r-5}}\) gives
\[
j^U-1\equiv 2^{r-2}\beta_j\pmod{2^r}\qquad(j\ \mathrm{odd}).\tag{5}
\]
For completeness, the higher binomial terms satisfy
\[
\nu_2\!\left(8^h\binom{2^{r-5}}h\right)
\ge 3h+(r-5)-\nu_2(h)\ge r,\qquad h\ge2,
\]
when \(h\le2^{r-5}\); for \(r=5\), no higher terms occur. If \(n\ge r\) is even, then \(j^n\equiv1\pmod4\) for all odd \(j\). Equations (1), (3), and (5) imply the **exact nonzero residue**
\[
a(n+U)-a(n)\equiv2^{r-2}B\equiv2^{r-1}\pmod{2^r}.\tag{6}
\]
Thus \(U\) is not an eventual period. Since the least eventual period divides every eventual period, and \(T\) is a power of two, its only possible proper divisors divide \(U\); hence the least period equals \(T\). Replacing \(r\) by \(k+5\) in (6) proves the stated exact valuation for all even \(n\ge k+5\).

**5. Small powers.** Modulo \(4\), the finite Stirling expansion, for \(n\ge2\), is
\[
a(n)\equiv2+3\cdot3^n\pmod4,
\]
which equals \(1\) for even \(n\) and \(3\) for odd \(n\). Modulo \(8\), for \(n\ge3\), it gives \(a(n)\equiv2+7\cdot3^n\pmod8\), equal to \(1\) at even \(n\) and \(7\) at odd \(n\). Both have least eventual period \(2\); moreover these mod-\(4\) residues show that the period \(2\) found above for \(r=4\) cannot be shortened. Modulo \(2\), all terms \(a(n)\) are odd, so the least period is \(1\). This completes the proof.

## Verification
The finite coefficients \(a(6)\) and \(a(8)\) were reconstructed by integer-only subset expansion rather than inferred from the period conjecture. The included standalone `VERIFY.py` independently computes the truncated integral-series coefficients \(c_m\), converts them to finite power-sum weights, and verifies the asserted period and sharp half-step residues for \(2\le r\le16\) over multiple indices; it returned `VERIFY_OK 393`. These finite tests are consistency checks, not a substitute for the proof of the universal statement.

## Relationship to prior work
Kallat (2026), Theorem 2.6 and Proposition 2.1, proves that for any \(G(e^t-1)\) with integral \(G\), the Carmichael value \(\lambda(2^r)=2^{r-2}\) is an eventual period for \(r\ge3\). That does **not** imply the smaller period or its minimality. The OEIS A158690 entry records the isolated observation that modulo \(16\), the eventual period appears to be \(2\); the present theorem proves the uniform pattern for all powers \(2^r\), and the exact valuations that force minimality. Straub's prime-power Fishburn congruences concern different ordinary generating-function coefficients and arithmetic-progression vanishings rather than these exponential-series eventual periods.

## Limitations
The theorem concerns only powers of two; it makes no determination of least eventual periods for odd or mixed moduli, and does not classify the optimal preperiod index. Independently established mathematical validation remains outstanding. Prior-art searches cannot exclude an unpublished or implicit general formulation elsewhere.

## References
1. A. Kallat, *A Proof of Bala's Congruence Conjectures for A158690*, arXiv:2609.07238v1, first publicly submitted September 7, 2026; especially Sections 2 and 3, https://arxiv.org/html/2609.07238v1 .
2. OEIS Foundation, *A158690*, https://oeis.org/A158690 (sequence, coefficient values, and the recorded modulo-16 observation).
3. A. Straub, *Congruences for Fishburn numbers modulo prime powers*, International Journal of Number Theory 11 (2015), 1679–1690, arXiv:1407.7521, https://arxiv.org/abs/1407.7521 .
