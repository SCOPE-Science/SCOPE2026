# Exact dyadic valuation distribution and Gaussian law for 3-central binomial coefficients

## Finding
For all integers \(n\geq0\), let \(c_n\) be the positive integer determined by
\[
(1-9x)^{-1/3}=\sum_{n\geq0}c_nx^n,
\qquad c_0=1,
\qquad c_{n+1}=\frac{3(3n+1)}{n+1}c_n.
\]
Put \(v(n)=\nu_2(c_n)\). For every integer \(L\geq0\), define the **complete dyadic-block valuation enumerator**
\[
P_L(z)=\sum_{0\leq n<4^L}z^{v(n)}.
\]
Then, with \(e=(1,0)\) and \(\mathbf1=(1,1)^{\mathsf T}\),
\[
\boxed{P_L(z)=eM(z)^L\mathbf1},\qquad
M(z)=\begin{pmatrix}2&2z\\1&z+2z^2\end{pmatrix}.
\]
Consequently the entire distribution over **every** block is encoded by
\[
\boxed{\sum_{L\geq0}P_L(z)t^L=
 \frac{1+t(z-2z^2)}{1-t(2+z+2z^2)+4t^2z^2}}.
\]
For \(N_L\) uniform on the integers \(0\leq n<4^L\) and \(X_L=v(N_L)\), the exact mean and variance are
\[
\boxed{\mathbb E X_L=L-\frac23+\frac{2}{3\cdot4^L}},\qquad
\boxed{\operatorname{Var}(X_L)=\frac{4L}{3}-\frac{14}{9}+\frac{2}{4^L}-\frac{4}{9\cdot16^L}}.
\]
In addition, as \(L\to\infty\),
\[
\boxed{\frac{X_L-L}{\sqrt{4L/3}}\ \xrightarrow{\ \mathrm{law}\ }\ \mathcal N(0,1)}.
\]

## Assumptions and scope
All coefficients are those of the above power series, not ordinary binomial coefficients. Valuation means the nonnegative exponent of the prime \(2\). All integer indices \(n\ge0\) and lengths \(L\ge0\) are covered, including \(P_0=1\). The central limit statement samples uniformly from a **complete** block of length \(4^L\), not an arbitrary interval.

## Proof
**1. Binary-carry formula from first principles.** For each \(j\ge1\), let \(r_j\in\{1,\ldots,2^j-1\}\) satisfy \(3r_j\equiv1\pmod{2^j}\). The coefficient product formula gives
\[
c_n=\frac{3^n}{n!}\prod_{h=0}^{n-1}(3h+1).
\]
Among \(0\le h<n\), exactly \(\lfloor(n+r_j-1)/2^j\rfloor\) satisfy \(2^j\mid(3h+1)\); subtracting the \(\lfloor n/2^j\rfloor\) terms contributed by \(n!\) yields
\[
v(n)=\sum_{j\ge1}\left(\left\lfloor\frac{n+r_j-1}{2^j}\right\rfloor-\left\lfloor\frac n{2^j}\right\rfloor\right).
\]
The nonnegative summand is the carry **into** binary position \(j\) on adding \(n\) and the lowest \(j\) digits of \(1/3-1\) in the \(2\)-adic integers. Explicitly,
\[
\frac13-1=-\frac23=\sum_{h\ge0}2^{2h+1}
\quad\text{in }\mathbb Z_2.
\]
Thus these fixed digits are \(b_{2h}=0\) and \(b_{2h+1}=1\). Writing the binary digits of \(n\) as \(a_j\), with initial carry \(q_0=0\), define
\[
q_{j+1}=\left\lfloor\frac{a_j+b_j+q_j}{2}\right\rfloor\in\{0,1\}.
\]
The floor formula proves \(v(n)=\sum_{j\ge1}q_j\). In particular, if \(n<4^L\), no nonzero carry survives beyond \(q_{2L}\): the next input bits are \(a_{2L}=b_{2L}=0\). Every carry counted is therefore among the first \(2L\) positions.

**2. Exact two-state enumeration.** Group the digits \((a_{2h},a_{2h+1})\) in consecutive pairs. From input carry \(0\), two pairs give output carry \(0\) with weight \(1\), and two pairs give output carry \(1\) with weight \(z\). From input carry \(1\), one pair gives output carry \(0\) with weight \(1\), one gives output carry \(1\) with weight \(z\), and two give output carry \(1\) with weight \(z^2\). The weight exponent is the number of **new** carries in the pair. Hence the transfer matrix is exactly \(M(z)\). The initial state is \(0\), and both final states are admitted. Each of the \(4^L\) binary words is counted once, proving the claimed \(P_L\). Inverting \(I-tM(z)\) gives the rational two-variable generating function. Equivalently,
\[
P_{L+2}(z)=(2+z+2z^2)P_{L+1}(z)-4z^2P_L(z),
\quad P_0(z)=1,\quad P_1(z)=2+2z.
\]

**3. Exact moments.** Since \(P_L(1)=4^L\), the mean is \(P'_L(1)/4^L\), and the variance is
\[
\frac{P''_L(1)+P'_L(1)}{4^L}-\left(\frac{P'_L(1)}{4^L}\right)^2.
\]
Differentiating the polynomial recurrence once and twice gives respectively
\[
P'_{L+2}(1)=5P'_{L+1}(1)-4P'_L(1)+12\cdot4^L
\]
and
\[
P''_{L+2}(1)=5P''_{L+1}(1)-4P''_L(1)
+10P'_{L+1}(1)-16P'_L(1)+8\cdot4^L.
\]
The initial derivatives at \(L=0,1\) are \(P'_0=0,P'_1=2,P''_0=P''_1=0\). Solving these elementary recurrences, or directly substituting the stated formulas into them, yields the exact mean and variance above. This argument includes \(L=0\), where both are zero.

**4. Gaussian limit.** Let \(\lambda(z)\) be the analytic eigenvalue branch of \(M(z)\) near \(z=1\) satisfying \(\lambda(1)=4\). Its characteristic equation is
\[
\lambda(z)^2-(2+z+2z^2)\lambda(z)+4z^2=0.
\]
The other eigenvalue equals \(1\) at \(z=1\), so its contribution to \(eM(z)^L\mathbf1\) is exponentially smaller uniformly for \(z\) sufficiently near \(1\). The dominant spectral coefficient is analytic and equals \(1\) at \(z=1\). Implicit differentiation of the characteristic equation yields \(\lambda'(1)=4\) and \(\lambda''(1)=16/3\). Therefore, as \(u\to0\),
\[
\log\frac{\lambda(e^u)}4=u+\frac23u^2+O(u^3).
\]
Using \(\mathbb E(e^{uX_L})=4^{-L}eM(e^u)^L\mathbf1\), substitute \(u=is/\sqrt{4L/3}\) and subtract the term \(Lu\). The characteristic functions converge to \(e^{-s^2/2}\) for every fixed real \(s\). The continuity theorem proves the claimed normal limit.

## Verification
A standalone Python standard-library checker, `verify.py`, independently uses the exact coefficient valuation recurrence
\[
v(n+1)=v(n)+\nu_2(3n+1)-\nu_2(n+1)
\]
to enumerate all values \(0\le n<4^L\) for \(0\le L\le7\), then checks every coefficient of \(P_L(z)\) against the transfer-matrix recurrence. It also verifies the exact rational mean and variance identities for those lengths, and performs symbolic tests of the eigenvalue derivatives. Run `python3 verify.py` from the extracted package. These are finite reproducibility checks; the preceding proof, not the finite checks, establishes the infinite theorem and limit law.

## Relationship to prior work
Straub, Moll and Amdeberhan prove integrality, identify the 2-adic digits of the inverse of three, and give a carry characterization of valuations (Corollary 3.4 and Theorem 3.7 of [1]). Their theorem determines the valuation of each individual coefficient and the odd-coefficient indices; it does **not itself state** the joint length/valuation generating function, the exact variance, or the Gaussian law for the complete dyadic blocks. The present proof starts from the arithmetic product and counts the carries with a concrete two-state weighted transfer operator, obtaining an explicit distribution law and nontrivial fluctuation constant. OEIS A004987 independently tabulates the underlying coefficient sequence but does not display the block-valuation enumerator or Gaussian law in its inspected entry. The origin of the sequence was Montgomery and Shapiro's problem, cited in [1]. Related 2-adic valuation work for Stirling numbers and integral sequences concerns different arithmetic sequences, not this distribution.

## Limitations
The Gaussian theorem refers only to complete blocks \(0\le n<4^L\); behavior over arbitrary truncations is not claimed. It is not a classification for all central-binomial parameters or primes. The work is independently unaudited; mathematical priority is subject to earlier unindexed or subsequently found equivalent work. The primality/divisibility formulas of [1] are acknowledged as prior results.

## References
[1] A. Straub, V. H. Moll and T. Amdeberhan, *The p-adic valuation of k-central binomial coefficients*, arXiv:0811.2028v1, first posted 2008-11-13, particularly §§2–3, (2.2), (2.9), (3.11), (3.15), Corollary 3.4 and Theorem 3.7. https://arxiv.org/abs/0811.2028 . Later published in *Acta Arithmetica* **140** (2009), 31–42, DOI:10.4064/aa140-1-2.
[2] H. Montgomery and H. S. Shapiro, Problem 11380, *American Mathematical Monthly* (August–September 2008), as cited in [1].
[3] *The On-Line Encyclopedia of Integer Sequences*, A004987, 3-central binomial coefficients, https://oeis.org/A004987 (inspected coefficient entry).
