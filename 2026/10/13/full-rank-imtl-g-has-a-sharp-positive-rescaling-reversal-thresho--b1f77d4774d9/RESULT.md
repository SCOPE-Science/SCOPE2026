# Full-rank IMTL-G has a sharp positive-rescaling reversal threshold
## Finding

IMTL-G chooses coefficients \(\alpha_i\) whose sum is one so that the aggregate gradient has equal projections onto the normalized task gradients. Its defining paper proves that after independently rescaling the task gradients by positive factors, the new aggregate is collinear with the old one, and the main text describes this as an unchanged direction.

The sign of that collinearity factor is decisive.

Let
\[
g=\sum_{i=1}^{T}\alpha_i g_i,
\qquad
\sum_{i=1}^{T}\alpha_i=1,
\]
where the nonzero task gradients are linearly independent. Let
\[
u_i=\frac{g_i}{\lVert g_i\rVert_2}
\]
and suppose
\[
g^\top u_i=C
\]
for every task.

Scale the task gradients by arbitrary positive factors:
\[
g_i'=k_i g_i,
\qquad
k_i>0.
\]
The source construction in its scale-invariance theorem gives
\[
\alpha_i'
=
\frac{\alpha_i/k_i}
{\sum_j\alpha_j/k_j},
\]
and therefore, whenever the denominator is nonzero,
\[
\boxed{
g'
=
\lambda g,
\qquad
\lambda
=
\left(
\sum_i\frac{\alpha_i}{k_i}
\right)^{-1}.
}
\]

Thus same-orientation invariance for every positive scale vector is equivalent to
\[
\boxed{
\alpha_i\ge0
\quad\text{for every }i.
}
\]

Indeed, nonnegative coefficients make the denominator strictly positive. Conversely, if
\[
\alpha_j<0,
\]
scale only task \(j\) by a factor \(k>0\). Then
\[
\lambda(k)
=
\left(
1-\alpha_j+\frac{\alpha_j}{k}
\right)^{-1}.
\]
The denominator has the unique positive zero
\[
\boxed{
k_\star
=
-\frac{\alpha_j}{1-\alpha_j}
\in(0,1).
}
\]
Hence
\[
k>k_\star
\Longrightarrow
\lambda(k)>0,
\]
\[
k=k_\star
\Longrightarrow
\text{the normalized construction is singular},
\]
and
\[
0<k<k_\star
\Longrightarrow
\lambda(k)<0.
\]

So a negative IMTL-G coefficient does not merely change the magnitude response to task scaling: a sufficiently small positive rescaling of that task reverses the aggregate direction.

There is a fully explicit full-rank example. Put
\[
r=\frac1{\sqrt2},
\]
and take three unit gradients
\[
u_1=(r,0,r),
\qquad
u_2=(0,r,r),
\qquad
u_3=\left(\frac12,\frac12,r\right).
\]
They are linearly independent. With
\[
g_i=u_i,
\]
the IMTL-G equal-projection solution is
\[
\boxed{
\alpha_1=\alpha_2=1+\frac1{\sqrt2},
\qquad
\alpha_3=-1-\sqrt2.
}
\]
The aggregate is
\[
\boxed{
g=(0,0,r)
}
\]
and
\[
g^\top u_i=\frac12
\]
for all three tasks.

Now scale only the third gradient:
\[
g_3'=k g_3.
\]
The source scale-transformation formula becomes
\[
\boxed{
\lambda(k)
=
\frac1{
2+\sqrt2-(1+\sqrt2)/k
}.
}
\]
Its threshold is
\[
\boxed{
k_\star=\frac1{\sqrt2}.
}
\]

For every
\[
0<k<\frac1{\sqrt2},
\]
the three scaled gradients are still linearly independent, but
\[
\lambda(k)<0.
\]
Therefore
\[
(g')^\top u_i
=
\frac{\lambda(k)}2
<
0
\]
for every task. Since positive rescaling does not change the unit directions, the model update \(-g'\) is a first-order ascent direction for all three scaled task objectives.

At
\[
k=\frac1{\sqrt2},
\]
the equal-projection system with the coefficient-sum normalization becomes singular even though the three scaled gradients themselves remain linearly independent. On the two sides of this point the aggregate diverges with opposite orientation.

## Assumptions and scope

The theorem concerns the source closed-form IMTL-G construction with coefficient normalization
\[
\sum_i\alpha_i=1.
\]

All task-gradient scale factors are positive, so task-gradient directions themselves are unchanged.

The full-rank example uses nonzero linearly independent task gradients and therefore does not rely on the rank-deficient extension of IMTL-G introduced in later work.

The all-task ascent statement additionally uses the explicit example's positive original common projection
\[
C=\frac12.
\]

This finding concerns the instantaneous aggregate-gradient construction. It does not assert that an entire neural-network training run must diverge after a loss rescaling.

## Proof

The defining scale-transformation construction sets
\[
\alpha_i'
=
\frac{\alpha_i/k_i}{D},
\qquad
D=\sum_j\frac{\alpha_j}{k_j}.
\]
Therefore
\[
g'
=
\sum_i\alpha_i'k_i g_i
=
\frac1D
\sum_i\alpha_i g_i
=
\frac1Dg.
\]
This proves
\[
\lambda=D^{-1}.
\]

If every coefficient is nonnegative, then because the coefficients sum to one and every \(k_i\) is positive,
\[
D>0
\]
for every positive scale vector. Hence the aggregate orientation cannot reverse.

Conversely, suppose
\[
\alpha_j<0.
\]
Set all scale factors except the \(j\)-th to one. Then
\[
D(k)
=
1-\alpha_j+\frac{\alpha_j}{k}.
\]
It is strictly increasing on the positive half-line, tends to negative infinity as \(k\) tends to zero, and satisfies
\[
D(1)=1.
\]
Its unique zero is
\[
k_\star
=
-\frac{\alpha_j}{1-\alpha_j}.
\]
The three sign regimes follow immediately.

For the explicit example, direct substitution gives
\[
\sum_i\alpha_i=1
\]
and
\[
\sum_i\alpha_i u_i=(0,0,r).
\]
Each dot product with \(u_i\) is \(1/2\).

The scale denominator for the third task is
\[
D(k)
=
\alpha_1+\alpha_2+\frac{\alpha_3}{k}
=
2+\sqrt2-\frac{1+\sqrt2}{k}.
\]
Its zero is
\[
k_\star=\frac1{\sqrt2}.
\]
The determinant of the three scaled gradient rows is nonzero for every \(k>0\), including \(k=k_\star\), so task-gradient full rank is preserved. At the critical scale, however, the matrix appearing in the source normalized equal-projection closed form loses invertibility; the obstruction is the coefficient-sum normalization rather than loss of gradient rank.

For \(k<k_\star\),
\[
g'=\lambda(k)g
\]
has negative common normalized projection. The directional derivative of scaled task \(i\) along the descent step \(-g'\) is
\[
(k_i g_i)^\top(-g')
=
-k_i\lVert g_i\rVert_2 (u_i^\top g')
>
0,
\]
so all three scaled objectives increase to first order.

## Verification

The accompanying `verify.py` reconstructs the source IMTL-G closed form from the gradient-difference and normalized-gradient-difference matrices.

It checks the exact coefficient vector of the three-task example, full rank before and at the critical scaling, the singularity of the normalized equal-projection matrix at
\[
k=1/\sqrt2,
\]
the closed multiplier formula away from the threshold, and negative projections for scale factors below the threshold.

It also checks the general one-negative-coefficient threshold identity over a deterministic grid of coefficient values. These computations are transcription guards; the sign theorem is proved algebraically above.

## Relationship to prior work

Liu and coauthors define IMTL-G by requiring equal projections of the aggregate onto normalized task gradients and fixing the otherwise underdetermined solution by requiring the task coefficients to sum to one. Their main text states that arbitrary positive loss scaling leaves the aggregate-gradient direction unchanged. Appendix Theorem 2 constructs the scaled solution and proves that the new aggregate is linearly correlated with the old one through the factor
\[
\left(\sum_i\alpha_i/k_i\right)^{-1}.
\]
The proof does not establish that this factor is positive.

The same source explicitly reports that its closed-form variant removes the hard constraints
\[
\alpha_i>0
\]
and says only that positive coefficients occurred almost always in its experiments. Its appendix proves positivity in the special case where every pair of normalized task gradients has the same angle, not for general gradient configurations.

Quinton and Rey later formalize IMTL-G as a Jacobian aggregator. Their Appendix B.6 observes that a generalized IMTL-G is not linear under scaling and writes the corresponding normalization denominator explicitly. They also give a negative-weight conflict example for a rank-deficient Jacobian, while noting that the full-row-rank case appears non-conflicting.

The result here is not the already-known statement that IMTL-G is non-linear under scaling. It gives the exact sign condition for the source scaling factor and a linearly independent three-task configuration in which positive task rescaling reaches a finite singularity and then makes the full-rank source-form aggregate conflict with every task. This also shows that full row rank alone does not guarantee non-conflict.

Focused published-record searches for negative IMTL-G weights, scale singularities, orientation reversal, and full-rank conflict did not identify this full-rank threshold phenomenon.

## Limitations

The example is an instantaneous gradient configuration rather than a complete fixed-objective training trajectory.

The scale singularity depends on using the source coefficient-sum normalization. A modified method that enforces nonnegative weights or chooses another normalization can avoid this mechanism.

The later Jacobian-descent paper already establishes the broader fact that its generalized IMTL-G is not linear under scaling; the contribution here is the sharp sign threshold and full-rank reversal mechanism.

No empirical frequency is claimed for negative IMTL-G coefficients in modern training workloads.

## References

1. Liyang Liu, Yi Li, Zhanghui Kuang, Jing-Hao Xue, Yimin Chen, Wenming Yang, Qingmin Liao, and Wayne Zhang, “Towards Impartial Multi-task Learning,” ICLR 2021, OpenReview identifier `IMPnRXEWpvr`. The public under-review source belongs to the ICLR 2021 submission cycle whose full-paper submission date was 2020-10-02.
2. Pierre Quinton and Valérian Rey, “Jacobian Descent for Multi-Objective Optimization,” arXiv:2406.16232v1, 2024.
