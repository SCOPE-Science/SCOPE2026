# Pell-classified Poincaré plateaus in smooth degenerate flag loci
## Finding
For every integer
\[
n\ge1,
\]
let
\[
X_n=(\mathcal F^a_{n+1})_{\mathrm{sm}}
\]
be the smooth locus of the type-
\(A\) PBW degenerate complete flag variety. Cerulli Irelli, Feigin, and Reineke prove that, in their grading convention,
\[
P^{\mathrm{sm}}_n(q)=q^{N_n}r_n(q),
\qquad
N_n=\frac{n(n-1)}2,
\]
where
\[
r_n(q)=\sum_{k=0}^{n}a_{n,k}q^k
\]
counts Schröder paths by the number of diagonal steps.

The coefficients admit the closed form
\[
\boxed{
 a_{n,k}
 =\binom{2n-k}{k}C_{n-k}
 =\frac1n\binom nk\binom{2n-k}{n-1}
}
\qquad(0\le k\le n),
\]
where
\[
C_j=\frac1{j+1}\binom{2j}{j}.
\]
Their adjacent ratio is
\[
\boxed{
\frac{a_{n,k+1}}{a_{n,k}}
=
\frac{(n-k)(n-k+1)}{(k+1)(2n-k)}
}
\qquad(0\le k<n).
\]

Put
\[
\rho_n=n-\sqrt{\frac{n(n+1)}2}.
\]
If
\[
\frac{n(n+1)}2
\]
is not a square, then the coefficient sequence has a unique maximum at
\[
\boxed{
 m_n=\left\lceil n-\sqrt{\frac{n(n+1)}2}\right\rceil.
}
\]
It increases strictly up to this term and decreases strictly afterwards.

If
\[
\frac{n(n+1)}2=s^2,
\]
then there are exactly two equal adjacent maxima, at
\[
\boxed{k=n-s\quad\text{and}\quad k=n-s+1.}
\]
There are no other ties. Thus the Poincaré coefficient profile has a two-term plateau exactly when
\[
\boxed{(2n+1)^2-8s^2=1.}
\]
The exceptional values begin
\[
1,8,49,288,1681,\ldots.
\]
The first nontrivial plateau is therefore the row
\[
n=8,
\]
where the two largest coefficients are
\[
a_{8,2}=a_{8,3}=12012.
\]

The modal exponents of the smooth-locus Poincaré polynomial are the preceding indices shifted by
\[
N_n=\frac{n(n-1)}2.
\]
In particular, the location of the largest graded piece has a deterministic square-root drift with an infinite Pell-classified exceptional subsequence.

## Assumptions and scope
Everything is over
\[
\mathbb C.
\]
The variety
\[
\mathcal F^a_{n+1}
\]
is the Feigin PBW degeneration of the complete flag variety of type
\(A_n\). The statement concerns the smooth locus and the Poincaré polynomial convention used in the cited source. No assertion is made here about intersection cohomology of the singular ambient degenerate flag variety.

The source proves that
\[
P^{\mathrm{sm}}_n(q)=q^{n(n-1)/2}r_n(q)
\]
and defines the exponent of
\(q\) in
\(r_n(q)\) as the number of diagonal
\((1,1)\) steps of a Schröder path. The new statement determines the exact coefficient profile, mode, and all plateau dimensions of this polynomial.

## Proof
Fix
\[
0\le k\le n.
\]
A Schröder path from
\((0,0)\) to
\((n,n)\) with exactly
\(k\) diagonal steps becomes, after deleting those diagonal steps, a Dyck path of semilength
\[
n-k.
\]
Conversely, start with any such Dyck path. It has
\[
2(n-k)
\]
non-diagonal steps and therefore
\[
2(n-k)+1
\]
gaps, including the two end gaps. Insert
\(k\) indistinguishable diagonal steps into these gaps, allowing repetitions. Inserting a diagonal step translates the remaining path by
\((1,1)\), so it preserves the subdiagonal condition. The construction is bijective.

Hence
\[
a_{n,k}
=
C_{n-k}\binom{2(n-k)+k}{k}
=
\binom{2n-k}{k}C_{n-k}.
\]
Simplifying the Catalan factor gives
\[
a_{n,k}
=
\frac{(2n-k)!}{k!(n-k)!(n-k+1)!}
=
\frac1n\binom nk\binom{2n-k}{n-1}.
\]

Taking the quotient of consecutive terms yields
\[
\frac{a_{n,k+1}}{a_{n,k}}
=
\frac{(n-k)(n-k+1)}{(k+1)(2n-k)}.
\]
The numerator minus the denominator after cross multiplication is
\[
(n-k)(n-k+1)-(k+1)(2n-k)
=
2k^2-4nk+n^2-n.
\]
The two real roots are
\[
n\pm\sqrt{\frac{n(n+1)}2}.
\]
Only the smaller root lies in the coefficient range. Thus the ratio is greater than
\(1\) for integer
\(k<\rho_n\), equal to
\(1\) only when
\(k=\rho_n\), and less than
\(1\) for integer
\(k>\rho_n\).

If
\(\rho_n\) is not integral, the unique mode is therefore
\[
\lceil\rho_n\rceil.
\]
If
\(\rho_n\) is integral, exactly one adjacent ratio equals
\(1\), so there is exactly one two-term plateau. Integrality is equivalent to
\[
\frac{n(n+1)}2=s^2
\]
for some integer
\(s\), and then
\[
\rho_n=n-s.
\]
Finally,
\[
\frac{n(n+1)}2=s^2
\]
is equivalent to
\[
(2n+1)^2-8s^2=1,
\]
which is the Pell equation. Its positive solutions generate
\[
n=1,8,49,288,1681,\ldots.
\]
Multiplying by the source's prefactor
\[
q^{N_n}
\]
shifts every modal exponent by
\(N_n\) and changes no coefficient.

## Verification
The bundled checker independently constructs the Schröder coefficient rows in two ways:

1. from the closed Catalan-insertion formula; and
2. from the Schröder-polynomial recurrence recorded in the archival source.

It compares these constructions for
\[
1\le n\le120,
\]
checks every adjacent-ratio identity, verifies the unique-mode/two-mode classification, and confirms that the plateau dimensions through
\[
n\le10000
\]
are exactly the square-triangular solutions of the Pell equation.

The checker also reproduces the source rows
\[
1+q,
\quad
2+3q+q^2,
\quad
5+10q+6q^2+q^3,
\]
and
\[
14+35q+30q^2+10q^3+q^4.
\]
These finite calculations are regression evidence only. The theorem for all
\(n\) follows from the bijective coefficient formula and the exact adjacent-ratio analysis above.

## Relationship to prior work
Cerulli Irelli, Feigin, and Reineke identify the smooth-locus Poincaré polynomial with a shifted Schröder polynomial and record its first rows and recurrence. Their paper does not state coefficient unimodality, a modal formula, a maximum-location theorem, or a Pell exceptional set.

The coefficient triangle itself is classical in Schröder-path enumeration. In particular, the standard formula
\[
\frac1n\binom nk\binom{2n-k}{n-1}
\]
is recorded for the Schröder triangle. The contribution here is not that coefficient formula in isolation, but its implication for the graded topology of the smooth locus: the complete strict-mode classification, the exact two-term plateau criterion, and the Pell parametrization of every exceptional flag dimension.

Recent work generalizes smooth fixed-point criteria from the Feigin degeneration to broader linear degenerations of flag varieties, but it does not supply the Schröder-coefficient modal or Pell statement for this Poincaré polynomial.

## Limitations
The theorem concerns only the smooth locus of the complete type-
\(A\) PBW degeneration. Although the archival source notes extensions to partial degenerations, no plateau law for those more general Poincaré polynomials is claimed.

The result determines the largest coefficient and its location but does not identify multiplicative or representation-theoretic structures on the corresponding cohomology groups.

The classical Schröder coefficient formula is known independently of degenerate flag geometry. The originality claim is restricted to the exact mode/plateau consequence for this geometric Poincaré family and its Pell classification.

## References
Giovanni Cerulli Irelli, Evgeny Feigin, and Markus Reineke, *Degenerate flag varieties: moment graphs and Schröder numbers*, arXiv:1206.4178, first submitted 19 June 2012; *Journal of Algebraic Combinatorics* 38 (2013), 159--189, DOI 10.1007/s10801-012-0397-6.

The On-Line Encyclopedia of Integer Sequences, A060693, Schröder coefficient triangle; the entry records
\(T(n,k)=\binom nk\binom{2n-k}{n-1}/n\).

Sabino Di Trani, *On the smooth locus in flat linear degenerations of flag varieties*, *Algebraic Combinatorics* 9 (2026), 513--541, DOI 10.5802/alco.477.
