# Independent mathematical audit

## correctness

PASS

Reconstruct X_i=epsilon_i A_i with independent Rademacher signs. Conditional on magnitudes and the sign-blind permutation, I_j=(1-epsilon_j epsilon_{j+1})/2, while S²=(sum b_j²-Z²/n)/(n-1), Z=sum epsilon_j b_j. The only quadratic monomial in Z² correlated with I_j is 2b_jb_{j+1}epsilon_j epsilon_{j+1}, with covariance -b_jb_{j+1}. Summing and dividing n(n-1) gives exact covariance. Conditional E[R]=(n+1)/2 eliminates cross-conditional term. Changing signs are iid transition bits, yielding binomial runs independent of magnitudes. Independently enumerated all sign vectors on b=[1,3,2,4], giving 17/12 covariance in agreement with formula, and checked uniform beta-order-statistic moment. Finite second moment suffices for expected pair products by Cauchy-Schwarz.

## originality

PASS

The McWilliams runs test and its distribution-free binomial law are established. This result asks a different joint-second-order question, displaying how sample centering creates covariance with R even though raw second moment is independent. Inspected later full-text runs work has no matching sample-variance covariance statement; original 1990 paper full PDF inaccessible, explicitly retained as priority risk. O is best-of-knowledge PASS.

## value

PASS

Gives exact conditional and unconditional dependency between a distribution-free symmetry diagnostic and unbiased scale estimation, including arbitrary magnitude orderings and a closed benchmark under the uniform law. Changes in ordering produce different covariance despite identical marginal runs distribution; this is a substantive statistical characterization rather than routine recalculation of marginal binomial variance.

The dated certificate retains the supplied scientific assessment, sources and limitations.
