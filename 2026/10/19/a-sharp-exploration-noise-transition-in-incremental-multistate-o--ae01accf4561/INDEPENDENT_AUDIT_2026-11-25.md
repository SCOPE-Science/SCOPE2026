# Independent mathematical audit

## correctness

PASS

Verified RESULT.md:38–84 on the simplex, including ε=ε_c and initial boundary points. Reflecting flux balance and rates bounded below by ε/2 force every equilibrium to be a positive exponential tilt. For Z=sinh((k+1/2)s)/sinh(s/2), differentiating the product with sinh(s/2) yields Z''+coth(s/2)Z'=k(k+1)Z. Thus nonzero self-consistency is exactly E_s[J²]=k(k−ε). The derivative of E_s[J²] is the covariance, under the law of d=|J|, of d² and d tanh(sd), strictly positive for s>0. The attainable open range (k(k+1)/3,k²) gives precisely ε_c=(2k−1)/3 without a hidden finite-tilt branch at equality. The entropy derivative is the negative sum of edge flux times log rate-weight ratio; equality requires every flux zero. A fixed path of at most 2k nearest-neighbor jumps in one unit interval has uniformly positive probability for the time-dependent rates along any solution, so all components are bounded below at late times. Compactness, strict dissipation, and connectedness of the omega-limit set then give convergence to one of finitely many equilibria. The tangent Hessian is a positive diagonal form minus one rank-one term; its test is Φ''(m)Var(J) versus one. At a nonzero branch the derivative of m(s)−k(1+ε)tanh(s/2) is tanh(s/2)H'_k(s)<0 for s>0, with the same stability conclusion by reflection. At uniformity below threshold the Hessian has exactly one negative eigenvalue. Positive logarithmic-mean edge mobility is invertible on the tangent space, so the linearization has the opposite inertia. The global interior stable set of the saddle is contained in a countable union of inverse flow images of its local stable manifold, hence is null. The second derivative of E_s[J²] at zero is Var_0(J²), giving the stated square-root coefficient. Independently, for k=2, ε=1/2, the moment equation gives cosh(s)=(1+√6)/2 and m≈1.54721585869527. The frozen VERIFICATION.md reports 444 finite checks from checker_published.py, which was inspected, not executed. No finite-population or zero-noise convergence conclusion is inferred.

## originality

PASS

The distinct result is the exact threshold, branch moment identity, and global convergence classification for strictly positive adjacent-step exploration. The geometric shape of stationary laws and the idea of a three-way convergence classification cannot be credited in isolation: the former appears in the motivating paper and the latter is already present in a closely related zero-noise record. The inspected noisy categorical model is not the same generator, and the zero-noise results do not imply the positive-noise flow theorem.

## value

PASS

The monotone second moment resolves a real obstruction in using the geometric ansatz: it identifies every positive-noise equilibrium and the exact cutoff for each width without numerical branch tracing. Strict dissipation and the stability analysis turn a local onset into a global description, and the independent observable E[J²] gives an exact relation along the polarized branches. These are useful distinctions from the zero-noise endpoint consensus model.

The dated certificate retains the supplied scientific assessment, sources and limitations.
