# Self-review

## Correctness — PASS

The surface is the finite right circular cone lateral surface, with apex and rim retained and base disk omitted. The induced metric is \(ds^2=dr^2+t^2r^2d\theta^2\) for \(0<t<1\). The universal-cover argument treats the shortest angular lift and bounds every competing winding path of developed angle at least \(\pi\) below by the two radial lengths. This establishes the exact global two-point distance law, rather than assuming a local unfolding gives the global intrinsic distance.

Maximization over target azimuth and slant radius yields the maximum of the apex distance and antipodal-rim distance. Minimizing that maximum gives all three branches of the Chebyshev radius, including the sharp equalities at \(t=1/4\) and \(t=1/2\); rotational symmetry gives the complete locus. Integrating the exact squared-distance law against normalized area produces a strictly convex radial quadratic, whose unique optimal radius is \(2L\sin(\pi t)/(3\pi t)\). Monotonicity of the sinc and tangent quotients proves exactly two intersections of the minimizing radii. Convexity on the product of the radial intervals gives the diameter, and elementary branch monotonicity gives its sharp ratio to the Chebyshev radius. The proof treats the full continuum \(L>0\), \(0<t<1\), and all endpoint equality cases internal to that interval.

The bundled independent-of-the-derivation numerical checker `verify_cone_center.py` ran successfully: 2,857,130 counted finite checks across 66 shape ratios, 0 failures, 0 maximum discrepancy on the target grid, and direct quadrature agreement to the stated tolerances. The finite program is corroboration and not a surrogate for the proof.

## Originality — PASS, subject to historical-priority risk

The classical isometric development of cone geodesics is prior art. Slavík (2010), MathCurve and the cone-specific Clairaut exposition illustrate cone geodesics but do not address global minimax centers or area-weighted least-squares centers. Ahn et al. (2015) solve a geodesic-center algorithm on simple planar polygons, a different domain; a terrain facility-location report by Aronov et al. (2001) optimizes distances to finite prescribed sites and does not imply the whole-cone, all-target classification. A MathOverflow discussion (2025, updated 2026) distinguishes geodesic radius from average-distance poles but states no explicit cone classification. A related cone pairwise squared-distance energy gives an average over both source and target and does not determine the minimizing source radius, nor the minimax/Fréchet coincidences. A conical-frustum diameter theorem likewise does not determine the full minimax center locus.

Research-record semantic searches on exact claims, aliases, quotient/developable equivalents and stronger covering statements found no equivalent or dominating statement. These negative searches are not a novelty certificate; a specialized unindexed source on one-center problems for cones may predate this work. The asserted new claim is the joint complete intrinsic center-locus and intersection classification, together with its sharp radius/diameter law; the standard cone development and distance integral themselves are not presented as separate discoveries.

## Mathematical value — PASS

Chebyshev centers and area Fréchet centers are canonical but geometrically different center functionals on a compact intrinsic metric-measure surface. Their **entire optimizer sets** are classified on a natural one-parameter family, with two nontrivial isolated coincidences and a sharp covering-radius/diameter inequality. This identifies changes in metric center topology (parallel circle versus apex) and in the relation between global worst-case and mean-square dispersion. Those global shape results are not a mere isolated integral evaluation or an arbitrary parameter slice.

## Scope, limitations, and priority risk

The cone's base disk is excluded; including it changes intrinsic paths. The area functional uses squared distances and normalized *lateral* area, not first-power distances or ambient Euclidean squared distance. Shapes outside \(0<t<1\) are degenerations, not equality cases. Approximate coincidence angles and numerical checks do not establish rationality, algebraicity, or independent certification. Full historical priority remains uncertain, particularly in specialized cone geodesic-center literature.

Self-review: passed. Independent audit: not yet performed.
