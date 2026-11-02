# Scientific review: sharp equilibrium-center law for average-distance Schelling stars

## Correctness — PASS

The stated game has no self-neighbors, and its strict bilateral swap rule makes every leaf--leaf exchange non-improving. For a hub agent \(i\) and leaf agent \(j\), the before/after costs are exactly \((D_i/m,|t_i-t_j|)\) and \((|t_i-t_j|,D_j/m)\). This proves the necessary-and-sufficient test without unstated regularity or genericity assumptions. The equal-grid sum formula, strict quadratic/root inequalities, and reflection prove the finite radical criterion, including integer ties. The limiting continuum inequality has the exact critical roots \(s_*=(\sqrt3-1)/2\) and \(1-s_*\). Uniform convergence of empirical absolute-deviation costs and finite subcover arguments justify both the deterministic asymptotic and the iid corollary. Near the critical grid root, its nonzero derivative yields the stated \(O(1)\) counting error. The cost distribution is obtained from the exact per-agent social-cost identity, not an assumption about dynamic convergence.

A standalone no-dependency verifier passed 20,586 exact rational direct-swap/certificate comparisons, 80,197 finite-lattice radical-criterion checks, the disconnected five-type example, and five larger-grid asymptotic sanity checks. Finite experiments corroborate, rather than replace, the continuum proof. Residual correctness risk: the limiting conditional-law argument has no external independent proof check.

## Originality — PASS, subject to literature-priority uncertainty

The closest inspected source is Bilò, Bilò, Döring, Lenzner, Molitor and Schmidt, *Schelling Games with Continuous Types*, arXiv:2305.06819v1 (2023), including its full text, §§1.1 and 2.1.2, and Appendix C.2.2. It defines the exact game, proves regular-graph convergence, and analyzes other graph classes. These results do not state the sharp equilibrium-center fraction, the irrational cutoff, the conditional hub-type distribution or the typical-equilibrium cost law on stars. More general potential, median-hub existence or worst-equilibrium efficiency results do not quantify the set of all equilibria and do not imply these claims without additional analysis. Prior discrete-type Schelling work uses different type domains. Targeted source and mathematical-record searches did not identify equivalent covering statements.

Residual originality risk: a specialist may have derived the same star census or a more general theorem not present in searchable sources; an absence of hits is not proof of absolute priority.

## Value — PASS

A star is the canonical highly irregular hub-and-spoke network. The source's regular-graph potential methods alone do not describe how common equilibrium configurations are on such networks. The unbounded uniform-type limit gives the exact share \(2-\sqrt3\) of all assignments that are equilibria, the sharp permitted hub-type band, and the expected inefficiency of a uniformly sampled equilibrium. The five-agent noninterval example shows that the exact finite geometry is not merely “choose a median” or an always-contiguous block. This is a motivated equilibrium-prevalence and typical-welfare invariant, not an arbitrary small-case enumeration.

## Boundaries and closest literature

The theorem assumes absolute real-type distance, no vacant sites, strict mutual improvement, a star and (for the universal numerical limit) asymptotically uniform types. It does not give a convergence-time law for an adjustment algorithm or imply the same constant for nonuniform type populations, alternative distance costs or arbitrary graphs. Relevant references are arXiv:2305.06819, arXiv:1909.02421 and arXiv:2105.06561. Priority and proof have not been independently audited.

Self-review: passed. Independent audit: not yet performed.
