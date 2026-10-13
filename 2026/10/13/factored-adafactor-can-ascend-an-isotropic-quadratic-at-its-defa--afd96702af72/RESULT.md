# Factored Adafactor can ascend an isotropic quadratic at its default first step
## Finding

Consider the \(2\times2\) isotropic quadratic
\[
f(X)=\frac12\|X\|_F^2,
\]
which is \(1\)-smooth and \(1\)-strongly convex with unique minimizer \(X^\star=0\).

Use source-form matrix Adafactor at its first step with
\[
\widehat\beta_{2,1}=0,\qquad d=1,\qquad \epsilon_1=e>0,
\]
and relative step \(\rho>0\). Start from
\[
X_0(B)=
\begin{bmatrix}
\sqrt{2e}&0\\
0&B
\end{bmatrix}.
\]
When \(\operatorname{RMS}(X_0)>\epsilon_2\), the source parameter-relative scale is
\[
\alpha=\frac{\rho}{2}\sqrt{B^2+2e}.
\]

The first factored second moment yields exactly two nonzero raw normalized update entries:
\[
u_1=\frac{\sqrt{2(B^2+6e)}}{4\sqrt e},
\qquad
u_2=\frac{B\sqrt{B^2+6e}}{B^2+2e}.
\]
Whenever clipping is active,
\[
\widehat u_i=\frac{2u_i}{\sqrt{u_1^2+u_2^2}}.
\]

As
\[
\frac{B}{\sqrt e}\to\infty,
\]
we have
\[
\widehat u_1\to2,\qquad \widehat u_2\to0,\qquad \frac{\alpha}{B}\to\frac{\rho}{2}.
\]
Therefore
\[
\boxed{
\frac{f(X_1)}{f(X_0)}\to1+\rho^2>1.
}
\]
Thus every positive relative step admits sufficient within-matrix scale separation for which the very first factored Adafactor step increases this isotropic strongly convex objective, despite matrix-level RMS clipping.

The defining paper's recommended first-step constants already give a concrete witness:
\[
e=10^{-30},\qquad \epsilon_2=10^{-3},\qquad d=1,\qquad \rho=10^{-2},\qquad B=1.
\]
For this instance,
\[
\boxed{
\frac{f(X_1)}{f(X_0)}>1.0000999999999.
}
\]

For comparison, replace the rank-one row/column second moment by the full elementwise second moment while retaining the same parameter-relative scale and RMS clipping. The two active raw normalized entries then tend to
\[
\sqrt{\frac23}\quad\text{and}\quad1,
\]
whose \(2\times2\) matrix RMS is
\[
\sqrt{\frac5{12}}<1.
\]
The clip is inactive, and
\[
\boxed{
\frac{f(X_1)}{f(X_0)}
\to
1-\rho+\frac{5}{12}\rho^2.
}
\]
This is strictly below \(1\) for
\[
0<\rho<\frac{12}{5}.
\]

Hence the rank-one factorization can reverse first-step descent: the global RMS budget is respected, but almost all of that budget is redirected toward a coordinate whose actual gradient is vanishingly small.

## Assumptions and scope

The result uses Algorithm 4 of the defining Adafactor paper for a matrix parameter at the first optimization step.

The asymptotic theorem fixes
\[
e=\epsilon_1>0,\qquad \epsilon_2<\infty,\qquad d=1,\qquad \rho>0
\]
and lets \(B/\sqrt e\) grow. The parameter-scale floor is then eventually inactive.

The explicit witness uses the source recommended values
\[
\epsilon_1=10^{-30},\qquad
\epsilon_2=10^{-3},\qquad
d=1,\qquad
\rho_1=10^{-2}.
\]

No claim is made that the complete Adafactor schedule diverges on this example. The theorem is a one-step obstruction to treating matrix-level update clipping as a descent safeguard.

The full-second-moment comparison isolates the mechanism; it is not a claim about Adam with momentum.

## Proof

Because \(\nabla f(X)=X\), the first gradient is \(G=X_0(B)\). The source adds \(e\) to every squared-gradient entry before forming row and column accumulators:
\[
G^2+e\mathbf 1\mathbf 1^\top
=
\begin{bmatrix}
3e&e\\
e&B^2+e
\end{bmatrix}.
\]
Its row and column sums are
\[
r=c=
\begin{bmatrix}
4e\\
B^2+2e
\end{bmatrix},
\]
with total
\[
S=B^2+6e.
\]

The source factored estimator is
\[
\widehat V=\frac{rc^\top}{S}.
\]
Thus
\[
\sqrt{\widehat V_{11}}=\frac{4e}{\sqrt S},
\qquad
\sqrt{\widehat V_{22}}=\frac{B^2+2e}{\sqrt S},
\]
which gives
\[
u_1=\frac{\sqrt{2S}}{4\sqrt e},
\qquad
u_2=\frac{B\sqrt S}{B^2+2e}.
\]

Only two entries of \(U\) are nonzero, so
\[
\operatorname{RMS}(U)=\frac12\sqrt{u_1^2+u_2^2}.
\]
When this exceeds \(d=1\), source clipping divides by that RMS and yields
\[
\widehat u_i=\frac{2u_i}{\sqrt{u_1^2+u_2^2}}.
\]

For fixed \(e>0\),
\[
u_1\sim\frac{B}{2\sqrt{2e}},
\qquad
u_2\to1,
\]
hence
\[
\widehat u_1\to2,\qquad \widehat u_2\to0.
\]
Also
\[
\alpha
=
\rho\operatorname{RMS}(X_0)
=
\frac{\rho}{2}\sqrt{B^2+2e},
\]
for all sufficiently large \(B\). Therefore
\[
\frac{(X_1)_{11}}B
=
\frac{\sqrt{2e}}B-\frac{\alpha}{B}\widehat u_1
\to-\rho
\]
and
\[
\frac{(X_1)_{22}}B
=
1-\frac{\alpha}{B}\widehat u_2
\to1.
\]
Since
\[
\frac{2f(X_0)}{B^2}\to1,
\]
the factored objective ratio tends to \(1+\rho^2\).

For a full elementwise second moment, the active first-step denominators are
\[
\sqrt{3e}\quad\text{and}\quad\sqrt{B^2+e}.
\]
The active normalized entries tend to \(\sqrt{2/3}\) and \(1\), so the matrix RMS tends to \(\sqrt{5/12}<1\). The clip is inactive. Dividing the updated coordinates by \(B\) gives limits
\[
-\frac{\rho}{2}\sqrt{\frac23}
\quad\text{and}\quad
1-\frac\rho2.
\]
Squaring and summing gives
\[
1-\rho+\frac{5}{12}\rho^2.
\]

## Verification

The accompanying `verify.py` reconstructs the first-step source row and column accumulators, rank-one second moment, matrix-RMS update clip, and parameter-relative scale.

High-precision decimal arithmetic checks the source-default witness and confirms
\[
f(X_1)>f(X_0).
\]
It also checks increasing scale-separation sequences against the two proved limiting ratios.

The computations are transcription guards only. The asymptotic statements are proved algebraically above.

## Relationship to prior work

Shazeer and Stern introduced Adafactor's row/column second-moment factorization, update clipping, increasing second-moment decay, and parameter-relative scaling. Their instability discussion centers on second-moment estimates becoming out of date under slow decay, motivating update clipping. The present example occurs at the first step, where
\[
\widehat\beta_{2,1}=0,
\]
so stale history is absent.

The defining source derives the rank-one approximation from row and column marginals and reports empirical behavior similar to full accumulators, but does not give a one-step descent theorem or the scale-separation mechanism above.

CAME later attributes part of the performance instability of memory-efficient adaptive optimization to errors from Adafactor-style factorization. That observation is qualitatively compatible with the finding but does not state this exact strongly convex ascent family.

Hong and Lin provide a later convergence analysis of Adafactor. Their analyzed update omits the original parameter-RMS multiplier, and their full-batch monotonicity statement requires specifically chosen regularization and step conditions. It therefore does not imply monotonicity for the defining paper's default first-step rule analyzed here.

The closest prior exact result in the checked corpus concerns CAME on equal-magnitude biregular update supports, where Adafactor-style factorization produces a sparsity-dependent amplification. That statement does not imply the present nonuniform diagonal effect: here the clip reallocates nearly all update energy to a tiny-gradient coordinate and the conclusion is objective ascent.

Focused searches for factored Adafactor objective increase, sparse diagonal gradients, magnitude inversion, and coordinate amplification did not identify an implication-equivalent published statement.

## Limitations

The theorem is a first-step \(2\times2\) construction.

The example uses extreme scale separation relative to \(\epsilon_1\). The source default \(\epsilon_1=10^{-30}\) makes the concrete unit-scale witness possible, but no claim is made that this configuration is typical in neural-network training.

Update clipping still enforces its stated matrix-RMS bound. The obstruction is the coordinate allocation inside that bound.

The finding does not contradict later convergence guarantees that use different scaling or impose sufficient step-size and regularization conditions.

## References

1. Noam Shazeer and Mitchell Stern, “Adafactor: Adaptive Learning Rates with Sublinear Memory Cost,” arXiv:1804.04235v1, first submitted 2018-04-11; ICML 2018, PMLR 80:4596–4604.
2. Yang Luo, Xiaozhe Ren, Zangwei Zheng, Zhuo Jiang, Xin Jiang, and Yang You, “CAME: Confidence-guided Adaptive Memory Efficient Optimization,” arXiv:2307.02047v1, first submitted 2023-07-05; ACL 2023.
3. Yusu Hong and Junhong Lin, “Theoretical Investigation of Adafactor for Non-Convex Smooth Optimization,” NeurIPS 2025.
