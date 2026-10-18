# Scientific review: sharp logit-slope oscillation barrier

## Correctness — PASS

The proof exactly reconstructs the finite-rationality SIS–logit system and its allowed payoffs from the primary model. The weighted divergence for the strictly positive Dulac multiplier \(1/I\) is strictly negative when \(\sigma m\le4\), even at equality, so no interior cycles exist. The constructed payoffs satisfy disease-free defection dominance, produce exactly one disease-free saddle and one endemic hyperbolic repelling focus, and satisfy exact rational Jacobian identities. A low-infection barrier argument proves that every interior orbit stays uniformly away from infection extinction, while bounded logit response prevents approach to full cooperation/defection. The only interior equilibrium is repelling, so Poincaré–Bendixson gives periodic omega-limits. The accompanying checker passed 136 rational identities and 5,320 sampled inequalities; these finite checks support, but do not replace, the analytic global argument.

## Originality — PASS, residual risks documented

The motivating paper, Maitra–Paarporn–Eksin (arXiv:2610.03173v1), establishes the same ODE and develops equilibrium-existence/local-stability results and numerical dynamics, but does not derive a sharp nonoscillation slope bound or prove global periodic omega-limits for an explicit payoff family. Strong nearby mathematical literature was compared at the level of equations and conclusions. Achterberg–Sensi (doi:10.1007/s11071-023-08498-4) proves no cycles in an adaptive contact-density SIS with different behavioral equations; its all-response conclusion does not imply nonoscillation in the payoff-logit feedback, and the constructed cycles show the model classes cannot be conflated. Brett et al. (doi:10.1080/17513758.2018.1549278) prove nonoscillation for particular contagion-based behavioral systems, also structurally different. A separate published mathematical result for a Plank-type transmission-modulated SIS establishes a hyperbolic repeller and periodic omega-limits for one other model; this general technique/phenomenon is prior, not the sharp universal payoff-slope statement here. Prior logit evolutionary-game cycles (Hommes–Ochea) do not imply the two-dimensional SIS statement.

Seven direct targeted mathematical-record queries and complementary primary-literature searches were used to compare aliases, reductions, strong broader results, and local findings. No inspected work covered the combined theorem. Residual risk is unindexed equivalent analysis of the exact SIS–logit payoff model, especially contemporaneous preprints; negative search is not proof of uniqueness or originality.

## Mathematical value — PASS

This is a sharp model-wide structural threshold, including its equality boundary and constructive tightness: below the universal payoff-slope limit disease–behavior waves are impossible, whereas arbitrarily near above it sustained periodic epidemic prevalence arises from almost every interior initial state for explicit legally admissible payoffs. The explicit global periodicity mechanism gives a rigorous complement to equilibrium and short-run numerical analysis of a new model. The result is not a mere numerical test, arbitrary parameter table, or relabeling of a general theorem: the nontrivial equilibrium classification and low-infection persistence are essential to sharpness.

## Scope and uncertainty

The theorem concerns the exact deterministic homogeneous finite-rationality equations, not networks or stochastic processes. It neither proves that each parameter set above the barrier oscillates nor that the periodic orbit is unique. The logit derivative bound, classical Dulac exclusion, and Poincaré–Bendixson theorem are standard tools; novelty is the sharp combination and exact admissible SIS realization. A specialized unpublished result might duplicate the theorem. No independent validation has occurred.

Self-review: passed. Independent audit: not yet performed.
