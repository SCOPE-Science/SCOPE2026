# Scientific assessment of the exact social-contagion SIR endemic-equilibrium classification

## Correctness — PASS

The fixed-control hypotheses are explicit and remain inside the admissible physical parameter range. The exact noncompliant-population balance determines the behavior-transfer coefficient independently of disease burden. The susceptible and infected two-by-two matrices have strictly positive inverses; their reduction yields a strictly decreasing scalar infection-pressure function. Its value at zero is the spectral radius of the next-generation matrix, and its limit at infinity is zero. This proves the sharp existence-and-uniqueness classification of positive endemic equilibria, including equality at the threshold. The recovered equations and total-population balance close the construction without an inconsistent assumed behavioral total.

For the claimed discrepancy with the printed formula, direct algebra gives \(\mathcal R_{\mathrm{inv}}-\mathscr R_{0,\mathrm{print}}=\beta\alpha(1-\alpha)ss^*[(\mu^*-\mu)-\mu]/J\). The stated exact parameter example has all six strictly positive rational compartments, zero residuals in each differential equation, invasion reproduction number \(1909/1850\), printed reproduction number \(913/925\), and infectious Jacobian determinant \(-649/1850\). The standalone rational checker prints `VERIFY_OK`. Generic claims rest on analytic proofs, not finite numerical runs.

## Originality — PASS, qualified by documented literature risk

The checked earlier analysis of the **same v3 source model** has already established the correction to the printed disease-free reproduction ratio, its exact algebraic discrepancy, and a local-stability reversal. These are **covered prior results** and are explicitly excluded from the accepted novelty claim. Crucially, that prior analysis states that its conclusion is confined to disease-free local invasion and does not address endemic equilibria. Its local instability example at the boundary \(\xi=0\) neither entails existence nor rules out multiple strictly positive endemic equilibria across \(0<\xi<1\). The new result is a complete theorem on positive equilibrium **existence, uniqueness and nonexistence**, and a rigorous polynomial degree reduction from the quartic anticipated in the motivating source.

In the motivating article's full publicly available v3, equations (2.2), (2.6), and Theorem 2.3 treat disease-free invasion; its text explicitly leaves the endemic-equilibrium calculation unfinished. The source's first version employs a different force of infection. Parkinson and Wang's predecessor, the related reaction-diffusion/control papers, and generic next-generation theory do not imply the exact positive-equilibrium count. The full source PDF, predecessors, and relevant mathematical literature were compared by scientific statements rather than by titles. No covering endemic-equilibrium classification was found. Unindexed literature and subsequent article revisions remain genuine originality risks.

## Mathematical value — PASS

The result settles a specific mathematically nontrivial open equilibrium-count question left by the source authors for their model: a putative quartic gives way to a single quadratic and a sharp global positive-equilibrium threshold. The complete count distinguishes a genuinely endemic stationary state from mere local disease-free instability and supplies an explicit positive six-compartment benchmark. The pre-existing printed-ratio correction is relevant context, not the reason for the new value verdict. No empirical or global-dynamical-stability claim is needed.

## Closest literature and limitations

Primary source: Ngo–Parkinson–Wang, arXiv:2509.09075v3 (especially equations (2.2), (2.6), Theorem 2.3 and the paragraph after it). Related complete scientific documents inspected: arXiv:2509.09075v1, arXiv:2507.01046v4, arXiv:2303.01489v3, arXiv:2407.17298v2, and the van den Driessche–Watmough (2002) preprint. The 2024 Pant–Safdar–Santillana–Gumel article was identified as a relevant but structurally different behavioral model; its full article was not inspected. Additional unindexed statements or later corrections remain possible. This result does not classify boundary control parameters, the stability of positive equilibria, periodic behavior, stochastic dynamics or time-dependent optimal controls.

Self-review: passed. Independent audit: not yet performed.
