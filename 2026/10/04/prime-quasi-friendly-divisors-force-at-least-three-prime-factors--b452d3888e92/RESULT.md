# Prime quasi-friendly divisors force at least three prime factors in the host

## Finding
Let \(q\) be an odd prime and \(N\) a positive integer satisfying
\[
\frac{\sigma(N)}{N}=\frac{q+2}{q}.
\]
Then
\[
\omega(N)\ge 3,
\]
where \(\omega(N)\) denotes the number of distinct prime divisors of \(N\).

In the terminology of Holdener and Holdener, this says that if a prime \(q\) is a quasi-friendly divisor of a positive integer \(N\), then \(N\) cannot have exactly two distinct prime factors. Their Proposition 23 gives only \(\omega(N)\ge2\); the argument below rules out the remaining two-prime-support case uniformly.

## Assumptions and scope
The source paper proves that if \(q\) is an odd prime and
\[
\frac{\sigma(N)}{N}=\frac{q+2}{q},
\]
then \(N\) is an odd square, \(q\) is its smallest prime divisor, and \(N\) has at least two distinct prime divisors. It also proves that every other prime divisor \(r\) of \(N\) satisfies
\[
r\ge \sigma(q)=q+1.
\]

The paper ends by asking whether any positive integer can have a prime quasi-friendly divisor at all and conjectures that the answer is no. The present result does not settle that full question; it proves that any hypothetical example must involve at least three distinct prime factors.

## Proof
Assume for contradiction that \(N\) has exactly two distinct prime divisors. By the source paper's Proposition 23, \(N\) is a square and \(q\) is its smallest prime divisor. Hence
\[
N=q^{2a}r^{2b}
\]
for some integers \(a,b\ge1\) and an odd prime \(r>q\). Proposition 22 gives \(r\ge q+1\), so in fact \(r\ge q+2\).

For every prime \(p\) and finite exponent \(e\ge1\),
\[
\frac{\sigma(p^e)}{p^e}<\frac{p}{p-1}.
\]
Therefore
\[
\frac{q+2}{q}
=
\frac{\sigma(q^{2a})}{q^{2a}}
\frac{\sigma(r^{2b})}{r^{2b}}
<
\frac{q}{q-1}\frac{r}{r-1}.
\]
After clearing positive denominators,
\[
(q-2)r<q^2+q-2,
\]
so
\[
r<q+3+\frac{4}{q-2}.
\]

If \(q\ge7\), then the right side is less than \(q+4\). Since \(q\) and \(r\) are odd primes and \(r\ge q+2\), this forces
\[
r=q+2.
\]
For \(q=5\), the same inequality gives \(7\le r<28/3\), again forcing \(r=7=q+2\). For \(q=3\), it gives \(5\le r<10\), so only \(r=5\) or \(r=7\) remain.

First treat every case with
\[
r=q+2.
\]
This includes all \(q\ge5\) and the subcase \((q,r)=(3,5)\). The defining abundancy identity becomes
\[
\sigma(q^{2a})\sigma(r^{2b})
=q^{2a-1}r^{2b+1}.
\]
Now \(\sigma(q^{2a})\equiv1\pmod q\), so it has no factor \(q\); similarly \(\sigma(r^{2b})\equiv1\pmod r\), so it has no factor \(r\). Since the product on the right has no prime factors other than \(q\) and \(r\), the two factors must therefore be
\[
\sigma(q^{2a})=r^{2b+1},
\qquad
\sigma(r^{2b})=q^{2a-1}.
\]
Put \(n=2a+1\), which is odd. Reducing the first equality modulo \(r\), and using \(q\equiv-2\pmod r\), gives
\[
0\equiv 1+q+\cdots+q^{n-1}
\equiv 1-2+2^2-\cdots+2^{n-1}\pmod r.
\]
Because \(r\ge5\), multiplication by \(-3\) is legitimate, and the geometric-sum identity yields
\[
2^n\equiv-1\pmod r.
\]
On the other hand, reducing the second equality modulo \(r\) gives
\[
1\equiv q^{n-2}\equiv(-2)^{n-2}\pmod r.
\]
Since \(n-2\) is odd,
\[
2^{n-2}\equiv-1\pmod r.
\]
Multiplying this last congruence by \(4\) and comparing with \(2^n\equiv-1\pmod r\) gives
\[
4\equiv1\pmod r,
\]
so \(r\mid3\), contradicting \(r\ge5\).

It remains only to exclude \((q,r)=(3,7)\). In that case
\[
\frac{\sigma(3^{2a})\sigma(7^{2b})}{3^{2a}7^{2b}}=\frac53,
\]
so
\[
\sigma(3^{2a})\sigma(7^{2b})
=5\cdot3^{2a-1}7^{2b}.
\]
Since \(\sigma(7^{2b})\equiv1\pmod7\), all of the factor \(7^{2b}\) on the right must divide \(\sigma(3^{2a})\). In particular,
\[
7\mid\sigma(3^{2a})=\frac{3^{2a+1}-1}{2}.
\]
Thus
\[
3^{2a+1}\equiv1\pmod7.
\]
But the multiplicative order of \(3\) modulo \(7\) is \(6\), which cannot divide the odd integer \(2a+1\). This contradiction closes the final case.

Hence \(N\) cannot have exactly two distinct prime divisors, and therefore \(\omega(N)\ge3\).

## Verification
The proof is symbolic and covers all odd primes \(q\) and all positive exponents. The accompanying `verify.py` is a regression check only. It verifies the algebraic cutoff for the second prime, checks the special \(q=3\) candidate set, confirms the relevant multiplicative order modulo \(7\), and brute-checks the defining abundancy equation over a large finite grid of two-prime squares. No finite experiment is used as an infinite proof.

## Relationship to prior work
Holdener and Holdener's Proposition 23 states that a solution of
\[
\frac{\sigma(N)}{N}=\frac{q+2}{q}
\]
with \(q\) an odd prime must be a square having at least two distinct prime divisors, with \(q\) the smallest. Proposition 22 further gives a lower bound for every other prime divisor. The paper's conclusion explicitly asks whether a prime quasi-friendly divisor can exist and conjectures that none do.

The result here is a strict strengthening of Proposition 23: the two-prime-support case is impossible for every odd prime \(q\). Targeted searches using the exact ratio, the paper title, the phrase “prime quasi-friendly divisor,” and the two-prime-support formulation did not locate this strengthening. An older paper of Ryan studies the same family of abundancy ratios, but an accessible full-text copy could not be inspected; the 2020 source cites that work and nevertheless still states the prime quasi-friendly-divisor question as open.

## Limitations
The theorem does not rule out hosts with three or more distinct prime factors. In particular, it does not settle whether \((q+2)/q\) is an abundancy ratio for any odd prime \(q\).

There is a residual originality risk from older or unindexed abundancy literature, especially the inaccessible full text of Ryan's 2002 paper. The source paper's own 2020 literature review and open-question statement mitigate, but do not eliminate, that risk.

## References
1. C. A. Holdener and J. A. Holdener, “Characterizing Quasi-Friendly Divisors,” *Journal of Integer Sequences* 23 (2020), Article 20.8.4, published 2 September 2020.
2. R. F. Ryan, “Results concerning uniqueness of \(\sigma(p^n q^m)/(p^n q^m)\) and related topics,” *International Mathematical Journal* 2 (2002), 497--514.
