# Prime-power divisor spectrum for cobalancing-square windows outside three small primes

## Finding
Let \(b_0=b_1=0\) and \(b_{n+2}=6b_{n+1}-b_n+2\) for \(n\ge0\). For each integer \(k\ge1\), define the positive integer
\[
G(k)=\gcd_{n\ge0}\left(\sum_{j=0}^{k-1}b_{n+j}^{2}\right).
\]
For every prime \(p\ge5\), \(p\ne7\), let \(d_p\) be the multiplicative order of \(\lambda=3+2\sqrt2\) in \((\mathbb F_p[X]/(X^2-2))^\times\). The following complete prime-power law holds:
\[
\nu_p(G(k))=
\begin{cases}
1+\nu_5(k),&p=5\text{ and }6\mid k,\\
0,&p=5\text{ and }6\nmid k,\\
\nu_p(k),&p\ge11\text{ and }d_p\mid k,\\
0,&p\ge11\text{ and }d_p\nmid k.
\end{cases}
\]
In particular, \(5\) divides \(G(k)\) at every multiple of six, even at those not divisible by five. The result covers all primes at least five except seven, for every window length; it does not give the full numerical gcd.

## Assumptions and scope
All indices and window lengths are integers as indicated. The cobalancing sequence is fixed by the above inhomogeneous recurrence. \(\nu_p\) is the usual valuation of a nonzero integer. The polynomial algebra \(\mathbb F_p[X]/(X^2-2)\) may be a field or a product of two fields; the norm-one element \(3+2X\) is a unit in either case. The factor \(d_p\) exists and divides \(p-(2/p)\), with \((2/p)\) the Legendre symbol, and therefore \(p\nmid d_p\).

## Proof
**1. A five-exponential decomposition.** The recurrence implies \(2\mid b_n\). Write \(u_n=b_n/2\), so \(u_0=u_1=0\) and \(u_{n+2}=6u_{n+1}-u_n+1\). Fix \(p\ge5\), \(p\ne7\), and work in the finite étale ring \(R=\mathbb Z_p[X]/(X^2-2)\). Put \(s=X\), \(\lambda=3+2s\), and
\[
A=\frac{s-1}{8s},\quad B=\frac{s+1}{8s},\quad
u_n=A\lambda^n+B\lambda^{-n}-\frac14.
\]
The displayed expression has \(u_0=u_1=0\) and obeys the inhomogeneous recurrence; hence it equals \(u_n\) for every \(n\ge0\). Both \(A\) and \(B\) are units, since \(2s\), \(s+1\), and \(s-1\) are units for odd \(p\). Squaring yields
\[
u_n^2=A^2\lambda^{2n}+B^2\lambda^{-2n}-\frac A2\lambda^n-\frac B2\lambda^{-n}+\frac5{64}.
\]
Let \(T_h(k)=\sum_{j=0}^{k-1}\lambda^{hj}\) for \(h\in\{-2,-1,1,2\}\). Each square window \(\sum_{j=0}^{k-1}u_{n+j}^2\) is a linear combination of the five exponentials \(\lambda^{hn}\) with respective coefficients \(A^2T_2\), \(B^2T_{-2}\), \(-AT_1/2\), \(-BT_{-1}/2\), and \(5k/64\).

**2. Inverting the five window observations.** The five bases \(\lambda^{-2},\lambda^{-1},1,\lambda,\lambda^2\) are pairwise distinct modulo \(p\). Indeed, collisions would force \(\lambda^j=1\) for some \(j\in\{1,2,3,4\}\). Since \(\lambda\) and \(\lambda^{-1}\) are units, the norm computations
\[
N(\lambda-1)=-4,\quad N(\lambda+1)=8,\quad
N(\lambda^2+\lambda+1)=49,\quad N(\lambda^2+1)=36
\]
exclude this for every prime in scope; \(\lambda^3-1\) and \(\lambda^4-1\) factor into these terms. Consequently the five-by-five Vandermonde matrix for consecutive shifts \(n=0,1,2,3,4\) has unit determinant in \(R\). It is invertible modulo every \(p^e\). As \(A\), \(B\), and \(2\) are units, divisibility of all window sums by \(p^e\) is equivalent to simultaneous divisibility of \(5k\) and of every \(T_h(k)\).

**3. Reducing to one order test.** Both \(\lambda-1\) and \(\lambda+1\) are units at these primes. Therefore
\[
T_1(k)=\frac{\lambda^k-1}{\lambda-1},\quad
T_2(k)=\frac{\lambda^{2k}-1}{\lambda^2-1},
\]
and the sums for negative exponents differ from the positive ones only by units. Divisibility of \(T_1(k)\) implies that of \(T_2(k)\), since \(\lambda^{2k}-1=(\lambda^k-1)(\lambda^k+1)\). Thus for every \(e\ge1\),
\[
p^e\mid G(k)\quad\Longleftrightarrow\quad
p^e\mid 5k\ \text{and}\ \lambda^k\equiv1\pmod{p^e}\text{ in }R.
\]
We used \(b_n^2=4u_n^2\) and \(p\ge5\), so the factor four has no effect.

**4. Exact valuations.** Reduction modulo \(p\) gives \(\lambda^k\equiv1\) exactly when \(d_p\mid k\). If this fails, the valuation is zero. If it holds, \(p\nmid d_p\) and the standard odd-prime binomial lifting argument in the unramified or split étale ring gives
\[
\nu_p(\lambda^k-1)=\nu_p(\lambda^{d_p}-1)+\nu_p(k),
\]
with the first term at least one. (For a ring element, divisibility means divisibility of both integral coordinates; the two coordinates have the same minimum valuation under conjugation \(\lambda\mapsto\lambda^{-1}\).) For \(p\ge11\), the second condition \(p^e\mid5k\) therefore truncates the common valuation to exactly \(\nu_p(k)\).

For \(p=5\), the element \(\lambda^3=99+70s\equiv-1\pmod5\) has order six. Directly, \(\lambda^6=19601+13860s\), so \(\nu_5(\lambda^6-1)=1\), because the second coordinate \(13860\) has exactly one factor five. Odd-prime lifting now gives \(\nu_5(\lambda^k-1)=1+\nu_5(k)\) when \(6\mid k\). Combined with the factor \(5k\) this proves the exceptional formula, completing the theorem.

## Verification
A standalone standard-library script, `verify.py`, checks the five-term square recurrence exactly, computes the global gcd from the first five windows, and compares the predicted valuations for all \(1\le k\le300\) and each of the 23 eligible primes below 103. There are 6900 exact valuation comparisons and 219 independent recurrence checks; all passed. The window reduction is valid because \(u_n^2\) satisfies the monic reversible recurrence whose characteristic polynomial is
\[
(X-1)(X^2-6X+1)(X^2-34X+1)
=X^5-41X^4+246X^3-246X^2+41X-1.
\]
The finite checks are corroboration, not a substitute for the all-primes proof.

## Relationship to prior work
Mbirika, Schrader, and Spilker (2023, arXiv:2301.05758), Section 6.1, Question 30, ask for gcds of sums of consecutive squares for Pell-related and balancing-related sequences, including cobalancing numbers. They derive partial results and report a factor-four observation for the cobalancing case, but do not give this exact all-good-prime valuation spectrum. Mbirika and Spilker (2022, arXiv:2204.12626) give exact gcd methods for homogeneous generalized Fibonacci recurrences, not this affine cobalancing-square sequence. Existing complementary results on balancing, Lucas-balancing, and Lucas-cobalancing windows do not imply the cobalancing calculation: the five-exponential affine square, its exceptional factor five, and its order criterion are different.

## Limitations
No valuations at primes \(2\), \(3\), or \(7\) are established. This is not a closed form for the entire integer \(G(k)\), and no assertion of uniqueness or independent external verification is made. The possible existence of an earlier unindexed general exponential-sum gcd theorem implying this formula remains an originality risk.

## References
- aBa Mbirika, Janee Schrader, and Jürgen Spilker, *Pell and associated Pell braid sequences as GCDs of sums of \(k\) consecutive Pell, balancing, and related numbers*, arXiv:2301.05758, first publicly posted 2023-01-13; see Section 6.1 and Question 30.
- aBa Mbirika and Jürgen Spilker, *GCD of sums of \(k\) consecutive squares of generalized Fibonacci numbers*, arXiv:2204.12626, first publicly posted 2022-04-26.
