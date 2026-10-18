# Independent mathematical audit

## correctness

PASS

PASS: Rebuilt the one-step projection identity and positive-semidefinite covering reformulation using w_i=p_i/C(p) and min cost of z>=0 with sum_i z_i v_i v_i^T >= I. The dual max tr Z subject to v_i^T Z v_i<=c_i has explicit positive-definite witness Z=alpha I+beta v0v0^T for t<d^2, with alpha=(d^2-t)/(d^2-1), beta=d^2(t-1)/(d^2-1) and tr Z=d(d+t)/(d+1); uniform z_i=d/(d+1) saturates. At t>=d^2 the dual Z=d^2 v0v0^T and z0=0,z_i=d saturate price d^2. Complementarity and independence of rank-one matrices (Gram eigenvalues 1-1/d^2 and 1+1/d) force all equality distributions, including t=d^2. Independent rational eigenvalue/primal-dual checks for d=2,3,5 at prices on both sides confirm boundary arithmetic; these do not replace proof for all d,t.

## originality

PASS

PASS (best knowledge): The exact optimization objective differs from the previously published unpriced least-eigenvalue SDP and from asymptotic MSE-annealed-exponent minimization. The cost heterogeneity on one row of the natural minimal-redundancy simplex frame creates a sharp d^2 transition, with a complete equality-case proof. This conclusion is best-of-knowledge, not a priority claim for general Kaczmarz SDP methods.

## value

PASS

PASS: Distinct row-measurement prices are mathematically natural in a minimal redundant tight frame; the precise cost frontier tells exactly when dropping a geometrically redundant measurement is optimal and characterizes the critical nonunique law. This sharp, all-dimensional optimizer classification is independently useful even without multi-step runtime claims.

The dated certificate retains the supplied scientific assessment, sources and limitations.
