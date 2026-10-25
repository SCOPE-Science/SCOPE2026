# Independent mathematical audit

## correctness

PASS

Reconstructed the uniform simplex law (iid circular gaps Dirichlet(1,...,1)) and coordinate-shift identity P(S_i>t_i,i in I)=(1-sum t_i)_+^(n-1). Separating equal and unequal indices yields exactly n[(1-b)^(n-1)+(n-1)(1-a-b)_+^(n-1)-n(1-a)^(n-1)(1-b)^(n-1)]. Normalizing by n(1-b)^(n-1) gives 1-n(1-a)^(n-1)+(n-1)((1-a-b)_+/(1-b))^(n-1), strictly decreasing until b=1-a and constant thereafter; variance at b=a is positive for a<alpha_n. This proves the one-switch/plateau/all-positive trichotomy with the claimed explicit zero. Zero-covariance nonindependence follows from G_n(b)=1 implying G_n(a)=1 while G_n(a)=0 has positive probability. Expansion at a=x/n,b=y/n verifies e^(-y)-(1+xy)e^(-x-y); bracketing establishes the moving zero limit. Independently recomputed rational-grid sign and exact covariance identities for n=3..11 and checked finite grid/exponential diagnostics in inspected verify.py; bounded numerics support, not prove, infinite statements.

## originality

PASS

The exact two-threshold covariance sign diagram, sharp switch and dependent plateau are distinguishable from the classical one-radius coverage count and from asymptotic spacing-score fluctuation laws. General Dirichlet tail identities make the formula accessible but do not by themselves state or imply the nontrivial uniform parameterized sign classification without its monotonicity and boundary analysis; assessed best-of-knowledge, not as historically certified priority.

## value

PASS

An exact, genuinely nonmonotone covariance sign law for two deterministically nested covering statistics is a natural finite-sample dependence question; the sharp threshold and dependent zero-covariance plateau provide an interpretable boundary of association that cannot be read off from monotone sample paths. The full all-n/all-two-radius classification is independently useful beyond textbook one-threshold expectation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
