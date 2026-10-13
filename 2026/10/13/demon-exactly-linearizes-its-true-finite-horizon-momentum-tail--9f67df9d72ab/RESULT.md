# DEMON exactly linearizes its true finite-horizon momentum tail
## Finding

Consider the DEMON momentum schedule with an integer horizon
\[
T\ge1
\]
and initial momentum
\[
0<b<1.
\]
The source schedule can be written exactly as
\[
\beta_t
=
\frac{b(T-t)}{T-bt},
\qquad
0\le t\le T.
\]

For the source SGDM recursion, a component already present in the momentum state \(v_t\) contributes to later parameter increments with products of the subsequent momentum coefficients. Define its true finite-horizon tail multiplier by
\[
E_T=0
\]
and, for \(0\le t<T\),
\[
E_t
=
\sum_{k=t}^{T-1}
\prod_{j=t}^{k}\beta_j.
\]

Then the entire product sum collapses to the exact linear law
\[
\boxed{
E_t
=
\frac{b(T-t)}{T(1-b)+b}.
}
\]

The source motivation instead freezes the momentum parameter at its current value and uses the geometric-series proxy
\[
P_t
=
\frac{\beta_t}{1-\beta_t}.
\]
For the DEMON schedule,
\[
P_t
=
\frac{b(T-t)}{T(1-b)}.
\]
Therefore
\[
\boxed{
E_t
=
\gamma_T P_t,
\qquad
\gamma_T
=
\frac{T(1-b)}{T(1-b)+b}.
}
\]
The factor \(\gamma_T\) is independent of \(t\).

Thus replacing the true varying-product tail by the frozen geometric series does **not** distort the shape of the intended decay. Both are exactly linear in the remaining horizon. The approximation changes only one global normalization.

The exact relative overestimate of the source proxy is
\[
\boxed{
\frac{P_t-E_t}{P_t}
=
\frac{b}{T(1-b)+b},
}
\]
uniformly over every \(0\le t<T\).

For example, at the common initial momentum
\[
b=0.9,
\]
the relative proxy error is about \(8.26\%\) when \(T=100\), about \(0.892\%\) when \(T=1000\), and about \(0.0899\%\) when \(T=10000\).

There is a one-step indexing distinction for a newly computed gradient. In Algorithm 1, \(g_t\) enters the new momentum state after the update at time \(t\). Its **future momentum-only** contribution, beyond its immediate parameter update, is therefore governed by
\[
E_{t+1}
=
\boxed{
\frac{b(T-t-1)}{T(1-b)+b}
},
\qquad
0\le t<T.
\]
This quantity also decays exactly linearly and vanishes for the penultimate gradient, because the source sets \(\beta_T=0\).

The source paper describes its varying-product replacement as a close approximation because momentum changes slowly relative to the decay of products. The identity above strengthens that interpretation: for the actual DEMON schedule, the true finite-horizon tail has exactly the intended linear profile.

## Assumptions and scope

The result concerns the DEMON schedule in the source SGDM algorithm.

The horizon \(T\) is a positive integer and the initial momentum satisfies
\[
0<b<1.
\]

The calculation is purely about linear momentum memory. It does not require any assumption on the loss, gradient sequence, stochasticity, convexity, or dimension.

The tail multiplier \(E_t\) measures the future parameter-update weight of a unit component already present in \(v_t\). For a newly computed gradient \(g_t\), the future momentum-only tail begins at \(t+1\), so its coefficient is \(E_{t+1}\).

The result does not assert that DEMON is optimal among momentum schedules, nor does it alter the source empirical comparisons or convergence theorem.

## Proof

Write
\[
C=T(1-b)+b.
\]
Because
\[
\beta_T=0,
\]
we have
\[
E_T=0.
\]

The product sum satisfies the exact backward recursion
\[
E_t
=
\beta_t\left(1+E_{t+1}\right).
\]
Indeed, the first future contribution is \(\beta_t\), and every later product contains \(\beta_t\) times the corresponding tail beginning at \(t+1\).

Assume
\[
E_{t+1}
=
\frac{b(T-t-1)}{C}.
\]
Then
\[
1+E_{t+1}
=
\frac{C+b(T-t-1)}{C}
=
\frac{T-bt}{C}.
\]
Using
\[
\beta_t
=
\frac{b(T-t)}{T-bt},
\]
we obtain
\[
E_t
=
\frac{b(T-t)}{T-bt}
\frac{T-bt}{C}
=
\frac{b(T-t)}{C}.
\]
Backward induction proves the formula for every \(0\le t\le T\).

For the frozen geometric proxy,
\[
1-\beta_t
=
1-
\frac{b(T-t)}{T-bt}
=
\frac{T(1-b)}{T-bt}.
\]
Hence
\[
P_t
=
\frac{\beta_t}{1-\beta_t}
=
\frac{b(T-t)}{T(1-b)}.
\]
Dividing the exact tail by this proxy gives
\[
\frac{E_t}{P_t}
=
\frac{T(1-b)}{T(1-b)+b}
=
\gamma_T,
\]
which is independent of \(t\). Therefore
\[
\frac{P_t-E_t}{P_t}
=
1-\gamma_T
=
\frac{b}{T(1-b)+b}.
\]

Finally, a gradient \(g_t\) enters the momentum state produced at time \(t\), so its later momentum multipliers begin with \(\beta_{t+1}\). Its future momentum-only weight is therefore exactly \(E_{t+1}\).

## Verification

The accompanying `verify.py` evaluates the defining finite product sum using exact rational arithmetic for many horizons and rational initial momenta.

It checks the backward recurrence, the closed form for \(E_t\), the source proxy \(P_t\), the time-independent ratio \(E_t/P_t\), and the one-step-shifted gradient tail.

The script also checks the three numerical relative-error examples in the finding.

No numerical experiment is used to prove the identity; the proof is finite algebra and backward induction.

## Relationship to prior work

Chen, Wolfe, Li, and Kyrillidis introduce DEMON by asking that the cumulative influence of momentum decrease with the remaining training horizon. Their derivation freezes the current momentum coefficient, replaces the future tail by the geometric series
\[
\beta_t/(1-\beta_t),
\]
and chooses the nonlinear schedule so that this proxy decreases linearly.

The same source explicitly notes that momentum changes at later iterations and calls the frozen-coefficient argument a close approximation, motivated by momentum products decaying faster than the schedule changes.

The source also writes the true time-varying products in its norm-growth identity, but does not sum the DEMON products into the finite-horizon formula above.

Focused searches for DEMON together with exact finite-horizon momentum products, cumulative gradient contribution, and linear tail identities did not identify a published statement equivalent to
\[
E_t
=
\frac{b(T-t)}{T(1-b)+b}.
\]
The closest indexed results concerned general heavy-ball stability or unrelated time-varying optimization recurrences and did not specialize the DEMON schedule.

## Limitations

The finding is a structural identity for the momentum schedule, not a convergence theorem for a loss function.

The source paper's use of the word “energy” is informal. The quantity analyzed here is the exact signed scalar multiplier carried by a fixed momentum component through future parameter updates. For a fixed vector component, its norm contribution scales by the same nonnegative coefficient because \(0<\beta_t<1\) before the endpoint.

The exact linearity does not imply that momentum is always beneficial, nor that the DEMON schedule is uniquely determined by this property.

## References

1. John Chen, Cameron Wolfe, Zhao Li, and Anastasios Kyrillidis, “Demon: Improved Neural Network Training with Momentum Decay,” arXiv:1910.04952v1, first submitted 2019-10-11; later revised as arXiv:1910.04952v4.
