# Review of the fixed-area fragmentation threshold theorem

## Correctness — PASS

The two occupied-count transient states have generator \(Q=[[-2h,2h],[c,-(h+c)]]\), and the absorption-rate vector is \((0,h)\). Direct inversion gives \(\mathbb E[e^{-sT_2}]=2h^2/(s^2+(3h+c)s+2h^2)\), the sum-of-two-independent-exponentials law, and \(\mathbb E[T_2]=(3h+c)/(2h^2)\). The extinction-time hazard increases strictly from zero to the smaller positive characteristic root. Comparing that root with the single-reserve hazard \(m\) proves exactly one survival-curve crossing below the sharp rescue threshold and dominance above it. Coupling rescue events proves strict increase of the crossover horizon. Implicit differentiation of the smaller root and the survival equality gives the reciprocal critical divergence. The thresholds differ by \(m\). The packaged symbolic and exact-rational checks passed, including all relevant boundary cases addressed analytically. They do not replace the proofs.

## Originality — PASS, with residual literature uncertainty

The specific claim is not merely that habitat fragmentation changes persistence: Quinn and Hastings (1987) already studied short-horizon subdivision advantages, Etienne and Heesterbeek (2000) examined reserve number and size, and Nicol and Possingham (2010) compared reserve-restoration choices. Their accessible abstracts describe short-horizon effects, mean extinction time, reproduction measures and management policies rather than a strict necessary-and-sufficient single-crossing law under positive recolonization, a threshold gap exactly equal to a single-reserve extinction hazard, and the critical crossover-time divergence. Hartig and Drechsler (2008) assume an exponential quasi-stationary survival law for each species; the present initially full two-patch process has an increasing hazard and is outside that assumption. Niebuhr et al. (2015) study spatial search walks by simulations, rather than this occupancy generator. The full texts of the most relevant older reserve-design papers were not accessible, leaving a genuine risk that equivalent specialized results were overlooked. Database searches did not return a directly dominating statement, but failed or negative searches are not proof of uniqueness.

## Mathematical value — PASS

The model addresses the precise fixed-area SLOSS (single large or several small) conservation choice while allowing a rescue effect. The result gives a complete, parameter-uniform classification of fixed-horizon preference, not just a numerical example or mean formula. The constant-width rescue gap and divergence law show exactly when improving mean persistence can nevertheless worsen sufficiently late survival and how rapidly the adverse horizon moves away as rescue strengthens. This is a natural management-sensitivity question with mathematical content beyond routine moment calculation.

## Limits of review

The theorem concerns two equal halves with independent exponential local extinction and successful recolonization at a prescribed rate. It has not been established for unequal fragments, shared disturbances, area-dependent dispersal, or individually structured populations. Source access was incomplete for Quinn–Hastings (1987), Etienne–Heesterbeek (2000) and Nicol–Possingham (2010). No independent mathematical audit has been carried out.

Self-review: passed. Independent audit: not yet performed.
