# Scientific review

## Correctness — PASS

The stated model has a positive-rate two-state telegraph input and no Gaussian forcing. Prescribed finite switching histories have positive probability in neighborhoods; chattering recovers all bounded measurable controls in support, giving an exact compact zonoid. The planar zonotope determinant area formula and the semigroup determinant identity reduce the area to a one-dimensional convolution. Its differential identity proves global \(C^2\) regularity and the exact one-sided third-derivative jumps at every underdamped impulse zero. Ratios of these positive jumps give a unique inverse reconstruction. A standalone independent quadrature–zonotope checker passed 39 finite assertions; that computation corroborates but does not replace the proof. No unproved infinite-time numerical step is used.

## Originality — PASS, qualified

Dutta et al., arXiv:2406.06120v1, Sections II–V and Appendix C, give the identical stochastic model and stationary joint-support boundaries; no finite-time support-volume cusp reconstruction is stated there. Haddad, Khodary and Halder, arXiv:2309.08222, Section IV, Theorem 5, already compute the volume of an arbitrary controllable single-input LTI reach set semi-analytically; hence neither the bounded-control equivalence nor generic finite-time area calculation is claimed new. Zhao, arXiv:2004.05530v1, addresses zonotope volume and discrete-time reachability, analytically treating real eigenvalues. The mathematically compared claim here is the exact all-horizon regularity transition and inverse damping/frequency/force law from nonzero third-derivative jump data, not the prior generic volume formula. Prior accessible research-index results concerned different oscillator statistics, finite-time areas of other flows or unrelated controlled systems. A broader implicit specialization of earlier reach-volume theory remains a substantive publication-priority risk, so this is a qualified self-review originality assessment, not a uniqueness certificate.

## Mathematical value — PASS

The support area is a natural phase-space accessibility measure that distinguishes inertia-controlled oscillatory dynamics from monotone relaxation. Its third-derivative singularities carry spectral and mechanical information even though the accessible support is invariant under every positive tumbling rate. The infinite cusp sequence is fully classified and provides a direct parameter-reconstruction mechanism from the geometry alone. This is more than a small numerical refinement, a routine restatement of a generic volume algorithm, or an arbitrary selected example: the nonanalytic boundary identifies a physical dynamical phase. The theorem does not promise practical extraction from finite noisy observations.

## Closest literature and residual limits

The strongest antecedent is the exact general single-input LTI reach-volume theory of Haddad, Khodary and Halder (2023), not merely the stationary particle analysis. A subsequent publication search or independent expert check could find a dominating corollary or a previously known oscillator-specific cusp law. Thermal noise destroys compact support, and the theorem does not estimate physical parameters without sufficient geometric access.

Self-review: passed. Independent audit: not yet performed.
