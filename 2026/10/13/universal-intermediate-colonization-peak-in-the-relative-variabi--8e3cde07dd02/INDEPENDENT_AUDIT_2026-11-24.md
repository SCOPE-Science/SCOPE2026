# Independent mathematical audit

## correctness

PASS

For the finite transient generator Q, the first two raw moments solve (-Q)m=1 and (-Q)s=2m; invertibility holds also at zero colonization. Differentiating the singleton equations with pair moments 3/(2 mu) and 7/(2 mu^2) gives m'=deg(v)/(2 mu^2), s'=5 deg(v)/(2 mu^3) and CV^2 slope deg(v)/(2 mu). For the high-rate check, from any proper nonempty set, each next event is a birth with probability at least lambda/(lambda+n mu); a block of at most n-1 births fills the graph. The jump count to full or empty is dominated by a fixed-size block times a geometric variable, and, conditional on the jump path, all holding rates are at least lambda. The entrance-time second moment is O(lambda^-2), and the probability of missing full occupancy is O(lambda^-1). With cycle length X and extinction mark Z of probability e, the recursions give mean E[X]/e and second moment E[X^2]/e+2 E[X] E[X;Z=0]/e^2. E[X] stays bounded below by the full-state holding mean; E[X^2] stays bounded, so the missing contribution E[X;Z=1] tends to zero. Decomposing the singleton extinction time at the first hit of full or empty transfers both normalized moments, not just a distributional limit. Continuity and a positive initial slope now imply finite interior attainment, not uniqueness. In the two-state chain in units mu=1, m1=1+r/2 and s1=2+5r/2+r^2/2 give the stated profile and unique maximum. Replay: RESULT.md lines 25–85; verify_extinction_cv.py lines 24–50 and 66–104 were inspected, not executed. Its finite exact checks do not certify the high-rate or all-graph statement.

## originality

PASS

Pass the combined fixed-graph singleton theorem: the exact initial slope and the resulting interior CV-squared maximum. Do not credit the high-rate exponential/renewal mechanism by itself as new. The closest catalogue result studies the same moment ratio at high rates from full occupancy; the matching two-patch computation is an elementary illustration and not the sole basis of the pass.

## value

PASS

There is a natural distinction between how long extinction takes on average and the relative dispersion of durations. The sign of the exact, degree-dependent weak-colonization response and the return to the exponential benchmark force an interior amplification on every connected finite landscape, without relying on a graph census or selected simulations. The two-site maximum is a usable normalization witness, not a claimed all-graph bound.

The dated certificate retains the supplied scientific assessment, sources and limitations.
