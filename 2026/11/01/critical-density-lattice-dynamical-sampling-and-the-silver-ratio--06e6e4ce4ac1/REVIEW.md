# Scientific review

**Correctness: PASS.** The samples from each period depend on a disjoint \(2K\)-site block, and the ordered block matrix has two new pivot coordinates with value \(2^{-t}\) at each time. This gives the exact determinant, while the Laurent Chebyshev identity produces an explicit inverse. The upper and lower inverse-norm estimates use the same exact formula for the coefficient-one-norm of the Chebyshev polynomials, with polynomial prefactors that vanish under \(K\)-th roots. Standard-library exact-rational calculations cover \(1\le K\le7\) but are not offered as an infinite proof.

**Originality: PASS against the material inspected, with unresolved historical-priority risk.** Bulai et al. (arXiv:2609.25472v1, 2026) build other lattice graph frames and study finite path conditioning but do not establish the stated local adjacency model and silver-ratio conditioning. Older dynamical sampling and spatiotemporal trade-off theorems cover the general reconstruction paradigm; this theorem claims only its precise critically sampled local stencil, exact determinant and sharp exponential Euclidean condition-number constant. Published-record searches for the specific formula and reductions found no equivalent. A plausible older journal article was accessible only through bibliographic/abstract material, so its uninspected full text remains an explicit priority risk.

**Value: PASS.** The fact that temporal measurements can compensate for sparse sensors is established, but determining whether the critical-density configuration remains numerically stable is a concrete mathematical gap. Here it never degenerates at fixed \(K\), yet conditioning deteriorates exponentially at an exact algebraic rate. The local inverse and full-space Riesz assertion distinguish it from finite path numerical examples and supply a useful benchmark for sensor design.

**Limitations.** No global arrangement optimum, closed-form individual singular values, or noise-robustness claim uniform in \(K\); no independent mathematical audit has been carried out.

Self-review: passed. Independent audit: not yet performed.
