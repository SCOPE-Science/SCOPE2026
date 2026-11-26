# Independent mathematical audit

## correctness

PASS

Split each exponential sum at k=0: for z=exp(2πiω), r=exp(-λ), the two geometric terms are exp(-λx)/(1-r/z) and z exp(-λ(1-x))/(1-rz). Combining them gives the displayed positive denominators and numerators. At z=1 the sum is strictly positive (there may be a single zero summand at c=1 on the seam). At z=-1, cancellation factors as (v-w) times a factor depending on v+w=2√q cosh(x-1/2), giving the central zero and the spatial branch exactly between c_A and c_B, with the seam and center merger endpoints. For nonreal z, real and imaginary cancellation requires proportional numerator coefficients; off the seam this reduces to (v-w)(1-q)=0, hence x=1/2, while on the seam there is only the real equation. The resulting seam and center ratios are strictly increasing in cos(2πω), by D_2-qD_1=(1-q)(1-q³); their values at -1 are c_A and c_C and at +1 are both above 1. These cases exhaust the half-open cell, giving 1,2,5,3,5. The threshold ordering follows from c_A>1/2, c_B/c_A=(1+q)/(2√q)>1 and c_C/c_B=2c_A>1; c_C<1 follows, for example, from 1/3<q<2/5 and √q>4/7. Independent bounded sampling checked the split closed form against the raw series (maximum discrepancy 8.88e-16) and the predicted roots at all three transition values and at c=0,1; the count rests on the exhaustive analytic split.

## originality

PASS

Prior Zak uniqueness for unimodal or totally positive windows covers relevant special regimes but does not cover the non-unimodal, non-TP multizero regimes. Neighboring exact classifications address compactly supported splines or asymmetric jumped exponentials, not this two-rate even difference. The bounded comparison did not locate exact coverage of the three thresholds and full-cell branch structure.

## value

PASS

This gives an explicit nonnegative decaying family in which simply giving up unimodality permits two different mechanisms that create extra zeros and an interval that loses them again. The full-cell count and exact seam, spatial and frequency branch endpoints make this a useful benchmark beyond positive-unimodal or totally positive uniqueness. Positivity alone does not explain the one-zero phenomenon.

The dated certificate retains the supplied scientific assessment, sources and limitations.
