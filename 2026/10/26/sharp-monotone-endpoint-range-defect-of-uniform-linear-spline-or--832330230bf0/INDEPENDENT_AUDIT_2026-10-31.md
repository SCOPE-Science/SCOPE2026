# Independent mathematical audit

## correctness

PASS

PASS: Tridiagonal uniform-hat Gram matrix gives alternating inverse endpoint row (-1)^j a_j with positive decreasing a_j, and r1=1/2, r_(n+1)=1/(4-r_n). Every bounded monotone f is a mixture of right-step functions plus constant. For endpoint kernel K the step response E(s)=integral_s^n K has first-cell minimum -delta_n at s=1/(1+r_n), delta_n=3/((2-r_n)(1+r_n))-1. Alternating-series bounds at later cell boundaries and their only internal critical points prove -delta_n<=E<=1 globally, treating n=1,2 separately; reflection gives right endpoint. The recurrence decreases to 2-sqrt3 and the defect increases strictly to (sqrt3-1)/2. Independent exact rational Gram inversion and every cell critical value n=1..30 reproduced the bound and the listed first three fractions (C4_OK).

## originality

PASS

PASS, qualified: Oswald and Passenbrunner give unrestricted spline L∞ bounds and related Gram inverses; these do not state a sharp endpoint projection bound restricted to monotone data. Zhang explicitly analyzes step-data Gibbs overshoot for finite-element L² projection and comes closest in physical effect, but treats interior/nodal discontinuities and local asymptotic models rather than the all-n finite-interval endpoint extremizer and recurrence. Oswald 2013 projection chapter not fully accessible and could conceal equivalent boundary estimates. A broader positivity-defect theorem may directly imply the special exact constant; this risk is noted.

## value

PASS

PASS: A sharp monotone-data boundary range-preservation defect is a natural stability/shape question for canonical uniform least-squares splines. The exact step witness, all-n recurrence, and strict limiting defect distinguish it from unrestricted norm estimates or arbitrarily chosen sample numbers.

The dated certificate retains the supplied scientific assessment, sources and limitations.
