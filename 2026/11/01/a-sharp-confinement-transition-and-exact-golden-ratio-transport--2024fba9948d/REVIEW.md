# Independent mathematical audit

## correctness

PASS

PASS. Since |rem(y,1)|<1, both |H(x)|<=|x|/k+1 and |H(x)|>=|x|/k-1 hold; the geometric iteration proves absorption for k>1 and escape beyond k/(1-k) for k<1. At k=1 the exact phase relation u_{j+1}={(1+a)u_j}, x_{j+1}=x_j+u_j on x>=0 plus odd symmetry proves eventual fixation iff bounded, using near-zero expansion of u. At a=phi-1 the two Markov intervals [0,phi^-1),[phi^-1,1) give an invariant positive piecewise-constant Parry density. The transfer operator preserves a four-dimensional affine-density subspace; the centered source vector satisfies the stated quadratic annihilator with eigenvalues phi^-1 and -phi^-2. Direct integration recovers all C_j, mean 1/sqrt5 and the exact finite-n variance sum; geometric-series resummation yields (5+3sqrt5)/50 and the constant correction. Independently verified density invariance and seven exact covariance lags symbolically, including the variance coefficient; read the real verify.py. No claim for arbitrary initial ensemble or nonlinear rem(a x,1) with nontruncating modulus.

## originality

PASS

PASS, with explicit classical-beta overlap. Moysis et al., Mathematics 2022, introduce exactly the remainder-added map and its normalizations, so that construction is not novel. The full accessible 2022 paper, especially its eq.(23) and the analysis of Lyapunov exponents and chaotic map behaviour, does not in the examined sections give a sharp all-k confinement boundary or exact stationary golden-phase all-lag covariance. The Parry density and ergodicity for golden beta maps are classical and specifically not counted as the contribution. The contribution is the exact unwrapped displacement covariance/variance for this concrete neutral remainder map, which is not logically implied by a general existence theorem for diffusion.

## value

PASS

PASS. Neutral dynamics separates bounded from escaping behaviour in an elementary yet discontinuous concrete model. A natural noninteger beta-Markov parameter has nonuniform invariant phase and correlated displacement, making its exact all-lag covariance and variance coefficient useful quantitative transport invariants. The result pinpoints deterministic drift bias relative to integer slopes; it does not imply cryptographic security or a Gaussian limit law.

The dated certificate retains the supplied scientific assessment, sources and limitations.
