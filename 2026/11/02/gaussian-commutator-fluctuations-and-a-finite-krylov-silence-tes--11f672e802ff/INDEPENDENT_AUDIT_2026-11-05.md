# Independent mathematical audit

## correctness

PASS

Reconstructed exact random-pair decomposition Q_±=P_h±D_h, P_h=I−2hH+O(h²), D_h=h² C+O(h³), deterministic propagation e^(−2jhH), and martingale-sum representation of X_n−m_n. Orthogonality bounds centered second moments by O(jh⁴) and replacing random X_{j−1} by deterministic mean leaves L² error O(h³), negligible after h^(−3/2) scaling. Bounded triangular-array coefficients √h v(t_j) give Lindeberg and covariance h∑v vᵀ→½∫_0^L v vᵀdt, with degeneracies allowed. Positivity of the integral, invertibility of exponentials, analyticity of C exp(−tH)x0, and Cayley–Hamilton yield the exact iff CH^k x0=0 (0≤k<d). Independent exact numeric 2×2 witness C=[[0,1/2],[-1/2,0]] and covariance recursion n=30,60,120,240 tends monotonically to e^(−2)(1−e^(−2))/16=0.007313727771742408 (values 0.00687824, 0.00709158, 0.00720153, 0.00725734). We verified admissible positive-definite witness. The asymptotic is centered random-order noise only, not continuum solver error.

## originality

PASS

Qualified PASS: general random matrix product central limit methods, randomized splitting rates and deterministic commutator error algebra are prior. The completed conclusion that survives is the exact weak-noise covariance at h^(3/2) for balanced pairwise implicit resolvents, including its finite vector-specific Krylov null criterion. Full Berger (1984) available rendered sections 5–6 were inspected: diffusive stochastic product limits and generic limiting semigroups do not themselves state this smaller centered noise coefficient or initial-data null equivalence. Eisenmann–Stillfjord independent-choice splitting does not require every pair to contain both operators. Search of published mathematical records returned unrelated Gaussian sign concentration/Krylov CG rather than an equivalent formula. An older generalized perturbative CLT may imply pieces; priority remains qualified.

## value

PASS

A structurally motivated diagnostic of residual random-order noise after balanced two-operator splitting, not another generic rate estimate. Exact computable covariance distinguishes active and silent initial Krylov subspaces for a fixed pair of generators; its sharp 2×2 noncommuting example proves h^(3/2) fluctuations can be genuine and the finite criterion is practically usable in operator choice. It does not claim new CLT techniques or total approximation rate.

The dated certificate retains the supplied scientific assessment, sources and limitations.
