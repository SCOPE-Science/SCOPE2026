# Independent mathematical audit

## correctness

PASS

The normalized logistic flight takes ux to ux exp(s)/(1-ux+ux exp(s)) with s=Au(1-x). At a positive fixed point this gives 1-u=s(exp(s)-1)/A and x=(A-s exp(s))/(A-s(exp(s)-1)). Positive x is equivalent to 0<s<W(A), and 1-u increases strictly from 0 to 1-exp(-W(A)). For 0<x<1 the return-map logit derivative is 1/[x(1-ux)]-Au>0 by A<4. The map-minus-identity sign is the sign of Au(1-x)-log(1+(1-u)/(u(1-x))), strictly decreasing in x; thus the positive fixed point exists precisely for u exp(Au)>1 and attracts the admissible positive starts. The pre-harvest biomass is constant on this limiting periodic orbit, not generally during a transient; sustainable yield refers to the limiting cycle in the proof. Divide the pulse removal by the actual time s/r. The derivative of the resulting normalized yield has the sign of CB/(A+s^2 exp(s))-(1-exp(-s)); the first term strictly decreases from A to 0 as positive C,B decrease and the denominator increases, and the other term strictly increases. This proves the unique transverse global maximizer and both zero-yield limits. The slope derivative at fixed s has sign opposite to C^2-s^2 exp(s); the optimizing equation as a function of C has positive derivative and is negative at C=s exp(s/2) by 2 sinh(s/2)>s. Thus the optimal C exceeds that point and the envelope derivative is strictly negative. Cycle conservation expresses the yield deficit from 1/4 exactly as the temporal mean of (x-1/2)^2. Rescaling s=Az yields analytic stationarity with leading 1-2z; the first corrections give s=A/2-3A^2/16+19A^3/192+O(A^4). Then u=1-A/4+O(A^2), x*=1/2+A/16+O(A^2), and the normalized flight at relative time z is 1/2+A(z-1/2)/8+O(A^2) uniformly on [0,1]. The squared deviation integrates to A^2/768+O(A^3); the strict ceiling follows for any nonconstant flight. Replay: `cd /workspace && python audit_checks.py 4` verifies the fixed point and score algebra, stationary coefficients, squared-flight coefficient, and the A=1 root bracket with rational bounds.

## originality

PASS

The feedback model and persistence conditions already belong to Córdova-Lepe et al. Their discussion identifies the actual per-time objective's first-order conditions as open. The contribution is the exact unique optimizing effort for that fixed feedback law, strict slope comparative static, and sharp small-slope deficit; an existing fixed-period solution and the usual continuous-harvest ceiling are not new here.

## value

PASS

This resolves a stated sustainable-yield question for the originating model's explicit linear example. Maximizing catch per physical time matters when effort changes both biomass and the time denominator. Uniqueness makes the effort prescription unambiguous, and the strict and quadratic losses explain the cost of slower feedback near the continuous limit beyond the generic upper bound.

The dated certificate retains the supplied scientific assessment, sources and limitations.
