# Scientific review

## Correctness — PASS

The stated generator and two-stage Lobatto IIIC tableau yield \(R(z)=(1-z+z^2/2)^{-1}\), verified symbolically from the Runge–Kutta stability-function identity. The transient upper-triangular block has a rational generating function whose complex-conjugate roots give an exact sine formula for every transient entry. The absorbing column equals the complementary tail of that series, and the special relation \(q=\cos\theta-\sin\theta\) reduces its sign to \(\cos(k\theta)+\sin(k\theta)\). The least integer crossing \(3\pi/4\) proves necessity for all chain lengths, not merely tested sizes. Boundaries, zero step, and strict interior signs are handled explicitly. An independent exact-rational matrix-inversion implementation checked finite cases and found no mismatch (26,022 assertion groups). Finite tests are not substituted for proof.

## Originality — PASS on checked evidence; historical overlap risk remains

The 2013 Lóczi–Ketcheson paper formalizes rational absolute monotonicity for general positivity guarantees, but does not state the exact absorbing-chain endpoint domain or its increasing-step boundary. The Higueras–Ketcheson–Kocsis work studies perturbations of methods to improve monotonicity, rather than this unmodified Lobatto IIIC map. Existing published results on Radau IIA, Gauss–Legendre/Padé \([2/2]\), and other maps concern different rational stability functions; neither a general radius of absolute monotonicity nor a small-step counterexample yields the claimed full large-step interval and all-length threshold. Public and research-record searches for aliases \([0/2]\) Padé, two-stage Lobatto IIIC, absorbing pure-birth positivity, and cotangent thresholds identified no equivalent or stronger exact claim. This is not proof of absolute historical novelty; older specialized numerical-analysis literature may remain unindexed.

## Mathematical value — PASS

The endpoint matrix is intended to represent Markov transition probabilities. Its exact nonnegative domain is a natural, operationally relevant invariant. The theorem gives a complete classification for every length and every nonnegative step, reveals a sharp four-to-five-state transition, and exhibits counterintuitive *large-step recovery* with a necessary step growing linearly in chain length. The explicit oscillatory entry formula and exact boundary zeros explain the mechanism rather than only reporting a negative numerical example. A large step may be inaccurate, so this is a positivity feasibility theorem, not a large-step accuracy recommendation.

## Closest literature, limits, and status

L. Lóczi and D. I. Ketcheson, *Rational functions with maximal radius of absolute monotonicity*, arXiv:1303.6651v1 (2013). I. Higueras, D. I. Ketcheson and T. A. Kocsis, *Optimal monotonicity-preserving perturbations of a given Runge–Kutta method*, arXiv:1505.04024v1 (2015; an updated 2018 version was also inspected). The RK tableau is standard. The claim applies only to unit-rate absorbing birth chains, unmodified two-stage Lobatto IIIC and endpoint entrywise signs. General generators, variable rates, internal stages and numerical accuracy are not covered. Historical novelty checks are best-effort and not an independent audit.

Self-review: passed. Independent audit: not yet performed.
