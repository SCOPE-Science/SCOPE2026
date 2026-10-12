# Zero forcing polynomial and minimum rank of two-prime-square residue-ring zero-divisor graphs

## Finding

Let \(p\ne q\) be primes and let \(G=\Gamma(\mathbb Z/(p^2q))\) be the standard zero-divisor graph on the nonzero zero-divisors. Put \(N=p^2+pq-p-1\). Then \[\mathcal Z(G;u)=u^{N-4}(u+(p-1)(q-1))(u+p-1)(u+q-1)(u+p(p-1)).\] Consequently \(Z(G)=M(G)=N-4\) and the real symmetric minimum rank is \(\operatorname{mr}(G)=4\). The minimum zero forcing sets are exactly the complements of one vertex from each of the four gcd classes \((x,p^2q)=p,pq,p^2,q\), so there are \(p(p-1)^3(q-1)^2\) minimum sets.

The factorization is uniform in both primes, including the boundary cases in which one of the four gcd classes is a singleton.

## Assumptions and scope

Let
\[
R=\mathbb Z/(p^2q),
\qquad
p\ne q
\]
for primes \(p,q\). The standard zero-divisor graph
\[
G=\Gamma(R)
\]
has vertex set the nonzero zero-divisors of \(R\), with distinct vertices adjacent exactly when their product is zero in \(R\).

Write
\[
A=\{x:(x,p^2q)=p\},
\quad
B=\{x:(x,p^2q)=pq\},
\]
\[
C=\{x:(x,p^2q)=p^2\},
\quad
D=\{x:(x,p^2q)=q\}.
\]

## Proof

Euler's totient formula gives
\[
|A|=(p-1)(q-1),\qquad |B|=p-1,
\]
\[
|C|=q-1,\qquad |D|=p(p-1).
\tag{1}
\]
Hence
\[
N=|V(G)|
=p^2+pq-p-1.
\]

An edge \(xy\) occurs exactly when
\[
p^2q\mid xy.
\]
Reading the \(p\)- and \(q\)-adic divisibilities of the four gcd classes shows:

\[
A\sim B,\qquad B\sim C,\qquad C\sim D,
\tag{2}
\]
where each relation in (2) is a complete join between the two classes. The class \(B\) is a clique, while \(A,C,D\) are independent sets, and there are no other cross-class edges.

This decomposition is also the one used in the published homological analysis of \(\Gamma(\mathbb Z_{p^2q})\).

Each of \(A,B,C,D\) is a twin class: \(A,C,D\) are false-twin classes and \(B\) is a true-twin class. Therefore a zero forcing set can leave at most one white vertex in each class. Two white twins cannot be distinguished by the first force that colors one of them.

Conversely, every coloring leaving at most one white vertex in each class is zero forcing. Because
\[
|A|=(p-1)(q-1)\ge2
\quad\text{and}\quad
|D|=p(p-1)\ge2,
\]
there is always a blue vertex in \(A\) and in \(D\). A blue vertex of \(D\) first forces a possible white vertex of \(C\), because \(D\) is adjacent only to \(C\). Independently, a blue vertex of \(A\) forces a possible white vertex of \(B\), because \(A\) is adjacent only to \(B\). Now \(B\) and \(C\) are fully blue. A blue vertex of \(C\) forces a possible white vertex of \(D\), and a blue vertex of \(B\) forces a possible white vertex of \(A\).

Thus the choice in each class is independent: one either colors the entire class blue or leaves exactly one vertex white. A class of size \(w\) contributes
\[
u^w+w u^{w-1}
=
u^{w-1}(u+w).
\]
Using (1),
\[
\begin{aligned}
\mathcal Z(G;u)
&=
u^{N-4}
(u+(p-1)(q-1))
(u+p-1)\\
&\qquad\cdot
(u+q-1)
(u+p(p-1)).
\end{aligned}
\]
Therefore
\[
Z(G)=N-4.
\]
The minimum zero forcing sets leave one vertex white in every class, so their number is
\[
|A||B||C||D|
=
p(p-1)^3(q-1)^2.
\]

For minimum rank, order the classes as
\[
A,B,C,D
\]
and consider
\[
Q=
\begin{pmatrix}
0&1&0&0\\
1&1&1&0\\
0&1&0&1\\
0&0&1&0
\end{pmatrix}.
\tag{3}
\]
Its determinant is \(1\). Replace each entry \(Q_{ij}\) by a constant block of the corresponding class sizes. The resulting symmetric matrix has nonzero off-diagonal entries exactly at the edges of \(G\), including the clique block on \(B\). Because all four classes are nonempty and \(Q\) is nonsingular, this matrix has rank \(4\). Hence
\[
\operatorname{mr}(G)\le4.
\]

The standard maximum-nullity inequality
\[
M(G)\le Z(G)
\]
gives
\[
\operatorname{mr}(G)
=
N-M(G)
\ge
N-Z(G)
=
4.
\]
Consequently
\[
\operatorname{mr}(G)=4
\]
and
\[
M(G)=Z(G)=N-4.
\]

## Verification

The accompanying `verify.py` constructs \(\Gamma(\mathbb Z/(p^2q))\) directly from residue multiplication, with no use of the class decomposition in the edge test. It then recovers the gcd class of every vertex and checks the four-class structure edge by edge.

For
\[
(p,q)=(2,3),(3,2),(2,5),
\]
every vertex subset is exhaustively tested for the zero forcing property and the complete polynomial is compared with the theorem. The larger cases
\[
(3,5),(5,2)
\]
check the direct graph structure, the factorized polynomial prediction, all \(16\) at-most-one-white class profiles, and the rank witness.

The block matrix from (3) is checked entry by entry and row-reduced exactly over the rationals.

Exact replay output:

```text
p=2, q=3: N=7, polynomial={3: 8, 4: 20, 5: 18, 6: 7, 7: 1}, witness_rank=4
p=3, q=2: N=11, polynomial={7: 24, 8: 52, 9: 38, 10: 11, 11: 1}, witness_rank=4
p=2, q=5: N=11, polynomial={7: 32, 8: 64, 9: 42, 10: 11, 11: 1}, witness_rank=4
p=3, q=5: N=20, predicted_polynomial={20: 1, 19: 20, 18: 140, 17: 400, 16: 384}, witness_rank=4
p=5, q=2: N=29, predicted_polynomial={29: 1, 28: 29, 27: 204, 26: 496, 25: 320}, witness_rank=4
ALL_16_TYPE_PROFILES_FORCE_OK
VERIFY_OK
```

The finite computations corroborate but do not replace the arbitrary-prime proof.

## Relationship to prior work

Anderson and Badawi give the standard nonzero-zero-divisor graph definition used here and study it from commutative algebra; their article lists primary Mathematics Subject Classification \(13A15\).

Rather, Imran, and Pirzada give a full modern treatment of the exact family \(\Gamma(\mathbb Z_{p^2q})\) in their study of edge ideals. Their full text partitions the graph into the same four gcd classes, gives their totient cardinalities, and identifies the complete joins \(A\)-\(B\), \(B\)-\(C\), and \(C\)-\(D\), with \(B\) a clique. That structural decomposition is prior coverage and is not claimed as new. Their article studies Betti numbers, regularity, and projective dimension; full-text searches found no occurrence of “zero forcing” or “minimum rank.”

Boyer and collaborators introduced the zero forcing polynomial and developed its general structural theory. A recent modular-compression framework also shows that zero forcing polynomials of graphs with a bounded number of twin types can be reduced to their type graph. Those general mechanisms are prior coverage. The contribution here is the exact arithmetic specialization, the complete minimum-set classification, and the matching real minimum-rank theorem for \(\Gamma(\mathbb Z_{p^2q})\).

Targeted searches under the zero-divisor-graph name, the \(\mathbb Z_{p^2q}\) specialization, zero forcing polynomial, maximum nullity, minimum rank, and \(P_4\)-blow-up/twin-class aliases did not locate this statement.

## Limitations

The theorem treats exactly the exponent pattern
\[
p^2q
\]
with distinct primes. It does not claim the same factorization for \(p^\alpha q^\beta\) with other exponent pairs or for three distinct prime factors.

The four-class graph decomposition is known prior work; originality is restricted to the forcing enumerator, all minimum forcing sets, and the exact real minimum-rank equality.

The minimum-rank statement is over real symmetric graph-pattern matrices.

Generic twin-class compression can algorithmically reduce the forcing polynomial, so the value of the result lies in the closed arithmetic formula and the complete algebraic graph classification rather than in compression alone.

## References

1. D. F. Anderson and A. Badawi, “On the Zero-Divisor Graph of a Ring,” *Communications in Algebra* 36 (2008), 3073–3092. DOI: 10.1080/00927870802110888. Published online 22 August 2008.
2. B. A. Rather, M. Imran, and S. Pirzada, “Linear strand of edge ideals of zero divisor graphs of the ring \(\mathbb Z_n\),” *Communications in Algebra* 52 (2024), 5069–5085. DOI: 10.1080/00927872.2024.2363953. Published online 1 July 2024.
3. K. Boyer, B. Brimkov, S. English, D. Ferrero, A. Keller, R. Kirsch, M. Phillips, and C. Reinhart, “The zero forcing polynomial of a graph,” arXiv:1801.08910, first posted 26 January 2018; *Discrete Applied Mathematics* 258 (2019), 35–48.
4. AIM Minimum Rank — Special Graphs Work Group, “Zero forcing sets and the minimum rank of graphs,” *Linear Algebra and its Applications* 428 (2008), 1628–1648. DOI: 10.1016/j.laa.2007.10.009.
