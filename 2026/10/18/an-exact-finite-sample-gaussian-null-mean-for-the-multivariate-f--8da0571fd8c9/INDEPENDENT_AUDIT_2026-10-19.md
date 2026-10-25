# Independent mathematical audit

## correctness

PASS

For every d>=2, n>=d+1, a>0, the Gaussian whitening projection has Gram nP for Haar d-plane in 1-perp. For fixed unit v, Z=v^TPv is Beta(d/2,(n-d-1)/2) (or deterministic one at n=d+1); diagonal and pairwise quadratic expectations collapse to M0,M1 Kummer moments using E[Q|Z]=(d-Z)/(n-2). Substitution into the exact published finite-data Fourier integral yields all three coefficients with divisor n. At n=d+1 the whole Gram is deterministic. Independent scipy Beta quadrature and minimal-simplex exact checks matched.

## originality

PASS

The exact finite-n Gaussian-null mean is not the published mean of the limiting null law; full finite covariance-Haar beta projection calculations are required. Best-of-knowledge PASS with priority caveat.

## value

PASS

Finite-n Gaussian Fourier–Stein expectation is a natural calibration invariant not given by the limiting null mean. The exact continuous d,n,a formula and smallest-sample degeneracy are independently useful while not claiming quantile calibration.

The dated certificate retains the supplied scientific assessment, sources and limitations.
