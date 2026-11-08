# Independent mathematical audit

## correctness

PASS

For complete n-agent synchronous adaptive HK with one initially absent edge between extremes a<b and every other dyad receptive, initial strict confidence inequalities imply Δ=b-a<2c0. While that edge remains absent, endpoints average n-1 values each and other agents average all n; after one update the n-2 middle agents coincide and remain between the endpoints. Endpoint gap contracts exactly by 1/(n-1) each step, and the middle-to-extreme distances after updates are <Δ/n<c0, so no other edge can disappear. The missing edge confidence is c0 δ^t; thus strict receptiveness at time t is ((n-1)δ)^t>Δ/c0. If q≤1 (including δ=0 and q=1) the edge never returns; the connected fixed row-stochastic averaging map has stationary degrees (n-1,n-1,n,...,n), giving limit L=((n-1)(a+b)+n Σ_middle x_j(0))/(n²-2), with positive endpoint gap at every finite time. For q>1 the exact first repair time is floor(log(Δ/c0)/log q)+1 and at T+1 all n agents take the common full-graph mean. Independent exact-Fraction simulation tested 20 rational cases including q below/at/above one and no unexpected edge losses. The infinite statement is proved by the explicit recurrence and invariant, not finite simulation.

## originality

PASS

Li–Luo–Porter 2025 introduces the exact adaptive-confidence model, proves broad convergence/stabilization and discusses coincident opinions with missing active links. The inspected source does not give the one-missing-extreme-edge sharp δ=1/(n-1) repair threshold, exact repair time, and finite/asymptotic consensus dichotomy.

## value

PASS

Sharp repair vs permanent non-receptiveness threshold, explicit integer lifetime divergence, γ-independent switching, and finite-time versus asymptotic consensus form a motivated full parameter classification in a canonical adaptive HK subfamily. It analytically resolves a behaviour previously observed numerically and is not a cosmetic normalization check.

The dated certificate retains the supplied scientific assessment, sources and limitations.
