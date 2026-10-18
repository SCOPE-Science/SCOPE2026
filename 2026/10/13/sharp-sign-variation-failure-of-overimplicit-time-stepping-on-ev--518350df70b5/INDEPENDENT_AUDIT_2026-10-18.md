# Independent mathematical audit

## correctness

PASS

For an irreducible finite birth-death Markov generator Q, G=(I−θhQ)^(−1) is strictly positive and stochastic, and P_θ,h=(θ−1)I/θ+G/θ. Detailed balance yields positive real eigenvalues, hence positive principal minors. Because inverse tridiagonal M-matrices are Green matrices with rank-one upper-triangle factors, G_(i,i+1) G_(i+1,i+2)=G_(i,i+2) G_(i+1,i+1). Therefore det P[rows i,i+1; cols i+1,i+2]=−(θ−1)G_(i,i+2)/θ², negative for θ>1 on every n≥3 chain, independent of h. The strict principal minor creates a ratio interval and a vector supported on i+1,i+2 with one sign change whose image contains −,+,−. For θ=1, tridiagonal M-matrix inversion has TN bidiagonal factors; for n=2, positive entries plus positive determinant are TN. Thus the exact all-parameter dichotomy follows. New exact rational checks verified identity and constructive witness in 54 tested n/rate/h/θ/triple cases.

## originality

PASS

Fallat–Tsatsomeros (2002) explicitly establishes TN tridiagonal M-matrix inverses and a TN Cayley factorization when a separate explicit factor is TN. The overimplicit θ>1 matrix has a positive identity-plus-resolvent representation but a negative adjacent minor, so the existing TN result does not cover this regime. Jin et al. and Higueras–Roldán address entrywise positivity or contractivity in discretizations, a strictly weaker property than ordered variation diminution. The universal negative-minor identity and explicit sign-creation witness remain best-of-knowledge original against these sources.

## value

PASS

Ordered sign variation is a natural discrete analogue of Sturm oscillation for one-dimensional diffusion. The theorem sharply separates stochastic positivity and spectrally positive damping, which hold for all θ≥1, from variation diminution, which fails immediately at θ>1 for any h and any heterogeneous chain of at least three states. This is a complete dimension-and-parameter boundary, not merely a small counterexample.

The dated certificate retains the supplied scientific assessment, sources and limitations.
