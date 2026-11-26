# Independent mathematical audit

## correctness

PASS

Direct Gaussian integration gives W=e^(−q²−p²)[e^(−a²)cosh(2aq)+cos(2ap)]/[π(1+e^(−a²))]; the integrated negative part has no further factor of two. Set β=acos(e^(−a²)) and t=(π−β)/(2a). Negative points have bounded position and lie in the stated momentum intervals; at q=0 a negative open region starts immediately to the right of t for every a>0. Lobes beyond the nearest symmetric pair start at |p|≥t+π/a and their total Gaussian tail is exponentially smaller. An alternative scaling p=t+as, q=√a w gives negative bracket divided by a³ tending to 2√2 s−2w² and exponential ratio tending to e^(−πs), with Jacobian a^(3/2). The exact identity for the cosine difference gives a bound C a³s, and the cosh lower bound restricts w²≤Cs; the integrand is dominated by C s e^(−cs) on that support. Integrating the parabolic positive part against e^(−πs), normalizing and accounting for both lobes gives (2^(7/4)/π³) a^(9/2)e^(−t²). The edge expansion t=π/(2a)−1/√2+O(a²) contributes both the positive 1/a exponent and e^(−1/2). Independent scaled Simpson quadrature for the nearest pair (s truncated at 17, 2048 panels, 64 position panels) gave ratios to the stated equivalent near 0.96317, 0.98295, 0.99351, 0.99681 at a=0.10,0.05,0.02,0.01; these corroborate, but do not establish, the analytic limit. The frozen checks/check_cat.py and its recorded results were inspected, not executed.

## originality

PASS

Credit only the sharp equivalent of the integrated negative part for the full even Gaussian cat. The exact Wigner formula and underlying cat normalization are prior. Neither the prior oscillatory negative-volume integral nor its proxy upper bound exhibits the exact edge-localized rate and prefactor found here.

## value

PASS

For the natural even cat approaching the vacuum the effect is nonperturbatively small. The result quantifies the mass where the fringes actually first become negative, distinguishing physical scale, secondary exponential and prefactor that a weak-amplitude expansion or logarithmic rate alone misses. The precise equivalent is a benchmark for detecting or numerically resolving negativity near the Gaussian limit.

The dated certificate retains the supplied scientific assessment, sources and limitations.
