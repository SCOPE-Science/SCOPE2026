# Independent mathematical audit

## correctness

PASS

Under r=u(d1+ab), b(qa−n)=d2+rkn/u² and u=1+ka, direct symbolic reduction along the predator nullcline y=a+nx gives G(x)=−x²(P+Qx)/[(u+knx)(1+qx)], where P=d1knq+d2(uq+kn)+bkn²>0 and Q=d2knq>0. This excludes all interior equilibria. Logistic comparisons bound every positive global trajectory and give liminf y≥a. An interior omega-limit without equilibria would contain a periodic orbit, ruled out by planar index because the positive quadrant is convex and contains no interior equilibria; a bounded complete boundary orbit with y≥a must equal (0,a). Local center dynamics have x′=−(P/u)x³+O(x⁴), z=y−a−nx=(nP/(su))x³+O(x⁴), with strong-stable manifold x=0. Positive orbits cannot follow that exceptional boundary manifold; exponential tracking yields t x(t)²→u/(2P), (y−a)/x→n. Independently reconstructed the exact rational identity with SymPy and a positive witness a=n=k=b=d1=d2=s=1, r=4,q=3,P=11,Q=3. The symbolic test does not prove the omega-limit or asymptotic steps, which are supplied analytically.

## originality

PASS

Best of knowledge PASS: Yao–Yang–Yuan (2024) defines the same delayed fear–Leslie–Gower model and its predator-only equilibrium. Its zero-delay specialization and strict linear invasion criteria do not resolve simultaneous zero linear invasion and quadratic drift, the cubic critical coefficient, or global attraction. Yu (2012) treats a different fear-free coexistence regime. The new result is the exact all-positive-orbit critical decay, not merely the familiar local center-manifold principle. Access to related degenerate predator–prey threshold papers cannot be exhaustive.

## value

PASS

The double-tangency boundary is a natural codimension-two stability transition at which linearized threshold criteria fail. The result supplies a strict global classification and universal algebraic extinction coefficient at the parameter boundary for every positive trajectory, repairing an actual gap in the source model rather than being a routine linear stability check.

The dated certificate retains the supplied scientific assessment, sources and limitations.
