# Review of the finite-ring arithmetic gap law

## Correctness

**PASS.** The model is fixed at \(0<a<b\), \(g>0\) with only intracell dissipation; periodic momenta and normalization exactly match arXiv:2203.01333, Eqs. (2.5), (2.23), and Appendix A. A branch-independent square-root identity gives \(F(q)=4g^2u(q)^2/[(S(q)+R(q))(g+Y(q))]\), proving nonnegativity and locating the *only* soft momenta. The nonzero quadratic curvature \(gs^2/(s^2+g^2)\) at those points is checked by direct expansion. Uniform upper and lower minimization estimates hold even for irrational exceptionally close resonances and include exact rational zeros. Kronecker density and continued-fraction bounds justify the distinct arithmetic consequences. The bundled standard-library checker replays the finite comparisons; its finite tests are not the proof.

## Originality

**PASS with residual risk.** arXiv:2203.01333 contains the full Bloch dispersion and thermodynamic closure criterion, while arXiv:1904.08432 contains the analogous periodic damping band and the **endpoint** quartic dispersion. Neither examined full text states the finite-\(N\) commensurability classification, the uniform \(\|N\theta\|^2/N^2\) law, or its irrational \(N^{-4}\) subsequences. The latter do not follow from the endpoint quartic expansion: the interior dispersion is quadratic and the fourth power comes from arithmetic approximation. The precise results are nevertheless consequences of the published exact dispersion once the uniform minimization and number-theoretic steps are performed; specialized finite-size literature not identified here remains a novelty risk. Relevant published research searches and available overlapping research records were compared by claim and model, not title alone.

## Value

**PASS.** The primary studies call an interval of periodic parameters gapless, a continuum-band statement that does not characterize any particular finite ring. Exact commensurability gives a sharp finite/infinite boundary and distinguishes genuinely zero-gap rational sizes from irrational sizes with arbitrarily small but strictly positive gaps. The uniform arithmetic profile identifies rare relaxation-scale anomalies not described by a generic \(N^{-2}\) finite-size law, while showing why a known endpoint \(N^{-4}\) dispersion is a distinct physical mechanism. These are naturally motivated spectral invariants of the cited solvable system rather than arbitrary parameter slices.

## Residual limitations

The rapidity-gap convention includes zero modes and is not identical to a gap measured after deleting all stationary modes. No uniformity as \(a\) approaches the endpoint \(b\), or across dissipation strengths, is asserted. A later or unindexed study of identical finite-size Bloch sampling could reduce originality; results are not independently audited.

Self-review: passed. Independent audit: not yet performed.
