# Independent mathematical audit

## correctness

PASS

Diagonalizing common SPD H decomposes original single-index SAGA into scalar random recurrences x′=(1−s)x+s(y_I−m), y_I′=x at old iterate, s=ηλ. Actual source derives exact conditional four-moment matrix for M=(x²,xm,m²,v), and a positive-definite quadratic V with Q=n+(n−1)²s, K=1+(n−1)s, positive (x,m) determinant and variance coefficient. Independently checked exact polynomial identity E[V′−V|x,y]=s P_n(s)x², P_n(s)=(2n−1)(s−1)(1+(n−1)s)−1, symbolically in formal n,s and with independently enumerated exact-rational n≤6 scalar updates. Unique positive root τ_n>1 follows from sign and quadratic structure. For 0<s<τ_n, summability of E x_k² plus stable table filter e_{k+1}=(1−1/n)e_k+(1/n)E x_k² implies all components converge in mean square. For s≥τ_n any nonzero deterministic scalar state keeps E V nondecreasing and cannot have E x²,e→0. The spectral-max criterion and τ_n monotonic/asymptotic expansion follow from the root equation, including excluded boundary. Finite tests verify identities but the analytic positivity, telescoping and necessity establish all n.

## originality

PASS

The original Defazio–Bach–Lacoste-Julien SAGA paper provides its estimator and a sufficient stepsize convergence bound in the strongly convex setting, and the 2019 expected-smoothness optimization provides improved sufficient guarantees, neither necessary-and-sufficient stability for all deterministic saved tables. A known n=2 scalar threshold and unrelated SAG all-n bounds do not imply the full n≥3 SAGA polynomial and necessity. No actually retrieved Resultary match covered the same algorithm, memory initialization, and sharp threshold. Older stochastic jump-linear-system or memory method equivalence is a genuine residual risk.

## value

PASS

A sharp all-initialization mean-square stability frontier for the canonical identical-component SAGA test family is a natural numerical-analysis invariant. It separates estimator memory instability from Hessian heterogeneity, yields exact sample-count dependence τ_n↓1, and supplies an explicit energy witness plus impossibility boundary. This is not a trivial substitute of n into a known two-component example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
