# Independent mathematical audit

## correctness

PASS

Condition on the first two iid draws and the remaining multinomial counts B_i. When the two match bin i, the increment to W_f is 2Δf(B_i)+Δ²f(B_i); when distinct i,j it is Δf(B_i)+Δf(B_j). Exchangeability of the pair collision indicators gives Cov(T,W_f)=binom(n,2)[(1-s2)sum p_i² EΔ²f(Bin(n-2,p_i))+2sum p_i(p_i-s2)EΔf(Bin(n-2,p_i))]. For convex f, the first term is nonnegative and strictly positive unless f affine (all positive p imply B_i full support). The second is Cov_{I~p}(p_I,g(p_I)) with nondecreasing g by binomial coupling, hence >=0. Uniform p cancels this covariance, and the binomial second difference yields a quadratic sign polynomial P_{n,m}(r), plus exact r=0 and r=1 cases. I independently enumerated all n=5, three-category occupancy vectors with p=(1/2,1/3,1/6) for f(k)=binom(k,2): Cov(T,W_f)=535/162>0. Analytic proof, not finite enumeration, controls all parameters.

## originality

PASS

Best-of-knowledge the full quantified final claim is not shown covered by the inspected primary statements, including aliases/stronger-theorem comparisons. Earlier work shares the variables, but Poisson approximations to their distributions do not assert finite mixed covariance signs or a universal all-convex-score inequality. Neither entails the strict iid nonuniform convex covariance inequality or exact two-threshold uniform frequency signs. No known exact table establishes the quantified all-n,m,p,f theorem. Computability of individual cases does not imply the uniform convex sign or quadratic classifications. Its bounding errors cannot determine the exact sign of Cov(T,F_r), particularly at equality n=2m; the two-draw first/second-difference identity supplies the missing statement. Inaccessible relevant full text is explicitly a residual risk; absence from a database alone is not novelty proof.

## value

PASS

Collision pairs are Simpson concentration, while additive convex occupancy scores quantify clustering; their strict universal finite-sample association under unequal categorical probabilities is a structural sign law. Uniform frequency counts show two exact sign transitions and a sharp zero at n=2m for singletons, meaningful inference invariants rather than arbitrary examples.

The dated certificate retains the supplied scientific assessment, sources and limitations.
