# Independent mathematical audit

## correctness

PASS

With orthonormal W=[w,V], invariant spectator range V and Hermitian A, the residual r=Aw-rho w is orthogonal to W. Independent Gaussian images G=SW and z=S(r/sigma) reduce the one nonspectator least-squares Ritz eigenvalue to rho+sigma e1^*G^dagger z; residualization against last m-1 columns gives U/sqrt(H) with residual sketch dimension nu=s-m+1. In the real case H is chi-square_nu and U standard N(0,1); in the complex case H Gamma(nu,1) and U circular CN(0,1). Exact Gamma integrations yield real p-moment finite iff p<nu, complex iff p<2nu, with tail I_{1/(1+x²)}(nu/2,1/2) or (1+x²)^-nu, respectively. Thus mean-squared error finite exactly s>=m+2 (real) and s>=m+1 (complex), with stated denominators. Divergence at the equality boundaries is established by inverse-Gamma/chi-square integrals, not simulated rare-event sampling. Independent 5000-sample regression simulations for real/complex m=3,s=3,4,5 checked predicted tail probabilities within sampling tolerances.

## originality

PASS

Though a ratio of independent Gaussians with an inverse chi-square/gamma denominator is classical regression, the exact identified nonspectator sketched Ritz eigenvalue distribution and sharp real-versus-complex oversampling moment-integrability phase diagram are not stated in examined primary sketched Rayleigh–Ritz theory. The result is natural for determining when ordinary expected squared Ritz error is meaningful.

## value

PASS

Identifies exactly the sketch row budget at which a highly natural Gaussian-sketched Ritz error has finite expected square, including a one-row real/complex gap. Infinite-moment warnings are actionable in randomized spectral computation, and the full finite p-moment cutoff is a meaningful structural stability invariant.

The dated certificate retains the supplied scientific assessment, sources and limitations.
