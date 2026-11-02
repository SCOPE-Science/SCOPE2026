# Scientific review

## Correctness — PASS

The code mechanism and every random weight are specified, including the zero-derivative absorbing branch. Independent sibling subtrees give the exact positive second-moment renewal equations. Their Riccati first integral yields an explicit double-pole solution and an integrated first-order pole for the actual initial-coordinate estimator. The rate optimization has a single interior maximum. The positive-tree construction supports monotone truncations and rules out moment reentry after singularity. The independent code verifier performs numerical ODE integration and 80,000 direct tree draws; it is supplementary to, not a substitute for, the proof.

## Originality — PASS, qualified

The original coding-tree mechanism, expectation representation and small-time Riccati experiment belong to Penent–Privault, arXiv:2201.05998; the only new claim is a sharp L2 horizon and its constant-rate optimum. Its Section 4 gives sufficient L1 conditions, not the squared-weight moment threshold derived here. Huang–Privault, arXiv:2404.05969, also studies second moments but for a separate random-tree-size algorithm without exponential branching clocks; the variance-bound optimization there does not cover this exact estimator. Henry-Labordère et al., arXiv:1603.01727, establish general branching diffusion representations and maturity restrictions for semilinear PDEs, not this exact scalar marked-code moment system. Semantic record searches with equivalent and numerical formulations found no direct equivalent among retrieved records, not a proof of global novelty. Specialized classical marked branching literature remains a priority risk.

## Value — PASS

The estimator is used to numerically represent ODE solutions, and variance determines whether ordinary sample averages admit the usual finite-variance Monte Carlo error analysis. Establishing a strict, optimal clock-rate horizon disambiguates mean integrability from numerical uncertainty: at positive times where the Riccati solution is smooth and the expected tree size is finite, every constant-rate exponential coding-tree estimator still has infinite variance. The exact pole also quantifies how rapidly the uncertainty deteriorates on approach to the horizon.

## Limitations and nearest literature

The global optimization is only over fixed exponential clock rates, not general lifetime distributions, other tree sampling algorithms, or general nonlinear ODEs. Rare-event simulations cannot establish failure of L2 integrability. Earliest underlying source is the January 16, 2022 arXiv posting of Penent–Privault. Exact priority beyond the inspected papers is not independently certified.

Self-review: passed. Independent audit: not yet performed.
