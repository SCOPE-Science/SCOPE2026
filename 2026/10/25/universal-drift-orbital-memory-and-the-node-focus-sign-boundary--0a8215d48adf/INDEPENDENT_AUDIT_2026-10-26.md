# Independent mathematical audit

## correctness

PASS

For stable real 2x2 drift B with trace k>0, detB>0 and SPD diffusion D, Q=[[-c,(a-d)/2],[(a-d)/2,b]] has B^T Q+QB=kQ (verified symbolically). The quadratic observable X^T Q X has generator L(T-mu)=-k(T-mu), mu=tr(QS), S>0 solves BS+SB^T=2D. Stationary conditional expectation then gives Cov=V exp(-k|t|) with V=2tr((S^{1/2}QS^{1/2})^2)>0 unless Q=0. Gaussian determinant identity yields characteristic function; integrated variance follows explicit kernel integral. detQ=detB-k^2/4=-Delta/4 gives indefinite/node both signs, definite/focus strict one sign, rank1 repeated-root one sign, scalar B activity 0. Independently checked symbolic 2x2 identity, 3 rational Lyapunov examples and finite lag Wick correlation.

## originality

PASS

The drift-only wedge is not pathwise stochastic angular velocity and has an exact one-dimensional generator eigenspace for any stable planar B and SPD noise; Godreche-Luck supplies general OU covariance but does not expressly state this distinguished observable/sign trichotomy, and Viot et al. study noise-containing increment angular momentum. General quadratic OU polynomial eigenfunctions create a plausible equivalence risk, stated explicitly.

## value

PASS

A physically motivated observable has universal single-time-scale memory independent of nonnormality, oscillations, and diffusion anisotropy, plus sharp node/focus sign-support boundary and exact integrated variance. This is substantive spectral/observable structure rather than routine computation of one covariance.

The dated certificate retains the supplied scientific assessment, sources and limitations.
