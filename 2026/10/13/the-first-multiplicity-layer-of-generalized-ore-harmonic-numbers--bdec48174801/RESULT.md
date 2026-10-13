# The first multiplicity layer of generalized Ore harmonic numbers
## Finding
For an integer
\[
k\ge1,
\]
let
\[
\sigma_k(n)=\sum_{d\mid n}d^k.
\]
Following the generalized Ore definition, call \(n\) \(k\)-harmonic if
\[
\sigma_k(n)\mid n^k\tau(n),
\]
where \(\tau(n)\) is the number of positive divisors.

If
\[
n>1,\qquad \Omega(n)\le2,
\]
then \(n\) is \(k\)-harmonic exactly in the single case
\[
(k,n)=(1,6).
\]

Thus every proper generalized case
\[
k\ge2
\]
satisfies the unconditional multiplicity barrier
\[
\Omega(n)\ge3
\]
for every \(k\)-harmonic integer \(n>1\).

## Assumptions and scope
The function \(\Omega(n)\) counts prime factors with multiplicity. Hence
\[
\Omega(n)\le2
\]
means that \(n>1\) is one of:
a prime \(p\), a prime square \(p^2\), or a squarefree semiprime \(pq\) with distinct primes \(p,q\).

The theorem concerns the complete first two multiplicity layers. It does not assert that proper \(k\)-harmonic numbers exist for any \(k\ge2\); the classical computational evidence reported by Cohen and Deng found none in a large finite range.

## Proof
First let
\[
n=p
\]
be prime and put
\[
x=p^k\ge2.
\]
Then
\[
\frac{n^k\tau(n)}{\sigma_k(n)}
=
\frac{2x}{x+1}.
\]
If this is an integer, then \(x+1\mid2x\). Since
\[
\gcd(x,x+1)=1,
\]
we must have
\[
x+1\mid2,
\]
which is impossible for \(x\ge2\).

Now let
\[
n=p^2
\]
and again put \(x=p^k\). Then
\[
\frac{n^k\tau(n)}{\sigma_k(n)}
=
\frac{3x^2}{x^2+x+1}.
\]
The denominator is coprime to \(x\), hence to \(x^2\). Therefore integrality would force
\[
x^2+x+1\mid3.
\]
But
\[
x^2+x+1\ge7,
\]
so no prime square is \(k\)-harmonic.

It remains to consider
\[
n=pq
\]
with distinct primes. Put
\[
x=p^k,\qquad y=q^k.
\]
Then
\[
H=
\frac{n^k\tau(n)}{\sigma_k(n)}
=
\frac{4xy}{(x+1)(y+1)}.
\]
Since \(x,y\ge2\),
\[
4xy>(x+1)(y+1),
\]
while clearly
\[
H<4.
\]
Thus if \(H\) is an integer, then
\[
H\in\{2,3\}.
\]

If \(H=2\), then
\[
2xy=(x+1)(y+1),
\]
which rearranges to
\[
(x-1)(y-1)=2.
\]
Hence
\[
\{x,y\}=\{2,3\}.
\]
Because \(x\) and \(y\) are prime \(k\)-th powers with the same exponent \(k\), this forces
\[
k=1,\qquad \{p,q\}=\{2,3\}.
\]
Thus \(n=6\), and indeed
\[
\sigma(6)=12\mid24=6\tau(6).
\]

If \(H=3\), then
\[
4xy=3(x+1)(y+1),
\]
or
\[
(x-3)(y-3)=12.
\]
Positive factor pairs of \(12\) give, up to order,
\[
(x,y)\in\{(4,15),(5,9),(6,7)\}.
\]
No pair consists of two prime \(k\)-th powers with the same positive exponent. Therefore this branch yields no solution.

The three possible factorization types are exhausted, proving the theorem.

## Verification
The accompanying checker independently tests every
\[
1\le k\le10
\]
and every
\[
2\le n\le50000
\]
with \(\Omega(n)\le2\), computing \(\sigma_k(n)\), \(\tau(n)\), and the divisibility condition exactly by integer arithmetic.

It finds only
\[
(k,n)=(1,6).
\]

The checker also verifies the three algebraic branches directly. This finite replay is corroborative only; the unrestricted result follows from the symbolic proof above.

## Relationship to prior work
Cohen and Deng introduced this generalized \(k\)-harmonic condition in 1998. A later primary paper by Sándor reproduces the definition and reports their result that for
\[
k>1
\]
no \(k\)-harmonic number occurs in the finite range
\[
1<n\le10^{10}.
\]
That finite computation does not imply an unrestricted lower bound on \(\Omega(n)\).

A published result on proper power-harmonic numbers proves a stronger support obstruction for even integers with exactly two distinct prime factors: for \(k\ge2\), no number \(2^a p^b\) is \(k\)-harmonic. The present statement is different in scope. It closes the complete multiplicity layer \(\Omega\le2\), including odd squarefree semiprimes and prime powers, and identifies the single ordinary-harmonic exception \(6\).

For \(k=1\), the classical Ore harmonic numbers are tabulated in OEIS A001599. The value \(6\) is the only term with \(\Omega\le2\), in agreement with the theorem.

## Limitations
The theorem gives only a lower bound
\[
\Omega(n)\ge3
\]
for hypothetical proper \(k\)-harmonic numbers. It does not settle their existence, nor does it classify the \(\Omega=3\) layer.

The original Cohen--Deng article was identified bibliographically but its full text was not available through the inspected open routes. The later full primary source confirms the definition and the finite \(10^{10}\) result. Because the original article is directly on the same object, possible prior appearance of this low-\(\Omega\) observation remains an explicit originality risk.

The exact structured source date uses the earliest day-resolved public source inspected here. The 1998 article is earlier historically, but the accessible records used in this review provide only year and issue, not a verified calendar day.

## References
1. G. L. Cohen and M. Deng, “On a generalization of Ore's harmonic numbers,” *Nieuw Archief voor Wiskunde* 16(3) (1998), 161–172.
2. J. Sándor, “On bi-unitary harmonic numbers,” arXiv:1105.0294v1, submitted 2 May 2011.
3. OEIS Foundation, A001599, “Harmonic or Ore numbers.”
