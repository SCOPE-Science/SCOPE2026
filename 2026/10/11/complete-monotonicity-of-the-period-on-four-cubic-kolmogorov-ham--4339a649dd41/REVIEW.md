# Independent mathematical audit

## correctness

PASS

Direct Hamiltonian differentiation and scaling (X,Y)=(sqrt(a/C)x,sqrt(b/C)y), tau=C t_physical establish H=xy(ax²+by²−C), four nondegenerate quadrant centers, and normalized energy e=h sqrt(ab)/C² in (0,1/8). The radial variable z=X²+Y² has turning points (1±sqrt(1−t))/2, t=8e. The exact minimal physical period is T=4/C ∫_0^{π/2}[cos²φ+t(1+sin²φ)]^(−1/2)dφ =4/(C sqrt(1+t))K(sqrt((1−t)/(1+t))). Positive-integral differentiation on compact interior energy intervals yields (−1)^n T^(n)>0 for every n≥0. At t→1 its value tends to sqrt(2)π/C; the K(k) logarithmic asymptotic yields (2/C)log(C²/(h sqrt(ab)))+o(1) as h→0. Coordinate reflection reverses phase at most, not physical time. The inspected verify_period.py performs finite quadrature/AGM sample comparisons only; the analytic integral is the infinite proof.

## originality

PASS

He–Liu–Xiao classify center configurations of cubic Hamiltonian Kolmogorov fields but do not state this original-time complete elliptic period and its strict all-order derivative signs. Villadelprat–Zhang study separable H=F(x)+G(y) and first-derivative monotonicity; the present xy(ax²+by²−C) Hamiltonian is not of that separable form, and their general criteria do not directly supply all derivative signs. The exact quadrature may be elementary from the Hamiltonian, but the complete-monotonicity classification with boundary constants is not the same as generic monotonicity. Search and primary reading support best-of-knowledge novelty; unindexed integrable-system calculations remain possible.

## value

PASS

For a natural three-parameter four-center cubic Hamiltonian family, absence of all critical periods is meaningful dynamical information and the stronger all-order sign pattern yields strict convexity and higher derivative constraints. The precise physical-time normalization and separatrix constant distinguish the result from mere orbit topology or an arbitrary unmotivated parameter slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
