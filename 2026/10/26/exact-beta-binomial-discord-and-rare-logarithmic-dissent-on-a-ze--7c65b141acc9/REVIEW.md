# Scientific review

## Correctness — PASS

The finite irreducible binary voter process reduces exactly to a two-coordinate Markov chain indexed by hub opinion and number of one-followers. Its rate matrix, the cut-flux identity, hub-state balance, complement symmetry and normalization determine the claimed full stationary law. The beta-binomial factorial moments yield the mean and variance; uniform product bounds prove the rare-event probability and harmonic conditional approximation. The full infinite-size limit is analytical, not inferred from finite tests. Independently solved rational stationary systems for seven finite sizes agree exactly; see `VERIFY.py` and `certificate.json`.

## Originality — PASS (qualified bibliographic assessment)

Full primary-text comparison includes Mobilia–Petersen–Redner (2007), Yildiz et al. (2011), Acemoglu et al. (2010), Mori et al. (2018), and Vendeville et al. (2020). The most relevant possible overlap is Mori et al. Appendix B's beta-binomial distribution, which concerns complete-graph population counts rather than the pendant-zealot star with distinguished hub and its precise dependence on network size. General network duality and expectations in Yildiz et al. do not state the present joint stationary law or its conditional logarithmic rare-event distribution. Both literature and available mathematical research records were searched for star, stubborn, zealot, beta-binomial, and harmonic conditional equivalents. Prior absence is not proven; possible equivalent unpublished or differently termed formulas are a residual bibliographic risk. Independent verification remains needed.

## Mathematical value — PASS

The result solves an interpretable *full equilibrium distribution*, not merely an averaged opinion, in the simplest heterogeneous contact topology pinned by two opposing fixed agents. It distinguishes typically almost unanimous followers from the divergent variance caused by extremely rare mesoscopic disagreement episodes. The uniform law for the logarithm of disagreement size conditional on such an episode gives a quantitative distributional explanation unavailable from first moments alone; it can inform stochastic social-model simulations and model comparisons. The result is specific to its update convention and offers no empirical behavioral claim.

Self-review: passed. Independent audit: not yet performed.
