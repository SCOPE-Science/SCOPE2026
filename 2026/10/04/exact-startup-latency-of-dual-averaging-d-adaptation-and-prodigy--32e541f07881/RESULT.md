# Exact startup latency of dual-averaging D-Adaptation and Prodigy
## Finding

D-Adaptation and Prodigy are learning-rate-free methods that learn a lower estimate of the unknown distance from the starting point to a solution. Their published dual-averaging recurrences have a finite startup latency even under the cleanest possible subgradient signal.

Consider the one-dimensional convex objective
\[
f(x)=G|x-D|,
\qquad
G>0,
\qquad
D>0,
\]
with starting point
\[
x_0=0
\]
and initial distance estimate
\[
d_0>0.
\]
Assume
\[
D>d_0\sqrt8.
\]
Then all iterates used in the cutoff calculation remain strictly to the left of the minimizer, so their subgradient is the constant
\[
g_k=-G.
\]

For the published dual-averaging D-Adaptation algorithm, while the learned estimate has not yet moved from \(d_0\),
\[
s_n=-n d_0G,
\qquad
\gamma_n=\frac1{G\sqrt n},
\qquad
x_n=d_0\sqrt n
\]
for
\[
n\ge1.
\]
Its proposed distance update is exactly
\[
\frac{\widehat d_n}{d_0}
=
R_n
:=
\frac{
n^{3/2}
-
1
-
\displaystyle\sum_{i=1}^{n-1}i^{-1/2}
}{
2n
}.
\]
The first values relevant to adaptation are
\[
R_1=0,
\]
\[
R_2\approx0.2071067812,
\]
\[
R_3\approx0.4148409403,
\]
\[
R_4\approx0.5894428687,
\]
\[
R_5\approx0.7395882837,
\]
\[
R_6\approx0.8721056509,
\]
\[
R_7\approx0.9914528744,
\]
and
\[
R_8\approx1.1005958493.
\]
Therefore
\[
d_1=\cdots=d_7=d_0,
\]
while
\[
d_8=R_8d_0>d_0.
\]
The first strict increase occurs at the end of the eighth update.

For the published dual-averaging Prodigy algorithm, use its prescribed weights
\[
\lambda_k=d_k^2.
\]
While the learned estimate remains equal to \(d_0\),
\[
s_n=-n d_0^2G,
\]
and, before the first increase,
\[
x_n
=
\frac{n}{\sqrt{n+1}}d_0.
\]
The proposed distance estimate after \(n\) updates is
\[
\frac{\widehat d_n}{d_0}
=
P_n
:=
\frac1n
\sum_{i=1}^{n-1}
\frac{i}{\sqrt{i+1}}.
\]
The relevant values are
\[
P_1=0,
\]
\[
P_2\approx0.3535533906,
\]
\[
P_3\approx0.6206024399,
\]
\[
P_4\approx0.8404518299,
\]
and
\[
P_5\approx1.0301323403.
\]
Hence
\[
d_1=\cdots=d_4=d_0,
\]
while
\[
d_5=P_5d_0>d_0.
\]
Prodigy first increases the same distance estimate at the end of the fifth update.

Thus on the same convex Lipschitz objective, with a perfectly coherent constant subgradient, Prodigy's dual-averaging modification reduces the exact startup latency of the distance estimate from eight updates to five.

The comparison is about when the adaptive distance estimate first becomes informative beyond its initialization. It does not assert that either algorithm has a globally optimal transient on this objective.

## Assumptions and scope

The D-Adaptation recurrence is Algorithm 1, the dual-averaging form, from the defining D-Adaptation paper.

The Prodigy recurrence is Algorithm 2, the dual-averaging form, with the prescribed weights
\[
\lambda_k=d_k^2.
\]

The objective
\[
f(x)=G|x-D|
\]
is convex and \(G\)-Lipschitz. The assumption
\[
D>d_0\sqrt8
\]
ensures that every point needed to compute the D-Adaptation cutoff remains in the constant-subgradient region. It is stronger than what is needed for Prodigy's fifth-update cutoff, which makes the comparison use one common objective and one common initialization condition.

Only the first increase of the learned distance estimate is classified. Later dynamics change after the estimates begin to grow and are not covered by the closed forms here.

## Proof

For D-Adaptation, suppose inductively that
\[
d_0=d_1=\cdots=d_{n-1}.
\]
Because
\[
g_i=-G,
\]
the accumulated dual vector is
\[
s_n
=
\sum_{i=0}^{n-1}d_i g_i
=
-n d_0G.
\]
The published normalization gives
\[
\gamma_n
=
\frac1{
\sqrt{
\sum_{i=0}^{n-1}|g_i|^2
}
}
=
\frac1{G\sqrt n},
\]
so
\[
x_n
=
x_0-\gamma_ns_n
=
d_0\sqrt n.
\]

The D-Adaptation proposal after \(n\) updates is
\[
\widehat d_n
=
\frac{
\gamma_n|s_n|^2
-
\displaystyle\sum_{i=0}^{n-1}
\gamma_i d_i^2|g_i|^2
}{
2|s_n|
}.
\]
Here
\[
\gamma_0=\frac1G,
\]
and for
\[
i\ge1
\]
one has
\[
\gamma_i=\frac1{G\sqrt i}.
\]
Substitution yields
\[
\gamma_n|s_n|^2
=
n^{3/2}d_0^2G,
\]
and
\[
\sum_{i=0}^{n-1}
\gamma_i d_i^2|g_i|^2
=
d_0^2G
\left(
1+
\sum_{i=1}^{n-1}i^{-1/2}
\right).
\]
Dividing by
\[
2|s_n|=2nd_0G
\]
gives
\[
\frac{\widehat d_n}{d_0}
=
R_n.
\]

Exact rational enclosures of the square roots give
\[
R_n<1
\qquad
\text{for }
1\le n\le7,
\]
and
\[
R_8>1.
\]
The accompanying verification file constructs these enclosures using integer-square inequalities, so the sign comparisons do not rely on floating-point rounding. Since the algorithm sets
\[
d_n=\max(d_{n-1},\widehat d_n),
\]
the first strict increase is exactly
\[
n=8.
\]

Now consider Prodigy. Suppose
\[
d_0=d_1=\cdots=d_{n-1}.
\]
The prescribed weights are then
\[
\lambda_i=d_0^2
\]
through the data entering the \(n\)-th proposal, and
\[
s_n
=
\sum_{i=0}^{n-1}\lambda_i g_i
=
-n d_0^2G.
\]

Before the first increase, the Prodigy normalization for the already-computed iterate \(x_i\) is
\[
\gamma_i
=
\frac1{
Gd_0\sqrt{i+1}
},
\]
so for
\[
1\le i\le n-1
\]
one has
\[
x_i
=
-\gamma_i s_i
=
\frac{i}{\sqrt{i+1}}d_0.
\]

The Prodigy proposal after \(n\) updates is
\[
\widehat d_n
=
\frac{
\displaystyle\sum_{i=0}^{n-1}
\lambda_i
\langle g_i,x_0-x_i\rangle
}{
|s_n|
}.
\]
In one dimension,
\[
g_i=-G,
\qquad
x_0-x_i=-x_i,
\]
so
\[
\widehat d_n
=
\frac{
d_0^2G
\displaystyle\sum_{i=1}^{n-1}x_i
}{
nd_0^2G
}.
\]
Substituting the formula for \(x_i\) gives
\[
\frac{\widehat d_n}{d_0}
=
P_n.
\]

Exact rational square-root enclosures give
\[
P_n<1
\qquad
\text{for }
1\le n\le4,
\]
and
\[
P_5>1.
\]
Therefore the first strict increase in Prodigy is exactly
\[
n=5.
\]

The common condition
\[
D>d_0\sqrt8
\]
keeps all subgradients entering both cutoff calculations equal to
\[
-G,
\]
so the two startup latencies occur on the same objective rather than on different constructed sequences.

## Verification

The accompanying `verify.py` performs three independent checks.

First, it directly replays both published dual-averaging recurrences on a constant subgradient and checks every displayed closed form through the first increase.

Second, it uses exact rational arithmetic and integer-square bounds to certify
\[
R_1,\ldots,R_7<1<R_8
\]
and
\[
P_1,\ldots,P_4<1<P_5.
\]

Third, it evaluates both algorithms on
\[
f(x)=G|x-D|
\]
with
\[
D>d_0\sqrt8
\]
and checks that every subgradient required by the cutoff proof is indeed constant.

The finite verification certifies the few radical inequalities. The general formulas in \(n\) used up to each cutoff are proved algebraically above.

## Relationship to prior work

Defazio and Mishchenko introduced D-Adaptation to learn the unknown solution distance needed for the optimal learning-rate scale in convex Lipschitz optimization. Their dual-averaging algorithm maintains a nondecreasing lower estimate
\[
d_k
\]
and derives it from accumulated subgradients.

Mishchenko and Defazio introduced Prodigy specifically as a faster-adapting modification of D-Adaptation. Their paper changes the dual-averaging weights to
\[
\lambda_k=d_k^2
\]
and states that the resulting step sizes can be larger while preserving the relevant error control.

Those papers provide convergence bounds and qualitative motivation for faster adaptation. The inspected algorithms and analyses do not state the exact constant-subgradient startup cutoffs
\[
8
\]
and
\[
5
\]
derived here.

Focused published-record searches for D-Adaptation and Prodigy startup latency, constant-subgradient dynamics, first distance-estimate growth, and exact finite cutoffs did not identify an implication-equivalent result.

## Limitations

The calculation is for the dual-averaging variants, not their SGD or Adam implementations.

The objective is one-dimensional and has a constant subgradient throughout the startup interval.

Only the first strict increase of
\[
d_k
\]
is classified. The post-activation trajectories are not compared.

The three-update latency reduction is a finite-time structural fact, not by itself a theorem that Prodigy is faster on every objective or metric.

## References

1. Aaron Defazio and Konstantin Mishchenko, “Learning-Rate-Free Learning by D-Adaptation,” arXiv:2301.07733v1, 2023.
2. Konstantin Mishchenko and Aaron Defazio, “Prodigy: An Expeditiously Adaptive Parameter-Free Learner,” arXiv:2306.06101v1, 2023.
