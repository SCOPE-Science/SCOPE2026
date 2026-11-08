# Independent mathematical audit

## correctness

PASS

For 0<θ<1, R>s>0, T,P,ε>0, the sigmoid logit equation xdot=logistic(βg)−x and logistic resource n-dot=εn(1−n)((1+θ)x−1) have x*=1/(1+θ), n*(β)=(K−C/β)/D, K=R−θs,D=R+T+θ(P−s),C=(1+θ)log(1/θ). The Jacobian trace along this branch has strictly positive β slope q(1+θ)(RP+sT)/D, a negative entry trace at branch threshold and det>0; hence unique interior transversal Hopf β_h. At Hopf standard canonical linear X,Y coordinates make the first Lyapunov coefficient equal to H(ε)/16, with H=−(1+θ)(R+T+P−s)/(qD)+εβ_h n_h(1−n_h)[(1−3θ)(P−s)−(3−θ)(R+T)]. The proof computes explicit third derivatives and uses the full planar Hopf formula; environment cross derivatives G_xy matter only through g_xx=g_yy=0 in that coefficient. A fresh independent calculation differentiated the original nonlinear sigmoid/resource vector field symbolically with Sympy and substituted its canonical planar coefficient, matching H/16 to ~1e−14 for θ=.1/R=2/s=.5/T=.5/P=50 at ε=1 and30, and an θ=.8 example. The sign change at ε_c≈23.6071 is realized by admissible positive payoff matrices. Equality H=0 correctly excludes nondegenerate Hopf criticality and no Bautin conclusion is asserted.

## originality

PASS

Primary same-model source Keith Paarporn arXiv:2311.02745v1 (full eight pages inspected, p.4 and Conclusion) locates the logit environmental Hopf threshold but explicitly says sign and computation of its first Lyapunov coefficient require future analysis. The present exact evaluated H(ε) with super/subcritical switch is new relative to that result; its own statement of β>β_h periodic orbit side does not establish sign in the admitted unresolved regime. Gong et al arXiv:2205.10734 analyzes different replicator–mutator polynomial update; static logit equilibria and other environmental games do not imply the same model-specific coefficient. Search did not find covering Resultary or primary formula; unresolved older/unindexed work remains risk.

## value

PASS

The first Lyapunov coefficient is a natural decisive nonlinear invariant at a trace-zero crossing. Explicit classification of its sign and a nonempty subcritical region for changing environmental timescale resolves a clear gap left in the same logit game model, changing cycle stability/direction beyond linear Hopf location. The degenerate equality is precisely excluded from unproved higher-order claims.

The dated certificate retains the supplied scientific assessment, sources and limitations.
