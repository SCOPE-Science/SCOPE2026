# Same-model review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

The derivation was checked from two exact representations of the same
variance-gamma law: the difference of two equal-shape gamma variables gives the
zero CDF in terms of a symmetric beta CDF, while the Bessel-\(K\) density gives
the local positive-side mass needed to move from zero to the median.

The beta expansion gives
\[
\frac12-F_\kappa(0)
=
D_r\kappa^{-1/2}
\left(1-\frac{r+1}{6\kappa}+O(\kappa^{-2})\right),
\]
and the identity \(D_r=(r-1)c_r\) for \(r>1\) causes the leading cancellation
at the limiting median \(r-1\). The next Bessel term changes character at
\(\nu=(r-1)/2=1\), producing the second threshold \(r=3\). The signs of all
corrections agree with the strict inequality
\(\operatorname{Med}(V_{r,\theta,\sigma})>(r-1)\theta\) for \(r>1\).

At \(r=2\), the general \(1<r<3\) formula gives \(A_2=1/2\), matching the direct
large-scale expansion of the exact asymmetric-Laplace median. Numerical
integration of the published variance-gamma density and independent root-finding
for the median agree with the predicted constants in representative cases on
both sides of both thresholds. The verification code and outputs are included.

No numerical experiment is used in place of the analytic proof.

## Originality

The originality assessment is **to the best of our knowledge**.

The closest source is Gaunt and Ouimet (2026), arXiv:2609.20212. Its Corollary
2.3 proves strict monotonicity in the scale parameter, the limit
\[
(r-1)\theta\quad(r>1),\qquad 0\quad(r\le1),
\]
and global bounds. The proof treats \(r<1\) and \(r=1\) separately in establishing
the zero limit, but it does not state a convergence rate, a sharp constant, or a
second threshold at \(r=3\).

Fischer, Gaunt and Sarantsev (2025) give the density, the local
power/logarithmic/finite density trichotomy at \(r=1\), the exact \(r=2\)
median, and the Wishart marginal representation. Their median discussion states
that general exact closed forms are unavailable and does not give the
large-scale rates here. Gaunt (2022) treats products and sums of correlated
zero-mean normal variables and their medians but likewise does not state these
small-correlation expansions.

Literature checks also covered synonymous formulations involving generalized
Laplace distributions, products of correlated normals, variance-gamma quantiles,
large-scale medians, and small-correlation product-normal medians. No matching
five-regime theorem or \(r=3\) median transition was located.

A material residual risk is S. Kotz, T. J. Kozubowski and K. Podgórski,
*The Laplace Distribution and Generalizations* (2001),
DOI 10.1007/978-1-4612-0173-1. Bibliographic information and the specific
results cited from it by the 2025 review were inspected, but the complete book
was not checked for an equivalent asymptotic quantile calculation under a
generalized-Laplace parametrization. This is the source most plausibly capable
of narrowing the originality claim.

Accordingly, novelty is restricted to the sharp large-scale median asymptotics,
the explicit two-threshold classification with the \(r=3\) logarithmic
resonance, and the displayed Wishart small-correlation consequences.

## Value

The result sharpens a current limit theorem into an explicit asymptotic
classification over the full shape range. The second threshold \(r=3\) is not
visible from the limiting median alone, and the exact constants distinguish
three qualitatively different convergence mechanisms above \(r=1\). The
Wishart corollary gives the transition a direct statistical interpretation for
off-diagonal covariance entries.

## Limitations

The expansions are pointwise in fixed \(r\) and fixed \(\theta>0\), not uniform
through \(r=1\) or \(r=3\). No nonasymptotic error bound is claimed. The
univariate statements do not address multivariate quantiles or dependence among
Wishart entries. Older generalized-Laplace literature remains a residual
originality risk as described above.
