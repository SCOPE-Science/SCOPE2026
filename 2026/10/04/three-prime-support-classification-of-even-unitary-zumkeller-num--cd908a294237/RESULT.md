# Three-prime-support classification of even unitary Zumkeller numbers

## Finding
A positive integer is *unitary Zumkeller* if its positive unitary divisors can be partitioned into two subsets of equal sum. It is *unitary half-Zumkeller* if its proper positive unitary divisors can be partitioned into two nonempty subsets of equal sum.

Let \(n\) be even and have exactly three distinct prime factors. Then \(n\) is unitary Zumkeller if and only if
\[
n=6q^c
\]
for some prime \(q>3\) and integer \(c\ge1\), or
\[
n\in\{60,70,90\}.
\]

Every number in this classification is also unitary half-Zumkeller. Therefore Das's Conjecture 3.1 holds for all even unitary Zumkeller numbers with exactly three distinct prime factors.

## Assumptions and scope
Write
\[
n=2^\alpha p^\beta q^\gamma,
\qquad
3\le p<q,
\qquad
\alpha,\beta,\gamma\ge1,
\]
with \(p,q\) odd primes. Put
\[
A=2^\alpha,\qquad B=p^\beta,\qquad C=q^\gamma.
\]

For a prime-power factorization, the unitary divisor sum is
\[
\sigma^\ast(n)=(A+1)(B+1)(C+1).
\]
Das proves that every unitary Zumkeller number satisfies
\[
\sigma^\ast(n)\ge2n.
\]
Hence any number under consideration must satisfy
\[
\left(1+\frac1A\right)
\left(1+\frac1B\right)
\left(1+\frac1C\right)\ge2.
\]

The classification below uses this necessary inequality to leave only four shapes and then gives explicit equal-sum partitions for all of them. No sufficiency is inferred from abundance alone.

## Proof
Suppose first that \(p\ge7\). Then \(q\ge11\), and monotonicity of
\[
x\longmapsto1+\frac1x
\]
gives
\[
\frac{\sigma^\ast(n)}n
\le
\frac32\cdot\frac87\cdot\frac{12}{11}
=
\frac{144}{77}
<2,
\]
contrary to the necessary condition. Therefore
\[
p\in\{3,5\}.
\]

Assume \(p=5\). If \(q\ge11\), then
\[
\frac{\sigma^\ast(n)}n
\le
\frac32\cdot\frac65\cdot\frac{12}{11}
=
\frac{108}{55}
<2.
\]
Thus \(q=7\). If \(\alpha\ge2\), then
\[
\frac{\sigma^\ast(n)}n
\le
\frac54\cdot\frac65\cdot\frac87
=
\frac{12}{7}
<2.
\]
If \(\beta\ge2\), then
\[
\frac{\sigma^\ast(n)}n
\le
\frac32\cdot\frac{26}{25}\cdot\frac87
=
\frac{312}{175}
<2.
\]
If \(\gamma\ge2\), then
\[
\frac{\sigma^\ast(n)}n
\le
\frac32\cdot\frac65\cdot\frac{50}{49}
=
\frac{90}{49}
<2.
\]
Hence
\[
\alpha=\beta=\gamma=1,
\]
so
\[
n=70.
\]

Now assume \(p=3\). If both \(\alpha\ge2\) and \(\beta\ge2\), then \(q\ge5\) gives
\[
\frac{\sigma^\ast(n)}n
\le
\frac54\cdot\frac{10}{9}\cdot\frac65
=
\frac53
<2.
\]
Thus either \(\alpha=1\) or \(\beta=1\).

First suppose \(\beta=1\) and \(\alpha\ge2\). If \(\alpha\ge3\), then
\[
\frac{\sigma^\ast(n)}n
\le
\frac98\cdot\frac43\cdot\frac65
=
\frac95
<2.
\]
Therefore \(\alpha=2\). The necessary inequality becomes
\[
\frac54\cdot\frac43\left(1+\frac1C\right)\ge2,
\]
so
\[
C\le5.
\]
Since \(C=q^\gamma\) with \(q\ge5\), one must have
\[
C=5.
\]
Thus
\[
n=60.
\]

It remains to take \(\alpha=1\). If \(\beta\ge3\), then
\[
\frac{\sigma^\ast(n)}n
\le
\frac32\cdot\frac{28}{27}\cdot\frac65
=
\frac{28}{15}
<2.
\]
Hence \(\beta\in\{1,2\}\).

If \(\beta=1\), there is no further restriction from the necessary inequality, and the shape is
\[
n=6q^\gamma
\]
with \(q>3\).

If \(\beta=2\), then
\[
\frac32\cdot\frac{10}{9}
\left(1+\frac1C\right)\ge2,
\]
which again gives
\[
C\le5.
\]
Hence
\[
C=5
\]
and
\[
n=90.
\]

This proves that every even three-prime-support unitary Zumkeller number must belong to the stated list. It remains to prove that every listed shape really is unitary Zumkeller and unitary half-Zumkeller.

Let
\[
Q=q^c.
\]
The unitary divisors of
\[
6Q
\]
are
\[
1,2,3,6,Q,2Q,3Q,6Q.
\]
The partition
\[
\{6,6Q\}
\quad\text{and}\quad
\{1,2,3,Q,2Q,3Q\}
\]
has equal sum
\[
6+6Q.
\]
Thus every \(6q^c\) is unitary Zumkeller. Removing \(6Q\), the proper unitary divisors have the equal-sum partition
\[
\{6,3Q\}
\quad\text{and}\quad
\{1,2,3,Q,2Q\},
\]
both with sum
\[
6+3Q.
\]
Hence every \(6q^c\) is unitary half-Zumkeller.

For the three exceptional numbers, explicit unitary Zumkeller partitions are
\[
\begin{aligned}
60:&\quad \{60\}\ \big|\ \{1,3,4,5,12,15,20\},\\
70:&\quad \{2,70\}\ \big|\ \{1,5,7,10,14,35\},\\
90:&\quad \{90\}\ \big|\ \{1,2,5,9,10,18,45\}.
\end{aligned}
\]
Their unitary half-Zumkeller partitions are
\[
\begin{aligned}
60:&\quad \{1,4,5,20\}\ \big|\ \{3,12,15\},\\
70:&\quad \{2,35\}\ \big|\ \{1,5,7,10,14\},\\
90:&\quad \{45\}\ \big|\ \{1,2,5,9,10,18\}.
\end{aligned}
\]
This proves both the classification and the three-prime-support case of Conjecture 3.1.

## Verification
The accompanying `verify.py` checks the symbolic inequalities as exact rational comparisons, verifies every displayed partition, and directly enumerates all subsets of the eight unitary divisors for a regression grid
\[
1\le\alpha,\beta,\gamma\le4,
\qquad
3\le p<q<20.
\]
Within that grid, direct subset enumeration agrees exactly with the theorem's classification, and every classified case also passes the direct proper-unitary-divisor half-Zumkeller test.

A successful replay prints `VERIFY_OK`.

The finite grid is only a regression check. The complete classification for arbitrary exponents and primes follows from the monotone inequalities and explicit partitions above.

## Relationship to prior work
Das introduced the systematic study of unitary Zumkeller and unitary half-Zumkeller numbers. The paper proves the necessary condition
\[
\sigma^\ast(n)\ge2n,
\]
classifies the two-prime-support unitary Zumkeller case, gives further prime restrictions for larger support, and explicitly says that other prime-power forms would be interesting to investigate. It ends by conjecturing that every even unitary Zumkeller number is unitary half-Zumkeller.

The current OEIS entries for unitary Zumkeller and unitary half-Zumkeller numbers list examples and cite Das's paper, but do not state this three-prime-support classification.

Targeted searches for three-prime-support unitary Zumkeller numbers, for the forms
\[
2^\alpha p^\beta q^\gamma
\]
and
\[
6q^c,
\]
and for Das's Conjecture 3.1 did not locate a prior theorem covering this result. Later papers returned by searches on e-unitary or generalized Zumkeller numbers use different divisor notions and do not imply the present classification.

## Limitations
The theorem covers exactly three distinct prime factors. It does not settle Das's conjecture for four or more distinct prime factors.

The proof uses only a necessary abundance inequality to eliminate all but four shapes; sufficiency is established separately by explicit partitions. No claim is made about the number of distinct partitions.

Literature non-detection is not a proof of novelty. An unindexed or unpublished proof of the same classification could exist.

## References
1. Bhabesh Das, “On unitary Zumkeller numbers,” *Notes on Number Theory and Discrete Mathematics* 30 (2024), no. 2, 436–442, DOI 10.7546/nntdm.2024.30.2.436-442. Online First 16 July 2024.
2. OEIS A290466, “Unitary Zumkeller numbers.”
3. OEIS A290467, “Unitary half-Zumkeller numbers.”
