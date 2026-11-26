# Independent mathematical audit

## correctness

PASS

The fixed 1/4 step gives separate multipliers 1/4 and 1-lambda_k on the extrapolated coordinates. The inner coordinate contracts by at most 3/4 on successive two-step running maxima. The FISTA quadratic identity gives t_k^2-t_k=t_(k-1)^2, with t_k comparable to k+1 and increments tending to 1/2. To check the critical energy identity, write y for the extrapolated outer coordinate, substitute z=t y-(t-1)v and z_next=z-lambda t y, v_next=(1-lambda)y, and complete the square; the remaining y^2 terms have coefficients lambda t and lambda^2 t^2(1-lambda). Monotonicity of lambda_k then yields E_next<=E-lambda_k t_k y^2, with the k=0 term t_0^2-t_0=0. For gamma<2 the v^2 coefficient grows like k^(2-gamma). At gamma=2 it is bounded below, so v and z are bounded; y-v=(z-v)/t gives O(1/k) increments and energy dissipation gives sum y_k^2/k<infinity. The log-mesh interpolation is Lipschitz at infinity and L^2 there, forcing y_k to vanish by the disjoint-interval argument. For every gamma>2, dominated convergence makes S(a)=sum lambda_k t_k<1 for some integer a, using the summable majorant proportional to (k+1)(k+2)^(-gamma). Starting from v=1, the convex combination for y and telescoping z give 1>=z_k>=1-S(a)>0 and 0<v_k,y_k<=1. z decreases to a positive limit; the v recurrence averages that convergent input with weights 1/t_k whose sum diverges. The initial u=0 stays zero. This proves convergence to a strictly nonoptimal inner minimizer for a chosen offset, not for all offsets.

## originality

PASS

The original FBi-PG iteration and subcritical convergence ideas are prior. The supported increment is the sharp uniform-in-offset selection boundary on this benchmark, specifically endpoint selection for the actual quadratic-identity FISTA recurrence and an obstruction at a sufficiently large offset for each supercritical exponent. Related critical convergence theorems use different discrete updates; an exact-recurrence inner objective rate cannot distinguish points on this line of inner minimizers.

## value

PASS

The rank-deficient quadratic cleanly distinguishes convergence of the inner objective from selection of a point on its minimizer line. It gives a sharp endpoint where summability alone predicts neither failure nor success, plus an explicit stable obstruction on the other side for every supercritical exponent. That is an informative boundary for the original FISTA schedule, not an unsupported general impossibility claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
