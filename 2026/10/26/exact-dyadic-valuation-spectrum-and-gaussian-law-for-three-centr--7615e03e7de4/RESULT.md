# Exact dyadic valuation spectrum and Gaussian law for three-central binomial coefficients

## Finding

Define the integer sequence \(c_n\), for \(n\ge0\), by
\[
(1-9x)^{-1/3}=\sum_{n\ge0}c_n x^n,
\qquad c_0=1,
\qquad (n+1)c_{n+1}=3(3n+1)c_n.
\]
For \(L\ge0\), let the complete two-adic valuation polynomial be
\[
H_L(u)=\sum_{n=0}^{2^L-1}u^{\nu_2(c_n)}.
\]
For an indeterminate \(z\), the following two exact generating functions hold:
\[
\boxed{\sum_{m\ge0}H_{2m}(u)z^m
 =\frac{1+(u-2u^2)z}{1-(2+u+2u^2)z+4u^2z^2}},
\]
\[
\boxed{\sum_{m\ge0}H_{2m+1}(u)z^m
 =\frac{2\{1+(u^3-2u^2)z\}}{1-(2+u+2u^2)z+4u^2z^2}}.
\]
They determine exactly how many indices in each dyadic block have **every** given two-adic valuation. In particular, for a uniformly chosen index \(n\) in \(\{0,\ldots,2^L-1\}\), let \(V_L=\nu_2(c_n)\). Then
\[
\mathbb E V_{2m}=m-\frac23+\frac{2}{3\cdot4^m},
\qquad \mathbb E V_{2m+1}=m,
\]
\[
\operatorname{Var}(V_L)=\frac23L+O(1),
\qquad
\frac{V_L-L/2}{\sqrt{2L/3}}\ \xrightarrow[L\to\infty]{\ d\ }\ \mathcal N(0,1).
\]
For \(m\ge1\), the maximum valuation in \(0\le n<2^{2m}\) is \(2m-1\) and occurs \(2^m\) times; in \(0\le n<2^{2m+1}\) it is \(2m+1\) and also occurs \(2^m\) times. The zero-valuation counts are respectively \(2^m\) and \(2^{m+1}\).

## Assumptions and scope

All indices \(n,m,L\) are nonnegative integers, and \(\nu_2\) is the exponent of two in a positive integer. The variables \(u,z\) are formal indeterminates in the exact identities; the central-limit assertion concerns the usual real-valued random variable \(V_L\). The first maximum assertion covers even lengths \(L\ge2\); the second covers odd lengths \(L\ge3\). At \(L=0,1\), all valuations are zero.

## Proof

**1. The published valuation identity and its binary interpretation.** The three-central coefficient formula and the floor-sum valuation identity of Straub, Moll and Amdeberhan [1, Proposition 2.1 and equation (2.9)] give, with \(q=2^a\) and the least positive inverse \(i_q\equiv3^{-1}\pmod q\),
\[
\nu_2(c_n)=\sum_{a\ge1}\left(\left\lfloor\frac{n+i_{2^a}-1}{2^a}\right\rfloor-\left\lfloor\frac n{2^a}\right\rfloor\right).
\]
Only finitely many terms are nonzero. The two-adic expansion is
\[
3^{-1}=1+\sum_{j\ge0}2^{2j+1}.
\]
Thus \(i_{2^a}-1\) is the integer whose first \(a\) binary digits are the alternating digits \(b_j=0\) for even \(j\), and \(b_j=1\) for odd \(j\). The \(a\)-th floor difference is exactly the carry from the first \(a\) positions in the base-two addition of \(n\) and this alternating two-adic digit string. Consequently, \(\nu_2(c_n)\) equals the total number of outgoing carries. This is a specialization of the known carry valuation theorem [1, Theorem 3.7], not a newly claimed pointwise criterion.

**2. An exact two-state weighted transfer.** Read the binary digits of \(n\) from least to most significant. The state \(s\in\{0,1\}\) is the incoming carry; each outgoing carry contributes a factor \(u\). Summing over the two possible digits of \(n\), a position with \(b_j=0\) has the matrix
\[
E(u)=\begin{pmatrix}2&0\\1&u\end{pmatrix},
\]
and one with \(b_j=1\) has
\[
O(u)=\begin{pmatrix}1&u\\0&2u\end{pmatrix}.
\]
Rows index the incoming state; columns the outgoing state. A complete even-odd pair has transfer
\[
T(u)=E(u)O(u)=\begin{pmatrix}2&2u\\1&u+2u^2\end{pmatrix}.
\]
After an even number of bits, an outgoing carry enters a zero input digit with \(b_j=0\) and terminates without further contribution. After an odd number of bits, an outgoing carry meets one further \(b_j=1\) digit, producing exactly one more carry, and then terminates. Therefore, with \(e=(1,0)\),
\[
H_{2m}(u)=eT(u)^m\begin{pmatrix}1\\1\end{pmatrix},
\qquad
H_{2m+1}(u)=eT(u)^m E(u)\begin{pmatrix}1\\u\end{pmatrix}.
\]
The latter terminal vector is essential: simply summing final states after an odd number of bits would miss a carry. Direct inversion of \(I-zT(u)\), using \(\operatorname{tr}T=2+u+2u^2\) and \(\det T=4u^2\), proves the two rational functions in the finding.

**3. Exact means and extremal multiplicities.** At \(u=1\), \(H_L(1)=2^L\). Differentiation of the rational functions at \(u=1\) gives
\[
\sum_{m\ge0}H'_{2m}(1)z^m
=\frac{-2z(1+2z)}{(z-1)(4z-1)^2},
\qquad
\sum_{m\ge0}H'_{2m+1}(1)z^m
=\frac{8z}{(4z-1)^2}.
\]
Coefficient extraction and division by \(2^L\) yield the stated exact expectations. A carry cannot first arise at position zero, since \(b_0=0\) and the incoming carry is zero. To obtain all the remaining possible carries, the first odd digit must equal one, every subsequent even digit must equal one, and subsequent odd digits may vary freely. The least-significant even digit is also free. Hence the even- and odd-length maximal exponents and multiplicities stated above. For zero carries, each odd-position input digit is forced to zero while even-position digits are free, giving the stated parity-zero counts (and agreeing with [1, Corollary 3.4]).

**4. Gaussian limit.** The positive matrix \(T(1)=\left(\begin{smallmatrix}2&2\\1&3\end{smallmatrix}\right)\) has simple Perron eigenvalue \(4\), and its other eigenvalue is \(1\). For real \(t\) near zero, the dominant eigenvalue of \(T(e^t)\) is the analytic function
\[
\lambda(e^t)=\frac{2+e^t+2e^{2t}+\sqrt{(2+e^t+2e^{2t})^2-16e^{2t}}}{2}.
\]
The discriminant is positive near \(t=0\). Elementary differentiation gives
\[
\lambda(1)=4,\qquad \lambda'(1)=4,\qquad \lambda''(1)=\frac{16}{3},
\]
and therefore
\[
\left.\frac{d}{dt}\log\lambda(e^t)\right|_{t=0}=1,
\qquad
\left.\frac{d^2}{dt^2}\log\lambda(e^t)\right|_{t=0}=\frac43.
\]
Spectral projection on the simple leading eigenvalue yields, for each parity of \(L\) and with \(m=\lfloor L/2\rfloor\), a moment generating function of the form
\[
\mathbb E e^{tV_L}=A_{\epsilon}(t)
\left(\frac{\lambda(e^t)}4\right)^m
\left(1+O(\rho^m)\right),
\]
where \(A_{\epsilon}\) is analytic and nonzero near zero with \(A_{\epsilon}(0)=1\), and \(0<\rho<1\) uniformly for \(t\) in a sufficiently small complex neighborhood of zero. The fixed extra factor of two in the odd-block normalization is absorbed in \(A_1\). Taking the first two derivatives of the logarithm proves the variance assertion \(\operatorname{Var}(V_L)=4m/3+O(1)=2L/3+O(1)\). Finally, Taylor expansion at \(t=s/\sqrt{4m/3}\) shows that the normalized moment generating functions tend to \(e^{s^2/2}\), establishing the standard normal limit. Replacing the center \(m\) by \(L/2\) changes it by at most \(1/2\), which vanishes after normalization.

## Verification

Run `python3 verify.py` with Python 3 and its standard library. The script calculates the first 4,096 coefficients from the exact integer recurrence, separately evaluates their valuations with modular-inverse floor sums, and compares 13 complete block histograms to the weighted carry transfer. It checks the second-order polynomial recurrence for both parity classes through 15 block pairs, and the explicit extremal counts. It does not purport to verify infinitely many indices computationally. The universal proof is the four-step argument above.

## Relationship to prior work

Straub, Moll and Amdeberhan [1] introduced the generalized central coefficients, proved their integrality, gave the pointwise valuation formula and its carry interpretation (Theorem 3.7), and proved the odd-index characterization (Corollary 3.4). Those results are assumed here and not presented as new. The contribution assessed here is a closed bivariate enumerator for **all** valuations on each dyadic block, two exact means, sharp valuation endpoints with multiplicities, and the explicit Gaussian limit with variance slope \(2/3\) per input bit. The OEIS entry [2] tabulates the underlying coefficient sequence but does not state these block-distribution results. A general transfer-matrix or additive-function theorem could imply parts of the asymptotic argument; the specialized two-parity rational functions and extremal multiplicities are additional explicit statements.

## Limitations

The formulas apply only to \(k=3\), \(p=2\) and initial intervals starting at zero with power-of-two cutoffs. They do not describe arbitrary subintervals or the joint valuations at distinct primes. The arithmetic input is a known valuation formula, not a new theorem about individual coefficients. Exact novelty beyond the inspected sources remains subject to unlocated equivalent treatments of digital carry statistics.

## References

[1] Armin Straub, Victor H. Moll and Tewodros Amdeberhan, *The p-adic valuation of k-central binomial coefficients*, arXiv:0811.2028v1 (first publicly submitted 13 November 2008), especially Proposition 2.1, equation (2.9), Corollary 3.4, and Theorem 3.7. https://arxiv.org/html/0811.2028v1

[2] OEIS A004987, *3-central binomial coefficients*, https://oeis.org/A004987 (sequence and cited literature; database accessed 24 October 2026).
