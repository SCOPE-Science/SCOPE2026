# The unique prime-containing Ruth–Aaron pair
## Finding
Let \(S(n)\) denote the sum of the prime factors of \(n\), counted with multiplicity, and put \(S(1)=0\). Suppose
\[
S(n)=S(n+1).
\]
If at least one of \(n\) and \(n+1\) is prime, then
\[
n=5.
\]
Thus the only ordinary multiplicity Ruth–Aaron pair containing a prime is
\[
(5,6).
\]

The key auxiliary statement is itself exact: for composite \(m\),
\[
S(m)=m-1
\quad\Longleftrightarrow\quad
m=6.
\]

## Assumptions and scope
This uses the original multiplicity convention for Ruth–Aaron numbers: repeated prime factors are counted repeatedly in \(S\). This is distinct from the later function \(P(n)\), which sums only distinct prime divisors.

The theorem classifies all Ruth–Aaron pairs having a prime member; there is no bound on the size or factorization complexity of the neighboring integer. It does not classify prime-power members of higher exponent or general low-support composite pairs.

## Proof
First prove the auxiliary lemma. For every integer \(t\ge2\),
\[
S(t)\le t.
\]
Indeed, this is immediate for primes. If \(t=ab\) with \(a,b\ge2\), complete additivity gives
\[
S(t)=S(a)+S(b)\le a+b\le ab=t,
\]
and induction on \(t\) completes the proof.

Now let \(m\) be composite and suppose
\[
S(m)=m-1.
\]
Choose a factorization \(m=ab\) with \(2\le a\le b\). Then
\[
m-1=S(m)=S(a)+S(b)\le a+b.
\]
Hence
\[
ab-a-b\le1,
\]
or equivalently
\[
(a-1)(b-1)\le2.
\]
Because \(2\le a\le b\), the only possibilities are
\[
(a,b)=(2,2)\quad\text{or}\quad(a,b)=(2,3).
\]
For \(m=4\), one has \(S(4)=4\ne3\). For \(m=6\), one has \(S(6)=2+3=5\). Therefore
\[
S(m)=m-1
\]
for composite \(m\) exactly when \(m=6\).

Now suppose \(S(n)=S(n+1)\).

If \(n+1\) is prime, then
\[
S(n+1)=n+1,
\]
whereas \(S(n)\le n\) for \(n\ge2\), and \(S(1)=0\). This is impossible.

If \(n\) is prime, then
\[
S(n)=n.
\]
Consequently
\[
S(n+1)=n=(n+1)-1.
\]
The integer \(n+1\) is composite, so the auxiliary lemma forces \(n+1=6\), hence \(n=5\). Directly,
\[
S(5)=5=S(6),
\]
so \((5,6)\) indeed is a Ruth–Aaron pair.

## Verification
The proof is unrestricted and symbolic. The accompanying checker independently verifies the two sharp finite predicates through two million: among composite \(m\) in the range, \(S(m)=m-1\) occurs only at \(m=6\); and among Ruth–Aaron pairs \((n,n+1)\) in the range, the only pair containing a prime is \((5,6)\). The finite computation corroborates but does not replace the proof.

## Relationship to prior work
Pomerance's 2002 paper studies the original multiplicity Ruth–Aaron equation \(S(n)=S(n+1)\), proves a strong global upper bound for its counting function, and discusses the unresolved infinitude problem. The inspected article does not state a classification of pairs containing a prime.

Iannucci and Mintos distinguish the original multiplicity function \(S\) from the distinct-prime-divisor function \(P\), then study low-component pairs for the latter. Their Theorem 1 classifies the distinct-prime-divisor pairs with component counts \(\{1,2\}\), obtaining \((5,6)\), \((24,25)\), and \((49,50)\). That theorem is about \(P\), not the multiplicity equation treated here, so it does not imply the present classification.

OEIS A039752 records the multiplicity Ruth–Aaron numbers. OEIS A001414 records \(S(n)\) and the standard inequality \(S(n)\le n\), but neither entry states the sharp composite equation \(S(m)=m-1\iff m=6\) or the resulting prime-member classification.

## Limitations
This theorem settles only the prime-member boundary of the ordinary Ruth–Aaron problem. It does not address whether infinitely many Ruth–Aaron pairs exist, nor does it classify pairs whose members are both composite with larger factorization complexity.

The original 1974 note and Drost's 1996 article were identified as historically relevant but were not available as fully searchable text in the inspected sources. The full 2002 and 2005 papers, exact sequence entries, and targeted statement searches found no covering result; nevertheless, a short elementary observation of this kind could exist in poorly indexed recreational-number-theory literature.

## References
1. Carl Pomerance, "Ruth-Aaron numbers revisited", in *Paul Erdős and His Mathematics I*, Bolyai Society Mathematical Studies 11 (2002), 567–579.
2. Douglas E. Iannucci and Enrique R. Mintos, "On Consecutive Integer Pairs With the Same Sum of Distinct Prime Divisors", *INTEGERS* 5 (2005), A12, published 29 June 2005. Subject Classification: 11A25, 11Y55.
3. OEIS Foundation, A039752, Ruth–Aaron numbers under the multiplicity convention.
4. OEIS Foundation, A001414, the sum of prime factors counted with multiplicity.
