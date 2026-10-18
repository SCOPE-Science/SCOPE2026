# Independent mathematical audit

## correctness

PASS

For all n>=2, fixed positive Poisson event rate Gamma and arbitrary Borel phase laws, normalized local rate g in [0,2] fixes EX=1-g for X=cos(theta). Maximizing E[T_n(X)] exactly gives the least GHZ decay 0 for even n, 0 for odd n and g<=1+cos(pi/n), and 1-T_n(1-g) otherwise. Even n supports +/-1; odd n has a concave upper envelope equal T_n on [-1,-cos(pi/n)] and 1 on the rest. Its second derivative is strictly negative in the left interior and its gluing derivative is zero; Jensen proves the unrestricted bound. The two explicitly symmetric atomic measures attain both branches and endpoints; Taylor gives coefficient n^2/(2sin^2(pi/n)). The GHZ qubit SLD calculation gives n^2*t^2*exp(-2Gamma_n*t). Independently evaluated Chebyshev second derivatives for n=3,5,7,11 as bounded corroboration, not an infinite proof.

## originality

PASS

The source physics manuscript gives the Poisson phase-kick generator, characteristic-function coherence factors, GHZ QFI, and some lattice exceptions. The new theorem optimizes the entire fixed-single-qubit-decay moment fiber for each n, with exact parity threshold and quadratic onset; these are not implied by a single deterministic lattice example or the ordinary dephasing rate formula alone. The exact one-moment concave-envelope technique is standard and not independently novel. An expanded version of the closest manuscript was not inspected completely; best-of-knowledge PASS subject to explicitly retained coverage risk.

## value

PASS

The inverse calibration question is natural in collective dephasing: a measured single-qubit decay does not determine multi-qubit GHZ survival. The exact all-size achievable envelope, parity obstruction and onset coefficient are quantitative limits useful for interpreting such noise characterizations, without asserting experimental robustness or globally optimal metrology.

The dated certificate retains the supplied scientific assessment, sources and limitations.
