# A sharp two-almost-prime barrier for equal consecutive alternating divisor sums
## Finding
Let \(\beta\) be the multiplicative alternating sum-of-divisors function
\[
\beta(p^a)=p^a-p^{a-1}+p^{a-2}-\cdots+(-1)^a
\]
on prime powers, extended multiplicatively. Let \(\Omega(m)\) denote the number of prime factors of \(m\), counted with multiplicity.

If
\[
\beta(n)=\beta(n+1)
\]
and
\[
\Omega(n)\le2,\qquad \Omega(n+1)\le2,
\]
then
\[
n=1.
\]
Therefore every nontrivial solution \(n>1\) of the consecutive-value equation satisfies
\[
\max\{\Omega(n),\Omega(n+1)\}\ge3.
\]
This multiplicity threshold is sharp: \(n=20\) is a solution, with
\[
\Omega(20)=3,\qquad \Omega(21)=2.
\]

## Assumptions and scope
The function is exactly the multiplicative function used by Tóth:
\[
\beta(1)=1,\qquad
\beta(p^a)=\frac{p^{a+1}+(-1)^a}{p+1}.
\]
The source also gives
\[
\beta(m)<m\qquad(m>1).
\]
For a squarefree integer \(m\), one has
\[
\beta(m)=\varphi(m).
\]
In particular, for distinct primes \(r,s\),
\[
\beta(rs)=(r-1)(s-1),
\]
while for a prime square,
\[
\beta(r^2)=r^2-r+1.
\]

An integer \(m>1\) with \(\Omega(m)\le2\) is either a prime, a prime square, or a product of two distinct primes. The proof exhausts these forms on two consecutive integers.

## Proof
Suppose
\[
\beta(n)=\beta(n+1)
\tag{1}
\]
and
\[
\Omega(n),\Omega(n+1)\le2.
\]

The case \(n=1\) works because
\[
\beta(1)=\beta(2)=1.
\]
Assume henceforth that \(n>1\).

If \(n+1\) is prime, then
\[
\beta(n+1)=n.
\]
But \(\beta(n)<n\) for every \(n>1\), contradicting (1). Thus \(n+1\) is not prime.

If \(n\) is prime, then \(n=2\) gives
\[
\beta(2)=1\ne2=\beta(3).
\]
For odd prime \(n\), the even integer \(n+1\) has at most two prime factors counted with multiplicity. Hence either \(n+1=4\), giving \(n=3\) and
\[
\beta(3)=2\ne3=\beta(4),
\]
or
\[
n+1=2q
\]
for an odd prime \(q\). Then
\[
n=2q-1,
\qquad
\beta(n)=n-1=2q-2,
\qquad
\beta(n+1)=\beta(2)\beta(q)=q-1,
\]
again contradicting (1).

Therefore both \(n\) and \(n+1\) are composite. The even member of the pair is composite and has multiplicity at most two, so it is either \(4\) or \(2q\) with \(q\) an odd prime. The value \(4\) has prime neighbors and has already been excluded. Hence the even member is
\[
2q
\]
with \(q\) odd prime, and
\[
\beta(2q)=q-1.
\tag{2}
\]

The odd neighboring composite has multiplicity exactly two. There are two possibilities.

First suppose it is a prime square:
\[
r^2=2q\pm1.
\]
Equation (1) and (2) give
\[
q-1=r^2-r+1,
\]
so
\[
q=r^2-r+2.
\tag{3}
\]
If \(r^2=2q-1\), substitution of (3) yields
\[
r^2-2r+3=0,
\]
which has no real root. If \(r^2=2q+1\), substitution yields
\[
r^2-2r+5=0,
\]
again impossible.

Now suppose the odd neighbor is a product of distinct odd primes:
\[
rs=2q\pm1,
\qquad r<s.
\]
Equation (1) and (2) give
\[
q-1=(r-1)(s-1),
\]
hence
\[
q=rs-r-s+2.
\tag{4}
\]
If \(rs=2q-1\), then (4) gives
\[
(r-2)(s-2)=1.
\]
Because \(r,s\) are odd primes, this forces
\[
r=s=3,
\]
contrary to distinctness. If \(rs=2q+1\), then (4) gives
\[
(r-2)(s-2)=-1,
\]
impossible because both factors are positive.

All possibilities for \(n>1\) have been eliminated. Thus \(n=1\) is the unique solution with
\[
\Omega(n),\Omega(n+1)\le2.
\]

Finally,
\[
\beta(20)=12=\beta(21),
\]
and
\[
\Omega(20)=3,\qquad \Omega(21)=2.
\]
Hence the lower bound \(3\) on the larger multiplicity is attained.

## Verification
The attached `verify.py` independently checks every
\[
1\le n<2{,}000{,}000
\]
for the conditions
\[
\Omega(n)\le2,\qquad \Omega(n+1)\le2,\qquad \beta(n)=\beta(n+1).
\]
It finds exactly
\[
n=1.
\]

The same verifier checks the sharpness witness
\[
\beta(20)=\beta(21)=12
\]
and verifies the prime-square and squarefree-semiprime formulas used in the symbolic proof across a large exact sample.

The finite computation is corroborative only. The theorem follows from the exhaustive algebraic case split above.

## Relationship to prior work
Tóth's survey introduces this multiplicative \(\beta\), lists
\[
1,20,116,135,171,194,740,\ldots
\]
as initial solutions of
\[
\beta(n)=\beta(n+1),
\]
and poses as Problem 3 whether infinitely many such \(n\) exist. The paper does not give a prime-factor-complexity obstruction for the equation.

OEIS A206368 is the exact sequence of starting values \(n\) for which
\[
\beta(n)=\beta(n+1).
\]
Its first nontrivial term is \(20\), which attains the multiplicity threshold proved here.

A later paper by Tóth on alternating sums of multiplicative functions revisits the same \(\beta\) for summatory identities and reciprocal sums, but its section on \(\beta\) does not treat equality at consecutive arguments.

There is an analogous low-complexity classification for the different equation
\[
\sigma(n)=\sigma(n+1),
\]
but that result does not imply the present theorem because \(\beta\) has different prime-power values. A separate result for Tóth's Problem 4 concerns divisibility of \(\beta(n)\) into \(n-1\); that divisibility condition neither implies nor is implied by equality of consecutive \(\beta\)-values.

## Limitations
The theorem does not decide whether infinitely many solutions of
\[
\beta(n)=\beta(n+1)
\]
exist. It proves only the exact first multiplicity barrier: a nontrivial solution cannot have both consecutive integers be primes or semiprimes in the multiplicity sense.

The originality comparison included the primary full text, the exact OEIS sequence, a later same-author paper on the same function, targeted searches for semiprime and prime-square formulations, and implication comparison with nearby low-complexity divisor-function results. An equivalent elementary argument in an unindexed source remains a residual risk.

## References
1. L. Tóth, “A survey of the alternating sum-of-divisors function,” arXiv:1111.4842v1, first public 21 November 2011; later *Acta Universitatis Sapientiae, Mathematica* 5 (2013), 93–107, DOI 10.2478/ausm-2014-0007.
2. OEIS Foundation, A206368, numbers \(n\) such that \(\beta(n)=\beta(n+1)\).
3. L. Tóth, “Alternating Sums Concerning Multiplicative Arithmetic Functions,” *Journal of Integer Sequences* 20 (2017), Article 17.2.1.
