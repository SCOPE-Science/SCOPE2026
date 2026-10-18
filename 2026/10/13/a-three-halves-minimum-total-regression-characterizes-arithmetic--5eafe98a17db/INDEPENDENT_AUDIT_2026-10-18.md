# Independent mathematical audit

## correctness

PASS

Conditioning on M=z_k makes the other value uniformly distributed over z_(k+1),...,z_N. Set U_k=mean of that tail; the assumed regression makes U_k=z_k/2+c. The identity (N-k)U_k=z_(k+1)+(N-k-1)U_(k+1) yields (N-k+1)z_(k+1)=(N-k)z_k+2c, so successive differences are equal for all k<=N-2. Conversely arithmetic endpoints give E[S|M]=3M/2+(a+Nd)/2. For canonical z=1..N, direct covariance computation yields Var S=(N+1)(N-2)/6, Var M=(N+1)(N-2)/18 and Cov(M,S)=3 Var(M)/2, proving the exact correlation. Independent exact rational arithmetic sample checks support the all-N algebra; no finite search is substituted for the recurrence proof.

## originality

PASS

The exact statement was compared against the primary literature with special-case implications and pre-existing formulas separated from the contribution. Priority is a bounded best-of-knowledge assessment; see all four explicit comparisons and residual risks. The exact inverse direction follows from a new recurrence on upper-tail means, not from generic sign or asymptotic theorems for order statistics.

## value

PASS

The inverse characterizing one observable conditional regression as exact equal spacing is a natural structural theorem for finite-population sampling without replacement, not just a covariance tabulation. It identifies when classical uniform-label formulas genuinely describe unknown population geometry, with a population-size-independent correlation consequence.

The dated certificate retains the supplied scientific assessment, sources and limitations.
