# Independent mathematical audit

## correctness

PASS

At fixed x and p_n=(log n+x)/n, the original isolates are asymptotically Poisson(lambda=e^-x). For two independently thinned replicas at retention 1-s/log n and 1-t/log n, mixed factorial moments of vertices isolated in both/one-only give independent Poisson mark intensities lambda, lambda(e^s-1), lambda(e^t-1); the common-mark probability tends to the original-isolate probability. The connectivity-without-isolates union bound controls non-isolate disconnections. The joint connectivity limit exp[-lambda(e^s+e^t-1)] gives E(F_n(s)^2) and, after subtracting Z_n*h_x(s), pointwise L2 concentration. Monotonicity and a finite mesh yield uniform compact profile convergence. The annealed isolate variance yields E F_n(s) <= O_x(e^-s+log n/n) uniformly up to s=log n; integrating F_n(s)F_n(t)<=F_n(max{s,t}) controls the squared full tail, proving E|log(n)A(G_n)-C_x Z_n|^2 ->0. This yields a Bernoulli two-atom limit with mean E1(lambda) and variance C_x^2 e^-lambda(1-e^-lambda). Independent rational graph enumeration checked two-retention expectation identities at n=3,4 (27/400, 822771/16000000 for the chosen rational probabilities). Numerical and finite checks are not a proof of the limit.

## originality

PASS

Brown–Cox–Ehrenborg define mean graph reliability; Brown–Kolokolnikov–Kooij 2024 study its approximations and ask ER average reliability. The annealed first moment is classical connectivity plus integration and is not novel. Inspected work does not state the random quenched two-replica L2 law or nonzero two-atom asymptotic variance. Best-of-knowledge PASS, not historical-priority certification.

## value

PASS

The probability that a critical random network is connected stays bounded between zero and one, so fixed-network reliability has a natural persistent random component. Establishing a quenched L2 profile and non-self-averaging two-atom area limit resolves a genuinely probabilistic refinement of average all-terminal reliability, beyond its easy annealed connectivity integral. The precise limiting conditional constant and variance are natural network-reliability statistics.

The dated certificate retains the supplied scientific assessment, sources and limitations.
