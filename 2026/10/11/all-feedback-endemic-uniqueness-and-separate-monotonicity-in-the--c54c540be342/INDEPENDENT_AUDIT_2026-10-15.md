# Independent mathematical audit

## correctness

PASS

At positive equilibrium I=z, infected balance fixes S+σC=(μ+α)/β=q, forcing β>μ+α. Solve the positive linear R,C stationary subsystem for C=αδ(1+ε₁z)z/D and R=αz(βz+μ+γ(1+ε₂z))/D with D>0. Conservation gives H(z)=z+αzK(z)/D(z)=1−q with quadratic D=d₀+d₁z+d₂z² and linear K=k₀+k₁z. The derivative H_z=1+α[k₀d₀+2k₁d₀z+(k₁d₁−k₀d₂)z²]/D² is >1 because the last coefficient is the sum of six manifestly nonnegative products including strictly positive β²(μ+σδ). Since H(0)=0,H(1−q)>1−q, exactly one interior root exists. Reconstructed S,R,C are strictly positive even at σ=0 or 1. Quotient differentiation gives ∂(K/D)/∂G₁=−δ(βz+γG₂+μ)(σβz+γG₂+σμ)/D²<0, and ∂(K/D)/∂G₂=−δγG₁(1−σ)(βz+δG₁+μ)/D²; implicit differentiation yields the claimed strict/zero prevalence response. At β≤μ+α only the disease-free equilibrium. Real-analytic I* follows from H_z>0 with local continuation near ε_j=0.

## originality

PASS

The exact prevalence-driven SIRCm model, independently varied immune-escape feedback coefficients, and full rectangular nonnegative domain differ from the source paper’s weak/strong asymptotic or diagonal sufficient regimes. Independent channel-derivative factorizations and the σ=1 sharp equality boundary are additional statement-level content.

## value

PASS

The model’s original publication explicitly leaves intermediate feedback uniqueness insufficiently covered, and the result supplies a natural complete classification across independently varying feedback strengths while distinguishing two mechanisms and the exact σ=1 boundary. It rules out spurious algebraic multistability in an identifiable nonlinear epidemic system, an independently useful structural fact rather than a mere symbolic reformatting; no biological efficacy is inferred.

The dated certificate retains the supplied scientific assessment, sources and limitations.
