# NosAdam-HH has a sharp outlier-forgetting transition at \(\gamma=1\)
## Finding

NosAdam replaces Adam's exponentially weighted second moment by a weighted average that deliberately gives older gradients more influence. Its hyperharmonic specialization uses
\[
b_k=k^{-\gamma},
\qquad
B_t=\sum_{k=1}^t k^{-\gamma},
\qquad
\gamma\ge0.
\]

This choice has a sharp memory transition that is not visible from the monotonicity statement alone.

Consider one coordinate and constants
\[
H>G>0.
\]
Let every squared gradient equal
\[
G^2
\]
except at one time
\[
\tau\ge1,
\]
where it equals
\[
H^2.
\]
The source weighted-average identity gives, for every
\[
t\ge\tau,
\]
\[
\boxed{
v_t
=
G^2+
(H^2-G^2)\frac{\tau^{-\gamma}}{B_t}.
}
\]

Define the outlier imprint
\[
\Delta_t=v_t-G^2.
\]
Then the exact imprint weight is
\[
\boxed{
\frac{\Delta_t}{H^2-G^2}
=
\frac{\tau^{-\gamma}}{B_t}.
}
\]

The asymptotic behavior changes sharply at
\[
\gamma=1.
\]

If
\[
0\le\gamma<1,
\]
then
\[
B_t\sim\frac{t^{1-\gamma}}{1-\gamma}
\]
and therefore
\[
\boxed{
t^{1-\gamma}\Delta_t
\longrightarrow
(1-\gamma)(H^2-G^2)\tau^{-\gamma}.
}
\]

If
\[
\gamma=1,
\]
then
\[
B_t\sim\log t
\]
and
\[
\boxed{
(\log t)\Delta_t
\longrightarrow
\frac{H^2-G^2}{\tau}.
}
\]

If
\[
\gamma>1,
\]
then
\[
B_t\longrightarrow\zeta(\gamma)
\]
and hence
\[
\boxed{
\Delta_t
\longrightarrow
(H^2-G^2)\frac{\tau^{-\gamma}}{\zeta(\gamma)}
>0.
}
\]

Thus the second-moment state fully forgets every fixed finite outlier exactly in the non-summable regimes
\[
\gamma\le1.
\]
For summable hyperharmonic weights
\[
\gamma>1,
\]
a fixed early outlier retains a permanent share of the adaptive denominator.

The all-baseline sequence has
\[
v_t^{\rm base}=G^2.
\]
Therefore the exact denominator-induced rescaling relative to that baseline is
\[
\boxed{
R_t
=
\frac{G}{\sqrt{v_t}}
=
\left[
1+
\left(\frac{H^2}{G^2}-1\right)
\frac{\tau^{-\gamma}}{B_t}
\right]^{-1/2}.
}
\]
It tends to one when
\[
\gamma\le1,
\]
whereas for
\[
\gamma>1
\]
it tends to the strict limit
\[
\boxed{
R_\infty
=
\left[
1+
\left(\frac{H^2}{G^2}-1\right)
\frac{\tau^{-\gamma}}{\zeta(\gamma)}
\right]^{-1/2}
<1.
}
\]

For the source comparison value
\[
\gamma=0.1,
\]
the outlier's normalized second-moment weight satisfies
\[
\boxed{
\frac{\tau^{-0.1}}{B_t}
\sim
0.9\,\tau^{-0.1}t^{-0.9}.
}
\]
So NosAdam does recover fully from a finite isolated spike at that setting, but only with a polynomial memory tail rather than Adam's exponential tail.

## Assumptions and scope

The theorem concerns the source NosAdam-HH second-moment recurrence in one coordinate.

The gradient sequence is externally prescribed. It isolates the adaptive-denominator memory of one exceptional squared gradient and does not claim that the sequence arises from a fixed deterministic objective.

The statement concerns the second-moment state and its denominator-induced rescaling. First-moment momentum can carry a separate transient after an outlier.

The phase transition uses the source hyperharmonic family
\[
b_k=k^{-\gamma}
\]
over the full displayed parameter range
\[
\gamma\ge0.
\]
No convergence claim for the full optimizer is inferred from the \(\gamma>1\) denominator calculation.

## Proof

The defining NosAdam identity is
\[
v_t
=
\frac1{B_t}
\sum_{k=1}^t b_k g_k^2.
\]
For NosAdam-HH,
\[
b_k=k^{-\gamma}.
\]

Under the stated sequence,
\[
g_k^2=G^2
\]
for all
\[
k\ne\tau,
\]
and
\[
g_\tau^2=H^2.
\]
Hence
\[
\sum_{k=1}^t k^{-\gamma}g_k^2
=
G^2B_t+(H^2-G^2)\tau^{-\gamma},
\]
which proves the exact finite-time formula.

For
\[
0\le\gamma<1,
\]
integral comparison for the decreasing function
\[
x^{-\gamma}
\]
gives
\[
B_t\sim\frac{t^{1-\gamma}}{1-\gamma}.
\]
For
\[
\gamma=1,
\]
the harmonic-number asymptotic gives
\[
B_t\sim\log t.
\]
For
\[
\gamma>1,
\]
the defining positive series converges to
\[
\zeta(\gamma).
\]
Substitution gives all three limits.

The rescaling identity is immediate from comparing
\[
1/\sqrt{v_t}
\]
with the all-baseline value
\[
1/G.
\]

## Verification

The accompanying `verify.py` reconstructs the source weighted-average recurrence directly.

It checks the exact finite-time single-outlier formula over several values of \(\gamma\), verifies the three asymptotic regimes numerically, checks the source comparison exponent \(\gamma=0.1\), and confirms the limiting denominator-rescaling behavior on both sides of the transition.

The finite computations are transcription guards. The phase transition itself follows from the standard asymptotics of the hyperharmonic partial sums proved above.

## Relationship to prior work

Huang, Wang, and Dong introduce NosAdam to give past squared gradients more weight than recent ones. Their Algorithm 1 implies
\[
v_t
=
\frac{\sum_{k=1}^t b_k g_k^2}{B_t},
\]
and their hyperharmonic specialization chooses
\[
b_k=k^{-\gamma}.
\]
They emphasize that NosAdam can both increase and decrease its second-moment state, contrasting this with AMSGrad's running maximum, and illustrate recovery after a very large gradient.

Those statements motivate the present question. The inspected full text does not state how fast a single large gradient is forgotten, does not identify the summability transition at
\[
\gamma=1,
\]
and does not state that a finite outlier leaves a permanent denominator bias when
\[
\gamma>1.
\]

The source also compares NosAdam-HH with Adam at
\[
\gamma=0.1.
\]
The exact law here shows that this setting has a polynomial outlier-memory tail of order
\[
t^{-0.9},
\]
rather than exponential forgetting.

Focused published-record searches for NosAdam, hyperharmonic outlier forgetting, permanent second-moment memory, and equivalent phase-transition formulations did not identify an implication-equivalent result.

## Limitations

The theorem isolates one exceptional squared gradient against a constant-magnitude background.

It describes the adaptive second-moment denominator, not the full parameter trajectory.

The permanent-memory regime
\[
\gamma>1
\]
does not by itself imply divergence or poor optimization performance.

The exact source comparison with Adam is qualitative here: Adam's exponential weighting forgets a fixed isolated perturbation exponentially, whereas the theorem classifies NosAdam-HH's polynomial, logarithmic, or permanent memory.

## References

1. Haiwen Huang, Chang Wang, and Bin Dong, “Nostalgic Adam: Weighting more of the past gradients when designing the adaptive learning rate,” arXiv:1805.07557v1, first submitted 2018-05-19.
2. Haiwen Huang, Chang Wang, and Bin Dong, “Nostalgic Adam: Weighting More of the Past Gradients When Designing the Adaptive Learning Rate,” IJCAI 2019, DOI `10.24963/ijcai.2019/355`.
