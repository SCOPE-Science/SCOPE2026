# Same-model review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

**PASS.** The first- and second-moment identities follow directly from invariance applied to the observables \(x\), \(y\), \(z\), \(x^2/2\), and \((x^2+y^2)/2\). The variance formula then reduces exactly to a quadratic in the stationary mean \(m=\langle z\rangle\), and the covariance formulas are algebraic consequences. Symbolic residual checks for the Lie derivative, parabola factorization, covariance relation, and sharp cap are included in the compact verification artifact.

The conditional identity was checked separately rather than inferred from pointwise dynamics. Disintegrating with respect to the \(z\)-marginal turns invariance of all test functions \(\psi(z)\) into the statement that the compactly supported signed measure \([b+z(\mathbb E[x\mid z]-c)]\nu\) has zero distributional derivative. Such a measure must vanish, yielding both zero mass at \(z=0\) and the asserted conditional mean for \(\nu\)-almost every height.

The endpoint rigidity was stress-tested against mixtures and nonstationary equality candidates. Zero variance forces \(y\) to be constant on the support. Invariance of the support then successively forces \(x\) and \(z\) to be constant as well, leaving exactly the corresponding equilibrium. At the double-root threshold this gives uniqueness of the compact stationary probability measure, but not uniqueness of compact invariant sets; the public statement preserves that distinction. The bounded-orbit statistical conclusion uses only compactness of the orbit closure and the standard invariance of weak limits of empirical measures.

## Originality

**PASS, to the best of our knowledge.** Rössler's 1976 paper is the source of the model. Starkov and Starkov (2007) was inspected in full at theorem level. It proves half-space localization statements for compact invariant sets and, when \(c^2-4ab<0\), the absence of periodic orbits. Those conclusions are treated as prior art. Their paper does not state the invariant-measure moment parabola, the covariance identities, the conditional stationary-height law, or the critical uniqueness of stationary statistics.

Kontorovich et al. (2009) is the closest prior statistical analysis found. It develops degenerated cumulant equations for the Rössler attractor and reports an approximate variance relation, with a 5.8% discrepancy in its standard numerical example; the paper explicitly describes exact variance evaluation as unresolved within that approximation. Its displayed relation omits the \(-b/a\) contribution that appears in the exact invariant-measure identity here. This record therefore does not claim novelty for “studying Rössler moments,” but for the exact all-invariant-measures closure and its rigidity consequences.

Sprott and Li (2017) numerically searched the no-equilibrium regime and reported failure to find periodic or chaotic solutions there, while Bramburger and Fantuzzi (2024) reconstructed approximate invariant measures and degree-two moments from data. Both were checked in full at the relevant Rössler sections. Neither states the exact formulas proved here. Malasoma and Malasoma (2020) was checked through its abstract and bibliographic metadata; because its full theorem-level text was not inspected, it remains a residual priority risk for parameter-space consequences, though its stated focus is a necessary condition for chaos and hidden-attractor bistability rather than stationary moment identities.

Residual priority risk also remains from less visible Rössler localization and statistical literature. The no-compact-invariant-set corollary for \(\Delta<0\) is particularly close to the 2007 localization theorem and is not the principal originality claim. The originality claim is limited to the exact stationary parabola and covariance identities, the heightwise conditional law, and the saddle-node stationary-measure rigidity, together with their sharp consequences.

## Value

**PASS.** The theorem collapses one projection of the full compact stationary-measure problem to a closed, sharp algebraic curve: once the mean height is known, the \(y\)-variance and two covariances are fixed exactly. Every point of that curve is realized by equilibrium mixtures, while endpoint equality classifies the measure itself. This provides simulation-independent diagnostics for physical measures and periodic-orbit measures, and gives a precise statistical description of the saddle-node threshold. It also upgrades the familiar discriminant \(c^2-4ab\) from an equilibrium-existence condition to a necessary condition for compact stationary dynamics.

## Scientific limitations

The theorem assumes \(a,b,c>0\) and compact support. It does not classify noncompact invariant sets, establish existence or uniqueness of a chaotic attractor, or provide a chaos criterion. The critical empirical-measure conclusion is statistical and does not prove pointwise convergence of every bounded trajectory. Some later model-specific literature, most notably the full theorem-level content of Malasoma and Malasoma (2020), was not exhaustively inspected, so the priority claim remains qualified as to the best of our knowledge.
