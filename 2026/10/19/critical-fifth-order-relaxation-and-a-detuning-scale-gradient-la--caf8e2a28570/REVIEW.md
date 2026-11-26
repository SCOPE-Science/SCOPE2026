# Independent mathematical audit

## correctness

PASS

With u=sin x the coefficients of u,u^3,u^5 in sqrt(pi) times the wave are 3cos(beta)+5sin(beta), -4cos(beta)-20sin(beta), and 16sin(beta). At the claimed angle these give a cubic coefficient c=-40/sqrt(34*pi) and a derivative with respect to shape of the linear coefficient of -sqrt(34/pi). At the critical shape the center graph h starts at order x^2; its invariance gives h(x)=mu*c*x^3/(1-mu)+O(x^5) since the position displacement is initially O(x^4), making h(x_next)-h(x)=O(x^5). Substituting gives the reduced map x_next=x-K*x^5+O(x^7), K=3*C*mu*c^2/(1-mu). Its reciprocal-fourth increments tend to 4K, giving the stated coefficient. Local center stability and exponential tracking apply to the smooth locally invertible map with transverse multiplier mu. The vertical invariant line is exactly the local strong-stable manifold; the position displacement is less than |x|/2 sufficiently near zero off that line. On detuning, the two quadratics in u^2 for a wave zero and an extremum have unique small positive roots only for negative detuning, with leading coefficients 17/20 and 17/60, respectively. The wave-zero Jacobian has determinant mu*(1+C*Psi'^2) and satisfies the strict Schur tests for sufficiently small nonzero detuning; the extrema have one multiplier mu and one greater than one since Psi*Psi''<0. Under x=sqrt(epsilon)*X and w=epsilon^(3/2)*W, the memory error from mu*A_sigma(X)/(1-mu) is bounded by mu^n times the initial error plus O(epsilon) on bounded X sets. The step size for X is epsilon^2; the cumulative consistency error is O(epsilon) on a finite slow interval plus a summable O(epsilon^2) transient. The confining squared wave polynomial bounds the limit ODE, and a stopped discrete Gronwall bound extends convergence throughout the interval. This also gives memory convergence away from slow time zero. The frozen verifier was read, not run; its recorded numerical diagnostics are not used as proof.

## originality

PASS

Credit the published map, test family, stability conditions and qualitative fixed-point branches, as well as generic quintic relaxation in other systems. The supported distinct content is the sharp exact-map critical relaxation off the identified strong-stable set together with the finite-time detuning-scale gradient limit and slaved-memory statement. Neither the critical angle nor the fixed-point count is relied on as a stand-alone novelty.

## value

PASS

At the physically specified wave shape, the usual linear stability test is inconclusive. The exact coefficient gives a local relaxation benchmark and distinguishes exponentially decaying memory on the vertical line from generic algebraic position decay. The detuning limit explains the neighboring one- and three-sink configurations dynamically with an explicit slow timescale and controls actual trajectories, not just equilibrium locations.

The dated certificate retains the supplied scientific assessment, sources and limitations.
