# Exact finite-gap shielding and first-contact correction for binary carry counts

## Finding
Let \(r\ge1\) and let \(t=\sum_{i=1}^{r}2^{a_i}\), where \(0\le a_1<\cdots<a_r\) are integers. Suppose all successive gaps \(d_i=a_{i+1}-a_i\) satisfy \(d_i\ge r\), and put \(q=\#\{1\le i<r:d_i=r\}\). Define \(C_t(n)\) to be the number of carries when \(n\) and \(t\) are added in base two. For every \(0\le k<r\), the natural density of integers with exactly \(k\) carries is
\[
\Pr(C_t(n)=k)=\frac{\binom{r+k-1}{k}}{2^{r+k}},
\]
where \(\Pr\) denotes natural density in the nonnegative integers. At the first contact layer, the density is
\[
\Pr(C_t(n)=r)=\frac{\binom{2r-1}{r}-q}{2^{2r}}.
\]
Consequently, if \(s_2\) denotes binary digit sum, then
\[
\boxed{\operatorname{dens}\{n\ge0:s_2(n+t)\ge s_2(n)\}=\frac12+\frac{\binom{2r}{r}}{2^{2r+1}}-\frac{q}{2^{2r}}.}
\]
In particular, when every gap is at least \(r+1\), the full nonnegative digit-sum law is **independent of the positions of the ones** and agrees with a sum of \(r\) independent geometric carry lengths. The uniform gap threshold \(r+1\) is sharp for \(r\ge2\): any configuration with a gap exactly \(r\) has a strictly smaller nondecrease density, by precisely \(2^{-2r}\) for each such gap.

## Assumptions and scope
The shift \(t\) is a positive integer of Hamming weight exactly \(r\). The gaps are measured between successive positions of set binary digits (thus a gap of \(r\) contains \(r-1\) zero digits). There is no upper bound on \(r\), the gaps, or the lowest set-bit position. No claim is made for a gap below \(r\), or for a complete description of the negative digit-sum tail. At \(r=1\), take \(q=0\) by convention.

For a finite-valued integer statistic \(X(n)\), its probability at a specified value is the limit of the proportion of \(0\le n<N\) having that value, as \(N\to\infty\); existence is justified below. Kummer's carry identity gives \(s_2(n+t)-s_2(n)=r-C_t(n)\), so nondecrease means at most \(r\) carries.

## Proof
Write \(z\) for a formal variable marking each carry, and give the binary digits of \(n\) the limiting uniform independent Bernoulli distribution. The incoming carry state is \(0\) or \(1\). The row-to-column weighted transition matrices at a digit of \(t\) equal to zero or one are
\[
A_0(z)=\begin{pmatrix}1&0\\1/2&z/2\end{pmatrix},\qquad
A_1(z)=\begin{pmatrix}1/2&z/2\\0&z\end{pmatrix}.
\]
For a tail consisting entirely of zero digits of \(t\), the generating function of additional carries is \(v(z)=(1,(2-z)^{-1})^{\mathsf T}\), because a carry survives each successive fair digit with probability one-half. The first \(a_1\) zero positions have no effect on an initial zero carry. Put \(B=A_1\) and \(h_i=d_i-1\). The probability generating function for the total number of carries is therefore
\[
P_t(z)=(1,0)B A_0^{h_1}B\cdots A_0^{h_{r-1}}Bv(z).
\]
This identity proves existence of each natural density: probabilities are determined up to an arbitrarily small error by a sufficiently long finite binary prefix; the remaining carry tail has geometric decay.

In the ring of formal power series at \(z=0\), set
\[
H(z)=\begin{pmatrix}1&0\\(2-z)^{-1}&0\end{pmatrix},\qquad
E(z)=\begin{pmatrix}0&0\\-(2-z)^{-1}&1\end{pmatrix}.
\]
Direct matrix multiplication gives the exact relation
\[
A_0(z)^h=H(z)+(z/2)^hE(z)\qquad(h\ge0).
\]
Replacing every finite zero-block matrix by \(H\) gives a universal reference generating function:
\[
P_\infty(z)=(1,0)BH\cdots HBv(z)=(2-z)^{-r},
\]
since \((1,0)BH=((2-z)^{-1},0)\) and \((1,0)Bv=(2-z)^{-1}\).

It remains to control every replacement error through degree \(r\). Each \(h_i\ge r-1\). The matrix \(B E B\) has entries of order at least \(z\) and top-left entry
\[
(BEB)_{11}=-\frac{z}{4(2-z)}=-\frac z8+O(z^2).
\]
Any one gap with \(h_i\ge r\) therefore contributes only terms of degree at least \(r+1\), while a gap with \(h_i=r-1\) contributes a term of degree \(r\). At degree \(r\), the other \(r-2\) one-digit factors each have top-left constant term \(1/2\); the chosen correction is \((z/2)^{r-1}(-z/8)\). Its total coefficient is thus
\[
-2^{-(r-1)}\cdot 2^{-3}\cdot2^{-(r-2)}=-2^{-2r}.
\]
Products containing two or more corrections contribute only degree greater than \(r\). Indeed, their explicit zero-block factors have degree at least \(2(r-1)\), and the adjacent \(B,E\) structure contributes at least one additional degree; \(2r-1>r\) for \(r\ge2\). The case \(r=1\) has no corrections. Hence the exact formal congruence is
\[
\boxed{P_t(z)=(2-z)^{-r}-\frac{qz^r}{2^{2r}}+O(z^{r+1}).}
\]
Expanding \((2-z)^{-r}\) by the negative binomial theorem proves the stated individual carry probabilities.

Finally, the identity \(\sum_{k=0}^{r}2^{-r-k}\binom{r+k-1}{k}=2^{-2r}\sum_{j=r}^{2r}\binom{2r}{j}\) follows by interpreting the left side as the probability of at most \(r\) failures before the \(r\)-th success in independent fair trials. Binomial symmetry changes the right side to \(1/2+2^{-2r-1}\binom{2r}{r}\). Subtracting \(q2^{-2r}\) completes the claim. The strict sharpness assertion follows whenever \(q>0\).

## Verification
The accompanying `verify.py` uses exact rational arithmetic in a two-state stochastic carry automaton. It checks the entire probability vector for \(0\le k\le r\) against the theorem for 264 distinct heterogeneous/equispaced configurations through \(r=8\), including boundary gaps and arbitrary initial shifts. A separate finite dyadic enumeration tests representative small configurations, using enough binary digits for the probabilities to stabilize. Running `python3 verify.py` returns `VERIFY_OK`. These finite tests are not a substitute for the unrestricted matrix proof.

## Relationship to prior work
Cheng (arXiv:2608.25899, first public 2026-08-26) determines the sharp asymptotic minimum of Cusick's nondecrease bias at fixed binary Hamming weight. The theorem here concerns a different question: an **exact** joint low-carry law for widely separated set bits and its first finite-spacing correction. Sobolewski and Spiegelhofer (arXiv:2411.07779) develop correlation-measure matrices and limits for infinite digit blocks; their general matrix framework is a starting point, but their theorems inspected do not state the finite threshold \(r+1\), the local binomial coefficients, or the additive defect indexed by the number \(q\) of just-touching gaps. Drmota, Kauers, and Spiegelhofer (arXiv:1509.08623) give recursive algorithms for all binary shifts; an algorithm capable of evaluating a parameter is not itself this closed family law. These observations concern the cited statements, not a guarantee of priority over all equivalent work.

## Limitations
The result characterizes only the carry probabilities through layer \(r\); higher-carry layers retain dependence on the detailed gap lengths. The gap hypothesis is essential. The argument derives a direct consequence of a classical finite-state carry model; it does not solve a general extremal problem for all Hamming-weight-\(r\) shifts. An equivalent explicit finite-gap stabilization theorem might exist outside the inspected primary literature. Independent mathematical and bibliographic validation remains outstanding.

## References
1. Kaimin Cheng, *Sharp extremal asymptotics for Cusick's sum-of-digits bias at fixed Hamming weight*, arXiv:2608.25899 (first posted 2026-08-26).
2. Bartosz Sobolewski and Lukas Spiegelhofer, *Decomposing the sum-of-digits correlation measure*, arXiv:2411.07779 (first posted 2024-11-11).
3. Michael Drmota, Manuel Kauers, and Lukas Spiegelhofer, *On a conjecture of Cusick concerning the sum of digits of \(n\) and \(n+t\)*, arXiv:1509.08623 (2015).
4. Lukas Spiegelhofer and Michael Wallner, *The binary digits of \(n+t\)*, arXiv:2005.07167 (2020).
5. Classical carry-count identity (Kummer's theorem and the binary digit-sum relation).
