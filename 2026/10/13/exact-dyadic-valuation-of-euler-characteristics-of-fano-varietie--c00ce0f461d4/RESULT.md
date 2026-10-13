# Exact dyadic valuation of Euler characteristics of Fano varieties of lines on cubic hypersurfaces
## Finding
Let
\[
Y_d\subset\mathbb P^{d+1}_{\mathbb C},
\qquad
d\ge2,
\]
be a smooth cubic hypersurface, and let
\[
F_d=F(Y_d)
\]
be its Fano variety of lines.

The Euler characteristics satisfy
\[
\chi(Y_d)
=
\frac{(-2)^{d+2}-1}{3}+d+2
\]
and
\[
\chi(F_d)
=
\frac{\chi(Y_d)\bigl(\chi(Y_d)-3\bigr)}{2}.
\]

The exact two-adic valuation of the Fano Euler characteristic is
\[
\nu_2\!\left(\chi(F_d)\right)
=
\begin{cases}
\nu_2(3d-4)-1,& d\text{ even},\\[4pt]
\nu_2(3d+5)-1,& d\text{ odd}.
\end{cases}
\]

In particular,
\[
\chi(F_d)\text{ is odd}
\iff
d\equiv2\text{ or }3\pmod4.
\]

There is also a complete dyadic stratification. For every integer
\[
t\ge0,
\]
the dimensions satisfying
\[
\nu_2\!\left(\chi(F_d)\right)=t
\]
occupy exactly two residue classes modulo
\[
2^{t+2}.
\]
They are characterized by
\[
3d-4\equiv2^{t+1}\pmod{2^{t+2}}
\]
on the even branch and
\[
3d+5\equiv2^{t+1}\pmod{2^{t+2}}
\]
on the odd branch.

The first Euler characteristics are
\[
27,\ 27,\ 324,\ 702,\ 4185,\ 13365,\ 61074,\ 226800,\ldots
\]
for
\[
d=2,3,4,5,6,7,8,9,\ldots
\]
respectively.

## Assumptions and scope
The ground field is \(\mathbb C\). The cubic hypersurface is smooth and has dimension at least two, so its Fano variety of lines is the standard smooth projective parameter space considered in the cubic-hypersurface literature.

The result concerns the topological Euler characteristic of the complex Fano variety. It does not assert an analogous valuation formula for individual Betti or Hodge numbers.

## Proof
For a smooth cubic hypersurface
\[
Y_d\subset\mathbb P^{d+1},
\]
the tangent-sequence computation gives
\[
c(TY_d)
=
\frac{(1+H)^{d+2}}{1+3H}.
\]
Since
\[
\int_{Y_d}H^d=3,
\]
the Gauss--Bonnet formula yields
\[
\chi(Y_d)
=
3\,[H^d]\frac{(1+H)^{d+2}}{1+3H}
=
\frac{(-2)^{d+2}-1}{3}+d+2.
\]

Galkin and Shinder prove the cubic \(Y\)-\(F(Y)\) relation
\[
[Y^{(2)}]
=
(1+\mathbb L^d)[Y]+\mathbb L^2[F(Y)]
\]
in the Grothendieck ring for a smooth cubic \(d\)-fold. Applying the complex Euler characteristic sends
\[
\mathbb L
\]
to \(1\), so
\[
\chi(Y^{(2)})
=
2\chi(Y)+\chi(F(Y)).
\]
The symmetric-square identity
\[
\chi(Y^{(2)})
=
\frac{\chi(Y)\bigl(\chi(Y)+1\bigr)}2
\]
therefore gives
\[
\chi(F_d)
=
\frac{\chi(Y_d)\bigl(\chi(Y_d)-3\bigr)}2.
\]

Now suppose \(d\) is even. Then
\[
\chi(Y_d)
=
\frac{2^{d+2}+3d+5}{3}
\]
is odd, while
\[
\chi(Y_d)-3
=
\frac{2^{d+2}+3d-4}{3}.
\]
Because
\[
0<|3d-4|<2^{d+2}
\]
for every even \(d\ge2\),
\[
\nu_2(3d-4)<d+2.
\]
The two summands
\[
2^{d+2}
\quad\text{and}\quad
3d-4
\]
therefore have different two-adic valuations, hence
\[
\nu_2\bigl(\chi(Y_d)-3\bigr)
=
\nu_2(3d-4).
\]
Thus
\[
\nu_2\!\left(\chi(F_d)\right)
=
\nu_2(3d-4)-1.
\]

Now suppose \(d\) is odd. Then
\[
\chi(Y_d)
=
\frac{-2^{d+2}+3d+5}{3}
\]
is even, while
\[
\chi(Y_d)-3
\]
is odd. Since
\[
0<3d+5<2^{d+2}
\]
for every odd \(d\ge3\),
\[
\nu_2(3d+5)<d+2.
\]
Again the summands have unequal two-adic valuation, so
\[
\nu_2\bigl(\chi(Y_d)\bigr)
=
\nu_2(3d+5),
\]
and hence
\[
\nu_2\!\left(\chi(F_d)\right)
=
\nu_2(3d+5)-1.
\]

For \(t\ge0\), the equation
\[
\nu_2(m)=t+1
\]
is equivalent to
\[
m\equiv2^{t+1}\pmod{2^{t+2}}.
\]
Since \(3\) is invertible modulo every power of \(2\), each branch determines exactly one residue class of \(d\) modulo \(2^{t+2}\). The even and odd branches are distinct, proving the stated dyadic stratification.

## Verification
The bundled exact checker independently computes
\[
\chi(Y_d)
\]
in two ways: from the closed formula and directly from the top Chern-class coefficient
\[
3\,[H^d]\frac{(1+H)^{d+2}}{1+3H}.
\]
It then computes
\[
\chi(F_d)
=
\frac{\chi(Y_d)(\chi(Y_d)-3)}2
\]
and verifies the valuation formula for every
\[
2\le d\le5000.
\]

The checker also verifies the first dyadic strata by residue class and reproduces the classical values
\[
\chi(F_2)=27,
\qquad
\chi(F_3)=27,
\qquad
\chi(F_4)=324.
\]

These finite computations are regression evidence only. The infinite valuation theorem is proved by the exact formulas and the valuation comparison above.

## Relationship to prior work
Galkin and Shinder establish the Grothendieck-ring relation between a cubic hypersurface and its Fano variety of lines and use it to compute Hodge-theoretic information in arbitrary dimension. Their paper also records the symmetric-square Euler-characteristic identity needed to pass from that relation to
\[
\chi(F_d)
=
\frac{\chi(Y_d)(\chi(Y_d)-3)}2.
\]

Later work lifts the same cubic/Fano relation to derived categories, confirming its structural role in the geometry of cubic hypersurfaces.

The contribution here is the exact two-adic analysis of the resulting Euler-characteristic sequence. Searches using the terms Fano variety of lines, cubic hypersurface, Euler characteristic, parity, congruence, divisibility, and two-adic valuation did not locate the displayed valuation formula, its parity criterion, or the two-residue-class stratification.

## Limitations
The theorem concerns smooth cubic hypersurfaces. Singular cubics have correction terms in the cubic/Fano relation and can have different Euler characteristics.

The result controls only the total Euler characteristic. It does not determine the two-adic behavior of individual Hodge numbers.

The valuation argument is short once the cubic/Fano Euler formula is available, so an unindexed source could contain the same arithmetic refinement.

## References
Sergey Galkin and Evgeny Shinder, *The Fano variety of lines and rationality problem for a cubic hypersurface*, arXiv:1405.5154, first submitted 20 May 2014.

Pieter Belmans, Lie Fu, and Theo Raedschelders, *Derived categories of flips and cubic hypersurfaces*, Proceedings of the London Mathematical Society 125 (2022), 1452--1482.
