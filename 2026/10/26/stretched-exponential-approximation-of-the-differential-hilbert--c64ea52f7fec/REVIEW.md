# Independent mathematical audit

## correctness

PASS

For the normalized Bergman measure the monomial norm is w_k(gamma), and the orthonormal basis expansion of (1−tz)^−2 followed by termwise integration on polynomial inputs gives exactly B_nk=(n+1)sqrt(w_n(beta)/w_k(alpha))/(n+k+1). The rank-one factors u,v of T converge locally as holomorphic Hilbert-space-valued power series (v is used as a linear functional without conjugating the parameter). Thus T is trace-norm holomorphic and has norm ||u||||v||. The binomial identity gives ||v||²=(1−|z|²)^(-alpha−2), while the coefficients of ||u||² are of order (n+1)^(1−beta). For beta<2 the product is bounded by the boundary power −1+(beta−alpha−2)/2; for beta≥2 the power is −1−alpha/2 with at most a square-root log loss. The positive theta margin absorbs the log and makes the radial bound integrable. The trace-class integral agrees entrywise with B. On the jth cell with half-width h_j the radius-two complex circle in rescaled coordinates stays at distance at least h_j from the unit circle. Cauchy estimates then give a Taylor remainder through degree 2m−1 of at most 2C h_j^(−1+theta)4^(−m). Gaussian exactness and the total weight two bound the cell residual by 8C h_j^theta 4^(−m). The geometric sum and omitted tail give (1), with at most Jm rank-one terms. Taking J=m=k, then k=floor(sqrt(n−1))≥sqrt(n)/2 for n≥4, gives (2) from the approximation-number characterization and operator norm ≤ trace norm. Small n are absorbed in the constant, and summability of exp(−cp sqrt(n)) holds for every p>0.

## originality

PASS

Credit the earlier indexed theorem with root-exponential spectral decay and all-p Schatten membership in the full same-operator regime, and credit Li–Zhou with the rank-one integral and trace class. Those are not independent novelty claims supported by this review. The primary finding's distinct contribution is the trace-norm error for its explicitly prescribed positive dyadic Gauss–Legendre sample operator, uniformly for independently chosen J and m. The earlier indexed approximants are coefficient-space row blocks rather than positive evaluation samples. The closest inspected general quadrature literature supplies techniques or different rules, not explicit coverage of this operator estimate for those samples.

## value

PASS

The explicit sample-based construction is useful beyond an abstract decay bound: positive parameter-independent nodes and weights on each interval give an operator applied using only Jm real evaluations of the input function, while the output error is controlled in trace norm on the full spaces. Separating the quadrature order and endpoint cutoff quantifies two different sources of error without computing singular vectors or relying on finite sections. No independent value is assigned to restating the earlier indexed spectral conclusions.

The dated certificate retains the supplied scientific assessment, sources and limitations.
