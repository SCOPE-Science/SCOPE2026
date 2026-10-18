# Independent mathematical audit

## correctness

PASS

PASS: The exact scalar Gaussian sketch factor is G=chi_p^2/p, with E G=1 and Var G=2/p, independent between steps. Deriving the covariance recursion yields the 3x3 M with rows (m²+2alpha²/p,omega²,-2omega m),(1,0,0),(m,0,-omega), m=1+omega-alpha. For alpha,omega>0, T(Q)=E[B(G)QB(G)^T] is a positive primitive map on 2x2 PSD matrices: T² sends every nonzero PSD matrix to PD, so the source-initialized rank-one covariance and positive first-coordinate observable see the Perron radius; omega=0 is direct. Independent symbolic determinants verify det M=omega³ and det(I-M)=alpha[2p(1-omega²)-alpha(p+2+(2-p)omega)]/p. Initial derivative of Perron root at alpha=0 is negative for omega<1, the unique unit crossing and growth at large alpha give iff stability. At rate r=2/(p+2), independent symbolic computation reproduced the discriminant 8p omega²[((p+2)omega)^2-4]/(p+2)^4; for 0<omega<r it is negative and the leading coefficient of det(rI-M) is negative, for omega=r determinant remains negative for positive alpha, and for omega>r the product eigenvalues omega³ precludes rho<r. At omega=0 minimizing the scalar quadratic gives unique alpha=p/(p+2). The exact p=1, alpha=omega=1/2 eight second moments and mean-versus-variance contrast were reconstructed. No finite numerical trial substitutes for the all-real-parameter Perron/discriminant proof.

## originality

PASS

Best-of-knowledge PASS: Han–Xie §5.6 defines exactly the raw unnormalized mBGK update and supplies sufficient second-moment bounds, not the scalar iff phase diagram or sharp joint alpha/omega minimum of the actual asymptotic second moment. Other stochastic heavy-ball theorems concern normalized projector sketches or different regression/noise models. A separate Resultary KGSM orthonormal 2×2 mean-square stability result concerns a different update distribution. An unindexed general random-coefficient AR(2) stability theorem may imply the matrix reduction, but no inspected prior provides both the exact p-dependent frontier and global no-momentum optimality for this method.

## value

PASS

PASS: The initiating optimization paper contrasts accelerated expected-iterate norms with sufficient expected-square bounds. Determining exactly when actual squared error converges, and constructing a stable-mean/divergent-variance example, resolves a distinct and important stability question about the published random update. The all-p necessary/sufficient formula and unique optimum without momentum are a genuine natural algorithmic boundary, not a parameter-renaming gain.

The dated certificate retains the supplied scientific assessment, sources and limitations.
