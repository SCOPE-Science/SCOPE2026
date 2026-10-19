# Scientific review

## Correctness

**PASS.** The original two-harmonic recurrence is specified exactly. A trigonometric identity forces the cubic zero at the shape \(\beta_*=\pi-\arctan(3/5)\). A smooth center reduction at the neutral fixed point produces the strict fifth-order restoring drift \(-3C\mu c^2x^5/(1-\mu)\), and the inverse-fourth-power asymptotic follows by a telescoping increment. The strong-stable exceptional line is identified explicitly. Two small-polynomial root calculations classify the local stationary split and Jacobian spectra. Uniform memory contraction, Euler consistency and discrete Grönwall estimates establish the fixed-horizon detuning limit. The included exact-symbolic and finite numerical checker returned `VERIFY_OK`.

## Originality

**PASS, subject to historical-priority uncertainty.** Gilet (2014, model equation (9), wave equation (20), figure 2) already derived the fixed-point families and plotted their shape variation; neither an unexplored number of fixed points nor a new general center-manifold theorem is being claimed. Rahman and Blackmore (2015 preprint) analyzed Neimark–Sacker crossings, typically away from a zero spatial slope. Rahman and Blackmore (2017 preprint) analyzed homoclinic/heteroclinic interactions and invariant curves while varying coupling, not this critical wave-shape detuning. The sharp critical inverse-fourth coefficient together with the \(\sqrt\varepsilon\)-space, \(\varepsilon^{-2}\)-time gradient-limit law is not covered by the inspected source statements or by the closest indexed comparisons. Related quintic critical exponents in other dynamical systems are not stronger coverage of this map. Unindexed earlier work on the same shape remains a priority risk.

## Mathematical value

**PASS.** This is a natural local singularity of the exact two-harmonic family introduced to study confinement-induced walker dynamics. The source's hyperbolic stability criteria become inconclusive when its basic wave slope vanishes; the theorem resolves the boundary without stopping at numerical simulation or generic exponent identification. It determines the exact relaxation amplitude, both sides of the fixed-point transition and a finite-time observable process limit resolving metastable behavior over diverging physical iteration counts. The original source plots stationary branches, but does not give their critical time-law or gradient crossover. The scope stays local and does not claim new experimental hydrodynamics.

## Sources and limitations

The closest primary sources are T. Gilet, *Physical Review E* 90 (2014), 052917, DOI: 10.1103/PhysRevE.90.052917; A. Rahman and D. Blackmore, arXiv:1507.08057 (2015); and A. Rahman and D. Blackmore, arXiv:1708.07593 (2017). Their model definitions, results, and relevant comparison sections were inspected. The formal demonstration uses standard smooth center manifold and stable foliation results. The standalone script checks algebra and finite trajectories, not the infinite theorem. Independent literature priority confirmation and an independent audit remain outstanding.

Self-review: passed. Independent audit: not yet performed.
