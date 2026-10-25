# Review: exact icosidodecahedral spherical contact law

## Correctness

PASS. The proof begins with actual normalized icosahedral edge midpoints and derives the four spherical Voronoi vertices and their orthogonal tangent directions. It then integrates the spherical radial Jacobian over a fully specified gnomonic diamond quadrant. Both endpoint coefficients are derived from local profiles rather than inferred from simulation. The standalone program independently reconstructs face incidences, compares angular integrals with the elementary CDF, checks normalization and support, and corroborates the predicted asymptotics. The critical exact-face identities are stated and derived in RESULT.md. This review does not represent external formal certification.

## Originality

PASS relative to accessible mathematical evidence. Na--Lee--Cheong (2001) provides the general spherical Voronoi machinery but not the particular thirty-vertex contact distribution; its complete available report was examined. published-finding corpus scientific comparison searches for the thirty-site distribution, aliases (rectified icosahedron, spherical edge midpoints, Voronoi radial law, cap coverage), and stronger coverage found results about spherical simplex cap unions, icosahedral section counts and width moments, which have different site sets or probability observables. Wang--Lee (2011) is a plausible adjacent source whose full text was not available; only the published abstract and metadata were reviewed, and priority remains uncertain. Search non-detection alone is not used as proof of novelty.

## Value

PASS. Thirty equidistributed directions of the icosidodecahedron are a canonical finite spherical code; its exact nearest-direction distribution determines the fraction of all orientations within any specified angular tolerance. The two transition thresholds distinguish initial cap collision, a change in which Voronoi vertices control the radial law, and total coverage. The endpoint exponents quantify local overlap onset and worst-case coverage sensitivity, information unavailable from a covering radius alone. The object and thresholds are intrinsic, with no arbitrary parameter slice.

## Residual limitations

The analytic result is restricted to uniformly sampled directions for this exact regular code. Adjacent icosahedral-grid literature not accessible in full leaves a historical-priority risk; independent review remains outstanding.

Self-review: passed. Independent audit: not yet performed.
