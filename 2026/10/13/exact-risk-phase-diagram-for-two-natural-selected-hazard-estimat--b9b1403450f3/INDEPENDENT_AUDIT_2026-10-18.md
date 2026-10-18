# Independent mathematical audit

## correctness

PASS

Derived exact selected inverse-sum expectation using Xi=sigma_i Yi iid Gamma(n,1), S=X1+X2 independent of T=X1/S ~ Beta(n,n), selection T>r/(1+r) for r=sigma1/sigma2. Integrating reciprocal Xi gives E[1/(sigma_J Y_J)]=1/(n-1)-x(r)^(n-1)/[(n-1)² B(n,n-1)], x=r/(1+r)². Entropy-risk subtraction yields Delta=that expectation-log(n/(n-1)). At r=1 it is strictly negative by central-binomial lower bound; as max(r,1/r)→∞ it tends to the positive constant 1/(n-1)-log(n/(n-1)). Since x decreases strictly with max(r,1/r)≥1, Delta increases strictly and has one crossing q_n∈(0,1/4), rho_n=(1+sqrt(1-4q_n))/(1-sqrt(1-4q_n)). Independently compared incomplete-beta integrals against the formula at n=2,5,8,11 and several hazard ratios; n=2 rho=4.2843765164, n=5 rho=2.6791419805, n=8 rho=2.2878314577. No universal admissibility follows.

## originality

PASS

Best-of-knowledge: the same-model 2021 primary paper gives both estimators and a beta-integral for reciprocal risk, explicitly reports no global risk hierarchy and does not derive a full analytic hazard-ratio boundary. Quadratic-loss and alternative-selection papers do not imply this entropy-loss comparison. Older rate/scale parameterization remains a substantive residual search risk.

## value

PASS

The exact risk-order phase boundary for the two natural selected exponential hazard estimators resolves a concrete decision ambiguity identified in the motivating statistics paper. It tells practitioners when the MLE has smaller entropy risk than the BSEE analogue without mistaking either for admissible in the full rule class; exact analytic hazard-ratio crossover is not a routine restatement of a simulation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
