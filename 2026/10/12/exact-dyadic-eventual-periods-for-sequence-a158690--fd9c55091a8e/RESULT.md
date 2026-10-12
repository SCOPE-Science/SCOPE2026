# Exact dyadic eventual periods for sequence A158690

## Finding
Let the integers \(a(n)\), \(n\geq0\), be defined by the formal exponential generating series
\[
\sum_{n\geq0}a(n)\frac{t^n}{n!}
=1+\sum_{m\geq1}\prod_{j=1}^{m}\bigl(1-e^{-(2j-1)t}\bigr).
\]
For every integer \(k\geq2\) and every integer \(n\geq k+3\), put \(h=2^{k-1}\). Then
\[
a(n+h)-a(n)\equiv
\begin{cases}
2^{k+2}\pmod{2^{k+3}},&n\text{ even},\\
0\pmod{2^{k+3}},&n\text{ odd}.
\end{cases}
\]
Consequently, for **every integer \(r\geq5\)** the sequence \(a(n)\bmod 2^r\) has **least eventual period exactly \(2^{r-3}\)**. In fact, that period works for every \(n\geq r\). The assertion concerns eventual periods, not periodicity from index zero or the minimal preperiod.

## Assumptions and scope
All series are formal power series over the integers or rationals, as appropriate; every coefficient in the defining series receives finitely many contributions. An eventual period \(d>0\) modulo \(M\) means \(a(n+d)\equiv a(n)\pmod M\) for all sufficiently large \(n\). A least eventual period is the smallest such positive integer. The theorem covers the entire infinite family of moduli \(2^r\), \(r\geq5\), but no assertion is made about odd prime powers or mixed moduli.

## Proof
**1. Integral Stirling expansion.** Put \(y=e^t-1\) and
\[
H(y)=1+\sum_{m\geq1}\prod_{j=1}^m\bigl(1-(1+y)^{-(2j-1)}\bigr)
=\sum_{m\geq0}c_m y^m.
\]
Because each factor lies in \(y\mathbb Z[[y]]\), every \(c_m\) is an integer. The Stirling-number expansion (with \(S(N,m)=0\) for \(m>N\)) gives, for \(N\geq1\),
\[
a(N)=\sum_{m=0}^{N}c_m\,m!S(N,m),\qquad
m!S(N,m)=\sum_{j=0}^{m}(-1)^{m-j}\binom mj j^N.
\]
To compare different indices, extend the finite sum to any sufficiently large common upper limit. Modulo a fixed power of two, the terms with sufficiently large \(m\) vanish, because \(m!\) is divisible by that power. Thus all subsequent congruence rearrangements are finite modulo their respective moduli.

**2. Universal odd-base lift.** Fix \(k\geq2\), \(h=2^{k-1}\), and \(n\geq k+3\). For each even integer \(j\geq0\), both \(j^n\) and \(j^{n+h}\) are divisible by \(2^{k+3}\). For odd \(j\), define the integer \(u(j)=(j^2-1)/8\). With \(t=k-2\), the binomial formula yields
\[
\frac{j^h-1}{2^{k+1}}=
\frac{(1+8u(j))^{2^t}-1}{8\,2^t}
\equiv u(j)\pmod4.
\]
Indeed, each term of degree \(s\geq2\), when present, is divisible by four after normalization: use \(\nu_2\binom{2^t}{s}\geq t-\nu_2(s)\) and \(3(s-1)-\nu_2(s)\geq2\). Hence
\[
\frac{j^{n+h}-j^n}{2^{k+1}}\equiv
\begin{cases}
u(j)\pmod4,&j\text{ odd},\ n\text{ even},\\
j\,u(j)\pmod4,&j\text{ odd},\ n\text{ odd},\\
0\pmod4,&j\text{ even}.
\end{cases}
\]
All quotients are integers.

**3. Finite-difference truncation modulo four.** For \(\epsilon\in\{0,1\}\), define on nonnegative integers \(j\)
\[
U_\epsilon(j)=
\begin{cases}
j^\epsilon(j^2-1)/8,&j\text{ odd},\\
0,&j\text{ even}.
\end{cases}
\]
Let \(\Delta U(j)=U(j+1)-U(j)\). For odd \(j\), direct calculation gives
\[
U_\epsilon(j+4)\equiv U_\epsilon(j)+(j+2)j^\epsilon\pmod4,
\quad U_\epsilon(j+8)\equiv U_\epsilon(j)+2j^\epsilon\pmod4.
\]
For even \(j\), these three function values vanish. Since
\[
\Delta^8=(E-1)^8\equiv E^8+2E^4+1\pmod4
\]
for the shift operator \(EU(j)=U(j+1)\), we obtain \(\Delta^8U_\epsilon(j)\equiv0\pmod4\) for all \(j\geq0\). Therefore \(\Delta^mU_\epsilon(0)\equiv0\pmod4\) for every \(m\geq8\).

A direct eight-coefficient expansion of \(H(y)\) and eight finite differences gives the following exact input and residue rows (the calculations are reproduced independently in the accompanying checker):

| \(m\) | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| \(c_m\) | 1 | 1 | 2 | 7 | 33 | 197 | 1419 | 11966 |
| \(\Delta^mU_0(0)\bmod4\) | 0 | 0 | 0 | 1 | 0 | 1 | 2 | 0 |
| \(\Delta^mU_1(0)\bmod4\) | 0 | 0 | 0 | 3 | 0 | 1 | 2 | 2 |

Consequently,
\[
\sum_{m\geq0}c_m\Delta^mU_0(0)\equiv2\pmod4,
\quad
\sum_{m\geq0}c_m\Delta^mU_1(0)\equiv0\pmod4.
\]
Combining the Stirling expansion in Step 1 and normalized power differences in Step 2 proves the displayed parity-sensitive congruence.

**4. Exact eventual period.** The number \(h=2^{k-1}\) is even. Adding the two congruences with starting indices \(n\) and \(n+h\), both of the same parity, gives
\[
a(n+2^k)-a(n)\equiv0\pmod{2^{k+3}},\qquad n\geq k+3.
\]
However, for every sufficiently large **even** \(n\), the half-shift difference \(a(n+2^{k-1})-a(n)\) is congruent to \(2^{k+2}\), and is thus nonzero modulo \(2^{k+3}\). Hence \(2^{k-1}\) is not an eventual period. Since the least eventual period of an eventually periodic sequence divides each eventual period, and \(2^k\) is a power of two, its least eventual period must be precisely \(2^k\). Relabel \(r=k+3\).

## Verification
The included standard-library-only Python program `verify.py` computes the sequence independently in two ways: direct exponential-generating-function convolution and an integral Stirling transform of \(H(y)\). The methods agree for every index \(0\leq n\leq145\), modulo \(8192\), and reproduce all 15 OEIS initial terms modulo that modulus. The checker also computes the eight polynomial coefficients and the two finite-difference rows, confirms 705 parity-sensitive half-shift congruences for \(2\leq k\leq7\), and checks the eventual periods for \(5\leq r\leq10\) wherever the finite range permits. The analytic/algebraic proof above, not the finite enumeration, establishes the infinite family.

## Relationship to prior work
Ahaan Kallat, *A Proof of Bala's Congruence Conjectures for A158690*, arXiv:2609.07238v1 (first public September 7, 2026), proves that Carmichael's function \(\lambda(M)\) is an eventual period modulo every \(M\), via the same formal Stirling representation. For \(M=2^r\), \(r\geq5\), that provides period \(2^{r-2}\), but not the least eventual period. The present result identifies the least period as \(2^{r-3}\) and proves its sharpness through a parity-sensitive half-shift obstruction. The OEIS entry records an isolated period-two example modulo \(16\), not the infinite classification for \(r\geq5\). The primary source and the relevant OEIS entry have been inspected in full for these statements. No claim is made that mathematical indexing alone establishes worldwide novelty.

## Limitations
The earliest exact preperiod for each modulus is not classified. The theorem does not address odd moduli. Any unindexed or inaccessible overlapping result could affect the originality assessment; no independent audit has been performed.

## References
1. A. Kallat, *A Proof of Bala's Congruence Conjectures for A158690*, arXiv:2609.07238v1, September 7, 2026, https://arxiv.org/html/2609.07238v1.
2. OEIS Foundation, *A158690*, https://oeis.org/A158690, particularly Peter Bala's December 18, 2021 conjectures and their 2026 update.
