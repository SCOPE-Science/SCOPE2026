# Independent mathematical audit

## correctness

PASS

For scalar |a|>1, Q>0, R>0, h!=0, each received update g(P)=Q+(a^2 R P)/(h^2 P+R) lies in [Q,Q+a^2 R/h^2], independent of previous P. After N>=1 losses, f^N(g(P))=B^N g(P)+Q(B^N-1)/(B-1) with B=a^2, giving deterministic Q B^N<=M<=C_+ B^N. For the staged transient kernel T=pI+cJ, the exact binomial expansion e1^T T^(n-1)1=Σ_{j=0}^{min(m-1,n-1)}C(n-1,j) p^(n-1-j)c^j follows for all m>=2, n>=1; its dominant j=m-1 term has survival asymptotic [c^(m-1)/((m-1)!p^m)]n^(m-1)p^n. Integer logarithmic thresholds then give Pr(M>x)=Theta(x^-alpha (log x)^(m-1)), alpha=-log p/log B, no unjustified sharp constant because lattice oscillations. Comparing B^(rN) moments yields finiteness iff p B^r<1, including boundary divergence, and monotone inversion gives claimed extreme quantile order. Independently computed exact rational powers of T vs finite binomial sum through n=30 for m=3,p=1/2,c=1/4, checking sample survival 9/32,39/512,81/8192 at n=5,8,12. Formula is proved algebraically; finite checks only diagnostics. Inspected RESULT.md blob c81e34ed..., metadata and audit status files.

## originality

PASS

Earlier Gilbert–Elliott channel results give power-tail bounds or logarithmic exponent for a two-state channel, whereas this precise m-stage upper-triangular transient kernel has a nontrivial Jordan block producing an n^(m-1) survival factor and hence (log x)^(m-1) peak covariance envelope. Standard phase-type and scalar Kalman ingredients may individually be classical; searched material did not establish the combined staged model classification. Qualified priority, not a claim to originate Jordan phase-type asymptotics.

## value

PASS

A motivated family of packet-loss models with identical persistence eigenvalue but varying numbers of progressive stages has exactly distinguished risk tails, moment thresholds and extreme quantiles. This demonstrates concrete limitations of characterizing networked estimator reliability by the power exponent alone and covers every stage count, not an arbitrary numerical example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
