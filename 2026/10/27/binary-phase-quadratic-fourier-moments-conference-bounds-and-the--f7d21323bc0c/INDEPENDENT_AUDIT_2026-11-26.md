# Independent mathematical audit

## correctness

PASS

On the continuous normalized torus the squared norm of P^2 separates repeated edges (weight 1 each), shared-vertex edge pairs (weight 4 each), and four distinct indices with three matching products (weight 36 when all agree and 4 otherwise). This gives equation (2), with increment 32 per collision. Each four-set contributes three unoriented cycle products; all three matching signs agree exactly when all three products of two different matching signs are positive. The weighted four-walk trace counts each of these cycles eight times and has n(n−1)(2n−3) nondistinct-vertex walks of weight 1. Since (S^2)_ii=n−1, the trace gives equation (1). Each off-diagonal square is nonnegative, and in odd order each is at least one, with exactly the stated equality criteria. For Paley's all-positive infinity row, the required finite-field off-diagonal correlation is −1: for x≠z substitute (x−y)/(z−y) on y≠z to sum the quadratic character over the field with 1 omitted. Symmetry uses chi(−1)=1. Thus the bordered square is qI, and deleting infinity subtracts the all-ones matrix from qI. Switching leaves each collision unchanged and uniquely normalizes the incident row. An independent exact Python replay using literal matching products rather than the frozen two-mask parity method exhausted the 8, 64, 1024 and 32768 normalized assignments at n=4,5,6,7 and reproduced (minimum, multiplicity)=(0,6),(0,12),(0,12),(5,3024). It independently verified both finite Paley witnesses, every indicated induced submatrix, and all seven moment values. The 7-set incidence bound gives b≥binomial(n,4)/7, and equality at order 10 forces every 7-subset optimal, giving equality for 7–10 by the same incidence identity. The order-6 Paley witness has b=0, inherited below order 6.

## originality

PASS

Pass the exact binary torus minimum/deficit and the quantitative seven-vertex obstruction together, not Seidel switching, graph enumeration, the conference construction, or the general square-free upper bound. There is a precise equivalent two-graph extremal count and a pre-existing catalogue of the ambient classes, but the inspected catalogue publishes neither the relevant fourth-trace extremum nor the collision counts. The inspected upper bound and conference results do not yield the seven-vertex lower bound or convert it to this moment law.

## value

PASS

The exact deficit connects the minimum of a natural binary Fourier-layer norm to conference structure and identifies infinite sharp families. The finite cutoff is structurally motivated: seven vertices is the first unavoidable four-mode collision and the sharp obstructing multiplicity propagates via incidence, with matching witnesses through ten. This is more than listing existing switching classes or recomputing a known table; it isolates a meaningful invariant and explains when it first forces a moment gap.

The dated certificate retains the supplied scientific assessment, sources and limitations.
