# Independent mathematical audit

## correctness

PASS

For odd n congruent 3 mod4, the determinant-one representation count equals (1/2)r(n-2)r(n+2), so the n=11 mod20 restriction is a positive-weight subsequence of the shifted two-square convolution. Sedunova's actual level-of-distribution input has x^(1/6-epsilon), sufficient for Richert's seven-factor sieve. On the fixed 11 mod20 class, n,n-2,n+2 are coprime to 5, k|n-2 is coprime to every squarefree sieve divisor d|n with (d,10)=1; the CRT retains a unique progression modulo the fixed factor 20 times dk. The fixed prime 5 is excluded from sieving, with positive two-square local factor 1-chi4(5)/5=4/5. The new fixed-modulus progression estimate has the same exponent and summed error up to constants; Richert's positive weights and the unrestricted squarefree error estimate then give >=c x/log x of REPRESENTATIONS with omega<=7. Small exact checks for n=11,31,51,71 independently confirm representation reduction but cannot verify the analytic lower bound. Residual technical risk: the fixed-modulus uniform error and weighted-sieve constants are compressed in the package rather than reproduced line-by-line from the original analytic sieve.

## originality

PASS

Sedunova's Theorem 2 establishes an unrestricted >=x/log x lower bound for squarefree seven-almost-prime norms. This unrestricted sum could be concentrated in the other admissible mod20 classes, so does not logically imply the restricted 11 mod20 statement. Her analytic Lemma 2 and Richert argument are directly reused and must be credited: originality is limited to the positive fixed-class local factor/CRT argument, not a new sieve level, prime-factor bound or unique norm count.

## value

PASS

The class n=11 mod20 is an explicit positive local congruence class for squarefree almost-prime hyperbolic orbit representatives; proving a lower bound inside a single prescribed class is not a formal consequence of the unrestricted sieve and makes a concrete arithmetic-distribution refinement. No prime-factor improvement or general equidistribution among all classes is claimed. Value is modest and specific; extension to arbitrary admissible progressions remains open in this package.

The dated certificate retains the supplied scientific assessment, sources and limitations.
