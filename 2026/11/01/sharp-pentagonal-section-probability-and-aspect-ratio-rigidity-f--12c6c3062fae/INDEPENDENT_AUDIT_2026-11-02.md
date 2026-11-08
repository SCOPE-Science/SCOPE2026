# Independent mathematical audit

## correctness

PASS

PASS: The pyramid centroid is (0,0,h/4), so after centering base z=−c, apex z=3c with c=h/4. For the chosen upper-hemisphere normal, opposite base-corner scalar products sum to −2cu_z, so the only generic pentagon event is ||a u_x|−|b u_y||<c u_z<a|u_x|+b|u_y|. Integrating four sign quadrants using the arcsine primitive yields p=(4/π)(arcsin(a/S)+arcsin(b/S)−arcsin(L/S)) with L²=a²+b², S²=L²+c². Exact differentiation gives one critical c, since c(a/√(b²+c²)+b/√(a²+c²)) increases strictly from 0 to a+b>L; balancing a,b at fixed diagonal is uniquely optimal at a=b; its height optimum c=a=b yields maximum 6 arccos(1/3)/π−2. Second derivatives give the stated diagonal negative Hessian. I independently checked derivative symbolically (identity TRUE), Hessian coefficients numerically and compared 50,000 Gaussian-direction edge counts on three asymmetric parameter triples (≤0.0015 discrepancy); sampling is not the proof.

## originality

PASS

PASS (best of knowledge), strictly excluding known square-case p*: The closest published right-rectangular pyramid random SHADOW law was read in full. Through polar duality it yields the square-case centroidal-section probability, so that number is NOT new. A nonsquare rectangle-base pyramid has a rhombic-base polar, and the nonorthogonal affine transformation that maps rhombus to rectangle does not preserve Haar orientation. Its shadow law therefore does not imply the general nonsquare section probability, the global aspect-height maximizer or local Hessian. Brandenburg–De Loera–Meroni supplies slicing chamber combinatorics; Black–Criado expected shadow bounds do not specify this exact law. Specialized unpublished rhombic-pyramid solid-angle formulas remain a risk.

## value

PASS

PASS: A complete Haar-oriented polygonal section law over a natural three-parameter right-pyramid family, with unique joint shape-height optimality and positive-definite quadratic stability, is a mathematically motivated geometric optimization result. It does not seek credit for the already-known square numerical constant or elementary polarity alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
