# Independent mathematical audit

## correctness

PASS

For complete weighted two-community graph (m,n>=2, within alpha>0 and between beta>0), matrix-tree minor after marking v gives zero-sum block eigenvalues U and V and 2x2 determinant beta*z*w*U, leading to Z(w,z)=beta*z*w[alpha(m-1+w)+beta n z]^(m-1)[alpha n+beta z(m-1+w)]^(n-1). Normalized specialization yields shifted independent-binomial laws. Differentiating log Z yields mixed covariance. At fixed cross-edge count K, all tree Gibbs weights equal, so E[D|K] is conductance-independent; coefficient ratio at K=2 vs K=1 has sign m-n, while the maximal K endpoint has difference sign n-m, proving nonmonotonicity when m!=n. Covariance factorization gives unique positive q*= (sqrt((m-1)(n-1))-1)/(m+n-1+sqrt((m-1)(n-1))) and flat zero covariance at m=n without independence. The supplied verify.py was read: independent exact Prüfer enumeration, Laplacian Bareiss determinant, conditional and covariance asserts; a separate checker exhaustively compared weighted joint coefficients in small sizes. No assertion of global interior turning-count classification.

## originality

PASS

Sanmartín/Schnörr/Hamprecht (2024) establish general weighted random spanning-tree degree distributions and covariance techniques; Rapoport (2023) supplies general correlations. These methods are ingredients, but their inspected statements do not directly provide the joint K vs fixed-vertex degree factorization, K-conditional nonmonotone regression law, or conductance-driven sign reversal for all m,n. The claim is a novel specialization only if an older stronger exact joint-edge-class formula does not subsume it; this is retained as explicit residual priority risk.

## value

PASS

The full bivariate finite-graph law and counterintuitive conditional regression, with a unique tunable covariance reversal, characterize a natural community graph Gibbs tree model. The strict sign change is a meaningful new structural dependence fact, not merely a recomputation of a known normalizing determinant.

The dated certificate retains the supplied scientific assessment, sources and limitations.
