# Scientific review: refresh-frequency reversal in loopless SVRG

## Correctness — PASS

The recurrence is reconstructed from the pre-step snapshot rule in the original algorithm, including the independence of component sampling and the refresh coin. Exact branch averaging gives a positive second-moment map. A positive-definite test covariance \(P\) satisfies \(\mathcal T^2(P)=P-hQK/d\) with \(K\succ0\), giving an exact necessary-and-sufficient stability criterion. The proof additionally shows that the physically required common initialization becomes positive definite after at most three steps and establishes the boundary and large-step failure cases. The derivative of the positive quadratic root proves the phase inversion. The standalone rational checker passed \(1{,}710\) varied parameter cases and the exact convergence/divergence witness. The infinite-time conclusions rest on the matrix-order argument, not enumeration.

## Originality — PASS, subject to stated priority risk

The defining constant-step loopless-SVRG paper and Qian–Qu–Richtárik's arbitrary-sampling extension give sufficient convergence estimates, but their inspected algorithmic and theorem sections do not contain the sharp all-probability scalar frontier. Sebbouh and coauthors treat a **different, decreasing-step** loopless variant. A previously derived fixed-probability \(p=1/2\) frontier is **recognized as covered**, not claimed as new. The additional strict sign reversal of the admissible step limit as the refresh probability varies, including a same-stepsize stable-versus-unstable example, is not implied by that fixed-probability result. Search of indexed mathematical findings revealed no equivalent statement. Unindexed equivalent work remains a priority risk; search absence is not a proof of priority.

## Value — PASS

Snapshot-refresh probability is an essential control parameter of variance-reduced methods. The exact sign change at \(v^2=1/2\) shows that spending more gradient computation on refresh can even reduce the maximum mean-square-stable step in this pre-step-refresh algorithm. The counterexample has strictly positive component curvatures and exact rational parameters, and it distinguishes two actual convergence classifications, not merely a small constant improvement. The scope is an intentionally solvable scalar benchmark, not a claim about general optimizer performance.

## Closest literature and limitations

The closest results are the original loopless-SVRG analysis (arXiv:1901.08689), the arbitrary-sampling extension (arXiv:1906.01481), the practical variants of Sebbouh and coauthors (arXiv:1908.02725), and the covered fixed-probability scalar specialization. Only the exact dependence on \(p\) and its reversal are newly asserted. General nonquadratic convergence, noncommuting Hessians, post-step refresh, and runtime-optimal choice of \(p\) remain outside the proof.

Self-review: passed. Independent audit: not yet performed.
