# Self-review

## Correctness
PASS. The Haar projection fraction is exactly beta-distributed. A direct Sherman--Morrison inverse yields explicit parallel and perpendicular step identities. Their singular orders differ by a square root, and beta-tail integration proves exact positive constants and the sharp if-and-only-if moment classification. Exact second moments and the ridge regularization asymptotics follow from beta identities and endpoint scaling. Reproducible finite-dimensional checks confirm critical identities but are not the basis of infinite-limit claims.

## Originality
PASS, qualified. Primary full-text comparisons included Cartis--Roberts on safeguarded derivative-free subspace minimization, Cartis--Fowkes--Shao on trust-region/regularized random subspace steps, and LeJeune et al. on high-dimensional sketched pseudoinverse equivalents. Their results do not directly imply the exact finite-dimensional, singular, unsafeguarded gradient-alignment phase classification in the stated domain. Related published mathematical records on Gaussian reduced least squares and rank-one random subspaces have different operators, dimensions, and quantifiers. Search coverage is not a proof of publication priority, and related exact random pseudoinverse identities may exist in specialized matrix-variate literature.

## Value
PASS. The rank-deficient Gauss--Newton model is a natural local object; the exact gradient is orthogonal to the curvature kernel but numerical/model inconsistency can insert a tiny nullspace component. For codimensions three and four, this changes finite mean-square steps into infinite ones despite almost-sure invertibility, which matters for designing safeguards and interpreting average-case random-subspace claims. The result is diagnostic and does not replace safeguarded algorithms.

## Scope and remaining risks
The full optimization objective may be unbounded below if the gradient contains a kernel component. Therefore only the unrestricted local quadratic subproblem is analyzed. Special spectral isotropy is needed for the sharp constants. No algorithmic convergence or numerical stability beyond the local model is asserted. Independent scientific verification and exhaustive publication-priority comparison have not been performed.

Self-review: passed. Independent audit: not yet performed.
