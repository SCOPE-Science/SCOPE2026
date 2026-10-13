# The TASL family is never unimodal
## Finding
Consider the tri-modal alpha-skew logistic density
\[
f_\alpha(x)=\frac{1}{C(\alpha)}
\left((1-\alpha x)^2+1\right)
\left((x^2-1)^2+2\right)
\frac{e^{-x}}{(1+e^{-x})^2},
\qquad x\in\mathbb R.
\]
For every real \(\alpha\), this density has at least two distinct strict local modes. Thus the one-parameter TASL family cannot be unimodal.

For \(\alpha>0\), one strict local maximum occurs in \((-\infty,0)\), and another occurs in \((2,\infty)\). For \(\alpha<0\), the corresponding statement follows by reflection. For \(\alpha=0\), there are symmetric strict local maxima in \((-\infty,-2)\) and \((2,\infty)\).

This contradicts the source's qualitative claim that changing \(\alpha\) allows the TASL density to transition among unimodal, bimodal, and trimodal configurations.

## Assumptions and scope
The result concerns exactly the density in equation (2.1) of Elbarougy et al. The normalizing constant is irrelevant to the location and number of local modes because it is positive and independent of \(x\).

A mode means a strict local maximum of the density, consistent with the source's own critical-point treatment of modality. The result proves a lower bound of two local modes; it does not classify exactly when the density is bimodal versus trimodal, nor does it rely on the source's separate assertion that there are at most three modes.

## Proof
Write
\[
A_\alpha(x)=(1-\alpha x)^2+1,
\qquad
B(x)=(x^2-1)^2+2.
\]
The logistic kernel satisfies
\[
\frac{e^{-x}}{(1+e^{-x})^2}
=\frac{1}{4\cosh^2(x/2)}.
\]
Because every factor is positive, the sign of \(f_\alpha'(x)\) is the sign of the logarithmic derivative
\[
q_\alpha(x)
=
-\frac{2\alpha(1-\alpha x)}{(1-\alpha x)^2+1}
+
\frac{4x(x^2-1)}{(x^2-1)^2+2}
-
\tanh(x/2).
\]

First suppose \(\alpha>0\). The rational terms vanish at infinity, so
\[
\lim_{x\to-\infty}q_\alpha(x)=1,
\qquad
\lim_{x\to+\infty}q_\alpha(x)=-1.
\]
At the origin,
\[
q_\alpha(0)=-\alpha<0.
\]
At \(x=2\),
\[
q_\alpha(2)
=
-\frac{2\alpha(1-2\alpha)}{(1-2\alpha)^2+1}
+
\frac{24}{11}
-
\tanh(1).
\]
Put \(y=1-2\alpha\), so \(y<1\). The first term becomes
\[
\frac{y^2-y}{y^2+1}.
\]
Its derivative has numerator \(y^2+2y-1\), and its minimum on \(y<1\) is attained at \(y=\sqrt2-1\), with value
\[
\frac{1-\sqrt2}{2}.
\]
Therefore
\[
q_\alpha(2)
\ge
\frac{1-\sqrt2}{2}+\frac{24}{11}-\tanh(1)
>
\frac{1-\sqrt2}{2}+\frac{13}{11}
=
\frac{37-11\sqrt2}{22}
>0.
\]

Hence the continuous function \(q_\alpha\) has the sign pattern
\[
+\quad\text{far to the left},\qquad
q_\alpha(0)<0,\qquad
q_\alpha(2)>0,\qquad
-\quad\text{far to the right}.
\]
Because \(q_\alpha\) is real analytic and not identically zero, these net sign changes force a \(+\)-to-\(-\) crossing in \((-\infty,0)\), a \(-\)-to-\(+\) crossing in \((0,2)\), and a \(+\)-to-\(-\) crossing in \((2,\infty)\). The first and third crossings are strict local maxima of \(f_\alpha\), separated by at least one local minimum.

For \(\alpha<0\), the identity
\[
f_\alpha(x)=f_{-\alpha}(-x)
\]
follows directly from the density, so the two-mode conclusion is reflected from the positive-parameter case.

Finally, when \(\alpha=0\), \(f_0\) is even and \(q_0\) is odd. The same estimate gives
\[
q_0(2)=\frac{24}{11}-\tanh(1)>0,
\]
while \(q_0(x)\to-1\) as \(x\to+\infty\). Thus there is a strict local maximum in \((2,\infty)\), and evenness supplies a second distinct strict local maximum in \((-\infty,-2)\).

Therefore no real value of \(\alpha\) makes the TASL density unimodal.

## Verification
The proof uses only the published density and exact sign inequalities.

The critical bound at \(x=2\) is uniform over all \(\alpha>0\). The parameter-dependent rational term has the exact lower bound
\[
\inf_{\alpha>0}
\left[
-\frac{2\alpha(1-2\alpha)}{(1-2\alpha)^2+1}
\right]
=
\frac{1-\sqrt2}{2}.
\]
Using only \(\tanh(1)<1\) then leaves the strictly positive lower certificate
\[
q_\alpha(2)>
\frac{37-11\sqrt2}{22}.
\]
The tail signs are exact because the polynomial logarithmic derivatives vanish as \(x\to\pm\infty\), while \(-\tanh(x/2)\to\pm1\).

No numerical root finding, plotting, finite grid, or assumption about the total number of stationary points is used in the proof.

## Relationship to prior work
Elbarougy et al. introduce the one-parameter TASL density and state that its shape parameter governs modality, explicitly describing smooth transitions among unimodal, bimodal, and trimodal configurations. The same paper derives a critical-point equation and uses numerical plots to discuss mode behavior. The present result shows directly from equation (2.1) that the unimodal part of that advertised phase description is impossible.

Das et al. study a different flexible alpha-skew-logistic construction with more shape flexibility and report densities with up to three modes. Otiniano et al. study a two-parameter weighted skew-logistic family whose parameter plane genuinely contains unimodal, bimodal, and trimodal regions. Those broader families do not imply unimodality for the distinct one-parameter TASL density, and their additional parameters prevent their modality diagrams from covering the present claim.

Focused searches for the TASL DOI, modality aliases, the phrase “at least two modes,” and corrections to the 2026 source did not locate a published correction or an equivalent proof.

## Limitations
The result proves only that unimodality is impossible. It does not give the exact bifurcation values separating bimodal from trimodal TASL densities, and it does not certify the source's claimed upper bound of three modes.

The proof concerns the standardized density in equation (2.1). Ordinary location-scale changes preserve the number of local modes, but no claim is made about other alpha-skew-logistic families with different weight polynomials.

An unindexed correction or an equivalent observation under different terminology remains a residual originality risk.

## References
1. R. Elbarougy, J. Das, P. J. Hazarika, G. G. Hamedani, A. Nandi, and M. S. Eliwa, “A novel one-parameter tri-modal alpha-skew logistic distribution: mathematical and reliability theory with applications to distant astronomical galaxies and biomedical data,” AIMS Mathematics 11 (2026), 7436–7467. DOI: 10.3934/math.2026305.
2. J. Das, P. Hazarika, G. G. Hamedani, M. Alizadeh, and J. E. Contreras-Reyes, “On the Flexible Alpha Skew-logistic Distribution: Properties and Applications,” Austrian Journal of Statistics 54 (2025), 18–43. DOI: 10.17713/ajs.v54i2.1902.
3. C. Otiniano, R. Vila, P. Brom, and M. Bourguignon, “A Weighted Skew-Logistic Distribution with Applications to Environmental Data,” Mathematics 12 (2024), 1287. DOI: 10.3390/math12091287.
