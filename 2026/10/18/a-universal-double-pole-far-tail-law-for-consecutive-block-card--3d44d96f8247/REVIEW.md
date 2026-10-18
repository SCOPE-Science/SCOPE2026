# Scientific review: double-pole tail of the consecutive-block merger

## Correctness — PASS

The existing exact one-step transition law makes the transient chain triangular. The repeated eigenvalue is exactly \(1/2\), at sizes two and three, and the \(3\)-to-\(2\) transition is positive. The size-dependent other diagonals strictly decrease below \(11/24\). The two-by-two Jordan calculation gives \(\Pr(T_3>t)=2^{-t}(1+2t/3)\). The first-step survival recursion then yields rational coefficient recursions with positive denominators, strictly positive leading coefficient, and an exponentially smaller remainder; the finite-time \(n=4\) identity establishes sharpness of that remainder base. Rational generating functions inherit the double pole and the exponential-moment boundary. The proof covers all fixed integer sizes and time limits. Exact checker: 1237 checks, including exact enumeration of permutations through size seven and finite-state propagation through size ten. These numerical finite checks are corroboration only.

## Originality — PASS on inspected evidence, with an important access qualification

The 2023 Chern–Jiu–Simonelli manuscript establishes the merger kernel and a central-limit result as initial size grows; the inspected portions (model, theorem statements, recurrence setup and concluding proofs) do not state a fixed-size sharp far-tail decomposition, universal double spectral pole, and leading coefficient. These are not merely a reformulation of the published growing-size limit theorem. The 2016 Rao–Zhang–Huang–Cheng article addresses the same process and discusses its finite distributions, making it a particularly important historical risk. Its full text was not accessible; neither its abstract nor the separate source's citation resolves possible algebraically equivalent formulas. No claim of novelty is made for the transition kernel, general rationality of finite-state generating functions, or generic triangular-matrix theory. The exact contribution is the identified repeated mode and all-initial-size positive prefactor with sharp secondary spectral scale. Independent priority assessment is still needed.

## Value — PASS

The unusually persistent two-state-and-three-state bottleneck is not apparent from a growing-size Gaussian limit or a mean stopping-time estimate. Its \(t2^{-t}\) rather than purely geometric extreme tail determines rare long absorption times, the exact moment convergence boundary, and the sharpest universal secondary exponential among fixed initial sizes. The explicit rational recursion makes these rare-event constants calculable without numerically iterating a long-time Markov chain.

## Literature and limitations

Chern, Jiu and Simonelli, *A central limit theorem for a card shuffling problem*, arXiv:2309.08841 (2023), full-text mathematical comparison. Rao, Zhang, Huang and Cheng, *A discrete probability problem in card shuffling* (2016), DOI:10.1080/03610926.2013.834451, bibliographic/abstract material only; historical coverage uncertain. The fixed-initial-size asymptotic is not uniform in initial size.

Self-review: passed. Independent audit: not yet performed.
