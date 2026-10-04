# A degree-two Blaschke upper curve for fixed-value Bohr majorants

## Finding

Let \(\mathcal S\) denote the Schur class. For \(0<\rho<1\), define \(R_*(\rho)\) to be the largest radius \(R\) such that every
\[
f(z)=\sum_{n\ge0}a_nz^n\in\mathcal S,
\qquad
|f(0)|=\rho,
\]
satisfies
\[
Mf(r)
:=
\sum_{n\ge0}|a_n|r^n
\le
P_\rho(r)
:=
\rho+\frac{(1-\rho^2)r}{1-\rho r}
\]
for every \(0\le r\le R\).

For
\[
0<\rho\le\frac13,
\qquad
s=\sqrt{\rho},
\]
set
\[
Q_s(r)
=
4s^5r^3
+
(-6s^4-4s^3+2s^2)r^2
+
(7s^2-2s-1)r
+
(1-s)^2.
\]
There is a unique zero
\[
R_2(\rho)\in(1/3,1)
\]
of \(Q_s\), and
\[
\frac13
\le
R_*(\rho)
\le
R_2(\rho).
\]

The upper curve is produced by the explicit degree-two Blaschke product
\[
B_\rho(z)
=
\left(
\frac{z-\sqrt{\rho}}
{1-\sqrt{\rho}\,z}
\right)^2.
\]

At the transition value
\[
\rho=\frac13,
\]
one obtains the concrete bound
\[
R_*(1/3)
\le
0.727436801449824\ldots,
\]
where the displayed number is the unique root in \((1/3,1)\) of
\[
2\sqrt3\,r^3
-
6\sqrt3\,r^2
+
(18-9\sqrt3)(r+1)
=
0.
\]

## Assumptions and scope

The comparison function \(P_\rho\) is the coefficient majorant of the disk automorphism
\[
\varphi_\rho(z)
=
\frac{\rho-z}{1-\rho z}.
\]
Multiplication of a Schur function by a unimodular constant leaves its majorant unchanged, so fixing \(|f(0)|=\rho\) may be reduced to fixing \(f(0)=\rho\).

Brevig's fixed-value corollary proves
\[
Mf(r)\le P_\rho(r)
\]
for
\[
0\le r\le\max(\rho,1/3).
\]
Hence, in the range treated here,
\[
R_*(\rho)\ge1/3.
\]

The result supplies an explicit upper obstruction. It does not prove that the degree-two Blaschke product is extremal among all Schur functions, and it does not determine the exact value of \(R_*(\rho)\).

## Proof

Fix
\[
0<\rho\le\frac13
\]
and write
\[
s=\sqrt{\rho}.
\]
Consider
\[
B_\rho(z)
=
\left(
\frac{z-s}{1-sz}
\right)^2.
\]
This is a finite Blaschke product, so
\[
B_\rho\in\mathcal S,
\qquad
B_\rho(0)=s^2=\rho.
\]

Write
\[
B_\rho(z)
=
\rho+\sum_{n\ge1}c_nz^n.
\]
Direct expansion gives, for every \(n\ge1\),
\[
c_n
=
s^{n-2}(1-\rho)
\left(
n(1-\rho)-(1+\rho)
\right).
\]
In particular,
\[
c_1=-2s(1-\rho)<0.
\]
For \(n\ge2\), the assumption \(\rho\le1/3\) gives
\[
n(1-\rho)
\ge
2(1-\rho)
\ge
1+\rho,
\]
so
\[
c_n\ge0.
\]
Therefore the coefficient majorant can be recovered from the ordinary value by reversing only the linear coefficient:
\[
M B_\rho(r)
=
B_\rho(r)-2c_1r.
\]
Thus
\[
M B_\rho(r)
=
\left(
\frac{r-s}{1-sr}
\right)^2
+
4s(1-s^2)r.
\]

Subtracting the automorphism majorant
\[
P_\rho(r)
=
s^2+\frac{(1-s^4)r}{1-s^2r}
\]
and simplifying yields the exact identity
\[
M B_\rho(r)-P_\rho(r)
=
-
\frac{
r(1-s^2)Q_s(r)
}{
(1-rs)^2(1-rs^2)
}.
\]
For
\[
0<r<1
\]
all factors in the denominator and the prefactor \(r(1-s^2)\) are positive. Hence the sign of the majorant defect is the opposite of the sign of \(Q_s(r)\).

It remains to locate the zero of \(Q_s\). First,
\[
Q_s(1)
=
2s(s-1)^2(2s^2+s-2)
<
0
\]
because
\[
0<s\le1/\sqrt3
\]
implies
\[
2s^2+s<2.
\]

At the other endpoint,
\[
Q_s(1/3)
=
\frac{2}{27}
\left(
2s^5-9s^4-6s^3+48s^2-36s+9
\right).
\]
The polynomial in parentheses can be written as
\[
9(1-2s)^2
+
s^2(12-6s-9s^2+2s^3),
\]
which is strictly positive for
\[
0<s\le1/\sqrt3,
\]
since
\[
12-6s-9s^2+2s^3
\ge
12-2\sqrt3-3
>
0.
\]
Thus
\[
Q_s(1/3)>0.
\]

Finally,
\[
Q_s'(r)
=
12s^5r^2
+
(-12s^4-8s^3+4s^2)r
+
7s^2-2s-1.
\]
As a function of \(r\), this is convex. Its endpoint values are
\[
Q_s'(1/3)
=
\frac{s-1}{3}
\left(
4s^4-8s^3-16s^2+9s+3
\right)
<0
\]
and
\[
Q_s'(1)
=
(s-1)
\left(
12s^4-8s^2+3s+1
\right)
<0.
\]
The two bracketed factors are positive on
\[
0<s\le1/\sqrt3.
\]
For the second one, the elementary estimate
\[
12s^4-8s^2+3s+1
\ge
1+s\left(3-\frac8{\sqrt3}\right)
\ge
1+\sqrt3-\frac83
>
0
\]
suffices. For the first one, using
\[
s^2\le\frac{s}{\sqrt3},
\qquad
s^3\le\frac{s}{3},
\]
gives
\[
4s^4-8s^3-16s^2+9s+3
\ge
3+s\left(9-\frac83-\frac{16}{\sqrt3}\right)
>
0
\]
throughout the same interval. Convexity of \(Q_s'\) therefore implies
\[
Q_s'(r)<0
\]
for every
\[
1/3\le r\le1.
\]

Hence \(Q_s\) is strictly decreasing from a positive value to a negative value and has a unique zero
\[
R_2(\rho)\in(1/3,1).
\]
For every
\[
r>R_2(\rho)
\]
one has \(Q_s(r)<0\), so
\[
M B_\rho(r)>P_\rho(r).
\]
Because \(B_\rho\) is an admissible Schur function with fixed value \(\rho\), the universal radius satisfies
\[
R_*(\rho)\le R_2(\rho).
\]

For \(\rho=1/3\), substituting
\[
s=1/\sqrt3
\]
reduces \(Q_s(r)=0\) to
\[
2\sqrt3\,r^3
-
6\sqrt3\,r^2
+
(18-9\sqrt3)(r+1)
=
0.
\]
Its unique root in \((1/3,1)\) is
\[
0.727436801449824\ldots .
\]

## Verification

The coefficient formula was independently obtained by expanding
\[
(z-s)^2(1-sz)^{-2}
\]
and collecting powers. The sign pattern is exact in the entire stated parameter range: one negative linear coefficient and nonnegative coefficients from degree two onward.

The rational identity for
\[
M B_\rho(r)-P_\rho(r)
\]
was simplified algebraically to one cubic numerator. The endpoint signs and strict monotonicity of that cubic are proved symbolically above, so no numerical root search is used to establish existence or uniqueness.

The decimal at \(\rho=1/3\) is only an evaluation of the unique algebraic root specified by the displayed cubic.

## Relationship to prior work

Brevig's 2026 note proves the sharp fixed-value comparison for
\[
r\le\max(\rho,1/3)
\]
and explicitly asks for the largest radius for each fixed
\[
0<\rho<1.
\]
The present result gives an explicit upper curve for the previously open low-value range
\[
0<\rho\le1/3.
\]

The same note explains that the radius \(1/3\) comparison is a special case of a Bhowmik--Das subordination-majorant theorem and that Bombieri's classical argument extends the lower range to \(r\le\rho\). Those results are lower guarantees and do not supply the degree-two upper obstruction above.

Khasyanov's 2023 operator-theoretic framework defines Bohr radii with a fixed initial coefficient and obtains formulas for Hadamard-convolution operators. Its fixed-coefficient radius compares a coefficient majorant with a uniform norm bound. That is a different target inequality from the present comparison with the coefficient majorant \(P_\rho\) of the matching disk automorphism. The inspected theorem does not state the cubic upper curve above.

Targeted searches for fixed-value Schur majorants, degree-two Blaschke obstructions, and the source's open problem did not locate a published statement equivalent to this result.

## Limitations

The upper curve need not be sharp. Other finite or infinite Blaschke products may violate the comparison at smaller radii.

The result treats only
\[
0<\rho\le1/3.
\]
For larger fixed values the coefficient sign pattern of the squared automorphism changes, so the same closed majorant formula no longer follows by reversing only one coefficient.

No claim is made about the exact asymptotics of \(R_*(\rho)\) as \(\rho\) approaches zero or about the full solution of the fixed-value problem.

## References

1. O. F. Brevig, *A bootstrap proof of Bohr's theorem*, arXiv:2609.26850v1, 2026.
2. B. Bhowmik and N. Das, *Bohr phenomenon for subordinating families of certain univalent functions*, Journal of Mathematical Analysis and Applications 462 (2018), 1087--1098.
3. R. Khasyanov, *The Bohr radius and the Hadamard convolution operator*, Journal of Mathematical Analysis and Applications 527 (2023), Article 127782; arXiv:2310.02723.
4. E. Bombieri, *Sopra un teorema di H. Bohr e G. Ricci sulle funzioni maggioranti delle serie di potenze*, Bollettino dell'Unione Matematica Italiana 17 (1962), 276--282.
