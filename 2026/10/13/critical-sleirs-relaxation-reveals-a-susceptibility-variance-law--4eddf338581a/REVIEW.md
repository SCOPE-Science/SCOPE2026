# Self-review

## Correctness

PASS. The exact critical Lyapunov derivative has two negative susceptible-deficit squares and a nonpositive recovered term, by the Cauchy bound on the nonnegative simplex. Its only zero-derivative state is the disease-free equilibrium. The infected block has one simple zero eigenvalue and one negative eigenvalue; the stable complement decays relative to the slowly varying positive Perron infected weight. The recovered and susceptible states are stable forced filters, and the resulting \((1/W)'\) limit has the strictly positive coefficient \(K/H\). All stated componentwise and cumulative limits follow. The standalone verifier reproduces exact rational constants and a numerical late-time trajectory.

## Originality

PASS for the **complete explicit critical asymptotic vector and susceptibility-variance dependence**, not for equality-case global stability in general. The primary source only states the strict disease-free theorem. Broader differential-susceptibility references already include closed-threshold global stability and were compared at statement and implication level. The published source theorem is restricted to \(\mathcal R_0<1\) and does not state the nonhyperbolic rate. No inspected source supplies this coefficient, though terminology and access risks remain.

## Value

PASS. An explicit nonlinear critical constant determines how long asymptomatic and symptomatic burdens persist as \(t^{-1}\), and how new exposures accumulate logarithmically. Holding the mean transmission and \(\mathcal R_0\) fixed while varying susceptibility contrast yields a sharp, monotone variance law; this natural comparison cannot be answered from the usual reproduction-number threshold alone.

## Closest literature and limitations

Pan–Tang 2024 gives the target equations and strict threshold. Hyman–Li 2009 and Bonzi et al. 2011 develop heterogeneous susceptibility epidemic threshold results; Bichara 2023 proves broad equality-case global stability in a different no-waning-infection class. Accordingly, a generic equality result is not asserted to be new. The proof is deterministic, excludes infection-free initial data from its tail law, and does not provide a next-order critical expansion. Some broader literature may contain an equivalent specialized rate under other notation.

Self-review: passed. Independent audit: not yet performed.
