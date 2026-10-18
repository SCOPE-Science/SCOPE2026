# Scientific review

## Correctness
The statement specifies connected simple cubic graphs and the stable positive-equilibrium threshold for equal symmetric competition. The Jacobian reduction proves the threshold from the least adjacency eigenvalue; positive definiteness also provides a Lyapunov proof of global attraction below threshold. Both explicit characteristic polynomials are exact. A standard-library certificate checks every labeled cubic graph on four, six, and eight vertices, the complete orbit decomposition, characteristic polynomials, the one-swap construction, and the unique reversed ordering at eight vertices. No finite experiment is extrapolated beyond the stated finite class. Risk: no behavior of nonstable solutions beyond the boundary is claimed.

## Originality
The motivating 2026 paper proves general bounds and reports positive *statistical* trends in clustering under rewiring, not universal monotonicity nor the sharp eight-vertex reversal. The known table of cubic graphs supplies its five classes, and Wagner spectral data are already established; these are treated as prior ingredients. The new combined conclusion identifies the smallest connected cubic counterexample, the exact thresholds, the unique class inversion at that order, and a single degree-preserving switch. Semantic and formulation-specific searches did not locate that compound claim; the possibility of unindexed prior computations remains a literature risk.

## Value
The recent ecological question is whether greater triangle density necessarily enhances stable coexistence when species degrees and competitive parameters are fixed. A sharp minimum-size counterexample with one local edge swap separates a statistical tendency from a structural necessity. This is a natural boundary condition on using clustering alone as a resilience proxy, rather than an arbitrary numerical graph score.

## Scope and nearest literature
Mooij et al., arXiv:2603.17584, is the closest source and uses the identical dynamical system. The 2024 Almaraz–Kalita–Langa–Soler-Toscano paper covers general Lotka–Volterra structural stability but no triangle-ordering threshold. Small cubic graphs and their spectra are prior graph-theoretic knowledge. The proof concerns exact deterministic local-stability thresholds for connected simple cubic competition graphs; average ecological trends and larger heterogeneous networks are left open.

Self-review: passed. Independent audit: not yet performed.
