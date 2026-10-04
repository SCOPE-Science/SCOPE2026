# Prime-peeling criterion for rational products of \(1+1/p\)

## Finding
Let
\[
\mathcal S=
\left\{
\prod_p\left(1+\frac1p\right)^{a_p}
:
a_p\in\mathbb Z_{\ge0},
\text{ and only finitely many }a_p\ne0
\right\}.
\]
The empty product gives \(1\). If only nonempty products are allowed, delete \(1\) from the final set.

There is a deterministic finite test for membership in \(\mathcal S\).

Start with a positive rational \(q\). If there is a prime \(P\ge5\) with
\[
\nu_P(q)\ne0,
\]
take the largest such \(P\). Then membership in \(\mathcal S\) requires
\[
\nu_P(q)<0.
\]
If this fails, reject \(q\). If it holds, the exponent of the generator belonging to \(P\) is forced:
\[
a_P=-\nu_P(q).
\]
Replace
\[
q
\quad\text{by}\quad
q\left(\frac{P}{P+1}\right)^{a_P}.
\]
Repeat.

At every successful step the largest prime having nonzero valuation strictly decreases, so the process terminates. At termination,
\[
q=2^x3^y
\]
for some integers \(x,y\). The original rational lies in \(\mathcal S\) if and only if
\[
x+2y\ge0
\qquad\text{and}\qquad
x+y\ge0.
\]
In that case the two remaining exponents are forced:
\[
a_2=x+2y,
\qquad
a_3=x+y.
\]

Hence the procedure both decides membership and reconstructs the unique representation.

A particularly simple corollary is
\[
\mathcal S\cap\mathbb Z_{>0}
=
\{2^u3^v:u,v\in\mathbb Z_{\ge0}\}.
\]
Thus the positive integers representable as finite products of powers of
\[
1+\frac1p
\]
are exactly the \(3\)-smooth positive integers.

## Assumptions and scope
For a prime \(\ell\), \(\nu_\ell(q)\) denotes the usual \(\ell\)-adic valuation of a positive rational \(q\), allowed to be negative.

The exponents \(a_p\) are nonnegative integers with finite support; equivalently, each prime actually used in the product has a positive integer exponent.

The theorem is a recognition and reconstruction theorem for rational numbers. It does not make an asymptotic statement about the number of representable rationals of bounded height.

## Proof
Suppose first that
\[
q=
\prod_p
\left(\frac{p+1}{p}\right)^{a_p}
\]
belongs to \(\mathcal S\), and let \(P\) be the largest prime with \(a_P>0\).

Assume
\[
P\ge5.
\]
The denominator contribution of the \(P\)-factor to the \(P\)-adic valuation is
\[
-a_P.
\]
No numerator from another generator contributes a factor \(P\). Indeed, if \(r<P\) is prime and
\[
P\mid r+1,
\]
then
\[
r+1=P,
\]
so
\[
r=P-1,
\]
which is even and greater than \(2\), hence not prime. The numerator \(P+1\) is also not divisible by \(P\).

Therefore
\[
\nu_P(q)=-a_P<0.
\]
Moreover every prime factor of \(r+1\), for a prime \(r\le P\), is at most \(P\), and when \(r=P\ge5\), every prime factor of \(P+1\) is strictly less than \(P\). Thus \(P\) is the largest prime at which \(q\) has nonzero valuation.

It follows that the largest prime visible in the reduced rational \(q\) is exactly the largest prime generator, and its exponent is recovered by
\[
a_P=-\nu_P(q).
\]
Dividing out that generator gives
\[
q'
=
q\left(\frac{P}{P+1}\right)^{a_P},
\]
whose representation uses only primes smaller than \(P\). This proves the validity of one peeling step and shows that the largest possible prime strictly decreases. Repeating eventually leaves only the primes \(2\) and \(3\).

Now write the terminal rational as
\[
q=2^x3^y.
\]
A representation using only the generators for \(2\) and \(3\) has the form
\[
q=
\left(\frac32\right)^u
\left(\frac43\right)^v
=
2^{-u+2v}3^{u-v},
\]
with
\[
u,v\in\mathbb Z_{\ge0}.
\]
Therefore
\[
x=-u+2v,
\qquad
y=u-v.
\]
Solving this linear system gives
\[
u=x+2y,
\qquad
v=x+y.
\]
Hence such a terminal representation exists exactly when
\[
x+2y\ge0
\qquad\text{and}\qquad
x+y\ge0,
\]
and then its exponents are unique.

This proves necessity of every step.

Conversely, suppose the peeling procedure never encounters a largest prime with nonnegative valuation and the terminal inequalities hold. Each successful peel records a positive integer exponent
\[
a_P=-\nu_P(q).
\]
The terminal inequalities give nonnegative integers
\[
a_2=x+2y,
\qquad
a_3=x+y.
\]
Reversing the recorded peeling steps reconstructs the original rational as
\[
\prod_p
\left(\frac{p+1}{p}\right)^{a_p}.
\]
Therefore the conditions are sufficient.

The same argument also proves uniqueness, because at every prime
\[
P\ge5
\]
the exponent is forced by the current largest valuation, and the final two exponents are uniquely determined by the two linear equations.

For the integer corollary, let
\[
q\in\mathcal S\cap\mathbb Z_{>0}.
\]
If a generator with largest prime
\[
P\ge5
\]
occurred, then the preceding argument would give
\[
\nu_P(q)=-a_P<0,
\]
contradicting integrality. Hence only the primes \(2\) and \(3\) can occur. Conversely, if
\[
q=2^u3^v
\]
with
\[
u,v\ge0,
\]
then
\[
q=
\left(\frac32\right)^{u+2v}
\left(\frac43\right)^{u+v},
\]
so every \(3\)-smooth positive integer belongs to \(\mathcal S\).

## Verification
The accompanying `verify.py` implements the peeling algorithm using exact rational arithmetic and trial-division factorization.

It verifies exact exponent recovery for all
\[
3^8-1=6560
\]
nonempty exponent vectors with exponents in
\[
\{0,1,2\}
\]
on the primes
\[
2,3,5,7,11,13,17,19.
\]
It also checks every positive integer through \(20000\), confirming that membership is equivalent to having no prime factor other than \(2\) and \(3\), and performs a grid test on reduced positive rationals of numerator and denominator at most \(250\).

These computations are regression evidence only. The all-rational criterion is proved symbolically above.

## Relationship to prior work
Noppakaew and Pongsriiam prove that a finite product
\[
\prod_p
\left(1+\frac1p\right)^{a_p}
\]
uniquely determines the primes and their positive exponents. They then ask in Question 32 for a determination of all rational numbers admitting such a representation.

Their uniqueness statement is not yet a membership criterion: it says that two existing representations cannot differ, but it does not decide from a given reduced rational whether a representation exists or recover one when it does.

The largest-prime argument above supplies exactly that missing step. For every prime at least \(5\), the sign of the largest visible valuation decides whether the next generator is possible and, if it is, determines its exponent. Only a two-dimensional terminal cone at the primes \(2\) and \(3\) remains.

The factors are the local quotients appearing in Dedekind's psi function:
\[
\frac{\psi(n)}n
=
\prod_{p\mid n}
\left(1+\frac1p\right).
\]
OEIS A001615 records \(\psi\) itself, and OEIS A203444 records the integer range of \(\psi\); neither database entry gives the multiplicative-semigroup membership criterion above for arbitrary repeated generator powers.

Targeted searches for Question 32, for the multiplicative semigroup generated by
\[
\frac{p+1}{p},
\]
for largest-prime or valuation peeling, and for a rational membership criterion did not locate an implication-equivalent result.

## Limitations
The result is an exact decision procedure rather than a closed inequality involving only the numerator and denominator of the input rational.

No counting asymptotic is given for representable rationals of bounded numerator, denominator, or height.

The strongest residual originality risk is an unindexed observation that the uniqueness proof can be sharpened into the same largest-prime reconstruction algorithm. The focal full text, targeted web searches, published-finding corpus semantic searches, and the closest Dedekind-psi OEIS entries were inspected without locating that statement.

## References
1. Passawan Noppakaew and Prapanpong Pongsriiam, “Product of Some Polynomials and Arithmetic Functions,” Journal of Integer Sequences 26 (2023), Article 23.9.1. Published 2 November 2023. Primary MSC 11A25.
2. OEIS A001615, Dedekind psi function.
3. OEIS A203444, numbers in the range of the Dedekind psi function.
