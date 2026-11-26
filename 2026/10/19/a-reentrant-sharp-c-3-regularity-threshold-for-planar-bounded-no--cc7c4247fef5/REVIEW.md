# Independent mathematical audit

## correctness

PASS

The compact fixed set is the convergent Minkowski series of contracted disks. Each summand has one supporting point for each unit normal; the series of these points is uniform. The total radius density ρ has finite integral by the geometric upper bound on each perimeter and is bounded below by ε. Integrating the sum against the continuous unit tangent gives the actual support-point displacement. The strictly increasing integral of ρ is thus the arclength coordinate, and the unit tangent extends continuously even at singular normal angles. Off the vertical normals, factoring out a^(2n) from the ellipse denominators gives a uniformly nonvanishing complex denominator on small neighborhoods and a geometric (b²/a)^n majorant, yielding real analyticity. At horizontal normals the radius is ε/(1−b²/a). At a vertical normal write t for the angle displacement, r=a/b>1, q=a²/b and N=floor(log_r(1/|t|)). The terms up to N are comparable to q^n, and the tail is bounded by a constant times q^N since q/r³=b²/a<1. This gives the finite vertical radius ε/(1−q) for q<1 and infinite radius for q≥1. The inverse arclength-to-angle derivative is 1/ρ, including zero by the inverse difference quotient at infinite radius. It is continuous and hence the regular curve is C². The C³ test is a C¹ signed curvature in arclength; by evenness, its derivative at the vertical point must be zero if it exists. For q<1, termwise differentiation is uniform when qr=a³/b²<1; otherwise the single Nth term gives a lower bound proportional to (qr)^N for the nonconstant curvature's difference quotient, including qr=1. For q=1 the difference quotient diverges as 1/(|t|log²(1/|t|)). For q>1 let α=log(1/a)/log(r). Then ρ is comparable to |t|^(α−1), |s| to |t|^α, and κ/|s| to |t|^(1−2α), ruling out α≥1/2, including b=a³. For α<1/2 the termwise bound |ρ_n′|≤3|cot(t)|ρ_n gives |dκ/ds|=|ρ′|/ρ³ bounded by a multiple of |t|^(1−2α); this verifies continuity, not merely existence, of the zero curvature derivative. These arguments establish the full iff, both curvatures, and the exceptional-point statement. The frozen verify.py was inspected but not run; it samples smooth summands and does not certify the phase boundary.

## originality

PASS

The complete sharp embedded-arclength C³ phase diagram, including both restored regimes and the endpoint at b=a^(3/2), is the supported distinct result. Tey's earlier thesis has genuine partial coverage beyond its diagonal example: credit the vertical curvature formula and prior obstruction in the open band a²<b<a^(3/2). Two related catalog records also overlap substantially in C² and parts of non-C³ or zero curvature. No date-based priority claim is made; the complete iff is not supplied or implied by the compared statements.

## value

PASS

This is the canonical planar anisotropic contraction with full disk disturbances, in a setting where precise embedded boundary smoothness is a documented question. The result rules out a single monotone regularity threshold: zero curvature can occur both with and without C³, and positive curvature does not ensure C³. The complete, sharp two-sided threshold and its equality cases give useful information about the actual geometric boundary rather than about the potentially singular parametrization by normals. It makes no higher-order or general nonnormal claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
