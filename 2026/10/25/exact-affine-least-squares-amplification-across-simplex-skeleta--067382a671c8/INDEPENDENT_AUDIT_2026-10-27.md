# Independent mathematical audit

## correctness

PASS

For n>=3 and 1<=s<=n, the face-balanced probability mixture has covariance contrast eigenvalue lambda=(2n-s-1)/[n(n-1)(s+1)]>0, so its affine reproducing kernel is K(t,u)=1+nB(sum_i t_i u_i-1/n), B=(n-1)(s+1)/(2n-s-1). Convexity of F(t)=E|K(t,T)| reduces the endpoint norm to a simplex vertex, where T_1 is 0 with probability 1-s/n and otherwise Beta(1,s-1). Integrating min(T_1,nu), nu=(s-1)/[(n-1)(s+1)], gives exact sharp symmetric L^1/L^infty norm 2B(1-nu)^s-1; s=1 is identity, s=n agrees with known volume formula. At fixed s, B->(s+1)/2 and norm->s; at s/n->alpha, the ratio norm/n->2alpha exp(-alpha)/(2-alpha). Independently recomputed rational covariance, endpoints and positivity for every n=3..39, 1<=s<=n; not a proof of the infinite ranges.

## originality

PASS

PASS qualified. The published Resultary 2026-10-04 full-volume simplex L2-projector norm is exactly the s=n endpoint by direct substitution, while the s=1 case is standard interpolation. Neither covers the intermediate face-balanced skeletal measure 2<=s<=n-1, its Beta atom mixture, nor its distinct asymptotic regimes. Polynomial face-Sobolev bases and finite-sample concentration control different inner products and random designs. No inspected broader theorem determines this skeletal projector Lebesgue function, although extensive approximation-theory literature leaves priority risk.

## value

PASS

PASS. Exact stability amplification of affine L2 projection is important in numerical approximation; skeleton-supported observations naturally interpolate between vertex data and volume data. The complete intermediate-skeleton formula and the fixed-rank/extensive-rank asymptotics quantify a nontrivial change in the projector norm, not a table recomputation of the volume endpoint. Application to arbitrary shape follows from face-balanced affine invariance, not arbitrary unbalanced face area measure.

The dated certificate retains the supplied scientific assessment, sources and limitations.
