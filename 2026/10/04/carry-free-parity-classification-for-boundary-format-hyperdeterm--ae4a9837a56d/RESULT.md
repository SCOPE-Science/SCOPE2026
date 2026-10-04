# Carry-free parity classification for boundary-format hyperdeterminants
## Finding
Fix integers
\[
r\ge 1,
\qquad
k_1,\ldots,k_r\ge 1,
\]
and put
\[
N=k_1+\cdots+k_r.
\]
Consider the boundary-format Segre variety whose dual hyperdeterminant has tensor format
\[
(N+1)\times(k_1+1)\times\cdots\times(k_r+1).
\]
Let \(D\) denote the projective degree of that dual hypersurface. The classical boundary-format degree is
\[
D
=
\frac{(N+1)!}{k_1!\cdots k_r!}
=
(N+1)\binom{N}{k_1,\ldots,k_r}.
\]

For every prime \(p\), the exact valuation is
\[
\nu_p(D)
=
\nu_p(N+1)
+
\frac{\sum_{j=1}^{r}s_p(k_j)-s_p(N)}{p-1},
\]
where \(s_p(m)\) is the sum of the base-\(p\) digits of \(m\).

Equivalently,
\[
p\nmid D
\]
if and only if both of the following hold:
\[
p\nmid N+1
\]
and the addition
\[
k_1+\cdots+k_r=N
\]
is carry-free in base \(p\).

For parity this becomes a complete classification. The degree \(D\) is odd if and only if \(N\) is even and the binary supports of
\[
k_1,\ldots,k_r
\]
are pairwise disjoint. If \(N\) is even and
\[
s=s_2(N),
\]
then the number of odd-degree boundary formats with fixed \(N\) and fixed \(r\), counted up to permutation of the \(r\) smaller tensor factors, is
\[
S(s,r),
\]
the Stirling number of the second kind. For odd \(N\), that number is zero.

Thus odd-degree boundary hyperdeterminants exist with \(r\) smaller factors exactly when
\[
N\text{ is even}
\quad\text{and}\quad
r\le s_2(N).
\]

For example, when
\[
N=14=2+4+8,
\]
there are exactly
\[
S(3,2)=3
\]
odd-degree formats with two smaller factors, represented by
\[
(2,12),\ (4,10),\ (6,8),
\]
and exactly
\[
S(3,3)=1
\]
with three smaller factors, represented by
\[
(2,4,8).
\]

## Assumptions and scope
The ground field is \(\mathbb C\). The tensor is in boundary format: the largest projective dimension \(N\) equals the sum of the remaining projective dimensions. Every \(k_j\) is positive, so all smaller Segre factors have positive dimension.

The degree is the total homogeneous degree of the irreducible hyperdeterminant defining the projective dual hypersurface. Tensor formats are regarded up to permutation of factors when the Stirling count is stated.

The algebraic-geometric motivation comes from the coisotropic interpretation of hyperdeterminants of Segre varieties. Boundary-format hyperdeterminants form the determinant-like boundary of the nondefective Segre duality condition and admit determinantal representations.

## Proof
For boundary format, the degree formula is
\[
D
=
\frac{(N+1)!}{k_1!\cdots k_r!}.
\]
Since
\[
N=k_1+\cdots+k_r,
\]
this can be rewritten as
\[
D
=
(N+1)\binom{N}{k_1,\ldots,k_r}.
\]

Fix a prime \(p\). Legendre's formula in digit-sum form is
\[
\nu_p(m!)
=
\frac{m-s_p(m)}{p-1}.
\]
Applying it to the factorial quotient gives
\[
\begin{aligned}
\nu_p(D)
&=
\nu_p(N+1)
+
\nu_p(N!)
-
\sum_{j=1}^{r}\nu_p(k_j!)\\
&=
\nu_p(N+1)
+
\frac{N-s_p(N)-\sum_j(k_j-s_p(k_j))}{p-1}\\
&=
\nu_p(N+1)
+
\frac{\sum_j s_p(k_j)-s_p(N)}{p-1}.
\end{aligned}
\]

The second summand is the standard multinomial carry count: it is zero exactly when the base-\(p\) addition
\[
k_1+\cdots+k_r=N
\]
produces no carries. Therefore
\[
p\nmid D
\]
exactly when \(p\nmid N+1\) and that addition is carry-free.

Set \(p=2\). The first condition becomes
\[
N\equiv0\pmod 2.
\]
A binary addition is carry-free precisely when no binary position is occupied by a \(1\) in two different summands. Hence the binary supports of the positive \(k_j\) must be pairwise disjoint, and their union must be the support of \(N\).

Let \(B(N)\) be the set of binary positions at which \(N\) has digit \(1\). Then
\[
|B(N)|=s_2(N).
\]
An unordered carry-free decomposition of \(N\) into \(r\) positive summands is equivalent to a partition of \(B(N)\) into \(r\) nonempty blocks: to a block \(C\subseteq B(N)\) associate
\[
\sum_{j\in C}2^j.
\]
The construction is invertible because binary expansion is unique. Therefore the number of formats up to permutation of the smaller factors is exactly
\[
S(s_2(N),r).
\]
This also shows immediately that such a format exists exactly when
\[
r\le s_2(N).
\]

## Verification
The bundled checker performs exact integer tests in three independent ways.

It enumerates all unordered positive partitions of \(N\) for
\[
1\le N\le 36,
\]
computes the boundary hyperdeterminant degree from the factorial quotient, and verifies that the number of odd degrees at each pair \((N,r)\) equals
\[
S(s_2(N),r)
\]
for even \(N\) and zero for odd \(N\).

It also factors every tested degree prime by prime and checks the digit-sum valuation formula directly. Finally, it verifies the carry-free criterion independently from base-\(p\) digit addition.

These finite computations are regression evidence only. The infinite theorem follows from Legendre's formula and the bijection with set partitions.

## Relationship to prior work
Kohn identifies hyperdeterminants as coisotropic forms of Segre varieties and explains the boundary-format case inside projective duality. In particular, boundary-format hyperdeterminants occur as Chow or coisotropic forms and admit determinant-like geometric interpretations.

Dionisi and Ottaviani give a self-contained boundary-format construction and state the classical total-degree formula
\[
\frac{(N+1)!}{k_1!\cdots k_r!}.
\]
Their paper develops the Binet--Cauchy property and nondegeneracy of boundary tensors; it does not state the prime-adic digit-sum law, the carry-free criterion, or the Stirling enumeration of odd-degree formats.

Claim-specific searches using boundary-format, hyperdeterminant, odd degree, parity, prime-adic valuation, carry-free addition, multinomial degree, and Stirling-number formulations did not locate the classification above. The closest previously recorded local result concerns hypercubical formats \(2^{\times d}\), whose degree is governed by a different generating function and does not imply this boundary-format classification.

## Limitations
The theorem applies only to boundary format. General nondefective Segre duals do not have the same factorial degree formula, so the carry law does not extend formally to arbitrary hyperdeterminants.

The Stirling count concerns parity and formats up to permutation of the smaller factors. Ordered formats are counted by
\[
r!\,S(s_2(N),r).
\]
For odd primes, the valuation formula remains exact, but counting all carry-free compositions requires keeping track of base-\(p\) digits with multiplicity and is not reduced here to a Stirling number.

The arithmetic theorem is derived from a classical degree formula and standard valuation identities. Although targeted searches found no prior statement of the resulting classification, an unindexed source could contain the same consequence.

## References
Kathlén Kohn, *Coisotropic Hypersurfaces in the Grassmannian*, arXiv:1607.05932v1, first submitted 20 July 2016.

Carla Dionisi and Giorgio Ottaviani, *The Binet-Cauchy Theorem for the Hyperdeterminant of Boundary Format Multidimensional Matrices*, arXiv:math/0104281, first submitted 29 April 2001; Journal of Algebra 259 (2003), 87--94.

I. M. Gel'fand, M. M. Kapranov, and A. V. Zelevinsky, *Discriminants, Resultants, and Multidimensional Determinants*, Birkhäuser, 1994, Chapter 14.
