# Independent mathematical audit

## correctness

PASS

PASS: Starting from the exact fixed-grid iteration Xhat_m=x0(1+a/m)^m+sum_j H_j(1+a/m)^(m-1-floor(m*T_j)), uniform first-order logarithmic expansion gives Q_m=(a^2*x0*exp(a))/2+sum_j H_j exp(a(1-T_j))[a(1-{mT_j})+a^2(1-T_j)/2]+o(1). Conditionally on jump count, Poisson event-time vectors have densities; Fourier/Riemann-Lebesgue equidistribution gives stable independent uniform phases, but the fine phase is the SAME uniform doubled modulo 1, not an independent uniform. The pointwise dyadic identity (1-u)-(1-{2u})/2=1_{u<1/2}/2 gives iid conditional Bernoulli marks and Var(D|J)=(a^2/16) sum H_j^2 exp(2a(1-T_j)). Finite jump count and a.s. finite marks justify the pathwise finite sum without moment assumptions. Independent deterministic Euler grid expansion and phase identity were checked; finite test is not proof of stable convergence.

## originality

PASS

PASS (best-of-knowledge): The proposed one-grid equivalence fails: two marginal distributions do not fix the dependence between resolutions or the Bernoulli correction. Shared coordinate marks within one resolution are different from two coupled grids. A general multilevel stable convergence theorem could imply the simple compound-Poisson limit via specialization. Abstract coverage alone does not establish that the 2015 theorem includes compound-Poisson jump forcing, the same non-jump-adapted scheme and the explicit conditional Bernoulli law. Priority remains materially qualified. Neither a single-grid stable convergence theorem nor an independent coupling of its limit marks implies the true joint law; a properly general multilevel theorem might imply it. This is a best-of-knowledge PASS with a substantive verification risk, not an assertion of historical priority. Specific priority and access qualifications are recorded below.

## value

PASS

PASS: Two-grid shared-noise differences are the primitive input in multilevel approximation. Their conditional variance cannot be inferred from one-grid marginals or independent simulated uniform phases. This exact compound-Poisson benchmark resolves the nontrivial dyadic coupling and provides a check for multilevel error laws, without claiming a broad MLMC central limit theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
