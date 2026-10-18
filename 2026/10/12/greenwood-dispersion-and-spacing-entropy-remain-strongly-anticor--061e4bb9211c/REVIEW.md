# Independent mathematical audit

## correctness

PASS

PASS: The Dirichlet gamma moment formula E prod D_i^{a_i}=Γ(m)prod Γ(1+a_i)/Γ(m+sum a_i) is valid for nonnegative indices; differentiating one/two exponents yields the log moments with correct equal-index and cross-index multiplicities. Independently simplified the displayed E(GH)-E(G)E(H) algebra to -(m-1)/((m+1)^2(m+2)), verified fourth moments for Var G=4(m-1)/((m+1)^2(m+2)(m+3)) and trigamma entropy-variance formula. Standard asymptotic H_{m+1}^{(2)}=ζ(2)-1/(m+1)+O(m^-2) yields Var H∼(π²/3-3)/m, hence the nonzero correlation limit. Independent numerical computations at m=2,3,10,100,1000 give correlations approximately -0.995711, -0.985086, -0.954857, -0.931962, -0.929024; the general assertion follows from analytic differentiation, not numerics.

## originality

PASS

PASS (best knowledge): Greenwood statistic is known and Dirichlet moments are classical, but Royen arXiv:1008.4059 calculates the square-sum marginal distribution/quantiles rather than Shannon-entropy covariance (full manuscript inspected). Holst/L’Ecuyer study broad sum-functions; the compared log-spacing statistic is unweighted ∑log D_i, whereas entropy is -∑D_i log D_i. Search of Resultary, Dirichlet compositional data, and exact covariance aliases showed no already-stated pairwise identity and nonzero standardized limit. Generic moment differentiation alone is not an already published statement about this natural pair; possibility of hidden old formula noted.

## value

PASS

PASS: Greenwood quadratic dispersion and Shannon evenness are canonical competing concentration summaries of simplex spacings. Exact finite-sample covariance quantifies their dependence; the striking nonzero limit -0.9287 despite O(m^-2) covariance gives usable normalization insight for joint spacing diagnostics and explains persistent dependence. The exact formula is an unknown, naturally motivated invariant beyond a generic moment calculation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
