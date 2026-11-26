# Independent mathematical audit

## correctness

PASS

Starting at (0,1), the two unimodular child maps give the consecutive Stern pair at every index, with leading zeros preserving (0,1). Nonzero pairs modulo seven project to eight states; vanishing numerator means precisely the start state. Constructing the transition matrix M in homogeneous coordinates independently, the (0,0) resolvent coefficient is the corresponding cofactor of I−zM divided by its determinant. Exact cancellation gave the stated rational function, gcd 1 and the partial fractions in RESULT.md lines 74–78. Expanding the denominator reproduces the recurrence; any eventual rational homogeneous recurrence would give a polynomial multiplier making the series polynomial, so must have degree at least six. In the reciprocal quartic, the two real linear coefficients of the displayed quadratics are distinct, have sum 1 and product −4. The sharper bound needed for their discriminants follows from 17<(4√2−1)^2 (equivalently √2<2), not from 17<49 alone as written. Thus all four reciprocal roots are distinct of modulus √2; coprimality leaves nonzero coefficients at each pole. The normalized mean square tends to the nonzero sum of squared coefficients since all cross-ratio geometric means vanish. This proves the limsup, not a pointwise lower bound. Independent replay: `cd /workspace && python checks/independent_replay.py 1` used exact SymPy determinants, rational gcd and partial fractions, and direct Stern counts through r=13 including r=0. The frozen verifier is corroboration; the proof handles every level.

## originality

PASS

Credit Reznick with the density 1/8 at modulus seven, the finite-state method and the eventual recurrence mechanism, as well as a sharp square-root result at modulus three. The supported distinct part is the explicit reduced modulus-seven series with its minimal recurrence and proof of sharp square-root error for that modulus. Statement-level checks found no coverage of that combination; historical priority is not certified.

## value

PASS

The exact dyadic modular distribution is a natural continuation of the worked modulus-three problem and the nearby small-modulus comparisons. The object is not an arbitrary initial segment: the smallest rational recurrence encodes every level, and the observed return-discrepancy exponent is resolved sharply, distinguishing the actual contributing modes from a general upper estimate. The reduced transfer and pole certificate is independently useful for this prime, beyond confirming the known density or generating sample counts.

The dated certificate retains the supplied scientific assessment, sources and limitations.
