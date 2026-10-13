# Self-review

**Correctness: PASS.** The ODE is reconstructed verbatim in normalized form from [1, Eq. (27)]. Positive invariance and \(I_D\ge I_0e^{-\gamma T}\) support upper and lower scalar Riccati comparisons for the rescaled risk. The resulting exponential \(\sqrt D\)-scale susceptible bound feeds the exact removal convolution, which proves the positive infected limit and subsequent recovered fraction. The moving-tube argument establishes the instantaneous algebraic risk equilibrium away from time zero. Integration of \(\dot{\log S}\) yields the exact decay exponent; continuous dependence gives the fast-time layer. Three finite numerical checks agree with, but are not proofs of, these limits.

**Originality: PASS, subject to stated search risk.** The original Gaussian SfIR source [1] poses the high-social-diffusion limit as an unsolved question and suggests all three epidemic classes should vanish (apart from recovered) for fixed positive time. This finding identifies a strictly positive infected limit and supplies a nonlinear initial-layer theorem and exact asymptotic coefficients. The closest related complete paper [2] studies a different Gamma-closure contact kinetic model and does not imply this result; relevant indexed mathematical records concern distinct models. No inference of universal uniqueness follows from searches.

**Value: PASS.** The correct limit separates an almost instantaneous infection-transfer event from ordinary removal: high social diffusion rapidly exhausts susceptibles but does not remove newly infected people at the same instant. The closed-form logarithmic extinction rate and self-contained fast-layer system give reusable, model-specific quantitative information that answers the motivating research question rather than a routine consistency check.

**Limitations and comparison.** The theorem concerns only the normalized four-ODE Gaussian closure of [1]. It assumes fixed positive initial infection and fixed model coefficients other than diffusion; no general claim for the PDE, other social-contact closures or simultaneous large-time/diffusion limits is made. General singular perturbation literature not explicitly traced may contain stronger abstract machinery, an acknowledged originality risk.

[1] Berestycki, Desjardins, Weitz and Oury, *Epidemic modeling with heterogeneity and social diffusion*, J. Math. Biol. 86 (2023), 60; DOI 10.1007/s00285-022-01861-w.

[2] Dimarco, Perthame, Toscani and Zanella, *Kinetic models for epidemic dynamics with social heterogeneity*, J. Math. Biol. 83 (2021), 4; DOI 10.1007/s00285-021-01630-1.

Self-review: passed. Independent audit: not yet performed.
