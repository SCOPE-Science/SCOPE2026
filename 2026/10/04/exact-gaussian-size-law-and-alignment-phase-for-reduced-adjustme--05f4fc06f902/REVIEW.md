# Independent mathematical audit

## correctness

PASS

Reconstructed Gaussian conditioning with residual variances tau_x^2+beta^T Sigma_perp beta and tau_y^2+theta^T Sigma_perp theta. Positive independent noises imply |rho|<1. Conditional regression gives Rx/sigma_x=rho U+sqrt(1-rho^2)E, with independent standard-normal U,E across observations. Conditional projection E^T U/||U|| has a fixed standard-normal law and is independent of U, so W=rho chi_n+sqrt(1-rho^2)G. The resampling reference is standard normal conditional on observed Ry; its two-sided tail gives the exact rejection integral. The denominator vanishes with probability zero for n>=1. At rho=0 size is exactly alpha; for n=1 the absolute statistic is normal in absolute value for every rho. The chi law of large numbers and bounded conditional variance prove local and divergent regimes; for 0<alpha<1 the normal-tail derivative proves strict local inflation. Conditional covariance and Cauchy-Schwarz prove the alignment formula, with rho=0 whenever either omission is zero or covariance cancels. Independent Simpson reconstructions on two meshes give 0.168815564178773 for n=100,rho=0.1 and 0.170075045753088 for kappa=1; these numerical checks supplement, not replace, the analytic proof.

## originality

PASS

Best-of-knowledge PASS only for the exact finite-n reduced-adjustment size integral and contextual alignment/cancellation diagnostic. Li-Liu A49 already gives the normalized normal-tail p-value; Niu et al. equations 21-22 already give local mean-shift inflation in a ridge-bias example. Gaussian chi-normal decomposition itself and the root-n shift mechanism are not separately novel. The inspected sources give error bounds or asymptotic results rather than this exact finite-n law under a fixed insufficient Gaussian reduction.

## value

PASS

The exact finite-sample validity diagnostic separates omission magnitude from alignment: two nonzero omitted directions can cancel, while collinearity attains the product-error order. The n=100,rho=0.1 example changes nominal 0.05 size to approximately 0.169. This is a motivated calibration benchmark for reduced-adjustment validity, not arbitrary parameter recomputation; the exact law and sharp correlation boundary provide information lost in magnitude-only bounds.

The dated certificate retains the supplied scientific assessment, sources and limitations.
