# Independent mathematical audit

## correctness

PASS

For fixed kappa in (0,1), E={1} union {1+exp(-n^kappa)}, the increasing density of points towards 1 is controlled by decreasing gaps g_n~kappa n^(kappa-1)exp(-n^kappa). At the first gap m=m(delta) <=delta, m~(log(1/delta))^(1/kappa) and H=exp(-m^kappa)/delta~m^(1-kappa)/kappa. Global delta-covering number is comparable to m because first m points are separated (up to two per interval) and tail costs O(H)=o(m). For local intervals length r, inverse-counting derivative gives N<=C[1+min(r,a)/delta+H log(1+r/a)], where a=delta H. With r<=a this is O(1+r/delta), and for r>=a optimize r^(-b) at constant multiple a, giving delta^(-b)H^(1-b) for 0<b<1; [a,2a] supplies separated H-point lower bound. b<=0 follows global cover and I=[1,2], b>=1 follows geometric covering plus any singleton at r~delta; R dilation restricted 1/2<R<=2 for nonempty E_R. Hence exactly the three displayed sharp asymptotic two-sided orders. Independently calculated crossover indices H and number of sparse points for multiple (kappa,delta), e.g. kappa=.6, delta=1e-5 gives m=43,H~7.11 and 6 points in [a,2a]; asymptotic proof is analytic, not numerical.

## originality

PASS

Best-of-knowledge PASS for the *finite-scale logarithmic orders* on the stretched-exponential sequence, not for the Legendre–Assouad functional nor for its power-law exponent. The primary spherical-maximal entropy paper analyzes polynomially converging radii 1+n^{-mu}; substituting a different gap inverse is mathematical work and produces nontrivial log factors invisible to the limiting power dimension. No exact published stretched-exponential three-regime table was found in the inspected sources, but failed bibliographic search does not prove priority.

## value

PASS

The set E_kappa is a natural sparse model between polynomially clustered and exponentially clustered radii. A full three-regime, two-sided *scale-resolved* entropy profile determines log corrections invisible to the usual limiting Assouad exponent and clarifies endpoint-sensitive logarithmic geometry. It is an exact natural invariant for the object and could be used when endpoint maximal-operator estimates require finite-scale control, without claiming a new maximal theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
