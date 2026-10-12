# Scientific review

## Correctness — PASS

The proof is analytic for every integer \(n\ge3\), every positive real rate vector, every \(\theta\in[0,1]\), and every positive stepsize. Cyclic factorization gives a strictly positive resolvent and exact diagonal \(F_j(a)=(1-q_j)/(1-\prod_kq_k)\). A product inequality proves that each diagonal decreases strictly to its stationary mass. Hence one and only one finite cutoff occurs below \(\theta_c=1-\pi_{\min}\), with none at or above it. The second-order reciprocal-step expansion proves the nonzero critical divergence coefficient. Exact rational matrix checks reconstruct the step independently for thousands of finite instances; no infinite conclusion relies on the finite checks.

## Originality — PASS, with specific residual risks

The closest fully inspected classical primary source is Z. Horváth, “On the positivity step size threshold of Runge–Kutta methods,” DOI 10.1016/j.apnum.2004.08.026 (available online 27 October 2004). Its universal positive-IVP step restrictions and invariant-positive-set construction do not specify directed cycle resolvent diagonals, arbitrary heterogeneous rates, or a threshold expressed by the smallest stationary mass. The 2023 full text by Higueras and Roldán uses a symmetric Dirichlet heat-grid generator and different dimension-dependent positivity polynomials. The complete 2016 arXiv study by Horváth, Song, and Terlaky addresses general set invariance rather than this exact family. Published results for the two-stage Padé map and a filtered Crank–Nicolson map solve different operator problems, and the existing two-state \(\theta\) and resolvent tests do not imply the rate-cycle scalar cutoff or its critical scaling without the new cycle calculation.

The search is not a proof that no equivalent result exists. Older general positivity and Markov-chain numerics may contain an unlocated special-case formula; arbitrary-generator extension and independence are not asserted.

## Value — PASS

Probability preservation is a fundamental design constraint when integrating Markov master equations. The theorem resolves the entire positive-rate directed-cycle family in every dimension at every stepsize, replacing a conservative fastest-rate restriction by the sharp stationary-mass threshold. The nontrivial boundary \(\theta_c\), unique crossing below it, and exact critical blowup distinguish genuinely unconditionally stochastic discretizations from merely stable ones. Heterogeneous jump rates matter: the threshold depends on the stationary distribution while the first finite-step failure occurs exactly at fastest-rate states.

## Independent validation status

Self-review: passed. Independent audit: not yet performed.
