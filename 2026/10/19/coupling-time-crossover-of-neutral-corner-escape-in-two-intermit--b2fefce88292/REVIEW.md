# Independent mathematical audit

## correctness

PASS

Reconstructed the first-exit proof on the exact unwrapped branch, including the output at the first hit. Jensen gives m_next >= m+m^p, so the inverse-power decrement on [0,r) localizes every n-step survivor to a fixed box after scaling by n^(1/(p-1)). At bounded n*epsilon the exact scaled recurrence is Euler-consistent until ODE blow-up. If blow-up precedes one, advance to a large but fixed mean M and bound the remaining time by a dyadic sum of order n*M^(1-p)+O(log n), forcing actual exit. The ODE maximum has derivative between M^p-rho*M and M^p, hence a universal blow-up coefficient. Scaling a solution down gives a supersolution by convex homogeneity; two starts on one positive ray cannot have the same blow-up time by the universal coefficient. Thus the time-one equality set has area zero by radial integration. For n*epsilon tending to infinity, the difference contracts by a factor at most (1-2*epsilon)(1+O(1/n)) on bounded sets; an o(n)-step layer with epsilon times its length divergent erases disparity while preserving the scaled mean to o(1). The scalar mean limit plus the exit bound gives the triangle u+v<2*a_p. As a separate exact check at epsilon=1/2, the first step applies the scalar branch to the mean and makes both coordinates equal. If b_n is the scalar n-fold backward threshold of r and 2*b_n<r, the survivor area is exactly 2*b_n^2, versus b_n^2 uncoupled. The limiting area normalization includes the factor r^-2. In (mean, absolute difference), the two nonnegative cross derivatives give monotonicity in rho. The square expands strictly near (a_p,b) with 0<b<a_p by strict damping of the upper coordinate, and the triangle loses positive area near an off-diagonal sum-boundary point by strict Jensen growth. Bounded-time dependence plus the large-mean exit bound handles continuity at finite rho; continuous-time fast synchronization gives continuity at infinity. The supplied script was read, not run; its finite trajectory comparisons are not needed for the proof.

## originality

PASS

The same map, local uniform square ensemble and escape exponent are established comparison points, not the novelty. The supported distinct claim is the all-sequence coefficient crossover, including its intrinsic finite-rho survival area and its sharp endpoints, not an assertion of priority for the exponent or Euler scaling alone.

## value

PASS

The power law alone misses a discontinuity in leading survivor mass between zero and any fixed positive coupling. The theorem resolves that noncommuting limit in a natural observation window and determines an intrinsic, continuous monotone coefficient with strict interior bounds. It upgrades a directly comparable numerical escape problem without claiming an invariant-measure result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
