# Squarefree three-prime numbers divisible by their prime-factor sum
## Finding
Define
\[
\beta(n)=\sum_{p\mid n}p,
\]
the sum of the distinct prime divisors of \(n\). Let
\[
n=pqr
\]
with distinct primes
\[
p<q<r.
\]
Then
\[
\beta(n)\mid n
\]
if and only if exactly one of the following two alternatives holds:
\[
p=2,\qquad r=q+2,
\tag{A}
\]
or
\[
p\ge3,\qquad r=pq-p-q>q,
\tag{B}
\]
where the displayed value of \(r\) is prime.

In branch (A),
\[
\beta(n)=2r.
\]
In branch (B),
\[
\beta(n)=pq.
\]
Hence the complete squarefree three-prime layer splits into a twin-prime branch and a shifted-product prime branch.

For example, branch (A) begins with
\[
30=2\cdot3\cdot5,\qquad
70=2\cdot5\cdot7,\qquad
286=2\cdot11\cdot13,
\]
while branch (B) begins with
\[
105=3\cdot5\cdot7,\qquad
231=3\cdot7\cdot11,\qquad
805=5\cdot7\cdot23.
\]

## Assumptions and scope
Only squarefree integers having exactly three distinct prime factors are considered. The function \(\beta\) is the arithmetic function studied by De Koninck and Luca in their work on integers divisible by the sum of their prime factors.

The theorem does not classify nonsquarefree integers, integers with four or more distinct prime factors, or the global counting function of all integers satisfying
\[
\beta(n)\mid n.
\]

## Proof
Let
\[
S=p+q+r=\beta(pqr).
\]
Assume first that
\[
S\mid pqr.
\tag{1}
\]

Because
\[
S>r
\]
and
\[
S=p+q+r<3r\le qr
\]
(the last inequality uses \(q\ge3\)), the divisor \(S\) of the squarefree integer \(pqr\) lies strictly between \(r\) and \(qr\).

The divisors of \(pqr\) are
\[
1,\ p,\ q,\ r,\ pq,\ pr,\ qr,\ pqr.
\]
Therefore (1) forces
\[
S=pq
\qquad\text{or}\qquad
S=pr.
\tag{2}
\]

Suppose first that
\[
S=pr.
\]
Then
\[
p+q+r=pr,
\]
so
\[
q=(p-1)r-p.
\tag{3}
\]
If \(p\ge3\), then
\[
q-r=(p-2)r-p>0,
\]
since \(r>p\). This contradicts \(q<r\). Thus
\[
p=2.
\]
Equation (3) becomes
\[
q=r-2,
\]
or equivalently
\[
r=q+2.
\]
This is branch (A).

Now suppose
\[
S=pq.
\]
Then
\[
p+q+r=pq,
\]
hence
\[
r=pq-p-q.
\tag{4}
\]
Since \(r\) is already assumed to be the largest prime, (4) necessarily satisfies
\[
r>q.
\]
This is branch (B). Notice that \(p=2\) cannot occur here, because then (4) would give
\[
r=q-2<q.
\]

Conversely, if branch (A) holds, then
\[
\beta(2qr)=2+q+r=2r,
\]
and therefore
\[
\beta(2qr)\mid2qr.
\]
If branch (B) holds, then
\[
\beta(pqr)=p+q+r=pq,
\]
and therefore
\[
\beta(pqr)\mid pqr.
\]
This proves both necessity and sufficiency.

## Verification
The attached `verify.py` uses exact integer arithmetic. It enumerates every squarefree integer
\[
n\le2{,}000{,}000
\]
having exactly three distinct prime factors, checks the divisibility condition directly, and independently checks the two symbolic branches above.

Every direct hit agrees with the theorem, and every parameter instance of either branch within the cutoff is a direct hit.

The computation is corroborative only. The unbounded theorem follows from the divisor interval
\[
r<S<qr
\]
and the exhaustive divisor split in the proof.

## Relationship to prior work
De Koninck and Luca introduced the counting problem for integers divisible by
\[
\beta(n)=\sum_{p\mid n}p
\]
and proved global upper and lower bounds for its counting function. Their paper studies the density-scale problem rather than an exact classification by number of prime factors.

OEIS A158804 is the database sequence of composite integers divisible by the sum of their distinct prime factors. It contains the small examples appearing above, but a list of examples does not imply an exhaustive characterization of the whole squarefree three-prime layer.

A later paper by De Koninck and Luca proves that for each fixed \(k\) there are infinitely many integers simultaneously divisible by the sums of the first \(k\) powers of their prime factors. That construction is substantially broader in a different direction and does not determine which squarefree three-prime integers satisfy the first-power condition.

Targeted searches for the exact three-prime condition, the two formulas in branches (A) and (B), the twin-prime reformulation, and the database identifier found no published theorem that contains this classification.

## Limitations
The theorem gives no conclusion about whether either parametrized branch contains infinitely many members. Branch (A) is infinite exactly if there are infinitely many twin primes. Branch (B) asks for prime pairs \(p<q\) for which
\[
pq-p-q
\]
is prime and larger than \(q\); no infinitude claim is made.

The principal originality risk is that this short divisor argument may have appeared in an unindexed elementary note or problem discussion. The inspected primary paper, its later sequel, the exact database entry, and targeted statement-level searches did not reveal such a result.

## References
1. J.-M. De Koninck and F. Luca, “Integers Divisible by the Sum of their Prime Factors,” *Mathematika* 52 (2005), 69–77, DOI 10.1112/S0025579300000346; first published 1 December 2005.
2. OEIS Foundation, A158804, composite integers that are a multiple of the sum of their distinct prime factors.
3. J.-M. De Koninck and F. Luca, “Integers divisible by sums of powers of their prime factors,” *Journal of Number Theory* 128 (2008), 557–563, DOI 10.1016/j.jnt.2007.01.010.
