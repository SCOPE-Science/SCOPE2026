# Independent mathematical audit

## correctness

PASS

On the specified stationary branch, the dimensionless unnormalized remaining half-line mass is U(y)=R_m(g(y)) in gas because U'=-g and U(infinity)=0. The source flux matching gives U(L)=1; the core has U=q exp(-my) and density mU, so L=log(q)/m and survival is U/q. This proves the three quantile formulas, including their joins. From the endpoints of J_m the gas-regime derivative is (H_m(qs)-H_m(q))/(mq), the exterior derivative is (H_m(qs)+1-m)/(mq), and the core derivative is zero. The first two are negative; hence positive y_q/q decreases strictly, even as log(q)/q initially increases for the width. Coupling by a common uniform survival level gives strict expectations of strictly increasing integrable observables. At q=1 the scaling-factor derivative cancels, leaving the stated s-independent kink; H_m is continuous at m=4 even with a singular spatial gas slope. For coexisting stationary profiles subtract the two quantiles: the difference integrates 1/H_m(u)-1/(mu)>0 from max(1,qs) to q. The endpoint q=m/4 is valid for the explicit gas profile, with a one-sided cusp, not a dynamical stability claim. For strong reset the core agrees identically with Exp(m), and translating the exterior multiplies both mass-one densities by 1/q. For weak reset, H_m(q)exp(-2H_m(q)/m)=q-q^2/m+O(q^3); the inverse of h exp(-2h/m) is a+2a^2/m+O(a^3), uniformly at a=O(q exp(-y)). Dividing by q and integrating the absolute first-order correction yields q/(4m), since integral_0^1 |2u-1|du=1/2. Replay: RESULT.md lines 73–146. As a separate bounded check of the strong coefficient, solve log(h/m)+m[log(H_m(1)/h)-2(H_m(1)-h)/m]=0 for h in (0,H_m(1)) by bisection (the expression tends to +infinity at zero, is negative at H_m(1), and has at most one interior minimum). The density crossing gives Delta_m=h(1-(1+h)/m), yielding 0.378426, 0.472058, 0.676129 and 0.804631 for m=4,5,10,20. The frozen verification code was inspected, not executed.

## originality

PASS

The phase selection, solution profiles, existence conditions, and width are known Grange inputs, not distinct findings. The supported distinct results are full-law physical radial order, its quantile kink, branch comparison, and sharp total-variation formulas on those profiles.

## value

PASS

The result resolves an operational localization question that droplet width and phase mass do not settle: all physical radii decrease even while the core widens. The kink and exact or sharp TV terms quantify distinct transition and scaling behavior for the whole normalized mass profile.

The dated certificate retains the supplied scientific assessment, sources and limitations.
