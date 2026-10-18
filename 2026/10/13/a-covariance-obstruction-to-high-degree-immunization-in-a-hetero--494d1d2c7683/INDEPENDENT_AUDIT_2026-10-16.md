# Independent mathematical audit

## correctness

PASS

For the published general-infection-rate SIS system, let w_k=phi(k)f_k′(0), degree distribution P(k) and mean degree <k>. With average equal budget sigma=<sigma_k>, the source thresholds imply R^U=(1-sigma)<w>/[(mu+gamma)<k>] and R^T=(<w>-<sigma_k w_k>)/[(mu+gamma)<k>]. Their difference is exactly -Cov_P(sigma,w)/[(mu+gamma)<k>]. Degree-targeting sigma_k monotone in k does not force positive covariance absent an increasing w_k assumption; f_k individual monotonicity and concavity do not impose cross-degree order. Concrete admissible two-degree case: P(1)=P(2)=1/2, phi(1)=phi(2)=1, mu=gamma=2/15, f_1(theta)=(4/5)theta/(1+theta), f_2(theta)=(1/5)theta/(1+theta), sigma_1=0, sigma_2=1/2. These f_k are positive for theta>0, strictly increasing, strictly concave, f_k(0)=0, and the targeted profile matches the cutoff form. Exact rational calculation gives R0=5/4, Cov=-3/40, R^U=15/16<1<R^T=9/8, and R^T-R^U=3/16, refuting the paper’s unconditional equal-budget ranking. The full original primary text with assumptions H1-H3, equations (17)-(19), covariance discussion and Theorem 4.2(3) was read.

## originality

PASS

Huang-Jiang DOI:10.3934/dcdsb.2018226 already explicitly derive the covariance algebra near equation (19). That identity is prior, not the original contribution. However they assert the covariance is positive solely from high-degree targeting and conclude in Theorem 4.2(3) that targeting always beats equal-budget uniform coverage, a false general implication when f′_k(0) is not degree ordered. The provided actual admissible sign-reversing two-degree functions and strict epidemic-threshold reversal correct that precise overgeneralization; no comparable counterexample occurs in the inspected complete primary article. Fu-Small-Walker-Zhang PRE 77 (2008) adopts a more special degree-linked infectivity family, which cannot imply the broad unqualified general-infection theorem. Resultary related vaccination findings are different models.

## value

PASS

An explicit counterexample reverses the claimed disease-control ordering (uniform below threshold, degree-targeted above) at equal budget, affecting a meaningful interpretation of network intervention strategies. The corrected exact covariance-sign criterion identifies the mathematical condition needed for valid targeting comparisons; biological efficacy outside this idealized SIS model is not claimed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
