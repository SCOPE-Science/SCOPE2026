# CAME's confidence stage has an exact stationary gain law
## Finding

CAME augments an Adafactor-style normalized update with a second factored statistic intended to measure confidence. On a constant matrix gradient, that confidence stage has an exact closed form.

Let
\[
G=gQ,
\qquad
g\ne0,
\]
where
\[
Q_{ij}\in\{-1,0,1\}.
\]
Assume the support of \(Q\) is biregular with density
\[
p\in(0,1]:
\]
every row has exactly the same fraction \(p\) of active entries and every column has exactly the same fraction \(p\).

Use the matrix CAME recurrence with zero initial states,
\[
\epsilon_1=0,
\qquad
d=1,
\qquad
0\le\beta_2<1,
\qquad
0<\beta_1,\beta_3<1,
\qquad
\epsilon_2\ge0.
\]

The first factored second moment is spatially constant. At time \(t\),
\[
v_t
=
(1-\beta_2^t)p g^2
\]
on every matrix entry. Hence the un-clipped normalized update has active magnitude
\[
\frac{1}{\sqrt{(1-\beta_2^t)p}},
\]
and its matrix RMS is
\[
\frac{1}{\sqrt{1-\beta_2^t}}.
\]
Since the clipping threshold is \(1\), update clipping removes this common temporal factor exactly:
\[
\boxed{
\widehat U_t
=
\frac{Q}{\sqrt p}
}
\]
for every \(t\).

Thus the CAME momentum is
\[
\boxed{
m_t
=
\frac{1-\beta_1^t}{\sqrt p}Q
}.
\]

The residual used to define confidence is
\[
\widehat U_t-m_t
=
\frac{\beta_1^t}{\sqrt p}Q.
\]
Its squared matrix is supported on the same biregular pattern. The second row-column factorization therefore produces a spatially uniform confidence matrix:
\[
\boxed{
S_t
=
h_t\mathbf 1\mathbf 1^\top
}
\]
with
\[
\boxed{
h_t
=
(1-\beta_3)
\sum_{i=1}^{t}
\beta_3^{t-i}
\left(
\beta_1^{2i}+\epsilon_2
\right)
}.
\]

Consequently the final pre-learning-rate direction is
\[
\boxed{
D_t
=
\frac{1-\beta_1^t}
{\sqrt p\,\sqrt{h_t}}
Q
}.
\]

Two effects follow immediately.

First, the matrix RMS is
\[
\boxed{
\operatorname{RMS}(D_t)
=
\frac{1-\beta_1^t}{\sqrt{h_t}}
},
\]
which is independent of the support density \(p\). Yet every active coordinate is amplified relative to the dense \(p=1\) case by
\[
\boxed{
p^{-1/2}
}.
\]
The confidence stage therefore cannot distinguish a dense constant update from a biregular sparse constant update by global RMS; it preserves the exact inverse-square-root density concentration inherited from the first factorization.

Second, when
\[
\epsilon_2>0,
\]
\[
h_t\longrightarrow\epsilon_2,
\]
so
\[
\boxed{
\operatorname{RMS}(D_t)
\longrightarrow
\epsilon_2^{-1/2}
}.
\]
When
\[
\epsilon_2=0,
\]
the confidence denominator vanishes. If
\[
\beta_3\ne\beta_1^2,
\]
then
\[
h_t
=
(1-\beta_3)\beta_1^2
\frac{
\beta_3^t-\beta_1^{2t}
}{
\beta_3-\beta_1^2
},
\]
while at
\[
\beta_3=\beta_1^2
\]
one has
\[
h_t
=
t(1-\beta_3)\beta_1^{2t}.
\]
Thus the unregularized confidence gain diverges exactly.

For the source experimental value
\[
\epsilon_2=10^{-16},
\]
the stationary limiting pre-learning-rate RMS is
\[
10^8.
\]
This is an input-response statement, not a claim that practical stochastic training reaches that stationary limit.

## Assumptions and scope

The gradient matrix is externally prescribed and constant in time.

The support is biregular: equal active density in every row and every column. Signs on the active entries may be arbitrary but fixed.

The first regularizer is set to
\[
\epsilon_1=0.
\]
The source uses a tiny positive value for numerical safety; the theorem isolates the exact algebraic core above that floor.

The update-clipping threshold is the source value
\[
d=1.
\]

The second confidence regularizer
\[
\epsilon_2
\]
is retained explicitly.

The result concerns the optimizer response and does not assert convergence or divergence on a fixed objective.

## Proof

Let the matrix dimensions be \(n\times m\). If the support density is \(p\), every row contains \(pm\) active entries and every column contains \(pn\) active entries.

Because
\[
G^2=g^2|Q|,
\]
the instantaneous squared-gradient row sums are all
\[
pmg^2,
\]
and the column sums are all
\[
png^2.
\]
Starting from zero, the first factored states are therefore
\[
r_t
=
(1-\beta_2^t)pmg^2\mathbf 1_n,
\]
\[
c_t
=
(1-\beta_2^t)png^2\mathbf 1_m.
\]
Their rank-one reconstruction is
\[
v_t
=
\frac{r_tc_t}{\mathbf 1_n^\top r_t}
=
(1-\beta_2^t)pg^2
\mathbf 1_n\mathbf 1_m^\top.
\]

Hence the active entries of the raw normalized update have magnitude
\[
[(1-\beta_2^t)p]^{-1/2}.
\]
Since a fraction \(p\) of all entries is active,
\[
\operatorname{RMS}(U_t)
=
(1-\beta_2^t)^{-1/2}.
\]
Update clipping with threshold \(1\) divides by exactly this value, proving
\[
\widehat U_t=Q/\sqrt p.
\]

The momentum recurrence is now scalar on the fixed pattern:
\[
m_t
=
\beta_1m_{t-1}
+
(1-\beta_1)\widehat U_t,
\qquad
m_0=0,
\]
so
\[
m_t=(1-\beta_1^t)Q/\sqrt p.
\]

The residual is therefore
\[
\widehat U_t-m_t
=
\beta_1^tQ/\sqrt p.
\]
Its square has active value
\[
\beta_1^{2t}/p.
\]
Each row sum is
\[
m\beta_1^{2t}
\]
and each column sum is
\[
n\beta_1^{2t};
\]
the density \(p\) cancels. Adding
\[
\epsilon_2
\]
to every entry changes these to
\[
m(\beta_1^{2t}+\epsilon_2)
\]
and
\[
n(\beta_1^{2t}+\epsilon_2).
\]

After exponential averaging with decay \(\beta_3\), the confidence factors are
\[
R_t=mh_t\mathbf 1_n,
\qquad
C_t=nh_t\mathbf 1_m.
\]
Their reconstruction is therefore exactly
\[
S_t=h_t\mathbf 1_n\mathbf 1_m^\top.
\]
Division of \(m_t\) by \(\sqrt{S_t}\) proves the stated direction and RMS laws.

The limit for positive \(\epsilon_2\) follows from stability of the scalar exponential average. The zero-floor closed forms are finite geometric sums.

## Verification

The accompanying `verify.py` directly implements the matrix recurrences for cyclic biregular supports.

It checks the first factored state, exact clipping cancellation, momentum law, second factored confidence state, density-independent global RMS, inverse-square-root active-coordinate scaling, and both confidence-floor limits.

The computation is a transcription check. The identities are proved algebraically above.

## Relationship to prior work

Luo, Ren, Zheng, Jiang, Jiang, and You introduce CAME by applying an Adafactor-style rank-one reconstruction to squared gradients and then a second rank-one reconstruction to the squared residual between the clipped current update and its momentum. They interpret the inverse square root of the residual statistic as confidence: smaller residual means a larger step.

Their algorithm specifies
\[
\beta_1=0.9,
\qquad
\beta_2=0.999,
\]
and reports experiments with
\[
\beta_3
\]
near one and
\[
\epsilon_2=10^{-16}.
\]

The defining paper discusses erroneous Adafactor updates qualitatively and motivates CAME as a confidence correction, but it does not state the exact constant-input confidence gain, the limiting \(\epsilon_2^{-1/2}\) RMS, or the biregular density cancellation derived here.

Shazeer and Stern introduced the underlying factored second-moment reconstruction and update clipping in Adafactor. Their paper establishes the row-column factorization and motivates update RMS near one, but does not contain CAME's second confidence factorization.

Focused published-record searches for stationary CAME updates, vanishing confidence residuals, constant-gradient recurrences, sparse biregular supports, and density amplification did not identify an implication-equivalent result.

## Limitations

The theorem uses a constant gradient input and does not model stochastic residual variance.

The exact first-stage cancellation assumes
\[
\epsilon_1=0.
\]

Biregularity is essential to the spatially uniform confidence reconstruction.

The large limiting gain is a diagnostic of the optimizer recurrence, not a prediction of a particular training run.

## References

1. Yang Luo, Xiaozhe Ren, Zangwei Zheng, Zhuo Jiang, Xin Jiang, and Yang You, “CAME: Confidence-guided Adaptive Memory Efficient Optimization,” arXiv:2307.02047v1, 2023; ACL 2023.
2. Noam Shazeer and Mitchell Stern, “Adafactor: Adaptive Learning Rates with Sublinear Memory Cost,” arXiv:1804.04235v1, 2018.
