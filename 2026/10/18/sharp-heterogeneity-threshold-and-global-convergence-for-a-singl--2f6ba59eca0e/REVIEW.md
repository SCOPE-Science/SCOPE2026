# Scientific review

## Correctness — PASS

All claims concern an explicitly specified deterministic continuous-time model with \(n\ge3\). Positive equilibria are in one-to-one correspondence with roots of \(L(s)=\lambda\); the derivative identity and strict monotonicity of \(E(s)\) give exactly one nondegenerate fold. Rank-one symmetric inertia gives the stable/unstable dimension, and the exact coercive potential with a strictly negative derivative outside equilibria proves global convergence, including nonhyperbolic and boundary cases. Jensen, Karamata and a differentiable envelope give the sharp heterogeneity comparison and sensitivities. The stdlib verification program passed five parameter tests, checked both branches and gradient residuals; a separate three-variable symbolic test checked the gradient identity. Computations support, but are not substituted for, the infinite-parameter proof.

## Originality — PASS, with residual risk

Landry–Restrepo (arXiv:2006.15453, model and main bifurcation sections) cover degree-distribution/link-triangle heterogeneity, not the exact individual-ratio single-hyperedge fold. Higham–de Kergorlay (arXiv:2108.05451, Theorem 5.3) give sufficient extinction conditions, not the necessary-and-sufficient two-endemic-equilibrium boundary. Kiss–Iacopini–Simon–Georgiou (arXiv:2309.12752, mean-field and bifurcation sections) treat homogeneous all-to-all simplicial systems. Liang–Cui–Liu (arXiv:2408.08602, general-order model and analytic results) is discrete-time and gives sufficient criteria. Bodó–Katona–Simon (2016, Sections 2, 5 and 6) provide model formulation, master equations and approximation rather than this threshold. Related mathematical statements include a coarse existence/support criterion for an Euler hypergraph system and a scalar homogeneous multistability construction; neither implies the exact heterogeneous threshold and global convergence. Searches of mathematical result records and relevant literature found no covering theorem. An unknown equivalent analytical result in specialized nonlinear-dynamics or epidemic literature remains possible; several more recent publisher treatments were not inspected in full.

## Value — PASS

Higher-order contagion naturally produces endemic hysteresis, but heterogeneous node responses usually obstruct complete phase diagrams. This result gives a genuinely complete classification in the smallest connected higher-order group geometry, an exact and computable critical transmission rate for arbitrary membership size, a strict general heterogeneity law under a biologically interpretable conserved geometric mean, and a Lyapunov mechanism excluding recurrent dynamics. The sharp comparison and global convergence are not merely a homogeneous scalar saddle-node rewritten with renamed parameters. Its restriction to a single all-or-nothing interaction is stated openly.

Self-review: passed. Independent audit: not yet performed.
