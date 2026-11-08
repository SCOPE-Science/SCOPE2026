# Independent mathematical audit

## correctness

PASS

The four-phase cyclic generator with signs ++-- has characteristic polynomial [z(z+2λ)-v²k²][(z+λ)²+λ²-v²k²]; the first factor gives the strictly dominant Perron root -λ+sqrt(λ²+v²k²) equal to the 2-state telegraph root. Adding drift uk and Brownian Dk² gives identical SCGF; Gärtner–Ellis gives interior LDP, ballistic endpoint no-switch events carry exponent λ and close the zero-D endpoints. Stationary sign correlations are e^{-λt}cos(λt) versus e^{-2λt}; integrating them proves transient gap v² e^{-λt}[sinh(λt)-sin(λt)]/λ²>0. Harmonic filtering yields positive stationary variance gap v²λ/[(κ+2λ)((κ+λ)²+λ²)]. Independent SymPy determinant, both variance integrals and filtered gap verified. No equality of mean run times is claimed.

## originality

PASS

Best-of-knowledge statement/implication comparisons of the precise final claim, with material primary reading and relevant Resultary searches. General renewal large deviations and stationary filter theory are inputs, but asserting coincident leading spectral branches while nonleading modes shift covariance requires this explicit four-phase model calculation. Inaccessible primary work is named as residual risk rather than declared noncovering.

## value

PASS

Explicit non-identifiability witness for an entire level-one large-deviation rate function while finite-time fluctuations and linear-trap observables disagree strictly; calibrated example isolates what persistent-memory data free-current LDP cannot identify.

The dated certificate retains the supplied scientific assessment, sources and limitations.
