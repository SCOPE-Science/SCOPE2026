# Independent mathematical audit

## correctness

PASS

The strict return tail at n uses the left-branch threshold x_(n-1) and the initial-section integral up to (1+x_(n-1))/2. For w_j=x_j^(-alpha), the increments are A-B/w_(j+1)+O(w_(j+1)^(-2)), A=alpha*2^alpha, B=alpha*(1+alpha)*2^(2*alpha)/2. Linear growth first gives w_j=Aj+O(log j); replacing 1/w_(j+1) by 1/(A(j+1)) introduces a summable error. Inversion gives the stated positive Q_alpha=B/(alpha*A^2). The integrated density has relative second coefficient d*r*2^(-beta)/(r+beta); substituting the orbit gives L. For k=floor(un)-1, k=un+O(1) and k>=n-1 uniformly. The floor incurs O(n^-1) in the relative leading term, the small-o density bound is uniform over this tail of indices, and log(k)/k differs from (log n)/(nu) by uniformly O(n^-1). This yields the two profiles, with the logarithmic term dominating also at beta=alpha. Differentiating u^(-p)(1-u^(-eta)) gives the stated maximizers and constants; comparison with n^(-p) gives the moment criterion for positive s (nonpositive orders are automatically finite).

## originality

PASS

The distinct result is the explicit crossover with sharp full-half-line conditional excess profiles and supremum constants for the specified local density expansion, not the logarithmic inverse orbit, the leading return tail, or the algebra of a generic Pareto profile. The inspected results do not supply the combined second-order arbitrary-start tail, its two competing coefficients, and the sharp normalized excess conclusion.

## value

PASS

The quantitative bias of the Pareto excess approximation depends on which of the start density and neutral orbit supplies the slowest correction. The boundary beta=alpha and the positive sharp supremum constants tell when improving start regularity no longer improves the error, even without an invariant probability law. This is a meaningful natural transition and a distributional error guarantee, not a standalone moment test.

The dated certificate retains the supplied scientific assessment, sources and limitations.
