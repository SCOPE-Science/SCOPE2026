# Exact MOPHL hazard phase diagram contradicts Theorem 1
## Finding
For the Marshall–Olkin Power Half-Logistic (MOPHL) distribution, let
\[
\alpha>0,\qquad \theta>0,\qquad \gamma>0,
\]
and write
\[
c=2\alpha-1>-1.
\]
The published hazard is
\[
r(x)
=
\frac{\theta\gamma e^{\gamma x^\theta}x^{\theta-1}}
{e^{\gamma x^\theta}+c},
\qquad x>0.
\]
Put
\[
u=\gamma x^\theta.
\]
Direct differentiation gives
\[
r'(x)
=
\frac{\theta\gamma x^{\theta-2}e^u}
{(e^u+c)^2}
\,
\Phi_{\theta,c}(u),
\]
where
\[
\boxed{
\Phi_{\theta,c}(u)
=
(\theta-1)(e^u+c)+\theta c u.
}
\]
All factors outside \(\Phi_{\theta,c}\) are positive. Hence the complete hazard-shape problem reduces to the sign of this one-variable function.

For
\[
\theta>1,
\]
define
\[
A_+(\theta)
=
\frac{\theta-1}{\theta}e^{1/\theta}.
\]
Then
\[
0<A_+(\theta)<1,
\]
and the exact classification is
\[
\boxed{
c\ge -A_+(\theta)
\quad\Longrightarrow\quad
r \text{ is strictly increasing}.
}
\]
At
\[
c=-A_+(\theta),
\]
the derivative vanishes only at
\[
u=\frac1\theta,
\]
so the hazard remains strictly increasing but has one horizontal tangent.

If instead
\[
\boxed{
-1<c<-A_+(\theta),
}
\]
then \(\Phi_{\theta,c}\) has exactly two positive zeros. Consequently,
\[
\boxed{
r \text{ has an increase–decrease–increase shape}.
}
\]

For
\[
0<\theta<1,
\]
define
\[
A_-(\theta)
=
\frac{1-\theta}{\theta}e^{1/\theta}.
\]
Then
\[
\boxed{
c\le A_-(\theta)
\quad\Longrightarrow\quad
r \text{ is strictly decreasing}.
}
\]
At
\[
c=A_-(\theta),
\]
the derivative vanishes only at
\[
u=\frac1\theta,
\]
and the hazard remains strictly decreasing.

If
\[
\boxed{
c>A_-(\theta),
}
\]
then \(\Phi_{\theta,c}\) has exactly two positive zeros, and
\[
\boxed{
r \text{ has a decrease–increase–decrease shape}.
}
\]

For
\[
\theta=1,
\]
the source's special-case classification is correct:
\[
c>0 \Rightarrow r \text{ increasing},\qquad
c=0 \Rightarrow r\equiv\gamma,\qquad
-1<c<0 \Rightarrow r \text{ decreasing}.
\]

Equivalently, the phase boundaries in the original Marshall–Olkin parameter are

for \(\theta>1\),
\[
\boxed{
\alpha_+(\theta)
=
\frac12
\left[
1-
\frac{\theta-1}{\theta}e^{1/\theta}
\right],
}
\]
with strict increase for
\[
\alpha\ge\alpha_+(\theta)
\]
and increase–decrease–increase behavior for
\[
0<\alpha<\alpha_+(\theta);
\]

and for \(0<\theta<1\),
\[
\boxed{
\alpha_-(\theta)
=
\frac12
\left[
1+
\frac{1-\theta}{\theta}e^{1/\theta}
\right],
}
\]
with strict decrease for
\[
0<\alpha\le\alpha_-(\theta)
\]
and decrease–increase–decrease behavior for
\[
\alpha>\alpha_-(\theta).
\]

The source's Theorem 1 therefore fails: away from \(\theta=1\), the global hazard shape depends jointly on \(\alpha\) and \(\theta\).

The paper's own principal simulation setting exposes the issue. It uses
\[
(\alpha,\theta,\gamma)=(0.03,2.52,0.03)
\]
and describes the resulting hazard as non-monotonic, even though Theorem 1 says every \(\theta>1\) hazard is strictly increasing. The corrected threshold is
\[
A_+(2.52)
=
0.8969786938870231\ldots,
\]
so
\[
\alpha_+(2.52)
=
0.0515106530564884\ldots.
\]
Since
\[
0.03<0.0515106530564884\ldots,
\]
that simulation setting lies exactly in the corrected increase–decrease–increase region.

For this setting, the two stationary points satisfy
\[
\gamma x^\theta
=
0.1211302351638599\ldots
\]
and
\[
\gamma x^\theta
=
0.7349193155750372\ldots,
\]
giving
\[
x=1.739916056312669\ldots
\]
and
\[
x=3.558258235319753\ldots.
\]

## Assumptions and scope
The parameter domain is the source's full admissible domain
\[
\alpha,\theta,\gamma>0.
\]
Since
\[
c=2\alpha-1>-1
\]
and
\[
e^{\gamma x^\theta}\ge1,
\]
the denominator of the hazard is positive for every \(x\ge0\).

The phase boundaries are independent of \(\gamma\). The scale parameter changes the locations of the turning points through
\[
x=(u/\gamma)^{1/\theta},
\]
but not whether turning points exist.

The finding corrects the hazard monotonicity theorem and the associated physical interpretation that \(\theta\) alone determines aging versus infant-mortality behavior. It does not reassess the source's censoring likelihood, Bayesian computation, fitted parameter estimates, or goodness-of-fit comparisons.

The words “increase–decrease–increase” and “decrease–increase–decrease” refer to the sign sequence of \(r'(x)\) on the positive line. No claim is made that these three-stage shapes coincide with every engineering convention for “bathtub” terminology.

## Proof
Because
\[
u=\gamma x^\theta,
\]
the hazard can be written
\[
r(x)
=
\theta\gamma x^{\theta-1}
\frac{e^u}{e^u+c}.
\]
Differentiation yields
\[
r'(x)
=
\frac{\theta\gamma x^{\theta-2}e^u}
{(e^u+c)^2}
\left[
(\theta-1)(e^u+c)+\theta c u
\right].
\]
Thus only
\[
\Phi_{\theta,c}(u)
=
(\theta-1)(e^u+c)+\theta c u
\]
controls the sign.

Suppose first that
\[
\theta>1.
\]
If \(c\ge0\), every term in \(\Phi_{\theta,c}\) is nonnegative and the first is positive, so the hazard is strictly increasing.

Now let
\[
-1<c<0
\]
and put
\[
q=-c\in(0,1).
\]
Then
\[
\Phi_{\theta,c}(u)
=
(\theta-1)e^u
-q\{(\theta-1)+\theta u\}.
\]
Its second derivative is
\[
\Phi_{\theta,c}''(u)
=
(\theta-1)e^u>0,
\]
so \(\Phi_{\theta,c}\) is strictly convex. Also
\[
\Phi_{\theta,c}(0)
=
(\theta-1)(1-q)>0
\]
and
\[
\Phi_{\theta,c}(u)\to+\infty.
\]
If an interior minimum exists, it satisfies
\[
(\theta-1)e^{u_*}=q\theta,
\]
so
\[
u_*
=
\log\!\left(
\frac{q\theta}{\theta-1}
\right).
\]
At this point,
\[
\Phi_{\theta,c}(u_*)
=
q(1-\theta u_*).
\]
Therefore the minimum is nonnegative exactly when
\[
u_*\le\frac1\theta,
\]
equivalently
\[
q
\le
\frac{\theta-1}{\theta}e^{1/\theta}
=
A_+(\theta).
\]
This proves strict increase when
\[
c\ge-A_+(\theta).
\]
At equality, strict convexity gives a unique zero of \(\Phi\), so \(r'\ge0\) with equality at only one point; hence \(r\) is still strictly increasing. If
\[
c<-A_+(\theta),
\]
the strict convex function has a negative minimum and positive values at both ends, so it has exactly two positive zeros and sign pattern
\[
+,-,+.
\]

Now suppose
\[
0<\theta<1.
\]
If \(c\le0\), both terms
\[
(\theta-1)(e^u+c)
\]
and
\[
\theta c u
\]
are nonpositive, with the first strictly negative, so the hazard is strictly decreasing.

Let
\[
c>0.
\]
Then
\[
\Phi_{\theta,c}''(u)
=
(\theta-1)e^u<0,
\]
so \(\Phi_{\theta,c}\) is strictly concave. Its endpoint values satisfy
\[
\Phi_{\theta,c}(0)
=
(\theta-1)(1+c)<0
\]
and
\[
\Phi_{\theta,c}(u)\to-\infty.
\]
At an interior maximum,
\[
(1-\theta)e^{u_*}=c\theta,
\]
so
\[
u_*
=
\log\!\left(
\frac{c\theta}{1-\theta}
\right)
\]
and
\[
\Phi_{\theta,c}(u_*)
=
c(\theta u_*-1).
\]
Thus the maximum is nonpositive exactly when
\[
u_*\le\frac1\theta,
\]
equivalently
\[
c
\le
\frac{1-\theta}{\theta}e^{1/\theta}
=
A_-(\theta).
\]
This proves the decreasing phase and, by strict concavity, the two-root sign pattern
\[
-,+,-
\]
when \(c>A_-(\theta)\).

Finally, when
\[
\theta=1,
\]
the derivative sign reduces to the sign of \(c\), exactly as stated in the source.

## Verification
The included checker evaluates the exact derivative factor \(\Phi_{\theta,c}\), the two threshold functions, and representative hazards at high precision.

For the source's simulation parameters
\[
(\alpha,\theta,\gamma)=(0.03,2.52,0.03),
\]
it verifies that the parameter lies below the corrected increasing-hazard threshold, finds the two positive roots of \(\Phi\), and confirms the derivative sign sequence
\[
+,-,+.
\]

It also checks two simple independent counterexamples to the published theorem:

for
\[
(\alpha,\theta,\gamma,x)=(0.01,2,1,1),
\]
the source predicts increasing hazard, but
\[
\Phi(1)
=
e-2.94<0;
\]

for
\[
(\alpha,\theta,\gamma,x)=(5,1/2,1,4),
\]
the source predicts decreasing hazard, but
\[
\Phi(2)
=
4.5-\frac{e^2}{2}>0.
\]

These numerical evaluations are consistency checks. The complete phase classification follows from strict convexity or strict concavity of \(\Phi\).

## Relationship to prior work
Adlan, Haj Ahmad, and Aboshady introduce the MOPHL distribution and print the correct derivative factor
\[
\Phi(x)
=
(\theta-1)(e^{\gamma x^\theta}+c)
+
\theta\gamma c x^\theta
\]
in Appendix A. Their proof then argues from the signs at the two endpoints and eventual exponential dominance to a global sign conclusion. That step is invalid: a strictly convex function can be positive at both ends and negative in the middle, and a strictly concave function can be negative at both ends and positive in the middle.

The source consequently states that every \(\theta>1\) hazard is strictly increasing and every \(0<\theta<1\) hazard is strictly decreasing. It also interprets \(\theta\) as determining the global aging trend. Yet its simulation section describes
\[
(\alpha,\theta,\gamma)=(0.03,2.52,0.03)
\]
as having a non-monotonic hazard. The corrected phase boundary resolves that internal inconsistency exactly.

Earlier Marshall–Olkin lifetime models are known to permit non-monotonic hazard shapes for suitable parameters, so the existence of non-monotonicity after a Marshall–Olkin transformation is not itself unexpected. However, the literature checked did not supply the exact MOPHL thresholds above or a correction of Theorem 1.

Focused searches using the exact DOI, MOPHL name, theorem terminology, hazard-shape aliases, and the joint \((\alpha,\theta)\) phase boundary did not locate a published corrigendum or an equivalent model-specific result.

## Limitations
The finding classifies the hazard derivative completely but does not classify all possible density shapes.

The turning-point locations in the non-monotonic regions are defined by two scalar roots of \(\Phi_{\theta,c}\); no claim is made that those roots have a simpler elementary closed form.

The source's statistical estimation procedures are not recomputed. Their interpretation by hazard regime should, however, use the corrected joint parameter phase diagram.

## References
1. R. Adlan, H. Haj Ahmad, and M. Aboshady, “The Marshall–Olkin Power Half-Logistic Distribution for Reliability Modeling of Degradation Data Under Generalized Hybrid Censoring,” Mathematics 14 (2026), 973. DOI: 10.3390/math14060973.
2. M. Mansoor, M. H. Tahir, G. M. Cordeiro, S. B. Provost, and A. Alzaatreh, “The Marshall-Olkin logistic-exponential distribution,” Communications in Statistics—Theory and Methods 48 (2019), 220–234. DOI: 10.1080/03610926.2017.1414254.
