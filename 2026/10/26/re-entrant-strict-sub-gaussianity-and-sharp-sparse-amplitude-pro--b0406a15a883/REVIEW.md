# Independent mathematical audit

## correctness

PASS

The frozen finding is mathematically correct. Symmetry gives the even log-MGF and zero odd derivatives; the t→0 coefficient makes the optimal proxy at least the variance. At p_a the variance is greater than one and the fourth moment is 3/2−1/(2a^4), so the fourth cumulant is below −3/2. The +a atom gives F(p_a,a)>g(a)=a²/2−1/4−log(4a^4), with g increasing on [4,∞) and g(4)>0 using log 2<3/4. This proves the strict proxy gap at every real a≥4 and an open excluded interval by continuity at the same tilt. Near each of p=0 and p=1, the fourth t-derivative of the variance-subtracted log-MGF is strictly negative near t=0 (values −2 and −2a^4 at the endpoints), and its lower derivatives through order three vanish at t=0. Taylor control, compact strictness away from zero, and the uniform tail bound M≤exp(a|t|)<exp(t²/2) for |t|>2a give both strict neighborhoods for each fixed a. The repaired contextual rate proof is valid: M_S≤M_X≤cosh(t)M_S for the three-mass law S of the rare atom and zero elsewhere, giving a proxy difference in [0,1]. At t=2L/a with L=log(1/p_a), the positive atom gives a lower bound asymptotic to a²/(2L). On t≤L/(2a) two integrations of M_S''≤1/√2 bound the proxy by a constant; above that range maximizing 2a/t−2L/t² in 1/t and bounding the log-sum error gives an upper bound a²/(2L)+O(a²/L²). This reproduces the original rate as a comparison, not a separate contribution. The repaired prior-work statement correctly uses nonpositive rather than strictly negative fourth cumulant for the general necessary condition.

## originality

PASS

The original's separate novelty framing of the sharp proxy rate is not supported: the rate reduces up to an additive one to the existing exactly characterized symmetric sparse three-mass proxy problem, with elementary leading bounds on that established model. The prior-work prose also misstated the necessary fourth-cumulant sign as strict. The repaired claim retains the materially distinct disconnected regime for the same two-radius mixture at every a≥4, with an explicit exclusion despite fourth cumulant below −3/2. The rate is retained only as quantitative context and credited via the three-mass comparison. No claim of novelty is made for the isolated facts that a Rademacher law is strict or that the fourth cumulant alone is a local test.

## value

PASS

The repaired record gives a natural counterexample to treating strict sub-Gaussianity as a monotone or connected property of the mixing weight. For every sufficiently separated pair of radii in the stated range, it puts two open strict regimes and a quantitatively negative-cumulant failure in the very same symmetric family. The explicit excluded weight and finite-tilt witness separate local cumulant diagnostics from global proxy control; value is not assigned to restating the known sparse three-mass proxy problem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
