# Independent mathematical audit

## correctness

PASS

The ORIGINAL Sarkar–Roy 2023 same mathematical model Section 4.2 Eq.(25) and Appendix B.2 Eq.(B.22) supply the bulk equal-time cosine-integral forward covariance; independent inspection of those formulae confirms the two reservoir contributions. The elementary Poisson-kernel integral converts each to K ρ(r)^(n+1)/(1-ρ(r)^2), with ρ=(sqrt(r²+Ω²)-r)/(sqrt(r²+Ω²)+r); in particular the original paper’s C0 temperature expression agrees after using a²=2Dk²/r. Write y=ρ/(1-ρ²)>0 and h(y)=(sqrt(1+4y²)-1)/2; then S=y1+y2, T=h(y1)+h(y2), h″>0. Parameterize y1,2=(S±δ)/2, δ∈[0,S): strict convexity yields monotone T from 2h(S/2) inclusive to h(S) exclusive. Inverting ρ=2y/(1+sqrt(1+4y²)), r=Ω(1-ρ)/(2sqrtρ) gives unique unordered finite rates, including equal-rate endpoint. Independence of C0 alone and quadratic non-Lipschitz conditioning at δ=0 follow directly. Independent numerical inversion and boundary checks used S=.25,1,3,9, several δ fractions; finite values are corroborative only.

## originality

PASS

Best-of-knowledge: The earlier forward formula is mathematically sufficient as data to derive the new inverse theorem with additional convexity reasoning; the audited novelty is the explicit complete injectivity/feasibility classification, not the known forward correlations. Source reading, explicit four comparisons and priority risks detailed below.

## value

PASS

A sharp inverse-identifiability theorem based on just two **local** bulk velocity measurements is motivated by reservoir inference, with a complete feasible-statistic wedge, equality boundary, and quantitative ill-conditioning. It separates model-specific parameter identification from microscopic driving-law identification and is more than restating a forward correlation formula.

The dated certificate retains the supplied scientific assessment, sources and limitations.
