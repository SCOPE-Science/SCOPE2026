# Independent mathematical audit

## correctness

PASS

Reconstructed six-compartment stationary equations directly from Frieswijk–Zino–Cao Proposition 5 equation (18): for fixed group masses epsilon and 1-epsilon, total infected fractions and mildly infectious fractions satisfy the stated balance relations. Eliminating quarantined compartments gives u/(1-u)=(M z)_1 and w/(1-w)=(M z)_2. Under the two critical conditions M=[[1+(R-1)epsilon,(1-1/R)(1-epsilon)/s],[s(R-1)epsilon,1-(1-1/R)epsilon]]. Independently expanded det(M)=1, trace(M)=2+epsilon(R-1)^2/R>2. Strictly positive M has Perron root >1; a positive Perron subsolution, unit supersolution, monotone iteration and strict subhomogeneity yield exactly one positive fixed point besides the origin. Setting epsilon=t^3, u=tU, w=t^2W leads to U^2=B W, W^2=C U, with unique positive solution and Jacobian determinant 3BC>0. Implicit function theorem establishes the claimed epsilon^(1/3), epsilon^(2/3) and population prevalence coefficients; reconstructed compartments are biologically admissible. Symbolic independent determinant and cubic-balance checks passed; finite residual tests do not establish this limit.

## originality

PASS

Qualified PASS: Frieswijk–Zino–Cao model and threshold equations are prior, but the paper explicitly assumes sigma_v=1 for its analytic endemic Theorem 2, disjoint from positive vaccinated-to-others coupling sigma_v<1. Hiraoka–Rizi–Kivelä–Saramäki treat static-network SIR percolation final sizes and herd-immunity thresholds, not the two-way SIQS endemic equilibrium. Wang–Gracy–Ishii–Johansson prove a generic modified SIS spectral-root criterion, not the jointly tuned epsilon^(1/3), epsilon^(2/3) singular exponents with SIQS constants. No inspected prior statement or stronger theorem automatically implies the exact limiting law. A general two-type critical bifurcation literature may contain an equivalent scaling result.

## value

PASS

This resolves a genuinely motivated critical-mixing limit in the source epidemic model. The minority epsilon produces total endemic burden of larger order epsilon^(2/3), with distinct group fractions epsilon^(1/3) and epsilon^(2/3), exact constants and unique endemic existence. The nonlinear singular behavior is not captured by the source linear invasion criterion.

The dated certificate retains the supplied scientific assessment, sources and limitations.
