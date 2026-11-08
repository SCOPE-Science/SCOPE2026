# Independent mathematical audit

## correctness

PASS

For symmetric matrix with prescribed diagonal (a,b,c), determinant is abc+2xyz-az^2-by^2-cx^2. If at least two diagonal entries nonzero, take a,b!=0, d=ab-x^2 and w=z-xy/a to obtain det=dc-(d/a)y^2-aw^2. For d!=0 a nondegenerate binary quadratic form contributes q-chi(-d) solutions for unequal target and q+(q-1)chi(-d) at target zero, using standard quadratic character identity sum_t chi(t^2-D)=-1. If d=0, det=-aw^2 contributes q(1+chi(-delta/a)). Summing x and the special d=delta/c yields the boxed formula for k=2,3. For k=1, det=x(2yz-cx) gives (q-1)^2+q(1+chi(-delta/c)); for k=0, det=2xyz has (q-1)^2 nonzero fibers. Subtract summed nonzero fiber counts from q^3 to get zero counts for k=0,1,2,3 respectively 3q²-3q+1, 2q²-2q+1, q²-q+1, q²+1. Independently direct-enumerated all diagonals and all off-diagonal triples over F3,F5,F7 and checked each fiber, plus read the frozen verifier for q11/F9. Finite checks corroborate the exact character-sum proof for every odd prime power.

## originality

PASS

Results on general GL_n matrices with specified diagonal count non-symmetric invertible matrices, so do not imply determinant-by-determinant conditional fibers for symmetric 3x3 matrices. Existing symmetric determinant divisibility counts average over diagonal parameters and likewise cannot recover these conditional quadratic-character formulas. Hodges's 1955 symmetric-matrix exponential-sum paper is a genuine potential broad-priority source; open-access/arXiv attempts failed and authorized institutional access returned VPN disconnected. Its abstract/metadata do not resolve whether the specialized conditional theorem is implicit. Best-of-knowledge qualified PASS with explicit priority risk rather than treating inaccessible source as proof or automatic failure.

## value

PASS

An explicit exact determinant law with fixed diagonal is a natural distribution for low-rank finite-field symmetric matrices. The striking singular-fiber dependence only on k, versus nonzero-fiber square-class sensitivity, gives a complete algebraic classification useful for random matrix and quadratic-form enumeration, not an arbitrary small numerical table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
