# Independent mathematical audit

## correctness

PASS

For a genuine supporting-base pyramid K=conv(F∪{a}), every extreme point besides a lies in F and the apex is unique. Distinct cone directions have distinct apexes because the base is the closed convex hull of all extreme points except the apex. For k directions, affine functionals ell_i vanish on respective bases, are positive at a_i and vanish at all other apexes; these imply the apices are affinely independent, k<=n+1. If k=n+1, all other extreme points would lie in the empty intersection of the simplex facet hyperplanes, forcing K to be that simplex. If k<=n, full-dimensionality gives another extreme point b lying in every H_i; translating the functionals to b makes their linear normals independent, so the common affine intersection L has dimension n-k. With B=K∩L, Krein–Milman (finite-dimensional) gives K=conv(B∪{a_i}) and full-dimensionality forces dim B=n-k. For k=n or n-1 this makes B a point or segment and K a simplex, contradicting k<n+1. Conversely simplices have n+1 apex directions. For every 0<=k<=n-2, pyramid over an m=n-k>=2 cross-polytope has exactly k cone apexes: deleting any ±e_j leaves a set affinely spanning the base m-space, so no cross-polytope vertex is an apex. Separately coded exact SymPy rank checks verified every k for 2<=n<=10 (54 cases), corroborating witness arithmetic only, not providing the universal proof.

## originality

PASS

Best of knowledge: a direct same-object manuscript proves only finiteness and explicitly conjectures the upper bound. Older free-join/pyramid-vertex results have different hypotheses and do not determine the universal exact spectrum or residual full-dimensional base. Resultary returns an exact-match mirror of the assigned result rather than independent coverage. A classical implicit affine-join classification remains a genuine historical risk; absence in searches is not certification.

## value

PASS

The theorem settles the specific n+1 simplex-only cone-direction question posed immediately after Feldman’s 2026 finiteness lemma. It strengthens that bound to the full dimension-by-dimension set of possible counts, excludes n and n−1 outside simplices and canonically identifies the residual base of every nonsimplex cone in arbitrary full-dimensional convex bodies, including nonpolytopal ones. These are motivated precise structural facts not arbitrary finite slices or a mere numerical test. The proof uses elementary affine geometry, but the explicit recently stated question and additional decomposition give it independent mathematical significance.

The dated certificate retains the supplied scientific assessment, sources and limitations.
