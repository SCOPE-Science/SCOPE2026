# Self-review

## Correctness — PASS
The three-qubit Ising triangle has ground energy \(-1\) with six ground basis vectors. In product states, the identity \(1+\sum_{i<j}z_iz_j=4\Pr(B_1=B_2=B_3)\) is exact for independent Bernoulli signs with means \(z_i\). Equality requires two pinned opposite \(Z\) eigenstates, leaving at most unit total transverse \(X\) expectation. Convex mixtures yield the necessary \(c\le1/3\), and a cyclic-and-global-flip twirl of \(\rho_+\otimes\rho_-\otimes(I+3cX)/2\) saturates it for the entire interval. Quantum states of energy \(-1\) live on six configurations; the compressed \(\sum X_j\) is the adjacency of \(C_6\), whose largest eigenvalue is \(2\), giving \(c\le2/3\). The uniform coherent ground vector and its mixture with the incoherent ground ensemble saturate all allowed values. The code independently checks exact finite matrices and rational witnesses, while the proof covers the continuous parameter interval.

## Originality — PASS, with explicit residual risk
The full text (main statements and supplemental SM7) of arXiv:2605.03022v1 was inspected. It develops general fixed-marginal separable-energy bounds and ferromagnetic/two-colorable saturation and discusses an antiferromagnetic symmetric-spin problem, but does not give the frustrated triangle's paired sharp \(1/3,2/3\) feasibility thresholds. The earlier energy-witness paper and related transverse-field Ising approximation work address broader but different questions; indexed records and pertinent previously recorded claims show no direct equivalent or stronger result. A specialized unindexed calculation or implicit corollary may exist: negative search evidence does not prove priority, and independent audit is needed before publication.

## Value — PASS
This identifies an exact boundary of the physically natural fixed-single-qubit-marginal extension of a recent separable-energy framework on the smallest frustrated non-two-colorable graph. Unlike a routine unconstrained ground-state observation, it separates classically correlated mixtures from coherent quantum ground-space states using both measured local transverse coherence and total energy. The open interval \(1/3<c\le2/3\) is a sharp entanglement-certification region, with explicit feasible states on both sides and both endpoints. The small size is intrinsic to the first frustrated cycle; the claimed value is the natural sharp local-marginal cutoff, not an unsupported generalization.

## Boundaries and priority risk
The result concerns fully separable versus unrestricted quantum feasibility at the exact ground energy only. No claim is made about entanglement depth, noisy robust certification, or arbitrary energy values. The closest research is the fixed-marginal optimization framework of Tóth–Pitrik; independent external scrutiny of specialized earlier studies remains necessary.

Self-review: passed. Independent audit: not yet performed.
