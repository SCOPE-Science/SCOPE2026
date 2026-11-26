# Independent mathematical audit

## correctness

PASS

Both row denominators are 1 and the relaxation cancels the row magnitude in B, giving x'=cx+ε|x|. The sign resets, and on each of the two disjoint parity subsequences of transition indices the switch indicators are iid with mean 2p(1-p), proving the log-rate. With a=1+c, b=1-c and L=log(a/b), the rate is (log(ab)+(2p-1)^2 L)/2. Taylor expansion gives the stated sqrt(c/2) width. At either boundary, a return cycle to + has geometric length of mean 1/p, with 0 switches on an immediate return and 2 otherwise. Its average reward is log(a)/p−2(1−p)L=0, and the rewards of length 1 and 2 are distinct, with positive probabilities. The iid finite-variance LIL gives both directions of log oscillation along return epochs (up to a finite initial offset). The positive two-state transfer matrix has trace a^s and determinant p(1-p)(a^(2s)−b^(2s)); its leading root gives the claimed asymptotic with a positive prefactor. The characteristic polynomial at 1 for s=1 is c(4p(1-p)−1); at p=1/2 the other eigenvalue is c<1. For s=2 the discriminant is increasing in (2p−1)^2, so its minimum is at fair sampling. For the frontier, Hölder gives convexity of f(s)=log ρ_s, and f(s)=s log(a)+log[(1+sqrt(D+(1−D)exp(−2Ls)))/2] with D=(2p−1)^2. Hence f'(0)=γ; the function is real analytic and not affine (f'(0)<log a, whereas f(s)/s→log a). A convex analytic nonaffine function is strictly convex since an equality chord would force an affine interval. Together with growth at large s, this proves the unique threshold exactly in the strict stability window, with s*≤1 and equality iff fair. The fair absolute-error martingale has constant positive mean but zero almost-sure limit, hence cannot be uniformly integrable.

## originality

PASS

The prior algorithm, generic Perron/renewal machinery and the general possibility of pathwise stability with growing moments are not credited as new. The supported distinct result is their joint exact bias, boundary and all-order moment classification for the stated sign-reset GAVE instance. No equivalent or dominating classification was found in the inspected sources; the external search was bounded and did not settle historical priority.

## value

PASS

An exact diagnosis on an instance of a published randomized solver: sampling bias can preserve almost-sure convergence while destroying even first absolute-moment control, and neither zero-exponent boundary is stable. The exact bias scale and critical moment order specify which guarantees survive; the result is not a mere example of a known generic gap between modes of convergence.

The dated certificate retains the supplied scientific assessment, sources and limitations.
