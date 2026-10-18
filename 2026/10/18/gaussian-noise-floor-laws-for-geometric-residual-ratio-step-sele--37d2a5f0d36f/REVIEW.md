# Scientific review

## Correctness
PASS. For every allowed residual dimension and window, Gaussian small-ball asymptotics and independent endpoint measurements prove the exact positive-moment boundary and polynomial tail; a beta-ratio identity gives the limiting distribution. Reciprocal symmetry gives the sharp half-probability of unit-curvature overshoot, and Borel–Cantelli gives the full-history critical-step limit. The verification script passed 852 seeded/algebraic checks; these are not exhaustive proofs.

## Originality
PASS, with bibliographic uncertainty. The underlying empirical residual ratio and adaptive update originate in Hu et al. [1]. Chi-square ratios and beta distributions are classical. The assessed new contribution is their complete joint consequence under noisy *measurement* of the source statistic, including noncentral finite-step tails, the \(dw\) moment threshold, exact one-step mean-square implication, and fixed/full-window split. The primary 2026 original text and related stochastic heavy-tail literature were compared by their assumptions and implications. Prior specialized noise-ratio calculations may exist.

## Value
PASS. A natural sampling/telemetry problem is resolved at a sharp dimension-window boundary. The result demonstrates that light-tailed sensor error can produce undefined second moments for a parameter feedback, and that enlarging a fixed window does not make the limiting unit-curvature step mean-square safe. The full-history contrast gives a meaningful design diagnostic.

## Limits and closest literature
The statement concerns independent Gaussian observation noise and an exogenous vanishing deterministic residual sequence, not a full noise-driven optimizer trajectory. [1] supplies the original adaptive rule with exact residuals. [2] studies general heavy-tailed gradient noise, which differs from residual telemetry. Central F/beta laws remain classical and are not claimed as new.

[1] Hu, Pollock, Xue, Zhu, *An adaptive framework for first-order gradient methods*, arXiv:2602.13620v1 (2026), https://arxiv.org/html/2602.13620v1.

[2] Wang et al., *Convergence Rates of Stochastic Gradient Descent under Infinite Noise Variance*, arXiv:2102.10346 (2021).

Self-review: passed. Independent audit: not yet performed.
