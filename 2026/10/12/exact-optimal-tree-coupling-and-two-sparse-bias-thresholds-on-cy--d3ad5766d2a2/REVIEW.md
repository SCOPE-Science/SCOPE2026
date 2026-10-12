# Scientific review

**Correctness — PASS.** A missing edge is exactly a cyclic \(01\) transition; counting transitions yields \(\mathbb E M=np(1-p)\), \(\Pr(M=0)=p^n+(1-p)^n\), and the single-run formula for \(\Pr(M=1)\). Every coupling incurs at least \(|M-1|\) edge disagreements; the rotation-equivariant coupling attains this exactly with the correct uniform spanning-tree marginal. Exact total variation follows from the conditional uniformity on the tree-support event. A binomial-to-Poisson argument and uniform control of all other bias regimes prove the two globally optimal asymptotic values and their different necessary scales. The checker confirms 1,936 exact finite assertions but proves no infinite assertion by itself.

**Originality — PASS, with stated residual risk.** Nachmias–Peled (arXiv:2510.19563v1) addresses determinantal local limits with degree growing to infinity; it does not contain these finite-cycle optimal transport or total-variation expressions. The later Mészáros–Peled paper (arXiv:2610.11554v1) proves an order upper bound for general graphs, not the exact cycle law, and specifies unbiased one-out choices. Frieze–Johansson addresses connectivity of other random-out models. Published mathematical-record and primary-literature comparisons revealed no implication that covers the theorem. An older cyclic-run, rotation-equivariant coupling, or random mapping result may contain an equivalent formulation.

**Value — PASS.** The exact discrepancy at bounded degree distinguishes the high-degree approximation regime from its smallest regular-degree counterpoint. Optimizing over a natural orientation bias reveals a nonzero irreducible transport error and two *different* sharp Poisson-scale optimizers for two standard probability metrics. The result explains how rare doubled-edge selections and missed edges affect optimal distributional approximation, not only an isolated finite numeric case.

The result concerns only homogeneous cycles and does not generalize the optimal coupling to arbitrary graphs.

Self-review: passed. Independent audit: not yet performed.
