# Prime squares exhaust the first five multiplicity layers of a prime-power-sum equation
## Finding
For
\[
n=\prod_{p\mid n}p^{a_p},
\]
define
\[
B(n)=\sum_{p\mid n}p^{a_p},\qquad
\beta(n)=\sum_{p\mid n}p,
\]
and let
\[
\Omega(n)=\sum_{p\mid n}a_p.
\]
If
\[
B(n)=\beta(n)^2
\]
and
\[
\Omega(n)\le5,
\]
then
\[
n=p^2
\]
for a prime \(p\).

Equivalently, every solution that is not a prime square satisfies
\[
\Omega(n)\ge6.
\]
This threshold is sharp because
\[
144=2^4\cdot3^2,
\]
for which
\[
B(144)=16+9=25=(2+3)^2=\beta(144)^2
\]
and
\[
\Omega(144)=6.
\]

## Assumptions and scope
The function \(B\) is the sum of the maximal prime powers in the factorization of \(n\), while \(\beta\) is the sum of its distinct prime divisors. The equation
\[
B(n)=\beta(n)^2
\]
was studied by De Koninck and Luca. Their work notes that every prime square is a solution and establishes global counting bounds for the full solution set.

The present statement concerns the exact initial layers measured by the total prime-factor multiplicity \(\Omega\). No claim is made about a complete parametrization of solutions once \(\Omega(n)\ge6\).

## Proof
Suppose
\[
B(n)=\beta(n)^2
\tag{1}
\]
and
\[
\Omega(n)\le5.
\]

If \(n\) has only one distinct prime divisor, say \(n=p^a\), then (1) is
\[
p^a=p^2,
\]
so
\[
a=2.
\]
Thus every one-prime solution is a prime square.

Assume now that \(n\) has at least two distinct prime divisors. If every exponent satisfies
\[
a_p\le2,
\]
then
\[
B(n)=\sum_{p\mid n}p^{a_p}
\le
\sum_{p\mid n}p^2
<
\left(\sum_{p\mid n}p\right)^2
=
\beta(n)^2,
\]
where the inequality is strict because at least two distinct primes occur. Hence some exponent is at least \(3\).

Because \(\Omega(n)\le5\), this leaves at most three distinct prime divisors.

First suppose that exactly three distinct primes occur. The exponent pattern must be
\[
(3,1,1).
\]
Let \(p\) be the prime with exponent \(3\), and let the other primes be \(q,r\). Put
\[
t=q+r.
\]
Equation (1) becomes
\[
p^3+t=(p+t)^2,
\]
so
\[
p^2(p-1)=t(t+2p-1).
\tag{2}
\]
Reducing (2) modulo \(p\) gives
\[
t(t-1)\equiv0\pmod p.
\]

If \(t=kp\), then division of (2) by \(p\) gives
\[
p(p-1)=k\bigl(p(k+2)-1\bigr).
\]
Reduction modulo \(p\) forces \(p\mid k\). Writing \(k=\ell p\) and dividing once more by \(p\) yields
\[
p-1=\ell\bigl(p(\ell p+2)-1\bigr),
\]
whose right-hand side is strictly larger than \(p-1\). This is impossible.

If \(t=kp+1\), then (2) gives
\[
p(p-1)=(kp+1)(k+2).
\]
Reduction modulo \(p\) forces
\[
p\mid k+2.
\]
Write
\[
k+2=\ell p.
\]
Then
\[
p-1=\ell(\ell p^2-2p+1).
\]
For \(p>2\), the right-hand side is at least \((p-1)^2>p-1\). For \(p=2\), equality could occur only at \(\ell=1\), which gives \(k=0\) and hence \(t=1\), impossible because \(t=q+r\ge5\). Thus there is no three-prime solution with \(\Omega(n)\le5\).

It remains to consider exactly two distinct primes. Write
\[
n=p^a q^b,
\qquad p<q.
\]
If \(b\ge3\), then
\[
q^b\ge q^3>(p+q)^2=\beta(n)^2,
\]
so (1) is impossible. Therefore
\[
b\le2,
\]
and the exponent at least \(3\) must be \(a\). Since \(a+b\le5\), the only possibilities are
\[
(a,b)=(3,2),(3,1),(4,1).
\]

For \((a,b)=(3,2)\), equation (1) gives
\[
p^3+q^2=(p+q)^2,
\]
so
\[
p^2=p+2q,
\qquad
q=\frac{p(p-1)}2.
\]
If \(p\) is odd, primality of \(q\) and \(p\mid q\) force \(q=p\), contrary to \(p<q\); for \(p=2\), the formula gives \(q=1\). Hence this case is impossible.

Now let \(b=1\) and \(a\in\{3,4\}\). Equation (1) is
\[
p^a+q=(p+q)^2.
\]
Modulo \(p\), this gives
\[
q(q-1)\equiv0\pmod p.
\]
Since \(p\ne q\), write
\[
q=mp+1
\]
with \(m\ge1\). Substitution and division by \(p\) give
\[
p^{a-1}=p(m+1)^2+m+2.
\]
Reducing modulo \(p\) yields \(p\mid m+2\), so write
\[
m=kp-2.
\]
Then
\[
p^{a-2}=(kp-1)^2+k.
\tag{3}
\]

If \(a=3\), the right-hand side of (3) is greater than \(p\): for \(p\ge3\) it is at least \((p-1)^2+1>p\), while for \(p=2\), the condition \(m\ge1\) forces \(k\ge2\), giving an even larger value. Thus \(a=3\) is impossible.

If \(a=4\) and \(k=1\), then (3) would give
\[
p^2=(p-1)^2+1,
\]
which has no prime solution. If \(k\ge2\), then
\[
(kp-1)^2+k>p^2,
\]
again contradicting (3). Thus \(a=4\) is impossible as well.

All multi-prime possibilities with \(\Omega(n)\le5\) have been excluded. Therefore every such solution is a prime square.

Finally,
\[
144=2^4\cdot3^2
\]
satisfies
\[
B(144)=2^4+3^2=25=(2+3)^2=\beta(144)^2,
\]
so the lower bound \(6\) for non-prime-square solutions is attained.

## Verification
The attached `verify.py` evaluates \(B(n)\), \(\beta(n)\), and \(\Omega(n)\) exactly for every
\[
2\le n\le2{,}000{,}000.
\]
It checks that every solution with \(\Omega(n)\le5\) is a prime square, and that the least total multiplicity among non-prime-square solutions encountered is \(6\), first attained by \(144\).

The verifier also checks the exact witness identity for \(144\). This finite computation is corroborative only; the theorem follows from the unbounded case split above.

## Relationship to prior work
A 2009 paper of Luca and Tipu publicly records that De Koninck and Luca had studied positive integers with at least two distinct prime factors satisfying
\[
B(n)=\beta(n)^2.
\]
The later full paper of De Koninck and Luca defines the same functions, notes that all prime squares belong to the solution set, and proves global upper and lower counting bounds. Its lower-bound construction demonstrates that many non-prime-square solutions exist, but the inspected text does not classify the first layers by \(\Omega(n)\).

The present result is complementary: rather than estimating the total number of solutions, it identifies the exact first multiplicity at which a non-prime-square solution can occur and gives the sharp witness \(144\).

Targeted searches for the equation together with \(\Omega\), “prime square,” the number \(144\), and low-prime-factor aliases did not locate a published statement implying this classification. A dedicated exact sequence for the equation was also not located in the targeted database search; that absence is not used as evidence of novelty.

## Limitations
The theorem does not classify solutions with \(\Omega(n)\ge6\), and it does not assert that \(144\) is the only solution having \(\Omega(n)=6\). It determines only the sharp minimum total prime-factor multiplicity outside the prime-square family.

Because the proof is elementary, an equivalent observation in an unindexed note or problem discussion remains a residual originality risk.

## References
1. F. Luca and V. Tipu, “On Positive Integers \(n\) with a Certain Divisibility Property,” *Journal of Integer Sequences* 12 (2009), Article 09.3.1, published 23 February 2009. The introduction cites the then-forthcoming work on \(B(n)=\beta(n)^2\).
2. J.-M. De Koninck and F. Luca, “On sums of powers of prime factors of an integer,” *Annales Universitatis Scientiarum Budapestinensis, Sectio Computatorica* 32 (2010), 13–21.
