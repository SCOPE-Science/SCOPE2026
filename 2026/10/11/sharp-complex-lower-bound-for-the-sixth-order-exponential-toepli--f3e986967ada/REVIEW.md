# Review of Sharp complex lower bound for the sixth-order exponential Toeplitz determinant

## Correctness

PASS. The cited source reduces the complex exponential problem to
\[
T_6(1)=D^2,
\qquad
D=
\frac{
(4-s)^2-w^2
}{16},
\]
where
\[
s=v_1^2
\]
and
\[
|w|\le1-|s|.
\]
Writing
\[
t=|s|,
\]
the reverse triangle inequality and
\[
|4-s|\ge4-t
\]
give
\[
16|D|
\ge
(4-t)^2-(1-t)^2
=
15-6t
\ge9.
\]
Thus
\[
|T_6(1)|
\ge
81/256.
\]

Every equality condition is controlled. Equality forces
\[
t=1,
\]
then
\[
w=0,
\]
and equality in
\[
|4-s|\ge4-|s|
\]
forces
\[
s=1.
\]
Thus
\[
v_1=\pm1,
\]
and Schwarz's lemma gives
\[
v(\zeta)=\pm\zeta.
\]
The converse is immediate. The source supplies the sharp upper constant
\[
625/256.
\]

## Originality

PASS. The full 2026 primary source was inspected through its parity factorization, real exponential specialization, complex exponential proposition, and final remarks. The complex proposition proves only the sharp upper modulus bound and does not state a positive lower complex modulus floor.

Targeted searches used the exact constants, the source DOI and title, the complex exponential specialization, and lower-bound/nonvanishing formulations. They located the primary source and older lower-order or different-class Toeplitz literature, but no statement implying the lower bound.

The result is not a corollary of the source's real theorem because complex Schwarz coefficients invalidate the real-order argument. The proof instead uses the source's separate complex Schur-parameter reduction.

## Value

PASS. The source explicitly uses the complex exponential class to show that the real upper bound fails. The new theorem shows that complexification is asymmetric: it enlarges the upper endpoint but leaves the lower modulus endpoint completely rigid.

This gives a sharp nonvanishing theorem for the determinant, completes both extremal modulus endpoints for the fresh complex specialization, and separates the two linear Schwarz phases: real linear maps attain the lower endpoint while the source's purely imaginary linear maps attain the upper endpoint.

Same-model review: passed. Independent audit: not yet performed.
