# Independent mathematical audit

## correctness

PASS

At pinned RESULT.md, the seed coordinate is fixed at 1 because k=1 and mu>0. Symmetric unseeded coordinates satisfy xdot=min(1−x, x²+((n−2)gamma−2sqrt(gamma tau))x+gamma). Exact identity q=(x−sqrt(gamma))²+2sqrt(gamma)(sqrt(tau_c)−sqrt(tau))x yields global cascade for tau<tau_c; at equality x(t)=gamma t/(1+sqrt(gamma)t), and above equality the smaller positive root traps the orbit. Discrete strict LTM activates iff tau<1. At tau=1 fixed n>=3, q=(x−B)²+D², D~sqrt(n−2)gamma^(3/4), both arctangents tend to pi/2, proving T_(1/2)~pi gamma^(−3/4)/sqrt(n−2). Boundary n=2 and gamma domain verified. The finite verify.py tests only consistency, not infinite parameters.

## originality

PASS

Compared exact clipped NOD and strict LTM to the founding 2026 preprint: its Theorem 2 explicitly assumes no binary neighbor sum equals its threshold. At the exact one-seed tie its conclusion does not apply. Other continuous sigmoid cascades, generic saddle-node ghost laws, and discrete conversion-set counts neither specify the same update nor entail the present sharp all-gamma network boundary plus coefficient. Unindexed same-model expansions remain possible.

## value

PASS

A sharp, all-parameter delineation of when a standard continuous contagion relaxation disagrees with strict binary contagion precisely at an excluded hypothesis boundary, including a critical trajectory and exact singular first-passage clock. Important for interpreting apparent versus actual cascades and finite observational horizons; not merely a normal-form restatement.

The dated certificate retains the supplied scientific assessment, sources and limitations.
