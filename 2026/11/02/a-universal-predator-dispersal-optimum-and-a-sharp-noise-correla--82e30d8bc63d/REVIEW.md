# Independent mathematical audit

## correctness

PASS

Orthogonal plus/minus transformation diagonalizes drift and noise covariance into two Hurwitz 2x2 Ornstein–Uhlenbeck blocks with A=a+2u and minus V=2v. Solving continuous Lyapunov equations yields P(A,V;Q,R)=[Q(V²+AV+bc)+b²R]/[2(A+V)(AV+bc)], valid even V=0 without division by V. Local prey variance is half sum of plus P(a,0) and minus P(A,2v). The derivative numerator b[cQ(V²-bc)-bR(A²+2AV+bc)] is a quadratic in V with unique positive zero for Q>0, negative throughout for Q=0<R, identically zero for Q=R=0. For R=0, V*=sqrt(bc), endpoints V=0 and infinity equal, gain=Qbc/[4A(A+sqrt(bc))²]. Inspected actual verification program and independently computed full 4x4 stationary Lyapunov covariance for bounded rational cases, agreeing with formula and optimum; universal proof is algebraic, not finite numerics.

## originality

PASS

Two-patch trophic stationary covariance via Lyapunov equations is strongly established. The candidate structural optimum and complete Q/R forcing trichotomy require a particular derivative optimization not located in inspected synchrony and perturbation sources. This is a narrow but legitimate specialization, rather than a claim of new Lyapunov machinery.

## value

PASS

The exact optimal predator mobility for stationary *local prey variance* is a meaningful natural stability statistic. The universal square-root rate with zero predator forcing, matching zero- and infinite-dispersal endpoint variances, exact gain and degenerate noise trichotomy are structural, not an arbitrary tiny numerical effect. The result sharply documents how noise-correlation changes optimal dispersal in a well-defined linear model.

The dated certificate retains the supplied scientific assessment, sources and limitations.
