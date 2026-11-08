# Independent mathematical audit

## correctness

PASS

For exact 2x2 stable symmetric diagonal A and fixed PSD Q, the source-described constant-forcing IF-SSPRK2 stages algebraically collapse to Phi(X)=DXD+(h/2)(DQD+Q), D=exp(hA); each entry contracts by exp(-h(ai+aj)). Solving stationary equations gives (Xh)ij=(h/2)coth(h(ai+aj)/2) qij, versus continuous qij/(ai+aj), producing Langevin error kernel d_a,d_b,d_m. The Langevin function L(t)=coth t-1/t is positive and strictly concave: sinh^3(t)>t^3 cosh(t), established by differentiating a positive auxiliary log ratio; thus log L is strictly concave. For q11*q22>0, det(E)=q11*q22*d_m^2*(theta^2-r^2) makes strict PSD/singular/indefinite cases exact; rank-one r=1 and a!=b gives indefiniteness for every h>0 while both Xs are PSD. Taylor and large-h expansions yield the claimed negative eigenvalue limits. Independently checked 12 numerical instances of exact stationary error and determinant sign.

## originality

PASS

Zhang–Lan–Jing 2026 construct positivity-preserving IF-SSPRK2 and finite-time convergence estimates; the exact stationary error Loewner classification by forcing correlation does not appear in accessible descriptions, although full stage source could not be inspected. Scalar trapezoidal stationary bias and continuous Gramian formulas are not claimed new. Related Riccati/exponential integrators are different maps. Qualified priority only.

## value

PASS

Stationary covariance is a natural uncertainty and model-prediction quantity. Showing that a PSD-preserving integrator can overestimate variance in some directions and underestimate in others at any h gives an actionable and exact two-mode matrix-order frontier, including a strong rank-one no-comparison obstruction.

The dated certificate retains the supplied scientific assessment, sources and limitations.
