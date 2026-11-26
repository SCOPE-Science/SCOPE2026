# Independent mathematical audit

## correctness

PASS

Symmetry and bounded jumps justify the cosh Lévy–Khintchine integral even with infinite Lévy activity: for fixed t its integrand is bounded by a constant times x². Dividing by Vt²/2 gives the r-average M(t) over the variance measure. Rearrangement on t<1/c, and the bound (1−1/M(t))/t≤1/t for the rest, establish the exact supremum formula including c=0. In the non-Gaussian case the objective is positive and goes to zero at both ends, so has a positive finite maximizer. For η≤μ([0,αL]), first maximize r pointwise within the lower and upper regions, then replace the lower region weight by η. Both steps can be equal simultaneously only for (1−η)δ_L+ηδ_(αL); it is the chain, not necessarily each individual inequality, that is strict otherwise. Attainment of the competing objective gives strictness of the scale; Gaussian scale zero is separately strict because η<1. The variance profile is realizable by the stated symmetric jump rates and Gaussian part when α=0. For η>0 the refined objective is pointwise strictly below the universal one, and attains its own maximum. For uniqueness, the derivative has the sign of A−B, where A=zr′ and B=r(r−1). Expansion of 2cosh(2z)−8cosh(z)+6 yields the printed B coefficients. The polynomial 4n(2n+3)(2n+4)−(n+1)(2n+5)(2n+6) is 8+(n−1)(12n²+42n+38), strictly positive for n≥1; it gives the claimed strictly decreasing coefficient ratios. In the derivative of the power-series quotient, pairing terms with exchanged indices makes every unequal-index contribution strictly negative. Therefore A/B decreases from 2 to 0 and crosses 1 once. At α=0 and ε=1−η, below (1−δ)log(1/ε) the normalized objective is negligible by r(z)−1≤z² exp(z)/12; above it the objective is at most 1/z, and at (1+δ)log(1/ε) the exponential growth of r yields the matching lower bound. The frozen checker and output were inspected, not executed. In a separate exact rational test I bounded exp(z) by its degree-68 Taylor sum and that sum plus z^69/(69!(1−z/70)), used the increasing functions (u±1/u)/2 for u≥1, and enclosed z³sinh z−z²(cosh z−1)−2(cosh z−1)² at 3.82237 and 3.82238 with signs + and −. After 60 exact-sign bisections, bounding 1/z−z/[2(cosh z−1)] over the bracket verified rounding to the printed 18 decimal places.

## originality

PASS

Credit Chen–Wang with the exact variational scale of the individual symmetric Skellam law and the general directional variational representation; the numerical universal constant is precisely their Skellam variational constant after rescaling. Credit the earlier Gaussian-noise entry with the inverse-log mechanism in the bounded one-sided setting. The distinct supported claim is the sharp class-wide two-location variance-profile envelope with equality characterization and the analytic uniqueness of the universal optimizer. The inspected Chen–Wang work explicitly does not assert interior-optimizer uniqueness, and neither it nor the inspected catalog analogues supplies this joint constrained extremal result. This is not a priority certification.

## value

PASS

At fixed actual variance, a jump cap by itself gives a uniform least scale, but the variance-share theorem answers the finer question of how much this guarantee improves when a prescribed fraction of variance comes from smaller jumps or Gaussian noise. It identifies attainable worst cases, not just a smaller valid constant, and distinguishes class-wide equality from the already known variational value for one law. The unique universal optimizer and finite nonzero maximizing argument clarify when strict MGF domination improves the optimal scale. These are substantive sharp concentration statements, not claims of tail-probability optimality.

The dated certificate retains the supplied scientific assessment, sources and limitations.
