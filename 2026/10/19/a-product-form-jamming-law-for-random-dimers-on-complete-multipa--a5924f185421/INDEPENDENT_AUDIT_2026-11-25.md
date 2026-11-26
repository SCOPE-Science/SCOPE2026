# Independent mathematical audit

## correctness

PASS

The frozen finding (RESULT.md lines 5–22) takes fixed q>=3, all proportions positive, and independent iid atomless priorities. Uniform priority order can be realized with independent exponential clocks of rate 1/N. At time T an edge whose two endpoints remain unmatched cannot have rung earlier; exponential memorylessness gives exact rate X_iX_j/N for pair i,j, including after conditioning on past occupancy. The scaled coordinate martingale has bracket at most T/N and the bounded-cube drift is Lipschitz, so Doob and Gronwall give convergence uniformly on compact time intervals. To verify the ODE parametrization, write F(g)=prod(1−a_jg) and y_i=a_iF(g)/(1−a_i g). With g'=F(g), differentiation gives y_i'=−y_i sum_{j≠i}y_j, and monotonicity plus F>0 up to its first root forces g to approach 1/a_*. Evaluating the polynomial y_i there gives precisely the unique-largest product and zero in every coordinate for ties. The key horizon comparison is deterministic: every subsequent edge consumes a distinct surviving vertex outside any selected largest part. Thus the change of that part, of the total and of every other part is bounded by twice the minority count at the fixed horizon. Taking N first and then the horizon to infinity proves the classwise terminal LLN even if the finite-N proportions break a limiting tie. Boundedness gives L1 convergence. The 8m,7m,5m example has matching counts 5m,3m,2m and limiting unmatched density 3/160. Direct recursion on labeled feasible edges gave exact finite terminal laws including P(U=2)=1/5 and P(U=0)=4/5 for K_{2,2,2} (python3 /tmp/opencode/frozen_math_reproduction.py); neither that calculation nor the supplied verifier's recorded simulation proves terminal asymptotics. The frozen verifier was inspected rather than run.

## originality

PASS

Credit the exact indexed q=3 coverage; the supported distinct result is the explicit all-fixed-q positive-density product in the stochastic terminal LLN, including q>=4, with the classwise and tie conclusions. Published mean-field work supplies related deterministic kinetics; the compared statements do not establish this arbitrary-q stochastic terminal claim.

## value

PASS

An all-fixed-q terminal formula separates unique-largest and tied-largest regimes and quantifies when irreversible deposition leaves a positive macroscopic vacancy even with a perfect matching available. Its product of all asymmetry factors and terminal-horizon control are useful for comparing heterogeneous complete substrates; the main contribution is the arbitrary-q law, not the already matched tripartite special case or a claim about spatial kinetics or fluctuations.

The dated certificate retains the supplied scientific assessment, sources and limitations.
