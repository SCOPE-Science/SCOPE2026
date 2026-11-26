# Independent mathematical audit

## correctness

PASS

The claim concerns total runs, not 1-runs, at a stationary start with fixed interior a,b and s_n/n tending to an interior rho. For 2s runs the two endpoint orientations have equal weights since pi_0 a = pi_1 b. Adding one zero or one one block gives the two terms of the affine joint-weight ratio T. Both laws have the full interval [s,n-s] as support when n >= 2s+1; the tilt is strictly positive there. Normalizing the affine tilt gives the exact TV identity |slope| times the null law's mean absolute deviation divided by twice its mean tilt. For the even-run law the entropy derivative is the log of q u(1-u-rho)/((u-rho)(1-u)); it decreases from +infinity to -infinity and its negative derivative at the root is sigma^{-2}. Centering at the moving saddle x_n for rho_n=s_n/n is necessary (there is no assumed convergence rate). The log adjacent-weight ratio differs from the corresponding entropy derivative by O(1/n) on a fixed interior neighborhood, with decrement bounded above by -c/n there. Central Stirling expansion, a Gaussian bound in that neighborhood and exponential tails beyond it give the normalized Gaussian limit and uniform integrability of its centered fluctuations. Thus the absolute-deviation coefficient is sigma sqrt(2/pi) and the mean tilt tends to t>0. The slope numerator factors as (a-b)(1-a-b), so the finite laws coincide exactly on the two stated curves; there are at least two support points even at n=2s+1. Independent standard-library replays `python3 record3_exact_check.py` and `python3 record3_asymptotic_check.py` corroborated the proof: 600 exact comparisons for n=3 through 10 across four rational parameter pairs and, for (.2,.4,.2), a scaled TV of 0.136569648 at n=10000 against 0.136568554 predicted. These are finite spot checks, not a limit proof; the supplied checker was inspected rather than run.

## originality

PASS

Credit the prior exact bivariate law and its immediate affine-ratio and equality consequences. The distinct claim supported here is the sharp adjacent-total-run conditional TV asymptotic, with its explicit rate coefficient. The primary and indexed comparisons did not establish it or a dominating specialization. This is a best-of-knowledge conclusion, not a priority certificate.

## value

PASS

The adjacent parity classes have the same leading conditional Gaussian shape, so a CLT or TV convergence to zero does not quantify their distinguishability. The sharp coefficient measures that loss and separates exact finite indistinguishability (two distinct mechanisms) from nonzero n^{-1/2} separation. This is a natural conditional comparison across all fixed interior run densities, not just a selected parameter example. It does not assert uniformity toward boundary densities or transition probabilities.

The dated certificate retains the supplied scientific assessment, sources and limitations.
