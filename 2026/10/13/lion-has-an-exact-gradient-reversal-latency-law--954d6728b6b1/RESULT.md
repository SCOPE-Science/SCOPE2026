# Lion has an exact gradient-reversal latency law
## Finding

Lion uses one exponential coefficient to mix the current gradient with the previous momentum before the sign operation and another coefficient to update the stored momentum. This split creates an exactly solvable lag after a persistent gradient reversal.

For one coordinate with zero weight decay,
\[
c_t=\beta_1m_{t-1}+(1-\beta_1)g_t,
\qquad
m_t=\beta_2m_{t-1}+(1-\beta_2)g_t,
\]
where
\[
0<\beta_1<1,
\qquad
0<\beta_2<1.
\]
Lion uses \(\operatorname{sign}(c_t)\) for the parameter update.

Assume a positive gradient \(G\) has persisted long enough that \(m_0=G\), and then the gradient reverses permanently to
\[
g=-rG,
\qquad
r>0.
\]
At post-reversal step \(n\ge1\),
\[
\boxed{
m_{n-1}=G[(1+r)\beta_2^{\,n-1}-r]
}
\]
and
\[
\boxed{
c_n=G[\beta_1(1+r)\beta_2^{\,n-1}-r].
}
\]

Because the new gradient is negative, Lion is still using the old sign exactly when
\[
\boxed{
\beta_2^{\,n-1}>\frac{r}{\beta_1(1+r)}.
}
\]

If
\[
r\ge\frac{\beta_1}{1-\beta_1},
\]
there is no strictly stale-sign update; equality gives \(c_1=0\). If
\[
0<r<\frac{\beta_1}{1-\beta_1},
\]
the exact number of strictly stale-sign updates is
\[
\boxed{
N_+(r)=
\left\lceil
\frac{\log(r/[\beta_1(1+r)])}{\log\beta_2}
\right\rceil.
}
\]

The stored momentum itself remains positive for
\[
\boxed{
N_m(r)=
\left\lceil
\frac{\log(r/(1+r))}{\log\beta_2}
\right\rceil
}
\]
steps, with
\[
N_+(r)\le N_m(r).
\]
Thus the \(\beta_1\) interpolation anticipates the reversal relative to the slower \(\beta_2\) state, but it can still preserve the old update sign for many steps.

At Lion's defining defaults
\[
\beta_1=0.9,
\qquad
\beta_2=0.99,
\]
an equal-magnitude reversal has
\[
\boxed{N_+(1)=59},
\qquad
\boxed{N_m(1)=69}.
\]
Also
\[
\frac{\beta_1}{1-\beta_1}=9.
\]
So the first update adopts the new sign immediately only for a reversal larger than nine times the old gradient magnitude; a nine-fold reversal makes the first pre-sign value exactly zero.

## Assumptions and scope

The claim concerns one coordinate of source-form Lion with weight decay omitted.

The old gradient regime is assumed long enough for the stored momentum to equal its constant-input fixed point \(G\).

The post-reversal gradient is externally prescribed as \(-rG\). The result isolates Lion's directional-memory response rather than a closed optimization trajectory in which gradients depend on changing parameters.

The boundary statement treats \(\operatorname{sign}(0)=0\).

## Proof

After reversal,
\[
m_n=\beta_2m_{n-1}-(1-\beta_2)rG,
\qquad
m_0=G.
\]
Subtracting the fixed point \(-rG\) gives
\[
m_n+rG=\beta_2(m_{n-1}+rG),
\]
hence
\[
m_n+rG=(1+r)G\beta_2^n.
\]
This proves the formula for \(m_{n-1}\).

Next,
\[
c_n=\beta_1m_{n-1}-(1-\beta_1)rG.
\]
Substitution gives
\[
c_n=G[\beta_1(1+r)\beta_2^{\,n-1}-r].
\]

The old sign persists precisely while the bracket is positive. At the first post-reversal step this is equivalent to
\[
r<\frac{\beta_1}{1-\beta_1},
\]
which proves the immediate-reversal threshold.

When the threshold ratio lies in \((0,1)\), monotonicity of \(\beta_2^j\) and \(\log\beta_2<0\) shows that the number of nonnegative integers \(j=n-1\) satisfying the strict inequality is exactly the displayed ceiling. The momentum-sign count follows from the identical argument applied to \(m_{n-1}>0\).

## Verification

The accompanying `verify.py` replays the scalar recurrence for multiple values of \(\beta_1\), \(\beta_2\), and \(r\).

It checks the two closed forms, the exact stale-sign count, the immediate-reversal threshold, the ordering of the two reversal clocks, the exact-power boundary, and the defining-default values \(59\), \(69\), and \(9\).

The computation is a transcription guard; the formulas are proved above.

## Relationship to prior work

Chen and coauthors introduce Lion with the two-coefficient sign-momentum rule and give the defaults
\[
\beta_1=0.9,
\qquad
\beta_2=0.99.
\]
Their analysis emphasizes the sign update's magnitude, batch-size behavior, hyperparameter tuning, and empirical limitations.

The inspected defining full text does not give a persistent gradient-reversal response, an exact stale-update count, or the nine-fold immediate-reversal threshold.

A later Lyapunov analysis interprets Lion as a principled constrained optimizer and studies its discrete- and continuous-time convergence structure. That broader theory does not state this exact step response.

Classical signed momentum is the closest structural relative, but Lion differs because the sign-driving interpolation uses \(\beta_1\) while the stored momentum uses \(\beta_2\). The two reversal clocks above quantify the consequence of that split.

Focused published-record searches for Lion gradient reversal, stale sign, momentum sign change, and exact reversal latency did not identify an implication-equivalent result.

## Limitations

The gradient sequence is externally prescribed and piecewise constant.

Weight decay is omitted.

Noisy, rotating, or parameter-dependent gradients can produce different sign histories.

The result diagnoses directional memory and does not by itself imply poor optimization performance.

## References

1. Xiangning Chen, Chen Liang, Da Huang, Esteban Real, Kaiyuan Wang, Yao Liu, Hieu Pham, Xuanyi Dong, Thang Luong, Cho-Jui Hsieh, Yifeng Lu, and Quoc V. Le, “Symbolic Discovery of Optimization Algorithms,” arXiv:2302.06675v1, first submitted 2023-02-13.
2. Lizhang Chen, Bo Liu, Kaizhao Liang, and Qiang Liu, “Lion Secretly Solves Constrained Optimization: As Lyapunov Predicts,” arXiv:2310.05898v1, 2023.
3. Jeremy Bernstein, Yu-Xiang Wang, Kamyar Azizzadenesheli, and Anima Anandkumar, “signSGD: Compressed Optimisation for Non-Convex Problems,” arXiv:1802.04434v1, 2018.
