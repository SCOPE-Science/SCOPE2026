# Independent mathematical audit

## correctness

PASS

With B_i=1−C_i/4, the first stage is B_1x_n and the macro-step multiplier is M=2B_1B_2−1. Put b=E B=1−μ/4 and d=E B²=b²+v/16. Independence within a macro-step gives E M=2b²−1 and Q−1=4(d²−b²)=4(d−b)(d+b), giving both factors with the denominator 64. Independence across macro-steps gives geometric first and second moments for deterministic initial data. When μ<4 the second factor is positive and the sign changes at v=μ(4−μ); when μ>4 the first is positive and the sign changes at v=(μ−4)(8−μ). At μ=4 both factors equal v, including the v=0 neutral case. These thresholds lie within the feasible range 0≤v<μ(8−μ) imposed by the open support. For shared draws the multiplier is 2B²−1, strictly inside (−1,1) except at C=4. The stated no-atom condition is sufficient (indeed any positive mass away from 4 suffices). The 1,6 example gives ordered multipliers 1/8, −7/4, −7/4, −1/2, hence the displayed first and second moments and shared second moment. Their absolute product is 49/256. Its fourth root is √7/4 and the strong law for the log-magnitudes proves almost-sure decay despite strictly growing second moment. The zero initial condition is identically zero and is not an instability example.

## originality

PASS

The published SRKCD method uses one sample for every stage of a macro-step. Its stability and earlier shared-sample results on moment explosion with typical-path decay are not claimed here as new. The closest randomized two-stage ODE work also uses scalar multiplier stability, but its independent random variables perturb stage time rather than draw separate client curvatures in this Chebyshev recurrence. No inspected source supplies the mean–variance boundary for the fresh-client recurrence or the same-versus-fresh contrast for identical marginals. The best-of-knowledge pass is for this explicit change of sampling and its sharp law, not the general expected-square or log-growth criteria.

## value

PASS

A plausible implementation change leaves all deterministic per-client scalar tests intact but can reverse mean-square behavior, even when the mean and typical paths decay. The exact distribution-free first-two-moments criterion and the explicit same-law comparison isolate sampling across stages as the cause. This is a motivated warning about what can be inferred from deterministic stability or average trajectories, not a failure claim about published shared-batch SRKCD.

The dated certificate retains the supplied scientific assessment, sources and limitations.
