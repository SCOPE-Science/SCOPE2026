# Independent mathematical audit

## correctness

PASS

Directly composing the + and - gradient maps x->(1-h)x±hb yields one-epoch X_next=(1-h)^2 X±h^2 b. Since the multiplier r lies in [0,1), iteration converges uniquely to δΣr^j ξ_j; independence gives Var=δ²/(1-r²). The two similarities x->rx±δ tile the invariant interval iff r≥1/2; r=1/2 gives uniform tiling; 0<r<1/2 satisfies the open-set condition with dimension log(2)/log(1/r) and sharp central gap g=δ(1-2r)/(1-r), whose endpoints are achieved by signed tails. The special r=0 gives exactly ±b, and h=1±1/√2 are boundary interval/uniform cases. Independent symbolic composition and gap checks corroborated the proof, not used as infinite proof.

## originality

PASS

Best-of-knowledge original optimizer-specific distributional phase boundary; standard Bernoulli-convolution geometry and Ying et al exact MSD are explicitly prior, not rebranded.

## value

PASS

An exact supported-state phase boundary is a natural invariant of stochastic optimization: it shows zero stationary mean and small MSE can coexist with a positive support gap excluding the true minimizer. The sharp learning-rate band is a concrete mechanism and diagnostic, not merely a restatement of abstract Cantor-set theory.

The dated certificate retains the supplied scientific assessment, sources and limitations.
