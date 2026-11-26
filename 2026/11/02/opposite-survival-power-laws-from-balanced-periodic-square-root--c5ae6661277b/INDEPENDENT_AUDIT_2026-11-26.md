# Independent mathematical audit

## correctness

PASS

The absolute-time phase is fixed along each residue-aligned d-step product. The Doob similarity gives a primitive stochastic limit P and the stated two orders, with the ordered two-A products at order T^-1. The fixed-support blocks need not individually be entrywise positive, but some fixed power of their limiting P is, and the corresponding products of normalized row maps are eventually uniformly contractive in total variation: their derivatives on zero-mass rows tend uniformly to that of the limiting fixed-block stochastic map. The trial probability row pi+T^-1/2 w is eventually positive and has one-block defect O(T^-1) because of centering, the Poisson equation and the O(T^-3/2) time shift; iterating the contraction gives an O(T^-1) row deviation. Its zero mass then produces multiplier 1+(pi D1+wC1)/T+O(T^-3/2), whose log-error tail is O(T^-1/2); the harmonic log has coefficient 1/d. The leftover s steps converge after Doob scaling to Q^s on a positive terminal vector, so the constants are strictly positive and the same error order holds. Centering is only required for the specified class/phase, and the Green series converges geometrically on zero-mass rows. Independent replay, `python3 /workspace/review-evidence/reproduce.py 3`, extracts the second-order coefficients from exact 2x2 characteristic polynomials, giving beta=-3/80 and 3/16 (swapped at odd phase), in agreement with the archived check; this verifies the example, not the infinite-time law. The killing factors remain positive and substochastic for every integer n>=1.

## originality

PASS

The supported distinction is the centered periodic finite killed-chain result with explicit class/phase-dependent exponent, residue error bound and a worked same-chain opposite-sign example. The local response coefficient is a standard simple-eigenvalue perturbation coefficient, and the scalar quadratic accumulation and appearance of critical-scale autocorrelation are not independently new. The strongest inspected statements do not establish this class-sensitive result or example. Priority against general discrete asymptotic integration is not settled.

## value

PASS

At the centered critical scale, a first-order stationary average predicts no class distinction and the exponential survival cost is the same. The two exact powers prove that a single killed chain can nevertheless exhibit increasingly unequal survival across initial cyclic classes, while the response formula specifies when second-order averaging alone fails. This is a structural distinction for a natural perturbative boundary, not a numerical extrapolation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
