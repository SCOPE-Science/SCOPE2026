# Review

**Correctness.** The exact finite-cycle threshold follows from the rank-two resolvent determinant and the endpoint value \(\lim_{E\downarrow2}(g_0-g_d)=d(N-d)/(2N)\). The proof identifies the two symmetry channels, establishes monotonicity, and states the equality case and the scaling limit separately. `CHECKER.py` corroborates the kernel and scaling equations with 40 passing checks; the proof, not the finite tests, establishes the general result.

**Originality.** The closest fully inspected primary source, Joglekar et al. (2010), uses imaginary PT-symmetric impurities on an open chain and studies exceptional-point thresholds. It does not state the real, positive, periodic-cycle bound-state count or the function \(\Psi_\pm\). Bierman (1970) addresses dilute many-impurity bands, but only the abstract was accessible and it does not state this finite-cycle formula. published-finding corpus searches returned related but non-equivalent work on two-dimensional lattice delta thresholds, metric-loop point interactions, and phase-twisted quantum graphs. An uninspected source could still contain an equivalent rank-two resolvent calculation.

**Value.** The theorem gives a complete, exact count of defect-induced levels above the band for every finite cycle and every separation, then identifies the separation-dependent weak-defect scale at which the second level appears. This distinguishes a single elevated level from two defect modes and gives an explicit limiting law rather than only a numerical \(1/N\) trend.

**Closest literature and residual risk.** The inspected PT-symmetric paper motivates the separation-dependent finite-size scale but has a different operator and spectral transition. The accessible many-impurity abstract motivates impurity-band questions but is not a finite-cycle classification. The result should be read as a best-knowledge exact extension; no claim is made that the underlying rank-two resolvent technique is new.

Self-review: passed. Independent audit: not yet performed.
