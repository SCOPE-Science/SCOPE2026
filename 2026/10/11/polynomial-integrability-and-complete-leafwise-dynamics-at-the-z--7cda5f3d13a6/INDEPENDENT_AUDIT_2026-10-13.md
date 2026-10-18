# Independent mathematical audit

## correctness

PASS

At a=0, u=x+y has u-dot=2y and H=z+u²/4 has H-dot=−uy+(u/2)(2y)=0. K=2y−(1+H)u+u³/12 similarly has K-dot=0. Polynomial inverse y=(K+(1+H)u−u³/12)/2, x=u−y, z=H−u²/4, and globally constant Jacobian determinant −2 verify a polynomial automorphism. Scalar u-dot=P=K+(1+H)u−u³/12 has inward cubic tails, hence all initial finite trajectories bounded and forward-complete; scalar order gives convergence to roots. Potential G=Ku+(1+H)u²/2−u⁴/48 satisfies dG/dt=P²=4y², so compact stationary measures force y=0 support, all equilibria. Cubic equation discriminant 432[16(1+H)³−9K²] gives all 3-root, double-root and single-root regimes; between adjacent roots each bounded complete orbit forms one heteroclinic modulo time translations. At cusp P=−u³/12 yields u~sign(u0)√(6/t), and fold P=−(u−r)²(u+2r)/12 yields t(u−r)→4/r on approaching side. Independently checked both polynomial first integrals and det=−2 in SymPy; read complete package verifier code.

## originality

PASS

The model’s original Pehlivan–Wei 2012 source introduces same three-dimensional system and generic chaotic/Hopf analysis; the accessible abstract/early preview do not provide a zero-coupling polynomial automorphism or complete leafwise invariant-measure/heteroclinic census. A 2021 mixing application uses a=2 numerical trajectories, not this integrable a=0 regime. Original 2012 remaining primary pages are inaccessible (publisher 403 and Oxford VPN disconnection), explicitly retained as significant uncertainty; inaccessible alone does not warrant O failure.

## value

PASS

The exactly zero coupling is a mathematically motivated singular boundary of a canonical 3D chaotic model. Two independent polynomial integrals and a global polynomial conjugacy expose every invariant leaf, complete heteroclinic census and explicit cusp/fold relaxation rates, and forbid all nonstationary invariant probabilities. These structural model-specific statements are not routine after only observing the equilibrium plane, even though scalar gradient deductions afterward are standard.

The dated certificate retains the supplied scientific assessment, sources and limitations.
