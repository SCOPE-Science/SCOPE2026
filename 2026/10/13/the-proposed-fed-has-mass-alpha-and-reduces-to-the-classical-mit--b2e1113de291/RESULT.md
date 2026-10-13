# The proposed FED has mass \(\alpha\) and reduces to the classical Mittag-Leffler law after normalization
## Finding
The 2026 source proposes a fractional exponential distribution (FED) for
\[
0<\alpha\le1,\qquad \lambda>0,
\]
with density
\[
f_{\rm pub}(x)
=
\alpha\lambda x^{\alpha-1}E_{\alpha,\alpha}(-\lambda x^\alpha),
\qquad x>0.
\]
Here
\[
E_{\alpha,\beta}(z)
=
\sum_{k=0}^{\infty}\frac{z^k}{\Gamma(\alpha k+\beta)}.
\]

The published expression is normalized only in the classical case \(\alpha=1\). The exact derivative identity is
\[
\boxed{
-\frac{d}{dx}E_\alpha(-\lambda x^\alpha)
=
\lambda x^{\alpha-1}E_{\alpha,\alpha}(-\lambda x^\alpha).
}
\]
Therefore
\[
\boxed{
\int_0^\infty f_{\rm pub}(x)\,dx=\alpha.
}
\]
For every genuinely fractional case
\[
0<\alpha<1,
\]
Eq. (6.17) of the source is a subdensity rather than a probability density.

The source's Eq. (6.20) is incompatible with Eq. (6.17) for the same reason. If the published density is integrated from \(x\) to infinity, one obtains
\[
\boxed{
\int_x^\infty f_{\rm pub}(t)\,dt
=
\alpha E_\alpha(-\lambda x^\alpha),
}
\]
not the stated survival
\[
E_\alpha(-\lambda x^\alpha).
\]
At \(x=0\), this inconsistency is the normalization defect itself.

The unique multiplicative repair is
\[
\boxed{
f_*(x)
=
\lambda x^{\alpha-1}E_{\alpha,\alpha}(-\lambda x^\alpha).
}
\]
Its survival is
\[
\boxed{
S_*(x)=E_\alpha(-\lambda x^\alpha).
}
\]
This is not a new distributional family: it is exactly the classical first-type Mittag-Leffler distribution, with scale
\[
\tau=\lambda^{-1/\alpha}.
\]
Indeed, the standard Mittag-Leffler density
\[
\frac{x^{\alpha-1}}{\tau^\alpha}
E_{\alpha,\alpha}\!\left[-(x/\tau)^\alpha\right]
\]
becomes \(f_*\) after this substitution.

The correction also sharpens the moment statement. For \(0<\alpha<1\), the source itself gives
\[
S_*(x)
\sim
\frac{1}{\lambda\Gamma(1-\alpha)}x^{-\alpha}.
\]
Hence for every real \(r>0\),
\[
\boxed{
\mathbb E[X^r]<\infty
\quad\Longleftrightarrow\quad
r<\alpha.
}
\]
Thus no positive integer moment exists when \(0<\alpha<1\). In particular,
\[
\boxed{\mathbb E[X]=\infty}
\]
throughout the genuinely fractional regime.

This contradicts the presentation of Eq. (6.19) as the \(m\)-th moments for
\[
m=1,2,\ldots,
\]
and the subsequent suggestion that lower-order moments are finite. The displayed Eq. (6.19) also integrates only to the finite upper endpoint \(\alpha\), even though the stated support is \([0,\infty)\), so it cannot equal a raw moment of the proposed law.

Finally, the likelihood must also be repaired. The source's Eq. (6.25) includes the term
\[
n\log\alpha
\]
coming from the erroneous multiplicative factor. For the normalized density \(f_*\), the correct log-likelihood is the displayed likelihood minus
\[
\boxed{n\log\alpha.}
\]
This changes estimation of \(\alpha\); it is not a harmless constant with respect to the model parameters.

## Assumptions and scope
The finding concerns the FED introduced in Sections 6.2–6.3 of the source, with \(0<\alpha\le1\) and \(\lambda>0\).

At \(\alpha=1\), the factor \(\alpha\) equals one and the construction reduces correctly to the exponential density
\[
\lambda e^{-\lambda x}.
\]
The defect is therefore specific to the genuinely fractional interval \(0<\alpha<1\).

The moment criterion concerns the normalized repair \(f_*\), equivalently the classical first-type Mittag-Leffler law. The published unnormalized expression does not itself define a probability distribution for \(\alpha<1\).

The NGDTM results for the differential-equation examples outside the FED construction are not assessed here.

## Proof
Starting from the series
\[
E_\alpha(-\lambda x^\alpha)
=
\sum_{k=0}^\infty
\frac{(-\lambda)^k x^{\alpha k}}{\Gamma(\alpha k+1)},
\]
termwise differentiation for \(x>0\) gives
\[
\frac{d}{dx}E_\alpha(-\lambda x^\alpha)
=
\sum_{k=1}^\infty
\frac{\alpha k(-\lambda)^k x^{\alpha k-1}}{\Gamma(\alpha k+1)}.
\]
Using
\[
\Gamma(\alpha k+1)=\alpha k\,\Gamma(\alpha k)
\]
and shifting the index yields
\[
\frac{d}{dx}E_\alpha(-\lambda x^\alpha)
=
-\lambda x^{\alpha-1}
E_{\alpha,\alpha}(-\lambda x^\alpha).
\]

For \(0<\alpha\le1\),
\[
E_\alpha(0)=1
\]
and
\[
E_\alpha(-\lambda x^\alpha)\to0
\qquad(x\to\infty).
\]
Therefore
\[
\int_0^\infty
\lambda x^{\alpha-1}E_{\alpha,\alpha}(-\lambda x^\alpha)\,dx
=1,
\]
while multiplication by the source's extra factor \(\alpha\) gives total mass \(\alpha\).

The survival formula follows from integrating the same derivative identity from \(x\) to infinity.

For the moment criterion, use the nonnegative tail identity
\[
\mathbb E[X^r]
=
r\int_0^\infty x^{r-1}S_*(x)\,dx,
\qquad r>0,
\]
with the value \(+\infty\) allowed. The source states the large-\(x\) equivalent
\[
S_*(x)
\sim
\frac{x^{-\alpha}}{\lambda\Gamma(1-\alpha)}.
\]
Hence the moment tail integrand is asymptotic to a positive constant times
\[
x^{r-1-\alpha}.
\]
The integral converges exactly when
\[
r-1-\alpha<-1,
\]
that is,
\[
r<\alpha.
\]
At \(r=\alpha\), divergence is logarithmic; for \(r>\alpha\), it is polynomial.

The likelihood correction is immediate because
\[
f_{\rm pub}(x)=\alpha f_*(x).
\]
For a sample of size \(n\), the published product density is therefore \(\alpha^n\) times the normalized likelihood, so the log-likelihood differs by \(n\log\alpha\).

## Verification
The bundled checker verifies the derivative identity coefficient-by-coefficient from the defining Mittag-Leffler series.

For the exactly tractable case \(\alpha=1/2\), it uses
\[
E_{1/2}(-\lambda\sqrt{x})
=
e^{\lambda^2x}\operatorname{erfc}(\lambda\sqrt{x})
\]
to confirm that the published density has total mass \(1/2\), while the corrected density has mass one.

It also checks the heavy-tail constant
\[
S_*(x)x^{1/2}
\to
\frac{1}{\lambda\sqrt\pi}
\]
and the resulting divergence of the truncated mean.

These computations are consistency checks. The normalization and moment conclusions follow analytically from the derivative identity and the published survival asymptotic.

## Relationship to prior work
The 2026 source explicitly calls Eq. (6.17) a new fractional exponential probability density and states that its integral is one for all \(0<\alpha\le1\). It then gives Eq. (6.20) as the survival function and develops moments and likelihood inference from the same expression.

However, the source's density differs by exactly a factor \(\alpha\) from the derivative of its own stated survival function. The inconsistency is visible directly between Eqs. (6.17) and (6.20).

The normalized repair is already classical. Haubold, Mathai, and Saxena's 2011 review has a dedicated section on the Mittag-Leffler statistical distribution, obtained by differentiating a survival/CDF expressed through \(E_\alpha\), and records the associated density and Laplace-transform theory. Contemporary software documentation likewise gives the first-type Mittag-Leffler density as
\[
x^{\alpha-1}E_{\alpha,\alpha}[-(x/\tau)^\alpha]/\tau^\alpha.
\]
Thus the repaired FED is a scale-parametrized form of an established Mittag-Leffler distribution rather than a new probability family.

Focused searches using the exact DOI, FED name, normalization factor, Eqs. (6.17)/(6.20), and Mittag-Leffler equivalence did not locate a published corrigendum or another source already diagnosing this 2026 normalization error.

## Limitations
The finding does not reassess the NGDTM convergence and uniqueness theorems for fractional differential equations.

No numerical maximum-likelihood study is rerun. The result establishes the analytic likelihood correction; its finite-sample estimator consequences are left open.

The complete fractional-moment formula for \(0<r<\alpha\) is not needed here; only the sharp existence threshold is established from the tail.

## References
1. A. Abuualshaikh, M. Z. Aldrabseh, T. S. Alshammari, K. A. Rashedi, and K. M. K. Alshammari, “A new generalized differential transform method for fractional ODEs with statistical applications,” AIMS Mathematics 11 (2026), 9541–9562. DOI: 10.3934/math.2026395.
2. H. J. Haubold, A. M. Mathai, and R. K. Saxena, “Mittag-Leffler functions and their applications,” Journal of Applied Mathematics (2011), Article ID 298628. DOI: 10.1155/2011/298628.
