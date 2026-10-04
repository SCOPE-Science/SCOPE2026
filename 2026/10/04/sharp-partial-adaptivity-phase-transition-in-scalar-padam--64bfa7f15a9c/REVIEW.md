# Review

## Correctness

PASS. The specialized Padam recurrence reduces exactly to
\[
x_{t+1}=x_t(1-q_t),
\qquad
q_t=\frac{\alpha\lambda^{1-2p}}{M_t^{2p}}.
\]
While \(q_t>2\), each step creates a new historical maximum and
\[
q_{t+1}=\frac{q_t}{(q_t-1)^{2p}}.
\]
For \(p\le1/4\), the inequality
\[
q/(q-1)^{2p}>2
\]
holds for every \(q>2\), so the overshoot region is invariant and the decreasing sequence converges to the unique fixed point \(2\). For \(p>1/4\), the derivative at that fixed point is \(1-4p<0\), forcing a finite crossing below or onto \(2\). Once \(q_t\le2\), the historical maximum freezes and the dynamics are exactly linear.

Risk: the theorem is for a boundary specialization, not the default smoothed and momentum Padam hyperparameters.

## Originality

PASS. The defining Padam paper introduces the historical maximum and the exponent \(p\), but the inspected full text does not state a deterministic scalar two-cycle or a max-memory phase transition. The follow-up analysis highlights \(p\le1/4\) for a sparse-gradient convergence bound with horizon-dependent learning rates, but does not imply the constant-step scalar dichotomy. Focused searches for Padam quadratic cycles, partial-adaptivity limit cycles, and exact \(p=1/4\) dynamics did not identify a covering result.

Residual risk: an equivalent scalar observation may appear in informal optimizer analyses that are not indexed under Padam.

## Value

PASS. Padam's central design parameter is precisely the exponent that interpolates between nonadaptive momentum and full AMSGrad normalization. The theorem shows that this exponent can qualitatively change deterministic dynamics even on a scalar quadratic: below the sharp threshold, the historical max locks the method onto a nonzero limiting oscillation from small initial conditions, whereas above it the same max memory forces finite self-stabilization. The threshold also coincides numerically with a range emphasized in Padam's convergence literature, making the boundary especially informative as a diagnostic.

Same-model review: passed. Independent audit: not yet performed.
