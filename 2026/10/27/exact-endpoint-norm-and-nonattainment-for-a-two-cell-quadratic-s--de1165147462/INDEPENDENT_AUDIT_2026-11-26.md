# Independent mathematical audit

## correctness

PASS

Independently use normalized cell coordinates u,v in [0,1] going from each outer endpoint toward the knot. The unit-cell polynomial kernel is F(u,v)=1+3(2u-1)(2v-1)+5(6u^2-6u+1)(6v^2-6v+1). Each half has mass 1/2, giving uncoupled kernel 2F, and enforcing equality of the traces removes the one-dimensional Riesz normal for their difference. Its squared norm is 36, so the correction is -F(u,1)F(v,1)/9 on the same cell and +F(u,1)F(v,1)/9 on the opposite cell, in agreement with the endpoint polynomials in physical coordinates. Direct Gram inversion also recovered the full frozen kernel. At x=0 each piece has two simple roots strictly in its half; the two negative masses computed from discriminants 2784 and 96 are 29 sqrt(174)/625 and sqrt(6)/25. Reproduction of 1 yields the stated constant. For global control, quadratic Bernstein interpolation on ten intervals covers the entire left half. Independently bounded each nonzero-endpoint control occurrence using a second Bernstein subdivision in the integration variable, integrating the sum of absolute control coefficients against its positive basis functions, with the cell weight 1/2. All 29 upper bounds were at most 30089/13824 < 9/4, while the exact endpoint value is >9/4 (replay: python3 /workspace/branches/frozen_math_recheck.py 4). Here all occurrences other than the distinguished K(0,*) row are bounded; grid points are not being used as a proxy for untested x. Convexity with the Bernstein coefficients forces strict inequality off x=0 on the left and off x=1 on the right by reflection. The output is continuous, so essential and ordinary output suprema coincide; the sign of the endpoint row attains the norm for measurable inputs and is approximable for this integral by continuous bounded inputs, smoothing around the simple roots. At equality a continuous input would have to match the sign up to a single phase almost everywhere on the nonzero set of the maximizing row. A sign change makes that incompatible with continuity, for both real and complex inputs. The frozen checker was read, not run.

## originality

PASS

The checked distinct result is the sharp global operator norm, exact maximizers and attainment distinction for the finite two-element continuous quadratic projection. Knot-sequence-independent boundedness and related spline kernel bounds are prior; no exact covering result for this space was verified.

## value

PASS

The first symmetric two-element C0 quadratic space is a natural finite-element stability benchmark fixed before computation. Its sharp norm quantifies the largest possible excursion of a projected bounded input, and the strict endpoint classification and continuous nonattainment describe how such excursions can be approached. In particular, by preservation of constants, the norm fixes the sharp overshoot (C-1)/2 for inputs in [0,1], useful without any extrapolation to other knots or continuity orders.

The dated certificate retains the supplied scientific assessment, sources and limitations.
