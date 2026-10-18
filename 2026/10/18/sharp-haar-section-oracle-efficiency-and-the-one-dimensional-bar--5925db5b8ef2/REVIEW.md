# Scientific assessment

**Correctness — PASS.** The exact norm-increment identity converts the expected section ratio into a squared-projected-norm increment. A Fourier/Parseval chord inequality bounds its circle-averaged increment by rotationally invariant derivative energy. Conditional Haar isotropy gives the derivative energy exactly as \((n-d)/(n(n-1))\), yielding the claimed coefficient; dominated convergence proves sharpness. A separate angular integration establishes the \(d=1\) law and the geometric first-improvement waiting time. All boundary cases \(n=2\), \(d=1\), \(d=n\), and antipodal vectors are covered. The accompanying code provides corroborative, not infinite, checks.

**Originality — PASS, with uncertainty.** The 2026 motivating paper defines the same efficiency and proves the useful exact norm identity, but its Proposition 1 supplies a larger correction term (factor four rather than one), its Proposition 7 gives a positive lower bound 96 times smaller, and its principal bounds do not cover \(d=1\). No matching sharp constant or rank-one angular law was identified in the other inspected records. A Haar stochastic-subspace descent result concerns a different optimization oracle. Bibliographic indexing is incomplete; rediscovery elsewhere is possible.

**Value — PASS.** The theorem determines the exact best possible uniform gap-retention constant for an entire natural class of Haar section oracles, extends the analysis to all legal section dimensions, and identifies a sharp structural distinction between random lines and sections of dimension at least two. It improves dimension-explicit constants used in a recent projection-free optimization analysis and quantifies the one-dimensional obstruction rather than merely observing it.

**Scope and residual risks.** This is a boundary-ball expected-oracle theorem, not a universal convergence guarantee on general feasible sets. The first-improvement calculation is local to a linear objective and one exact line-oracle step. Independent bibliographic audit remains outstanding.

Self-review: passed. Independent audit: not yet performed.
