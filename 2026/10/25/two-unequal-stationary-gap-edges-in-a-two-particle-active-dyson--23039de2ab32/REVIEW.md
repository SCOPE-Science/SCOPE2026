# Independent mathematical audit

## correctness

PASS

The ordered two-particle equations give Gdot=-lambda G+2g/G+2vS with S=(sigma2-sigma1)/2 in {-1,0,+1}, switching -1,+1 to zero at rate 2gamma and zero to each outer at gamma. The negative drift derivative -lambda-2g/G^2<-lambda gives pathwise exponential contraction; extreme drift roots a=(sqrt(v^2+2lambda g)-v)/lambda and b=(sqrt(v^2+2lambda g)+v)/lambda bound the exact invariant gap support. Integrated stationary conservation equations have zero endpoint currents. At a+epsilon the attracting mode -1 has field -h_a epsilon+O(epsilon^2), h_a=lambda(a+b)/a, while the other two fields point strictly right; integrated mode masses satisfy H0=O(epsilon H-), H+=O(epsilon^2 H-). Positivity of H- and the flux identity give d(log H-)/d epsilon=2gamma/(h_a epsilon)+O(1), hence a finite strictly positive C_a and exponent alpha_a=2gamma/h_a; differentiating through flux gives p_G~C_a alpha_a epsilon^(alpha_a-1). At b the symmetric calculation gives h_b=lambda(a+b)/b and alpha_b=2gamma/h_b. The exact thresholds h_b/2=lambda K/(K+v)<h_a/2=lambda K/(K-v), K=sqrt(v^2+2lambda g), give the stated three divergence/vanishing regions, finite positive critical limits, and alpha_a+alpha_b=2gamma/lambda, alpha_b-alpha_a=2gamma v/(lambda K). Fresh symbolic SymPy identities establish the algebra independently; the finite-volume code in the package was inspected as a bounded corroboration only, not used to prove asymptotic power laws.

## originality

PASS

The published active-Dyson model and its support bounds, generic two-particle RTP transport ODEs, and linear-force telegraph edge exponents are all prior art. The assessed conclusion specializes the nonlinear reciprocal-force gap and extracts *both* explicit unequal edge powers, positive amplitudes, thresholds and full sign-regime ordering; its priority must be qualified given the general ODE literature.

## value

PASS

The gap marginal is an intrinsic two-particle observable whose near-contact and maximal-separation event rates quantify physical stationary structure. Two distinct thresholds and the impossible reverse mixed regime are motivated, parameter-uniform consequences absent from single-particle data. Exact positive-power laws for both ends are independently useful even without a closed-form interior density or amplitudes.

The dated certificate retains the supplied scientific assessment, sources and limitations.
