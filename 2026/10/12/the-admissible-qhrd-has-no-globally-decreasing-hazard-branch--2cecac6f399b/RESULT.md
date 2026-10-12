# The admissible QHRD has no globally decreasing hazard branch
## Finding
The quadratic hazard rate distribution used in the source has
\[
h(y)=\alpha+\beta y+\lambda y^2,
\qquad y>0,
\]
with cumulative hazard
\[
H(y)=\alpha y+\frac{\beta}{2}y^2+\frac{\lambda}{3}y^3
\]
and survival
\[
R(y)=e^{-H(y)}.
\]

The source imposes
\[
\alpha\ge0,\qquad
\lambda\ge0,\qquad
\beta\ge-2\sqrt{\alpha\lambda}
\]
to keep the hazard nonnegative.

Under exactly these admissibility conditions, a globally decreasing hazard is impossible.

If
\[
\lambda=0,
\]
then the constraint becomes
\[
\beta\ge0.
\]
Hence
\[
h(y)=\alpha+\beta y
\]
is constant when \(\beta=0\) and increasing when \(\beta>0\). There is no admissible decreasing linear case.

If
\[
\lambda>0
\]
and
\[
\beta\ge0,
\]
then
\[
h'(y)=\beta+2\lambda y>0
\]
for every \(y>0\), so the hazard is increasing.

If
\[
\lambda>0
\]
and
\[
\beta<0,
\]
then
\[
h'(y)=0
\]
only at
\[
y_*=-\frac{\beta}{2\lambda}>0.
\]
The derivative is negative before \(y_*\) and positive after \(y_*\). Thus the only nonmonotone admissible shape is bathtub-shaped. Moreover,
\[
h(y_*)
=
\alpha-\frac{\beta^2}{4\lambda}
\ge0
\]
by the same admissibility condition.

Therefore the admissible shape classification is
\[
\boxed{
\text{constant/increasing, or bathtub; never globally decreasing and never inverted-bathtub.}
}
\]

The source states instead that
\[
\beta<0,\qquad\lambda=0
\]
produces a decreasing linear hazard that remains positive under the admissibility conditions. This is incompatible with its own parameter constraint.

The inconsistency is also present in Figure 3. The curve labeled “Decreasing (linear)” uses
\[
(\alpha,\beta,\lambda)=(3,-0.05,0).
\]
For this formal parameter triple,
\[
h(y)=3-0.05y,
\]
so
\[
h(60)=0
\]
and
\[
h(y)<0
\qquad(y>60).
\]
The cumulative hazard is
\[
H(y)=3y-0.025y^2.
\]
It reaches its maximum at \(y=60\), returns to zero at \(y=120\), and becomes negative for \(y>120\). Consequently,
\[
f(y)=h(y)e^{-H(y)}
\]
is negative for \(y>60\), while
\[
F(y)=1-e^{-H(y)}
\]
decreases on \((60,120)\), satisfies
\[
F(120)=0,
\]
and is negative for \(y>120\).

The finite plotting range in Figure 3 stops at \(y=30\), before the formal hazard reaches zero, which hides the loss of probability validity.

## Assumptions and scope
The support is
\[
y>0.
\]
The result uses the parameter constraints explicitly stated in the source:
\[
\alpha\ge0,\qquad
\lambda\ge0,\qquad
\beta\ge-2\sqrt{\alpha\lambda}.
\]

The all-zero parameter triple is excluded because it does not define a proper lifetime distribution.

The finding concerns the structural hazard-shape claim and Figure 3. It does not invalidate admissible parameter settings used elsewhere in the paper.

Negative \(\beta\) is permitted when \(\lambda>0\) and the quadratic minimum remains nonnegative; those cases yield bathtub hazards rather than globally decreasing hazards.

## Proof
Differentiate the hazard:
\[
h'(y)=\beta+2\lambda y.
\]

When \(\lambda=0\), admissibility gives
\[
\beta\ge-2\sqrt{\alpha\cdot0}=0.
\]
Hence \(h'(y)=\beta\ge0\).

When \(\lambda>0\) and \(\beta\ge0\), one has
\[
h'(y)>0
\]
for \(y>0\).

When \(\lambda>0\) and \(\beta<0\), the derivative is affine with positive slope \(2\lambda\), so it has exactly one zero:
\[
y_*=-\frac{\beta}{2\lambda}.
\]
Thus it changes sign from negative to positive, never from positive to negative. The minimum value is
\[
h(y_*)
=
\alpha-\frac{\beta^2}{4\lambda}.
\]
The stated parameter constraint is equivalent, in this negative-\(\beta\) case, to
\[
\beta^2\le4\alpha\lambda,
\]
so
\[
h(y_*)\ge0.
\]
This proves the complete classification.

For the Figure 3 parameters,
\[
H(y)=3y-\frac{0.05}{2}y^2
=
3y-0.025y^2.
\]
Since
\[
H'(y)=h(y),
\]
the survival derivative is
\[
R'(y)=-h(y)R(y).
\]
After \(y=60\), the formal hazard is negative, so the formal survival increases rather than decreases and the density \(f=hR\) is negative. Since
\[
H(120)=0,
\]
one has \(F(120)=0\); after \(120\), \(H<0\) and hence \(F<0\).

## Verification
The bundled checker verifies the full analytic case split and the source's Figure 3 example.

It samples admissible parameter triples across the increasing and bathtub regimes and confirms nonnegative hazards over dense positive grids.

For the decreasing-curve parameters, it verifies:
\[
h(60)=0,
\]
negative density immediately after \(60\),
\[
F(120)=0,
\]
and negative CDF values after \(120\).

It also checks representative admissible negative-\(\beta\), positive-\(\lambda\) triples and confirms the bathtub minimum formula.

The finite computations supplement the exact derivative and parameter-constraint proof.

## Relationship to prior work
The primary source gives the QHRD density, CDF, survival, hazard, and admissibility condition, then immediately asserts a decreasing linear branch with \(\beta<0\) and \(\lambda=0\). Those two statements cannot both hold.

A closely related 2025 QHRD inference paper by several of the same authors uses the same admissibility condition and advertises increasing, decreasing, bathtub, and inverted-bathtub hazard shapes. Its mathematical definitions do not repair the decreasing branch. The present result gives the exact admissible classification and identifies the concrete invalid Figure 3 parameter triple in the 2026 article.

The classical linear-failure-rate literature studies the special case
\[
h(y)=\alpha+\beta y
\]
as a lifetime distribution. On unbounded support, a negative slope cannot remain nonnegative for all \(y>0\). That general fact supports the boundary case but does not by itself provide the current article's full quadratic classification or identify its plotted invalid example.

Focused searches using the target DOI, QHRD name, decreasing-hazard terminology, the admissibility inequality, the Figure 3 parameters, and correction terminology did not locate a published correction of this source-specific contradiction.

## Limitations
The result corrects the global hazard-shape classification, not the whole inferential analysis.

A decreasing segment is possible in an admissible bathtub case with \(\beta<0\) and \(\lambda>0\); what is excluded is a hazard that decreases over the entire positive support.

The source's finite-window Figure 3 curve is positive on its displayed interval, but that does not make the corresponding unbounded-support lifetime law valid.

A recent or unindexed correction could exist outside the sources examined.

## References
1. H. Haj Ahmad, M. N. Mousa, M. E. Moshref, N. Youns, and M. M. M. Mansour, “Reliability inference of the quadratic hazard rate model under step-stress partially accelerated life testing with progressive Type-II censoring,” AIMS Mathematics 11 (2026), 6106–6140. DOI: 10.3934/math.2026253.
2. M. Nagy, A. H. Mansi, M. N. Mousa, M. E. Moshref, N. Youns, and M. M. M. Mansour, “On estimation of the quadratic hazard rate model parameters: Simulation and application,” AIP Advances 15 (2025), 055126. DOI: 10.1063/5.0257356.
3. L. J. Bain, “Analysis for the linear failure-rate life-testing distribution,” Technometrics 16 (1974), 551–559. DOI: 10.1080/00401706.1974.10489237.
