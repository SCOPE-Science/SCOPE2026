# Independent mathematical audit

## correctness

PASS

The frozen formulas are correct, but the iff statement in original RESULT.md line 32 omits R>r: with equal radii the point d=n(R−r)=0 is not interior, even though R/r<(n+1)/(n−1). The delivered RESULT.md fixes the radius-ratio criterion and rechecks the full phase law. The axial profile is the lower of the two spherical quadratics. The candidate has a≤b, so the ellipsoid's containment expression on each arc is convex in x and its maximum is at an endpoint. Independent exact algebra reproduces the right-tip excess, the aspect ratios, and equality at both transitions. In normalized coordinates the appropriate left-tip and latitude weights 1/(n+1), n/(n+1) give first moment zero and covariance I/n. With two poles and rim coordinate k=(R−r)/d the stated rim weight and pole weights satisfy the moment equations; p_+=(1−nk)/(2n(1−k)) proves the sharp nonnegativity threshold. The smaller-ball latitude lies inside the lens precisely at t−d≥r/n. The increasing quadratic g=d²+2dr/n+r²−R² locates d₀: for unequal radii, g(R−r)<0<g(n(R−r)) and g(R+r)>0. Thus the first transition is interior, and the second is interior precisely when R−r>0 and n(R−r)<R+r, i.e. 1<R/r<(n+1)/(n−1). Equality at the upper ratio is excluded tangency. For equal radii only the two-pole phase occurs in the proper-overlap domain. The normalized contact measures give a sufficient global optimality certificate, not just stationarity.

## originality

PASS

The corrected claim retains the supported distinct explicit all-dimensional unequal-ball intersection formulas and thresholds. Todd explicitly named the same optimization problem and approach, an important historical caveat, but the inspected passage does not give the formulas. Kahan's original result was recovered and is restricted to common centers; the paper explicitly leaves noncentered tightness as a complication. The nearest indexed statements concern the convex hull of unequal balls or the equal-radius lens slice. No exact encompassing theorem was established in the checked primary or indexed evidence. This is best-of-knowledge, not a claim to originating the problem or its method.

## value

PASS

The minimum-volume outer enclosure of a spherical lens is a standard geometric optimization object, and unequal radii produce a new set of potential contacts relative to the equal-radius case. Knowing exactly when the smaller ball remains optimal despite being clipped, when the right pole first becomes active, and which phases can occur provides more than an existence argument or a numerical approximation. The corrected transition condition prevents attributing an interior transition to a family in which only the two-pole regime is present.

The dated certificate retains the supplied scientific assessment, sources and limitations.
