# TAdam has a sharp block-size outlier response law
## Finding

TAdam replaces Adam's first-moment exponential average by an incremental Student-\(t\) mean estimate. The defining source states that gradients with large Mahalanobis distance are down-weighted and later warns that a very large whole-vector block can under-detect a sparse aberrant component.

At the natural inlier fixed point of TAdam's pseudo-count, both effects admit an exact response law.

Consider a TAdam block of dimension
\[
d\ge1,
\]
degrees of freedom
\[
\nu>0,
\]
and first-momentum parameter
\[
\frac12<\beta<1.
\]
Suppose the previous robust mean is
\[
m=g_0,
\]
and define the positive diagonal scale
\[
V=\operatorname{diag}(v+\varepsilon).
\]

For an exact inlier \(g=g_0\), the source Student-\(t\) weight is
\[
w_0=\frac{\nu+d}{\nu}.
\]
The source pseudo-count recurrence is
\[
W^+
=
\frac{2\beta-1}{\beta}W+w.
\]
Under repeated exact inliers it converges to
\[
\boxed{
W_\star
=
\frac{\beta(\nu+d)}
{\nu(1-\beta)}.
}
\]
At this state,
\[
\frac{w_0}{W_\star+w_0}
=
1-\beta,
\]
so an inlier is blended with exactly Adam's usual first-momentum coefficient.

Now present one gradient
\[
g=g_0+\delta
\]
and define its squared Mahalanobis distance from the previous robust mean by
\[
D=\delta^\top V^{-1}\delta.
\]
The source weight is
\[
w(D)=\frac{\nu+d}{\nu+D}.
\]
Substitution into the source first-moment update gives
\[
\boxed{
m^+-m
=
(1-\beta)
\frac{\nu}{\nu+\beta D}
\,\delta.
}
\]

Ordinary Adam, from the same first-moment state, would contribute
\[
(1-\beta)\delta.
\]
Therefore the exact relative TAdam attenuation is
\[
\boxed{
R_{\rm rel}(D)
=
\frac{\nu}{\nu+\beta D}.
}
\]

This response is strictly decreasing in \(D\). In the natural Mahalanobis norm, however, the actual mean displacement has the redescending profile
\[
\boxed{
\lVert m^+-m\rVert_{V^{-1}}
=
(1-\beta)
\frac{\nu\sqrt D}{\nu+\beta D}.
}
\]
It tends to zero for arbitrarily remote outliers. Its unique maximum occurs at
\[
\boxed{
D_\star=\frac{\nu}{\beta},
}
\]
and the sharp gross-displacement bound is
\[
\boxed{
\lVert m^+-m\rVert_{V^{-1}}
\le
\frac{1-\beta}{2}
\sqrt{\frac{\nu}{\beta}}.
}
\]

The source recommends
\[
\nu=d
\]
as a default. Suppose an outlier is supported on \(k\) block coordinates and has the same standardized magnitude \(z\) on each active coordinate:
\[
\frac{|\delta_j|}{\sqrt{V_{jj}}}=|z|.
\]
Then
\[
D=kz^2,
\]
so
\[
R_{\rm rel}
=
\frac{d}{d+\beta kz^2}.
\]
Consequently,
\[
\boxed{
R_{\rm rel}\le\frac12
\iff
|z|\ge
\sqrt{\frac{d}{\beta k}}.
}
\]

For a dense outlier with \(k=d\), the half-attenuation threshold is
\[
|z|\ge\frac1{\sqrt\beta},
\]
independent of dimension. For a one-coordinate outlier with \(k=1\), it is
\[
|z|\ge\sqrt{\frac d\beta}.
\]
Thus sparse aberrations become progressively harder to suppress when a larger parameter block is treated as one Student-\(t\) sample.

At the source default
\[
\beta=0.9,
\]
the sharp maximum displacement under \(\nu=d\) is approximately
\[
0.0527046\sqrt d,
\]
and the one-coordinate half-attenuation threshold is approximately
\[
1.05409\sqrt d.
\]

## Assumptions and scope

The theorem concerns the source TAdam first-momentum update at the exact fixed point of its pseudo-count under repeated identical inliers.

The diagonal scale \(V\) is frozen while the single outlier's first-momentum contribution is evaluated. This matches the source outlier weight, which uses the previous second-moment state.

The statement is about the first-momentum robustness mechanism. TAdam's second moment is updated separately, so the theorem is not a complete one-step parameter-update bound.

The restriction
\[
\beta>\frac12
\]
keeps the source pseudo-count decay coefficient nonnegative and covers its default \(\beta=0.9\).

The dimension law concerns the source default choice \(\nu=d\). Other degrees-of-freedom choices follow from the general formulas above.

## Proof

Let
\[
C=\nu+d.
\]
For repeated exact inliers,
\[
D=0
\]
and
\[
w_0=\frac C\nu.
\]
The pseudo-count fixed-point equation is
\[
W_\star
=
\frac{2\beta-1}{\beta}W_\star+w_0.
\]
Since
\[
1-\frac{2\beta-1}{\beta}
=
\frac{1-\beta}{\beta},
\]
one obtains
\[
W_\star
=
\frac{\beta C}{\nu(1-\beta)}.
\]

For a new displacement \(\delta\), the Student-\(t\) weight is
\[
w(D)=\frac C{\nu+D}.
\]
The source first-moment update gives
\[
m^+-m
=
\frac{w(D)}{W_\star+w(D)}\delta.
\]
Substituting the two expressions and cancelling \(C\) gives
\[
\frac{w(D)}{W_\star+w(D)}
=
\frac{\nu(1-\beta)}
{\nu+\beta D}.
\]
This proves the exact attenuation law.

The Mahalanobis norm is therefore
\[
\Phi(D)
=
(1-\beta)
\frac{\nu\sqrt D}{\nu+\beta D}.
\]
Writing
\[
y=\sqrt D,
\]
the nonconstant part is
\[
\frac{y}{\nu+\beta y^2}.
\]
Its derivative is proportional to
\[
\nu-\beta y^2,
\]
so the unique maximum occurs at
\[
y^2=\nu/\beta.
\]
Substitution yields
\[
\Phi_{\max}
=
\frac{1-\beta}{2}
\sqrt{\frac\nu\beta}.
\]

For the default \(\nu=d\) and a \(k\)-coordinate standardized outlier,
\[
D=kz^2.
\]
Solving
\[
\frac{d}{d+\beta kz^2}\le\frac12
\]
gives the stated threshold.

## Verification

The accompanying `verify.py` reconstructs the source pseudo-count and Student-\(t\) first-momentum update.

It checks convergence of the exact-inlier pseudo-count to \(W_\star\), exact recovery of Adam's coefficient on inliers, equality of the closed outlier attenuation formula over randomized parameters, the unique Mahalanobis maximum, and the sparse-versus-dense half-attenuation thresholds.

The computations are transcription guards. The sharp bound and dimension law are proved algebraically above.

## Relationship to prior work

Ilboudo, Kobayashi, and Sugimoto introduce TAdam by replacing Adam's first-moment EMA with an incremental Student-\(t\) mean estimate. Their source weight is
\[
w=\frac{\nu+d}{\nu+D},
\]
where \(D\) is a squared Mahalanobis distance. They explain qualitatively that large-\(D\) gradients are down-weighted and that normal gradients are up-weighted.

The later journal treatment generalizes the mechanism as \(t\)-momentum. It explicitly discusses parameter-wise, block-wise, and whole-vector variants and warns that the whole-vector variant can underestimate a single aberrant component because \(d\) is large and the Mahalanobis distance may not exceed that scale.

Those qualitative statements are prior work. The inspected sources do not give the exact pseudo-count-calibrated response
\[
\nu/(\nu+\beta D),
\]
the sharp redescending displacement maximum at
\[
D=\nu/\beta,
\]
or the sparse-support threshold
\[
|z|=\sqrt{d/(\beta k)}
\]
under the source default \(\nu=d\).

Focused published-record searches for bounded TAdam influence, Mahalanobis displacement maxima, and block-size outlier thresholds did not identify an implication-equivalent result.

## Limitations

The theorem isolates one outlier after the pseudo-count has equilibrated on exact inliers.

The previous diagonal second-moment state is treated as fixed while measuring the outlier's first-momentum influence.

The result does not classify sequences of many consecutive outliers or the full parameter trajectory.

The source default \(\nu=d\) is used only for the block-size specialization; the general response formulas hold for arbitrary positive \(\nu\).

## References

1. Wendyam Eric Lionel Ilboudo, Taisuke Kobayashi, and Kenji Sugimoto, “TAdam: A Robust Stochastic Gradient Optimizer,” arXiv:2003.00179v1, first submitted 2020-02-29.
2. Wendyam Eric Lionel Ilboudo, Taisuke Kobayashi, and Kenji Sugimoto, “Robust Stochastic Gradient Descent With Student-t Distribution Based First-Order Momentum,” IEEE Transactions on Neural Networks and Learning Systems, DOI `10.1109/TNNLS.2020.3041755`.
