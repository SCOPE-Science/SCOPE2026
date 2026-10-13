# The GGWP critical second-moment boundary invalidates four Table 1 rows
## Finding
For the gamma-generated Weibull–Pareto (GGWP) distribution with
\[
a>0,\qquad b>0,\qquad \beta>0,\qquad \theta>0,
\]
the 2026 source proves the survival equivalent
\[
\Pr(T>t)
\sim
C\,t^{-1/\beta},
\]
where
\[
C=
\frac{a e^{-1/b}}{b(1-e^{-1/b})}\,
\theta^{1/\beta}
>0.
\]
Consequently, for every real \(r>0\),
\[
\boxed{
\mathbb E[T^r]<\infty
\quad\Longleftrightarrow\quad
r<\frac1\beta.
}
\]
At the critical boundary
\[
\beta=\frac1r,
\]
the moment does not remain finite: it diverges logarithmically.

The most important published boundary case is
\[
\beta=\frac12.
\]
Then
\[
\Pr(T>t)\sim C t^{-2}.
\]
Therefore
\[
\mathbb E[T]<\infty,
\qquad
\boxed{\mathbb E[T^2]=\infty},
\]
and hence
\[
\boxed{\operatorname{Var}(T)=\infty}.
\]
As a result, the usual finite coefficient of variation, standardized skewness, and standardized kurtosis are not defined.

This corrects two mutually inconsistent parts of the source. Its moment theorem and corollary use the strict conditions
\[
\text{mean finite}\iff\beta<1,
\qquad
\text{variance finite}\iff\beta<\frac12,
\]
but the prose immediately following the moment discussion states that for
\[
\beta=0.5
\]
all moments exist. Table 1 then reports finite variance, skewness, kurtosis, and coefficient of variation in four rows having
\[
\beta=0.5.
\]

Those four affected parameter rows are
\[
(a,b,\beta,\theta)
=
(0.64,0.8,0.5,0.8),
\]
\[
(0.80,0.8,0.5,0.8),
\]
\[
(1.60,0.8,0.5,0.8),
\]
and
\[
(2.80,0.8,0.5,0.8).
\]
Their reported means are compatible with the theorem because the first moment is finite at \(\beta=0.5\). Their finite variance, coefficient of variation, skewness, and kurtosis entries are not population quantities of the stated GGWP law.

More generally, if \(m\) is a positive integer and
\[
\beta=\frac1m,
\]
then the moments of orders \(1,\ldots,m-1\) are finite while the \(m\)-th moment diverges logarithmically.

## Assumptions and scope
The claim uses the GGWP parameterization and tail constant printed in the source. It concerns population moments, not finite sample moments.

The usual coefficient of variation requires a finite variance. The usual standardized skewness and kurtosis require the relevant central moments and a finite, nonzero variance. Since the second raw moment already diverges at \(\beta=1/2\), these standardized population summaries are unavailable regardless of the finiteness of any numerical expression produced by truncation or finite-range quadrature.

No claim is made that the source's likelihood inference, simulation estimators, or data fits are invalid. The correction is confined to the moment boundary and the derived descriptive entries at that boundary.

## Proof
For a nonnegative random variable and \(r>0\),
\[
\mathbb E[T^r]
=
r\int_0^\infty
t^{r-1}\Pr(T>t)\,dt,
\]
with the value \(+\infty\) allowed.

The source's exact tail theorem gives
\[
\Pr(T>t)
\sim
C t^{-1/\beta},
\qquad C>0.
\]
Thus
\[
t^{r-1}\Pr(T>t)
\sim
C t^{r-1-1/\beta}.
\]
The tail integral converges exactly when
\[
r-1-\frac1\beta<-1,
\]
equivalently
\[
r<\frac1\beta.
\]

At equality,
\[
r=\frac1\beta,
\]
the integrand is asymptotic to
\[
\frac{rC}{t},
\]
so
\[
r\int_R^M t^{r-1}\Pr(T>t)\,dt
\sim
rC\log(M/R)
\]
and diverges as \(M\to\infty\). This proves the critical logarithmic divergence.

For \(\beta=1/2\), one has \(1/\beta=2\). Hence the first moment is finite but the second moment is infinite. Since
\[
\operatorname{Var}(T)
=
\mathbb E[T^2]-\{\mathbb E[T]\}^2,
\]
the variance is infinite.

The coefficient of variation
\[
\frac{\sqrt{\operatorname{Var}(T)}}{\mathbb E[T]}
\]
is therefore not a finite population quantity. Likewise, the conventional standardized skewness and kurtosis require finite second and higher central moments, so they are undefined.

## Verification
The included checker evaluates the exact GGWP survival from the published CDF at high precision for all four affected Table 1 parameter rows.

At \(\beta=1/2\), it verifies numerically that
\[
t^2\Pr(T>t)\to C.
\]
It also prints the coefficient
\[
2C
\]
of the logarithmic divergence of the truncated second-moment tail:
\[
2\int_R^M t\,\Pr(T>t)\,dt
\sim
2C\log(M/R).
\]

These calculations are consistency checks. The divergence is proved analytically from the positive tail equivalent and does not rely on numerical truncation.

## Relationship to prior work
Chesneau and Sadok introduce the GGWP distribution and explicitly prove its power-law survival asymptotic. Their theorem states that the moment of order \(r\) exists exactly when
\[
r<1/\beta.
\]
Their following corollary correctly gives the strict variance condition
\[
\beta<1/2.
\]
However, the subsequent prose says that at \(\beta=0.5\) all moments exist, and Table 1 reports finite second- and higher-moment summaries at that same boundary. The present result resolves this internal inconsistency by evaluating the theorem at its critical equality case.

The correction uses no alternative parameterization and no approximation to the model. It is the direct consequence of the source's own asymptotic constant being strictly positive.

Focused searches using the exact DOI, GGWP name, critical \(\beta=1/2\) boundary, variance, skewness, kurtosis, and correction terminology did not locate a published corrigendum or another source identifying these four rows.

## Limitations
This finding does not independently recompute every numerical entry in Table 1. It establishes that four classes of reported population summaries cannot be finite in the four \(\beta=0.5\) rows.

The result does not challenge the rows with \(\beta<1/2\) on moment-existence grounds. It also does not assess numerical accuracy of finite summaries in parameter regimes where the required moments genuinely exist.

The logarithmic divergence statement is first-order; no finite-part renormalization is proposed.

## References
1. C. Chesneau and I. Sadok, “A unified gamma-generated Weibull–Pareto distribution for heavy-tailed and skewed data with applications to medicine, engineering, and environment,” AIMS Mathematics 11 (2026), 23629–23662. DOI: 10.3934/math.2026952.
