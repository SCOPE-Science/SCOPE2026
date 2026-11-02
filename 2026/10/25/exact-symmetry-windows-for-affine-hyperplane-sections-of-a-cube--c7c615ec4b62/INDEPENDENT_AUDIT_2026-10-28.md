# Independent mathematical audit

## correctness

PASS

Reflect negative normal coefficients so the cut is sum(w_i y_i)=t with w_i>=0 and 0<t<W; coordinates w_i=0 contribute a passive cube factor. r<=2 gives point/segment factors, hence symmetry. For r>=3, restrictions of distinct coordinate normals to L={v:sum w_i v_i=0} are never proportional because a third positive weight prevents e_i-lambda e_j being a multiple of w. In a centrally symmetric section facets necessarily pair by parallel opposite outward normals. Thus every coordinate active as a facet has both y_i=0 and y_i=1 active and symmetry center coordinate 1/2. Since the active normals span L*, at least r-1 distinct coordinates are active. If r all, center y_i=1/2 implies t=W/2; if exactly r-1, the omitted coordinate inequalities are redundant, and solving y_j=(t-sum_{i!=j}w_i y_i)/w_j over the entire (r-1)-cube yields W-w_j<=t<=w_j, so w_j=m. The converse follows by central complement or affine cube parametrization. Classification includes endpoints and full Cartesian passive factors: r<=2 or t=W/2 or W-m<=t<=m. Independent exact rational vertex-and-central-reflection tests of 3330 sections (dimensions 3,4, weights 0..3) all matched. Finite checks corroborate the all-dimensional facet proof.

## originality

PASS

Metric central symmetry of every affine hyperplane section is resolved by an exact normal-weight/offset criterion, unlike previously studied graph reconstruction, vertex counts or center-only extremal sections. Relevant 1996 vertex-spanned hyperplane full text was not obtained, so historical priority remains qualified.

## value

PASS

The dichotomy between central slices and genuinely off-center affine parallelotopes gives a complete geometry of symmetry for all cube hyperplane cuts, not merely isolated examples. The exact dominant-normal interval [W-m,m] and vertex/facet classification can be used directly in cube section and zonotope questions. It naturally sharpens the basic fact that through-center cube sections are symmetric.

The dated certificate retains the supplied scientific assessment, sources and limitations.
