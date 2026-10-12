# The inverted ZLindley mean inactivity formula has the wrong exponential-integral sign
## Finding
Let \(Y\) have the inverted ZLindley distribution with parameter
\[
\alpha>0
\]
and CDF
\[
F(t)
=
\left(
1+\frac{\alpha}{2(1+\alpha)t}
\right)e^{-\alpha/t},
\qquad t>0.
\]
The source defines the mean inactivity time by
\[
m(t)
=
\mathbb E[t-Y\mid Y\le t]
=
\frac{\int_0^t F(y)\,dy}{F(t)}.
\]

The paper's Eq. (15) gives
\[
\int_0^t F(y)\,dy
=
\alpha\Gamma\!\left(-1,\frac{\alpha}{t}\right)
+
\frac{\alpha}{2(1+\alpha)}
\operatorname{Ei}\!\left(-\frac{\alpha}{t}\right).
\]
The sign of the exponential-integral term is incorrect.

The correct identity is
\[
\boxed{
\int_0^t F(y)\,dy
=
\alpha\Gamma\!\left(-1,\frac{\alpha}{t}\right)
-
\frac{\alpha}{2(1+\alpha)}
\operatorname{Ei}\!\left(-\frac{\alpha}{t}\right)
}
\]
or, equivalently,
\[
\boxed{
\int_0^t F(y)\,dy
=
\alpha\Gamma\!\left(-1,\frac{\alpha}{t}\right)
+
\frac{\alpha}{2(1+\alpha)}
E_1\!\left(\frac{\alpha}{t}\right).
}
\]

This is not a harmless convention difference. Under the standard real convention
\[
E_1(z)=-\operatorname{Ei}(-z),
\qquad z>0.
\]
With the sign printed in the source, the resulting quantity can be negative even though mean inactivity time is the conditional expectation of the nonnegative random variable \(t-Y\) on \(\{Y\le t\}\).

More strongly, for every fixed \(\alpha>0\),
\[
\boxed{
m_{\mathrm{pub}}(t)
\sim
-\frac{t^2}{\alpha}
\qquad
(t\downarrow0),
}
\]
while the true mean inactivity time satisfies
\[
\boxed{
m(t)
\sim
\frac{t^2}{\alpha}
\qquad
(t\downarrow0).
}
\]

For example, at
\[
\alpha=1,\qquad t=0.1,
\]
the source's Eq. (15), divided by \(F(t)\), gives
\[
-0.004129762121352886\ldots,
\]
whereas the corrected formula gives
\[
0.008950714155759697\ldots.
\]
Direct numerical integration of the defining formula gives the same positive value.

Thus Eq. (15), and any mean-inactivity expression derived from it without changing the sign, must be corrected.

## Assumptions and scope
The parameter and time domain are
\[
\alpha>0,\qquad t>0.
\]
The result concerns the source's mean inactivity time formula only. The CDF and density used in the derivation are not challenged.

The notation
\[
\Gamma(s,z)
\]
denotes the upper incomplete gamma function, and
\[
E_1(z)
=
\int_z^\infty \frac{e^{-u}}{u}\,du
\]
for \(z>0\). With the standard real exponential integral,
\[
E_1(z)=-\operatorname{Ei}(-z).
\]

No claim is made here about the source's moment formulas, likelihood inference, order statistics, or other reliability measures.

## Proof
Split the defining integral using the published CDF:
\[
\int_0^t F(y)\,dy
=
\int_0^t e^{-\alpha/y}\,dy
+
\frac{\alpha}{2(1+\alpha)}
\int_0^t \frac{e^{-\alpha/y}}{y}\,dy.
\]

For the first term, set
\[
u=\frac{\alpha}{y}.
\]
Then
\[
y=\frac{\alpha}{u},
\qquad
dy=-\frac{\alpha}{u^2}\,du,
\]
and the limits \(y\downarrow0\) and \(y=t\) correspond to \(u\uparrow\infty\) and \(u=\alpha/t\). Therefore
\[
\int_0^t e^{-\alpha/y}\,dy
=
\alpha
\int_{\alpha/t}^{\infty}
u^{-2}e^{-u}\,du
=
\alpha\Gamma\!\left(-1,\frac{\alpha}{t}\right).
\]

For the second term, the same substitution gives
\[
\int_0^t \frac{e^{-\alpha/y}}{y}\,dy
=
\int_{\alpha/t}^{\infty}
\frac{e^{-u}}{u}\,du
=
E_1\!\left(\frac{\alpha}{t}\right)
=
-\operatorname{Ei}\!\left(-\frac{\alpha}{t}\right).
\]
Substitution into the split integral gives the corrected formula.

To obtain the small-time asymptotics, put
\[
z=\frac{\alpha}{t}.
\]
As \(z\to\infty\),
\[
\Gamma(-1,z)
=
e^{-z}z^{-2}\{1+O(z^{-1})\}
\]
and
\[
E_1(z)
=
e^{-z}z^{-1}\{1+O(z^{-1})\}.
\]
Also
\[
F(t)
=
\left(
1+\frac{z}{2(1+\alpha)}
\right)e^{-z}
\sim
\frac{z}{2(1+\alpha)}e^{-z}.
\]

The true numerator is dominated by the positive \(E_1\) term:
\[
\int_0^t F(y)\,dy
\sim
\frac{\alpha}{2(1+\alpha)}
e^{-z}z^{-1},
\]
hence
\[
m(t)
\sim
\frac{\alpha}{z^2}
=
\frac{t^2}{\alpha}.
\]

The source-sign numerator instead has the same dominant term with a minus sign, yielding
\[
m_{\mathrm{pub}}(t)
\sim
-\frac{t^2}{\alpha}.
\]
This proves that the printed expression is negative for all sufficiently small positive \(t\), for every \(\alpha>0\).

## Verification
The accompanying checker evaluates three expressions independently:

1. direct quadrature of
\[
\int_0^t F(y)\,dy;
\]

2. the corrected special-function formula
\[
\alpha\Gamma(-1,\alpha/t)
+
\frac{\alpha}{2(1+\alpha)}E_1(\alpha/t);
\]

3. the source-sign expression with
\[
+\operatorname{Ei}(-\alpha/t).
\]

For several positive parameter-time pairs, direct quadrature and the corrected expression agree to high precision.

At
\[
(\alpha,t)=(1,0.1),
\]
the checker obtains
\[
m(t)=0.0089507141557596967\ldots
\]
from both direct integration and the corrected formula, while the source-sign expression gives
\[
m_{\mathrm{pub}}(t)
=
-0.0041297621213528864\ldots.
\]

The checker also verifies numerically that
\[
\frac{\alpha m(t)}{t^2}\to1
\]
and
\[
\frac{\alpha m_{\mathrm{pub}}(t)}{t^2}\to-1
\]
as \(t\downarrow0\). These numerical limits are consistency checks; the asymptotics are proved above.

## Relationship to prior work
Alqasem and Elshahhat introduce the inverted ZLindley model and explicitly develop mean inactivity time as a reliability characteristic. Their Eq. (11) gives the standard defining integral, Eq. (12) splits it into two positive integrals, and Eq. (15) changes the second integral to a positive multiple of
\[
\operatorname{Ei}(-\alpha/t).
\]
Because this function is negative for positive \(\alpha/t\), that step reverses the sign of the second positive integral.

The standard exponential-integral identity
\[
E_1(z)=-\operatorname{Ei}(-z),
\qquad z>0,
\]
shows that the correct sign is the opposite of the one printed in Eq. (15).

Focused searches using the exact DOI, inverted-ZLindley name, mean-inactivity terminology, exponential-integral aliases, and sign-correction language did not locate a published corrigendum or another source already identifying this model-specific error. A later 2026 paper on inference for the inverted Z-Lindley distribution concerns step-stress testing under censoring and does not provide a correction of this mean-inactivity formula.

## Limitations
The finding corrects one reliability formula and its small-time behavior; it does not reassess the complete reliability analysis in the article.

The full monotonicity or aging properties of the corrected mean inactivity time are not classified here.

A very recent unindexed author correction could exist outside the records examined.

## References
1. O. A. Alqasem and A. Elshahhat, “A New One-Parameter Model Supports an Upside-Down Bathtub Failure Rate: Theory, Inference, and Real-World Applications,” Mathematics 14 (2026), 1566. DOI: 10.3390/math14091566.
2. NIST Digital Library of Mathematical Functions, §6.2, exponential integrals; for positive real \(z\), \(E_1(z)=-\operatorname{Ei}(-z)\).
