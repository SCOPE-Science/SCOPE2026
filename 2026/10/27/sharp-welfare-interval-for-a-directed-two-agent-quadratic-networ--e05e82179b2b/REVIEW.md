# Independent mathematical audit

## correctness

PASS

Normalize positive heterogeneous quadratic cost coefficients via v_i=sqrt(gamma_i)x_i, y_i=b_i/sqrt(gamma_i), t=g/sqrt(gamma1 gamma2) in (0,1). Triangular best responses give unique Nash v=(y1+t y2,y2). Planner Hessian H=[[1,-t],[-t,1]] is positive definite and H^-1y nonnegative, giving unique feasible maximizer. Welfare at Nash is D/2 with D=(y1+t y2)^2+y2^2>0; planner welfare is (y1^2+2t y1y2+y2^2)/(2(1-t^2)). Ratio differences factor exactly into t^2*y1*(y1+2t*y2)/((1-t^4)D) and t^2*y2^2/((1-t^2)D); equality iff y1=0 or y2=0 respectively. Connected incentive path attains every value; strictly positive incentives exclude endpoints. For t>=1 welfare diverges along v1=v2; the Nash response matrix is nilpotent M^2=0 at every t. Independent exact rational welfare evaluations passed 192 cases, not used for the universal proof.

## originality

PASS

Compared mathematical objects and implications, not merely similar titles: Iwanaga–Kobayashi 2026 use a symmetric undirected binary adjacency, uniform own-cost 1/2, real unconstrained actions and spectral radius of symmetric adjacency; their assumptions do not admit a one-way nilpotent edge. A symmetric spectral welfare bound cannot specialize by relabeling to strictly upper-triangular directed M because M is not symmetric and rho(M)=0 for all t. The α-potential maximizer need not equal the true Nash equilibrium on a directed graph. Residual priority risks documented, including uninspected plausible original sources; absence of search hits is not assumed to certify novelty.

## value

PASS

A two-agent one-directional productive externality is a minimal natural directed counterexample to bounding welfare inefficiency by strategic-response spectral radius. The full sharp, incentive-dependent best-to-worst interval with heterogeneous costs and divergent lower endpoint is a useful complete quantitative benchmark.

The dated certificate retains the supplied scientific assessment, sources and limitations.
