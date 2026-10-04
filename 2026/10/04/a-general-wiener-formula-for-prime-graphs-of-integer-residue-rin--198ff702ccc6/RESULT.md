# A general Wiener formula for prime graphs of integer residue rings

## Finding

Let 
\[
n=\prod_{i=1}^r p_i^{a_i}\ge 2
\]
be the prime factorization of \(n\), and let \(PG(\mathbb Z_n)\) denote the prime graph of the ring \(\mathbb Z_n\): its vertices are the residue classes modulo \(n\), and distinct vertices \(x,y\) are adjacent exactly when \(xy=0\) in \(\mathbb Z_n\).

Define
\[
T(n)=\prod_{i=1}^r p_i^{a_i-1}\bigl((a_i+1)p_i-a_i\bigr)
\]
and
\[
S(n)=\prod_{i=1}^r p_i^{\lfloor a_i/2\rfloor}.
\]
Then
\[
|E(PG(\mathbb Z_n))|=\frac{T(n)-S(n)}2.
\]
Since the zero vertex is adjacent to every other vertex, every nonadjacent pair is at distance two. Hence the complete distance distribution is
\[
d_1=\frac{T(n)-S(n)}2,
\qquad
 d_2=\binom n2-\frac{T(n)-S(n)}2.
\]
With the convention that the coefficient of \(x^0\) is the number of vertices, the Hosoya polynomial is
\[
H(PG(\mathbb Z_n);x)
=n+\frac{T(n)-S(n)}2x+
\left(\binom n2-\frac{T(n)-S(n)}2\right)x^2,
\]
and the Wiener index is
\[
W(PG(\mathbb Z_n))
=n(n-1)-\frac{T(n)-S(n)}2.
\]

This single formula applies to every positive integer \(n\ge2\). In particular, it simultaneously resolves the four infinite families explicitly left open in the 2024 paper of Hidayat, Krisnawati, Khuluq, Fatimah, and Musyarrofah: higher prime powers, \(p^kq\), \(p^kq^h\), and square-free products of arbitrarily many distinct primes.

## Assumptions and scope

The graph is the ring prime graph used by Bhavanari and subsequent authors, not the Gruenberg--Kegel prime graph of a finite group. The ring is the finite commutative unital ring \(\mathbb Z_n\). Distinct vertices are adjacent exactly when their product is zero modulo \(n\).

The theorem does not claim a closed product formula for arbitrary finite commutative rings, although the proof first gives the general counting identity
\[
|E(PG(R))|=\frac12\left(\sum_{x\in R}|\operatorname{ann}(x)|-|\{x\in R:x^2=0\}|\right)
\]
for every finite commutative ring \(R\) with identity.

## Proof

For a commutative ring with identity, the defining condition \(xRy=0\) is equivalent to \(xy=0\), because taking the middle factor equal to \(1\) gives one implication and commutativity gives the other. Thus in \(\mathbb Z_n\), distinct vertices \(x,y\) are adjacent precisely when
\[
xy\equiv0\pmod n.
\]
The residue class \(0\) is adjacent to every other vertex, so any two distinct nonadjacent vertices have distance exactly two. Therefore, once the number of edges is known, both the Hosoya polynomial and the Wiener index follow immediately.

Let
\[
T(n)=|\{(x,y)\in\mathbb Z_n^2:xy\equiv0\pmod n\}|.
\]
For a fixed residue class \(x\), the congruence \(xy\equiv0\pmod n\) has exactly \(\gcd(x,n)\) solutions \(y\) modulo \(n\). Indeed, if \(g=\gcd(x,n)\), then the congruence is equivalent to \(n/g\mid y\), giving exactly \(g\) residue classes. Hence
\[
T(n)=\sum_{x\bmod n}\gcd(x,n).
\]
Grouping residues by \(d=\gcd(x,n)\), and using that there are \(\varphi(n/d)\) residues with gcd equal to \(d\), gives
\[
T(n)=\sum_{d\mid n}d\,\varphi(n/d)
=n\sum_{e\mid n}\frac{\varphi(e)}e.
\]
The divisor sum is multiplicative. For a prime power \(p^a\),
\[
\sum_{j=0}^a\frac{\varphi(p^j)}{p^j}
=1+a\left(1-\frac1p\right),
\]
so
\[
T(n)=\prod_{p^a\parallel n}p^{a-1}\bigl((a+1)p-a\bigr).
\]

The ordered count \(T(n)\) includes diagonal pairs \((x,x)\), whereas a simple graph has no loops. Let
\[
S(n)=|\{x\bmod n:x^2\equiv0\pmod n\}|.
\]
By the Chinese remainder theorem this count is multiplicative. Modulo \(p^a\), the condition \(p^a\mid x^2\) is equivalent to \(p^{\lceil a/2\rceil}\mid x\), and there are exactly \(p^{\lfloor a/2\rfloor}\) such residues. Therefore
\[
S(n)=\prod_{p^a\parallel n}p^{\lfloor a/2\rfloor}.
\]

After deleting the \(S(n)\) diagonal solutions, every unordered edge contributes exactly two ordered pairs. Consequently
\[
|E(PG(\mathbb Z_n))|=\frac{T(n)-S(n)}2.
\]
Since every distinct pair is at distance one or two,
\[
W(PG(\mathbb Z_n))
=|E|+2\left(\binom n2-|E|\right)
=n(n-1)-|E|,
\]
which yields the displayed formula. The Hosoya polynomial follows from the same two distance counts.

## Verification

The included checker independently factors every integer \(2\le n\le300\), computes \(T(n)\) and \(S(n)\) from the product formulas, constructs the prime graph directly from modular multiplication, and compares the exact edge count and Wiener index. It also checks the six special families treated explicitly in the 2024 paper on many prime choices. The replay returns `VERIFY_OK`.

The finite replay is only a consistency check; the universal proof is the divisor-counting argument above.

## Relationship to prior work

The 2022 survey on Wiener indices of graphs over rings recorded only special prime-graph cases and posed further prime-graph Wiener problems. Hidayat, Krisnawati, Khuluq, Fatimah, and Musyarrofah then revisited the subject in 2024. They corrected earlier formulas for \(p^2\) and \(p^3\), derived formulas for \(pq\), \(p^2q\), \(p^2q^2\), and \(pqr\), and ended by explicitly asking for four broader families: \(p^k\) with \(k>3\), \(p^kq\) with \(k>2\), \(p^kq^h\) with \(k,h>2\), and square-free products of arbitrarily many distinct primes.

The formula proved here covers every \(n\), so it contains every one of those special cases and answers all four stated open families at once. It also explains why a case-by-case distance-matrix partition is unnecessary: the prime graph always has diameter at most two, and the sole nontrivial count is the number of zero-product pairs.

A 2025 paper on prime graphs of polynomial and power-series rings studies diameter, girth, and a modified vertex set of strong zero divisors; it does not provide a Wiener formula for \(PG(\mathbb Z_n)\).

## Limitations

The novelty check found no published all-\(n\) Wiener formula for this ring prime graph through the sources and searches inspected. The main residual bibliographic risk is that the same edge count could have been stated under another name such as a zero-product graph, without explicit use of the prime-graph terminology.

The formula is specific to \(\mathbb Z_n\). For a general finite commutative ring, the annihilator-sum identity above remains valid, but evaluating it may require additional ring-structure information.

## References

1. N. Hidayat, V. H. Krisnawati, M. H. Khuluq, F. M. Fatimah, and A. F. Musyarrofah, “The Wiener Index of Prime Graph \(PG(\mathbb Z_n)\),” *European Journal of Pure and Applied Mathematics* 17(3) (2024), 1659–1673, DOI 10.29020/nybg.ejpam.v17i3.5166.
2. T. Asir, V. Rabikka, A. M. Anto, and N. Shunmugapriya, “Wiener index of graphs over rings: a survey,” *AKCE International Journal of Graphs and Combinatorics* 19(3) (2022), 316–324, DOI 10.1080/09728600.2022.2140088.
3. K. Patra and S. Kalita, “Prime Graph of the Commutative Ring \(\mathbb Z_n\),” *MATEMATIKA* 30 (2014), 59–67, DOI 10.11113/matematika.v30.n.663.
4. W. M. Alqarafi, W. M. Fakieh, and A. A. Altassan, “Prime Graphs of Polynomials and Power Series Over Noncommutative Rings,” *International Journal of Mathematics and Mathematical Sciences* (2025), DOI 10.1155/ijmm/5232935.
