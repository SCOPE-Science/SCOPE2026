# Independent audit — 2026-09-30 UTC

Record: `2026/09/20/pure-n-way-dependence-student-t-size-iid-gaussian-marginals--06f336863f9d`  
Assigned source tree: `c354052402b69a80b3f29fe1747592b6e4695ebb`  
Audited current source tree: `c354052402b69a80b3f29fe1747592b6e4695ebb`  
Audited repository state: `SCOPE-Science/SCOPE2026` `eff2c6312cec5b0dee5115e5f42211a853092dfb`  
Current RESULT.md blob: `6d123fed0f8fc1b964f337d005971c8373227d3a`  
Disposition: **passed**

## Correctness

**independently_supported**. The finite-sample theorem is correct. The density is nonnegative for |theta|<=1, integrates to one, and integrating out any coordinate annihilates the sole highest-order sign interaction, so every proper subvector is exactly iid standard normal. If a deterministic sample has positive mean and at least one nonpositive coordinate, minimizing the residual sum of squares at fixed mean gives Q>=n m^2/(n-1), hence T_n<=n-1; the bound is sharp by perturbing the equality configuration. Therefore for c>=n-1 the upper tail lies entirely in the positive orthant, where f_theta/f_0=1+theta, while the lower tail lies in the negative orthant, where the ratio is 1+(-1)^n theta. This gives the stated exact one-sided and even-n two-sided rescalings. For n=4, 2P(t_3>3)=1/3-sqrt(3)/(2pi)>0.05, so the ordinary 5% critical value lies in the exact regime and the rejection probability is 0.05(1+theta), ranging from zero to ten percent.

## Originality

**qualified_supported_exact_studentization_effect**. The highest-order product interaction is a standard Sarmanov-type construction and limited-independence parity phenomena are established prior art. Student's classical iid-normal law and older examples where incomplete independence alters testing error are also prior. Searches combining Student t/studentized mean, (n-1)-wise independence, Gaussian marginals, Sarmanov and higher-order interaction did not locate the exact threshold n-1, the tail multipliers, or the four-observation 5%-to-10% example. Novelty is therefore supported for this explicit Student-statistic calculation, with residual risk from older Sarmanov/copula/robustness literature under different terminology.

## Scientific value

**meaningful_exact_finite_sample_counterexample**. The example is strikingly strong in its marginal agreement: with n=4 every triple is exactly an iid Gaussian sample, yet the canonical t-test can have any exact size from 0% to 10% at nominal 5%. The short deterministic threshold explains the mechanism and gives a clean benchmark for how much full joint independence matters to exact studentization.

## Independent checks

- Integrated the interaction density over omitted coordinates to verify exact proper-subvector independence.
- Solved the fixed-mean residual-sum-of-squares minimization and checked sharpness of the n-1 threshold.
- Recomputed the t_3 tail at 3 and verified that the standard 5% two-sided critical value lies above the threshold.

## Literature and evidence checked

- https://github.com/SCOPE-Science/SCOPE2026/tree/e9ed144c13b7834896a844cc4f9cac3c25a168a6/2026/09/20/pure-n-way-dependence-student-t-size-iid-gaussian-marginals--06f336863f9d
- https://doi.org/10.1093/biomet/6.1.1
- https://doi.org/10.1080/03610929608831759
- https://doi.org/10.4153/CMB-1975-073-5
- https://doi.org/10.1016/j.orl.2023.01.004
- https://arxiv.org/abs/2211.01596
## Limitations

- No global extremum is proved over all (n-1)-wise independent Gaussian-marginal laws.
- For odd n this particular sign interaction cancels between the two high-threshold tails in a two-sided test.
- The result concerns exact finite-sample calibration, not asymptotics under general dependent sequences.
- Equivalent older formulations under Sarmanov, copula or exact-robustness terminology remain a residual originality risk.
