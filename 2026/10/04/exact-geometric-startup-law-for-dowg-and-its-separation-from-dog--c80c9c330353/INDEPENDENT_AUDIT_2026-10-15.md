# Independent mathematical audit

## correctness

PASS

Under g=-G on the pre-hit interval, the published DoG denominator is sqrt((t+1)G^2), so x_1=r_eps and x_n/r_eps=prod_{j=2}^n(1+j^-1/2). Summing log(1+1/sqrt j) yields 2sqrt n-(1/2)log n+O(1), hence tau_DoG=(log R)^2/4+O(log R loglog R). In DoWG, v_t=G^2 r_eps^2(1+sum_{1<=k<=t} y_k^2); p=y/sqrt S obeys F(p)=p(1+p)/sqrt(1+p^2(1+p)^2), a monotone increasing orbit from 1/sqrt 2 to the unique root p^3+2p^2-2=0. F_prime(p*)=(1+2p*)/(1+p*)^3<1 ensures exponentially summable deviations; product y_t=C*(1+p*)^(t-1)(1+o(1)). Independent numerical iteration gave Tribonacci lambda=1.839286755214161 (lambda^3-lambda^2-lambda-1=0). The analytic estimates justify the asymptotic first-hit count and do not assert post-hit behavior.

## originality

PASS

The defining papers provide the precise DoG/DoWG algorithms and relative aggressive weighting motivation, with convergence bounds but not the constant-subgradient exact coherent trajectory or Tribonacci fixed point. The comparison goes beyond their pointwise stepsize statements because paths diverge. Resultary nearby startup-latency work concerns dual-averaging D-Adaptation/Prodigy rather than these trajectories. No stronger implication-equivalent prior was identified after actual source-method comparison; equivalent unindexed optimizer-notes remain possible.

## value

PASS

Distance adaptation from a conservative initial radius is central to parameter-free optimization. Exact pre-hit laws on a canonical convex Lipschitz signal isolate an intrinsic qualitative startup difference—stretched exponential versus geometric and quadratic-log versus linear-log first-hit latency—without overclaiming global optimization dominance.

The dated certificate retains the supplied scientific assessment, sources and limitations.
