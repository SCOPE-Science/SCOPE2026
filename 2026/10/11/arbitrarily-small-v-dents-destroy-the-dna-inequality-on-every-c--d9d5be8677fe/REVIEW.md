# Independent mathematical audit

## correctness

PASS

For every C2 regular convex Jordan boundary Gamma, curvature is nonnegative and integrates to 2pi, so some point has kappa>0. In tangent coordinates f(x)=kappa x^2/2+o(x^2), f_prime(x)=kappa x+o(x). For endpoints (-t,f(-t)), (t,f(t)) and V vertex (0,kappa t^2), segment slopes are +kappa t/2+o(t), -kappa t/2+o(t). The unique reflex corner has negative turn -kappa t+o(t); signed total turn stays 2pi so absolute total curvature is 2pi+2kappa t+o(t). Arc length 2t+kappa^2 t^3/3+o(t^3), new segments length 2t+kappa^2 t^3/4+o(t^3); perimeter p-kappa^2 t^3/12+o(t^3). Thus average curvature ac(dented)=2pi/p+(2kappa/p)t+o(t). Removed cap is contained in O(t^2) boundary layer. If B(o,r) subset int K, homothety K_epsilon=o+(1-epsilon)(K-o) satisfies K_epsilon+epsilon rB subset K; taking epsilon=M t^2 with Mr above cap-depth constant places it inside the dented cell. Its average curvature 2pi/((1-Mt^2)p)=2pi/p+O(t^2) is strictly smaller. SymPy independently verified slopes, reflex coefficient and length defect. This is local existential for a specific V-dent family; neither every dent nor smoothness of the dented boundary is asserted.

## originality

PASS

Classical Lagarias--Richardson proves the DNA inequality for convex cells, which does not control the nonconvex V dent. Larson describes nonconvex DNA inequalities and classifies polygonal dents; the supplied record cites a Section9 explicit suggestion of the smooth-convex dent corollary, but the full Larson paper was not independently accessible this run (arXiv PDF retrieval failed; subsequent authorized retrieval was safety-blocked). Only Larson abstract was materially viewed. The independent calculation supports a naturally motivated smooth extension, and indexed searches found no decisive broader proof; residual risk about Larson full Section9 and later papers is retained rather than manufacturing a whole-document comparison.

## value

PASS

A classical convex-body DNA inequality has a geometric stability boundary: an arbitrarily shallow O(t^2) inward dent has a first-order O(t) absolute-curvature penalty, while a valid competing inscribed homothetic curve loses only O(t^2). This proves a structural sharp scale separation for all C2 convex cells, a natural smooth counterpart to polygonal-dent classifications, not a small arbitrary numerical example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
