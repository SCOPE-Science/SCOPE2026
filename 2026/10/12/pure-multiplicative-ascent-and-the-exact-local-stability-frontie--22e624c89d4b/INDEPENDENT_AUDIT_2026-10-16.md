# Independent mathematical audit

## correctness

PASS

With m(θ)=θh(θ−a)/(c+h(θ−a)^2/2), m(a)=0, m′(a)=ah/c, σ(0)=1/2, slog′(0)=1. Differentiating the source-defined core map gives T′(a)=1−η_A h/2+η_M ah/c. The one-dimensional hyperbolic fixed-point criterion gives local attraction iff |q|<1, repulsion iff |q|>1; |q|=1 unclassified. With η_A=0 and θ_0>a>0, m(θ)>0, so T(θ)>θ; a finite monotone limit would be a fixed point above a, impossible. Since m(θ)→2 as θ→∞, increments →η_M log3 and θ_k/k→η_M log3 by Cesàro. Independent centered finite difference at a=2,c=3,h=5, η_A=.8,η_M=.06 converges to q=−.8; positive initial pure trajectory increases and its increment approaches .0659167373.

## originality

PASS

MDPI 2026 primary article Sections 3.4,4.3 gives precisely the additive/multiplicative signed-log core update and warns qualitatively of instability, but its inspected material does not give the positive-minimizer derivative/dominance inequality or linear asymptotic divergence speed. Earlier multiplicative descent methods optimize with different maps. Originality scoped to this source equation and scalar positive quadratic, not generic fixed-point calculus itself.

## value

PASS

The sign of HMGD’s multiplicative correction at positive minimizers matters for actual algorithm tuning: it identifies an exact hyperbolic attraction frontier and a globally diverging purely multiplicative branch even on a smooth strongly convex objective, quantifying speed. This is a motivated algorithmic counterexample to unqualified stability interpretation, not just a normalization exercise.

The dated certificate retains the supplied scientific assessment, sources and limitations.
