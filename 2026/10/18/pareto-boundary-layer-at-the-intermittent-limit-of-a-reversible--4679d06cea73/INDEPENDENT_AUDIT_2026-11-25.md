# Independent mathematical audit

## correctness

PASS

The reverse probabilities are the inverse-branch derivatives because the base preserves Lebesgue. The branches contract by at most lambda<1 and the finite-word probabilities are continuous in the initial x; uniform convergence of the stable compositions then gives the weakly continuous version of the conditional law, including at x=0. The stationary backward history pushes forward to the natural stationary measure for the triangular map: advancing a history prepends the current branch to its stable composition. At any y, at most two words of length m can code it, since the corresponding intervals partition [0,1] up to endpoints. Their probabilities are at most lambda^m each, so boundaries have zero mass. The cylinder [0,y_n] therefore has mass lambda^n by starting the all-zero branch history at zero. For b=a/2, let w_n=delta lambda^n/y_n. The exact increment is delta b lambda^(n-1)/(1-(b/lambda)y_n). Also 1/y_(n+1)-1/y_n>=b, so y_n<=4/(n+4) for a>=1/2. Replacing the denominator factor by 1 costs O_T(delta log(1/delta)) through n<=T/delta. Summing gives w_n=delta+(a/lambda)(1-lambda^n)+o(1) in this range. At n=floor(t/delta), lambda^n tends to exp(-t/2), giving the claimed scaled orbit. For z>0, bracketing by times t(z)±eta with t(z)=2 log(1+1/z) then gives the limiting CDF. The atom-free endpoint gives its value at z=0; a monotone CDF mesh gives compact-uniform convergence. The limit's survival is 1/(1+z), with divergent integral, not an assertion about convergence of unbounded moments or a planar density. The frozen rational and finite bracket checks were inspected but not executed; the proof supplies the full limit.

## originality

PASS

The supported distinct finding is the scaled near-intermittent law together with the cylinder-orbit crossover. The map, endpoint-cylinder mass and intermittency itself are credited to the original family analysis. The present measure-theoretic use of those masses does not invoke its corrected density premise.

## value

PASS

The conditioning and scale are intrinsic: the endpoint is the neutral location at intermittency, and linear loss and quadratic drift balance when y is of order 1-a. The weak limit describes the entire transition in the boundary layer, retains a nontrivial law despite endpoint collapse, and shows an infinite-mean limiting profile without needing a planar density. It is more informative than either the unscaled masses or a single endpoint asymptotic.

The dated certificate retains the supplied scientific assessment, sources and limitations.
