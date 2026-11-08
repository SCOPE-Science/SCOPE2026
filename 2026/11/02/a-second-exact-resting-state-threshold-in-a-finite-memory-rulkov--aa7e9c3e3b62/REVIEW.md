# Independent mathematical audit

## correctness

PASS

Reconstructed post-memory-fill stationary equations: x*=sigma-1 in (-2,0), sigma=tanh(kappa sigma), kappa=m/(2tau), and full (m+2)-dimensional Jacobian characteristic P(lambda)=lambda^m[(lambda-1)(lambda-a)+mu]-mu eta sum_{j=0}^{m-1}lambda^j, a=5/(2-sigma)^2, eta=(1-sigma^2)/(2tau). Root-sign tests prove central and positive branches unstable for 0<mu<1/64, and negative branch unstable if 1<kappa<kappa*. At kappa>kappa*, 0<a<1 and the simple root at 1 moves into the unit disk for small mu. At kappa*=artanh(sqrt(5)-2)/(sqrt(5)-2), a=1 and the double root splits into a complex pair with |lambda|^2=1+mu[1-(m+3)rho*/2]+O(mu^(3/2))<1 for all m>=1. Independently computed kappa*=1.0192230012646086 and rho*=0.962423650119207, and checked Jacobian root moduli for m=1,2,3,5,10 with kappa below/at/above threshold. These finite numerical cases supplement the analytic proof. No global or arbitrary-mu stability claimed.

## originality

PASS

The scalar fixed-point intersection equation and the original finite-memory sigmoid Rulkov formulation are prior work, but the inspected evidence does not establish the exact full-lag branch stability threshold, especially stability at its singular endpoint. Best-of-knowledge originality only; the closest source's complete main text was not independently accessible here, a material priority risk.

## value

PASS

An exact, boundary-inclusive local rest-stability classification for the finite-window delayed neuronal model separates equilibrium stability from oscillatory spiking/bursting regimes. Full characteristic polynomial retains every memory mode, providing a motivated second threshold beyond the known equilibrium-creation point.

The dated certificate retains the supplied scientific assessment, sources and limitations.
