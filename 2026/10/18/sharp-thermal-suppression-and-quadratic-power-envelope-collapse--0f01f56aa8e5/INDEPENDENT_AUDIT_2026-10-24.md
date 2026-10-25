# Independent mathematical audit

## correctness

PASS

The claimed process redraws the sign at Poisson rate alpha, so actual reversals have rate alpha/2 and correlation decay alpha. The pinned RESULT.md two-by-two Fourier resolvent is G=(s+alpha)/(s(s+alpha)+v^2 q^2) with s=Dq^2-i omega; an independent SymPy complex-division check reconstructed Im(G)/omega=[(alpha+Dq^2)^2+omega^2-v^2q^2]/([D^2q^4+alpha Dq^2+v^2q^2-omega^2]^2+(2Dq^2+alpha)^2omega^2). For moving probes omega=qV, the sign numerator is (alpha+Dq^2)^2-(v^2-V^2)q^2. AM-GM yields the exact cutoff V^2+4alpha D >= v^2; strict negativity at q=sqrt(alpha/D) on the other side, and solving the quadratic in |q| gives q_plus/minus and product alpha/D. Fourier power equals -mu rho0 V^2 times integral q^4 |U_q|^2 K dq/(2pi). A real nonnegative Schwartz Gaussian multiplied by 1+cos(q0 x) produces symmetric Fourier packets at q0 and the origin, with zero-mode contribution o(L) and strictly negative band contributions proportional to L, giving an honest fixed-L positive-power witness, not an inadmissible delta. At equality only isolated q can make K=0, so every nonzero real Schwartz U has negative coefficient when V is nonzero. Plancherel gives the exact L2 spectral supremum, though not necessarily an attained optimizer. Setting D=(v^2/4alpha)(1-eta), q=(2alpha/v)(1+sqrt(eta) z), and V=v sqrt(eta) y yields uniform finite-region leading term (16alpha^2/(9v^2)) eta^2 y^2(1-y^2-z^2); its maximum is 4alpha^2/(9v^2) eta^2 at z=0, y^2=1/2. This checks boundary V=0, normalization, and no claim at finite potential strength. Source verifier matrix inversion and quadrature were read; the independent algebraic check and full proof establish unrestricted quantifiers.

## originality

PASS

Best-of-knowledge original sharp all-Schwartz existence cutoff and power-envelope critical exponent/coefficient for the finite translational diffusivity extension. The foundational 2026 trajectory-response theorem determines the spectrum *implicitly* from a general response construction but does not state the finite-D all-speed iff criterion or maximize power near the thermal critical point. Earlier 1D negative drag studies omit independent Brownian diffusion or optimize different probe statistics. Literal parameter coincidence is not enough; the new uniform L2 spectral variational characterization and scaling are substantive specialized consequences, not claimed as a new general response principle.

## value

PASS

The independent thermal diffusion cutoff is a physically motivated sharp boundary for positive mechanical work in the 1D RTP weak-probe model. The all-speed impossibility and constructive nonnegative probe criterion are stronger than a plotted negative-response example. The exact L2-normalized maximal transferable-power asymptotic, quadratic critical exponent and unique limiting maximizing velocity/wave-number selection quantify suppression near D_c and are not mere substitutions of a constant into an existing formula. Meaningful even though restricted to ideal dilute baths, leading weak coupling and prescribed speed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
