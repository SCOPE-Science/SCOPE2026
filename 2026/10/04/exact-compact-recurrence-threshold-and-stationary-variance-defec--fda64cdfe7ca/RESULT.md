# Exact compact-recurrence threshold and stationary variance defect for an error-function jerk flow
## Finding
Consider the three-dimensional flow
\[
\dot x=y,\qquad \dot y=z,\qquad
\dot z=\mu-a x-\frac{31}{20}y-\frac{113}{100}z+xy-\frac{33}{100}x^2-\frac52 z\operatorname{erf}(z),
\]
where the printed decimal coefficients in the source are interpreted as the exact decimals shown above. Define
\[
\Delta=a^2+\frac{33}{25}\mu.
\]
A nonempty compact invariant set exists if and only if \(\Delta\ge0\).

At \(\Delta=0\), the unique compactly supported invariant probability measure is the Dirac mass at the double equilibrium \(r_0=-\frac{50}{33}a\).

For \(\Delta>0\), define
\[
r_\pm=\frac{50}{33}\left(-a\pm\sqrt{\Delta}\right).
\]
Every compactly supported invariant Borel probability measure \(\nu\), with \(m=\int x\,d\nu\), satisfies
\[
\int y\,d\nu=\int z\,d\nu=\int xy\,d\nu=0
\]
and the exact stationary defect identity
\[
\frac{33}{100}\operatorname{Var}_\nu(x)
+\frac52\int z\operatorname{erf}(z)\,d\nu
=\frac{33}{100}(r_+-m)(m-r_-).
\]
Hence \(r_-\le m\le r_+\), and equality at an endpoint occurs only for the Dirac mass at the corresponding equilibrium. Moreover,
\[
\operatorname{Var}_\nu(x)\le (r_+-m)(m-r_-)
\le \frac{(r_+-r_-)^2}4.
\]
The final variance bound is sharp over all invariant probability measures: equality is attained by the equal mixture of the two equilibrium Dirac masses. It is strict for every non-equilibrium ergodic invariant measure.

For the hidden-chaos parameter choice reported by Rasul and Salih, \(\mu=0\) and \(a=1.69=169/100\), the two equilibria have \(x\)-coordinates \(-169/33\) and \(0\). Therefore every compactly supported non-equilibrium ergodic invariant measure satisfies
\[
-\frac{169}{33}<\int x\,d\nu<0,
\qquad
\sigma_x<\frac{169}{66}\approx2.5606060606.
\]

## Assumptions and scope
The theorem concerns the special jerk family printed as equation (4.1) by Rasul and Salih. The coefficients \(1.55\), \(1.13\), \(0.33\), and \(2.5\) are treated as the exact decimal values \(31/20\), \(113/100\), \(33/100\), and \(5/2\). The parameters \(a\) and \(\mu\) are arbitrary real numbers. The measure statements apply to compactly supported invariant Borel probability measures for the autonomous flow. The compact-invariant-set statement is about nonempty compact invariant sets.

No assertion is made that the numerically displayed hidden attractor in the source has been rigorously established as a compact invariant chaotic set. Rather, if a compact invariant statistical state is carried by that regime, it must obey the identities and bounds above. No claim is made about unbounded trajectories, finite-time transients, global existence outside compact invariant sets, or the absence of homoclinic or other nonrecurrent compact orbit closures at the critical parameter.

## Proof
Let \(L\) denote the generator of the flow and let \(\nu\) be a compactly supported invariant probability measure. Compact support justifies integrating derivatives of the polynomial test functions used below. Invariance gives \(\int Lf\,d\nu=0\).

Taking \(f=x\), \(f=y\), and \(f=x^2/2\) gives, respectively,
\[
\int y\,d\nu=0,\qquad
\int z\,d\nu=0,\qquad
\int xy\,d\nu=0.
\]
Write \(m=\int x\,d\nu\). Averaging the \(z\)-equation and using the three preceding identities gives
\[
0=\mu-am-\frac{33}{100}\int x^2\,d\nu
-\frac52\int z\operatorname{erf}(z)\,d\nu.
\]
Since \(\int x^2\,d\nu=m^2+\operatorname{Var}_\nu(x)\), this becomes
\[
\frac{33}{100}m^2+am-\mu
+\frac{33}{100}\operatorname{Var}_\nu(x)
+\frac52\int z\operatorname{erf}(z)\,d\nu=0.
\]
The first three terms factor as
\[
\frac{33}{100}(m-r_-)(m-r_+)
\]
when \(\Delta\ge0\), which yields the defect identity.

The function \(s\mapsto s\operatorname{erf}(s)\) is nonnegative on \(\mathbb R\), vanishing only at \(s=0\). Therefore both terms on the left of the defect identity are nonnegative. This proves \(r_-\le m\le r_+\) and the first variance bound. The second follows from the elementary quadratic estimate
\[
(r_+-m)(m-r_-)\le\frac{(r_+-r_-)^2}4.
\]

If \(\Delta<0\), the quadratic \(\frac{33}{100}m^2+am-\mu\) is strictly positive for every real \(m\). The averaged equation is then impossible, because its remaining terms are nonnegative. Thus no compactly supported invariant probability measure exists. Any nonempty compact invariant set carries an invariant probability measure by the usual time-average compactness argument, so no nonempty compact invariant set can exist. Conversely, if \(\Delta\ge0\), at least one equilibrium exists, and that singleton is a compact invariant set. This proves the threshold equivalence.

At \(\Delta=0\), the averaged equation is a sum of nonnegative terms,
\[
\frac{33}{100}(m-r_0)^2
+\frac{33}{100}\operatorname{Var}_\nu(x)
+\frac52\int z\operatorname{erf}(z)\,d\nu=0.
\]
Hence \(x=r_0\) and \(z=0\) almost surely. Applying invariance to \(f=xy\) gives
\[
0=\int L(xy)\,d\nu=\int (y^2+xz)\,d\nu=\int y^2\,d\nu,
\]
so \(y=0\) almost surely. The measure is therefore the Dirac mass at the double equilibrium.

The same argument proves endpoint rigidity for \(\Delta>0\): if \(m=r_-\) or \(m=r_+\), the defect identity forces \(x\) constant and \(z=0\), and the \(xy\) test function forces \(y=0\). Thus the measure is the corresponding equilibrium Dirac mass.

The maximum of \((r_+-m)(m-r_-)\) is attained at \(m=(r_-+r_+)/2\). The invariant measure \(\frac12\delta_{(r_-,0,0)}+\frac12\delta_{(r_+,0,0)}\) has this mean and variance \((r_+-r_-)^2/4\), proving sharpness over all invariant measures. An ergodic invariant measure with equality would have to be this nonergodic two-point mixture or an equilibrium Dirac, so every non-equilibrium ergodic invariant measure satisfies the strict bound.

For \(\mu=0\) and \(a=169/100\), one has \(\Delta=(169/100)^2\), \(r_-=-169/33\), \(r_+=0\), and \((r_+-r_-)/2=169/66\), yielding the stated hidden-regime bounds.

## Verification
A dependency-free exact-rational checker, `verify.py`, recomputes the coefficient normalization, discriminant factor, equilibrium coordinates, critical forcing for the published hidden parameter, and the half-gap standard-deviation bound. It returns `VERIFY_OK` when these exact arithmetic checks pass. The invariant-measure implications are proved analytically above; the script is not used as a substitute for the infinite-time argument.

The critical logical checks were also performed symbolically: the stationary identities follow from \(Lx\), \(Ly\), \(L(x^2/2)\), and \(L(xy)\); the sign of \(z\operatorname{erf}(z)\) is global; and the compact-set obstruction uses existence of an invariant probability measure on a compact invariant set, not a finite trajectory computation.

## Relationship to prior work
Rasul and Salih introduce the error-function jerk system above, calculate its equilibria and local bifurcations, and numerically study self-excited and hidden chaotic regimes. Their reported hidden case uses \(\mu=0\) and \(a=1.69\). The source does not state the compact-recurrence threshold, the invariant-measure defect identity, the mean interval, the variance envelope, or the critical uniqueness statement proved here.

Liu, Sang, Wang, and Ahmad study hidden and self-excited attractors in quadratic polynomial jerk systems using local bifurcation and numerical diagnostics. That polynomial class does not contain the nonpolynomial \(z\operatorname{erf}(z)\) damping term used here, and the cited work does not imply this stationary defect identity. Llibre and Makhlouf study zero-Hopf bifurcations for the full quadratic polynomial jerk family; again, the present error-function term lies outside that class.

A search of the published-finding corpus mathematical research index for the exact source, the error-function term, invariant-measure formulations, and equivalent mean/variance claims returned no same-system result. The closest indexed analogue was an exact compact-recurrence threshold and variance-gap law for the Rössler system; its vector field and defect observable are different, and no conjugacy or reduction was found that would imply the present theorem.

## Limitations
The theorem is conditional on the vector field as printed in equation (4.1), with the displayed decimals treated exactly. It does not certify the existence, ergodicity, or numerical Lyapunov exponents of any particular chaotic attractor. It does not classify all compact invariant sets at the critical parameter: uniqueness is proved for compactly supported invariant probability measures, so nonrecurrent compact orbit structures are not excluded by the argument. Searches cannot establish absolute novelty against every unpublished or poorly indexed source; the residual originality risk is therefore nonzero.

## References
1. T. I. Rasul and R. H. Salih, “Bifurcation analysis with self-excited and hidden attractors for a chaotic jerk system,” *Journal of Mathematics and Computer Science* 35(3) (2024), 319–335. DOI: 10.22436/jmcs.035.03.05. First verified public date: 2024-05-22.
2. M. Liu, B. Sang, N. Wang, and I. Ahmad, “Chaotic Dynamics by Some Quadratic Jerk Systems,” *Axioms* 10(3) (2021), 227. DOI: 10.3390/axioms10030227.
3. J. Llibre and A. Makhlouf, “The Zero–Hopf bifurcations of the quadratic polynomial differential jerk systems in \(\mathbb R^3\),” *Aequationes Mathematicae* 99 (2025), 1995–2007. DOI: 10.1007/s00010-025-01182-5.
