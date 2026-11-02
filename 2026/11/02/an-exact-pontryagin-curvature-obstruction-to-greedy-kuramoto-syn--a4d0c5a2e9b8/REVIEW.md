# Self-review

**Correctness — PASS.** Differentiation of the squared order parameter gives exactly the Kuramoto drift coefficient \(3K/2\). Pontryagin maximization for a Euclidean ball, together with the adjoint equation, forces Hessian-gradient collinearity on an optimal greedy arc. The nonzero exact cross product at a regular state contradicts that necessity. The strict inequality follows from existence of a minimizing control. The real-analytic zero-set principle turns the explicit witness into an open dense statement. The packaged symbolic identities were rerun and passed.

**Originality — PASS under inspected evidence.** The primary 2026 work explicitly reports numerical greedy suboptimality and qualitatively anticipates generic failure; neither observation is claimed here as a discovery. Its analysis does not state or prove this exact Pontryagin collinearity obstruction, explicit radical witness, or the parameter-uniform open-dense local-target theorem. Closest mathematical database records concern phase-locking stability or unrelated optimization, not minimum-time Kuramoto curvature. Priority risk persists for general optimal-control literature, where the maximum principle itself is standard.

**Mathematical value — PASS.** This resolves an exact structural issue behind numerical evidence: greedy ascent fails the necessary extremal equations at nearly every three-oscillator configuration, irrespective of coupling and available power. The theorem offers a cheap analytical diagnostic before applying dynamic programming, without asserting a fully optimized policy or a quantitative time gain.

**Literature boundaries.** O'Keeffe, arXiv:2608.10354v1, Sections II, III and VII, already has the source model, HJB formulation, exact gradient-flow identity, dynamic-programming comparisons, and informal geometric interpretation. Pontryagin conditions are standard and do not establish originality independently. This result is limited to nearby target thresholds and N=3.

Self-review: passed. Independent audit: not yet performed.
