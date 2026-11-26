# Independent mathematical audit

## correctness

PASS

The unperturbed energy identity gives the coefficient −rD_F(r) by integrating −xF(x)/r once around the circle and pairing x with −x. The finite affine flows and their crossing times are jointly smooth near any fixed regular circle with transversal crossings, so the expansion holds in C¹ there and a simple zero yields the stated locally unique hyperbolic crossing cycle and multiplier. Taking the odd difference of two step-affine changes leaves one baseline slope and at most two threshold terms, regardless of the signs of the switch locations. For distinct absolute radii each radial jump is genuine. Direct integration and differentiation give the displayed affine p_j in r². Below the first threshold the function is constant, so there are no simple zeros. Between thresholds the derivative has at most one zero. Beyond the second threshold the necessary cubic equation for a critical point is nonidentically zero: at s=a², p₁²(s−b²) has even order of vanishing and p₂²(s−a²) odd order, with both p_j nonzero. Squaring can add roots, but cannot lose a critical point. Rolle then gives the respective limits 2 and 4. Coincident absolute radii leave one affine numerator and at most two simple zeros; an identically zero term or flat interval gives none. The attaining affine pieces have genuinely nonzero jumps at 1 and 5. Separate 90-digit interval evaluation of the Abel formula at all twelve endpoints gives (+,−),(−,+),(+,−),(−,+),(+,−),(−,+) on the six stated brackets; none of the endpoint intervals includes zero. These force six distinct zeros, and Rolle's required intervening critical points exhaust the critical-point allowances, so all six zeros are simple. The independent witness replay is /workspace/branches/50b33517-9142-46a9-94f2-16bb2060db8b/independent_signs.py with independent_signs_certificate.txt beside it. The frozen verify.py was inspected, not executed; its replay is python verify.py with SymPy and mpmath. These finite sign checks certify the attaining witness, not the universal root bound. The count does not include grazing, sliding, multiple, flat or escaping-radius bifurcations.

## originality

PASS

The supported contribution is the universal first-order upper bound and forced regional allocation for two genuine jumps with arbitrary affine slopes and switch locations on either side. The known Abel expansion and six-root lower construction are not novel. Chen–Jin–Li–Lu's construction already selects two inner and four outer roots, but does not show this is exhaustive for its witness or forced for arbitrary maximizers.

## value

PASS

A matching upper bound closes the first-order regular-circle problem left open by the six-root construction. It identifies where every maximizing system must place its roots and separates the equal-absolute-radius degeneration, without conflating first-order cyclicity with the unresolved unrestricted cycle problem. The simple cubic certificate gives a transferable root-count method for this natural switching geometry.

The dated certificate retains the supplied scientific assessment, sources and limitations.
