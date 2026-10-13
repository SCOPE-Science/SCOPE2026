# The bounded \(p\)-exponential density has the opposite endpoint phase below and above one
## Finding
For the one-parameter bounded \(p\)-exponential distribution,
\[
p>0,\qquad 0<x<p+1,
\]
the published density is
\[
f_p(x)
=
\frac{p}{p+1}
\left(
1-\frac{x}{p+1}
\right)^{p-1}.
\]
Equivalently,
\[
\boxed{
f_p(x)=\frac{p}{(p+1)^p}(p+1-x)^{p-1}.
}
\]

This gives a complete density-shape phase diagram with boundary \(p=1\).

If \(0<p<1\), then
\[
\boxed{f_p'(x)>0,}
\]
so the density is strictly increasing. It is log-convex and
\[
\boxed{f_p(x)\to+\infty\quad(x\uparrow p+1).}
\]

If \(p=1\), then
\[
\boxed{f_1(x)=\frac12,\qquad 0<x<2,}
\]
so the law is uniform.

If \(p>1\), then
\[
\boxed{f_p'(x)<0,}
\]
so the density is strictly decreasing. It is log-concave and
\[
\boxed{f_p(x)\to0\quad(x\uparrow p+1).}
\]
Its boundary supremum is
\[
\sup_{0<x<p+1}f_p(x)=\frac{p}{p+1}.
\]

Therefore the density never has the published “initially decays, then bends upward” geometry. It is monotone throughout its support for every admissible parameter value.

The correction is specific to density geometry. The published hazard formula
\[
h_p(x)=\frac{p}{p+1-x}
\]
is correct and satisfies
\[
h_p'(x)=\frac{p}{(p+1-x)^2}>0
\]
for every \(p>0\). Hence the family remains increasing-failure-rate for all admissible parameters even though the density phase description requires reversal.

## Assumptions and scope
The parameter domain is \(p>0\), with open support \((0,p+1)\).

Because the support is open, “mode at \(x=0\)” is best interpreted as a boundary-supremum statement. For \(p>1\), the density approaches its supremum \(p/(p+1)\) as \(x\downarrow0\); for \(0<p<1\), the density has no finite attained mode and diverges as \(x\uparrow p+1\). At \(p=1\), the density is constant and every interior point is a mode in the nonunique sense.

The correction does not alter the CDF, survival, quantile, moment formulas, scaled-beta representation, or the increasing hazard formula. It addresses density monotonicity, endpoint limits, log-shape classification, and the qualitative interpretation of Figure 1.

## Proof
Rewrite the density as
\[
f_p(x)=\frac{p}{(p+1)^p}(p+1-x)^{p-1}.
\]
Differentiating gives
\[
\boxed{
f_p'(x)=-\frac{p(p-1)}{(p+1)^p}(p+1-x)^{p-2}.
}
\]
Every factor other than \(-(p-1)\) is positive on the support. Therefore \(f_p'(x)>0\) when \(0<p<1\), \(f_p'(x)=0\) when \(p=1\), and \(f_p'(x)<0\) when \(p>1\).

For the endpoint, let \(\delta=p+1-x\). Then
\[
f_p(x)=\frac{p}{(p+1)^p}\delta^{p-1}.
\]
Thus the density diverges when \(p-1<0\), remains constant when \(p-1=0\), and vanishes when \(p-1>0\).

For log-shape,
\[
\log f_p(x)=\log\!\left(\frac{p}{p+1}\right)+(p-1)\log\!\left(1-\frac{x}{p+1}\right),
\]
so
\[
\frac{d^2}{dx^2}\log f_p(x)=-\frac{p-1}{(p+1-x)^2}.
\]
Therefore \(f_p\) is log-convex for \(0<p<1\), log-linear at \(p=1\), and log-concave for \(p>1\).

Finally,
\[
h_p(x)=\frac{p}{p+1-x},
\qquad
h_p'(x)=\frac{p}{(p+1-x)^2}>0.
\]

## Verification
The accompanying checker evaluates the exact density and derivative for representative values on both sides of \(p=1\). It verifies strict increase for representative \(0<p<1\), constancy at \(p=1\), strict decrease for representative \(p>1\), the exact endpoint scaling
\[
f_p(p+1-\delta)\delta^{1-p}=\frac{p}{(p+1)^p},
\]
and the increasing hazard derivative. It also verifies numerical normalization for representative parameters.

These finite evaluations are consistency checks. The phase diagram is proved analytically above.

## Relationship to prior work
Bakouch et al. define the model and give the correct density formula. The public full text then gives incompatible qualitative descriptions.

The discussion accompanying Figure 1 says the density has a common shape across parameter values, “initially decays” before bending upward, and ultimately blows up at the finite right endpoint for all \(p\). The exact density formula rules this out: the density is globally monotone, and right-endpoint blow-up occurs only when \(0<p<1\).

Section 2.3 correctly computes
\[
\frac{d}{dx}\log f_p(x)=-\frac{p-1}{p+1-x}
\]
and
\[
\frac{d^2}{dx^2}\log f_p(x)=-\frac{p-1}{(p+1-x)^2},
\]
but then states that for \(0<p\le1\) the density is decreasing. The derivative has the opposite sign for \(0<p<1\). The same section's \(p>1\) log-concavity statement is correct.

The article also identifies the law as
\[
X=(p+1)Y,\qquad Y\sim\mathrm{Beta}(1,p),
\]
which independently confirms the corrected monotonicity.

Focused searches using the exact DOI, model name, density monotonicity, endpoint behavior, and Figure 1 terminology did not locate a published corrigendum or model-specific correction.

## Limitations
The finding does not challenge the model's normalization, CDF, quantile, moment identities, or increasing-failure-rate property.

No inference procedure is reassessed here. The correction concerns analytic density shape and the interpretation attached to it.

A recent unindexed correction could exist outside the publisher and indexed search records examined.

## References
1. H. S. Bakouch, H. S. Salinas, F. A. Moala, T. Hussain, S. Aldossari, and A. Al-Buainain, “The One-Parameter Bounded p-Exponential Distribution: Properties, Inference, and Applications,” Mathematics 14 (2026), 1076. DOI: 10.3390/math14061076.
