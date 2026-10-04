# Exact higher-support spectra for the new systematic simplex LCD families
## Finding

Mondal and Lee introduce two LCD-optimal families obtained by adjoining an identity block to a simplex-type generator. They are the binary family from Theorem 3.1(i),
\[
C_2(m)\subseteq \mathbb F_2^{\,m+2^m-1},
\qquad m\ge3,
\]
and the ternary family from Theorem 3.7,
\[
C_3(m)\subseteq \mathbb F_3^{\,m+3^m-1},
\qquad m\ge2.
\]
In both cases a generator can be written
\[
G_q(m)=[I_m\mid S_q(m)],
\]
where \(q\in\{2,3\}\) and the columns of \(S_q(m)\) are all nonzero vectors of \(\mathbb F_q^m\).

For every \(1\le r\le m\), the generalized Hamming weight is
\[
d_r(C_q(m))
=
q^m-q^{m-r}+r.
\]

There is also a closed formula for the entire support-size spectrum of \(r\)-dimensional subcodes. Write \(G_q(a,b)\) for the Gaussian binomial coefficient, with \(G_q(a,b)=0\) when \(b<0\) or \(b>a\). Define
\[
F_q(s,r)
=
\sum_{j=0}^{s}
(-1)^j
\binom{s}{j}
G_q(s-j,r).
\]
Then for every \(r\le s\le m\), the number of \(r\)-dimensional subcodes having support size
\[
q^m-q^{m-r}+s
\]
is exactly
\[
\binom{m}{s}F_q(s,r).
\]
No other support sizes occur.

For example, the binary \([10,3,5]_2\) code of the source has hierarchy
\[
(5,8,10),
\]
and its two-dimensional subcodes have support \(8\) three times and support \(9\) four times. The ternary \([10,2,7]_3\) example has hierarchy
\[
(7,10).
\]

## Assumptions and scope

The binary family is exactly the family \(C'_{\Delta^*}\) in Theorem 3.1(i), after restricting to the \(m=|A|\) active coordinates of the message space. Its simplex block contains every nonzero vector of \(\mathbb F_2^m\) once.

The ternary family is exactly \(C'_{D_{F^{(1)}}}\) in Theorem 3.7. The defining set is
\[
D_{F^{(1)}}=\mathbb F_3^m\setminus\{0\},
\]
so its non-systematic block contains every nonzero vector of \(\mathbb F_3^m\) once.

For an \(r\)-dimensional subcode \(D\), the support is the union of the supports of all words in \(D\), and
\[
d_r(C)=\min_{\dim D=r}|\operatorname{Supp}(D)|.
\]

## Proof

Let \(U\le\mathbb F_q^m\) be an \(r\)-dimensional message subspace. Its image under \(G_q(m)\) is an \(r\)-dimensional subcode.

Consider first the simplex block. A column \(v\in\mathbb F_q^m\setminus\{0\}\) is zero on the entire subcode precisely when
\[
u\cdot v=0
\qquad\text{for every }u\in U.
\]
Equivalently,
\[
v\in U^\perp.
\]
Since
\[
\dim U^\perp=m-r,
\]
there are
\[
q^{m-r}-1
\]
nonzero columns outside the support of the simplex block. Therefore every \(r\)-subcode has exactly
\[
(q^m-1)-(q^{m-r}-1)
=
q^m-q^{m-r}
\]
support positions in that block.

The identity block records the ordinary coordinate support of \(U\). Let
\[
s(U)=
\left|
\left\{
i:
u_i\ne0\text{ for some }u\in U
\right\}
\right|.
\]
Then
\[
|\operatorname{Supp}(UG_q(m))|
=
q^m-q^{m-r}+s(U).
\]

Every \(r\)-dimensional subspace needs at least \(r\) active coordinate positions, so
\[
s(U)\ge r.
\]
Equality is attained by any coordinate \(r\)-space. Hence
\[
d_r(C_q(m))
=
q^m-q^{m-r}+r.
\]

It remains to count subcodes at each support size. Fix a coordinate set \(S\subseteq\{1,\ldots,m\}\) of size \(s\). The number of \(r\)-subspaces contained in \(\mathbb F_q^S\) and having support exactly \(S\) is the number not contained in any coordinate hyperplane of \(\mathbb F_q^S\). Inclusion-exclusion over the \(s\) coordinate hyperplanes gives
\[
F_q(s,r)
=
\sum_{j=0}^{s}
(-1)^j
\binom{s}{j}
G_q(s-j,r).
\]
There are
\[
\binom{m}{s}
\]
choices for \(S\), yielding the claimed frequency
\[
\binom{m}{s}F_q(s,r).
\]

Summing these frequencies over \(s\) recovers
\[
G_q(m,r),
\]
the total number of \(r\)-dimensional subspaces of \(\mathbb F_q^m\), so the spectrum is exhaustive.

## Verification

`artifacts/verify.py` checks the closed formulas against direct reduced-row-echelon enumeration of all message subspaces for the source examples and nearby instances:
\[
(q,m)=(2,3),(2,4),(3,2),(3,3).
\]

For each instance and every subcode dimension, the verifier builds
\[
[I_m\mid S_q(m)]
\]
explicitly, enumerates every subspace exactly once, computes its support, and compares the resulting histogram with the inclusion-exclusion formula. It also checks that the minimum of each histogram equals
\[
q^m-q^{m-r}+r.
\]
Successful replay prints `VERIFY_OK`.

## Relationship to prior work

Mondal and Lee determine the ordinary weight distributions and prove LCD optimality of these families. Their article contains no generalized-Hamming-weight discussion.

The generalized Hamming weights of simplex codes themselves are classical, and prior work also studies generalized or extended weight enumerators of simplex codes. That broader coverage determines the fixed contribution
\[
q^m-q^{m-r}
\]
from the simplex block. It does not, however, determine the higher-support spectrum after adjoining the systematic identity block. The extra term depends on the coordinate support of the message subspace, and the exact multiplicities require the full-support subspace count above.

Focused public and research-record searches using “systematic simplex”, “augmented simplex”, the exact formula
\[
q^m-q^{m-r}+r,
\]
binary and ternary specializations, and generalized-Hamming-weight terminology did not locate a prior statement for these newly introduced LCD families.

## Limitations

The theorem applies to the two systematic simplex families in Theorems 3.1(i) and 3.7. It does not automatically extend to the paper's other LCD constructions, whose non-systematic blocks are not the complete nonzero vector set.

The originality claim concerns the identity-augmented LCD families and their complete higher-support spectra. No novelty is claimed for the classical generalized Hamming weights of the simplex block alone.

The support-spectrum formula is structural and exact, but it does not classify the automorphism groups or equivalence classes of these codes.

## References

1. Nilay Kumar Mondal and Yoonjin Lee, *Infinite families of LCD codes and their weight distributions*, Applicable Algebra in Engineering, Communication and Computing, published 4 September 2026, DOI 10.1007/s00200-026-00756-3.
2. V. K. Wei, *Generalized Hamming weights for linear codes*, IEEE Transactions on Information Theory 37 (1991), 1412--1418.
3. Relinde P. M. J. Jurrius, *Weight enumeration of codes from finite spaces*, Designs, Codes and Cryptography 63 (2012), 321--330, DOI 10.1007/s10623-011-9557-2.
