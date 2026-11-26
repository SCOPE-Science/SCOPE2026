# Independent mathematical audit

## correctness

PASS

Checked the killed Brownian resolvent by its boundary values, continuity, and derivative jump −2 for generator (1/2)∂². Integration over the full interval gives the mean duration of one attempt; integrating over the safe interval and multiplying by the alarm rate gives the probability of a fresh attempt. This probability is strictly below one because an attempt can exit before its alarm. The renewal quotient gives the stated mean with the cosh((L−a)sqrt(2r)) denominator and the no-alarm limit L². As a separate all-rate check, put c=1−a/L and y=L sqrt(2r). The numerator 2(cosh(y)−1)/y² is the moment-generating function of the sum X of two independent uniform variables on [−1/2,1/2]. By symmetry it equals E cosh(y sqrt(X²)). The function s↦cosh(y sqrt(s)) is strictly convex for y>0 by its power series, and E X²=1/6; strict Jensen proves that the numerator exceeds cosh(y/sqrt(6)) at all positive y. Above the critical c the coefficient of y² is negative in the ratio, providing an improving rate. For 0<a<L the mean diverges at high rate, giving an attained positive optimum in the improving regime. At a=0 positivity at every finite rate and asymptotic 1/r give an unattained zero infimum; a=L is in the never-beneficial regime. With z=y² and delta=c²−1/6 the expansion is 1−delta*z/2+(7/4320)z²+O(|delta|z²+z³); the quadratic coefficient follows also from E X⁴=1/15. Uniform high-rate growth near critical c and strict inequality at delta=0 for z>0 imply that all global minimizers converge to z=0. The stationary equation there has one branch by the implicit-function theorem, positive for small delta>0, with z=(1080/7)delta+O(delta²); converting time and substituting gives both claimed coefficients. The frozen finite-difference script was inspected, not executed; its recorded 157 checks are only corroborative. The exact argument requires no numerical optimization.

## originality

PASS

The winding model of Grange gives the same process, mean, and a numerical optimizer at the fixed ratio a/L=1/2, and ordinary resetting covers the centered all-safe endpoint. The supported distinct content is the variable-radius policy’s exact all-rate threshold, strict critical case and unique near-onset optimizer with its rate and gain laws. Other published and indexed threshold results use different control parameters or stopping rules.

## value

PASS

Varying the fixed safe-zone radius generalizes the winding policy in a way that poses a genuine control question: for which spatial policies can any positive alarm rate help? The strict global boundary rules out beneficial large rates when local perturbation alone cannot do so, and the onset laws quantify both the optimizing rate and the initially small gain. This is useful as an exact benchmark under the stated instantaneous, symmetric dynamics; it does not assert physical implementability, optimization over the cutoff itself, or global uniqueness far from threshold.

The dated certificate retains the supplied scientific assessment, sources and limitations.
