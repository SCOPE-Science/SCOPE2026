# Scientific review: fixed-mean renewal probing frontier

## Correctness

**PASS.** The proof begins with the exact two-level unitary and rank-one post-failure projection. It derives the renewal mean-time identity for every i.i.d. waiting law of positive finite mean, including atoms at zero. It proves the unique tangency \(\tan x_*=2x_*\) and constructs the global concave majorant of \(\sin^2x\), proving the inequality for all nonnegative integrable waiting times (not merely a finite discretization). Equality is checked separately on all three ranges, including the full set of high-mean optimizers and the nonattainment qualification for strictly positive low-mean intervals. Reproducible independent matrix and finite-grid computations corroborate the analytic argument.

## Originality

**PASS, conditional on the checked literature, without a claim of priority certification.** The original renewal mean formula (Kulkarni–Majumdar, Eq. 135) and the general random-probing identity (Kessler–Barkai–Ziegler) are prior work, not claimed as new. Belan–Parfenyev and the publicly available fully connected model theorem already give an *unconstrained* global optimum (and thus cover the first, constant-time segment of this result). The new claim is the full **fixed exact mean** frontier, including the two sharp mean-budget boundaries, the intermediate unique deterministic protocol, the nonunique high-budget resonant mixtures, and every optimizer. The closest full published findings were compared by implication, not title. A generic concavification framework or an overlooked older control theorem might subsume this specialization; this is residual priority risk, not evidence of established coverage.

## Mathematical value

**PASS.** The prescribed average probing interval is a physically meaningful interrogation-budget constraint. The complete frontier has two nontrivial changes in optimal protocol structure, distinguishing low-mean randomized timing from an intermediate deterministic optimum and high-mean resonant randomization. In particular, perfectly periodic interrogation at a coherent zero can fail forever despite a finite attainable optimum at the same exact average frequency. The all-mean boundary, exact attaining families and strict-positivity caveat together constitute a natural constrained-optimal-control classification, rather than a small numerical improvement.

## Scope and remaining risks

The detector is a closed coherent two-state transition and every failure resets to the initial ray; no generalization to multi-state quantum walks, nonrenewal or adaptive schedules is proved. The optimizer in the short-mean range uses zero inter-test intervals, replaced by an infimizing sequence when strictly positive times are mandatory. External publication priority has not been independently established, and broad abstract renewal-control literature may contain equivalent concave-envelope arguments.

Self-review: passed. Independent audit: not yet performed.
