# Adam-GC has a sharp dimension-dependent mean-drift envelope
## Finding

Gradient Centralization (GC) projects each weight-gradient vector onto the zero-mean hyperplane. For SGD and SGDM, the defining paper proves that this projection preserves the mean of the weight vector throughout training.

The same invariant does not automatically survive Adam's coordinatewise adaptive denominator.

Consider one weight vector
\[
w\in\mathbb R^d,
\qquad
d\ge2,
\]
with Adam moments initialized at zero. Let
\[
h\ne0
\]
be the first centralized gradient, so
\[
\sum_{i=1}^d h_i=0.
\]
Assume no weight decay and use the source Adam denominator
\[
\sqrt{\widehat v}+\varepsilon,
\qquad
\varepsilon>0.
\]

At the first step, bias correction cancels both moment coefficients:
\[
\widehat m=h,
\qquad
\widehat v=h\odot h.
\]
Hence the parameter update is exactly
\[
\boxed{
\Delta w_i
=
-\alpha
\frac{h_i}{|h_i|+\varepsilon}.
}
\]

Writing
\[
\bar w=\frac1d\sum_iw_i,
\]
the induced weight-mean drift is
\[
\boxed{
\Delta\bar w
=
-\frac{\alpha}{d}
\sum_{i=1}^d
\frac{h_i}{|h_i|+\varepsilon}.
}
\]

For
\[
d=2,
\]
every nonzero centered gradient has the form
\[
h=(a,-a),
\]
so the two adaptive update components cancel exactly and
\[
\boxed{\Delta\bar w=0.}
\]

For every
\[
d\ge3,
\]
the sharp dimension-only envelope is
\[
\boxed{
|\Delta\bar w|
<
\alpha\frac{d-2}{d},
\qquad
\sup_h|\Delta\bar w|
=
\alpha\frac{d-2}{d},
}
\]
where the supremum is over nonzero finite centered gradients.

A sharp family is
\[
h(a)
=
(a,\ldots,a,-(d-1)a),
\qquad
a>0.
\]
For this family,
\[
\sum_i
\frac{h_i}{|h_i|+\varepsilon}
=
(d-1)\frac{a}{a+\varepsilon}
-
\frac{(d-1)a}{(d-1)a+\varepsilon},
\]
which tends to
\[
d-2
\]
as
\[
a/\varepsilon\to\infty.
\]

Thus the projected-gradient weight constraint proved for SGD/SGDM is not an invariant of source-form Adam-GC. In high dimension, the first adaptive step can move the weight mean by almost one full learning rate even though the centralized gradient itself has mean exactly zero.

The official implementation contains an exact structural repair. Its GC2 variants form the adaptive Adam update first and then centralize that final update before applying it. For every weight vector to which this final-delta centralization is applied,
\[
\boxed{
\sum_i\Delta w_i=0
}
\]
at every step, so the weight mean is preserved exactly.

## Assumptions and scope

The sharp envelope concerns the first source-form Adam-GC step with zero initial first and second moments, positive denominator regularizer \(\varepsilon\), no weight decay, and one centralized weight vector.

The result is independent of the Adam moment coefficients because the first-step bias corrections cancel them.

The statement concerns the affine mean constraint of the parameter update, not whether Adam-GC improves training loss or generalization.

The exact every-step repair statement applies to implementations that centralize the final preconditioned update itself, as in the official GC2 variants, for the tensors or vectors on which that operation is executed.

No claim is made that ordinary Adam-GC always exhibits near-maximal drift; the theorem gives the exact formula and sharp worst-case envelope.

## Proof

Define
\[
\phi(x)=\frac{x}{x+\varepsilon},
\qquad
x\ge0.
\]
At the first Adam-GC step,
\[
m=(1-\beta_1)h,
\qquad
v=(1-\beta_2)h\odot h.
\]
After bias correction,
\[
\widehat m=h,
\qquad
\widehat v=h\odot h,
\]
which proves the update and mean-drift formulas.

It remains to prove the sharp envelope. Split the nonzero components of \(h\) into positive magnitudes
\[
x_1,\ldots,x_p
\]
and negative magnitudes
\[
y_1,\ldots,y_n.
\]
Because \(h\) is centered,
\[
\sum_{i=1}^p x_i
=
\sum_{j=1}^n y_j
=
A>0.
\]

Assume without loss of generality that
\[
S
=
\sum_i\frac{h_i}{|h_i|+\varepsilon}
\ge0.
\]
Then
\[
S
=
\sum_{i=1}^p\phi(x_i)
-
\sum_{j=1}^n\phi(y_j).
\]

The function \(\phi\) is increasing and concave on the nonnegative half-line with \(\phi(0)=0\). Therefore
\[
\sum_{i=1}^p\phi(x_i)
\le
p\phi(A/p)
\]
by Jensen's inequality, while
\[
\sum_{j=1}^n\phi(y_j)
\ge
\phi(A).
\]
Consequently
\[
S
\le
p\phi(A/p)-\phi(A)
=
(p-1)
\frac{A^2}{(A+p\varepsilon)(A+\varepsilon)}
<
p-1.
\]
Since at least one component has the opposite sign,
\[
p\le d-1,
\]
and hence
\[
S<d-2.
\]
Applying the same argument to \(-h\) gives
\[
|S|<d-2.
\]

The sharp family with \(d-1\) equal positive entries and one balancing negative entry makes
\[
|S|\to d-2,
\]
proving the supremum.

Finally, centralizing the final adaptive update replaces any proposed update vector \(\delta\) by
\[
\delta-\frac1d\mathbf1\mathbf1^\top\delta,
\]
whose components sum to zero identically. This proves the exact GC2 mean-preservation statement.

## Verification

The accompanying `verify.py` reconstructs the first Adam-GC step from zero moments for many centered gradients and confirms the closed mean-drift formula.

It numerically checks the sharp bound in dimensions from \(2\) through \(64\), verifies that the explicit sharp family approaches
\[
\alpha(d-2)/d,
\]
and confirms exact mean preservation after final-delta centralization.

The computations are transcription guards. The infinite sharp envelope is proved analytically above.

## Relationship to prior work

Yong, Huang, Hua, and Zhang define Gradient Centralization by projecting each gradient vector onto the zero-mean hyperplane. Their paper gives separate SGDM and Adam algorithms. In its theoretical weight-space analysis, it explicitly follows SGD with GC and proves that the projected update keeps the weight-vector mean fixed, yielding an affine constrained optimization interpretation.

The same paper's Adam algorithm centralizes the raw gradient before updating Adam's first and second moments and then performs the usual coordinatewise adaptive division. The inspected paper does not derive a corresponding Adam weight-mean invariant.

The official repository makes the implementation distinction explicit. Its ordinary `Adam_GC` centralizes the gradient before moment accumulation and then applies the adaptive update directly. Its `Adam_GC2` and `Adam_GCC2` variants instead centralize the final adaptive update before changing the parameter. The repository documentation says that preserving the weight-vector mean usually works better for adaptive learning-rate methods.

Sadu, Dubey, and Sreeja later propose Moment Centralization for adaptive optimizers, motivated by explicitly forcing the first-order moment to have zero mean. Their AdamMC algorithm still divides the centralized first moment coordinatewise by a second-moment denominator. Their inspected analysis does not state the final parameter-mean drift envelope derived here.

Thus the broad concern that adaptive optimization interacts nontrivially with centralization is not new. The finding here is narrower: the exact first-step Adam-GC mean-drift formula, the sharp dimension-only supremum, the special two-dimensional cancellation, and the \(d=3\) onset.

Focused published-record searches for Adam-GC mean drift, affine-constraint failure, final-update centralization, and dimension-dependent bounds did not identify an implication-equivalent theorem.

## Limitations

The sharp theorem is a first-step result. Later Adam states can have more complicated moment histories.

Weight decay and other parameter-changing terms are excluded from the sharp first-step envelope.

The bound is a worst-case statement over centralized gradients; it does not estimate typical neural-network drift.

The official GC2 repair is an implementation fact already reflected in the repository; the new contribution is the exact drift law and sharp envelope for the source Adam-GC ordering.

## References

1. Hongwei Yong, Jianqiang Huang, Xiansheng Hua, and Lei Zhang, “Gradient Centralization: A New Optimization Technique for Deep Neural Networks,” arXiv:2004.01461v1, first submitted 2020-04-03; ECCV 2020.
2. Official Gradient Centralization implementation, repository revision `ed2a608ccdbb731301e00bf838c83821df1b8d70`, including `Adam_GC`, `Adam_GC2`, and `Adam_GCC2`.
3. Sumanth Sadu, Shiv Ram Dubey, and S. R. Sreeja, “Moment Centralization based Gradient Descent Optimizers for Convolutional Neural Networks,” arXiv:2207.09066v1, 2022.
