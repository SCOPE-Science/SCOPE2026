# Uniform Aligned-MTL has a sharp full-rank conflict window
## Finding

Let
\[
g_1,g_2\in\mathbb R^d
\]
be nonzero and linearly independent, and write
\[
a=\lVert g_1\rVert_2,\qquad
b=\lVert g_2\rVert_2,\qquad
\rho=\frac{g_1^\top g_2}{ab}\in(-1,1),\qquad
q=\frac ab.
\]
With
\[
G=[g_1\;\;g_2],\qquad H=G^\top G,
\]
source-form Aligned-MTL at uniform weights is
\[
\widehat G=\sigma_{\min}(G)\,G H^{-1/2},
\qquad
d=\frac12\widehat G\mathbf 1.
\]

The original task derivatives are
\[
G^\top d
=
\frac{\sigma_{\min}(G)}2H^{1/2}\mathbf 1.
\]
Writing
\[
s=\sqrt{1-\rho^2},
\]
their signs are exactly the signs of
\[
\boxed{a+b(\rho+s)}
\]
and
\[
\boxed{b+a(\rho+s)}.
\]

If
\[
\rho\ge-\frac1{\sqrt2},
\]
both quantities are positive for every \(q>0\). Thus \(-d\) is a strict first-order descent step for both tasks.

If
\[
-1<\rho<-\frac1{\sqrt2},
\]
define
\[
\boxed{\tau(\rho)=-\rho-\sqrt{1-\rho^2}}.
\]
Then
\[
0<\tau(\rho)<1,
\]
and strict common descent holds exactly when
\[
\boxed{
\tau(\rho)<q<\frac1{\tau(\rho)}
}.
\]
At the left endpoint task \(1\) is neutral; below it task \(1\) is harmed. At the right endpoint task \(2\) is neutral; above it task \(2\) is harmed. Equivalently,
\[
\boxed{
|\log q|<-\log\tau(\rho)
}.
\]
As \(\rho\to-1\), \(\tau(\rho)\to1\), so the safe imbalance window collapses.

There is an exact symmetric corollary. If
\[
a=b
\]
and
\[
-1<\rho\le0,
\]
then
\[
\boxed{
d=\frac{g_1+g_2}{2}.
}
\]
Thus in the norm-balanced conflict regime, Aligned-MTL changes the internal aligned columns but leaves the actual uniform model-update direction exactly equal to ordinary averaging.

For
\[
0<\rho<1,
\]
the equal-norm aggregate is
\[
\boxed{
d=
\sqrt{\frac{1-\rho}{1+\rho}}\,
\frac{g_1+g_2}{2}.
}
\]

## Assumptions and scope

The result uses exact Aligned-MTL with the smallest singular value as the global scale and the source default uniform task weights.

The two gradients are linearly independent, so the smallest singular value is positive and no rank-deficient convention is needed.

A task is improved to first order by the model step \(-d\) exactly when
\[
g_i^\top d>0.
\]

The theorem is an instantaneous aggregation statement, not a complete training-trajectory theorem.

## Proof

The task Gram matrix is
\[
H=
\begin{bmatrix}
a^2&ab\rho\\
ab\rho&b^2
\end{bmatrix}.
\]
Since \(|\rho|<1\), it is positive definite. For any positive-definite two-by-two matrix,
\[
H^{1/2}
=
\frac{H+\delta I}
{\sqrt{\operatorname{tr}H+2\delta}},
\qquad
\delta=\sqrt{\det H}.
\]
Here
\[
\delta=ab\sqrt{1-\rho^2}=abs.
\]
Therefore
\[
H^{1/2}\mathbf1
=
\frac1{\sqrt{a^2+b^2+2abs}}
\begin{bmatrix}
a^2+ab\rho+abs\\
b^2+ab\rho+abs
\end{bmatrix}.
\]
All omitted factors are positive, so the task-derivative signs reduce to
\[
a+b(\rho+s)
\]
and
\[
b+a(\rho+s).
\]

The quantity \(\rho+s\) is negative exactly when
\[
\rho<-\frac1{\sqrt2}.
\]
In that regime, putting \(\tau=-(\rho+s)\) gives
\[
g_1^\top d>0\iff q>\tau,
\qquad
g_2^\top d>0\iff q<1/\tau.
\]
This proves the phase diagram.

If \(a=b\), the vector \(\mathbf1\) is an eigenvector of \(H\) with eigenvalue \(a^2(1+\rho)\). For \(\rho\le0\), that is the smaller eigenvalue, so
\[
\sigma_{\min}(G)H^{-1/2}\mathbf1=\mathbf1
\]
and hence \(d=(g_1+g_2)/2\). For \(\rho>0\), the smallest eigenvalue is \(a^2(1-\rho)\), yielding the displayed shrinkage factor.

## Verification

The accompanying `verify.py` reconstructs Aligned-MTL from the task Gram eigendecomposition.

It checks randomized full-rank pairs against the closed sign formulas, verifies both sharp boundaries, confirms the safe norm-ratio interval, and checks the equal-norm aggregate identity on both sides of zero cosine.

The computation is a transcription guard. The theorem is proved analytically above.

## Relationship to prior work

Senushkin and coauthors define the condition number of the gradient matrix as a joint indicator of conflict and dominance, use fixed uniform task weights in the main objective, and construct Aligned-MTL by replacing all singular values with the smallest singular value. They emphasize that the transformed task gradients become orthogonal and equal in magnitude before being recombined.

The defining paper states that this construction is intended to remove negative interaction, but the inspected full text does not classify the signs of the original task derivatives after recombination.

Quinton and Rey later prove that Aligned-MTL is not universally non-conflicting and also that it is not linear under scaling. Their displayed non-conflict witness is rank deficient. Those broader facts are prior-covered.

The result here remains in the defining paper's linearly independent setting and gives the exact full-rank two-task boundary. Strong conflict alone is not enough for failure: conflict requires
\[
\rho<-\frac1{\sqrt2}
\]
together with sufficient norm imbalance. The equal-norm identity additionally shows a regime where internal orthogonalization is completely invisible in the actual parameter-update direction.

Focused published-record searches did not identify this full-rank phase diagram or the equal-norm conflict identity.

## Limitations

The exact classification is for two tasks and uniform preferences.

Nonuniform preferences are not classified here.

The theorem concerns descent against the original tasks, which is distinct from orthogonality of the transformed task gradients.

The general statement that Aligned-MTL is not universally non-conflicting is already known; the contribution is the sharp full-rank threshold and symmetric identity.

## References

1. Dmitry Senushkin, Nikolay Patakin, Arseny Kuznetsov, and Anton Konushin, “Independent Component Alignment for Multi-Task Learning,” arXiv:2305.19000v1, first submitted 2023-05-30; CVPR 2023.
2. Pierre Quinton and Valérian Rey, “Jacobian Descent for Multi-Objective Optimization,” arXiv:2406.16232v1, first submitted 2024-06-23.
