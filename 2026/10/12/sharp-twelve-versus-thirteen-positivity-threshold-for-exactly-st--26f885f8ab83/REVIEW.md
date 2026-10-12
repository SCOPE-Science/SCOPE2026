# Scientific review

**Correctness — PASS.** The complete-graph projectors reduce the matrix BDF2 recurrence exactly to one scalar, and nonnegativity is equivalent to the explicit interval \(-1/(m-1)\le u_k\le1\). The proof handles real stepsizes by positive/repeated-root formulas, oscillatory tail estimates, and exact low-index inequalities. The thirteen-state witness is certified by \(e^3>16\). The standalone checker confirms algebraic identities and elementary rational exponential bounds, while the analytic proof, not enumeration, supports the unbounded quantifiers.

**Originality — PASS, with stated residual risk.** Primary texts on multistep positivity and boundedness were compared at the level of their hypotheses, starting procedures and conclusions. They establish general monotonicity frameworks, not the claimed all-steps, all-stepsizes, exact-semigroup-start twelve-state complete-graph boundary. General impossibility results do not determine its minimal state count. An older symmetric-network-specific calculation under a different term could still overlap; this judgment is not a proof of global novelty.

**Value — PASS.** A-stability alone cannot guarantee a probabilistically meaningful transition matrix. The exact first-step initialization removes artifacts from a lower-order starter and leaves a natural, sharply classified family of reversible Markov diffusions: positivity holds in every time step for up to twelve states yet fails at the next state count. The result separates spectral stability from probability preservation and provides a concrete design boundary for multistep diffusion solvers.

Primary references: Hundsdorfer–Ruuth–Spiteri, *Monotonicity-preserving linear multistep methods* (CWI MAS-R0210, 2002); Hundsdorfer–Mozartova–Spijker, *Stepsize Restrictions for Boundedness and Monotonicity of Multistep Methods* (CWI, 2010); Hundsdorfer, *Partially implicit BDF2 blends for convection dominated flows* (1998). Limitation: the result is for uniform complete graphs and exact exponential starts, not arbitrary generators or starts.

Self-review: passed. Independent audit: not yet performed.
