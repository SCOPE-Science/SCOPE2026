# Both subunit FEPW shapes force a unique bathtub hazard
## Finding
For the flexible exponential power–Weibull distribution with positive scales
\[
\tau>0,
\qquad
\kappa>0,
\]
the published hazard can be written as
\[
h(x)
=
\eta\tau^\eta x^{\eta-1}e^{(\tau x)^\eta}
+
\varphi\kappa^\varphi x^{\varphi-1},
\qquad x>0.
\]

The source states that this hazard is decreasing when both shape parameters satisfy
\[
0<\eta<1,
\qquad
0<\varphi<1.
\]
In fact, throughout that entire open parameter quadrant the hazard is strictly bathtub-shaped with exactly one minimum:
\[
\boxed{
\exists!\,x_*>0:
\quad
h'(x)<0\ \text{for }0<x<x_*,
\qquad
h'(x)>0\ \text{for }x>x_*.
}
\]
Moreover,
\[
\boxed{
h(x)\to\infty\quad(x\downarrow0),
\qquad
h(x)\to\infty\quad(x\to\infty).
}
\]
Thus a globally decreasing FEPW hazard is impossible when both scales are positive and both shape parameters are below one.

The source's own first parameter setting in its decreasing-hazard Figure 2(b) makes the plotting issue especially pronounced:
\[
\tau=0.01,
\qquad
\eta=0.05,
\qquad
\kappa=0.03,
\qquad
\varphi=0.4.
\]
For these values the exponential-power contribution to the hazard derivative cannot even become positive before
\[
\boxed{
x_0=3.7589973457546\times10^{27}.}
\]
The unique hazard minimum occurs still later, at approximately
\[
\boxed{
x_*=1.7683454747093\times10^{30}.}
\]
A graph ending at \(x=100\) therefore shows only the long initial decreasing branch and cannot determine the global hazard shape.

## Assumptions and scope
The theorem concerns the interior parameter regime
\[
\tau,\kappa>0,
\qquad
0<\eta,\varphi<1.
\]
The scale-boundary cases \(\tau=0\) or \(\kappa=0\) are excluded because the corresponding competing-risk component disappears and the four-parameter representation degenerates.

The statement classifies the full-support hazard shape. It does not say that the hazard cannot be decreasing on a finite observational window. Indeed, the source's plotted examples can decrease over very large finite ranges before the exponential-power term eventually forces an upturn.

The theorem is specific to the quadrant where both shape parameters are below one. Other FEPW shape regimes are not classified here.

## Proof
Differentiate the hazard:
\[
h'(x)
=
\eta\tau^\eta x^{\eta-2}e^{z}
\bigl(\eta z+\eta-1\bigr)
-
\varphi(1-\varphi)\kappa^\varphi x^{\varphi-2},
\]
where
\[
z=(\tau x)^\eta.
\]
Let
\[
z_0=\frac{1-\eta}{\eta},
\qquad
x_0=\frac{z_0^{1/\eta}}{\tau}.
\]
For \(0<x\le x_0\), one has
\[
\eta z+\eta-1\le0,
\]
while the Weibull derivative term is strictly negative. Hence
\[
h'(x)<0
\qquad
(0<x\le x_0).
\]

Now take \(x>x_0\). The first derivative contribution is positive. Divide it by the absolute value of the negative Weibull contribution and define
\[
R(x)
=
\frac{
\eta\tau^\eta x^{\eta-\varphi}e^z
(\eta z+\eta-1)
}{
\varphi(1-\varphi)\kappa^\varphi
}.
\]
Then
\[
\operatorname{sgn}h'(x)=\operatorname{sgn}(R(x)-1).
\]
Since
\[
x=\frac{z^{1/\eta}}{\tau},
\]
differentiation with respect to \(z\) gives
\[
\frac{d}{dz}\log R
=
1+
\frac{\eta-\varphi}{\eta z}
+
\frac{\eta}{\eta z+\eta-1}.
\]
Write
\[
z=z_0+s,
\qquad
s>0.
\]
Multiplication by the positive quantity
\[
\eta z(\eta z+\eta-1)
\]
yields
\[
\eta z(\eta z+\eta-1)
\frac{d}{dz}\log R
=
\eta
\left[
\eta s^2+(1+\eta-\varphi)s+(1-\eta)
\right].
\]
Every coefficient on the right is strictly positive because
\[
0<\eta,\varphi<1.
\]
Therefore
\[
\frac{d}{dz}\log R>0
\]
and \(R\) is strictly increasing on \((x_0,\infty)\).

At the left endpoint,
\[
R(x)\to0
\qquad
(x\downarrow x_0),
\]
because \(\eta z+\eta-1\to0\). At infinity the factor \(e^z\) dominates every power, so
\[
R(x)\to\infty.
\]
The intermediate-value theorem and strict monotonicity give exactly one solution
\[
R(x_*)=1.
\]
Consequently \(h'\) is negative before \(x_*\) and positive after it.

Finally, because \(\eta-1<0\) and \(\varphi-1<0\), both hazard components diverge as \(x\downarrow0\). As \(x\to\infty\), the exponential-power component
\[
\eta\tau^\eta x^{\eta-1}e^{(\tau x)^\eta}
\]
diverges. Thus the unique critical point is the unique global minimum.

## Verification
The accompanying checker evaluates the exact derivative, the ratio \(R\), and its logarithmic derivative in the transformed variable \(z\).

It verifies the sign pattern for a grid of admissible parameter values and numerically solves the unique equation \(R=1\). These finite checks illustrate the analytic theorem; they are not used as proof.

For the source's first Figure 2(b) setting, the checker obtains
\[
x_0=3.7589973457546\times10^{27}
\]
and
\[
x_*=1.7683454747093\times10^{30}.
\]
It also confirms that \(h'(100)<0\), explaining why the finite plotting window displays a decreasing curve despite the inevitable later upturn.

## Relationship to prior work
The 2026 FEPW article derives the hazard and its derivative and states that the hazard is increasing when both shape parameters exceed one, decreasing when both lie below one, and bathtub-shaped when the shape parameters lie on opposite sides of one. Its Figure 2(b) illustrates the claimed decreasing regime with several parameter choices having \(0<\eta,\varphi<1\).

The classical exponential-power component is itself known to admit bathtub behavior. Its hazard is proportional to
\[
x^{\eta-1}e^{x^\eta},
\]
whose derivative changes sign once when \(0<\eta<1\). Adding the decreasing Weibull hazard does not remove that eventual upturn; the ratio argument above proves that it merely shifts the unique minimum to the right.

The closest additive and modified Weibull literature establishes flexible hazard families for different functional forms. Those results do not supply the exact FEPW theorem that the entire both-subunit quadrant has one and only one minimum.

Focused searches using the exact DOI, the FEPW name, the claimed decreasing quadrant, the hazard derivative, competing-risk terminology, and correction terminology did not locate a published correction or an equivalent model-specific theorem.

## Limitations
The result does not classify the mixed-shape regimes or the cases where one or both shape parameters equal one.

The minimum can occur at astronomically large times, so the theorem does not imply that a finite engineering dataset will visibly contain the upturn.

A very recent or unindexed correction could exist outside the sources examined.

## References
1. M. G. M. Ghazal, “Hamiltonian Monte Carlo–based inference for the flexible exponential power–Weibull distribution with applications in reliability analysis,” AIMS Mathematics 11 (2026), 11659–11705. DOI: 10.3934/math.2026481.
2. NIST/SEMATECH e-Handbook of Statistical Methods, “Exponential Power Hazard Function,” documenting the exponential-power hazard and its reliability use.
3. M. K. Shakhatreh, A. J. Lemonte, and G. M. Cordeiro, “On the generalized extended exponential–Weibull distribution: Properties and different methods of estimation,” International Journal of Computer Mathematics 97 (2020), 1029–1057. DOI: 10.1080/00207160.2019.1605062.
