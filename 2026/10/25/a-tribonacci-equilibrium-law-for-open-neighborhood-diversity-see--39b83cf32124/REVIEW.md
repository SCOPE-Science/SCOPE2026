# Independent mathematical audit

## correctness

PASS

Utility is the indicator that the two neighbor colors differ. Same-color swaps leave utility unchanged; an opposite-color nonadjacent pair simply exchanges its two destination utilities and cannot both improve. For adjacent opposite colors r,s with outer colors a,d, both improve exactly when both initial utilities are 0, i.e. a=s and d=r; then both final utilities are 1. On C₃ the outer positions coincide, so this never occurs. On larger cycles the three edges on those four positions change from three bichromatic to one. In a mixed coloring the unchanged global color counts force at least two bichromatic edges, giving the asserted move bound. Closed walks of length n in the allowed three-bit overlap graph with a distinguished starting index biject to labeled cyclic words, counting each color once by the appended bit even for periodic words. Independently summing nonzero permutation terms of I−tT gives 1−t−zt+zt²−zt³−z²t³+z²t⁴+z³t⁶, the claimed product. At z=1 it is (1+t²)(1−t)(1−t−t²−t³). The cubic companion power sums have initial values 3,1,3; the cubic has one real root τ>1 (check the two extrema), and its conjugate pair has modulus τ^−1/2 by the unit product. This yields the exact periodic correction and asymptotic probability. A separate bit-mask check of every pair on all colorings for n=3..10 reproduced the move criterion and the nine E₈ coefficients. To replay, flip each opposite-color bit pair, compare destination utilities with origin utilities using the two-neighbor XOR, and tally stable words by bit count. The supplied verify.py was inspected but not run; the finite audit check is not the all-size proof.

## originality

PASS

Credit the exact same adjacent move rule and cyclic equilibrium language already recorded for adjacent-only monotone swaps. The surviving distinct result is the unrestricted-pair reduction for the specified open-neighborhood peaked utility, together with its exact color-weighted enumeration and law. This pass does not credit the underlying forbidden-word condition as an unprecedented combinatorial characterization or the transfer-matrix method as new.

## value

PASS

The locality result turns an unrestricted bilateral improvement game into an exactly analyzable local process and proves termination of every improvement path. The weighted census gives the number of stable assignments for each prescribed color population, not just the unweighted exponential growth rate. This is a motivated equilibrium statistic even though the local graph also arises in a different restricted game and the counting tools are standard.

The dated certificate retains the supplied scientific assessment, sources and limitations.
