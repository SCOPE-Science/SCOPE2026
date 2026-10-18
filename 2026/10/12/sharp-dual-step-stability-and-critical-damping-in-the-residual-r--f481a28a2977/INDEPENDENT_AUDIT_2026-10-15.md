# Independent mathematical audit

## correctness

PASS

The exact deterministic N=1, f=0, B=0, theta=1 specialization of b-ASADMM retains the residual-reduction correction -(beta/2)x_k in the x first-order condition, yielding (a+beta)x+= (a+beta/2)x+lambda and lambda+=lambda-(2x+-x)/sigma. With r=(a+beta/2)/(a+beta) and u=1/[sigma(a+beta)], its state matrix has trace 1+r-2u and determinant r-u. Independently verified characteristic and Jury identities symbolically: 1-T+D=u>0, 1-D=1-r+u>0, and 1+T+D=2+2r-3u>0 precisely for sigma>3/(4a+3beta). At equality the eigenvalue -1 obstructs asymptotic convergence, below it a real root less than -1 exists. The discriminant 4u²-4ru+(1-r)² and r>1/2 give a unique spectral minimum at u+=(r+sqrt(2r-1))/2, sigma*=2/[a+beta/2+sqrt(a(a+beta))], rho*=1/2[1-sqrt(a/(a+beta))]. Exact source-coupled sigma=2/beta rate follows by substitution, optimal only for a/beta=1/8, with rho_src→1 for large a/beta and rho*∼beta/(4a). The proof covers this decoupled deterministic scalar mode only; it does not assert universal b-ASADMM convergence.

## originality

PASS

Best-of-knowledge new statement/implication after source-specific primary comparison and targeted published-record searches; residual priority and access risks are itemized below.

## value

PASS

An exact stability frontier, unique damping optimum and arbitrarily large rate gap for the actual residual-reduction core provide a quantitative algorithm-tuning benchmark missing from a general sufficient convergence proof. The source proof coupling is shown rate-optimal only at one metric/penalty ratio, a meaningful diagnosis rather than a mere parameter renaming.

The dated certificate retains the supplied scientific assessment, sources and limitations.
