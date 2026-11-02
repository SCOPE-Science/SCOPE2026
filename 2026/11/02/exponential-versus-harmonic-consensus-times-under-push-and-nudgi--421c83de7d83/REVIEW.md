# Self-review

## Correctness — PASS

The claim is a count-chain theorem with explicit probability normalization, fixed parameter domain, and all nonconsensus initial states. Direct calculation yields both up/down probabilities. The scalar first-step recurrence proves the finite push expectation; monotone birth/death ratios and a Riemann-sum sandwich prove its *uniform* exponential rate, including starting states with only one dissenter. The harmonic potential argument and the required-selection coupon bound prove both nudging inequalities without asymptotic approximations. The standalone checker matches separate exact-rational linear-system calculations for 352 configurations of population size and parameters, direct agent-level transition calculations for 2952 configurations, 1232 harmonic inequalities, and numeric rate trends. No finite enumeration is treated as proof of the all-size result.

## Originality — PASS (qualified)

A full accessible version of the initiating 2024 paper [1] was inspected, especially its exact update equations and simulation-based sections; it does not give an exact complete-graph absorbing-time formula or the paired exponential-versus-harmonic bound. The 2015 jump-voter work [2] changes multiple voters through an independent jump mechanism. The 2019 news-source model [3] and 2021 two-class majority-rule paper [4] contain relevant consensus-time phenomena but with distinct transition kernels; the latter demonstrates exponential escape in another model. Earlier generic birth-death asymptotic tools [6] are credited explicitly. The precise logarithmic barrier and comparative harmonic bounds for [1] were not located in the accessible record or indexed findings. Residual risk: a specialist reduction or treatment of the exact rates might exist despite the searches; absence in the searched corpus is not proof of global priority.

## Mathematical value — PASS

The two media strategies have superficially similar one-agent transitions and both absorb almost surely at the same final consensus, but they differ exponentially in expected convergence time. The positive action integral and all-initial-state uniformity quantify why apparent finite-time mixed plateaus can persist even with a unique absorbing state. The matching-order finite nudging bounds are a direct quantitative benchmark for media-strategy design. This is more than re-expression of a standard hitting-time formula because it isolates a sharp, model-specific dynamical contrast and gives its explicit rate.

## Scope and residual risks

The classification is complete only for undirected complete networks, fixed positive parameters, and mean hitting times. It does not claim full distributional asymptotics or extension to sparse graphs. Prior work in generic birth-death theory supplies broadly applicable methods and might inspire equivalent derivations; specialized priority uncertainty remains. The calculations do not amount to external validation.

Self-review: passed. Independent audit: not yet performed.
