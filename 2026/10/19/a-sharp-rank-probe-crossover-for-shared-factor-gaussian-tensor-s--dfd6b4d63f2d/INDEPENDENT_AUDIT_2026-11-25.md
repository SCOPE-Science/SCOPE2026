# Independent mathematical audit

## correctness

PASS

Conditioning on the single random u gives independent N(0,S) probes, where S=||Mᵀu||²=Σs_i²G_i²>0 almost surely. The standardized probes have a law independent of u, so the squared denominator is SW with independent W~χ²_ℓ. Integrating the smooth anisotropic Gaussian density over the radius-√x ball gives F_S(x)=a_S x^{r/2}(1+O(x)), with a_S=1/[2^{r/2}Γ(1+r/2)∏s_i]; the radial density gives the matching relative error. The χ² coefficient a_W is the same without ∏s_i and with ℓ in place of r. Conditioning on the factor with the larger exponent gives dominated convergence via its finite negative moment. At equality, splitting at x/ε and ε leaves two O(x^{r/2}) ends and a middle integral (r/2)a_S a_W x^{r/2}∫dy/y with O(x^{r/2}) error. Substituting x=ℓF²/τ² gives the factor two in front of log τ and the stated constants, including the gamma negative moment and the Laplace integral by Tonelli. Integrating the tail proves the sharp inverse-moment cutoff, with divergence also at equality. Conditional SLLN proves the limit F/√S (Var(S)=2Σs_i⁴>0). These are fixed nonzero spectra, not a uniform varying-rank claim. Frozen verification notes and supplied checker were inspected but not executed. Independent isotropic quadrature integrating the product CDF gave exact/leading ratios 0.9996264, 0.9860243, 0.9934920 and 0.9934920 at (r,ℓ,τ)=(1,3,80),(2,2,250),(2,3,250),(3,2,250).

## originality

PASS

The closest distinct Resultary work concerns least-squares coefficient errors for reused tensor factors and independent tensor rows; earlier embedding work assumes independent factor columns. Product normal logarithms, gamma product laws, and the general conditioning method are prior inputs, not themselves new. The supported distinct result is the arbitrary fixed singular-spectrum rank-versus-probe trichotomy with its constants for this shared-left norm sketch, combined with the exact residual randomness as the right sample size goes to infinity. No examined exact or stronger result supplies that full model-specific classification.

## value

PASS

Reusing a random left probe is a natural reduction in sampling/storage that leaves all right draws conditionally independent. The theorem gives a precise reliability cost: a rank-controlled failure exponent, a calibrated logarithmic penalty exactly at matching rank and probe count, and a nonvanishing random error even with unlimited right draws. Both the inverse-moment frontier and anisotropic leading constants can be needed when using such probes for norm validation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
