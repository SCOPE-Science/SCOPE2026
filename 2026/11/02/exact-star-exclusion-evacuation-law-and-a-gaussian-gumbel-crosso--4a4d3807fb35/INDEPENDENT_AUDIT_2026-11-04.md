# Independent mathematical audit

## correctness

PASS

The finite star has independent exponential clocks and a vacant hub initially. At k remaining particles, the waiting time to visit the hub is Exp(ka), followed by a competing hub death at gamma or return to one of N-k+1 vacant leaves at total (N-k+1)b; the first-event renewal equation solves to f_k(s)=ka gamma/[s^2+s(gamma+ka+(N-k+1)b)+ka gamma]. Strong Markov renewal at each removal gives an independent product over k=1..m, each quadratic factor is a convolution of two positive exponentials because the discriminant is at least (gamma-ka)^2. Inverse rates yield mean [C_N H_m+(a-b)m]/(a gamma) and variance stated in RESULT; I reconstructed a two-state k=1 backward-equation check. For m=N a finite Gamma-product identity with v_N(s)=s(s+C_N)/(a gamma+(a-b)s) and uniform Stirling of Gamma(N+1)/Gamma(N+1+v) gives, at b_N sqrt N/a->theta finite, characteristic function exp(-t^2/2)Gamma(1-it theta)exp(-it theta gamma_E), i.e. independent Gaussian plus theta-centered-Gumbel. When b_N sqrt N/a->infinity, v_N(-it/R_N)=-it+o(1/log N) and the centered characteristic function tends to Gamma(1-it)exp(-it gamma_E), proving the full crossover. Independent small-generator and characteristic-function checks support, but do not prove, the limits.

## originality

PASS

Qualified PASS: the directed-star exclusion process Mottishaw–Waclaw–Evans studies steady-state currents, while Meerson et al study external-target survival in spatial exclusion. Hathcock–Strogatz prove Gaussian/Gumbel universality for birth–death absorption, a powerful antecedent, but do not in the inspected PRL primary paper provide this exact star-specific hub-trap product law or the critical b_N~a/sqrt N Gaussian plus independently scaled Gumbel crossover. The limits themselves and coupon-collector extreme-value laws are expressly credited; originality rests on exact finite law and nontrivial crossover for this exclusion process.

## value

PASS

The exact hypoexponential law, mean and variance for every finite N,m and rate triple solve a natural exclusion-network evacuation problem. The m=N scaling exhibits a rigorous and quantitatively located interpolation between collective central-limit fluctuations and an extreme-value bottleneck, with a genuine independent Gaussian+Gumbel law at the crossover. This is a model-specific structural result and benchmark even though the two limiting distribution families are classical.

The dated certificate retains the supplied scientific assessment, sources and limitations.
