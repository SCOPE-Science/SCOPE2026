# A prime-power divisibility law for Riordan numbers with a unique five-adic resonance

## Finding
For Riordan numbers \(R_0=1\), \(R_1=0\), and \((n+1)R_n=(n-1)(2R_{n-1}+3R_{n-2})\), **every odd prime** \(p\) and integer \(r\ge1\) satisfy
\[
\nu_p(R_{p^r+1})=
\begin{cases}
r+1,&p=5\text{ and }r\text{ even},\\
r,&\text{otherwise}.
\end{cases}
\]
Thus the sole exceptional odd prime is five, and it has a sharp parity-dependent extra factor.

## Assumptions and scope
The Riordan numbers count noncrossing partitions with no singleton blocks, equivalently Motzkin paths without horizontal steps at height zero. Their exact recurrence, with \(R_0=1,R_1=0\), is the definition used here. \(\nu_p(m)\) is the largest exponent \(e\ge0\) such that \(p^e\mid m\), for a nonzero integer \(m\). The quantifiers are over all odd rational primes \(p\) and all positive integers \(r\), without a bounded-index restriction. No claim is made for \(p=2\).

## Proof
Put \(T(z)=z^{-1}+1+z\), and let \(\operatorname{CT}\) denote the Laurent-series constant coefficient. The Catalan numbers \(C_j\) satisfy
\[
C_j=\operatorname{CT}\!\left((1-z)(z^{-1}+2+z)^j\right).
\]
The classical binomial transform \(R_n=\sum_{j=0}^n(-1)^{n-j}\binom nj C_j\) therefore gives the **exact identity**
\[
R_n=\operatorname{CT}\!\left((1-z)T(z)^n\right).\tag{1}
\]
In the ring of formal power series, define
\[
K(z)=\frac{1-z}{T(z)}=\frac{z(1-z)^2}{1-z^3}=\sum_{m\ge1}k_mz^m.
\]
The coefficients obey \(k_m=1\) when \(m\equiv0,1\pmod3\) and \(k_m=-2\) when \(m\equiv2\pmod3\); also \(k_0=0\).

For any prime \(p\), the freshman's-dream congruence \(T(z)^{p^r}\equiv T(z^{p^r})\pmod p\) holds coefficientwise as a Laurent-polynomial congruence. Taking the constant coefficients in (1) and in \(R_{p^r-1}=\operatorname{CT}(K(z)T(z)^{p^r})\) yields
\[
R_{p^r}\equiv1\pmod p,\qquad R_{p^r-1}\equiv k_{p^r}\pmod p.\tag{2}
\]
The recurrence with index \(p^r+1\) reads
\[
R_{p^r+1}=\frac{p^r}{p^r+2}\bigl(2R_{p^r}+3R_{p^r-1}\bigr).\tag{3}
\]
For odd \(p\), the denominator is a \(p\)-adic unit. By (2), the parenthesis is congruent to \(5\pmod p\) when \(p^r\equiv0,1\pmod3\), and to \(-4\pmod p\) when \(p^r\equiv2\pmod3\). The latter case is nonzero for every odd prime. The former is nonzero unless \(p=5\). Because \(5^r\equiv1\pmod3\) precisely for even \(r\), equation (3) proves the asserted valuation in every case except \(p=5\) and even \(r\).

For that case, \(r\ge2\) and \(L=5^{r-1}\) is at least five with \(L\equiv2\pmod3\). If integer Laurent polynomials \(A,B\) satisfy \(A\equiv B\pmod5\), then \(A^5\equiv B^5\pmod{25}\). Apply this to \(A=T(z)^{5^{r-1}}\) and \(B=T(z^L)\), congruent modulo five by freshman's dream, to obtain
\[
T(z)^{5^r}\equiv T(z^L)^5\pmod{25}.\tag{4}
\]
Direct expansion, with coefficients symmetric in positive and negative exponents, gives
\[
T(z)^5=51+\sum_{j=1}^{5}b_j(z^j+z^{-j}),\qquad(b_1,b_2,b_3,b_4,b_5)=(45,30,15,5,1).\tag{5}
\]
Since \(L>1\), (1), (4), and (5) give \(R_{5^r}\equiv51\equiv1\pmod{25}\). For the preceding index, (4) and the expansion of \(K\) give
\[
R_{5^r-1}\equiv\sum_{j=1}^{5}b_jk_{jL}
=-90+30+15-10+1=-54\equiv21\pmod{25}.\tag{6}
\]
Consequently, \(2R_{5^r}+3R_{5^r-1}\equiv2+3\cdot21=65\equiv15\pmod{25}\), which is divisible by five but not by twenty-five. In (3), the denominator is coprime to five, proving \(\nu_5(R_{5^r+1})=r+1\) for each even \(r\ge2\). All cases are now proved.

## Verification
Run `python3 verify.py` using the standard library. It independently evaluates the integer recurrence and the Catalan binomial transform and checks 24 prime-power instances over odd primes \(3,5,7,11,13\), plus the exceptional modulo-25 identities at five-power indices. Its expected success marker is `VERIFY_OK`. These calculations test the proof but are not a substitute for the all-exponent Laurent-polynomial argument.

## Relationship to prior work
Deutsch and Sagan establish foundational Catalan/Motzkin/Riordan congruences, and the Catalan-binomial representation is classical. Chen, Deng, and Yang record a Riordan recurrence. Krattenthaler and Müller develop methods for Riordan congruences modulo powers of three, including explicit generating-function congruences modulo 9 and 27; their theorem concerns the ternary prime only. Their later work develops binary congruences, which do not imply the odd-prime classification above. The evaluated all-odd-prime exact valuation, with its sharp five-adic parity exception, is not a statement located in these inspected sources. Generic algorithms for fixed prime-power moduli do not themselves evaluate this infinite simultaneous family. The possibility of an equivalent unindexed result remains open to independent inspection.

## Limitations
The theorem excludes the prime two and does not classify valuations at indices other than \(p^r+1\), or higher normalized residues. The claim is a self-reviewed mathematical argument, not an independently audited theorem. Finite testing is supplemental. Unindexed literature could contain an earlier equivalent result.

## References
- E. Deutsch and B. E. Sagan, *Congruences for Catalan and Motzkin numbers and related sequences*, arXiv:math/0407326v1 (2004). https://arxiv.org/abs/math/0407326
- W. Y. C. Chen, E. Y. P. Deng and L. L. M. Yang, *Riordan Paths and Derangements*, arXiv:math/0602298v1 (2006). https://arxiv.org/abs/math/0602298
- C. Krattenthaler and T. W. Müller, *A method for determining the modulo powers of three behaviour of recursive sequences*, arXiv:1308.2856v1 (2013), Section 9. https://arxiv.org/abs/1308.2856
- C. Krattenthaler and T. W. Müller, *Motzkin numbers and related sequences modulo powers of 2*, arXiv:1608.05657v1 (2016). https://arxiv.org/abs/1608.05657
- OEIS A005043, *Riordan numbers*, classical recurrence and references. https://oeis.org/A005043
