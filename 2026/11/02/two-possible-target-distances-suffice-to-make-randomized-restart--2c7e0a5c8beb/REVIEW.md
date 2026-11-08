# Independent mathematical audit

## correctness

PASS

For generator ∂xx, conditional first-hitting survival S_R(t)=erf[R/(2sqrt t)], F_R=1−S_R, A_R=∫_0^t S_R(s)ds. A target distance is sampled ONCE for the full search; conditional renewal gives M_R(ψ)=E A_R(Z)/E F_R(Z), then weighted sum of conditional ratios, not ratio of averages. For ψ=(43/50)δ(2/5)+(7/50)δ10 and P(R=1)=19/20, P(R=5)=1/20, independent high-precision evaluation gives 4.1947990668979<21/5. For all deterministic t, analytical short-time inequalities imply lower bound 4.267532 on t≤2.9; monotonic A_R,F_R enclose every middle t∈[2.9,20] by 35 exhaustive intervals with minimum certified lower bound 4.3631715; t≥20 lower bound 4.3389016. The actual source exact-rational program supplies explicit enclosures for pi, square roots, exponentials, error functions and every middle bound. For all Poisson rates u=√r>0, positive exponential-series truncation produces cubic 161u³+144u²−378u+144>0, verified by rational Bernstein coefficients in 3 covering intervals and positive increasing tail u≥1. For one fixed R, M_R(ψ) is an F_R-weighted average of deterministic M_R(t), so no strict improvement over all fixed clocks. Thus continuum inequalities are analytically and certified-finitely covered; not inferred from numerical sampling.

## originality

PASS

Best-of-knowledge distinct claim after comparison with directly relevant primary sources and published mathematical findings. Prior special cases and baseline formulas are explicitly credited. Complete historical originality is not certified.

## value

PASS

The quenched versus annealed distinction matters in optimal restart under hidden heterogeneous targets. Existing broad-tail advantages do not answer how few fixed target locations can defeat sharp restart. An explicit binary-support strict certificate and rigorous minimality theorem are meaningful structural optimization boundaries, independent of finding globally best randomized clock.

The dated certificate retains the supplied scientific assessment, sources and limitations.
