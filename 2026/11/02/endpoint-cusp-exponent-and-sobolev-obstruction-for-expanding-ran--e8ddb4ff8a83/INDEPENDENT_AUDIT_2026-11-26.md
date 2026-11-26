# Independent mathematical audit

## correctness

PASS

Each branch is onto, with inverse Lipschitz bound rho_j = [2 alpha + (1-alpha) theta_j]^{-1}<1. An interior jump of a BV input enters at most one branch image per map (the turning-point jump maps to the boundary); continuous branch weights and the triangle inequality contract the sum of absolute interior jumps by at most sum pi_j rho_j < 1. Stationarity a.e. therefore yields a continuous representative and a pointwise equation in the interior. A zero propagates to every inverse image of any one active map. Its full-branch cylinders cover the interval with diameters tending uniformly to zero, so a zero contradicts normalization. Inverting z=theta_j t+A_j t^alpha gives t~(z/A_j)^{1/alpha} and weight ~A_j^{-1/alpha}z^gamma/alpha. The positive common limiting branch value h(c) gives the stated coefficient; integrating divides it by 1+gamma, and the positive limit gives the one-sided exponent. At finite p>=1/(1-gamma), an absolutely continuous representative with trace zero actually satisfies |h(1-z)|=o(z^{1-1/p}) by the vanishing local L^p norm of h', so equality at the threshold is excluded too. W^{1,infty} and W^{2,1} imply Lipschitz regularity here. This is conditional on a stationary BV density and proves no subthreshold membership. Independent replay: python3 /workspace/branches/audit_kernel_checks.py checked the trial-input kernel on a different mixture, not a stationary density; the continuity, positivity and obstruction are analytic. The frozen check.py's nominal assertion count is a bookkeeping convention, not a measure of coverage.

## originality

PASS

The deterministic endpoint law and loss of W^{2,1} are directly covered by a distinct indexed record; no independent novelty or priority is credited for that specialization. The credited difference is the finite weak-cusp Bernoulli law for the actual common stationary density (including its positive weighted coefficient), with the first-derivative Sobolev exclusion including the borderline. The deterministic statement does not imply this genuinely mixed law, and the critical mixture result has a different exponent and regularity. Decision is best-of-knowledge, not a priority determination.

## value

PASS

The positive asymptotic for actual mixed stationary densities rules out transferring the strong/critical W^{2,1} approach intact to the weak-cusp side. The critical-inclusive W^{1,p} exclusion and endpoint mass coefficient are usable quantitative constraints rather than a regularity observation about an arbitrary trial input. No value is attributed to a new deterministic priority claim or to a sharp two-sided Sobolev classification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
