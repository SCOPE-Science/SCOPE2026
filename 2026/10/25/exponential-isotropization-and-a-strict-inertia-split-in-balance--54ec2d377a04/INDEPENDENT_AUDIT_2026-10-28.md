# Independent mathematical audit

## correctness

PASS

Identified the edge/base polytope as the simplex sum x_i=2, x_i>=0, class sums<=1. With Y=X/2 the ambient uniform simplex has Dirichlet(1,...,1) coordinate law, with block totals Dirichlet(m,...,m); the truncation max T_j<=1/2 is exactly the polytope and its forbidden events T_j>1/2 are pairwise disjoint, giving h=1-rp_{m,k}. Tilted-Dirichlet second moments yield u=E[T_1^2|cap] with tails p_{m+2,k},p_{m,k+2}. Block permutation symmetry and the conditional within-block Dirichlet(1,...,1) covariance yield the two eigenvalues on orthogonal subspaces of dimensions r(m−1) and r−1. Applied two beta half-tail recurrences to derive the exact positive gap 2^(1−rm)(r−2)/[(r−1)(m+1)((r−1)m+1) B(m,(r−1)m)h], hence strict finite anisotropy. Stirling and h→1 give C_r sqrt(m) rho_r^m with rho_r<1. An independent Fraction/binomial-sum calculation verified both eigenvalues, exact gap and positivity for 45 (r,m) pairs r=3..7,m=2..10 including (3,2): 4/49 vs 5/147, gap 1/21. Algebra, not finite tests, proves the infinite parameter family.

## originality

PASS

PASS best-of-knowledge: prior rank-two matroid work evaluates Ehrhart and face vectors of the same polytope family; no inspected primary result yields continuous-volume covariance spectra, strict anisotropy or sharp exponential equilibration.

## value

PASS

The balanced complete multipartite base polytope is canonical and has two inequivalent tangent representations; equality of directional covariance is not forced by symmetry. The exact sign and magnitude of its anisotropy and the sharp exponential isotropization scale constitute a meaningful geometric invariant and transition, distinct from the known discrete lattice and face counts.

The dated certificate retains the supplied scientific assessment, sources and limitations.
