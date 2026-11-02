# Independent mathematical audit

## correctness

PASS

PASS: From the actual RESULT.md (Git blob 5f240788a14bb48d5c59f246357fc8ea18bc509f), the generator L f=omega^2 sum_i partial_ii f+Lambda^2 partial_omegaomega f+r[f(0)-f] yields E omega^2=2Lambda^2/r, E omega^4=24Lambda^4/r^2, E X_i^2=4Lambda^2/r^2, E X_i^2 omega^2=56Lambda^4/r^3, E X_i^2 X_j^2=224Lambda^4/r^4 (i != j), and E X_i^4=672Lambda^4/r^4. Centered h=omega^2-2Lambda^2/r and g_j=X_j^2-4Lambda^2/r^2 satisfy Lh=-rh, Lg_j=2h-rg_j; hence P_s g_j=e^-rs(g_j+2s h), yielding exactly the displayed covariance. Summing d^2 entries and integrating 2 int_0^infty Cov_Q(s) ds gives 32Lambda^4 d(19d+28)/r^5; dividing by (4d Lambda^2/r^2)^2 gives 2(19+28/d)/r. Regenerative stationarity and all polynomial moments are valid due to exponential cycle age. Independently rederived covariance and normalization across d=1,2,5,10 using private exact arithmetic (independent_extra.py: RESET_BATH_OK); checker.py and saved output were not treated as proof.

## originality

PASS

PASS, qualified: The direct antecedent establishes the common-resetting diffusing-diffusivity model and one-time stationary distributions, not this stationary two-time squared-coordinate kernel or evaluated Green–Kubo coefficient. The 2025 gas model computes equal-time squared-coordinate correlation without resetting and in a nonstationary regime. Neither supplies the all-lag stationary result by its stated theorem; general regenerative/renewal identities could conceivably yield the formula after further calculation.

## value

PASS

PASS: Squared spatial spread is a natural physical observable in a common fluctuating diffusivity environment; the exact stationary lag kernel quantifies persistent rank-one correlation. The non-vanishing 38/r normalized time-average error at large dimension, versus 94/(rd) with independent baths, is a meaningful quantitative breakdown of self-averaging, not a normalization-only exercise.

The dated certificate retains the supplied scientific assessment, sources and limitations.
