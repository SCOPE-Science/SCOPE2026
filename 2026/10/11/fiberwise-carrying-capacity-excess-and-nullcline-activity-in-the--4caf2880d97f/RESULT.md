# Fiberwise carrying-capacity excess and nullcline activity in the Holling–Tanner oscillator
## Finding
Consider the classical positive Holling–Tanner predator–prey system
\[
\dot x
=
r x\left(1-\frac{x}{K}\right)
-
\frac{cxy}{x+h},
\qquad
\dot y
=
s y\left(1-\frac{y}{\gamma x}\right),
\]
with
\[
r>0,\quad K>0,\quad c>0,\quad h>0,\quad s>0,\quad \gamma>0.
\]
Here \(x\) is prey abundance, \(y\) is predator abundance, \(K\) is prey carrying capacity, the predation term has Holling type II saturation, and the predator has prey-dependent carrying capacity \(\gamma x\).

Let \(\mu\) be any compactly supported invariant Borel probability measure whose support lies in the strictly positive quadrant. Define the prey-nullcline function
\[
H(x)
=
\frac{r}{c}(x+h)\left(1-\frac{x}{K}\right).
\]
Then the two biological nullclines are exact stationary conditional calibrations:
\[
\boxed{
\mathbb E_\mu[y\mid x]=H(x)
}
\]
and
\[
\boxed{
\mathbb E_\mu\!\left[\frac1x\,\middle|\,y\right]
=
\frac{\gamma}{y}
}.
\]

Because \(y>0\), the first law forces
\[
\boxed{0<x<K\quad \mu\text{-almost surely}.}
\]
Thus no compact stationary state supported strictly inside the positive quadrant can charge the prey carrying-capacity line \(x=K\), even though that line is part of the usual forward-invariant boundary estimate.

The predator-fiber harmonic law has an exact nonnegative defect. For \(\mu\)-almost every predator abundance,
\[
\boxed{
\mathbb E_\mu[x\mid y]-\frac{y}{\gamma}
=
\mathbb E_\mu\!\left[
\frac{(x-y/\gamma)^2}{x}
\,\middle|\,y
\right]
}.
\]
Since
\[
\frac{\dot y}{y}
=
s\left(1-\frac{y}{\gamma x}\right),
\]
the same identity is
\[
\boxed{
\mathbb E_\mu[x\mid y]-\frac{y}{\gamma}
=
\frac1{s^2}
\mathbb E_\mu\!\left[
 x\left(\frac{\dot y}{y}\right)^2
\,\middle|\,y
\right]
\ge0
}.
\]
After averaging,
\[
\boxed{
\mathbb E_\mu[x]-\frac{\mathbb E_\mu[y]}{\gamma}
=
\frac1{s^2}
\mathbb E_\mu\!\left[
 x\left(\frac{\dot y}{y}\right)^2
\right]
\ge0
}.
\]
Equality holds exactly for the atom at the unique positive equilibrium.

The conditional laws also yield two exact activity decompositions. The first regression residual is
\[
y-H(x)
=
-\frac{x+h}{c}\frac{\dot x}{x},
\]
so
\[
\boxed{
\operatorname{Var}_\mu(y)
=
\operatorname{Var}_\mu(H(x))
+
\frac1{c^2}
\mathbb E_\mu\!\left[
(x+h)^2\left(\frac{\dot x}{x}\right)^2
\right]
}.
\]
The second residual is
\[
\frac1x-\frac{\gamma}{y}
=
-\frac{\gamma}{s}\frac{\dot y}{y^2},
\]
hence
\[
\boxed{
\operatorname{Var}_\mu\!\left(\frac1x\right)
=
\gamma^2\operatorname{Var}_\mu\!\left(\frac1y\right)
+
\frac{\gamma^2}{s^2}
\mathbb E_\mu\!\left[\frac{\dot y^2}{y^4}\right]
}.
\]
Each activity defect vanishes exactly for the positive equilibrium atom.

Therefore every non-equilibrium compact stationary state assigns positive mass to both sides of both classical nullclines:
\[
\mu\{y<H(x)\}>0,
\qquad
\mu\{y>H(x)\}>0,
\]
and
\[
\mu\{x>y/\gamma\}>0,
\qquad
\mu\{x<y/\gamma\}>0.
\]
In particular, every nonconstant positive periodic orbit crosses each nullcline at least twice per least period.

## Assumptions and scope
The invariant measure is supported on a compact subset of \((0,\infty)^2\). This supplies positive lower bounds for both coordinates and makes the logarithmic generator tests below regular.

No ergodicity assumption is imposed. The theorem applies simultaneously to positive equilibrium measures, periodic-orbit measures, and compact invariant mixtures.

Tanner's 1975 predator–prey work is the foundational source used for the archive date. Later Holling–Tanner literature establishes positive invariance, the unique positive equilibrium, global-stability criteria, one- and two-limit-cycle regimes, Hopf bifurcations, and canard cycles. Those orbit-geometric results are prior work.

A dedicated Holling–Tanner bifurcation article lists \(34C25\) first in its Mathematics Subject Classification, so that primary code is used here.

## Proof
Because the support is compact and contained in the positive quadrant, both \(x\) and \(y\) are bounded away from zero on the support.

Let \(\phi\) be any continuous function on the compact \(x\)-projection of the support. Choose a continuously differentiable function \(F\) with
\[
F'(x)=\frac{\phi(x)}{x}.
\]
For the flow generator \(L\),
\[
LF
=
\phi(x)
\left[
r\left(1-\frac{x}{K}\right)
-
\frac{cy}{x+h}
\right].
\]
Invariance gives
\[
\mathbb E_\mu[LF]=0
\]
for every \(\phi\), hence
\[
\mathbb E_\mu[y\mid x]
=
\frac{r}{c}(x+h)\left(1-\frac{x}{K}\right)
=H(x).
\]
Since the conditional expectation of the strictly positive random variable \(y\) is strictly positive almost surely, \(H(x)>0\) almost surely. All parameters and \(x+h\) are positive, so
\[
1-\frac{x}{K}>0
\]
almost surely, proving \(0<x<K\).

Now let \(\psi\) be any continuous function on the compact \(y\)-projection and choose \(G\) with
\[
G'(y)=\frac{\psi(y)}{s y}.
\]
Then
\[
LG
=
\psi(y)
\left(1-\frac{y}{\gamma x}\right).
\]
Stationarity for every \(\psi\) gives
\[
\mathbb E_\mu\!\left[\frac1x\,\middle|\,y\right]
=
\frac{\gamma}{y}.
\]

Set
\[
a_y=\frac{y}{\gamma}.
\]
Conditioning on \(y\), expand
\[
\frac{(x-a_y)^2}{x}
=
x-2a_y+\frac{a_y^2}{x}.
\]
Using
\[
\mathbb E[1/x\mid y]=1/a_y
\]
gives
\[
\mathbb E\!\left[\frac{(x-a_y)^2}{x}\,\middle|\,y\right]
=
\mathbb E[x\mid y]-a_y.
\]
Also,
\[
\frac{\dot y}{y}
=
s\frac{x-a_y}{x},
\]
so
\[
\frac{(x-a_y)^2}{x}
=
\frac{x}{s^2}
\left(\frac{\dot y}{y}\right)^2.
\]
This proves the conditional and global prey-excess formulas.

If their global defect vanishes, then
\[
x=\frac{y}{\gamma}
\]
almost surely. Thus \(\dot y=0\) on invariant support. Along every support trajectory, \(y\) is constant and then so is \(x=y/\gamma\); consequently every support point is an equilibrium.

The positive equilibrium has
\[
y_*=\gamma x_*
\]
where \(x_*\) solves
\[
r(x_*+h)\left(1-\frac{x_*}{K}\right)
=
c\gamma x_*.
\]
The left side minus the right side is a concave quadratic with positive constant term and negative leading coefficient. Its two roots have negative product, so exactly one root is positive. Its value is positive at \(x=0\) and negative at \(x=K\), hence
\[
0<x_*<K.
\]
Therefore the equality measure is exactly \(\delta_{(x_*,\gamma x_*)}\).

For the first variance identity, the conditional law says
\[
\mathbb E[y-H(x)\mid x]=0.
\]
The prey equation gives the pointwise residual formula
\[
y-H(x)
=
-\frac{x+h}{c}\frac{\dot x}{x}.
\]
Conditional orthogonality therefore yields the displayed Pythagorean variance decomposition.

For the second identity,
\[
\mathbb E\!\left[\frac1x-\frac{\gamma}{y}\,\middle|\,y\right]=0
\]
and the predator equation gives
\[
\frac1x-\frac{\gamma}{y}
=
-\frac{\gamma}{s}\frac{\dot y}{y^2}.
\]
A second conditional Pythagorean decomposition gives the reciprocal-variance law.

If the first activity defect vanishes, then \(\dot x=0\) on invariant support. Hence \(x\) is constant along every support trajectory and the prey equation fixes \(y=H(x)\), so the trajectory is an equilibrium. If the second defect vanishes, then \(\dot y=0\) and the preceding equality argument again gives equilibrium support. Thus each defect vanishes exactly at the unique positive equilibrium atom.

For a non-equilibrium invariant state, stationarity of \(\log x\) and \(\log y\) gives
\[
\mathbb E\!\left[\frac{\dot x}{x}\right]=0,
\qquad
\mathbb E\!\left[\frac{\dot y}{y}\right]=0.
\]
Each mean-square speed is positive, so each zero-mean speed takes both signs on sets of positive measure. Those sign changes are precisely the two-sided nullcline statements.

For a nonconstant periodic orbit, the normalized time measure is invariant. A continuous periodic speed with positive and negative values has at least two zeros in a least period, proving the crossing count for each nullcline.

## Verification
The packaged checker uses only the Python standard library and exact rational arithmetic.

It verifies the two pointwise regression-residual identities,
\[
y-H(x)
=
-\frac{x+h}{c}\frac{\dot x}{x}
\]
and
\[
\frac1x-\frac{\gamma}{y}
=
-\frac{\gamma}{s}\frac{\dot y}{y^2}.
\]

It checks the algebraic conditional defect
\[
\frac{(x-y/\gamma)^2}{x}
=
x-rac{2y}{\gamma}+rac{y^2}{\gamma^2x}
\]
and its conversion to the predator per-capita speed.

It also checks that the positive-equilibrium polynomial has negative root product and opposite signs at \(0\) and \(K\), which certifies a unique positive equilibrium in \((0,K)\).

The stored checker output is `VERIFY_OK`.

The conditional-expectation quantifiers, equality rigidity, and nullcline crossing conclusions are analytic arguments; no finite trajectory sampling is used as proof.

## Relationship to prior work
Tanner's 1975 article develops predator–prey models with intrinsic population growth rates, prey self-limitation, predator searching time, and cyclic behavior. It supplies the earliest checked day-resolved public source date for this model lineage.

Hsu and Huang prove global stability results for a class containing the Holling–Tanner model. Gasull, Kooij, and Torregrosa show that the model can have two limit cycles. Braza studies the two-Hopf bifurcation structure and the stable and unstable periodic branches, with population outbreaks as an application.

A complete open 2014 same-model study describes the classical prey logistic term, Holling type II predation, and predator logistic growth with prey-dependent carrying capacity. It reviews positive invariance, the unique positive equilibrium, global stability, one- and two-cycle results, and then proves a canard-cycle theorem for small predator growth rate. Targeted searches of that complete text found no occurrence of `conditional`, `variance`, `average`, or `stationary` matching the invariant-measure theorem here.

The accepted result concerns a different structural layer. The prey nullcline is an exact conditional mean predator abundance at every prey level, while the predator nullcline is an exact conditional harmonic calibration of prey abundance at every predator level. The latter yields a nonnegative fiberwise excess
\[
\mathbb E[x\mid y]-\frac{y}{\gamma},
\]
quantified exactly by predator per-capita activity. This is not implied by limit-cycle existence, uniqueness, bifurcation diagrams, or global equilibrium stability.

## Limitations
The theorem requires compact invariant support strictly inside the positive quadrant. Boundary equilibria and measures charging an extinction axis are outside its domain.

The result concerns the autonomous classical Holling–Tanner kinetics with constant positive parameters. Delays, harvesting, diffusion, feedback controls, stochastic forcing, and other model extensions are not covered.

It determines conditional means, a harmonic conditional moment, and selected variance defects, not the full invariant distribution, cycle period, or amplitude extrema.

The 1997 two-limit-cycle source was compared through its bibliographic record and accessible statement material rather than used for blanket whole-document noncoverage.

Because the generator identities are short, an equivalent weighted formulation could remain in older unindexed predator–prey literature.

## References
1. J. T. Tanner, “The Stability and the Intrinsic Growth Rates of Prey and Predator Populations,” *Ecology* 56, 855–867 (1975), DOI 10.2307/1936296.
2. S. B. Hsu and T. W. Huang, “Global Stability for a Class of Predator-Prey Systems,” *SIAM Journal on Applied Mathematics* 55, 763–783 (1995), DOI 10.1137/S0036139993253201.
3. A. Gasull, R. E. Kooij, and J. Torregrosa, “Limit Cycles in the Holling-Tanner Model,” *Publicacions Matemàtiques* 41, 149–167 (1997), DOI 10.5565/PUBLMAT_41197_09.
4. P. A. Braza, “The Bifurcation Structure of the Holling--Tanner Model for Predator-Prey Interactions Using Two-Timing,” *SIAM Journal on Applied Mathematics* 63, 889–904 (2003), DOI 10.1137/S0036139901393494.
5. C. Zheng, F. Zhang, and J. Li, “Canard Limit Cycle of the Holling-Tanner Model,” *Discrete Dynamics in Nature and Society* 2014, 856475 (2014), DOI 10.1155/2014/856475.
