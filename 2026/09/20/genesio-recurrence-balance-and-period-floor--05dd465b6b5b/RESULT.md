# Exact recurrence balances and a sharp period floor for the Genesio system

Consider the Genesio system
\[
\dot x=y,\qquad \dot y=z,\qquad \dot z=-cx-by-az+x^2,
\tag{1}
\]
with real parameters \(a,b,c\). Equivalently,
\[
x'''+a x''+b x'+cx-x^2=0.
\tag{2}
\]

## Main result

Define
\[
\mathcal J(x,y,z)=yz+\frac a2y^2+\frac c2x^2-\frac13x^3.
\tag{3}
\]
Then every classical solution of (1) satisfies the exact balance law
\[
\boxed{\dot{\mathcal J}=z^2-b y^2.}
\tag{4}
\]
Consequently:

1. **Bounded-orbit Cesaro balance.** Every bounded forward solution is forward global and obeys
   \[
   \lim_{T\to\infty}\frac1T\int_0^T\bigl(z(t)^2-b y(t)^2\bigr)\,dt=0.
   \tag{5}
   \]

2. **Compact invariant-measure balance.** Every compactly supported invariant probability measure \(\mu\) satisfies
   \[
   \int z^2\,d\mu=b\int y^2\,d\mu,
   \qquad
   \int y\,d\mu=\int z\,d\mu=0,
   \qquad
   \int x^2\,d\mu=c\int x\,d\mu.
   \tag{6}
   \]
   Hence any invariant measure not supported on the equilibrium set requires \(b>0\). If \(c=0\), the only compactly supported invariant probability measure is the Dirac mass at the origin. If \(c\ne0\), every invariant measure that is not a Dirac equilibrium measure has mean \(m=\int x\,d\mu\) strictly between the two equilibrium abscissae \(0\) and \(c\), because
   \[
   \operatorname{Var}_\mu(x)=cm-m^2>0.
   \tag{7}
   \]

3. **Nonpositive-\(b\) recurrence barrier.** If \(b\le0\), every bounded forward solution converges to one of the equilibria
   \[
   (0,0,0),\qquad (c,0,0),
   \tag{8}
   \]
   with the two coinciding when \(c=0\). In particular, for \(b\le0\) there are no bounded non-equilibrium periodic, quasiperiodic, or chaotic recurrent trajectories.

4. **Strict universal period floor.** Every nonconstant periodic orbit has \(b>0\), \(c\ne0\), and minimal period \(P\) satisfying
   \[
   \boxed{P>\frac{2\pi}{\sqrt b}.}
   \tag{9}
   \]
   The bound is locally sharp: the known Hopf locus has linear frequency \(\sqrt b\), so along any nondegenerate Hopf branch the cycle periods tend to \(2\pi/\sqrt b\).

Thus the same parameter \(b\) that appears as the linear velocity coefficient fixes an exact RMS acceleration/velocity ratio on every compact recurrent statistical state and gives the optimal unattained lower edge of the period spectrum.

## Proof

Differentiate (3) along (1):
\[
\begin{aligned}
\dot{\mathcal J}
&=\dot y\,z+y\dot z+a y\dot y+c x\dot x-x^2\dot x\\
&=z^2+y(-cx-by-az+x^2)+ayz+cxy-x^2y\\
&=z^2-by^2,
\end{aligned}
\]
which proves (4). The accompanying symbolic check obtains an identically zero residual.

If a forward orbit is bounded, polynomial local existence plus boundedness prevents finite-time escape, so the solution is forward global. The function \(\mathcal J\) is bounded on the orbit closure. Integrating (4) gives
\[
\frac{\mathcal J(T)-\mathcal J(0)}{T}
=
\frac1T\int_0^T(z^2-by^2)\,dt,
\]
and the left side tends to zero, proving (5).

For a compactly supported invariant probability measure, integration of the generator identity \(L\mathcal J=z^2-by^2\) gives the first equality in (6). The identities \(Lx=y\), \(Ly=z\), and
\[
Lz=-cx-by-az+x^2
\]
give the remaining equalities. If \(b<0\), the first identity in (6) is \(\int z^2d\mu+|b|\int y^2d\mu=0\), so \(y=z=0\) on the support and invariance forces \(x(x-c)=0\). If \(b=0\), the same identity gives \(z=0\) on the support. Along an invariant trajectory inside this compact support, \(y\) is then constant; nonzero \(y\) would make \(x\) drift linearly and leave every compact set, so \(y=0\), and invariance again forces \(x(x-c)=0\). Thus any compact invariant measure not supported on equilibria requires \(b>0\). If \(c=0\), the last identity gives \(\int x^2d\mu=0\), and invariance then successively forces \(y=z=0\), so \(\mu=\delta_{(0,0,0)}\). For \(c\ne0\), (7) follows from \(\int x^2d\mu=cm\); positive variance for every non-Dirac invariant measure gives strict location of the mean between \(0\) and \(c\).

For the convergence assertion, set \(W=-\mathcal J\). When \(b\le0\),
\[
\dot W=-z^2+b y^2\le0.
\tag{10}
\]
A bounded forward orbit has compact closure, so LaSalle's invariance principle applies. If \(b<0\), the zero-derivative set in (10) has \(y=z=0\); invariance then requires \(x(x-c)=0\). If \(b=0\), the zero-derivative set has \(z=0\). A trajectory that remains there has constant \(y\); boundedness forces \(y=0\), and invariance again requires \(x(x-c)=0\). Hence the omega-limit set lies in the finite equilibrium set. An omega-limit set of a precompact continuous-time orbit is connected, so it consists of one equilibrium, proving convergence.

Finally let a nonconstant periodic orbit have minimal period \(P\). Integrating (4) over one period gives
\[
\int_0^Pz^2dt=b\int_0^P y^2dt.
\tag{11}
\]
Because a nonconstant orbit has \(y\not\equiv0\), this implies \(b>0\). Since \(y=x'\) is periodic and has zero mean, the sharp Wirtinger inequality gives
\[
\int_0^P z^2dt=\int_0^P(y')^2dt
\ge \left(\frac{2\pi}{P}\right)^2\int_0^P y^2dt.
\tag{12}
\]
Combining (11) and (12) yields \(P\ge2\pi/\sqrt b\).

Equality in (12) would force \(y\) to be a pure first harmonic. Writing \(\omega=\sqrt b\), this makes
\[
x(t)=m+R\cos(\omega t-\phi),\qquad R>0.
\]
Then \(x'''+bx'=0\), so (2) reduces to
\[
a x''+cx-x^2=0.
\]
The second Fourier harmonic of the left side has coefficient \(-R^2/2\), because the linear terms contain only the constant and first harmonic. This is impossible for \(R>0\). Therefore equality cannot occur and (9) is strict. Integrating \(\dot z\) over the orbit also gives \(\int x^2dt=c\int xdt\); hence \(c=0\) would force \(x\equiv0\), so every nonconstant cycle also requires \(c\ne0\).

At the known Hopf locus \(c=ab\) at the origin (and \(c=-ab\) at the second equilibrium), the linear pair is \(\pm i\sqrt b\). Therefore any nondegenerate Hopf branch has periods converging to \(2\pi/\sqrt b\), showing that the strict bound has the correct sharp limiting constant.

## Relation to prior literature

Genesio and Tesi introduced this three-dimensional quadratic jerk system in the context of harmonic-balance prediction of chaotic motion. Later work has concentrated on local stability, numerical bifurcation structure, synchronization/control, integrability, dynamics at infinity, and Hopf or zero-Hopf bifurcations.

A 2013 numerical study of a normalized Genesio jerk equation reported that certain negative-parameter regions produced no bounded attracting dynamics, while its positive region displayed limit cycles, period doubling, and chaos. The result above supplies an exact obstruction in the standard coordinates: whenever \(b\le0\), every bounded forward trajectory converges to equilibrium, regardless of \(a\) and \(c\).

The 2025 global analysis of Valls proves the Hopf loci and identifies the linear Hopf frequency \(\sqrt b\), while its global theorem concerns the Poincare sphere at infinity and its integrability results concern algebraic surfaces and first integrals. The present period theorem is complementary: every actual nonconstant periodic orbit has period strictly larger than the linear Hopf value, although that value is approached at a nondegenerate Hopf onset.

To the best of our knowledge, the checked Genesio literature does not state the combination of (4)--(9): the compact invariant-measure RMS identity, the global bounded-orbit recurrence barrier for \(b\le0\), and the strict sharp period floor. Classical third-order stability literature, including work descending from Barbasin's method, is a residual source of possible equivalent Lyapunov identities; the novelty claim is therefore placed primarily on these global recurrence and period consequences for the Genesio system rather than on the mere algebraic act of differentiating (3).

## Limitations

The convergence result is conditional on forward boundedness; it does not claim that every Genesio trajectory is bounded. It also does not exclude compact invariant sets made only from equilibria and connecting orbits when those exist; the recurrence conclusion concerns non-equilibrium recurrent trajectories and invariant statistics.

Originality is to the best of our knowledge. The full text of the 1952 Barbasin paper was not inspected, and older third-order stability work may contain an equivalent auxiliary function for a broader scalar equation. The accessible 2013 stability paper for the Genesio system states that Lyapunov functions are used to estimate regions of attraction, but the inspected material does not state the invariant-measure identities or strict period lower bound. The 2025 Valls paper was inspected in searchable full text and did not contain the invariant-measure, bounded-orbit, or minimum-period statements located here.

## Reproducibility

`artifacts/verify_genesio_balance.py` verifies the polynomial identity (4) symbolically and checks the nonzero second-harmonic obstruction used to make the period bound strict. `artifacts/verification.txt` records the resulting exact outputs.

## References

1. R. Genesio and A. Tesi, "Harmonic balance methods for the analysis of chaotic dynamics in nonlinear systems," *Automatica* 28 (1992), 531--548. https://doi.org/10.1016/0005-1098(92)90177-H
2. O. Umut and S. Yasar, "A Simple Jerky Dynamics, Genesio System," *International Journal of Modern Nonlinear Theory and Application* 2 (2013), 60--68. https://doi.org/10.4236/ijmnta.2013.21007
3. O. Umut, "On the Stability of Genesio System," *Far East Journal of Dynamical Systems* 23 (2013/2014). https://doi.org/10.17654/0972111813014
4. P. T. Cardin and J. Llibre, "Transcritical and zero-Hopf bifurcations in the Genesio system," *Nonlinear Dynamics* 88 (2017), 547--553. https://doi.org/10.1007/s11071-016-3259-2
5. M. Diab, J. L. G. Guirao and J. A. Vera, "Zero-Hopf Bifurcation in a Generalized Genesio Differential Equation," *Mathematics* 9 (2021), 354. https://doi.org/10.3390/math9040354
6. C. Valls, "Global dynamical aspects and integrability analysis of the Genesio system," *Discrete and Continuous Dynamical Systems - B* 30 (2025), 3206--3221. https://doi.org/10.3934/dcdsb.2025016
7. E. A. Barbasin, "On the stability of the solution of a certain nonlinear equation of third order," *Priklad. Mat. Mekh.* 16 (1952), 629--632.
