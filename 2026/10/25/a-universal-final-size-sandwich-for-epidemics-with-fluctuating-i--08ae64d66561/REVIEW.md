# Independent mathematical audit

## correctness

PASS

For closed deterministic mean-field SIR with exogenous bounded measurable susceptibility paths b(t), shared stationary one-time marginal nu, S0,I0,gamma>0, solve the Volterra survival S(t)=S0 E exp(-int_0^t b(u)I(u)du). The integral pressure z=int_0^infty I(t)dt is positive finite, and mass balance gamma z=I0+S0-S_infty. The density w(t)=I(t)/z defines risk-path weighted mean C=int b(t)w(t)dt. Conditional Jensen over an independent w-distributed time U and ordinary Jensen give exp(-mean(nu)z)<=E exp(-zC)<=E_nu exp(-bz), since b(U) has law nu. The strictly convex final-size residual functions F_q(v)=gamma v-I0-S0+S0q(v) each have one positive root. Their signs at actual z force frozen z_nu<=z<=homogeneous z_hom, hence same inequalities for Z=gamma z. No Markov or time-independence assumed. Independently solved benchmark scalar roots 0.5032405991518699 and 0.715565435681715 for source sample parameters; this bounded check cannot replace Jensen argument.

## originality

PASS

The relevant 2023 primary diffusion-risk epidemic article establishes a restricted comparison of its Gaussian risk model in a no-diffusion setting; this does not quantify over arbitrary bounded stationary-marginal exogenous path laws or give the exact frozen-risk lower and homogeneous upper bound for one shared marginal. Classical permanent heterogeneity gives a benchmark, not arbitrary dynamic turnover ordering. Could be an implicit known Feynman–Kac Jensen theorem, retained as explicit risk.

## value

PASS

A distribution-free final-attack-size ordering isolating persistence versus temporal turnover of individual susceptibility is a mathematically motivated epidemiological principle. It handles all temporal correlations in one argument while preserving endogenous infection pressure, and supplies a useful sharp bracket without solving stochastic dynamics.

The dated certificate retains the supplied scientific assessment, sources and limitations.
