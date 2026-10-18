# Mathematical assessment: silhouette law of the cube–octahedron family

## Correctness

PASS. The domain \(1\le t\le3\) and generic directions are explicit, including all parameter boundaries. For \(1<t<2\) the halfspaces give exactly the 24 axis–diagonal and 12 diagonal–diagonal edges, whereas \(2<t<3\) replaces the latter 12 by 12 axis–axis edges. The cuboctahedron retains only axis–diagonal edges. Summing edges separating facets with opposite normal signs gives the claimed five regimes. In the signed-permutation fundamental chamber the only changing diagonal normal signs are those of \((+,-,-)\) and \((-,+,+)\), precisely when the largest coordinate crosses the sum of the other two. The exact solid angle of the dominance cones establishes the asserted probability. A separate exact rational projected-hull checker verifies the facet inventory, edge graph, sign counts, and \(2358\) sample projections; finite tests are checks, not the infinite proof.

## Originality

PASS relative to inspected and recoverable evidence, without claiming definitive priority. The closest primary source, Gantapara et al., arXiv:1412.2597v1 (2014), defines and uses an equivalent continuously truncated-cube family but studies packings, mesophases, and orientational order, not planar projected polygon counts. Their earlier 2013 Physical Review Letters abstract likewise concerns phase behavior. Published exact results on the same family concern projected **area**, inscribed tetrahedral volume, centro-affine eigenvalues, or illumination number, none giving the vertices of the projected boundary. A previous central-section polygon law for a truncated octahedron concerns intersections rather than shadows. General asymptotic silhouette bounds and the classical separating-facet criterion supply background, not this exact all-parameter two-atom/one-atom classification. Search and implication checks are recorded in `AUDIT.json`.

Historical-priority limitations: Some public mathematical records could be read only as summaries because their linked full-text pages were inaccessible; an exhaustive survey of older visualization and computer-graphics literature has not been completed. These create a residual risk of prior coverage, but the available direct comparisons did not expose a dominating theorem.

## Value

PASS. This is a complete shadow-complexity classification of a natural three-dimensional convex-body interpolation, with exact Haar probabilities, equality regimes, and endpoint collapses. The invariant does not remain constant merely because a polytope has the same number of vertices: between the octahedron and cuboctahedron all generic shadows are dodecagons throughout an interval containing non-zonohedra, while between cuboctahedron and cube the count has two atoms with a parameter-independent, nontrivial exact probability. The classification supports both polyhedral shape discrimination and explicit checks of general silhouette algorithms; it is not an arbitrary isolated parameter evaluation.

## Scope and remaining risks

Generic orthographic shadow vertex counts only; exceptional directions, polygon metrics, perspective projections and higher-dimensional analogues are not determined. Numerical sampling cannot certify the all-direction statement and is not treated as such. General front/back facet separation is established background, rather than an originality claim. Independent mathematical validation and comprehensive historical-priority assessment remain outstanding.

Self-review: passed. Independent audit: not yet performed.
