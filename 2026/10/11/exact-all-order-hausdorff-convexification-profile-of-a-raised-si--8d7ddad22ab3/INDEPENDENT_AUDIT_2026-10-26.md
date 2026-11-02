# Independent mathematical audit

## correctness

PASS

For every integer n>=2 and k>=1 and 0<epsilon<1/(n-1)^2, the normalized regular-simplex inner products give ||sum (lambda_i-mu_i)v_i||^2 = n/(n-1) sum (lambda_i-mu_i)^2. A coordinate discrepancy a forces horizontal distance >= n*a/(n-1). For any base barycentric lambda, floor counts f_i=floor(k lambda_i) have sum F>=k-n+1; every height j*epsilon/k for 0<=j<=F is accessible above that exact base point by selecting raised multiplicities c_i<=f_i and filling remaining k-j summands with one common base point. This gives d<=epsilon for k<n and d<=(n-1)epsilon/k for k>=n. Below threshold, the top centroid point (0,epsilon) is epsilon from the base and horizontally more than epsilon from every stratum containing a lifted vertex. At/above threshold, lambda_1=(k-n+1+(n-1)/n)/k and lambda_{i>1}=(n-1)/(nk) yield exactly J=k-n+1 attainable lifted copies; j<=J gives vertical gap >=(n-1)epsilon/k, while j>J forces a horizontal barycentric discrepancy >=1/(nk) and therefore horizontal gap >=1/((n-1)k)>(n-1)epsilon/k. Height J gives exact equality. For the Schneider index, the top face of A+s conv(A) is union_i(v_i+sT) and covers (1+s)T iff s>=n-1; for s>=n-1 its bottom slab [0,s epsilon] and top slab [epsilon,(1+s)epsilon] cover the prism. No boundary cases are skipped, including n=2, k=1 or k=n. An independent 14-instance exact Fraction-based multiplicity enumeration and KKT projection corroborated the claimed sharp witnesses. Reconstructed the 7-blob tree, matching the assigned SHA. Thus C passes analytically; finite checks do not replace the infinite proof.

## originality

PASS

The motivating van Hintum construction and equality for k<=n-1 are explicitly prior; FMMZ's general Schneider-index bound supplies the upper half. The asserted contribution is the exact lower bound and full post-threshold profile for the specific raised-simplex family, plus its simultaneous saturation of the general upper bound at every averaging order. The motivating primary five-page preprint was fully read and does not state that equality; the 2018 primary theorem gives no matching witness. Resultary semantic searches and complete readings of closest simplex-skeleton and finite vertex-grid published claims revealed distinct objects/invariants, not dominating results. This is a best-of-knowledge PASS, not a historical-priority guarantee.

## value

PASS

The raised regular-simplex cap is the natural canonical example in the recent sharp-threshold problem for Hausdorff convexification. Determining its exact first post-threshold decrease and every subsequent distance is a motivated all-order geometric invariant, not an arbitrary narrow slice or repetition of the early noncontraction theorem. A single explicit family attaining a previously established Schneider-index inequality at every k supplies its missing extremizing examples and a lower obstruction (n-1)/n to stronger universal k=n contraction. This is a mathematically meaningful exact classification for a natural input; it does not assert a universal upper bound, a maximal epsilon interval, or generality for arbitrary norms.

The dated certificate retains the supplied scientific assessment, sources and limitations.
