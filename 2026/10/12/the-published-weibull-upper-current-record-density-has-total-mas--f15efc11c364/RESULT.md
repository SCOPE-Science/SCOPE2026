# The published Weibull upper-current-record density has total mass \((2/3)^m\), not one
## Finding
Let \(X\) have the two-parameter Weibull distribution
\[
F(x)=1-\exp\!\left[-(x/\lambda)^k\right],\qquad x\ge 0,\quad k,\lambda>0,
\]
and let \(UC_m\) be the \(m\)-th upper current record, with integer \(m>1\). Put
\[
t=(x/\lambda)^k
\]
and let \(P(m,z)\) denote the regularized lower incomplete gamma function.

The upper-current-record formulas (2.5)–(2.6) in Aldallal (2026) are incorrect. In particular, the displayed density there is
\[
\widetilde f_{UC_m}(x)
=
2^m f(x)\,P\!\left(m,\frac t2\right).
\]
It is not a probability density: its total mass is exactly
\[
\int_0^\infty \widetilde f_{UC_m}(x)\,dx
=
\left(\frac23\right)^m
<1.
\]

The correct upper-current-record density and CDF are
\[
f_{UC_m}(x)
=
2^m f(x)P(m,t)
\]
and
\[
F_{UC_m}(x)
=
P(m,2t)-2^m e^{-t}P(m,t).
\]

Thus the upper-current-record part of Theorem 1 of the 2026 Weibull paper is false as printed. The correction concerns the marginal upper-current-record distribution. It does not by itself establish that the paper's separate joint-record likelihood formulas are invalid.

## Assumptions and scope
The argument uses the paper's Weibull convention
\[
f(x)
=
\frac{k}{\lambda}\left(\frac{x}{\lambda}\right)^{k-1}
e^{-(x/\lambda)^k},
\qquad
\overline F(x)=e^{-(x/\lambda)^k},
\]
and the standard current-record formula
\[
f_{UC_m}(x)
=
2^m f(x)
\left[
1-\overline F(x)
\sum_{j=0}^{m-1}
\frac{\{-\log \overline F(x)\}^{j}}{j!}
\right].
\]
This general formula is printed as equation (2.10) in the target paper and as equation (1.1) in Barakat, Nigm, and Aldallal (2014).

The correction is asserted for every integer \(m>1\) and every \(k,\lambda>0\). No simulation, asymptotic approximation, or parameter restriction is used.

## Proof
Substitute
\[
\overline F(x)=e^{-t},
\qquad
-\log\overline F(x)=t
\]
into the general upper-current-record density. The bracket becomes
\[
1-e^{-t}\sum_{j=0}^{m-1}\frac{t^j}{j!}
=
P(m,t),
\]
because for positive integer \(m\),
\[
P(m,t)
=
1-e^{-t}\sum_{j=0}^{m-1}\frac{t^j}{j!}.
\]
Therefore
\[
f_{UC_m}(x)=2^m f(x)P(m,t).
\]

The Weibull change of variable \(t=(x/\lambda)^k\) gives
\[
f(x)\,dx=e^{-t}\,dt.
\]
Hence the printed equation (2.6) has total mass
\[
2^m\int_0^\infty e^{-t}P\!\left(m,\frac t2\right)\,dt.
\]
Expanding the regularized gamma function,
\[
P\!\left(m,\frac t2\right)
=
1-e^{-t/2}
\sum_{j=0}^{m-1}\frac{(t/2)^j}{j!}.
\]
Consequently,
\[
\begin{aligned}
\int_0^\infty e^{-t}P\!\left(m,\frac t2\right)\,dt
&=
1-
\sum_{j=0}^{m-1}
\frac{1}{2^j j!}
\int_0^\infty t^j e^{-3t/2}\,dt\\
&=
1-
\sum_{j=0}^{m-1}
\frac{2}{3^{j+1}}\\
&=
3^{-m}.
\end{aligned}
\]
Multiplication by \(2^m\) gives the exact mass \((2/3)^m\).

For the corrected CDF, define
\[
G_m(t)=P(m,2t)-2^m e^{-t}P(m,t).
\]
Using
\[
\frac{d}{dt}P(m,t)=\frac{t^{m-1}e^{-t}}{\Gamma(m)},
\]
the derivative of \(P(m,2t)\) cancels the derivative contribution from \(P(m,t)\) inside the second term, leaving
\[
G_m'(t)=2^m e^{-t}P(m,t).
\]
Also \(G_m(0)=0\) and \(G_m(t)\to1\) as \(t\to\infty\). Since \(f(x)\,dx=e^{-t}\,dt\), this proves that
\[
F_{UC_m}(x)=G_m((x/\lambda)^k)
\]
is the CDF associated with the corrected density.

## Verification
There are three independent exact checks.

First, the target paper's own general equation (2.10), specialized to the Weibull survival function, gives \(P(m,t)\), not \(P(m,t/2)\).

Second, the printed equation (2.6) has total mass \((2/3)^m\), so for every \(m>1\) it fails the most basic density normalization requirement.

Third, the target paper states that the Weibull model reduces to the Rayleigh model when \(k=2\). Under the parameter identification
\[
\lambda=\sqrt{2}\,\sigma,
\qquad
t=\frac{x^2}{2\sigma^2},
\]
the corrected formulas become
\[
F_{UC_m}(x)
=
P\!\left(m,\frac{x^2}{\sigma^2}\right)
-
2^m e^{-x^2/(2\sigma^2)}
P\!\left(m,\frac{x^2}{2\sigma^2}\right)
\]
and
\[
f_{UC_m}(x)
=
\frac{2^m x}{\sigma^2}
e^{-x^2/(2\sigma^2)}
P\!\left(m,\frac{x^2}{2\sigma^2}\right),
\]
exactly the upper-current-record formulas in Theorem 1 of Aldallal's January 2026 Rayleigh paper.

## Relationship to prior work
Barakat, Nigm, and Aldallal (2014) give the general current-upper-record density
\[
2^m f(x)
\left[
1-\overline F(x)
\sum_{j=0}^{m-1}
\frac{\{-\log\overline F(x)\}^{j}}{j!}
\right].
\]
That earlier formula directly yields the corrected Weibull density after substituting the Weibull survival function.

Aldallal's January 2026 Rayleigh-current-record article gives the correct Rayleigh specialization in its Theorem 1. The February 2026 Weibull article explicitly says that \(k=2\) reduces to Rayleigh, but its equations (2.5)–(2.6) do not reduce to those January formulas. The error in the February proof is the use of
\[
\sum_{j=0}^{m-1}\frac{z^j}{j!}=e^zP(m,z),
\]
where for the paper's stated convention of regularized lower gamma the correct identity is
\[
\sum_{j=0}^{m-1}\frac{z^j}{j!}=e^z\{1-P(m,z)\}.
\]

Focused searches of the target DOI/title, the corrected gamma-function form, the normalization defect, the Rayleigh specialization, and correction/erratum terms found no published correction of the February 2026 equations.

## Limitations
The finding is limited to the upper-current-record marginal formulas in Theorem 1 and results that are explicitly derived from the printed upper density, including the upper marginal moment calculation in Section 3. It does not assert, solely from this defect, that the paper's separately stated joint-current-record likelihood or all later estimation and prediction procedures are false.

The corrected density is already implied by the general current-record formula in the 2014 literature. The originality here is the identification, exact normalization diagnosis, and correction of the February 2026 Weibull specialization, together with its inconsistency with the author's January 2026 Rayleigh specialization.

A nonindexed corrigendum or later correction could reduce the originality of this observation.

## References
1. R. A. Aldallal, “Bayesian estimation and prediction of Weibull current records with application to Saudi industrial data,” AIMS Mathematics 11 (2026), 4369–4394. DOI: 10.3934/math.2026175.
2. R. A. Aldallal, “Rayleigh Current Record Distributed Data: Estimation and Prediction with Application on Saudi Arabia Industrial Data,” Journal of Statistical Theory and Applications 25 (2026), article 2. DOI: 10.1007/s44199-025-00150-x.
3. H. M. Barakat, E. M. Nigm, and R. A. Aldallal, “Current records and record range with some applications,” Journal of the Korean Statistical Society 43 (2014), 263–273. DOI: 10.1016/j.jkss.2013.09.004.
