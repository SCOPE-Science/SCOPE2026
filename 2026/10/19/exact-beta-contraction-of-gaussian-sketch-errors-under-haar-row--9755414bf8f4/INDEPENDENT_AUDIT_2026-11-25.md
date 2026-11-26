# Independent mathematical audit

## correctness

PASS

Set m=n−r and p=n−ℓ. For ℓ<n the Haar row projector has the law of projection onto the kernel of a p by n Gaussian H. In coordinates [Q,Q_perp], minimization over both the QR error v and the projected-out coefficient z sets v=H1ᵀz, z=−ζ(H2H2ᵀ)⁻¹H2u. H2 has p≤m and full row rank, also giving injectivity of the sketch on col(Q). Conditional on H2, H1ᵀz/∥z∥ is standard Gaussian with a law independent of H2. For H2ᵀ=VW^(1/2), the independent Stiefel and Wishart factors give ∥z∥²/ζ²=B sᵀW⁻¹s; B=∥Vᵀu∥² is the stated Beta by the squared sphere-coordinate split and is independent of (s,W), including the degenerate B=1 boundary. The inverse quadratic form is a Schur-complement chi-square with m−p+1=ν degrees. For the Gaussian sketch, the conditional covariance of v/ζ is inverse Wishart with ℓ degrees: integrating the conditional density changes the Wishart scale by I+vvᵀ/ζ² and yields the claimed multivariate Student law. Orthogonality of e makes excess loss the squared QR-error radius, and θ↦θ X/Y is strictly ordered in survival probabilities at positive thresholds for 0<θ<1. The q-moment threshold and ratios follow by independence and gamma integration. For the tail limit P(Y<y)≤y^(ν/2)/(2^(ν/2)Γ(ν/2+1)) for all y, so conditioning on X or BX justifies dominated convergence and both constants. At ℓ=n Haar gives zero error; at ℓ=r both sketches share the same marginal law, not the same independent-sketch realization.

## originality

PASS

The independent scalar attenuation law for arbitrary design rank is distinct from the inspected Gaussian marginal Student law and from the exact Haar expected-risk and matrix-Beta analysis. The overlapping later indexed result establishes rank one, not arbitrary rank. Credit the known Gaussian law, mean identity and classical distributional tools, not a new claim to those ingredients.

## value

PASS

For the standard Gaussian and Haar sketch-and-solve comparison, the exact independent multiplier turns a comparison of means into a distributional comparison of coefficient errors and excess risk. It distinguishes the case of no contraction at minimal sketch size from strict all-threshold improvement while retaining the same heavy-tail exponent and moment cutoff. This gives usable finite-size risk information even in regimes where the expected excess risk is infinite.

The dated certificate retains the supplied scientific assessment, sources and limitations.
