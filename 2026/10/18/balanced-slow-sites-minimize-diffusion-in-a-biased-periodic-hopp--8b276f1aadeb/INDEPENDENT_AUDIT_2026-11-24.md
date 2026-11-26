# Independent mathematical audit

## correctness

PASS

The phase weights r_i/R give stationary traffic p/R and q/R per bond, so net drift is n(p-q)/R and entropy production is that value times log(p/q). For a bounded phase corrector with adjusted clockwise increments u_i, the drift equation is p u_i-q u_(i-1)=v r_i, with sum u_i=n. The squared bracket rate of the corrected martingale averages to sum u_i^2/R from any initial phase by finite-state ergodicity. The bounded correction changes variance by O(sqrt(T))+O(1), so this rate is the asserted limit. Writing P for the cyclic backward shift, (pI-qP)^(-1)=sum_(j=0)^(n-1) t^j P^j/[p(1-t^n)]. Multiplying by its transpose yields the symmetric entries (t^d+t^(n-d))/[delta(1-t^n)], since p^2(1-t^2)=delta. The constant mode gives row sum delta^(-2); subtracting it and splitting diagonal/unordered pairs yields the exact formula. The ordered k-gap spans have total kn, and strict convexity yields the integer balancing equality condition for every k. The floor increment pattern has sites ceil(jn/m)-1, which equal floor(jn/m-1/b) for b the denominator of n/m in lowest terms. Conversely the k-span conditions force all deviations x_i-in/m to lie in a range shorter than one, giving a common floor intercept. For reduced slope a/b any intercept can be shifted by an integer and by ja/b to give the same translated cyclic set, proving uniqueness including a nontrivial gcd. The energy is strictly convex in the real gap simplex by its single-gap portion, so maxima must be vertices; these are exactly one large gap and m-1 unit gaps. The hypotheses allow nonvertex placements, giving strict separation. Substitution also gives the stated illustrative rates 81/104 and 1161/1456. The strict ordering excludes p=q and q=0: the unbiased corrector is constant, and the one-way kernel has no off-diagonal contribution. Inspected the supplied verify.py and recorded finite checks, without execution; all-size correctness is analytical.

## originality

PASS

Credit only the two-sided fixed-inventory transport classification and the explicit link to a cyclic pair energy. General periodic diffusion formulas and the most-homogeneous minimization theorem are prior. In particular, the balanced minimizer and its equality class are a direct specialization of classical lattice-gas theory once the transport kernel is identified; they are not new rearrangement facts. The identified literature does not give the consecutive-block maximum and full two-sided equality classification for these transport rates. The strongest direct indexed match is later in the corpus chronology and is identified rather than used as an independent priority claim.

## value

PASS

The exact optimum at both ends and both equality classes describe how much dispersion can be changed by rearranging the same slow-site inventory while holding the drift and dissipation fixed. The strict consecutive-block maximum is not supplied by the classical ground-state result, and the exact additive transport baseline and optimizing arrangements apply to all admissible periods and positive biases. This is more than calculating the diffusion of a prescribed arrangement or reasserting the known lattice-gas minimum.

The dated certificate retains the supplied scientific assessment, sources and limitations.
