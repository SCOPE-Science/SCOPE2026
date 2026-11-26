# Independent mathematical audit

## correctness

PASS

For the stated positive radial weight the monomials are orthogonal and the inverse squared norms are j−Cα j^(1−α)+Cα² j^(1−2α)−D with error O(j^(1−3α)+j^(−α)+j^(−1)). The gamma-ratio contribution to that error is O(j^(−α)), already included; the explanatory sentence at RESULT.md:80 should not be read to bound it individually by O(j^(−1)). Right-endpoint summation on j/N and the j−1 shift yield G(s)=sF1(s)+e^(−s)/2=F0(s)−e^(−s)/2. The cusp powers have bounded-variation Riemann-sum control where needed; for α>1/2 the second cusp power is integrably singular and its sum is O(N^(−2α)) after scaling. The sum of the reciprocal errors is O(N^(−3α)) for 3α<2, O(N^(−2)log N) at equality and O(N^(−2)) for that term above equality; the other errors preserve each stated remainder. These estimates are uniform on the claimed compact coordinate sets, including boundary evaluation for polynomials. The N^(−1) profiles cannot vanish identically, although their diagonal values can vanish. VERIFICATION.md and check.py are supplementary frozen numerical evidence; no script execution or formal proof check was used.

## originality

PASS

The exact finite two-point coefficients and compact-uniform remainder trichotomy for the fixed cusp-plus-linear radial family were not found in the inspected sources. The leading kernel limit and the radial reciprocal-moment technique are not new. The assessment is restricted to the subleading expansion, not a new general universality or summation principle.

## value

PASS

This gives an explicit positive radial model separating the nonlinear cusp correction from the smooth slope and discretization, including a reproducible crossover at α=1/2 and off-diagonal profiles that remain meaningful when a diagonal coefficient cancels. It is a useful quantitative test of higher-order boundary limits, not a claim about arbitrary rough weights.

The dated certificate retains the supplied scientific assessment, sources and limitations.
