# Exact step-size amplification from fused decoupled decay under Stiefel polar retraction

## Statement

Let
\[
\operatorname{St}(d,r)=\{W\in\mathbb R^{d\times r}:W^TW=I_r\},
\]
and let \(\Delta\in T_W\operatorname{St}(d,r)\), so
\[
W^T\Delta+\Delta^TW=0.
\]
For a full-column-rank matrix \(Y\), write its polar factor as
\[
\mathcal P(Y)=Y(Y^TY)^{-1/2}.
\]
Fix \(a>0\). Then the following identities hold.

### Theorem 1: radial shrinkage is exactly a tangent-step rescaling

\[
\boxed{\mathcal P(aW+\Delta)=\mathcal P\!\left(W+\frac{\Delta}{a}\right).}
\]
Moreover,
\[
\boxed{(aW+\Delta)^T(aW+\Delta)=a^2I_r+\Delta^T\Delta,}
\]
so if \(s_1,\ldots,s_r\) are the singular values of \(\Delta\), then
\[
\boxed{\sigma_i(aW+\Delta)=\sqrt{a^2+s_i^2}.}
\]
In particular \(aW+\Delta\) has full column rank for every tangent \(\Delta\) whenever \(a\ne0\), and
\[
\boxed{
\kappa_2(aW+\Delta)
=
\sqrt{\frac{a^2+s_{\max}^2}{a^2+s_{\min}^2}}.
}
\]
If \(s_{\max}>s_{\min}\), decreasing \(a>0\) strictly worsens this condition number.

For an AdamW-style fused ambient decay with learning rate \(\eta\), decay coefficient \(\lambda\), and tangent task direction \(D\), take
\[
\Delta=-\eta D,
\qquad
a=1-\eta\lambda>0.
\]
Then
\[
\boxed{
\mathcal P\bigl((1-\eta\lambda)W-\eta D\bigr)
=
\mathcal P\bigl(W-\eta_{\rm eff}D\bigr),
\qquad
\eta_{\rm eff}=\frac{\eta}{1-\eta\lambda}.
}
\]
Thus fused decoupled Euclidean weight decay does not disappear after a single polar retraction: for a tangent task step it is exactly a **step-size amplification**.

### Theorem 2: exact frame displacement and monotonic amplification

The retracted frame obeys
\[
\boxed{
\left\|\mathcal P(aW+\Delta)-W\right\|_F^2
=
2\sum_{i=1}^r
\left(1-\frac{a}{\sqrt{a^2+s_i^2}}\right).
}
\]
Consequently, if \(\Delta\ne0\), this displacement is strictly decreasing in \(a>0\). In the AdamW parameterization \(a=1-\eta\lambda\), it is therefore strictly increasing in \(\lambda\) throughout \(0\le\eta\lambda<1\). More explicitly,
\[
\frac{d}{d\lambda}
\left\|\mathcal P((1-\eta\lambda)W+\Delta)-W\right\|_F^2
=
2\eta\sum_i
\frac{s_i^2}{\bigl((1-\eta\lambda)^2+s_i^2\bigr)^{3/2}}>0,
\]
when \(\Delta\) is held fixed and nonzero. If instead \(\Delta=-\eta D\), the same formula contains \(s_i^2=\eta^2\sigma_i(D)^2\).

### Theorem 3: decay and retraction do not commute

Let
\[
R=\mathcal P(W+\Delta)\in\operatorname{St}(d,r).
\]
For every \(a>0\),
\[
\boxed{\mathcal P(aR)=R.}
\]
Hence a radial decay applied to an already retracted Stiefel point and followed by another polar retraction is an exact no-op, while the fused update \(\mathcal P(aW+\Delta)\) is generally different and equals the amplified tangent step from Theorem 1.

For fixed tangent \(D\) and \(a=1-\eta\lambda\), smoothness of the polar retraction at the origin gives
\[
\eta_{\rm eff}=\eta+\eta^2\lambda+O(\eta^3),
\]
therefore
\[
\boxed{
\mathcal P((1-\eta\lambda)W-\eta D)
-
\mathcal P(W-\eta D)
=
-\eta^2\lambda D+O(\eta^3).
}
\]
This reconciles the finite-step effect with the fact that the Riemannian gradient of \(\frac\lambda2\|W\|_F^2\) is identically zero on the Stiefel manifold: the fused AdamW effect is second order in the small-step limit, not an intrinsic first-order regularization field.

### Corollary 4: tangent polar steps cannot lose rank

Setting \(a=1\) in Theorem 1 gives
\[
(W+\Delta)^T(W+\Delta)=I_r+\Delta^T\Delta,
\]
so
\[
\boxed{\sigma_{\min}(W+\Delta)\ge1}
\]
for **every** tangent \(\Delta\), with no small-step hypothesis. Thus exact column-rank loss is impossible for a tangent Stiefel step before polar retraction.

Write
\[
A=W^T\Delta,\qquad B=(I-WW^T)\Delta.
\]
Then \(A^T=-A\) and
\[
aW+\Delta=W(aI+A)+B.
\]
Since \(aI+A\) is invertible for \(a>0\), the new column space is the graph over \(\operatorname{span}(W)\) of
\[
Z=B(aI+A)^{-1}.
\]
If \(\theta_i\) are the principal angles between \(\operatorname{span}(W)\) and \(\operatorname{span}(aW+\Delta)\), then
\[
\boxed{\{\tan\theta_i\}=\{\sigma_i(Z)\}.}
\]
Because
\[
(aI+A)^T(aI+A)=a^2I+A^TA\succeq a^2I,
\]
we obtain
\[
\boxed{
\theta_{\max}
\le
\arctan\frac{\|B\|_2}{a}
\le
\arctan\frac{\|\Delta\|_2}{a}.
}
\]
For an ordinary tangent polar step \(a=1\), the angle bound holds without any restriction such as \(\|\Delta\|<1\). Purely vertical tangent directions (\(B=0\)) rotate the frame but leave its column space unchanged.

## Proof

The tangent condition cancels the cross term:
\[
(aW+\Delta)^T(aW+\Delta)
=a^2W^TW+a(W^T\Delta+\Delta^TW)+\Delta^T\Delta
=a^2I+\Delta^T\Delta.
\]
This proves the Gram identity and the singular-value formula. Positive homogeneity of the polar factor gives
\[
\mathcal P(aY)=\mathcal P(Y)\qquad(a>0),
\]
which applied to \(Y=W+\Delta/a\) proves Theorem 1.

For Theorem 2, put
\[
H=(a^2I+\Delta^T\Delta)^{1/2},
\qquad Q=(aW+\Delta)H^{-1}.
\]
Then \(Q=\mathcal P(aW+\Delta)\). Since \(W^T\Delta\) is skew-symmetric while \(H^{-1}\) is symmetric,
\[
\operatorname{tr}(W^T\Delta H^{-1})=0.
\]
Hence
\[
\operatorname{tr}(W^TQ)=a\operatorname{tr}(H^{-1})
=\sum_i\frac{a}{\sqrt{a^2+s_i^2}}.
\]
Using \(\|Q-W\|_F^2=2r-2\operatorname{tr}(W^TQ)\) gives the claimed formula. Its derivative with respect to \(a\) is negative whenever at least one \(s_i>0\), and \(da/d\lambda=-\eta\), proving monotonicity in the decay coefficient.

Theorem 3 follows immediately from positive homogeneity because \(R\) already has orthonormal columns. The small-step expansion uses the defining property of a smooth retraction, \(D R_W(0)[X]=X\), together with \(\eta/(1-\eta\lambda)=\eta+\eta^2\lambda+O(\eta^3)\).

For the principal-angle statement, the decomposition \(\Delta=WA+B\) yields
\[
aW+\Delta=W(aI+A)+B
=\bigl(W+B(aI+A)^{-1}\bigr)(aI+A).
\]
Right multiplication by the invertible \(aI+A\) does not change the column space. The standard graph representation of a subspace gives \(\tan\theta_i=\sigma_i(B(aI+A)^{-1})\). The displayed norm bound then follows from \(\sigma_{\min}(aI+A)\ge a\).

## Context and comparison with prior work

Guerrero (2026) studies Stiefel-constrained transformer projections, uses tangent updates followed by polar retraction, and identifies the zero Riemannian gradient of Euclidean weight decay on \(\operatorname{St}(d,r)\) as a mechanism. The same paper uses a trust-bounded polar update and emphasizes its conditioning. The results above separate three operations that are easy to conflate: intrinsic/projected \(L^2\) decay is zero; radial shrinkage of an already retracted point is erased by the next polar projection; but an AdamW-style radial term fused with a nonzero tangent task step before a single polar retraction rescales that task step exactly.

The polar retraction itself, its projection interpretation, and Stiefel geometry are classical; see Edelman--Arias--Smith (1998) and Absil--Malick (2012). Decoupled Euclidean weight decay is due to Loshchilov--Hutter (2019). Current GeometricOptimizers.jl documentation explicitly suppresses Euclidean decay on Stiefel and Grassmann parameters because its Riemannian gradient vanishes; that implementation therefore realizes the intrinsic no-op semantics, not the fused ambient update analyzed here. Spectral Compact Training (Kohlberger, 2026) is a related example in which unconstrained optimizer updates are followed by a Stiefel QR retraction, illustrating that optimizer/retraction ordering is practically consequential, although its update is not assumed tangent and is therefore outside the theorem above.

To the best of our knowledge, the inspected literature does not state the exact fused-decay identity, its effective-step interpretation, the monotone chordal-displacement law, or the accompanying order-sensitivity theorem. The standard polar identities used in the proof are not claimed as new.

## Computational model and reproducibility

All statements are exact-arithmetic matrix identities. The verification artifact `artifacts/verify_stiefel_decay.py` tests random tangent matrices and checks the Gram identity, effective-step equivalence, sequential-decay no-op, singular-value formula, chordal formula, and graph/principal-angle identity. It also gives a deterministic horizontal example showing strict displacement amplification. The recorded output was generated with NumPy 2.3.5.

## Limitations

The main theorem assumes the non-decay part of the update is tangent at the current Stiefel point. An ambient AdamW step with an unprojected gradient need not satisfy the cancellation identity. The exact step transform is stated only for \(1-\eta\lambda>0\); the zero and negative scaling regimes have different polar-sign behavior and are not treated. The results are one-step deterministic identities and do not analyze optimizer moment evolution, stochastic training, generalization, or long-time convergence. The exact conditioning and chordal formulas are specific to polar retraction; positive-homogeneity aspects have analogues for some QR conventions, but those are not asserted here. No claim is made that Guerrero's experiments applied fused decay to the constrained Stiefel blocks.

## References

1. R. D. Guerrero, “Stiefel Attention: When the Geometry of Transformer Projection Matrices Dominates Optimizer Choice—and When It Does Not,” arXiv:2609.19363, 2026. https://arxiv.org/abs/2609.19363
2. I. Loshchilov and F. Hutter, “Decoupled Weight Decay Regularization,” ICLR 2019, arXiv:1711.05101. https://arxiv.org/abs/1711.05101
3. P.-A. Absil and J. Malick, “Projection-like Retractions on Matrix Manifolds,” SIAM Journal on Optimization 22(1), 135–158, 2012. https://doi.org/10.1137/100802529
4. A. Edelman, T. A. Arias, and S. T. Smith, “The Geometry of Algorithms with Orthogonality Constraints,” SIAM Journal on Matrix Analysis and Applications 20(2), 303–353, 1998. https://doi.org/10.1137/S0895479895290954
5. GeometricOptimizers.jl, “Weight Decay on Manifolds,” documentation generated 2026-08-29. https://juliagni.github.io/GeometricOptimizers.jl/stable/weight_decay/
6. B. R. Kohlberger, “Spectral Compact Training: Pre-Training Large Language Models via Permanent Truncated SVD and Stiefel QR Retraction,” arXiv:2604.00733, 2026. https://arxiv.org/abs/2604.00733
