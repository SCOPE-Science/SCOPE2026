# Independent mathematical audit

## correctness

PASS

With Theta_t=Theta0+sqrt(2kappa)B_{t^beta}, velocity U_t=exp(iTheta_t) has E(U_t conjugate(U_s))=exp(-kappa|t^beta-s^beta|). Itô integration by parts for t>=1 with f=t^(1-beta)/(kappa beta) gives position as bounded/lower-order fU and f-prime terms plus martingale iv sqrt(2/(kappa beta)) integral t^((1-beta)/2)U_t dW. This martingale is square integrable at infinity iff beta>2, giving a.s. and L2 endpoint; for beta<=2 its quadratic variation grows T^(2-beta) or log T. After u=t^beta, angular second harmonic covariance exp(-4kappa|u-w|) and Young inequality force normalized bracket anisotropy to vanish; continuous martingale CLT proves the exact coordinate variances v^2/(kappa beta|2-beta|) for subcritical growing position and supercritical shrinking residual, v^2/(2kappa) at beta=2. The tail f and f-prime remainder is bounded O(T^(1-beta)), negligible under T^(beta/2-1). Integral of known MSD yields terminal gamma/beta second moment. Independently compared the asymptotic coordinate variance to half of known total MSD, and verified covariance kernel and power normalizations analytically. No claim endpoint itself Gaussian.

## originality

PASS

Sevilla et al. 2024 introduce exactly the scaled-angular model and its MSD identity: no novelty claimed for model, second moment, or gamma/beta evaluation. The assessment specifically considers almost-sure localization and vector Gaussian CLTs on both sides. Relevant primary full text could not be retrieved after arXiv/OA and authorized institutional attempts, leaving explicit priority risk. No source at hand decisively subsumes the full conclusion; best-of-knowledge PASS qualified.

## value

PASS

Identifies a sharp, nontrivial unconfined localization threshold for a constant-speed active particle, plus distinct Gaussian laws of diverging position and shrinking terminal error. These limit laws are not equivalent to a second-moment calculation and reveal the stochastic mechanism behind an unusual endpoint phenomenon.

The dated certificate retains the supplied scientific assessment, sources and limitations.
