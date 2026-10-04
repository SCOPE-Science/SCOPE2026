# Finite diagonal core sets are exactly projection-balanced

## Finding

Let \(F\) be a field and let \(n\ge2\). Let \(S\) be a finite subset of the diagonal matrices in
\[
M_n(F).
\]
For each coordinate \(j\), define
\[
X_j
=
\left\{
a_j:
\operatorname{diag}(a_1,\ldots,a_n)\in S
\right\}
\subseteq F
\]
and the monic polynomial
\[
h_j(x)
=
\prod_{a\in X_j}(x-a),
\]
with the empty product interpreted as \(1\).

Under the canonical identification
\[
M_n(F)[x]\cong M_n(F[x]),
\]
the null ideal of \(S\) has the exact column-divisibility form
\[
\boxed{
N(S)
=
\left\{
(p_{ij}(x)):
h_j(x)\mid p_{ij}(x)
\text{ for every }i,j
\right\}.
}
\]

It follows immediately that
\[
\boxed{
S\text{ is core}
\quad\Longleftrightarrow\quad
X_1=X_2=\cdots=X_n.
}
\]
Thus a finite diagonal set is core exactly when every diagonal coordinate attains the same set of field values.

Because core-ness is invariant under simultaneous conjugation, the same statement applies to every finite simultaneously diagonalizable set: in a common eigenbasis, the sets of attained eigenvalues must agree across all coordinates.

Now specialize to
\[
F=\mathbf F_q.
\]
For \(m\ge1\), let \(c_{n,m}\) be the number of subsets of an \(m^n\)-point box whose projection onto every coordinate is the full \(m\)-element alphabet. Inclusion-exclusion gives
\[
\boxed{
c_{n,m}
=
\sum_{j_1,\ldots,j_n=0}^{m}
(-1)^{j_1+\cdots+j_n}
\left(
\prod_{r=1}^{n}\binom{m}{j_r}
\right)
2^{\prod_{r=1}^{n}(m-j_r)}.
}
\]
Therefore the exact number of core subsets of the diagonal subalgebra of \(M_n(\mathbf F_q)\) is
\[
\boxed{
1+
\sum_{m=1}^{q}
\binom{q}{m}c_{n,m}.
}
\]
The initial \(1\) counts the empty set.

For every fixed \(n\ge2\), almost every subset of the diagonal subalgebra is core as \(q\to\infty\). More quantitatively,
\[
\boxed{
\frac{\#\{\text{core subsets of diagonal }M_n(\mathbf F_q)\}}
{2^{q^n}}
\ge
1-nq\,2^{-q^{n-1}}.
}
\]

## Assumptions and scope

Polynomials have coefficients in \(M_n(F)\), the indeterminate is central, and evaluation is from the right:
\[
\left(\sum_k A_kx^k\right)(D)
=
\sum_k A_kD^k.
\]

A subset \(S\subseteq M_n(F)\) is called core when its null ideal
\[
N(S)
=
\{f\in M_n(F)[x]:f(A)=0\text{ for every }A\in S\}
\]
is a two-sided ideal.

The structural theorem concerns finite diagonal sets over an arbitrary field. The exact enumeration and asymptotic statement concern finite fields.

The simultaneously diagonalizable corollary assumes simultaneous diagonalizability over the ground field itself.

## Proof

Write
\[
D=\operatorname{diag}(a_1,\ldots,a_n)
\]
and
\[
f(x)=\sum_{k=0}^{d}A_kx^k.
\]
Under
\[
M_n(F)[x]\cong M_n(F[x]),
\]
let
\[
p_{ij}(x)
=
\sum_{k=0}^{d}(A_k)_{ij}x^k
\]
be the \((i,j)\)-entry polynomial.

Since \(D^k\) is diagonal,
\[
(A_kD^k)_{ij}
=
(A_k)_{ij}a_j^k.
\]
Therefore
\[
f(D)_{ij}
=
p_{ij}(a_j).
\]
Hence \(f\) vanishes on every matrix in \(S\) exactly when, for every column \(j\), every entry polynomial \(p_{ij}\) vanishes on the finite set \(X_j\). Over a field, the monic polynomial of smallest degree vanishing on the distinct points of \(X_j\) is
\[
h_j(x)=\prod_{a\in X_j}(x-a),
\]
and a scalar polynomial vanishes on \(X_j\) exactly when it is divisible by \(h_j\). This proves
\[
N(S)
=
\left\{
(p_{ij}):
h_j\mid p_{ij}
\text{ for all }i,j
\right\}.
\]

Assume first that all \(h_j\) are equal to one polynomial \(h\). Then
\[
N(S)=M_n(hF[x]),
\]
which is a two-sided ideal of \(M_n(F[x])\). Thus \(S\) is core.

Conversely, assume \(N(S)\) is a two-sided ideal. Fix two coordinates \(j,k\). The polynomial matrix having \(h_j\) in one entry of column \(j\) and zero elsewhere lies in \(N(S)\). Right multiplication by the matrix unit \(E_{jk}\) transfers that entry into column \(k\). Since \(N(S)\) is a right ideal, the result must still lie in \(N(S)\), so
\[
h_k\mid h_j.
\]
Interchanging \(j\) and \(k\) gives
\[
h_j\mid h_k.
\]
The polynomials are monic, so
\[
h_j=h_k.
\]
Thus all \(h_j\) agree. Since each \(h_j\) is the square-free monic polynomial whose root set is \(X_j\), equality of the polynomials is equivalent to
\[
X_1=\cdots=X_n.
\]

For the counting formula, fix a common projection set
\[
X\subseteq\mathbf F_q
\]
of size \(m\). A diagonal subset with all coordinate projections equal to \(X\) is the same thing as a subset of \(X^n\) whose projection onto each coordinate is all of \(X\).

For each coordinate-symbol pair, impose the bad event that the symbol does not occur in that coordinate. If \(j_r\) symbols are forbidden in coordinate \(r\), then the surviving box has
\[
\prod_{r=1}^{n}(m-j_r)
\]
points and therefore
\[
2^{\prod_{r=1}^{n}(m-j_r)}
\]
subsets. Choosing the omitted symbols and applying inclusion-exclusion yields
\[
c_{n,m}
=
\sum_{j_1,\ldots,j_n=0}^{m}
(-1)^{j_1+\cdots+j_n}
\left(
\prod_{r=1}^{n}\binom{m}{j_r}
\right)
2^{\prod_{r=1}^{n}(m-j_r)}.
\]
There are
\[
\binom qm
\]
choices for \(X\). Distinct common projection sets give disjoint families of subsets, so summing over \(m\) and adding the empty set gives the exact count.

Finally, choose a subset of \(\mathbf F_q^n\) uniformly at random. If every coordinate projection is all of \(\mathbf F_q\), then the subset is core. For a fixed coordinate and a fixed field element, the probability that none of the
\[
q^{n-1}
\]
tuples carrying that value is selected equals
\[
2^{-q^{n-1}}.
\]
A union bound over the \(nq\) coordinate-value pairs gives
\[
\Pr(\text{not core})
\le
nq\,2^{-q^{n-1}},
\]
which proves the asymptotic statement.

## Verification

The included checker independently performs two kinds of finite verification.

First, for
\[
(q,n)\in\{(2,2),(2,3),(2,4),(3,2),(4,2)\},
\]
it enumerates every subset of the diagonal algebra and directly checks whether all coordinate projection sets agree. The resulting exact core-subset counts are
\[
10,\quad196,\quad63778,\quad290,\quad42610,
\]
respectively.

Second, it evaluates the inclusion-exclusion formula for the same parameters and confirms exact agreement with the brute-force counts, including the decomposition by common projection-set size.

For selected noncore subsets, it also constructs the explicit right-ideal obstruction predicted by the proof: a column generator divisible by \(h_j\) is moved by a matrix unit into a column whose required polynomial \(h_k\) does not divide it.

The checker returns `VERIFY_OK`.

Finite enumeration is not used to prove the theorem.

## Relationship to prior work

Werner's 2022 paper introduced the systematic study of core subsets for matrix-coefficient null ideals and posed the broad problem of determining which subsets of \(M_n(D)\) are core. It gives a full algorithmic characterization only for finite subsets of \(M_2(F)\), while its general-\(n\) results are sufficient conditions and structural reductions.

Swartz and Werner subsequently studied a different higher-dimensional regime: subsets of one irreducible similarity class in \(M_3(F)\). Their paper emphasizes that the general \(n>2\) problem becomes substantially harder in that setting.

Rissner and Werner later counted core subsets in \(M_2(\mathbf F_q)\) and proved that asymptotically almost all subsets of the full \(2\times2\) matrix ring are core. Their exact counts are organized by similarity classes.

The present result treats a different all-dimensions family: arbitrary finite subsets of the diagonal subalgebra. The column-wise form of the null ideal gives a complete criterion for every \(n\), an exact finite-field count, and a direct asymptotic bound. Searches for diagonal, simultaneously diagonalizable, projection-balanced, and coordinate-projection formulations did not locate this characterization or count.

## Limitations

The criterion uses simultaneous diagonal form. It does not classify finite sets of commuting matrices that are not diagonalizable, nor arbitrary subsets of \(M_n(F)\).

The exact counting formula concerns subsets of the diagonal subalgebra, not all subsets of the full matrix ring.

The asymptotic statement keeps \(n\) fixed while the field order tends to infinity.

An equivalent result could be phrased in terms of rectangular set systems or column ideals without using the terminology of core sets.

Failed searches do not prove novelty.

## References

1. N. J. Werner, “Null ideals of subsets of matrix rings over fields,” *Linear Algebra and its Applications* 642 (2022), 50–72, DOI 10.1016/j.laa.2022.02.007.
2. E. Swartz and N. J. Werner, “Null ideals of sets of \(3\times3\) similar matrices with irreducible characteristic polynomial,” arXiv:2212.14460v1, first public version 29 December 2022.
3. R. Rissner and N. J. Werner, “Counting core sets in matrix rings over finite fields,” arXiv:2405.04106v1, first public version 7 May 2024.
