# Independent mathematical audit

## correctness

PASS

For each coordinate i, exact quadratic minimization updates error by T_i=I−e_i e_i^T H/H_ii; both equal-cost samplers apply n updates. For n=2, idempotent T_i yield four independent-sampling paths and two permutation paths. Their Euclidean Gram expectation difference is exactly (1−c^4/(a²b²))I/4 for arbitrary SPD 2x2 H; Sylvester gives |c|²<ab and strict positivity for nonzero start. In the explicit n=3 example H has leading principal minors 1,7/16,3/32, so SPD. An independent rational SymPy enumeration of all 6 RR and 27 IID products reproduces RR−IID Euclidean error 1949/55296>0 and RR−IID Hessian energy −1309/55296<0 for e=(0,1,0). Thus n=1 coincides, n=2 impossible, n=3 witness exists. This is one epoch only, not all epochs or all higher dimensions.

## originality

PASS

Best-of-knowledge qualified PASS for the joint dimension-sharp all-2D Euclidean identity and explicit smallest 3D Euclidean-versus-objective reversal. Gürbüzbalaban–Ozdaglar–Vanli–Wright analyze random permutation against IID sampling in a specialized diagonally dominant Hessian family and convergence criteria, whereas Wright–Lee analyze another structured family with rates. Oswald–Zhou derive randomized SOR energy seminorm results; Lai–Lim discuss symmetric positive-semidefinite matrix products, whereas Euclidean coordinate-step operators here are generally oblique. Prior dimension-two Gauss–Seidel deterministic-order transient findings concern a different risk and sampling scheme. No inspected published result states this full exact comparison; an unindexed special case could still exist.

## value

PASS

A practical optimization diagnostic is whether reshuffling uniformly reduces Euclidean solution error versus independent resampling, not merely the objective. The exact two-coordinate isotropic advantage and dimension-three counterexample identify the minimal structural failure of that plausible universal rule; one concrete SPD system improves objective while worsening Euclidean error. These are genuinely distinct metrics with opposite signs, a substantive boundary for algorithm comparisons.

The dated certificate retains the supplied scientific assessment, sources and limitations.
