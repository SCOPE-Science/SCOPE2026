# Exact confidence gain for a constant biregular CAME input

## Finding

Let a nonzero scalar \(g\in\mathbb R\setminus\{0\}\) and a fixed sign-support matrix \(Q\in\{-1,0,1\}^{a\times b}\) determine the constant prescribed gradient \(G=gQ\). Suppose the nonzero support of \(Q\) is biregular: each row and each column has the same positive active fraction \(p\in(0,1]\). Write \(s=\operatorname{sgn}(g)\in\{-1,+1\}\). Run the matrix CAME recurrence with zero initial moments, first regularizer \(\epsilon_1=0\), clipping threshold \(d=1\), \(0\le\beta_2<1\), \(0<\beta_1,\beta_3<1\), and confidence regularizer \(\epsilon_2\ge0\). Use the source convention of applying exponential moving averages to row and column **sums** before rank-one reconstruction.

At every integer time \(t\ge1\), the first factored second-moment matrix is constant across entries:
\[
v_t=(1-\beta_2^t)p g^2\,\mathbf1_a\mathbf1_b^\top.
\]
Its unclipped normalized direction is \(s Q/\sqrt{(1-\beta_2^t)p}\), whose RMS equals \((1-\beta_2^t)^{-1/2}\). Consequently clipping with threshold one cancels that factor exactly and gives
\[
\boxed{\widehat U_t=\frac{sQ}{\sqrt p},\qquad
m_t=\frac{s(1-\beta_1^t)}{\sqrt p}\,Q.}
\]
The residual is \(\widehat U_t-m_t=s\beta_1^t Q/\sqrt p\). Because its square no longer depends on the sign of \(g\), the second factored confidence statistic is spatially uniform:
\[
\boxed{S_t=h_t\,\mathbf1_a\mathbf1_b^\top,\qquad
h_t=(1-\beta_3)\sum_{i=1}^t\beta_3^{t-i}(\beta_1^{2i}+\epsilon_2).}
\]
Therefore the final, pre-learning-rate direction is
\[
\boxed{D_t=\frac{s(1-\beta_1^t)}{\sqrt p\,\sqrt{h_t}}\,Q,\qquad
\operatorname{RMS}(D_t)=\frac{1-\beta_1^t}{\sqrt{h_t}}.}
\]
In particular, the global RMS is independent of \(p\), while active-coordinate **magnitudes** grow by the exact factor \(p^{-1/2}\) relative to otherwise identical dense support. The orientation follows \(\operatorname{sgn}(g)Q\), not necessarily \(Q\).

If \(\epsilon_2>0\), then \(h_t\to\epsilon_2\) and
\[
\operatorname{RMS}(D_t)\longrightarrow\epsilon_2^{-1/2}.
\]
For \(\epsilon_2=0\) and \(\beta_3\ne\beta_1^2\), the exact finite-time expression is
\[
h_t=(1-\beta_3)\beta_1^2\frac{\beta_3^t-\beta_1^{2t}}{\beta_3-\beta_1^2},
\]
while on the resonance \(\beta_3=\beta_1^2\) it is \(h_t=t(1-\beta_3)\beta_1^{2t}\). Thus \(h_t\to0\) and the unregularized global RMS diverges. With the experimental second-floor value \(\epsilon_2=10^{-16}\), the formal stationary pre-learning-rate RMS equals \(10^8\).

## Assumptions and scope

The gradient is **externally prescribed**, real, nonzero and constant in time; this is an input-response theorem rather than a convergence or divergence theorem for any optimization objective. The rectangular matrix support is simultaneously row- and column-regular, its signs are arbitrary and fixed, and the same density \(p\) holds in both directions. Positive \(p\), nonzero \(g\), and \(\beta_2<1\) make the first normalization well-defined at every finite positive time. Since \(\beta_1>0\), the confidence sum is strictly positive at finite positive times even when \(\epsilon_2=0\). The exact first-stage cancellation uses \(\epsilon_1=0\), whereas a practical positive first floor can perturb it. The source's update-clipping threshold is \(d=1\). No claim of a training-time stationary regime, stochastic-residual calibration, or sign-insensitive **direction** is made.

## Proof

Write the matrix dimensions as \(a\times b\). Each row has exactly \(pb\) active entries and each column has exactly \(pa\). Since \(G_{ij}^2=g^2 |Q_{ij}|\), the instantaneous squared-gradient row sums all equal \(p b g^2\), and the column sums all equal \(p a g^2\). From zero initialization the first exponentially averaged factors at time \(t\) are
\[
r_t=(1-\beta_2^t)p b g^2\mathbf1_a,
\qquad c_t=(1-\beta_2^t)p a g^2\mathbf1_b.
\]
Their rank-one reconstruction is
\[
v_t=\frac{r_t c_t^\top}{\mathbf1_a^\top r_t}
=(1-\beta_2^t) p g^2\mathbf1_a\mathbf1_b^\top.
\]
Dividing \(G=gQ\) by the positive square root of \(v_t\) gives
\[
U_t=\frac{g}{|g|}\frac{Q}{\sqrt{(1-\beta_2^t)p}}
=\frac{sQ}{\sqrt{(1-\beta_2^t)p}}.
\]
Because precisely a fraction \(p\) of entries is active, \(\operatorname{RMS}(U_t)=(1-\beta_2^t)^{-1/2}\ge1\). The prescribed clipping divides \(U_t\) by this RMS, giving \(\widehat U_t=sQ/\sqrt p\) for **both signs of \(g\)**. The first-moment recurrence, \(m_0=0\) and \(m_t=\beta_1m_{t-1}+(1-\beta_1)\widehat U_t\), yields \(m_t=s(1-\beta_1^t)Q/\sqrt p\).

The confidence residual equals \(s\beta_1^t Q/\sqrt p\); squaring gives active value \(\beta_1^{2t}/p\) and zero otherwise. The squared residual plus \(\epsilon_2\) therefore has identical row sums \(b(\beta_1^{2t}+\epsilon_2)\), and identical column sums \(a(\beta_1^{2t}+\epsilon_2)\). After exponential averaging with \(\beta_3\), these factors are \(R_t=b h_t\mathbf1_a\) and \(C_t=a h_t\mathbf1_b\). Consequently the confidence reconstruction
\[
S_t=\frac{R_t C_t^\top}{\mathbf1_a^\top R_t}
=h_t\mathbf1_a\mathbf1_b^\top.
\]
The final direction \(D_t=m_t/\sqrt{S_t}\) is the displayed expression. Its global RMS is \((1-\beta_1^t)/\sqrt{h_t}\), because \(Q\) has RMS \(\sqrt p\), and its active-entry magnitudes scale by \(p^{-1/2}\). The displayed limits and the resonant/geometric finite sums follow from the scalar convolution defining \(h_t\). This proves every asserted identity. \(\square\)

## Independent mathematical checks and exact limits

The first-stage sign is essential. For \(g<0\), already at \(t=1\) a normalized active entry has sign opposite to the corresponding entry of \(Q\); any formula omitting \(\operatorname{sgn}(g)\) from \(\widehat U_t\), \(m_t\), the residual, or \(D_t\) is false under the stated quantifier \(g\ne0\). An independent direct matrix-recurrence computation checked both \(g=+2\) and \(g=-2\) over seventeen iterates with biregular sparse support, including both factorizations and normalization. Those finite checks corroborate the algebra but do not prove the general theorem. The stationary law applies only under the prescribed idealized recurrence and does not infer an actual learning rate, loss change, or practical stochastic optimizer behavior.

## Relationship to prior work

Luo, Ren, Zheng, Jiang, Jiang and You introduce the CAME factored-gradient and residual-confidence mechanism and interpret the inverse square root of the residual statistic as confidence. Their Algorithm 2 explicitly normalizes the **signed** gradient \(g_t\) by a nonnegative reconstructed second moment and specifies clipping before momentum and second residual factorization. It does not state the closed-form constant biregular-input confidence recursion, the cancellation of global support density, or the \(\epsilon_2^{-1/2}\) limiting RMS. The first factorization and RMS clipping originate in Shazeer and Stern's Adafactor. The present conclusion is restricted to the specified exact constant-gradient test class and does not assert a universal optimization-performance improvement or novelty of the underlying recurrence.

## References

1. Y. Luo, X. Ren, Z. Zheng, Z. Jiang, X. Jiang, and Y. You, *CAME: Confidence-guided Adaptive Memory Efficient Optimization*, ACL 2023, 2023, Algorithm 2. https://aclanthology.org/2023.acl-long.243.pdf ; arXiv:2307.02047.
2. N. Shazeer and M. Stern, *Adafactor: Adaptive Learning Rates with Sublinear Memory Cost*, 2018, arXiv:1804.04235. https://arxiv.org/abs/1804.04235
