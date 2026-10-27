# Scientific review

## Correctness — PASS
The published FREE map (equation (2.6) of arXiv:2408.13601v1) has been substituted with Hermitian weighted edge-flip jumps. Its diagonal Kraus expression yields the primitive transition matrix \(P_h=I-L\operatorname{diag}(f_h(d))\), whose stationary vector follows from exact detailed balance. A graph Laplacian null-space calculation and strict decrease of \(f_h\) prove the if-and-only-if unitality condition. The entire off-diagonal matrix-unit space decomposes into two-by-two blocks with eigenvalues \(e^{-hs_{ij}}\pm w_{ij}f_h(s_{ij})\). Their moduli are strictly less than one for connected graphs with at least three vertices, proving uniqueness of the **full quantum** fixed point. Taylor expansions about the uniform distribution give the displayed entropy coefficients. The verifier performs 109276 finite test families, which are corroboration rather than an infinite proof. The two-vertex stationary-coherence exception is stated explicitly.

## Originality — PASS, subject to independent publication-priority review
Primary full text of Chen and coauthors (arXiv:2408.13601v1, §§2–4 and conclusion) proves positivity, trace preservation and finite-time error, not the exact degree-biased global stationary state, weighted-regularity/unitality classification or entropy coefficients. Their separate second-order midpoint paper (arXiv:2506.00346v1, §3) uses a different recurrence and gives no direct covering theorem for FREE. Cao and Lu's distinct numerical Lindblad methods and ordinary reversible-Markov-chain stationary theorems were considered as possible stronger coverage. The generic detailed-balance and entropy theorems supply established ingredients; their application alone is not misrepresented as new. Targeted mathematical-record and published-finding searches found no direct same-formula implication. Specialized studies of renewal-chain embeddings or quantum unitality may contain an equivalent result, which remains a documented risk.

## Mathematical value — PASS
The formula gives the complete asymptotic equilibrium for a physically legitimate unital Lindblad model under an established positivity/trace-preserving integrator, and identifies an unconditional loss of another meaningful physical property: unitality and entropy preservation at maximal mixing. Quantified one-step fourth-order entropy loss and first-order stationary bias explain why small finite-horizon errors do not preclude long-time qualitative bias. A three-dimensional weighted path is the smallest witness, and the full quantum fixed-point theorem rules out unexamined coherences as a loophole. The result does not claim broad numerical convergence or arbitrary Lindblad structure.

## Closest literature and residual risks
- Chen et al., arXiv:2408.13601v1: exact studied numerical channel, established positivity/trace/fixed-horizon accuracy but no inspected matching invariant-state classification.
- Chen and Borzì, arXiv:2506.00346v1: later midpoint method, not FREE, no direct implication.
- Cao and Lu, arXiv:2103.01194: alternative structure-preserving method, not the exact channel analyzed.
- Classical reversible Markov chains: supplies standard detailed-balance algebra and primitivity but not the identification of the quantum integrator's graph restriction or exact entropy defect.
- Residual risk: an unlocated specialized result could derive the same graph-weighted equilibrium from embedded-jump-chain theory; publication priority requires human confirmation.

Self-review: passed. Independent audit: not yet performed.
