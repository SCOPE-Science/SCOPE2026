# Exact zero and one fibers of the divisor-sum divisibility defect
## Finding
For any integer \(n\ge1\), let
\[
B(n)=\#\{d\mid n:\sigma(d)\nmid\sigma(n)\},
\]
where \(\sigma\) denotes the ordinary sum-of-divisors function. Let \(\tau\) denote the divisor-counting function.

**Structural lower bound.** For every factorization
\[
n=\prod_{i=1}^{r}p_i^{a_i},
\]
we have
\[
B(n)\ge\sum_{i=1}^{r}\bigl(a_i+1-\tau(a_i+1)\bigr).
\tag{1}
\]
The lower bound is exact for prime powers.

**Complete first two fibers.** The zero fiber consists of all squarefree positive integers, including \(1\). The one fiber consists exactly of
\[
n=p^2m\quad\text{or}\quad n=p^3m,
\tag{2}
\]
where \(p\) is prime, \(m\ge1\) is squarefree, \(\gcd(p,m)=1\), and every prime \(q\mid m\) satisfies respectively
\[
q\equiv-1\pmod{p+1},\qquad
q\equiv-1\pmod{p^2+p+1}.
\tag{3}
\]
The congruence condition is vacuous for \(m=1\). In every one-defect case, the unique divisor whose divisor sum fails to divide \(\sigma(n)\) is
\[
d=n/p.
\]
The one fiber is infinite but has natural density zero.

Examples include
\[
B(4)=B(8)=B(20)=B(63)=B(104)=1,
\]
whereas
\[
B(12)=2.
\]

## Assumptions and scope
All prime powers and divisors are positive integers. The function \(\sigma(n)=\sum_{d\mid n}d\) is multiplicative for coprime inputs, and
\[
\sigma(p^a)=1+p+\cdots+p^a=\frac{p^{a+1}-1}{p-1}.
\tag{4}
\]
Squarefree means no prime square divides the integer. The convention \(1\) is squarefree is used. The natural density of a set \(S\subseteq\mathbb N\) is the limit, if it exists, of \(\#(S\cap[1,X])/X\) as \(X\to\infty\).

The theorem classifies the two smallest fibers of the exact sequence OEIS A173440. It makes no claim about complete higher fibers.

## Proof
**1. Divisibility between prime-power divisor sums.** For every prime \(p\) and integers \(0\le j\le a\),
\[
\sigma(p^j)\mid\sigma(p^a)
\quad\Longleftrightarrow\quad
j+1\mid a+1.
\tag{5}
\]
Indeed, by (4), this is equivalent to the divisibility of \(p^{a+1}-1\) by \(p^{j+1}-1\). The standard Euclidean identity
\[
\gcd(p^u-1,p^v-1)=p^{\gcd(u,v)}-1
\]
then gives (5), including \(j=0\).

**2. A general lower bound.** Fix a prime-power block \(p_i^{a_i}\) of \(n\). For every \(j\) with \(0\le j<a_i\) and \(j+1\nmid a_i+1\), the divisor
\[
d_{i,j}=p_i^j\frac{n}{p_i^{a_i}}
\]
is a violating divisor: multiplicativity and cancellation show that \(\sigma(d_{i,j})\mid\sigma(n)\) would imply \(\sigma(p_i^j)\mid\sigma(p_i^{a_i})\), contradicting (5). There are exactly
\[
a_i+1-\tau(a_i+1)
\]
such indices, since the indices that do divide correspond bijectively to divisors of \(a_i+1\). Divisors arising from different blocks are distinct because their prime-power exponent vectors differ. Summing proves (1). For \(n=p^a\), these are all the violating divisors, so equality holds.

If \(a\ge4\), then \(a+1-\tau(a+1)\ge2\): this follows from \(\tau(k)\le k-2\) for \(k\ge5\), which holds by counting proper divisors at most \(k/2\) (with \(k=5\) immediate). For \(a=2\) or \(a=3\), the corresponding contribution is exactly \(1\). For \(a=1\), it is \(0\).

Consequently, if \(B(n)=0\) then every exponent equals \(1\), so \(n\) is squarefree. Conversely, if \(n\) is squarefree, each divisor is a product of a subset of its prime factors; its divisor sum is a subproduct of \(\sigma(n)=\prod_{p\mid n}(p+1)\), and so \(B(n)=0\). This also covers \(n=1\).

**3. Reduction of the one fiber.** If \(B(n)=1\), inequality (1) implies that exactly one prime, call it \(p\), has exponent \(a=2\) or \(3\), with all other primes having exponent \(1\). Thus
\[
n=p^a m,\qquad a\in\{2,3\},\qquad \gcd(p,m)=1,
\]
with \(m\) squarefree. All divisors have the shape
\[
d=p^j e,\qquad 0\le j\le a,\ e\mid m.
\]
For \(a=2\), the only potentially violating exponent is \(j=1\); for \(a=3\), it is \(j=2\), because \(\sigma(p)\mid\sigma(p^3)\). In both cases set
\[
M=\sigma(p^{a-1}),
\]
so \(M=p+1\) when \(a=2\), and \(M=p^2+p+1\) when \(a=3\). As
\[
\gcd\bigl(\sigma(p^{a-1}),\sigma(p^a)\bigr)
=\gcd\bigl(\sigma(p^{a-1}),p^a\bigr)=1,
\tag{6}
\]
we have, for \(e\mid m\),
\[
\begin{aligned}
\sigma(p^{a-1}e)\mid\sigma(p^am)
&\Longleftrightarrow M\mid\sigma(p^a)\sigma(m/e)\\
&\Longleftrightarrow M\mid\sigma(m/e).
\end{aligned}
\tag{7}
\]
The factor \(\sigma(e)\) is canceled in the first equivalence by multiplicativity and the squarefreeness of \(m\). Formula (7) is an exact criterion for every potential violating divisor.

For \(e=m\), we have \(m/e=1\), so (7) always fails because \(M>1\); the divisor \(p^{a-1}m=n/p\) is necessarily violating. If \(m>1\), take \(e=m/q\) for each prime \(q\mid m\). Absence of any additional violating divisor forces
\[
M\mid\sigma(q)=q+1.
\tag{8}
\]
Conversely, if (8) holds for every prime \(q\mid m\), then every nonempty product \(\sigma(m/e)=\prod_{q\mid m/e}(q+1)\) is divisible by \(M\). Hence (7) fails only at \(e=m\), so the unique violating divisor is \(n/p\). This proves the if-and-only-if conditions (2)–(3).

**4. Infinitude and density.** For any fixed prime \(p\), each modulus
\[
M=p+1\quad\text{or}\quad M=p^2+p+1
\]
is at least \(3\). Dirichlet's theorem supplies infinitely many primes \(q\equiv-1\pmod M\). Taking \(m=q\) in (2) gives infinitely many distinct one-defect integers.

For fixed \(p\) and fixed exponent \(a\in\{2,3\}\), every admissible squarefree cofactor \(m\) has no prime divisor congruent to \(1\pmod M\), since \(1\not\equiv-1\pmod M\). The sum of reciprocals of primes \(q\equiv1\pmod M\) diverges (the classical reciprocal-prime theorem for reduced residue classes). For any finite collection \(\mathcal Q\) of those primes, the density of integers avoiding all primes in \(\mathcal Q\) is exactly
\[
\prod_{q\in\mathcal Q}\left(1-\frac1q\right).
\]
This tends to zero as the collection expands, so the fixed-\(p\), fixed-\(a\) family has density zero.

Finally, a one-defect integer with repeated prime \(p>P\) is divisible by \(p^2\), and the upper density of the union of such possibilities is at most
\[
\sum_{p>P}\frac1{p^2}\le\sum_{k>P}\frac1{k^2}\longrightarrow0.
\]
The union of the finitely many fixed-\(p\) families with \(p\le P\) has density zero; letting \(P\to\infty\) proves that the entire one fiber has natural density zero.

## Verification
The attached `verify.py` uses only the Python standard library. It computes \(\sigma(n)\) by an exact divisor sieve, enumerates every divisor of every integer
\[
1\le n\le1{,}000{,}000,
\]
and directly evaluates \(B(n)\). Independently, it checks the theorem's predicted fiber class using the prime factorization of \(n\), tests the general lower bound, and confirms that the one-defect cases have exactly the unique bad divisor \(n/p\). Prime-power divisibility (5) is also exhaustively tested over a separate finite parameter grid.

Finite verification is corroborative only; the proof is unrestricted and does not infer density or infinitude from computations.

## Relationship to prior work
OEIS A173440, authored 18 February 2010, defines exactly this function and records that \(B(n)=0\) for squarefree inputs. Its companion A173439 counts divisors whose divisor sums *do* divide \(\sigma(n)\), giving the complementary relation
\[
B(n)=\tau(n)-\mathrm{A173439}(n).
\]
The exact A173440 entry and its accompanying table through \(16384\) contain neither the converse zero-fiber theorem, the complete one-fiber congruence families, nor the sharp blockwise lower bound (1). The table alone cannot establish the infinite classification.

Amdeberhan, Moll, Sharma, and Villamizar give comprehensive formulas for prime-adic valuations of \(\sigma(n)\), and their full open-access article has primary MSC \(11A25\). Those valuation formulas address the prime factors of a *single* divisor sum, not the simultaneous divisibility of \(\sigma(d)\) into \(\sigma(n)\) for all divisors \(d\mid n\). In particular, the inspected article does not state the first two fibers of A173440 or imply the complete one-defect criterion.

Searches with the exact database identifier and direct divisor-sum divisibility formulations found no equivalent or stronger global classification. The main original contribution is the one-defect fiber and its structural and density consequences, not the already-recorded squarefree sufficient condition.

## Limitations
The theorem does not determine \(B^{-1}(k)\) for \(k\ge2\), nor does it give an asymptotic counting formula for the one fiber beyond natural density zero. The analytic density corollary uses classical Dirichlet and reciprocal-prime theorems in arithmetic progressions. An equivalent elementary classification might exist in unindexed commentary not located by the searches.

## References
1. OEIS Foundation, A173440, number of divisors \(d\) of \(n\) such that \(\sigma(d)\) does not divide \(\sigma(n)\), original entry by Jaroslav Krizek, 18 February 2010.
2. OEIS Foundation, A173439, number of divisors \(d\) of \(n\) such that \(\sigma(d)\) divides \(\sigma(n)\), original entry by Jaroslav Krizek, 18 February 2010.
3. T. Amdeberhan, V. H. Moll, V. Sharma, and D. Villamizar, "Arithmetic properties of the sum of divisors," arXiv:2007.03088v1, 6 July 2020, primary MSC \(11A25\).
4. Classical Dirichlet theorem and reciprocal-prime divergence for reduced residue classes; see standard treatments of primes in arithmetic progressions.
