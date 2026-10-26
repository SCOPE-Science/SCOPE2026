# Scientific review

## Correctness — PASS

For every \(n\ge3\) and \(0<\delta<1\), the SPD potential \(H=(1-\delta)I+\delta\mathbf1\mathbf1^\top\) keeps trajectories within the stated open ellipsoid and all best responses unclipped. Averaging the exact selected-coordinate updates yields the displayed two-by-two moment transition, with strictly positive determinant and Perron eigenvalue below one. The coefficient of that mode is strictly positive for every nonzero perturbation. Symbolic expansions yield both slowdown coefficients. The included checker performs 145 consistent finite assertions over 14,744 update strings; it is corroborative, not a substitute for proof.

## Originality — PASS (subject to publication-priority risk)

The full text of Misiak–Dziubiński (arXiv:2602.15986, Sections 2, 3.2.2, and stability proof) analyzes exactly the motivating game and random update mechanism, but provides stability and convergence observations rather than this exact Euclidean expected-square recursion and its two sharp slowdown constants. Gower–Richtárik (arXiv:1506.03296, Sections 3.4, 4.3–4.4) subsumes the **update method**, not this closed-form second-moment law; its theorem is an upper bound. Carson–Ma (arXiv:2609.15605) treats asynchronous, delayed general iterations with bounds. Relevant published two-coordinate Gauss–Seidel work was also compared; its state-space and model differ. Available record and literature searches did not identify an equivalent or stronger special-case formula. Search failure does not establish uniqueness; a known or unindexed exact compound-symmetry computation remains possible.

## Value — PASS

The motivating network-game paper singles out slow clique convergence, and this result turns that observed behavior into an explicit exact expected squared-error rate valid for every nonzero local initial disturbance. In contrast to generic contraction inequalities, it gives the sharp per-update factor and its critical-parameter and large-population constants; these quantify iteration costs in the canonical complete-network benchmark without simulation or initial-direction optimization. The fact is a narrowly specialized exact model theorem, not a universal network-game convergence law.

## Limitations

Exactness requires non-clipping locality, uniform independent selection, identical linear substitutes, and complete-graph symmetry; it does not cover distant starts, general graphs, or the almost-sure exponent. Priority remains vulnerable to unindexed equivalent work. No independent scientific audit was performed.

Self-review: passed. Independent audit: not yet performed.
