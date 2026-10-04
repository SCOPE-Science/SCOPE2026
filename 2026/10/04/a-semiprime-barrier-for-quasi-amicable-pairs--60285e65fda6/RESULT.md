# A semiprime barrier for quasi-amicable pairs
## Finding
Let \(\Omega(t)\) be the number of prime factors of \(t\), counted with
multiplicity. If \(m\ne n\) are a quasi-amicable pair, meaning
\[
\sigma(m)=\sigma(n)=m+n+1,
\]
then
\[
\max\{\Omega(m),\Omega(n)\}\ge 3.
\]
Equivalently, no quasi-amicable pair can have both members with at most two
prime factors counted with multiplicity. In particular, there is no
quasi-amicable pair in which both members are semiprimes.

## Assumptions and scope
For \(t>1\), write
\[
L(t)=\sigma(t)-t-1,
\]
the sum of the nontrivial divisors of \(t\), where both \(1\) and \(t\) are
excluded. Thus \((m,n)\) is quasi-amicable exactly when
\[
L(m)=n,\qquad L(n)=m,
\]
with \(m\ne n\).

A semiprime is an integer with exactly two prime factors counted with
multiplicity, so it is either \(p^2\) or \(pq\) for distinct primes \(p<q\).

## Proof
First, neither member of a quasi-amicable pair is prime. If \(p\) is prime,
then it has no nontrivial divisors and therefore
\[
L(p)=0,
\]
which cannot be the positive other member of a quasi-amicable pair.

Suppose, toward a contradiction, that both members satisfy
\[
\Omega(m)\le2,\qquad \Omega(n)\le2.
\]
Since both are composite, each is a semiprime.

A prime square cannot occur. Indeed, if \(m=p^2\), then the only nontrivial
divisor of \(m\) is \(p\), so
\[
n=L(p^2)=p.
\]
But then \(L(n)=L(p)=0\), contradicting \(L(n)=m>0\).

Hence both members must be products of two distinct primes. Write
\[
m=pq,\qquad n=rs
\]
with \(p<q\) and \(r<s\) prime. The only nontrivial divisors of \(pq\) are
\(p\) and \(q\), and similarly for \(rs\). Therefore
\[
n=p+q,\qquad m=r+s. \tag{1}
\]

For two distinct primes \(u<v\),
\[
uv-u-v=(u-1)(v-1)-1>0.
\]
Thus
\[
m=pq>p+q=n.
\]
Applying the same inequality to \(r<s\) gives
\[
n=rs>r+s=m.
\]
The two strict inequalities contradict each other. Therefore both members
cannot have \(\Omega\)-value at most \(2\), proving
\[
\max\{\Omega(m),\Omega(n)\}\ge3.
\]

## Verification
The proof is unrestricted and elementary. The accompanying checker performs a
finite corroboration through \(2{,}000{,}000\). It computes
\(\Omega(t)\), \(\sigma(t)\), and \(L(t)\) exactly by a smallest-prime-factor
sieve. It then checks every \(t\) in the range with \(\Omega(t)\le2\) and
verifies that no positive mate \(L(t)\) with \(\Omega(L(t))\le2\) satisfies
\(L(L(t))=t\).

The finite sweep is not used to prove the theorem.

## Relationship to prior work
Hagis and Lord proved several low-factor restrictions for quasi-amicable
numbers. Their Proposition 2 says that a relatively prime quasi-amicable pair
has a product with at least four distinct prime factors; this still permits,
at the level of that proposition, two squarefree semiprimes having two distinct
prime factors each. Their Proposition 4 rules out small prime powers as
members: if \(p^a\) belongs to a quasi-amicable pair, then \(p\) is odd and
\(a\) is odd with \(a>3\). Their Corollary 4.1 says that both members cannot
both be prime powers.

The result here closes the full \(\Omega\le2\) boundary, without a coprimality
assumption. The only branch not already eliminated by prime-power restrictions
is the squarefree-semiprime branch, where the identities in (1) give the
immediate two-sided size contradiction.

Pollack later proved that the set of quasi-amicable numbers has asymptotic
density zero. His full paper defines the same object, uses
\(\omega(n)\) in its analytic estimates, and has primary classification
11A25; it does not state a semiprime classification, and an exact-text search
for "semiprime" returns no occurrence.

OEIS A005276 records members of quasi-amicable pairs and the historical
literature. Its table is consistent with the theorem but does not state this
unrestricted multiplicative-complexity barrier.

## Limitations
The theorem does not classify pairs in which one member has three or more
prime factors counted with multiplicity. It also does not address the open
same-parity or infinitude questions.

The earliest historical papers on the object predate the exact-day source used
for date metadata. Hagis and Lord's paper is identified as the April 1977 issue
of *Mathematics of Computation*, but the inspected source gives no exact
public day. Pollack's paper supplies an explicit public date, 21 April 2011.
A short semiprime observation could also occur in an older source not available
as searchable full text; this remains the main originality risk.

## References
1. P. Hagis, Jr. and G. Lord, "Quasi-amicable numbers", *Mathematics of
   Computation* 31 (1977), no. 138, 608--611,
   DOI 10.1090/S0025-5718-1977-0434939-3.
2. P. Pollack, "Quasi-Amicable Numbers are Rare", *Journal of Integer
   Sequences* 14 (2011), Article 11.5.2, published 21 April 2011.
   2010 Mathematics Subject Classification: Primary 11A25; Secondary 11N37.
3. OEIS Foundation, A005276, "Betrothed (or quasi-amicable) numbers".
