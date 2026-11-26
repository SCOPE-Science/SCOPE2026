# Independent mathematical audit

## correctness

PASS

Under x=se+M^(1/2)y the section cuts the unit ball at signed offset (t-sw)/sqrt(q), where w=u·e and q=u^T M u. The hyperplane Jacobian is sqrt(det M)/sqrt(q), so the four-volume is a nonvanishing angular factor times (h+2zt-t²)², with z=sw and h=q-z². Since q-z²=b²(1-w²)+(a²-s²)w² is uniformly positive, a common interior interval exists. Five distinct offsets in that interval recover all monomial coefficients by Vandermonde interpolation, proving the lower bound even for arbitrary separable factors. At s=0 the span is {1,h,h²}, of dimension 1 or 3 according as h is constant or nonconstant. At s≠0, h=b²+βz² with β=(a²-b²-s²)/s² and z ranges over an interval. The odd coefficients span {z,b²z+βz³} and the even ones span {1,(4-2β)z²-2b²,(b²+βz²)²}. The respective dimensions are (1,2) at β=0, (2,2) at β=2, and (2,3) otherwise. The leading pivots also give the stated determinant 32β³(β-2). Both exceptional conditions require a>b. This independent symbolic reconstruction proves every regime; the frozen CHECK.py is an inspected cross-check, not the basis of the lower bound.

## originality

PASS

The closest recorded analogue classifies ranks in dimension three and already identifies a focal exception there. The available primary rigidity theorems identify possible bodies but do not give the minimal local rank. The exact five-dimensional classification, especially the second exceptional displacement, is distinct on the checked evidence.

## value

PASS

Minimal rank measures the exact number of angular and offset channels, a quantitative refinement of local separability. This is the complete axial family in the first odd dimension above the three-dimensional example, not a chosen parameter slice. The second exceptional position changes the minimal channel count without having the focal geometry; the parity split explains why expanding the quartic alone misses it.

The dated certificate retains the supplied scientific assessment, sources and limitations.
