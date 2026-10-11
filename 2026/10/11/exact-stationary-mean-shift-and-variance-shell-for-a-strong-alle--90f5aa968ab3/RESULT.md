# Exact stationary mean-shift and variance shell for a strong-Allee Holling-II predator–prey flow
## Finding
Consider the normalized strong-Allee predator–prey model
\[
\dot x=x\left[(1-x)(x-\alpha)-\frac{y}{K}\right],\qquad
\dot y=y\left[\frac{\omega x}{1+\eta x}-\sigma\right],
\]
with \(K,\omega,\eta,\sigma>0\), \(0<\alpha<1\), and
\[
\frac{\omega\alpha}{1+\eta\alpha}<\sigma<\frac{\omega}{1+\eta}.
\]
The positive equilibrium has prey coordinate
\[
x_*=\frac{\sigma}{\omega-\sigma\eta},
\]
so \(\alpha<x_*<1\).

Let \(\mu\) be any compactly supported invariant probability measure whose support is contained in \((0,\infty)^2\), and write
\[
\bar x=\int x\,d\mu,\qquad \bar y=\int y\,d\mu,
\]
\[
\operatorname{Var}_\mu(x)=\int (x-\bar x)^2\,d\mu.
\]
Then
\[
\boxed{\bar x-x_*=\eta\int\frac{(x-x_*)^2}{1+\eta x}\,d\mu}
\]
and
\[
\boxed{\frac{\bar y}{K}+\operatorname{Var}_\mu(x)=(1-\bar x)(\bar x-\alpha)}.
\]
Hence \(\alpha<\bar x<1\). Moreover, \(\bar x=x_*\) holds only for the Dirac measure at the positive equilibrium. Therefore every non-equilibrium compact interior invariant measure satisfies
\[
x_*<\bar x<1.
\]
In particular, every positive nonconstant periodic orbit has time-mean prey density strictly above the coexistence equilibrium prey density.

For the source's numerical values \(\alpha=1/5\), \(K=13/10\), \(\omega=1\), \(\eta=3/5\), and \(\sigma=0.44106\),
\[
x_*=\frac{110265}{183841}=0.5997845964719513\ldots,
\]
so any positive nonconstant periodic orbit at those parameters must have mean prey density strictly greater than this value.

## Assumptions and scope
The statement concerns invariant probability measures with compact support strictly inside the positive quadrant. This interior-support assumption makes \(\log x\) and \(\log y\) smooth and bounded on the support, so their generator averages vanish under \(\mu\). No claim is made for invariant measures charging either coordinate axis, for noncompact invariant measures, or for transient trajectories.

The coexistence inequalities are exactly the source's conditions for a unique positive equilibrium. The result is a stationary finite-amplitude constraint: it does not assert existence or uniqueness of a periodic orbit, and it does not replace the source's local Hopf analysis.

## Proof
Because \(\mu\) is invariant and has compact support in the open positive quadrant,
\[
0=\int \frac{d}{dt}\log y\,d\mu
 =\int\left(\frac{\omega x}{1+\eta x}-\sigma\right)d\mu.
\]
Since \(\sigma/\omega=x_*/(1+\eta x_*)\), this becomes
\[
0=\int\left(\frac{x}{1+\eta x}-\frac{x_*}{1+\eta x_*}\right)d\mu
 =\frac{1}{1+\eta x_*}\int\frac{x-x_*}{1+\eta x}\,d\mu.
\]
Using
\[
x-x_*=(x-x_*)\frac{1+\eta x}{1+\eta x}
       =\frac{x-x_*}{1+\eta x}+\eta\frac{x(x-x_*)}{1+\eta x},
\]
a more direct rearrangement is
\[
\frac{x-x_*}{1+\eta x}
=(x-x_*)-\eta\frac{x(x-x_*)}{1+\eta x}.
\]
To isolate a nonnegative defect, instead write \(x=x_*+(x-x_*)\) in the factor \(x\):
\[
0=\int\frac{x-x_*}{1+\eta x}\,d\mu
 =\int(x-x_*)\,d\mu-\eta\int\frac{x(x-x_*)}{1+\eta x}\,d\mu,
\]
and
\[
\frac{x(x-x_*)}{1+\eta x}
=\frac{x_*(x-x_*)}{1+\eta x}+\frac{(x-x_*)^2}{1+\eta x}.
\]
The first term integrates to zero, giving
\[
\bar x-x_*=\eta\int\frac{(x-x_*)^2}{1+\eta x}\,d\mu.
\]
The denominator is positive, so the right-hand side is nonnegative and vanishes exactly when \(x=x_*\) \(\mu\)-almost surely. The support of an invariant measure is invariant. If its support lies in the line \(x=x_*\), the first vector-field component must vanish there, forcing
\[
y=K(1-x_*)(x_*-\alpha)=:y_*.
\]
Thus equality occurs only for \(\mu=\delta_{(x_*,y_*)}\).

Similarly,
\[
0=\int \frac{d}{dt}\log x\,d\mu
 =\int\left[(1-x)(x-\alpha)-\frac{y}{K}\right]d\mu.
\]
Because
\[
(1-x)(x-\alpha)=-x^2+(1+\alpha)x-\alpha,
\]
and \(\int x^2d\mu=\bar x^2+\operatorname{Var}_\mu(x)\),
\[
\frac{\bar y}{K}
=(1-\bar x)(\bar x-\alpha)-\operatorname{Var}_\mu(x),
\]
which is the second boxed identity. Interior support gives \(\bar y>0\), hence \((1-\bar x)(\bar x-\alpha)>0\), so \(\alpha<\bar x<1\). Combining this with the strict first identity for non-equilibrium measures yields \(x_*<\bar x<1\).

## Verification
The proof uses only the displayed vector field, invariance of \(\mu\), elementary algebra, and positivity of the denominator \(1+\eta x\). The exact coexistence coordinate agrees with the source's equilibrium formula. The accompanying dependency-free script `verify.py` checks the rational identity underlying the mean-shift law, the quadratic moment identity, and the exact numerical value of \(x_*\) in the source's \(\sigma=0.44106\) example. The general proof above is analytic and does not depend on finite numerical testing.

## Relationship to prior work
Ma, Zhao, and Du introduce the normalized system, establish positivity and boundedness, classify its equilibria, prove a supercritical Hopf bifurcation, and numerically display the resulting stable limit cycle. Their article gives \(x_*=\sigma/(\omega-\sigma\eta)\) and the same coexistence inequalities used here, but it does not state a finite-amplitude invariant-measure mean identity or a variance shell.

Zu and Mimura study an earlier strong-Allee Holling-II predator–prey model, and Xie studies a related model with both fear and Allee effects. Their prey equations differ from the quadratic normalized prey equation above. The Holling-II predator equation makes the first weighted-mean mechanism structurally plausible across related models, but those models do not algebraically imply the second quadratic variance shell for the Ma–Zhao–Du flow. Full-text searches of the Ma–Zhao–Du article and the accessible Xie article did not locate the paired stationary identities stated here.

## Limitations
The first mean-shift mechanism is an elementary consequence of the saturating Holling-II predator growth term and may have analogues in classical predator–prey averaging literature. The originality asserted here is the source-specific paired finite-amplitude statement: the exact nonnegative prey-mean defect together with the exact mean-predator/prey-variance shell for this normalized strong-Allee flow. A full text of the 2010 Zu–Mimura paper was not available in the inspected lawful sources, so possible antecedents for the generic first component remain a residual literature risk. This does not affect the proof, and the different prey equation means that paper cannot directly imply the source-specific quadratic shell without additional work.

## References
1. Y. Ma, M. Zhao, Y. Du, “Impact of the strong Allee effect in a predator-prey model,” *AIMS Mathematics* 7 (2022), 16296–16314. DOI: 10.3934/math.2022890.
2. J. Zu, M. Mimura, “The impact of Allee effect on a predator–prey system with Holling type II functional response,” *Applied Mathematics and Computation* 217 (2010), 3542–3556. DOI: 10.1016/j.amc.2010.09.029.
3. B. Xie, “Impact of the fear and Allee effect on a Holling type II prey–predator model,” *Advances in Difference Equations* 2021, 464 (2021). DOI: 10.1186/s13662-021-03592-6.
