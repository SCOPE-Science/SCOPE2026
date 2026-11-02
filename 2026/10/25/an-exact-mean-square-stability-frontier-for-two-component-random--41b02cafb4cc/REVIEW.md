# Independent mathematical audit

## correctness

PASS

The reverse two-step epoch matrix is M^T because individual gradient matrices are symmetric. Independent epoch permutations yield the exact PSD-preserving covariance update T(X)=1/2(MXM^T+M^TXM). Its spectral radius is the positive-cone Perron eigenvalue, so strict contraction on PSD covariances is equivalent to convergence for all deterministic starts. The small-step Lyapunov operator associated with H1+H2>0 is stable, hence the first positive det(I−T)=0 crossing gives the initial stability interval, and a PSD fixed covariance at the boundary certifies nondecay for some rank-one deterministic start. Four fresh independent exact symbolic specializations verify det(I−T)=αβη³(1−x)F1F2/4; the concrete quartic root was counted exactly by Sturm analysis. Finite symbolic specializations corroborate, not replace, the general algebra in the reviewed proof.

## originality

PASS

Ying et al. 2018 analyze constant-step random reshuffling but supply sufficient small-step and steady-state performance guarantees. Mulayoff–Michaeli analyze exact mean-square stability for iid minibatch SGD, a different operator. No inspected theorem states the two-step reshuffling first-boundary factorization; a general random matrix-product result could have an equivalent specialization.

## value

PASS

For a minimal but noncommuting quadratic least-squares example, this gives an exact necessary-and-sufficient initial mean-square step-size range, rather than conservative single-component or general sufficient bounds. The example demonstrates a meaningful epoch-level stability gain beyond one component active multiplier bound.

The dated certificate retains the supplied scientific assessment, sources and limitations.
