# Review

## Correctness

PASS. On the support-aligned lattice, uniform additive noise makes the signSGD downward probability exactly \(k/M\) at state \(k\), and the upward probability exactly \((M-k)/M\). This is the \(M\)-ball Ehrenfest chain. Binomial detailed balance proves the unique invariant law. The period-two structure follows because every update changes the lattice index by one. Exact conditional moment identities give the transient second moment and the stationary loss \(\delta B/4\).

Risk: distributional convergence without parity conditioning is false; the finding explicitly retains that period-two obstruction.

## Originality

PASS. The defining signSGD paper gives the constant-sign update, bounded-variance oracle assumptions, symmetric-unimodal noise discussion, and a noisy quadratic experiment, but no additive-noise stationary law. The 2020 geometric analysis treats deterministic sign methods and norm geometry rather than stochastic invariant measures. A highly relevant 2026 paper solves an exact signSGD stationary law under pure multiplicative noise and explicitly identifies its period-two lattice structure; its additive-noise proposition instead solves the stationary second moment of ordinary SGD. The inspected source therefore does not cover the finite binomial Ehrenfest law, support-width phase parameter, or exact linear-in-step signSGD additive floor proved here.

Residual risk: the same birth-death identification may have appeared under classical Markov-chain terminology without signSGD naming.

## Value

PASS. Constant-magnitude sign updates are known to create a granularity floor, and recent work distinguishes multiplicative from additive noise as qualitatively different scheduling regimes. The exact Ehrenfest reduction resolves the additive side on a canonical bounded symmetric noise model: it gives the full invariant law, a closed noise floor \(\delta B/4\), the exceptional \(M=2\) last-iterate oscillation, and a direct contrast with the quadratic-in-step floor of pure multiplicative noise. This is a structural benchmark rather than a generic recomputation of a Markov chain.

Same-model review: passed. Independent audit: not yet performed.
