# Self-review

## Correctness — PASS
The two-orientation Fokker–Planck system yields the normalized, nonnegative stationary position density and wall contact formula. Cartesian independence gives exact dimension-wise pressures. A monotonicity identity for \(\tanh z/z\) proves strict convexity and majorization; exact one-form integration proves path independence. Coercivity and the precise second variation prove existence of the symmetry-broken minimizers and the small-stiffness limit. The standalone checker reproduces 1670 deterministic consistency tests; the global assertions rely on proof, not sampling.

## Originality — PASS (qualified best-knowledge)
The 2026 Li–Eichhorn–Dabelow paper contains the exact one-dimensional RTP wall law and a high-dimensional AOUP **approximation** with dimension-wise pressure. We neither claim the one-dimensional law nor its pressure form as new. The exact product-telegraph high-dimensional model plus the strict all-shape ordering, null cycle work, unbounded aspect law and elastic threshold are not stated in the inspected main text or supplementary equations. Nikola et al. (2015) address flexible-wall modulations on curved interfaces, and Ezhilan et al. (2015) address confinement of athermal swimmers between plates. Searches across available research records found no dominating claim. The main residual risk is that the new conclusions could be considered readily implied by tensorizing the known one-dimensional result or in literature on finite-volume active containers not retrieved here.

## Value — PASS
At fixed volume, passive gases perform no net mechanical work under shape deformation. The studied driven gas instead has a universal strictly ordered shape-work landscape, an explicitly positive loss of equal-shape stability against finite Hookean elasticity, and a sharp inverse-stiffness log-aspect growth. This specifies a physical mechanism of shape selection and a mechanical design threshold, not merely a recomputed density or a change of notation.

## Boundaries
A compliant-box force balance is analyzed only under quasistatic stationarity and the specified Hookean potential; full stochastic wall dynamics are unproved. The product-telegraph orientation is intentionally different from isotropic multidimensional RTP orientation. The hard-wall point-particle divergence need not persist at microscopic wall thicknesses. Independent mathematical or priority auditing is outstanding.

Self-review: passed. Independent audit: not yet performed.
