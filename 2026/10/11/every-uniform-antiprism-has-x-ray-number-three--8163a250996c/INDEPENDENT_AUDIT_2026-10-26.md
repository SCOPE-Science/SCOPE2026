# Independent mathematical audit

## correctness

PASS

Reconstructed the all-integer n>=3 result for the Euclidean unit-edge uniform n-antiprism, with a=pi/(2n), H=sqrt(4cos(a)^2-1), and three unoriented line directions (cos(2pi j/3),sin(2pi j/3),H). Unit-edge geometry gives R=1/(2sin(2a)), h=H/(2cos a), and four outward facet normals e3, (gamma,0,-zeta), (gamma cos(2a), +/- gamma sin(2a),zeta), where gamma=H/(sqrt(3)cos a), zeta=tan(a)/sqrt(3). Verified gamma^2+zeta^2=1 and zeta H=gamma sin a. Their four strict scalar products reduce X-raying each upper vertex of angle theta to circular distance(theta,phi)<beta=pi/2-a; by bottom-face reflection/rotation, the lower criterion is circular distance(theta-pi,phi)<beta. For n>3, beta>pi/3 and 3 arcs of centers 0,2pi/3,4pi/3 cover every angle; for n=3 the only uncovered angles are arc midpoints, while all transformed upper/lower vertex angles are arc centers. Inclusion of each face Gauss image in an incident vertex Gauss image covers the full boundary; the universal d-dimensional X-ray lower bound gives X>=3. Verified failure of the almost-smooth condition because e3 dot m0=-tan(a)/sqrt(3)<0<1/2. Independently regenerated convex hull facets of both vertex rings and numerically tested all incident outward normals and strict direction signs for every integer 3<=n<=120 (without relying on packaged verify.py), maximum unit-normal mismatch 1.30e-15 and smallest computed best-direction strict dot 0.1139. This finite diagnostic does not establish the quantified theorem; the exact trigonometric proof does.

## originality

PASS

Best-of-knowledge all-n X-ray theorem is not implied by inspected full primary literature on general almost-smooth bodies or ordinary illumination of two-plane convex hulls. The closest exact X-ray published result on Platonic solids covers only the n=3 octahedral endpoint; the exact-match Resultary entry is the audited work mirrored, not independent earlier coverage. Actual semantic published-record and multi-alias targeted web searches found no independent all-n uniform-antiprism X-ray result, but negative searches are not novelty proofs. A general classical result hidden in older illumination literature remains a priority risk.

## value

PASS

Uniform antiprisms form a canonical infinite family of convex uniform three-polytopes, making their exact X-ray number a natural geometric invariant. The n=3 regular octahedron case is already known, but the theorem resolves every n>=4 simultaneously, including an explicit dimension-minimal three-direction certificate with unchanged 120-degree azimuths and a natural n-dependent common slope. The proof connects vertex normal cones to exact circular arcs and shows the family is outside the only close broad sufficient class of almost-smooth bodies. This is a mathematically motivated family-level classification rather than a named-object substitution or a finite catalog.

The dated certificate retains the supplied scientific assessment, sources and limitations.
