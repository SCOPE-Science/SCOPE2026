# Independent mathematical audit

## correctness

PASS

Conditioning on the new type yields p_A=q(1-y)/(1+(1-2q)y) and p_B=q(1+y)/(1-(1-2q)y), so their average is f_q(y)=q+b y²/(1-a²y²), b=2q(1-q)(1-2q). The fourth-moment summability of y_j makes the quartic Taylor remainder converge in L²; for a fair-walk imbalance T_n=sum S_j²/(j+2)², E T_n=log n+O(1) and Var T_n=4 log n+O(1). Subsequence Borel-Cantelli and monotonicity give a.s. T_n/log n->1. A bounded-increment martingale representation yields sqrt(log n) Gaussian compensator fluctuations; the edge martingale has bracket nq(1-q)+o(n), while the mixed bracket is O(log n)/sqrt(nlog n)->0. Thus the joint normal limits are independent; q=1/2 and hard-choice binomial cases follow exactly. Independently recomputed q=1/4,y=1/3 rational predictor f=19/70 and cross bracket -9/70. Verifier was read, not reported executed in this run.

## originality

PASS

The soft two-type attachment model is explicitly already known (Ben-Hamou–Broutin–Cazaux 2026 and prior community-modulated recursive trees), but those main theorems concern degree proportions/local limits. The cross-type edge compensator, its logarithmic bias and separate joint CLT of fluctuations at two scales are additional observables not implied by degree limit convergence. Best-of-knowledge qualified by related homophily literature.

## value

PASS

Cross-type edge counts are natural homophily measurements. Their q-dependent O(log n) bias, sign reversal across q=1/2, and asymptotically independent predictable and unpredictable noise at scales sqrt(log n) and sqrt n provide usable quantitative structure not supplied by standard degree-proportion convergence.

The dated certificate retains the supplied scientific assessment, sources and limitations.
