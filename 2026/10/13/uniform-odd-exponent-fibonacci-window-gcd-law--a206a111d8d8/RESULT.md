# Uniform odd-exponent Fibonacci window-gcd law

## Finding
Let \(F_0=0\), \(F_1=1\), and \(F_{n+2}=F_{n+1}+F_n\) for every \(n\ge0\). For positive integers \(r,k\), define the power-window sum
\[
W_n^{(r)}(k)=\sum_{j=1}^{k}F_{n+j}^{r}\quad(n\ge0),
\]
and let \(\mathcal G_r(k)=\gcd_{n\ge0}W_n^{(r)}(k)\), with the gcd taken as a positive integer. Then, uniformly for **every** pair of positive odd integers \(r,k\),
\[
\boxed{\mathcal G_r(k)=
\begin{cases}
2,&k\equiv3\pmod6,\\
1,&k\equiv1,5\pmod6.
\end{cases}}
\]
In addition, the infinite gcd admits an exact finite reduction, valid for every positive integer \(r\) and every positive integer \(k\):
\[
\mathcal G_r(k)=\gcd\bigl(W_0^{(r)}(k),W_1^{(r)}(k),\ldots,W_r^{(r)}(k)\bigr).
\]
The uniform odd-power statement extends the known first-power and square-power odd-window laws to every odd exponent, including all arbitrarily large odd exponents.

## Assumptions and scope
The classification concerns standard nonnegative-index Fibonacci numbers, positive odd powers \(r\), positive odd window lengths \(k\), and every shift \(n\ge0\). No upper bounds on these indices or parameters are imposed. The proof uses only elementary recurrence algebra, Cayley–Hamilton for a finite integer matrix, Cassini's identity, and the Fibonacci residues modulo \(2\) and \(4\). The finite-prefix formula itself does not require oddness of either parameter.

## Proof
**1. Invertible power recurrence and the finite-prefix reduction.** Put
\[
A=\begin{pmatrix}1&1\\1&0\end{pmatrix},\qquad
v_n=\begin{pmatrix}F_{n+1}\\F_n\end{pmatrix};\qquad
v_{n+1}=Av_n.
\]
Because \(\det A=-1\), both \(A\) and its inverse are integral. On the free abelian group of homogeneous degree-\(r\) polynomials in two variables, substitution by \(A\) induces an integer invertible matrix \(T_r\) of size \(r+1\). Its inverse is induced by \(A^{-1}\), so \(T_r\) is unimodular. Thus the characteristic polynomial has the form
\[
\chi_r(t)=t^{r+1}+c_rt^r+\cdots+c_1t+c_0,
\quad c_j\in\mathbb Z,\quad c_0=\pm1.
\]
By Cayley–Hamilton, the sequence \(x_n=F_n^r\), and every fixed linear combination of its translates, obeys
\[
x_{n+r+1}+c_rx_{n+r}+\cdots+c_1x_{n+1}+c_0x_n=0.
\]
Consequently the window-sum sequence \(W_n^{(r)}(k)\) satisfies this same monic integer recurrence. Every later term is an integer combination of its first \(r+1\) terms, proving the finite-prefix gcd identity in the Finding.

**2. Recover the missing zero-index difference.** Set
\[
D_n=F_{n+k}^{r}-F_n^{r}\quad(n\ge0).
\]
The sequence \(D_n\) satisfies the same recurrence. With \(g=\mathcal G_r(k)\), subtraction of adjacent windows gives
\[
W_{n+1}^{(r)}(k)-W_n^{(r)}(k)=D_{n+1},
\]
so \(g\mid D_n\) for every \(n\ge1\). Apply the recurrence for \(D_n\) at \(n=0\): since \(c_0=\pm1\), it expresses \(D_0\) as an integer linear combination of \(D_1,\ldots,D_{r+1}\). Therefore \(g\mid D_0=F_k^r\) as well. In particular,
\[
g\mid F_k^r,\qquad g\mid(F_{k+1}^r-1).
\]

**3. Exclude every odd prime.** Suppose \(r,k\) are odd and an odd prime \(p\) divides \(g\). The last two divisibilities imply \(F_k\equiv0\pmod p\) and \(F_{k+1}^r\equiv1\pmod p\). Cassini's identity, with \(k\) odd, reads
\[
F_{k+1}^{2}-F_kF_{k+2}=(-1)^k=-1.
\]
Hence \(F_{k+1}^{2}\equiv-1\pmod p\). Taking the \(r\)-th power and using that \(r\) is odd yields
\[
1\equiv(F_{k+1}^r)^2=(F_{k+1}^2)^r\equiv(-1)^r=-1\pmod p.
\]
This would force \(p\mid2\), a contradiction. Thus \(g\) is a power of \(2\).

**4. Determine the exact power of two.** Fibonacci residues modulo \(2\) have period \(3\), repeating \((0,1,1)\); modulo \(4\) they have period \(6\), repeating \((0,1,1,2,3,1)\).

When \(k\equiv3\pmod6\), each block of \(k\) consecutive Fibonacci numbers has an even number of odd entries. Since taking any positive power preserves parity, \(W_n^{(r)}(k)\) is even for every \(n\). But \(k+1\equiv4\pmod6\), so \(F_{k+1}\equiv3\pmod4\). For odd \(r\),
\[
D_1=F_{k+1}^r-1\equiv3^r-1\equiv2\pmod4.
\]
As \(g\mid D_1\), the gcd cannot be divisible by \(4\); therefore \(g=2\).

When \(k\equiv1\pmod6\), \(F_{k+2}\) is even and \(F_2=1\), so \(D_2=F_{k+2}^r-1\) is odd. When \(k\equiv5\pmod6\), \(F_{k+1}\) is even and \(F_1=1\), so \(D_1\) is odd. As \(g\) divides these differences and has no odd prime factors, \(g=1\) in both cases. The three residue classes exhaust the odd window lengths.

## Verification
A standalone exact-integer script, `verify.py`, can be run using `python3 verify.py`. It computes window gcds both from the first \(r+1\) windows and from a strictly longer independently accumulated window list. The included output records agreement with the theorem for every odd exponent from \(1\) to \(23\) and every odd window length from \(1\) to \(61\): \(372\) parameter pairs and \(8184\) longer-list windows. It also checks the period modulo \(4\) and the even-exponent boundary below. These are finite consistency tests; the unrestricted proof is the four-step argument above.

## Relationship to prior work
Guyer and Mbirika [1], especially Theorems 5.5 and 5.6, determine the first-power case \(r=1\), including the same odd-window residue classes. Mbirika and Spilker [2], Theorem 5.2, determine the square-power case \(r=2\), again with the same odd-window output, and their Section 6.1 identifies higher-power GCDs as a research direction. Those two papers do not state the uniform conclusion for every odd exponent \(r\ge3\), nor does either result imply it solely by comparing the displayed numeric values for \(r=1\) and \(r=2\). The new ingredient is an integer-unit constant recurrence for arbitrary powers, coupled with the odd-exponent Cassini obstruction. The first-power indexed sequence in [3] records the \(r=1\) case, not all odd exponents.

## Limitations
This theorem intentionally classifies **odd powers and odd window lengths**, not all exponent-window pairs and not arbitrary Gibonacci starting values. The parity assumption on the exponent is substantive: for example, every sum of \(25\) consecutive fourth powers of Fibonacci numbers is divisible by \(5\). Indeed, the identity \(F_{n+5}=5F_{n+1}+3F_n\) gives \(F_{n+5}\equiv3F_n\pmod5\); as \(F_0\equiv0\pmod5\) and \(F_1,F_2,F_3,F_4\not\equiv0\pmod5\), exactly the indices divisible by \(5\) give zero Fibonacci terms modulo \(5\). Thus precisely five terms in any \(25\)-block vanish modulo \(5\), while the fourth power of every other term is \(1\), yielding \(20\equiv0\pmod5\). Thus the displayed \(1\)/\(2\) dichotomy cannot simply be extended to all even exponents. The proof settles the stated infinite family but makes no claim of bibliographic exhaustiveness or independent external validation.

## References
[1] D. Guyer and aBa Mbirika, “GCD of sums of \(k\) consecutive Fibonacci, Lucas, and generalized Fibonacci numbers,” *Journal of Integer Sequences* 24 (2021), Article 21.9.8; arXiv:2104.12262, especially Theorems 5.5–5.6, https://arxiv.org/pdf/2104.12262.

[2] aBa Mbirika and J. Spilker, “GCD of sums of \(k\) consecutive squares of generalized Fibonacci numbers,” *Fibonacci Quarterly* 60 (2022), 255–269; arXiv:2204.12626 (first publicly submitted 2022-04-26), especially Theorem 5.2, Table 2 and Section 6.1, https://arxiv.org/pdf/2204.12626.

[3] OEIS A210209, “GCD of all sums of \(n\) consecutive Fibonacci numbers,” https://oeis.org/A210209.
