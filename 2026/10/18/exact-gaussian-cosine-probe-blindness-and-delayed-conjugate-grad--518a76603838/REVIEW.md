# Independent mathematical audit

## correctness

PASS

For rank-r orthogonal projector P and independent standard Gaussian n×s probe Z, projected and perpendicular squared Frobenius norms are independent χ²_(rs) and χ²_((n−r)s), giving T~Beta(rs/2,(n−r)s/2). Substitution yields exact global cosine loss, support maximum 1−2√K/(K+1), two CDF roots t± and proper tails. The sparse crossover is controlled by K√(r/n) and W=(n/r)T→χ²_q/q for finite rs=q or 1 for growing rs; weak normalization rationalizes the exact loss; high crossover bound on cosine tends zero. On diagonal A with Chebyshev–Lobatto k+1 eigenvalues and remaining 1, E probe loss≤tr(A−I)²/n≤k(K−1)²/n independently of s. Explicit spectral weights c_j/λ_j yield CG energy-polynomial orthogonality up to k−1 by barycentric identities, so after k CG steps energy error exactly 1/T_k((K+1)/(K−1))=sech(k arcosh((K+1)/(K−1))). Taking K=k^4,n=k^10 yields bound 1/k and error→1; two diagonal 0.6-Jacobi smoothing sweeps multiply probes by 0.16, leaving cosine unchanged. Independent Monte Carlo checked Beta CDF on three n,r,s,K settings; polynomial moment orthogonality and exact residual magnitude checked for k=3,5,8. Delayed CG is a separate k+1-eigenvalue construction, NOT claimed on the rank-r two-eigenvalue diagnostic example.

## originality

PASS

Osborne–Guo–Owens–Matusik (2026) defines exactly this flattened cosine training loss and Gaussian probe smoothing, but reports engineering performance and does not establish the full rank-r Beta law, crossover or a k-step worst-case CG obstruction with uniformly vanishing diagnostic. Classical Kantorovich cosine extrema and CG Chebyshev polynomial constructions separately predate this result; their mathematical combination with an explicit uniform-in-s probe expectation bound is the assessed increment. Published SCOPE CG and solver records found in Resultary concern other algorithms and spectral models.

## value

PASS

The targeted Gaussian cosine probe objective is used to assess preconditioners; the exact law determines sample-to-sample variability, the sparse outlier detectability threshold, and the limit of increasing probe count. The constructed growing-step CG failure at vanishing diagnostic directly establishes the diagnostic’s worst-case blind spot and prevents an unjustified guarantee from a small training loss. This is a motivated, quantitative failure boundary, not an arbitrary diagonal counterexample.

The dated certificate retains the supplied scientific assessment, sources and limitations.
