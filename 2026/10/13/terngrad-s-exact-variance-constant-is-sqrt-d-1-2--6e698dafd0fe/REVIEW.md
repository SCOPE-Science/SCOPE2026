# Review

## Correctness

PASS. Source-form TernGrad gives the exact moment identity
\[
\mathbb E\|Q(g)\|_2^2=\|g\|_\infty\|g\|_1.
\]
A sharp Cauchy--Schwarz reduction proves that
\[
\sup_{g\ne0}
\frac{\|g\|_\infty\|g\|_1}{\|g\|_2^2}
=
\frac{\sqrt d+1}{2},
\]
with a complete equality family. This yields the minimal variance parameter and the exact isotropic-quadratic one-step factor. Direct finite-distribution replay agrees with every displayed formula.

Scientific risk: the optimization consequence is deliberately limited to one deterministic isotropic quadratic step.

## Originality

PASS. The defining TernGrad paper exposes the mixed norm quantity but does not optimize it. A later compression-theory table assigns ternary quantization the sufficient parameter
\[
\sqrt d-1,
\]
while the accepted result proves the minimal value
\[
\frac{\sqrt d-1}{2}.
\]
Focused comparisons found no implication-equivalent sharp constant, equality classification, or exact TernGrad quadratic stepsize frontier.

Residual risk: an unindexed mathematical note may contain the same sharp norm inequality outside the compression literature.

## Value

PASS. Compressor variance is a central parameter in convergence guarantees for compressed optimization. The factor-two sharpening is exact in every nontrivial dimension, identifies the worst gradient shape, and yields a natural complete stepsize classification on the isotropic quadratic.

Self-review: passed. Independent audit: not yet performed.
