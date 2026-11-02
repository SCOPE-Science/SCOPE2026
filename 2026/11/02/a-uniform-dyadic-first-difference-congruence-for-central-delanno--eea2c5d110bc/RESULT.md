# A uniform dyadic first-difference congruence for central Delannoy numbers

## Finding
Let \(d(n)=\sum_{k=0}^{n}2^k\binom nk^2\) be the central Delannoy numbers and let \(\mathbb Z_2\) denote the ring of \(2\)-adic integers. There is a continuous extension
\[
F(x)=\sum_{k\ge0}2^k\binom{x}{k}^{2},\qquad x\in\mathbb Z_2,
\]
whose values at nonnegative integers are \(d(n)\). For all \(x\in\mathbb Z_2\) and nonzero \(h\in32\mathbb Z_2\),
\[
\boxed{\frac{F(x+h)-F(x)}h\equiv4x+2x(x-1)(2x-1)\pmod8.}
\]
In particular, for every \(b\ge0\) with \(b\equiv1,2\pmod4\), every odd positive \(a\), and every integer \(r\ge5\),
\[
\boxed{\nu_2\bigl(d(b+a2^{r+1})-d(b+a2^r)\bigr)=r+2.}
\]
This gives the full first nonzero slope stratum of Lengyel's 2021 Conjecture 4, with an explicit uniform onset.

## Assumptions and scope
Here \(\binom{x}{k}=x(x-1)\cdots(x-k+1)/k!\), \(\binom{x}{0}=1\), and congruences of \(2\)-adic rationals mean that the difference belongs to the indicated ideal of \(\mathbb Z_2\). The quotient in the first displayed congruence is a \(2\)-adic integer; it need not be an ordinary integer when \(h\) has an odd factor. The integer result concerns precisely the shifts \(b\equiv1,2\pmod4\), with \(b\ge0\), \(a\ge1\) odd, and \(r\ge5\). No assertion is made for the other two shift residue classes.

## Proof
For every \(x\in\mathbb Z_2\), each generalized binomial coefficient \(\binom{x}{k}\) is in \(\mathbb Z_2\). Since \(2^k\binom{x}{k}^2\) lies in \(2^k\mathbb Z_2\), the defining series for \(F\) converges uniformly on \(\mathbb Z_2\), hence is continuous. For an ordinary nonnegative integer \(n\), the binomial coefficients vanish at \(k>n\), so \(F(n)=d(n)\).

Put \(B_k(x)=\binom{x}{k}\). The generalized Vandermonde identity, valid as a polynomial identity and therefore for arbitrary \(x,h\in\mathbb Z_2\), gives
\[
\frac{B_k(x+h)-B_k(x)}h
 =\sum_{j=1}^k B_{k-j}(x)\frac{B_j(h)}h,
\qquad
\frac{B_j(h)}h=\frac1j\binom{h-1}{j-1}.
\]
Writing \(s(k)=\lfloor\log_2 k\rfloor\), every summand on the right lies in \(2^{-s(k)}\mathbb Z_2\), and therefore
\[
\frac{B_k(x+h)^2-B_k(x)^2}{h}\in2^{-s(k)}\mathbb Z_2.
\]
Consequently, for every \(k\ge5\),
\[
2^k\frac{B_k(x+h)^2-B_k(x)^2}{h}\in 2^{k-s(k)}\mathbb Z_2\subseteq8\mathbb Z_2.
\]
The bound is uniform in \(x\) and in every nonzero \(h\in\mathbb Z_2\), so one may divide the uniformly convergent difference series termwise; the omitted tail has quotient in \(8\mathbb Z_2\).

For the remaining four summands, define \(P_k(x)=2^kB_k(x)^2\). Their explicit forms are
\[
P_1(x)=2x^2,\quad P_2(x)=x^2(x-1)^2,\quad
P_3(x)=\frac29[x(x-1)(x-2)]^2,\quad
P_4(x)=\frac1{36}[x(x-1)(x-2)(x-3)]^2.
\]
Every coefficient of each of these four polynomials lies in \(2^{-2}\mathbb Z_2\), because \(\nu_2(36)=2\). For any polynomial with this coefficient property, direct expansion of powers shows
\[
\frac{P(x+h)-P(x)}h-P'(x)\in h\,2^{-2}\mathbb Z_2,
\]
so the difference is in \(8\mathbb Z_2\) whenever \(h\in32\mathbb Z_2\). Thus the complete quotient is congruent modulo \(8\) to \(P'_1(x)+P'_2(x)+P'_3(x)+P'_4(x)\).

To dispose of the last two derivatives, differentiate the binomial coefficient via the formal generating-function identity \((1+z)^x=\sum_{j\ge0}B_j(x)z^j\):
\[
B'_k(x)=\sum_{j=1}^k\frac{(-1)^{j-1}}j B_{k-j}(x)
\in2^{-s(k)}\mathbb Z_2.
\]
It follows that \(P'_k(x)=2^{k+1}B_k(x)B'_k(x)\in2^{k+1-s(k)}\mathbb Z_2\). For \(k=3,4\), these derivatives belong to \(8\mathbb Z_2\). The first two derivatives are \(P'_1(x)=4x\) and \(P'_2(x)=2x(x-1)(2x-1)\), proving the stated uniform congruence.

If \(b\equiv1\) or \(2\pmod4\), direct reduction of the resulting polynomial gives
\[
4b+2b(b-1)(2b-1)\equiv4\pmod8.
\]
Set \(h=a2^r\), with \(a\) odd and \(r\ge5\). Apply the uniform congruence at \(x=b\) with increments \(h\) and \(2h\), respectively, and subtract:
\[
\frac{F(b+2h)-F(b+h)}h\equiv 4\pmod8.
\]
The quotient is therefore exactly divisible by \(4\) and not by \(8\) in \(\mathbb Z_2\). Since \(\nu_2(h)=r\) and both arguments are nonnegative integers, the claimed \(2\)-adic valuation of the Delannoy-number difference is \(r+2\).

## Verification
The accompanying standalone Python program computes central Delannoy numbers from the exact recurrence \((n+1)d(n+1)=(6n+3)d(n)-nd(n-1)\). It checks the uniform first-difference congruence on an explicit finite grid of indices and increments, and checks the shifted valuation for several odd multipliers, shifts in both residue classes, and indices beyond the uniform threshold. It also checks the four low-degree polynomial coefficients, the valuation bound for all summands through a finite cutoff, and the algebraic residue classes. These are independent finite sanity checks. The proof for every index uses the Vandermonde identity, binomial integrality, and uniform tail estimates, not extrapolation from the checks.

## Relationship to prior work
Tamás Lengyel, *On Some p-adic Properties and Supercongruences of Delannoy and Schröder Numbers* (INTEGERS 21 (2021), A86; published 27 August 2021), states in Conjecture 4 that the successive dyadic difference has valuation \(r+2\nu_2(b(b+1))\) for fixed nonexceptional shift \(b\), odd multiplier \(a\), and sufficiently large \(r\). For \(b\equiv1,2\pmod4\), the factor \(\nu_2(b(b+1))\) equals \(1\); the present theorem verifies the entire first stratum simultaneously and supplies a universal explicit threshold. Its uniform difference-quotient congruence is more precise than a statement of individual term valuations. Lengyel's other assertions about \(\nu_2(d(n)-1)\) do not determine cancellation in the two-term differences. Mikić (2023) addresses other divisibility questions for generalized central trinomial coefficients and Legendre polynomials. Jia and Huang (2024) study weighted Delannoy/Schröder sums and odd-prime congruences, rather than these individual dyadic differences.

## Limitations
This does not resolve Lengyel's Conjecture 4 for \(b\equiv0\) or \(3\pmod4\), nor does it show that \(r=5\) is the smallest valid universal threshold. The original conjecture treats other valuations and shifts. No independent audit has been performed. Unindexed covering literature cannot be categorically excluded.

## References
1. T. Lengyel, *On Some p-adic Properties and Supercongruences of Delannoy and Schröder Numbers*, INTEGERS 21 (2021), Article A86, published 2021-08-27. https://sites.oxy.edu/lengyel/papers/v86%20ON%20SOME%20p-ADIC%20PROPERTIES%20AND%20SUPERCONGRUENCES%20OF%20DELANNOY%20AND%20SCHRODER%20NUMBERS,%20INTEGERS2021.pdf
2. J. Mikić, *On new divisibility properties of generalized central trinomial coefficients and Legendre polynomials*, arXiv:2311.14623 (2023).
3. C.-B. Jia and J.-Q. Huang, *Congruences involving Delannoy numbers and Schröder numbers*, arXiv:2410.17522v1 (2024-10-23).
