# Linear divisibility and an exact dyadic family for cobalancing square-sum GCDs

## Finding
Let \(b_0=b_1=0\) and \(b_{n+2}=6b_{n+1}-b_n+2\) for every integer \(n\ge0\). These are the cobalancing numbers. Define, for \(n\ge0\) and \(k\ge1\),
\[
H_k(n)=\sum_{j=1}^{k}b_{n+j}^{2},\qquad G(k)=\gcd\{H_k(n):n\ge0\}.
\]
Then the following exact reduction holds for **every** positive window length:
\[
\boxed{G(k)=\gcd\bigl(40k,H_k(0),H_k(1),H_k(2),H_k(3)\bigr).}
\]
Equivalently, the four window values may be replaced by \(H_k(0)\) and the three boundary differences \(b_{k+1}^{2}\), \(b_{k+2}^{2}-4\), \(b_{k+3}^{2}-196\). In particular, \(G(k)\mid40k\).

There is also a closed form on a natural infinite dyadic family: for **every integer** \(r\ge0\),
\[
\boxed{G(12\cdot2^{r})=120\cdot2^{r}=10(12\cdot2^{r}).}
\]
More strongly, for all \(n,r\ge0\), each sum \(H_{12\cdot2^r}(n)\) is divisible by \(15\) and has **exact** two-adic valuation \(r+3\).

## Assumptions and scope
The index \(n\) ranges over nonnegative integers and the window length \(k\) over positive integers. The GCD means the positive generator of the ideal of all window sums. No assumption about primality or a finite cut-off is made. The exact family consists of the lengths \(12,24,48,96,\ldots\); the general finite GCD identity applies to every length, not just that family.

## Proof
**1. A universal polynomial identity.** Put \(u_n=2b_n+1\). Then \(u_0=u_1=1\) and \(u_{n+2}=6u_{n+1}-u_n\). With \(\alpha=3+2\sqrt2\) and \(\beta=3-2\sqrt2\), we have \(u_n=A\alpha^n+B\beta^n\), where \(A=(\sqrt2-1)/(2\sqrt2)\), \(B=(\sqrt2+1)/(2\sqrt2)\), and \(AB=1/8\). Consequently, \(b_n^2=(u_n^2-2u_n+1)/4\) is a linear combination of five exponential sequences with bases \(1,\alpha,\beta,\alpha^2,\beta^2\). Its constant component is \((2AB+1)/4=5/16\). Writing \(T\) for the forward shift, the polynomial
\[
R(T)=(T^2-6T+1)(T^2-34T+1)=T^4-40T^3+206T^2-40T+1
\]
annihilates every nonconstant component and satisfies \(R(1)=128\). Hence, identically for every \(n\ge0\),
\[
b_{n+4}^2-40b_{n+3}^2+206b_{n+2}^2-40b_{n+1}^2+b_n^2=40.\tag{1}
\]
Summing (1) across a window gives
\[
H_k(n+4)-40H_k(n+3)+206H_k(n+2)-40H_k(n+1)+H_k(n)=40k.\tag{2}
\]
Let \(d=\gcd(40k,H_k(0),H_k(1),H_k(2),H_k(3))\). Equation (2), a monic recurrence, proves inductively that \(d\) divides every \(H_k(n)\). Conversely the GCD of all windows divides the first four windows and, by (2), divides \(40k\). Thus \(d=G(k)\), proving the general formula.

**2. Modulo \(3\) and \(5\).** The recurrence gives the cyclic sequences
\[
(b_n\bmod3)=(0,0,2,2)^{\infty},\qquad
(b_n\bmod5)=(0,0,2,4,4,2)^{\infty}.
\]
A full cycle of squared terms sums to \(8\equiv2\pmod3\) in the first case, and to \(40\equiv0\pmod5\) in the second. Every block of twelve squared terms is therefore divisible by both \(3\) and \(5\). Whenever \(12\mid k\), concatenation of twelve-term blocks proves \(15\mid H_k(n)\) for all \(n\).

**3. Exact dyadic window valuation.** Every \(b_n\) is even, and modulo \(4\) its values follow the four-cycle \((0,0,2,2)\). Consequently the squares modulo \(16\) follow \((0,0,4,4)\), and
\[
H_4(n)\equiv8\pmod{16}\qquad(n\ge0).\tag{3}
\]
For the lifting step put
\[
M=\begin{pmatrix}6&-1&2\\1&0&0\\0&0&1\end{pmatrix},\qquad
v_n=\begin{pmatrix}b_{n+1}\\b_n\\1\end{pmatrix},
\quad v_{n+1}=Mv_n.
\]
A direct calculation gives
\[
\frac{M^4-I}{4}=\begin{pmatrix}297&-51&123\\51&-9&21\\0&0&0\end{pmatrix}
\equiv \begin{pmatrix}1&1&1\\1&1&1\\0&0&0\end{pmatrix}\pmod2.
\]
Repeated squaring yields, for every \(m\ge2\),
\[
M^{2^m}\equiv I+2^m C\pmod{2^{m+1}},
\quad C=\begin{pmatrix}1&1&1\\1&1&1\\0&0&0\end{pmatrix}.
\]
Since both initial coordinates of \(v_n\) are even, \(Cv_n\equiv(1,1,0)^\mathsf T\pmod2\). Thus
\[
b_{n+2^m}=b_n+2^m h_n,\qquad h_n\text{ odd}.\tag{4}
\]
Let \(L=2^m\). Applying (4) to the second half of a block gives
\[
H_{2L}(n)-2H_L(n)
=2^{m+1}\sum_{j=1}^{L}b_{n+j}h_{n+j}
+2^{2m}\sum_{j=1}^{L}h_{n+j}^{2}.\tag{5}
\]
Because \(b_{n+j}\) is even and \(h_{n+j}\) odd, \(b_{n+j}h_{n+j}\equiv b_{n+j}\pmod4\). A block of \(L\) terms, with \(4\mid L\), has \(\sum b_{n+j}\equiv0\pmod4\). Therefore the first summand on the right of (5) is divisible by \(2^{m+3}\). The second is divisible by the same power if \(m\ge3\); for \(m=2\), it is also divisible because it consists of four odd squares and hence has even sum. So
\[
H_{2^{m+1}}(n)\equiv2H_{2^m}(n)\pmod{2^{m+3}}.\tag{6}
\]
Starting from (3), induction in (6) proves the **exact** congruence
\[
H_{2^m}(n)\equiv2^{m+1}\pmod{2^{m+2}}
\qquad(m\ge2,n\ge0).\tag{7}
\]
Now set \(m=r+2\) and \(k=12\cdot2^r=3\cdot2^m\). Every \(H_k(n)\) is the sum of three blocks of length \(2^m\). Equation (7) gives
\[
H_k(n)\equiv3\cdot2^{m+1}\equiv2^{r+3}\pmod{2^{r+4}}.\tag{8}
\]
Thus every such window has two-adic valuation exactly \(r+3\). Step 2 also shows that every window is divisible by \(15\), giving \(15\cdot2^{r+3}=120\cdot2^r\mid G(k)\). Step 1 gives \(G(k)\mid40k=480\cdot2^r=3\cdot5\cdot2^{r+5}\). Since the two odd prime valuations are already maximal and (8) fixes the exact power of two, the GCD equals \(120\cdot2^r\), as claimed. \(\square\)

## Verification
The standalone standard-library script `verify.py` recomputes the recurrence (1), the initial modular cycles, the base block sums, the matrix-power congruences at the first fourteen lifting levels, the exact finite-GCD reduction for all lengths through \(419\), and the dyadic formula for \(0\le r\le5\). These independent finite checks are corroboration; the infinite assertions follow from the displayed identities and induction, not from their numerical ranges.

## Relationship to prior work
Mbirika, Schrader and Spilker (2023), Section 6.1, Question 30, explicitly ask for closed forms for GCDs of sums of consecutive squares of the balancing and cobalancing families. Their stated cobalancing-square observation is divisibility by four. The present result supplies a finite exact formula for **every** length, an independent uniform divisor bound, and an exact infinite dyadic subfamily. Their results on un-squared cobalancing terms (Section 5) do not imply these square-sum claims. Mbirika and Spilker (2022) concern generalized Fibonacci recurrences with a different characteristic polynomial. A separate exact formula for the **Lucas-balancing** square-sum GCD concerns different sequence values and does not imply the cobalancing-square formula. The polynomial-recurrence method is classical; novelty is claimed only for the stated consequences about cobalancing-square windows.

## Limitations
A simple conventional named-sequence formula for \(G(k)\) at *every* positive length is not asserted. The divisibility \(G(k)\mid40k\) does not say that the upper bound is attained. The dyadic identity applies to lengths \(12\cdot2^r\) only. Originality was checked against the cited primary sources, targeted indexes and related mathematical results; unindexed derivations or later publications remain a risk. Publication priority has not been independently certified.

## References
1. aBa Mbirika, Janee Schrader and Jürgen Spilker, *Pell and associated Pell braid sequences as GCDs of sums of consecutive Pell, balancing, and related numbers*, arXiv:2301.05758 (first posted 13 January 2023), especially Definitions 6--7, Section 5, and Section 6.1, Question 30; https://arxiv.org/html/2301.05758v3.
2. aBa Mbirika and Jürgen Spilker, *GCD of sums of consecutive squares of generalized Fibonacci numbers*, arXiv:2204.12626 (first posted 26 April 2022); https://arxiv.org/abs/2204.12626.
3. OEIS A053141, cobalancing numbers; https://oeis.org/A053141.
