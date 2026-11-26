# Independent mathematical audit

## correctness

PASS

Normalize the support to 0,t,1. The minimum and maximum are linear combinations with weights t,1-t of two nested threshold indicators each. The four cross covariances are ab, b²−a, a², ab, giving D+Fw at w=t(1−t), where D=ab and F=(b−a)²−a. The variance product has coefficients AB, L=−4AB+2C(A+B), K=(A+B−2C)². Exact polynomial coefficient arithmetic confirmed the frozen identities for the derivative factor at 0 and 1/4. At 0 the factor after extracting 2ab(1−b) is at least 3b²/16. At 1/4 the frozen bound using a/b²≤9/16 gives a positive factor because 81b³−369b²+127b+80≥80−37b>0 when b≤4/9. The derivative factor is affine, so it is strictly positive throughout. F≥0 even at n=2, where F=0 and the covariance is still positive. The positive variances and w≤1/4 with equality only at t=1/2 prove the strict maximum. Evaluation there gives the stated formula and the values 8/19 and 1/4 at n=2 and 3.

## originality

PASS

The new content supported by the comparison is strict support-location optimality for n≥3, not the n=2 optimizer or the evaluation of the correlation at the midpoint. No available prior result inspected settles the n≥3 location optimization with equal masses.

## value

PASS

The fixed-equal-mass problem is the natural location analogue of the two-draw discrete extremum. Three points are the first support with an adjustable gap ratio. Proving strict optimality at every sample size, including where changing masses can improve upon uniformity, resolves that first variable-gap problem and distinguishes the two optimization regimes. The value is in the global location comparison and equality criterion, not in reevaluating the known midpoint formula.

The dated certificate retains the supplied scientific assessment, sources and limitations.
