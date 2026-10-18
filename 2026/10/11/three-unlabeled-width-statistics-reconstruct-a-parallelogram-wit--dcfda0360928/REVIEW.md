# Independent mathematical audit

## correctness

PASS

PASS. For a,b>0 and edge-line phi in (0,pi/2], W=a|cos theta|+b|cos(theta-phi)|. Direct integration independently agrees with mu=2(a+b)/pi, nu=(a²+b²)/2+(2ab/pi)[sin phi+(pi/2-phi)cos phi], and D²=a²+b²+2ab cos phi. Setting s=pi mu/2, X=s²-D² and Y=s²/2-nu gives T=Y/X=1/2-F(phi)/pi with F=(sin phi-phi cos phi)/(1-cos phi), F'=sin phi(phi-sin phi)/(1-cos phi)²>0. F runs from 0 to 1, so inversion uniquely recovers phi and ab, then sorted roots of t²-st+ab give unordered side lengths; T range [1/2-1/pi,1/2). On bounded nonflattening classes, all steps prior to roots are Lipschitz and sqrt discriminant gives uniform 1/2 Holder; perturbing equal sides (1,1)→(1+t,1-t) moves stats by O(t²) but lengths O(t), proving optimality at rhombi. Independently checked quadrature for multiple parameters. Degenerate phi=0 and sides=0 excluded; rectangle endpoint and rhombi included.

## originality

PASS

Best-of-knowledge PASS after exact-object and logical-implication comparison. Kim–Yaskin–Zvavitch projection-distribution counterexamples for arbitrary convex bodies do not imply either uniqueness or nonuniqueness of three moments+diameter on parallelograms. Finch's moment examples for a square or 3D regular polyhedra are special cases and cannot recover all arbitrary oblique side lengths or sharp inverse modulus. Orthotope tomography fixes right angles in higher dimension and does not dominate oblique parallelogram shape recovery. An indexed-search miss alone is not treated as novelty proof.

## value

PASS

PASS. Projection widths under anonymous directions are a natural geometric tomography observable. For the full 3-parameter class of nondegenerate planar parallelograms, only mean, second moment and support maximum recover the unordered side lengths and acute edge-line angle, with sharp global moment-range and optimal 1/2 inverse Holder modulus. This is a motivated complete inverse classification and stability boundary, not a table of one shape's moments or an arbitrary finite slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
