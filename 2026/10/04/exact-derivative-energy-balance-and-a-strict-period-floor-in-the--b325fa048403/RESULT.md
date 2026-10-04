# Exact derivative-energy balance and a strict period floor in the Michelson flow
## Finding
For the Michelson flow \(\dot x=y,\ \dot y=z,\ \dot z=c^2-y-\tfrac12x^2\) with \(c>0\), every compactly supported invariant probability measure \(\mu\) satisfies \(\int x^2\,d\mu=2c^2\) and \(\int y^2\,d\mu=\int z^2\,d\mu\). If \(\mu\) is not supported on the two equilibria \((\pm\sqrt2\,c,0,0)\), then the common derivative energy is positive. Every nonconstant periodic orbit has least period \(P>2\pi\), and along every such orbit \(x\) attains values with both \(|x|<\sqrt2\,c\) and \(|x|>\sqrt2\,c\).

## Assumptions and scope
The phase space is \(\mathbb R^3\), \(c>0\), and
\[
\dot x=y,\qquad \dot y=z,\qquad \dot z=c^2-y-\frac12x^2.
\]
The measure statement concerns compactly supported invariant Borel probability measures. The periodic-orbit statement concerns a nonconstant classical periodic solution and its least positive period \(P\).

The foundational 1986 article gives this third-order Michelson equation and studies bounded, periodic, quasiperiodic, and numerically chaotic solutions. Available bibliographic metadata for that article resolves its publication only to February 1986. To avoid fabricating a day, `first_public_date` records the earliest inspected same-object source with a verified exact public date, 2006-12-05; the earlier 1986 article remains explicitly cited and inspected.

## Proof
Let \(L\) be the Lie derivative. Invariance gives \(\int L\phi\,d\mu=0\) for every polynomial \(\phi\). Since
\[
Lx=y,\qquad Ly=z,\qquad Lz=c^2-y-\frac12x^2,
\]
we get
\[
\int y\,d\mu=0,\qquad \int z\,d\mu=0,\qquad \int x^2\,d\mu=2c^2.
\]
Also
\[
L\!\left(\frac{x^3}{3}\right)=x^2y,
\]
so \(\int x^2y\,d\mu=0\). Finally,
\[
L(yz)=z^2+c^2y-y^2-\frac12x^2y.
\]
Integration therefore yields
\[
\int z^2\,d\mu=\int y^2\,d\mu.
\]
If this common value is zero, then \(y=z=0\) almost surely. Invariance of the support then forces \(c^2-x^2/2=0\), hence the support lies in \((\pm\sqrt2\,c,0,0)\). Thus every other compact invariant measure has positive common derivative energy.

For a nonconstant periodic solution of least period \(P\), \(y=\dot x\), \(z=\dot y\), and \(y\) has zero time mean. Its orbit measure gives
\[
\int_0^P z(t)^2\,dt=\int_0^P y(t)^2\,dt>0.
\]
Wirtinger's inequality gives
\[
\int_0^P \dot y(t)^2\,dt\ge\left(\frac{2\pi}{P}\right)^2\int_0^P y(t)^2\,dt,
\]
so \(P\ge2\pi\). Equality would make \(y\) a first harmonic. With \(P=2\pi\), after a time shift, write \(y=A\cos t\), hence \(x=m+A\sin t\) and \(z=-A\sin t\). Substitution into the third equation reduces to
\[
0=c^2-\frac12(m+A\sin t)^2
\]
for every \(t\). The \(\sin^2t\) coefficient is \(-A^2/2\), forcing \(A=0\), contradicting nonconstancy. Hence \(P>2\pi\).

Finally,
\[
\frac1P\int_0^P x(t)^2\,dt=2c^2.
\]
If \(x(t)^2\) stayed entirely on either side of \(2c^2\), equality of the average and continuity would force \(x(t)^2\) to be constant, hence an equilibrium. A nonconstant cycle therefore visits both \(|x|<\sqrt2\,c\) and \(|x|>\sqrt2\,c\).

## Verification
The included `verify.py` uses only the Python standard library and exact rational sparse-polynomial arithmetic. It reconstructs the Lie derivatives used above and checks the nonzero quadratic coefficient in the equality case. Its recorded output is `VERIFY_OK`. The Wirtinger step is analytic and is not replaced by finite computation.

## Relationship to prior work
Michelson's 1986 paper derives the scalar equation \(x'''+x'+x^2/2=c^2\), proves a small-parameter periodic branch, and follows periodic frequencies, invariant tori, and more complicated bounded behavior. The inspected text does not state the invariant-measure identities or a universal strict lower bound \(P>2\pi\).

Wilczak's full-text 2006 paper fixes \(c=1\), recalls two rigorously established odd periodic solutions, and proves infinitely many homoclinic and heteroclinic connections between them. Llibre and Zhang prove a local Hopf-zero periodic orbit for sufficiently small \(c>0\). Llibre and Makhlouf study local zero-Hopf bifurcation in the generalized family \(\dot z=a+by+cz-x^2/2\). These results concern existence and connecting/bifurcation geometry, not the global stationary balances or period/amplitude barriers above.

Targeted published-finding corpus and web searches for Michelson aliases, the exact moment identities, a Wirtinger period estimate, and a \(2\pi\) lower bound found only analogous results for other vector fields. Search failure is not a novelty proof; an unindexed or differently phrased older result remains a residual risk.

## Limitations
The result does not prove existence or uniqueness of nontrivial invariant measures or periodic orbits, locate branches, estimate the positive gap \(P-2\pi\), or describe stability, entropy, symbolic dynamics, or physical measures. The exact derivative-energy balance changes in generalized Michelson systems with additional damping. The foundational 1986 publication date is month-resolved in the inspected metadata, so no artificial day is assigned to it.

## References
1. D. Michelson, “Steady solutions of the Kuramoto–Sivashinsky equation,” Physica D 19 (1986), 89–111, DOI 10.1016/0167-2789(86)90055-2.
2. D. Wilczak, “Symmetric homoclinic solutions to the periodic orbits in the Michelson system,” Topological Methods in Nonlinear Analysis 28 (2006), 155–170.
3. J. Llibre and X. Zhang, “On the Hopf-zero bifurcation of the Michelson system,” Nonlinear Analysis: Real World Applications 12 (2011), 1650–1653, DOI 10.1016/j.nonrwa.2010.10.019.
4. J. Llibre and A. Makhlouf, “Zero-Hopf bifurcation in the generalized Michelson system,” Chaos, Solitons & Fractals 89 (2016), 228–231, DOI 10.1016/j.chaos.2015.11.013.
