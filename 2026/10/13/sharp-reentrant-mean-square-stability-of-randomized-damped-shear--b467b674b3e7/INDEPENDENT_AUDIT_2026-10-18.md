# Independent mathematical audit

## correctness

PASS

For A1=−aI+bE12 and A2=−aI−bE21, exact exp(2hAi) is a damped triangular shear. Directly (M1^T M1+M2^T M2)/2=exp(−4ah)(1+2b²h²)I and (E M)^T(E M)=exp(−4ah)(1+b²h²)I. Independent symbolic matrix multiplication verified the undamped identities. Conditioning at each iid step gives the exact all-k mean-square and mean norm laws, not a finite-time extrapolation. The derivative of F(z)=log(1+z²/2)/z reduces to g(s)=2s/(1+s)−log(1+s), whose derivative (1−s)/(1+s)^2 proves a unique positive maximum at s_*>1. The three regimes beta<,=,>beta* give all-step stable, one neutral, or exactly two crossings with a reentrant unstable band. Checks include b=0 and a=1,b=4,h=1/4 yielding q=3/e and m=2/e.

## originality

PASS

The original randomized exponential generator selection and generic mean-square stability tests are known. The claim is the exact two-shear scalar energy law and global nonmonotonic phase diagram over all positive grid steps, not a new general Lyapunov criterion; the originating finite-horizon convergence theory does not imply this long-time sharp regime without specialized computation.

## value

PASS

Identifies an exact, sharp and genuinely counterintuitive reentrant stability boundary for a natural two-generator randomized splitting: coarser steps can be mean-square stable when intermediate steps are unstable, and mean and mean-square can move in opposite directions. Provides a diagnostic model for separating convergence from approximation accuracy.

The dated certificate retains the supplied scientific assessment, sources and limitations.
