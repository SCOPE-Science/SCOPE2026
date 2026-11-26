# Independent mathematical audit

## correctness

PASS

Use the continuous density-quotient version of conditioning at T (not an arbitrary version of a regular conditional law on singleton points). On histories up to t<T its density is the remaining explosion-time density for N_t independent lineages divided by E′(T); the branching property makes these restrictions consistent. The power-form solution of the branching ODE gives the defective PGF and E(t); the conditional PGF is zF′_t(z(1−w))/F′_t(1−w). Normalization, the coefficient of z, the derivative at z=1 and the square-root mixture follow by substitution. For bounded s, put d=D(e^{−sw})/w. The first factor z d^{−α} is g(s)(1+j(s)w+O(w²)), while the second is [1+c(e^{bu}−1)(d^b−1)]^{α/b}. Its Taylor expansion gives the stated analytic coefficients with error O(u³+uw). Since w∼b^{1/b}u^{1/b}=o(u), mixed terms are o(u²), and comparison of w with u² gives all three regimes. At equality the two terms add and may cancel at individual (s,T); the claim is the stated locally uniform expansion, not a nonvanishing coefficient at every s. The normalized first coefficient is a difference of two gamma transforms above 1/2 and an atom-minus-gamma at equality; below 1/2 it is unbounded and cannot represent a finite signed measure. This makes no claim of a total-variation derivative. A separate 70-digit check at T=1.4 and s=0.8 verified the PGF, atom and mean identities for α=0.3,0.5,0.7. At u=0.001 the rescaled next residual divided by its predicted coefficient was respectively 0.998387, 1.000049, 1.000159, approaching 1 from u=0.01 and 0.003. The frozen verification.py and reported 453 finite checks were inspected, not rerun; the bounded computations corroborate rather than prove the expansions.

## originality

PASS

The general conditional PGF and its leading gamma limit are prior results, and the Sibuya semigroup and explosion marginal are covered by a prior theta-process representation. The supported distinct claim is the explicit conditioning-time-dependent correction, its interaction with the lattice scale, and the finite signed-measure threshold for that coefficient.

## value

PASS

The leading gamma limit erases T, whereas the first correction records it. The next term separates the scale of the lattice spacing from the analytic time scale, exposing a genuine exponent crossover. The finite-measure boundary also pinpoints where a transform correction can be interpreted as a signed measure despite mutual singularity of the finite-time and limiting laws. These refinements, rather than the explicit substitution into a known PGF, carry the value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
