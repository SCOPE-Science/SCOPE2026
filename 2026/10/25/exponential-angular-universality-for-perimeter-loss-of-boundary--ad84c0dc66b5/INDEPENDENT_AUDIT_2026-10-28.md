# Independent mathematical audit

## correctness

PASS

Verified the full-edge hull decomposition into unchanged edge segments and corner chords; by the cosine law the exact corner loss is F_alpha(a,b)=a+b-sqrt(a^2+b^2-2ab cos(alpha)). For a fixed corner the two directed distances to the nearest sampled points have density N(N-1)L^-2(1-(a+b)/L)^(N-2) on a,b>0, a+b<L. Their sum has mean 2L/(N+1) and their ratio is uniform, yielding the stated Phi(alpha)=1-(1-c^2)atanh(c)/c, c=cos(alpha/2). On an empty-edge event the global loss-minus-corner sum is bounded by (m+1)L and the union bound yields precisely the claimed exponential error. Local disjoint arc void probabilities imply 2m independent mean-one exponential limits; uniform exponential gap tails plus exponentially unlikely empty edges yield moment convergence, not only a weak limit. Gamma(2,1)-uniform factorization yields mean sum Phi and variance sum(6Phi-4c^2-Phi^2); Z is nondegenerate nonnegative, hence non-Gaussian. Independently recalculated angular mean/variance by direct midpoint integration at five angles to <1e-7.

## originality

PASS

PASS best-of-knowledge for the exact finite-sample angular mean and exponential edge-memory bound; local independent Poisson corner processes, whose limiting law may imply the weak part, are credited and not portrayed as newly originated.

## value

PASS

Expected perimeter loss is a basic intrinsic-volume error for boundary-sampled polygons. Its sharp all-algebraic-orders angle universality, finite-N 1/(N+1) normalization and exponentially small residual dependence on side lengths provide a natural useful exact benchmark distinct from max-Hausdorff approximation and missing area; the explicit non-Gaussian corner sum adds quantitative interpretation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
