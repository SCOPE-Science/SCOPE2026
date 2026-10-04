# Stationary height circle and slab-crossing recurrence in the T-system
## Finding
Consider the normalized T-system
\[
\dot x=y-x,\qquad \dot y=mx-xz,\qquad \dot z=-nz+xy,
\]
with \(m>0\) and \(n>0\). For every compactly supported invariant probability measure \(\mu\), let \(\bar z=\int z\,d\mu\). Then
\[
\mathbb E_\mu[xy\mid z]=nz\quad \mu\text{-a.s.},
\]
\[
\int x^2\,d\mu=\int xy\,d\mu=n\bar z,
\qquad
\int z^2\,d\mu=m\bar z,
\]
and consequently
\[
\operatorname{{Var}}_\mu(z)=\bar z(m-\bar z),
\qquad
\int \left(z-\frac m2\right)^2d\mu=\frac{{m^2}}4.
\]
In particular \(0\le \bar z\le m\). The endpoint cases are rigid: \(\bar z=0\) holds exactly for the origin measure, while \(\bar z=m\) holds exactly for convex mixtures of the two nonzero equilibria \((\pm\sqrt{{mn}},\pm\sqrt{{mn}},m)\).

There is also a sharp recurrence consequence. Every compact invariant measure not supported on the three equilibria gives positive mass both to the open slab \(0<z<m\) and to the exterior \(z<0\) or \(z>m\). Hence every nonconstant periodic orbit enters \(0<z<m\) and also leaves the closed slab \(0\le z\le m\).

## Assumptions and scope
The result is for the normalized two-parameter T-system with \(m>0\) and \(n>0\). The usual three-parameter form
\[
\dot X=a(Y-X),\qquad \dot Y=(c-a)X-aXZ,\qquad \dot Z=-bZ+XY
\]
with \(a>0\) is transformed to the normalized form by \(x=X/\sqrt a\), \(y=Y/\sqrt a\), \(z=Z\), \(\tau=at\), \(m=c/a-1\), and \(n=b/a\). Compact support is used only to justify the invariant-measure generator identities for the polynomial observables and bounded functions of \(z\).

The classical chaotic parameter example \(a=2.1\), \(b=0.6\), \(c=30\) lies in this regime. No claim is made here that every parameter pair has a non-equilibrium compact invariant set.

## Proof
Define
\[
F(x,y,z)=y^2+z^2-2mz=y^2+(z-m)^2-m^2.
\]
Direct differentiation along the normalized flow gives the exact coboundary
\[
\frac{dF}{dt}=-2nz(z-m).
\]
For an invariant probability measure, the integral of the generator of a smooth observable is zero. Since \(n>0\), integrating the displayed identity yields
\[
\int z(z-m)\,d\mu=0,
\]
so \(\int z^2d\mu=m\bar z\). Therefore
\[
\operatorname{{Var}}_\mu(z)=\int z^2d\mu-\bar z^2
=\bar z(m-\bar z)\ge0,
\]
which forces \(0\le\bar z\le m\). Completing the square gives the measure-independent second-moment circle
\[
\int\left(z-\frac m2\right)^2d\mu
=\frac{{m^2}}4.
\]

Next, applying stationarity to \(x^2\) and \(z\) gives
\[
0=2\int x(y-x)d\mu,
\qquad
0=\int(xy-nz)d\mu,
\]
hence \(\int x^2d\mu=\int xyd\mu=n\bar z\). More strongly, for every continuously differentiable scalar function \(\Phi\), stationarity of \(\Phi(z)\) gives
\[
\int \Phi'(z)(xy-nz)d\mu=0.
\]
On the compact \(z\)-support, derivatives of smooth test functions are dense among continuous test functions. Thus
\[
\mathbb E_\mu[xy-nz\mid z]=0,
\]
which is the stated conditional law.

If \(\bar z=0\) or \(m\), the variance formula forces \(z\) to be constant \(\mu\)-almost surely. The support of an invariant measure is invariant. On \(z=0\), invariance requires \(xy=0\); if \(x=0\), then \(\dot x=y\), and if \(y=0\), then \(\dot y=mx\). Because \(m>0\), the only invariant point in that plane is the origin. On \(z=m\), invariance requires \(xy=mn\), while \(\dot y=0\). Preservation of \(xy=mn\) then gives \(y(y-x)=0\); since \(mn>0\), this forces \(x=y\) and \(x^2=mn\). Hence the invariant support is contained in the two nonzero equilibria, proving endpoint rigidity.

Finally, put \(q(z)=z(z-m)\). The stationary balance gives \(\int q(z)d\mu=0\). The function \(q\) is negative exactly on \(0<z<m\), positive exactly on \(z<0\) or \(z>m\), and zero only at \(z=0,m\). If a compact invariant measure is not supported on the three equilibria, endpoint rigidity shows that it is not concentrated on \(q=0\); zero mean of \(q\) therefore requires positive mass on both sign regions. Applying this to the normalized time measure of a nonconstant periodic orbit proves the slab-crossing statement.

## Verification
The accompanying `verify.py` computes the relevant Lie derivatives symbolically with exact algebra. It verifies
\[
L F=-2nz(z-m),\qquad L(x^2)=2x(y-x),\qquad Lz=xy-nz,
\]
and the algebra used in the endpoint-support tangency argument. Running `python verify.py` produces `VERIFY_OK`; the exact output is included in `verification_output.txt`.

## Relationship to prior work
Tigan's early work introduced the T-system and studied bifurcation and stability, with a public conference source dated 7--9 October 2004. Tigan and Opriş later analyzed heteroclinic Shilnikov horseshoe chaos; an open preprint was posted in 2006. Craioveanu and Tigan studied Hopf bifurcations in 2008 (primary MSC 34D20). Later work treated heteroclinic orbits, competitive-mode classification, ultimate bounds, control, and synchronization.

The closest statement found is the 2021 full-text study by Constantinescu, Tigan, and Zhang. It proves that at \(n=0\), the same polynomial \(F=y^2+z^2-2mz\) is a first integral and its level sets are invariant cylinders; it also classifies special invariant algebraic surfaces and global dynamics. The present claim concerns the complementary dissipative regime \(n>0\): the exact derivative \(LF=-2nz(z-m)\) is converted into a stationary moment circle, a conditional product law, endpoint rigidity, and a slab-crossing recurrence theorem. Those implications were not found in the inspected T-system sources.

A 2015 paper gives global exponential attractive sets for a Lorenz-family class including references to the T-system, but its stated aim is ultimate boundedness through generalized Lyapunov functions rather than exact invariant-measure identities. A 2023 bifurcation paper explicitly records the normalized T-system used here and studies pitchfork/Hopf bifurcations. A 2024 Jacobi-stability paper studies local geometric stability and supplies the early 2004 reference trail. These provide nearby coverage but do not imply the stationary identities above.

## Limitations
Originality here means that the exact statement and its implication structure were not found in the inspected literature and published-result database; it is not a claim that an exhaustive search of all literature is possible. The 2004 proceedings item was identified through later bibliographic references; the accessible full text used for equation-level comparison was the 2006 arXiv paper and the 2021 open-access article. The 2015 ultimate-bound source was inspected through its publisher abstract and references, not its complete proof text.

The conditional identity is an invariant-measure statement and does not by itself prove existence, uniqueness, mixing, or physicality of a non-equilibrium invariant measure. The recurrence conclusion is qualitative: it forces visits to both sign regions of \(z(z-m)\) but does not quantify their frequency or excursion size.

## References
1. G. Tigan, “Bifurcation and the stability in a system derived from the Lorentz system,” Third International Colloquium: Mathematics in Engineering and Numerical Physics, Bucharest, 7--9 October 2004; proceedings published by Geometry Balkan Press, 2005, pp. 265--272.
2. G. Tigan and D. Opriş, “Analysis of a 3D chaotic system,” arXiv:math/0608568, submitted 23 August 2006; later Chaos, Solitons & Fractals 36 (2008), 1315--1319, DOI: 10.1016/j.chaos.2006.07.052.
3. M. Craioveanu and G. Tigan, “Hopf bifurcations analysis of a three-dimensional nonlinear system,” Bulletin of the Academy of Sciences of Moldova, Mathematics 3(58) (2008), 57--66; primary MSC 34D20.
4. F. Zhang, C. Mu, S. Zhou, and P. Zheng, “New results of the ultimate bound on the trajectories of the family of the Lorenz systems,” Discrete and Continuous Dynamical Systems - B 20 (2015), 1261--1276, DOI: 10.3934/dcdsb.2015.20.1261.
5. D. Constantinescu, G. Tigan, and X. Zhang, “Coexistence of chaotic attractor and unstable limit cycles in a 3D dynamical system,” Open Research Europe 1 (2021), article 50, PMCID: PMC10446012.
6. D. Constantinescu and G. Tigan, “On the bifurcations of a 3D symmetric dynamical system,” Symmetry 15 (2023), 923, DOI: 10.3390/sym15040923.
7. F. Munteanu, “Jacobi Stability for T-System,” Symmetry 16 (2024), 84, DOI: 10.3390/sym16010084.
