# Independent mathematical audit

## correctness

PASS

At each shared-Hessian eigenmode the component update is e+=q e+t c_i. A complete epoch gives e_{k+1}=q^n e_k+t Z_k. Independent epoch resampling makes its exact second moment a geometric sum in q^{2n}; IID weighted variance is v B_n(q), while permutation off-diagonal covariance -v/(n-1) yields v[n B_n(q)-A_n(q)^2]/(n-1). Their difference, with Hessian eigenvalue weights, proves equation (1) at every n>=2, K>=1, dimension d>=1. Direct algebra gives A_n(q)^2-B_n(q)=2q(1-q^n)(1-q^{n-1})/[(1-q)^2(1+q)]; all non-q factors are positive for -1<q<1. Concentrating centered data on any single eigenvector proves both uniform-data iff conditions and mixed regimes. Exact n=2, eta=3/2, centers +/-1 yields terminal squared errors RR=81/16, IID=45/16, while eta=1/2 reverses the sign. An independently written rational permutation/IID checker checked signed q for n=2..8; it supplements the unrestricted proof.

## originality

PASS

Best-of-knowledge new all-horizon signed contraction/overshoot phase classification for terminal RR versus IID on common-Hessian quadratics; known finite-population covariance and averaged-output literature are explicitly separated.

## value

PASS

The exact reciprocal-curvature boundary identifies when replacing sample-with-replacement noise by permutation anticorrelation helps or hurts the terminal optimization objective, including a strong strictly reversed example at stable overshooting steps. It gives a necessary-and-sufficient, all-horizon spectral criterion rather than a routine rate-bound restatement, and distinguishes operationally important output metrics.

The dated certificate retains the supplied scientific assessment, sources and limitations.
