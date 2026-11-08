# Independent mathematical audit

## correctness

PASS

For fixed m=2r+1, precisely m unordered vertex pairs at step r maximize polygon diameter 2cos(pi/(2m)), and their vertices are shared. In each corner cone the two longest-diagonal inward loss forms have slopes (q,p) and (p,q), where p=sin(pi/(2m)), q=sin(3pi/(2m)), and the edge-coordinate area Jacobian divided by polygon area is exactly 2/m. After scaling corner coordinates by sqrt(N), disjoint vertex neighborhoods converge jointly to independent intensity-2/m Poisson processes. Strict first-order transversality and positive gap outside neighborhoods justify localization and a uniformly O(N^-1) Taylor remainder, giving weak convergence of the minimum over finite diameter pairs. The two directional minima at one vertex are dependent and their joint survival is the Poisson void probability for union of two triangles; direct trapezoidal/midpoint integration confirms all piecewise intersection formulas. Each one-diagonal sum has CDF lambda² t^4/6+O(t^6). Pairwise diagonal intersections require at least 3 corner processes and contribute O(t^6), so inclusion–exclusion gives m lambda²/6=1/(6mp²q²). Finally small-angle limits give 8/(27 pi^4) versus even 1/(12 pi^4), ratio 32/9. Independent checks of 5 vertex gradients and 600 exact-versus-quadrature overlaps are supplementary only.

## originality

PASS

Lao (2010) Chapter 6 Theorem 6.8 treats area-uniform EVEN polygons, whose diametral corners are disjoint; Chapter 5 section 5.2 treats odd polygons with BOUNDARY/arclength sampling and shared endpoints, not the fixed odd area-uniform case with its sqrt(N) scaling and 2D cone intensity. Appel–Najim–Russo (2002) and Mayer–Molchanov (2006) address general random-point diameters; the precise role of repeated diameter endpoint maxima required a high-priority comparison. An authorized institutional retrieval of Appel et al returned VPN disconnected; only abstract and later summaries available, and that priority risk is explicitly retained. No decisive direct prior implication for the coupled bivariate law was established from accessible statements; do not claim absolute novelty.

## value

PASS

Random-sample diameter is a canonical geometric extreme statistic. Odd regular polygons are the first natural symmetric class where maximal-diameter chords share endpoints, so the missing dependence invalidates naive products of independent Weibull variables. The bivariate cone process and exact lower-tail coefficient are nontrivial geometry-probability invariants, not a minor constant gain. The parity contrast quantifies an important structural distinction from even polygons.

The dated certificate retains the supplied scientific assessment, sources and limitations.
