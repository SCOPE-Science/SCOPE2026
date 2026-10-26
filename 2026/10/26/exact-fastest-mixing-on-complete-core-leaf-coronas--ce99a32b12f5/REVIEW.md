# Self-review of exact fastest mixing on complete-core leaf coronas

## Correctness — PASS

The claim concerns all symmetric stochastic kernels on \(K_m\circ K_1\), not merely orbit-invariant kernels. Automorphism averaging is valid because the objective is the convex spectral norm of \(P-J\) and preserves feasibility. The full two-parameter spectrum has one stationary eigenvalue, one layer-contrast eigenvalue, and two further eigenvalues of multiplicity \(m-1\). The largest positive contrast eigenvalue supplies a sharp universal lower bound; its unique scalar minimizer yields the displayed weights. At those weights, algebraic inequalities place every other eigenvalue within the same modulus. The proof also handles the endpoint \(m=2\), the distinct parameter endpoints, the heuristic spectrum and the asymptotic gap. A standalone numerical implementation independently assembles transition matrices and reproduces stated checks; finite checks are corroboration, not a substitute for the proof.

## Originality — PASS, subject to the specified literature risks

The general FMMC convex formulation [1] and automorphism reduction [2] cover the methodology but do not state these exact optimum weights or the \(4/5\) spectral limit for complete-core one-leaf coronas. The closest known graph-specific comparison, Jafarizadeh [3, Section 7.4 and Appendix E], studies the same graph as a complete-cored symmetric star of arm length one. Its explicit simple-weight branch requires \((m-1)\pi_1\le\pi_0\), which becomes \(m\le2\) at uniform masses; therefore it does not provide a feasible explicit optimizer for the present \(m\ge3\) regime. It does provide a more general reduction, and a different algebraic specialization of that reduction remains a genuine residual overlap risk. published-finding corpus semantic searches identified no equivalent published claim; a negative search result is not a proof of uniqueness.

## Value — PASS

This is a standard, motivated fastest-mixing optimization on a natural dense-core/pendant-periphery topology. The exact global solution resolves the previously conditional core-size regime, identifies the active stochastic constraints (every core self-loop vanishes), and proves the unexpected constant \(4/5\) limiting SLEM. Both standard edge-weight heuristics deteriorate toward SLEM one with increasing core order, and their spectral-gap disadvantage grows asymptotically by \(m/5\). Earlier work already demonstrates unbounded disadvantages on other topologies; this report attributes novelty only to the exact corona family and its rates.

## Limits and relationship to prior literature

There is no classification of all symmetry-breaking optimizers, no result for nonuniform stationary distributions, and no independent review. The strongest prior overlap risk is the existing complete-cored symmetric-star reduction; the reviewed theorem is more explicit in the uniform-mass, \(m\ge3\) regime, but related implicit solution methods warrant independent historical checking.

[1] Boyd, Diaconis and Xiao, *Fastest Mixing Markov Chain on a Graph*, 2004, DOI: 10.1137/S0036144503423264.

[2] Boyd, Diaconis, Parrilo and Xiao, *Fastest Mixing Markov Chain on Graphs with Symmetries*, arXiv:0709.0955v1 (2007-09-06), Sections 1–5.

[3] Jafarizadeh, *Fastest Mixing Reversible Markov Chain: Clique Lifted Graphs and Subgraphs*, 2020, DOI: 10.1109/TSIPN.2020.2964211; author version arXiv:2501.02421, Section 7.4 and Appendix E.

Self-review: passed. Independent audit: not yet performed.
