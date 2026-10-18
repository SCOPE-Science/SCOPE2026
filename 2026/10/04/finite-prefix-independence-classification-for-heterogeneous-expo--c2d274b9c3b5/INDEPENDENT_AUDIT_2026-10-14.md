# Independent mathematical audit

## correctness

PASS

For q=k-1 iid Exp(rate 1) prefix observations, M=max(X_1,...,X_q), Y=Exp(x), Z=Exp(z), the likelihood ratio density f_{max(M,Y)|Y>M}/f_{max(M,Y)} is proportional to [1+(q/x)T_x(e^{-t})]^{-1} with T_x(u)=(u^{1-x}-u)/(1-u). Differentiation gives (1-x+xu-u^x)/(u^x(1-u)^2), with strict sign from convexity/concavity and the decreasing change u=e^{-t}. This gives sign Cov(I_k,I_{k+1})=sign(x-1)=sign(lambda-lambda_k) for all z>0. Pairwise independence inductively forces lambda_1=...=lambda_{n-1}. Conversely, when the first n-1 are iid, earlier record indicators depend on ranks, independent of prefix maximum; the arbitrary independent terminal X_n tests only that maximum. n=2 is vacuous; x=1 exactly zero. L_q(s)=prod_{j=1}^q j/(s+j) reproduces joint/marginal formula algebraically. Finite testing was not used as a universal proof.

## originality

PASS

The potentially original result is the all-n finite-prefix iff condition with unconstrained last scale and a signed adjacent-covariance law, not the classical iid independence or the infinite-sequence equal-law corollary. Direct primary comparisons and Resultary semantic search identify only low-index heterogeneous-exponential formulas and a nonexponential counterexample, neither dominating the stated theorem.

## value

PASS

The independence classification is an exact structural boundary for a standard heterogeneous exponential record model. It identifies a one-observation detection delay and determines the direction of induced covariance independently of the next scale, refining the qualitative prior observation that heterogeneous indicators generally depend. It is a motivated, complete finite-prefix classification rather than an arbitrary small example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
