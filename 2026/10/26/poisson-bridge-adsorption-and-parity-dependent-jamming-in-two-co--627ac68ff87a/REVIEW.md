# Independent mathematical audit

## correctness

PASS

The three-state vacant-pair Markov process (a,b,c) has internal event rates binom(a,2), binom(b,2) and cross intensity λc; every successful bridge removes one vacancy in each clique. At absorption each complete clique has at most one vacancy, so U=2*1_{M≠n mod 2} exactly. Under time u=nt, scaled drifts converge uniformly on bounded intervals to x=y=(1+u)^(−1), z=(1+u)^(−2) and cross intensity λz. The process time-change gives Poisson(λT/(1+T)) up to u=T. The nonnegative potential Φ=c/a+c/b with Φ=0 when c=0 satisfies L[max(1,λ) Φ]≤−λc, including a=b=1 and λ=0 boundaries. Uniform tail expectation ≤2max(1,λ)/(1+T) closes the full-time limit; taking parity yields P(U=2)=(1−(−1)^n e^(−2λ))/2+o(1). Independently recomputed exactly with rational arithmetic 3,135 potential-generator cases for a,b≤11 and λ∈{0,1/3,1,3,8}, all inequalities held. A bounded check cannot prove the fluid limit or all-state inequality; their algebraic arguments were reconstructed separately.

## originality

PASS

Best-of-knowledge PASS for the specific fixed-λ rare-bridge Poisson law and order-one alternating defect in edge-priority adsorption on K_n Cartesian K_2. Known random sequential adsorption/matching theory motivates the model but the inspected path-coverage, vertex-greedy, or sparse-graph results do not state or imply this count. Full Dyer–Frieze paper inaccessible remains significant priority uncertainty.

## value

PASS

Exact asymptotic rare-event law plus a finite-n parity identity explain how n paired bridge edges among Θ(n²) edges produce a persistent alternating jamming effect. These are natural random-greedy matching observables, with a substantive late-time tail lemma rather than a cosmetic variant of coverage density.

The dated certificate retains the supplied scientific assessment, sources and limitations.
