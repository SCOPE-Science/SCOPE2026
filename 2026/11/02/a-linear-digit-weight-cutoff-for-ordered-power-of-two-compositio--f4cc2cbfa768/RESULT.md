# A linear digit-weight cutoff for ordered power-of-two compositions

## Finding
Let \(\vartheta(n)\) be the number of ordered compositions of \(n\geq 0\) into parts belonging to \(\{1,2,4,8,\ldots\}\), with \(\vartheta(0)=1\), and let \(s_2(m)\) denote the number of ones in the binary expansion of a nonnegative integer \(m\). For **every** integer \(N\geq1\) and \(n\geq0\),
\[
\boxed{s_2(n+N)\geq 2N\quad\Longrightarrow\quad 2^N\mid\vartheta(n).}
\]
Equivalently, any index not annihilated modulo \(2^N\) satisfies \(s_2(n+N)\leq2N-1\).

Consequently, for all positive integers \(K\) such that \(2^K\geq N\),
\[
\#\{0\leq n<2^K:2^N\nmid\vartheta(n)\}
\leq \sum_{j=0}^{2N-1}\binom{K+1}{j}
=O_N(K^{2N-1}).
\]
Thus the exceptional count below \(x\) is \(O_N((\log x)^{2N-1})\), where the implicit constant may depend on \(N\). For \(N\geq3\), this cuts the published exponential-in-\(N\) binary-weight threshold to a linear-in-\(N\) one, with a correspondingly smaller polylogarithmic exponent. The bound is a sufficient condition, not an exact support characterization or an assertion that the exponent is optimal.

## Assumptions and scope
All series are formal power series over \(\mathbb Z\) or its quotient modulo \(2^N\). The coefficients count *ordered* compositions; the statement does not concern the distinct binary partition function. There are no primality, growth, or parity assumptions on \(n\) or \(N\).

## Proof
Set
\[
S(z)=\sum_{j\geq0}z^{2^j},\qquad
T(z)=\sum_{0\leq i<j}z^{2^i+2^j},\qquad
F(z)=\sum_{n\geq0}\vartheta(n)z^n=\frac1{1-S(z)}.
\]
Squaring \(S(z)\) and separating equal and unequal exponent pairs gives the *exact integral identity*
\[
S(z)^2=S(z)-z+2T(z),\qquad
S(z)(1-S(z))=z-2T(z).
\]
Since \(S(z)/z\) has constant term one and \(T(z)/z\) has positive order, division in \(\mathbb Z[[z]]\) yields
\[
F(z)=\frac{S(z)/z}{1-2T(z)/z}
=\sum_{r\geq0}2^r\frac{S(z)T(z)^r}{z^{r+1}}.
\]
The last expression is a valid formal-power-series expansion because \(T(z)/z\) has positive order; it may also be truncated modulo any fixed power of two. In particular, for every \(N\geq1\),
\[
\vartheta(n)\equiv
\sum_{r=0}^{N-1}2^r[z^{n+r+1}]S(z)T(z)^r\pmod{2^N}.
\]
If the right-hand side is nonzero modulo \(2^N\), at least one summand is nonzero. For such an \(r\), the coefficient of \(z^{n+r+1}\) in \(S(z)T(z)^r\) is nonzero. Consequently \(n+r+1\) is a sum of precisely \(2r+1\) (not necessarily distinct) powers of two: one from \(S\) and two from each factor \(T\). Binary carrying never increases the number of ones, hence
\[
s_2(n+r+1)\leq2r+1.
\]
By the elementary subadditivity \(s_2(u+v)\leq s_2(u)+s_2(v)\), and using \(n+N=(n+r+1)+(N-r-1)\), we obtain
\[
s_2(n+N)\leq 2r+1+s_2(N-r-1)
\leq 2r+1+(N-r-1)=N+r\leq2N-1.
\]
Taking the contrapositive proves the divisibility theorem. This proof uses only formal-series identities and binary carrying; no finite computation is used to infer the universal statement.

For the counting assertion, when \(2^K\geq N\), every \(n\) with \(0\leq n<2^K\) has \(n+N<2^{K+1}\). The integers in this range with binary weight at most \(2N-1\) number no more than \(\sum_{j=0}^{2N-1}\binom{K+1}{j}\); translation by \(N\) is injective. This completes the proof.

## Verification
A standalone verifier, `verify.py`, computes \(\vartheta(n)\bmod 2^9\) independently from the composition recurrence, reconstructs the truncated factorization of \(F(z)\) modulo \(2^9\), and checks equality of their coefficients. It also tests the new vanishing criterion across finite ranges. Passing finite tests is corroborative only; the proof above is unrestricted.

## Relationship to prior work
Knopfmacher and Robbins (2003) give the ordered binary-composition recurrence and generating function. Alkauskas (first posted March 4, 2010; Journal of Integer Sequences 13, Article 10.5.3) proves the cutoff
\[
s_2(n+2^{N-1})\geq2^N\ \Longrightarrow\ 2^N\mid\vartheta(n),
\]
and gives residue tables modulo small powers of two. The same paper discusses a subsequent exponential-order threshold improvement for \(N\geq4\). Its full text does not state the shifted \(s_2(n+N)\) linear cutoff or the resulting \(O_N((\log x)^{2N-1})\) exceptional-count bound.

The gain is strict for each \(N\geq3\): take \(n=2^L-N-1\), with \(L\geq2N\). Then \(s_2(n+N)=L\), whereas \(n+2^{N-1}=2^L+(2^{N-1}-N-1)\) has binary weight \(1+s_2(2^{N-1}-N-1)<2^N\). These indices therefore satisfy the new criterion but not the published original sufficient criterion. The earlier theorem's table classifications for small moduli remain fully acknowledged; this finding claims only the all-precision quantitative improvement.

## Limitations
The linear digit-weight condition is sufficient, not necessary; it does not identify the complete residue distribution or establish a lower bound for the exceptional count. The exponent \(2N-1\) is an upper-bound exponent, and could be improvable. Historical priority of this all-precision quantitative bound has not been independently established; unlocated relevant literature is a residual originality risk.

## References
1. G. Alkauskas, *Congruence Properties of the Function that Counts Compositions into Powers of 2*, Journal of Integer Sequences 13 (2010), Article 10.5.3; preprint arXiv:1003.1064v1 (2010-03-04). https://arxiv.org/abs/1003.1064 ; https://cs.uwaterloo.ca/journals/JIS/VOL13/Alkauskas/alkauskas2.pdf
2. A. Knopfmacher and N. Robbins, *On Binary and Fibonacci Compositions*, Annales Univ. Sci. Budapest., Sect. Comp. 22 (2003), 193–206. https://ac.inf.elte.hu/Vol_022_2003/doi/193_22.pdf
