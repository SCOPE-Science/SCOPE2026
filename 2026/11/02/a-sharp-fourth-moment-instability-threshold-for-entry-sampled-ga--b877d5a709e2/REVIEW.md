# Self-review

## Correctness — PASS

The update matches Algorithm 1 of arXiv:1810.05251 and the entrywise specialization of arXiv:1912.13291. Exact normalization gives \(\|A_r\|_F^2=2(1+r^2)\), probabilities summing to one, invertible update matrices, and a scalar second-moment contraction of \(3/4\). A symbolic fourth-degree expansion produces the stated three-dimensional invariant transfer matrix. An order-preserving polynomial-map fixed point and the absence of a common eigenline of two constituent updates give a positive-definite eigenquartic; this is what justifies applying the leading spectral value to every nonzero initial vector, rather than merely reporting a matrix eigenvalue. The unique root of \(\det(I-C_r)\) and endpoint tests prove the sharp classification. The packaged verifier checks the algebra and 36 exact finite-history identities. No simulation is used as a substitute for the proof.

## Originality — PASS (qualified best-knowledge assessment)

Closest primary sources are Razaviyayn–Hong–Reyhanian–Luo (arXiv:1810.05251), Du–Sun (arXiv:1912.13291; arXiv:2011.10353), and Han–Xie (arXiv:2208.05437). Their relevant developments concern the same sampling rule or more general methods but give mean and/or second-moment estimates. Such estimates do not imply decay of the fourth moment; here the latter can grow. Targeted comparisons of fourth moments, higher moments, equivalent entrywise stochastic updates, and orthogonal coefficient matrices did not identify the exact quartic transfer or the polynomial threshold. The method, second-moment bound type, and positive-operator tools are established prior art. An earlier higher-moment random-product treatment under different terminology remains a risk; this is not independent priority certification.

## Value — PASS

The coefficient matrix has spectral condition number exactly one throughout, yet the fourth moment changes from exponential decay to exponential growth at a nontrivial exact algebraic boundary, while almost-sure and mean-square convergence remain unaffected. A rare update with small coefficient can have very large conditional fourth power even though importance weighting controls the second moment. This provides a motivated reliability counterexample for entrywise randomized linear solvers and a contrast with row Kaczmarz, whose fourth moment decays on the identical system. The result is confined to the stated family and sampling prescription.

Self-review: passed. Independent audit: not yet performed.
