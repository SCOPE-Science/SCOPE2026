# The predator-free endemic branch is quadratic and unique in a delayed eco-epidemic model

## Finding

Consider the model
\[
\dot x=rx\left(1-\frac{x+y}{K}\right)-\frac{\beta xy}{\alpha+y}-\frac{mxz}{(a+x)(b+z)},
\]
\[
\dot y=\frac{\beta xy}{\alpha+y}-\frac{nyz}{cz+y}-\nu y,
\]
with the predator equation as printed in the source. A predator-free endemic equilibrium has the form \((x^*,y^*,0)\) with \(x^*>0\) and \(y^*>0\).

Every such equilibrium exists if and only if
\[
\mathcal R_I:=\frac{\beta K}{\alpha\nu}>1,
\]
and, when it exists, it is unique. Its infected-prey coordinate is the unique positive root of
\[
F(y)=r(\alpha+y)\left[\beta K-\alpha\nu-(\beta+\nu)y\right]-\beta^2Ky,
\]
and
\[
x^*=\frac{\nu(\alpha+y^*)}{\beta}.
\]
Thus the predator-free endemic branch is governed by a quadratic equation, not by the cubic printed as Eq. (4) in the source.

Writing
\[
A=\beta K-\alpha\nu,
\qquad
B=\beta^2K-r(\beta K-\alpha\beta-2\alpha\nu),
\]
the unique positive root for \(A>0\) is
\[
y^*=\frac{-B+\sqrt{B^2+4r^2\alpha(\beta+\nu)A}}{2r(\beta+\nu)}.
\]

The source's Proposition 1 states feasibility under \(\beta>\nu\alpha\). That condition is not sufficient for the printed model. For example,
\[
r=\alpha=\nu=1,\qquad \beta=2,\qquad K=\frac25
\]
satisfies \(\beta>\nu\alpha\), but gives \(\mathcal R_I=4/5<1\) and
\[
F(y)=-\frac{15y^2+24y+1}5<0
\]
for every \(y>0\). Hence no predator-free endemic equilibrium exists in this case.

## Assumptions and scope

All parameters appearing in the two prey equations are positive, as in the biological model. The claim concerns only equilibria with predator coordinate equal to zero and both prey coordinates strictly positive. The gestation delay is irrelevant to this boundary-equilibrium calculation because the predator coordinate is identically zero at equilibrium.

The quantity \(\mathcal R_I\) is not introduced as a new global reproduction number. It is the local invasion ratio of infected prey at the prey-only equilibrium \((K,0,0)\), because the linearized infected-prey equation there is
\[
\dot y=\left(\frac{\beta K}{\alpha}-\nu\right)y+o(y).
\]

## Proof

Set \(z=0\), \(x>0\), and \(y>0\). From the infected-prey equilibrium equation,
\[
0=\frac{\beta xy}{\alpha+y}-\nu y,
\]
we obtain
\[
x=\frac{\nu(\alpha+y)}{\beta}.
\]
The susceptible-prey equilibrium equation, divided by \(x>0\), is
\[
r\left(1-\frac{x+y}{K}\right)=\frac{\beta y}{\alpha+y}.
\]
Substituting the expression for \(x\) and multiplying by \(\beta K(\alpha+y)\) gives exactly
\[
F(y)=r(\alpha+y)\left[\beta K-\alpha\nu-(\beta+\nu)y\right]-\beta^2Ky=0.
\]
This is quadratic in \(y\).

If \(\beta K\le\alpha\nu\), then for every \(y>0\),
\[
\beta K-\alpha\nu-(\beta+\nu)y<0,
\]
so both terms in \(F(y)\) are strictly negative. Therefore no positive root exists.

Now suppose \(A=\beta K-\alpha\nu>0\). Then \(F(0)=r\alpha A>0\), while \(F(y)\to-\infty\) as \(y\to\infty\), so a positive root exists. Multiplying by \(-1\) gives
\[
r(\beta+\nu)y^2+By-r\alpha A=0.
\]
Its leading coefficient is positive and its constant term is negative, so its two real roots have opposite signs. Hence exactly one root is positive. The quadratic formula gives the expression stated above.

Finally, linearizing the infected-prey equation at \((K,0,0)\) yields growth rate \(\beta K/\alpha-\nu\). Therefore the same condition \(\mathcal R_I>1\) is precisely the condition for infected prey to invade the prey-only equilibrium.

## Verification

The bundled script symbolically reconstructs the quadratic from the printed two prey equations and checks the exact counterexample
\[
r=\alpha=\nu=1,\qquad \beta=2,\qquad K=\frac25.
\]
It also checks a feasible case
\[
r=\alpha=\nu=1,\qquad \beta=2,\qquad K=1,
\]
for which
\[
F(y)=1-6y-3y^2
\]
and the unique positive root is
\[
y^*=-1+\frac{2\sqrt3}3,
\qquad
x^*=\frac1{\sqrt3}.
\]
Substitution into both predator-free prey equilibrium equations gives zero exactly.

## Relationship to prior work

Sarwardi, Mollah, Raezah, and Al Basir (2024), DOI 10.3934/math.20241356, print the model above, then state that the predator-free endemic equilibrium is determined by a cubic Eq. (4), give a sign table allowing up to three positive roots, and state Proposition 1 with condition \(\beta>\nu\alpha\). Direct elimination from their printed model instead gives the quadratic and threshold proved here.

Naji and Hasan (2012) study a different Crowley--Martin eco-epidemiological model. In its predator-absent SIS subsystem, the endemic equilibrium is unique above its infection threshold. This is qualitatively consistent with a single predator-free endemic branch, but their model uses mass-action incidence together with recovery and therefore does not imply the present saturated-incidence calculation.

Mortoja, Panja, and Mondal (2019), DOI 10.1016/j.egg.2018.100035, study a related delayed disease-in-prey model with Crowley--Martin predation and nonlinear incidence. The accessible abstract establishes the model family and equilibrium analysis but does not expose a statement equivalent to the quadratic elimination and exact threshold above. Because the full text was not lawfully available in the inspected sources, it remains a residual literature risk rather than evidence of coverage.

## Limitations

The result corrects and classifies only the predator-free endemic equilibrium of the printed 2024 model. It does not assess the interior equilibrium, the Hopf-bifurcation calculations, or the numerical delay simulations. It also does not claim that the source authors' unpublished algebra or code used the same cubic as the printed article.

## References

1. S. Sarwardi, H. Mollah, A. A. Raezah, F. Al Basir, “Direction and stability of Hopf bifurcation in an eco-epidemic model with disease in prey and predator gestation delay using Crowley-Martin functional response,” AIMS Mathematics 9 (2024), 27930–27954. DOI: 10.3934/math.20241356.
2. R. K. Naji, K. A. Hasan, “The dynamics of prey-predator model with disease in prey,” Journal of Mathematical and Computational Science 2 (2012), 1052–1072.
3. S. G. Mortoja, P. Panja, S. K. Mondal, “Dynamics of a predator-prey model with nonlinear incidence rate, Crowley-Martin type functional response and disease in prey population,” Ecological Genetics and Genomics 10 (2019), 100035. DOI: 10.1016/j.egg.2018.100035.
