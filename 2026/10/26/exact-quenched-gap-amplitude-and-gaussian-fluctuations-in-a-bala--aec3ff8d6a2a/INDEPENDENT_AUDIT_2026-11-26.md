# Independent mathematical audit

## correctness

PASS

The conclusion is for the least singular value (one-fermion energy at the stated Hamiltonian normalization), not a parity-constrained gap. Factoring M=(I+S)diag(h) and setting z_i=(-1)^i h_i v_i gives the pinned-left/free-right string quotient with exact mass w_N=1 and w_i=J_i^(-2) otherwise. Its stiffness is a squared first difference, whose inverse is min(i,j). Scaling gives the Green operator with atomic mass on j/N. The Lipschitz-operator bound follows by integrating against the cumulative mass discrepancy: both min(x,y)f(y) and 1_{y>x}f(y) have uniformly bounded variation in y for ||f||_Lip<=1, controlling the supremum and the a.e. derivative. The discrepancy is at most the maximum absolute centered partial sum divided by N plus O(1/N); the strong law and Kolmogorov maximal inequality give a.s. convergence and O_P(N^-1/2), respectively. The limiting map has a bounded image in C^{1,1}, so is compact in Lip. With k=pi/2 the top simple isolated eigenvalue is m/k^2, with right sine mode u and left functional 2 integral(u f); spectral separation and norm convergence identify the nearby eigenvalue with the top finite-matrix eigenvalue. The simple-eigenvalue expansion has a quadratic remainder. Its linear term is the empirical sum of centered masses with coefficient 2 sin^2(kj/N)/(k^2 N), up to O(1/N) from quadrature and the endpoint. The bounded weighted triangular-array CLT uses integral sin^4=3/8; the map rho -> rho^(-1/2) gives variance 3 pi^2 s^2/(32 m^3). For s^2=0 the centered sum vanishes and the remainder at sqrt(N) scale goes to zero. No extrapolation to heavy tails, other balance profiles or parity-constrained excitations is made.

## originality

PASS

The balanced chain and gap exponent are prior. On the inspected evidence the distinct result is the almost-sure sharp one-fermion gap amplitude and its explicit Gaussian fluctuation variance for that bounded iid chain. No prior statement or applicable stronger result giving this pair was established; this is a bounded priority judgment.

## value

PASS

The exact normalization and fluctuations are intrinsic gap statistics of an independently motivated balanced critical chain. They distinguish self-averaging of the leading prefactor from nonzero disorder corrections and give constants useful for comparing finite-chain data with asymptotics; neither is a restatement of z=1 or of a finite simulation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
