# Independent mathematical audit

## correctness

PASS

Unit-mass positivity allows the normalization 0≤f≤1, and optimizing a difference of two evaluations gives half the L1 difference of their kernel densities with respect to normalized Haar measure. Continuous functions approximate the density sign test in this pairing; the location-pair maximum exists by continuity. For n=2 the coefficient at separation 2 arccos c is 2√(1−c²)/π. For n=3, after factoring the kernel difference and integrating in cos z, it is 4√(1−c²)/(3π) times 2 for c≤1/2 and times 2c+1/(2c) for c>1/2. The squared comparison on the second interval reduces to the positive product (1+c(2c−1)²)(4c³+4c²+c−1), so both orders have unique antipodal separation. At n=4 the two linear factors of the polynomial in cos z give a first interior root for 0<c<2/3, then two roots with order reversed at 1/√2. I independently integrated the three signed pieces and differentiated (1−c²)I(c)². On the first piece the derivative has the sign of the stated quintic for c>0, because the quartic factor is strictly negative there. An exact root count confirmed one quintic zero in (0,2/3); exact polynomial root exclusion and a negative sign test on rational supersets certify that both later pieces strictly decrease. The continuous pieces join at their endpoints. The maximum is therefore unique, at c=0.338107185334655885947…; separation 2.451782841069227906928… and sharp coefficient 0.883882377829196849049…. At c=0 the coefficient is 8/(3π), strictly smaller.

## originality

PASS

The abstract contraction formula and the Fourier kernel representation are established. The distinct result is the evaluated n=4 coefficient, with global proof and a uniquely non-antipodal separation after checking the two smaller nonconstant orders. The closest actual statements inspected concern Lipschitz contraction, two-harmonic BV contraction, or the abstract TV variational reduction; none gives this three-harmonic maximum.

## value

PASS

The exact operator contraction quotient measures worst-case oscillation loss for a canonical positive Fourier summation method. Antipodal pairs suffice in the first two nonconstant cases, then provably fail at the third, so the choice of n=4 captures a structural change rather than an arbitrary order. The exact coefficient and unique separation quantify this failure with a global bound that the abstract contraction formula and sample numerics do not supply.

The dated certificate retains the supplied scientific assessment, sources and limitations.
