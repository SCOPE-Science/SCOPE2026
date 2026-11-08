# Independent mathematical audit

## correctness

PASS

Diagonalizing the two-node Gram matrix gives a symmetric bounded component and antisymmetric denominator 1-exp(-λ|δ|^α). The mean difference m(u+δ/2)-m(u-δ/2)=m′(u)δ+o(δ), yielding weight blow-up proportional to |δ|^(1-α) when α>1. Gaussian noise therefore has one-sided regularly varying tails with exponent β=1/(α-1) and constant (σ/λ)^β Γ((β+1)/2)/√π ∫|m′|^β. Integrability gives finite second moment iff α<3/2, including logarithmic divergence at α=3/2. The nugget integral reduces to ∫ d²/(η+λd^α)² dd, giving the stated log coefficient or gamma-product power coefficient for α>3/2; bounded Lipschitz noiseless contribution cannot alter tail leading terms. Independently checked kernel-mean/weight collision scaling at α=1.25,1.75,2.0 via direct numerical integration; no numerical test is a uniform proof.

## originality

PASS

The α=2 Gaussian collision case is explicitly known and not claimed original. Prior kernel quadrature studies bound fixed-design weight magnitudes in terms of separation or discuss selected Nyström subspaces, without the complete iid collision-tail all-exponent law, threshold 3/2 and exact ridge coefficients. Earlier specialized collision analysis is a residual priority risk.

## value

PASS

Near-coincident iid nodes create a sharp variance phase transition and exact heavy-tail/regularization asymptotics for a canonical probabilistic numerical integration rule; the threshold matters for when sampling variance exists and how much nugget stabilization costs.

The dated certificate retains the supplied scientific assessment, sources and limitations.
