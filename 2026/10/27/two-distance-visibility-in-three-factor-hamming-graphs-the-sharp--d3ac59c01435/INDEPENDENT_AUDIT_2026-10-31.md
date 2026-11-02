# Independent mathematical audit

## correctness

PASS

Every selected pair must have Hamming distance <=2. For a non-planar diameter-2 anticode, choose (0,0,0),(1,1,0): all off-plane points have crossed types (0,1,t) or (1,0,t); one type forces containment in a radius-one ball, both force a four-point parity tetrahedron. Inside a plane, geodesic visibility is exactly C4-freeness of its selected zero-one matrix; balls and tetrahedra satisfy visibility. Thus maxima are max{a+b+c-2,Z(a,b),Z(a,c),Z(b,c)}; disjoint carrier counts give the displayed multiplicity. Row-pair counting proves Z(q,q)=3,6,9,12,16 for q=2..6. The circulant difference set {0,1,3} proves Z(q,q)>=3q for q>=7. Independent direct geodesic search over all subsets of (2,2,2),(2,2,3),(2,3,3) reproduces (max,count)=(4,10),(5,12),(6,30). General q uses the structural argument.

## originality

PASS

The published k-distance mutual-visibility introduction gives definitions and bounds, and ordinary two-factor Hamming visibility is equivalent to C4-free bipartite packing, yielding Z(r,s). Previously studied total mutual visibility of three-factor Hamming products has a different universal quantifier over all ambient vertex pairs. The new diameter-2 three-carrier upper bound, exact multiplicity, and threshold q=6 are not supplied by these primary results.

## value

PASS

A natural finite-graph visibility invariant for the canonical three-factor Hamming product reduces exactly to a classical difficult extremal problem. The sharp q=6 transition explains which geometry governs the maximum, and multiplicity enumerates all maximizers while leaving larger Zarankiewicz values explicitly open.

The dated certificate retains the supplied scientific assessment, sources and limitations.
