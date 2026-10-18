# An explicit free seven-line–one-conic arrangement of weak type \(2,7,2\)

## Finding

In the complex projective plane, the reduced degree-nine divisor
\[
V(F),\qquad F=xy(x+y)(x+z)(x-z)(y+z)(y-z)(x^2+xy+y^2-z^2)
\]
consists of exactly seven distinct lines and one nonsingular conic. It has precisely two ordinary double points, seven ordinary triple points and two ordinary quadruple points; no other singularities occur. Its total Tjurina number is \(48\), and it is **free with exponents \( (4,4)\)**. All defining coefficients are rational, so the arrangement is also defined over the real numbers. This supplies an explicit realization of the numerically admissible seven-line type \( (2,7,2)\) discussed but not constructed in the cited classification.

## Assumptions and scope

Work over the field \(\mathbb C\), in homogeneous coordinates \([x:y:z]\) on \(\mathbb P^2\). Let \(q=x^2+xy+y^2-z^2\), let \(L=xy(x+y)(x+z)(x-z)(y+z)(y-z)\), and put \(F=Lq\). The free exponents refer to the two degrees of a homogeneous basis of \(\operatorname{AR}(F)=\{(a,b,c):aF_x+bF_y+cF_z=0\}\). There is no claim about all arrangements with the same weak combinatorics or their projective classification.

## Proof

**Components and incidence.** The seven displayed linear factors are pairwise nonproportional. The symmetric Hessian matrix of \(q\) is
\[
\begin{pmatrix}2&1&0\\1&2&0\\0&0&-2\end{pmatrix}
\]
with determinant \(-6\), so the conic is nonsingular. All eleven distinct pairwise line-intersection points and their multiplicities are as follows.

* The six *line-double points* are \([0:1:-1]\), \([0:1:1]\), \([1:0:-1]\), \([1:0:1]\), \([1:1:-1]\), and \([1:1:1]\). The first four lie on the conic; the last two do not.
* The five *line-triple points* are \([0:0:1]\), \([0:1:0]\), \([1:0:0]\), \([1:-1:-1]\), and \([1:-1:1]\). Exactly the final two lie on the conic.

The list is exhaustive since its six double incidences and five triple incidences account for all \(6+3\cdot5=21=\binom72\) pairs of distinct lines. Each line restricts the quadratic form \(q\) to a separable binary quadratic: substitution in the seven line equations yields nonzero discriminants. Hence the conic is transverse to every line, including at the six shared line-intersection points. The incidence multiplicity between conic and lines at those shared points is exactly
\[
4\cdot2+2\cdot3=14=7\cdot2.
\]
By Bézout, there are no further conic–line intersections. The four original line-double points on \(q\) become triple points and the two original line-triple points on \(q\) become quadruple points. The other two line-double and three line-triple points persist, proving \((n_2,n_3,n_4)=(2,7,2)\). All singularities are ordinary transverse multiple points. Their local Tjurina numbers are \((m-1)^2\); therefore \(\tau(F)=2+4\cdot7+9\cdot2=48\).

**Free logarithmic derivations.** Define quartic triples \(P=(P_1,P_2,P_3)\) and \(Q=(Q_1,Q_2,Q_3)\) by
\[
\begin{aligned}
P_1&=-2xz(2xy-9y^2+3z^2),\\
P_2&=2yz(9x^2-2xy-3z^2),\\
P_3&=27x^2y^2-9x^2z^2-4xyz^2-9y^2z^2+3z^4,\\
Q_1&=-x(3x^3+8x^2y+10xy^2-9xz^2+6y^3-18yz^2),\\
Q_2&=y(6x^3+10x^2y+8xy^2-18xz^2+3y^3-9yz^2),\\
Q_3&=2z(x-y)(3x^2+8xy+3y^2).
\end{aligned}
\]
A direct coefficientwise expansion over the integers yields all three exact identities
\[
P_1F_x+P_2F_y+P_3F_z=0,\qquad
Q_1F_x+Q_2F_y+Q_3F_z=0,
\]
\[
\det\begin{pmatrix}x&y&z\\P_1&P_2&P_3\\Q_1&Q_2&Q_3\end{pmatrix}=-243F.
\]
By Saito's determinant criterion, \(F=0\) is a free divisor, with quartic Jacobian syzygies \(P,Q\) forming a basis of \(\operatorname{AR}(F)\), and exponents \((4,4)\). The degree check \(1+4+4=9\) agrees with the determinant identity. This establishes the complete assertion without relying on numerical rank inference or a genericity assumption.

## Verification

The accompanying standalone Python 3 program `verify.py` uses only exact integer polynomial arithmetic and no external library. It constructs the seven lines and the conic, enumerates all line-pair intersections using cross products, verifies incidence sets, tests the seven quadratic restriction discriminants, checks the Bézout sum and singularity counts, and expands both Jacobian syzygies and their determinant. Running `python3 verify.py` must print `VERIFIED_OK`. No floating-point computation is used. Its finite checks are exact coefficient identities for the stated single homogeneous divisor, not experiments offered as proof of a family.

## Relationship to prior work

Pokora, *Freeness of arrangements of lines and one conic with ordinary quasi-homogeneous singularities* (arXiv:2312.13052, especially the degree-seven part of the proof of Theorem 1.3 and Remarks 3.2–3.3 in version 5), gives five numerical candidates for seven lines, but displays explicit realizations only of the first three: \((5,2,4)\), \((5,4,3)\), and \((8,1,4)\). It identifies the type \((2,7,2)\) as an outstanding realization question. Remark 3.2 explains why a previously suggested diagram from Neusel's 1992 thesis fails to produce the required six conic points. The present divisor uses different line equations, satisfies the exact desired incidence vector, and supplies a quartic Saito basis. The general numerical inequalities for freeness do not themselves construct a divisor or certify these exact coefficient identities.

## Limitations

This is a single explicit real-coefficient complex arrangement, not a classification of all realizations, not a uniqueness theorem, and not a proof of the Numerical Terao conjecture. No assertion is made about arbitrary positive-characteristic reductions, for which the determinant factor \(-243\) may vanish. The full text of Neusel's 1992 thesis was not independently available; the comparison with its pictured construction relies on the detailed discussion in Pokora's openly accessible full paper. Other unlocated equivalent realizations remain a bibliographic risk.

## References

1. Piotr Pokora, *Freeness of arrangements of lines and one conic with ordinary quasi-homogeneous singularities*, arXiv:2312.13052 (first public version 2023-12-20), especially pp. 9–12 and Remarks 3.2–3.3 of v5, https://arxiv.org/abs/2312.13052 and https://arxiv.org/pdf/2312.13052.
2. M. Neusel, *Konfigurationen von Geraden und einer Quadrik mit Baumauflösung – ein Bilderbuch*, doctoral thesis, Göttingen (1992), cited in [1]. Original not independently examined.
3. K. Saito, *Theory of logarithmic differential forms and logarithmic vector fields*, J. Fac. Sci. Univ. Tokyo Sect. IA Math. **27** (1980), 265–291 (standard determinant criterion for free divisors).
