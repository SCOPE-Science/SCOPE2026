# Independent mathematical audit

## correctness

PASS

The diagonal comparison is half-normal with variance parameter one, against n-1 mutually independent planar Gaussian norms divided by sqrt(2). Conditioning on the diagonal gives Eq. (1); polar symmetry gives 4/pi times the angular integral on [0,pi/4]. The maximizing endpoint is pi/4 below two, where the coefficient of the quadratic increment of W_q^(-2) is (2-q)/u_q^2, and zero above two, where it is 1, including q=infinity. Each contributes a half-Gaussian integral. At two the angular weight is constant. For S(x)~C x^(-beta) exp(-a x^2), inversion gives x_s~sqrt(log(1/s)/a). The half-normal Mills ratio at x_s gives the factor x_s^(beta*alpha-1), with alpha=1/(2a), and hence the stated logarithmic power. Integration by parts for U=S(|Z|), then rescaling by n, gives Gamma(alpha+1): small-s power bounds dominate the rescaled logarithm near zero, and the kernel bounds the large rescaled variable exponentially. Substitution gives the three sharp constants with the specified GUE normalization. As exact checks, at infinity S(x)=2 erfc(x)-erfc(x)^2, yielding C=2/sqrt(pi); at q=2 the binomial integral is sum_{k=0}^{n-1} (-1)^k binom(n-1,k)/sqrt(1+2k), giving 1-1/sqrt(3) at n=2. At q=1 an orthogonal rotation gives the maximum of 2n-1 exchangeable absolute standard normals, so the exact identity holds and its leading coefficient is 1/2. At any n>=2, the off-diagonal maximum decreases strictly under coupling and the independent half-normal has strictly positive density between the two distinct positive maxima, proving strict monotonicity up to infinity. The finite quadrature is supplementary; replay the independent calibrations by Eq. (1), with q=infinity using the erfc formula or q=1.5 using the angular integral, at n=200,2000,20000. The frozen verify.py was inspected, not executed. The proof is for each fixed q, not for q varying with n.

## originality

PASS

Credit is limited to the fixed-q first-pivot phase diagram beyond the already credited q=1 and q=2 cases and its coupled monotonicity. The finite-q single-competitor tail prefactors are older Gaussian-chaos results, not a new tail theorem. The closest GEPP result gives the relevant exact first-pivot statistic at the endpoints only; the Gaussian-chaos source does not treat that statistic. Applying a tail result alone, or a weak limit for the off-diagonal maximum alone, is not the sharp pivot expectation. The proof uses a separate half-normal tail inversion and a controlled regular-variation moment transfer for this comparison. No directly covering earlier pivot or two-population theorem was established in the bounded check.

## value

PASS

The pivot convention changes the no-swap probability even asymptotically: arbitrary fixed choices below two can change the polynomial power, while the exact Euclidean point and the region above it have different logarithmic orders. A common sharp leading constant for every fixed exponent above two, including the maximum norm, makes the comparison quantitative. This completes a natural norm-dependent first-step question in Gaussian pivoting beyond the known endpoints, without claiming any downstream stability or permutation result. The already known angular-tail calculations and the elementary monotonicity alone would not justify the value decision.

The dated certificate retains the supplied scientific assessment, sources and limitations.
