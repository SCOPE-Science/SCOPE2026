# Independent mathematical audit

## correctness

PASS

For 0<alpha<1, every h_n in (0,1/2) tending to zero is fixed for the n+1 observations. Survivors are exactly [0,a_n], a_n=F^{-n}(h_n), since F is increasing and pushes positive states upward. Setting u=x^{-alpha} gives u_{j+1}=u_j-c_alpha+O(1/u_j), c_alpha=alpha*2^alpha, and u_j>=h_n^{-alpha} throughout survivor trajectories. Hence |u_j-u_0+c_alpha*j|<=C*n*h_n^alpha uniformly; at the upper endpoint a_n^{-alpha}=h_n^{-alpha}+c_alpha*n+O(n*h_n^alpha), whose relative error tends to zero for arbitrary cutoff sequences. Quoted local invariant density rho(x)~rho(1/2)/(2^{alpha+1} x^alpha) yields mu([0,y])~K*y^{1-alpha}; thus mu(E_n)~K(h_n^{-alpha}+c_alpha*n)^{-(1-alpha)/alpha}. Conditional B_n=X_n/a_n converges to Beta(1-alpha,1) by regular variation. For theta_n=n*h_n^alpha tending to finite theta, uniform inverse-coordinate estimates on B_n>=delta give C([0,1])-weak limit ((1+c_alpha*theta)B^{-alpha}-c_alpha*theta*t)^(-1/alpha) under X_j/h_n scaling. For theta_n to infinity, on delta<=B_n<=1-delta obtain n^(1/alpha)-rescaled limit [c_alpha(B^{-alpha}-t)]^(-1/alpha); endpoint singularity B=1 has probability zero. The proof is analytic, not inferred from finite numerical experiments. This is a horizon-dependent but within-trajectory fixed retention boundary; alpha>=1 and within-orbit moving holes are unproved.

## originality

PASS

Best-of-knowledge exact functional two-scale crossover for arbitrary shrinking retained neighborhoods. The inverse-iterate and density inputs are classical; the new aspect is the coupled n*h_n^alpha conditional C([0,1]) process limit including all finite and infinite theta. Related fixed-hole and opposite-hole escape works are not conflated with this claim. Priority is qualified: older renewal/neutral-fixed-point theory may imply the same limit in transformed coordinates.

## value

PASS

Conditioned survival near a neutral fixed point is a natural intermittent-dynamical question; the scale n*h_n^alpha separates three genuine conditional path laws and the exact survival-mass transition. The result identifies both scaling and full limiting trajectories for all deterministic boundaries, instead of a routine special case or only an exponent. No claim of new invariant density or general open intermittent-map theory.

The dated certificate retains the supplied scientific assessment, sources and limitations.
