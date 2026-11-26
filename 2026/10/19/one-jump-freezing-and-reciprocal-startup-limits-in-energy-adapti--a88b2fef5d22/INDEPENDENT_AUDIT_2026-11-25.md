# Independent mathematical audit

## correctness

PASS

The exact auxiliary-energy decrement gives ||x_{k+1}-x_k||=(r_k-r_{k+1})/||F(x_k)|| whenever the direction is nonzero. The first step gives x_1=x_star+O(1/eta) and r_1=O(1/eta) explicitly. In a closed ball around x_star with ||F||>=m>0, choose eta so that ||x_1-x_star||+r_1/m is strictly below the radius. This bounds the step taking a purported first exit as well as all earlier steps, so no exit occurs. Thus r decays with ratio at most (1+2 eta m^2)^(-1), total remaining path length is at most r_1/m, and the limit stays inside the nonstationary ball. Set epsilon=1/(2 eta). Expanding the first displacement and energy gives x_1=x_star+epsilon r_0 v_0/||v_0||^4+O(epsilon^2) and r_1=epsilon r_0/||v_0||^2+O(epsilon^2). Local Lipschitz continuity gives F(x_1)=v_star+O(epsilon), so the second displacement contributes -epsilon r_0 v_star/(||v_0||^2 ||v_star||^2)+O(epsilon^2). Since r_2=O(epsilon^2), the full subsequent path contributes at most r_2/m. For the scalar quadratic, F=x/(2 sqrt(c+x^2/2)) gives the stated inverse landing point. At c=x_0=1, the first-step formulas give x_1=-2+9/(eta+3) and r_1=3 sqrt(3/2)/(eta+3). On [-2,-1], F is negative with magnitude at least 1/sqrt(6), so the increasing tail moves by at most 9/(eta+3); -2+18/(eta+3)<-1 for eta>=16 closes that trap. Substituting F(1)=1/sqrt(6) and F(-2)=-1/sqrt(3) gives 9+9 sqrt(2)/2.

## originality

PASS

The mathematical contribution is the general conditional large-step theorem for autonomous preconditioners, including the uniform infinite-tail estimate and first correction. Neither the recurrence nor the qualitative possibility of auxiliary-energy depletion is new. An independently indexed scalar result gives exact equivalent coverage of the reciprocal quadratic limit and correction; those scalar formulas should not be treated as an originality basis independent of the general theorem. The relative catalogue dates do not settle priority.

## value

PASS

An unconditionally stable auxiliary variable can vanish while a primal iterate converges away from stationarity, even for a strongly convex objective. The general theorem tells when this occurs, locates the infinite-trajectory limit and its first correction, and separates the first-step overshoot from the entire small remaining path. This directly clarifies what the stability guarantee of an existing optimization scheme does not deliver, beyond a single numerical failure or scalar formula.

The dated certificate retains the supplied scientific assessment, sources and limitations.
