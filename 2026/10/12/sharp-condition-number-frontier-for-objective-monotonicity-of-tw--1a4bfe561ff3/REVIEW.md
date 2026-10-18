# Independent mathematical audit

## correctness

PASS

PASS: For a complete two-step CSD cycle with reused alpha=1/a, normalized spectral gradient weights p_i and moments a, m2, m3, expansion of ((1-lambda_i/a)^4-1)/lambda_i gives energy change ||g||^2(2a^3-4a m2+m3)/(2a^4). Averaging (lambda-1)(kappa-lambda)>=0 and its lambda multiple yields endpoint bounds. When a<=(kappa+1)/4 the coefficient of m2 is nonnegative, so the endpoint-supported cubic Q_kappa(r) bounds all spectra; otherwise Jensen gives the strictly negative -a(2a^2-(kappa+1)a+kappa) since kappa*<3+2sqrt2. The cubic discriminant is 4(kappa-1)^6(kappa^2+1)(2kappa^4-10kappa^3+3kappa^2-10kappa+2), reducing under z=kappa+1/kappa to 2z^2-10z-1. Negative/zero/positive signs give strict descent/equality/positive-r ascent intervals; positivity of the remaining roots follows by Descartes sign count. The rational kappa=5 example has reused alpha=17/21 and objective ratio 5599232/5250987>1. An independently written SymPy checker verified the algebraic factorization/discriminant and exact rational witness; infinite dimensionality relies on the moment proof.

## originality

PASS

The first question is a worst-initialization, all-dimension one-cycle energy inequality, not a convergence-rate theorem. The closest complete CSD primary paper Li–Wang establishes exceptional non-superlinear periodic orbits and their decays, with no sharp uniform monotonicity threshold. Another paper introduces a different direction-modified algorithm. The 2005 foundational CSD asymptotics remain an explicitly material access risk.

## value

PASS

The distinction between convergent CSD cycles and one-cycle objective safety is operationally important: the first step is exact line search while the reused second step can raise the objective. An all-dimension sharp threshold 4.8937..., explicit open unsafe phase and 2D exact witness characterize when a natural delayed-gradient implementation retains a descent guarantee, beyond generic convergence rates or a mere isolated counterexample.

The dated certificate retains the supplied scientific assessment, sources and limitations.
