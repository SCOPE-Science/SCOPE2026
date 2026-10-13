# Sun's prime-counting root monotonicity conjecture
## Finding
Let \(\pi(x)\) be the number of primes not exceeding \(x\). For every integer \(n>4\) and every integer \(k\) with
\[
1\le k\le n,
\]
one has
\[
\pi(kn)^{1/k}>\pi((k+1)n)^{1/(k+1)}.
\]
This proves Conjecture 2.7(i) from Sun's paper on combinatorial properties of primes.

## Assumptions and scope
All logarithms are natural. The proof uses the classical Rosser--Schoenfeld explicit lower bound
\[
\pi(x)>\frac{x}{\log x}\qquad(x\ge17).
\]
No hypothesis on prime gaps is used.

The argument concerns exactly the two-parameter range in the conjecture:
\[
n\in\mathbb Z,\quad n>4,\qquad 1\le k\le n.
\]

## Proof
Put
\[
x=kn,\qquad A=\pi(x),\qquad B=\pi(x+n),
\]
and let
\[
d=B-A.
\]
The interval
\[
(x,x+n]
\]
contains exactly \(n\) integers. Since \(x\ge5\), every prime in this interval is odd. Therefore
\[
d\le \left\lceil\frac n2\right\rceil.
\tag{1}
\]

Assume first that
\[
x\ge17.
\]
The explicit prime-counting bound gives
\[
A>\frac{x}{\log x}.
\tag{2}
\]

We first establish a convenient elementary estimate. For \(x\ge17\),
\[
\log x<x^{2/5}.
\tag{3}
\]
Indeed,
\[
17^{2/5}>3>\log17;
\]
the first inequality is equivalent to
\[
17^2>3^5,
\]
that is,
\[
289>243,
\]
while \(3>\log17\) follows from
\[
e^3>1+3+\frac{3^2}{2!}+\frac{3^3}{3!}+\frac{3^4}{4!}+\frac{3^5}{5!}>17.
\]
Moreover, the derivative of
\[
x^{2/5}-\log x
\]
is
\[
\frac{(2/5)x^{2/5}-1}{x}>0
\]
for \(x\ge17\). This proves (3).

Taking logarithms in (3) yields
\[
\log\log x<\frac25\log x.
\]
Hence
\[
\frac{\log(x/\log x)}{\log x}
=
1-\frac{\log\log x}{\log x}
>
\frac35.
\tag{4}
\]

Since \(u\log u\) is increasing for \(u>e^{-1}\), (2) and (4) give
\[
A\log A
>
\frac{x}{\log x}\log\!\left(\frac{x}{\log x}\right)
>
\frac{3x}{5}
=
\frac{3kn}{5}.
\tag{5}
\]
For every integer \(n\ge5\),
\[
\left\lceil\frac n2\right\rceil\le\frac{3n}{5}.
\tag{6}
\]
Combining (1), (5), and (6),
\[
kd\le k\left\lceil\frac n2\right\rceil<A\log A.
\tag{7}
\]

If \(d=0\), then \(B=A\) and the desired inequality is immediate because \(A>1\). If \(d>0\), then
\[
k\log\frac BA
=
k\log\left(1+\frac dA\right)
<
\frac{kd}{A}
<
\log A.
\]
Therefore
\[
k\log B<(k+1)\log A,
\]
so
\[
B^k<A^{k+1}.
\]
Taking the positive \(k(k+1)\)-st root gives
\[
A^{1/k}>B^{1/(k+1)}.
\]

It remains only to check \(x=kn<17\). The possible pairs \((n,k)\) are
\[
\begin{aligned}
&(5,1),(5,2),(5,3),(6,1),(6,2),(7,1),(7,2),(8,1),(8,2),\\
&(9,1),(10,1),(11,1),(12,1),(13,1),(14,1),(15,1),(16,1).
\end{aligned}
\]
For these pairs, direct prime counting gives respectively
\[
(A^{k+1},B^k)=
\]
\[
\begin{aligned}
&(9,4),(64,36),(1296,512),(9,5),(125,49),(16,6),(216,64),\\
&(16,6),(216,81),(16,7),(16,8),(25,8),(25,9),(36,9),\\
&(36,9),(36,10),(36,11),
\end{aligned}
\]
and every first coordinate is larger than the second. Thus
\[
B^k<A^{k+1}
\]
also in every remaining case.

The conjecture follows.

## Verification
The accompanying `verify.py` uses an exact sieve of Eratosthenes. It performs four checks.

First, it reconstructs every pair with
\[
n>4,\quad1\le k\le n,\quad kn<17
\]
and verifies the exact integer inequality
\[
\pi(kn)^{k+1}>\pi((k+1)n)^k.
\]

Second, it checks the classical lower bound
\[
\pi(x)>\frac{x}{\log x}
\]
through \(x=100000\) as a computational stress test.

Third, it verifies the original conjectured inequality for every
\[
5\le n\le2000,\qquad1\le k\le n.
\]

Fourth, it checks the interval-parity estimate and the sufficient inequality
\[
\pi(kn)\log\pi(kn)>k\left\lceil\frac n2\right\rceil
\]
through the same finite range whenever \(kn\ge17\).

The finite calculations are corroborative. The universal proof above rests on the published explicit prime-counting bound and elementary inequalities.

## Relationship to prior work
Sun's paper poses sixty conjectures about exact combinatorial behavior of the prime-counting function and related quantities. Its Conjecture 2.7(i) is exactly the inequality proved here. The latest inspected arXiv revision, dated 25 February 2016, still states the assertion as a conjecture.

The proof uses the classical explicit lower bound of Rosser and Schoenfeld,
\[
\pi(x)>\frac{x}{\log x}\qquad(x\ge17),
\]
and only the elementary observation that an interval of \(n\) consecutive integers above \(2\) contains at most
\[
\left\lceil\frac n2\right\rceil
\]
primes. The combination appears not to have been recorded as a solution of Sun's conjecture in the inspected sources.

The OEIS entry A238277 cited by Sun concerns Conjecture 2.7(ii), the square-valued interval-count assertion. It does not tabulate or imply the root-monotonicity statement in part (i).

## Limitations
The theorem proves only Conjecture 2.7(i). It does not address the square-valued interval-count statement in Conjecture 2.7(ii), nor Sun's neighboring conjectures.

The originality search covered the full primary paper, its latest pre-archive revision, exact-formula web searches, indexed research-record searches, and the related OEIS entry. An equivalent proof in unindexed notes or a source not surfaced by those searches remains a residual risk.

## References
1. Z.-W. Sun, “Problems on combinatorial properties of primes,” arXiv:1402.6641, first public 25 February 2014; final inspected preprint revision 25 February 2016; later in *Number Theory: Plowing and Starring through High Wave Forms*, World Scientific, 2015.
2. J. B. Rosser and L. Schoenfeld, “Approximate formulas for some functions of prime numbers,” *Illinois Journal of Mathematics* 6 (1962), 64--94.
3. M. Corciovei-Bănescu, “The relation between \(\pi(x)\) and certain arithmetic functions,” *Notes on Number Theory and Discrete Mathematics* 17 (2011), no. 3, 1--9.
4. OEIS Foundation, A238277.
