# Independent mathematical audit

## correctness

PASS

For cut depths a,b,c>=0 and q=a²+b²+c² in (0,1/2), (a+b)²,(a+c)²,(b+c)²<=2q<1, so the three similar removed corner triangles have disjoint interiors. Thus area(K)=(1-q)/2. Edge-length/support-function formula V2(K,-K)=1/2 sum_F length(F)h_{-K}(unit outward normal) over the up-to-six edges simplifies to 1-s+ab+ac+bc with s=a+b+c. Therefore Δ=1-V2/(2 area K)=(2s-s²-q)/(2(1-q)). Fixed q gives a continuous interval sqrt(q)<=s<=sqrt(3q); derivative (1-s)/(1-q) is positive up to 1, negative after. The minimum is at one nonzero cut a=sqrt(q), giving sqrt(q)/(1+sqrt(q)); the maximum at equal cuts when q<=1/3, or at s=1 when q>=1/3, giving plateau Δ=1/2. Equality cases hold exactly by Cauchy–Schwarz and s-level feasibility. Independent convex-hull mixed-area calculations for five separate polygon choices matched exact identities within 3.4e-16. This is an exact 2D calculation, not extrapolation from numerical optimization.

## originality

PASS

The general Godbersen inequality and simplex equality cases are known. A published one-vertex truncation profile gives the one-cut boundary; a quadrilateral reflected mixed-area formula does not include generic hexagonal three-cut bodies. The exact two-parameter fixed-q optimization and transition at q=1/3 are not established by the inspected references; corpus records were summary-level only.

## value

PASS

The fixed-removed-area problem is a natural stability refinement of sharp Godbersen equality, not just a reparameterization of the general inequality. The exact one-cut minimum, equal-cut maximum and nontrivial plateau transition at q=1/3 classify a three-dimensional cut family with clear extremizers; an exact result useful when comparing truncated simplices.

The dated certificate retains the supplied scientific assessment, sources and limitations.
