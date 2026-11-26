# Independent mathematical audit

## correctness

PASS

At the first step the gradient is X_0 and the source adds e to every squared-gradient entry before taking marginals. They are r=c=(4e,B^2+2e), with total B^2+6e, yielding exactly the two printed active normalized updates for B>0. Put a=sqrt(2e), s=sqrt(B^2+2e), and t=u_2/u_1=2aB/s^2. When both the floor is inactive and clipping is active, the displacement on the diagonal is rho*s*(1,t)/sqrt(1+t^2), so the exact objective ratio is 1+rho^2−2rho(a+Bt)/(s sqrt(1+t^2)). For fixed e, B tending to infinity gives the claimed limit. At the recommended B=1, the parameter RMS exceeds 0.5 and u_1>2, so both conditions hold. The subtracted term is at most 6rho*a/B<8.5e-17, proving the strict numerical bound without rounding. An independent decimal replay gave 1.000099999999999915147186257614. For the counterfactual full elementwise moment the raw entries are sqrt(2/3) and B/sqrt(B^2+e); their matrix RMS never reaches 1. Taking the limit of the resulting normalized coordinates gives 1−rho+5rho^2/12 and hence descent in the stated interval. The gradient in the small coordinate becomes small relative to B, not absolutely as B increases at fixed e.

## originality

PASS

The supported distinction is the default-scale first-step ascent on an isotropic strongly convex objective, proved with a family and isolated by a same-scale full-moment comparison. The inspected source and nearby records address the ingredients or other failure modes, but do not cover that result. The later full-batch monotonicity theorem concerns a different scaling with a restricted step and is not a contradictory or dominating claim.

## value

PASS

The small example tests a specific safeguard of a standard algorithm at its published settings: a clipped update can increase even an isotropic quadratic without any stale history. The exact family identifies the mechanism and the counterfactual holding all other pieces fixed distinguishes magnitude misallocation by the factorization from a generic overly large step. This is a useful boundary on a descent interpretation of clipping, not just an arbitrary anomalous run.

The dated certificate retains the supplied scientific assessment, sources and limitations.
