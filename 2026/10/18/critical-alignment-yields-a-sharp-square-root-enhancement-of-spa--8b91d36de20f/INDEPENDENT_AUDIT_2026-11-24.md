# Independent mathematical audit

## correctness

PASS

Integrating the mass-one PDE gives m'=2(sinh m-m cosh m); this is strictly negative for m>0, and uniqueness and the sign imply positive m decreases to zero. The expansion is -(2/3)m^3-(1/15)m^5+O(m^7). Then u=m^(-2) satisfies u'=4/3+2/(15u)+O(u^(-2)); first u~4t/3, then u=4t/3+O(log t), and reinserting yields u=4t/3+(log t)/10+O(1). In particular the integrated m and m^2 terms have finite constant remainders after subtracting sqrt(3t) and (3/4)log t. The Fourier matrix has trace -2 cosh m and half diagonal difference sinh(m)-ik. Since k=2pi n>1, its root taking value i omega at zero is i omega-(k/omega)m+i m^2/(2 omega^3)+O(m^3). Thus the real parts are -1±(k/omega)m-m^2/2+O(m^3), and the gap is positive of order t^(-1/2). In analytic eigenvector coordinates the remainder R=-P^(-1)P_m m' is O(t^(-3/2)). Incorporate R_ii into the diagonal; the real gap retains its bound. The slow and fast graph ratios satisfy Riccati equations with respective negative and positive real linear coefficients and off-diagonal forcing O(t^(-3/2))(1+|ratio|^2). The forward slow integral from a large t0 with zero initial ratio and backward fast integral from infinity are contractions in a small bounded ball. For the forward kernel split at t/2: the early part decays exponentially in sqrt(t), while the near part has width O(sqrt(t)); for the backward kernel substitute v=(sqrt(t)+y)^2. Both yield graph ratios O(t^(-1)). The two independent graph amplitudes have integrable logarithmic-derivative corrections, so their leading constants are finite and nonzero; the fast line pulls back uniquely by invertibility. Integrating the slow real part gives -t+(sqrt(3)k/omega)sqrt(t)-(3/8)log t+C+o(1), and the divergent integrated gap ensures dominance outside the line. At fixed positive means the Fourier map can be perturbed in all four real directions by small sine and cosine waves, so the exceptional condition is real codimension two. At m0=0 a nonzero coefficient has order e^(-t) by bounded diagonalizing oscillations; a zero coefficient remains zero. Exchanging orientations and reflecting x covers negative m0. This is fixed mode and deterministic hydrodynamic time, not a uniform or microscopic asymptotic.

## originality

PASS

Credit the deterministic PDE, Curie–Weiss flip law, autonomous magnetization and generic techniques of asymptotic integration as prior. The checked literature does not identify the precise critical fixed-spatial-mode norm asymptotic, its logarithmic exponent, or its exceptional fast subspace for that PDE. Diagonalization at m=0, scalar critical magnetization decay, or diffusion in a stationary run-and-tumble model is not this assertion.

## value

PASS

Gives a sharp asymptotic in a physically distinguished critical regime of an existing evolution: the zero mode is only algebraic, whereas a fixed nonzero mode has an exponential law with a frequency-dependent subexponential enhancement and a universal power. The separate exceptional line and the contrast with exactly zero mean prevent mistaking a formal eigenvalue shift for a law of all perturbations. These dynamics are not determined by the spectral abscissa of the limiting matrix alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
