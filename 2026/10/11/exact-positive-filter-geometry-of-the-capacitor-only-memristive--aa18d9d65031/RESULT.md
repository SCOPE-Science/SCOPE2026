# Exact positive-filter geometry of the capacitor-only memristive Colpitts state
## Finding
For the capacitor-only diode-bridge memristor used in the Colpitts oscillator of Zhou, You, Liang and Li, introduce
\[
R=e^{u/(2n)},\qquad \kappa=\frac{\alpha d}{2n}.
\]
When \(n>0\) and \(\alpha d>0\), the fourth equation of the published dimensionless system,
\[
\dot u=\alpha d\left(e^{-u/(2n)}\cosh\!\left(\frac{x}{2n}\right)-1\right),
\]
becomes exactly
\[
\dot R=\kappa\left(\cosh\!\left(\frac{x}{2n}\right)-R\right).
\]
Thus the nonlinear memory coordinate is a stable first-order filter after exponentiation.

For every bounded complete trajectory,
\[
R(t)=\kappa\int_{-\infty}^t e^{-\kappa(t-s)}\cosh\!\left(\frac{x(s)}{2n}\right)\,ds.
\]
Because the kernel is positive and \(\cosh r\ge1\), every bounded complete trajectory satisfies \(R(t)\ge1\), equivalently \(u(t)\ge0\). Therefore no nonempty compact invariant set of the published system can intersect \(\{u<0\}\). If \(K\) is compact invariant and
\[
X_K=\max_{p\in K}|x(p)|,
\]
then every point of \(K\) also satisfies the pointwise bound
\[
0\le u\le 2n\log\cosh\!\left(\frac{X_K}{2n}\right).
\]

For every compactly supported invariant Borel probability measure \(\mu\), stationarity of \(R\) gives
\[
\int e^{u/(2n)}\,d\mu
=
\int\cosh\!\left(\frac{x}{2n}\right)\,d\mu.
\]
Using \(\cosh r\ge1+r^2/2\), this implies
\[
\int e^{u/(2n)}\,d\mu-1
\ge
\frac{1}{8n^2}\int x^2\,d\mu.
\]
The physical circuit has the identical structure. With \(\mathcal R=e^{\rho v_0}\) and \(\kappa_{\rm phys}=2\rho I_{s0}/C_0\), its memory equation becomes
\[
\dot{\mathcal R}=\kappa_{\rm phys}\left(\cosh(\rho v_{ce})-\mathcal R\right).
\]
Accordingly, bounded complete physical trajectories satisfy \(v_0\ge0\), and compact stationary states obey \(\langle e^{\rho v_0}\rangle=\langle\cosh(\rho v_{ce})\rangle\).

## Assumptions and scope
The result applies to System (12) in the cited 2022 article, before the later offset-boosting modifications. It requires only \(n>0\) and \(\alpha d>0\), which hold for the physical parameter definitions in that model. The compact-set conclusions concern complete trajectories contained in a compact invariant set; they do not claim that every forward trajectory started with \(u<0\) is bounded or recurrent. The invariant-measure statement assumes a compactly supported invariant Borel probability measure of the classical autonomous flow.

## Proof
Set \(R=e^{u/(2n)}\). Then \(e^{-u/(2n)}=R^{-1}\), so the chain rule gives
\[
\dot R=\frac{R}{2n}\dot u
=\frac{\alpha d}{2n}R\left(R^{-1}\cosh\!\left(\frac{x}{2n}\right)-1\right)
=\kappa\left(\cosh\!\left(\frac{x}{2n}\right)-R\right).
\]
Variation of constants between \(s<t\) yields
\[
R(t)=e^{-\kappa(t-s)}R(s)
+\kappa\int_s^t e^{-\kappa(t-r)}\cosh\!\left(\frac{x(r)}{2n}\right)\,dr.
\]
On a bounded complete trajectory, \(R(s)\) remains bounded as \(s\to-\infty\). Since \(\kappa>0\), the homogeneous term tends to zero, proving the infinite-past formula.

The kernel has mass one and the input is at least one, so \(R(t)\ge1\). If the trajectory lies in compact \(K\), then \(|x|\le X_K\) and hence the filter input is at most \(\cosh(X_K/(2n))\); the same formula gives \(R(t)\le\cosh(X_K/(2n))\). Taking logarithms gives the stated pointwise bounds for \(u\).

If \(\mu\) is compactly supported and invariant, the generator identity \(\int L R\,d\mu=0\) is legitimate because \(R\) and \(LR\) are continuous and bounded on the support. Since
\[
LR=\kappa\left(\cosh\!\left(\frac{x}{2n}\right)-R\right),
\]
the stationary identity follows. The quadratic lower bound is the pointwise inequality \(\cosh r\ge1+r^2/2\) integrated against \(\mu\).

For physical variables, applying the same chain rule to the published equation
\[
\dot v_0=\frac{2I_{s0}}{C_0}\left(e^{-\rho v_0}\cosh(\rho v_{ce})-1\right)
\]
with \(\mathcal R=e^{\rho v_0}\) gives the displayed physical filter equation.

## Verification
The bundled `verify.py` replays the transformed scalar identity using exact rational arithmetic after replacing \(e^{-u/(2n)}\) by \(R^{-1}\), and checks the coefficient in the quadratic consequence of \(\cosh r\ge1+r^2/2\). The compact-recurrence conclusions are analytic consequences of variation of constants; no finite simulation is used as an infinite-time proof.

## Relationship to prior work
The 2022 source introduces a diode-bridge-plus-capacitor emulator, derives the physical and dimensionless equations, studies equilibria, bifurcation, multistability, transient chaos and offset boosting, and records at equilibrium the relation \(e^{-\rho v_0}\cosh(\rho v_{ce})=1\). The filter identity above extends that static relation to every bounded complete recurrent trajectory and every compact stationary state.

The earlier generalized memristive Colpitts circuit of Lu et al. uses a diode bridge followed by a parallel \(RC\) filter rather than the capacitor-only state in the 2022 model. The related 2014 canonical-Chua diode-bridge model explicitly contains the leakage term \(-v_C/(RC)\) in the internal-state equation, so exponentiation does not produce the linear filter stated here. Deng and Wang's 2017 memristive Colpitts implementations use a different emulator architecture and do not state this capacitor-only recurrence law in the inspected material. published-finding corpus searches using the source title, state equation, exponential coordinate, recurrence barrier, and invariant-measure aliases returned no same-object statement.

## Limitations
The result does not classify the attractors, prove existence of chaos, or establish boundedness for arbitrary initial data. It is specific to the capacitor-only memory equation with positive \(n\) and \(\alpha d\). Modified offset-boosted equations must be transformed separately. The originality comparison cannot exclude an unindexed observation of the same exponential coordinate in broader diode-bridge literature; the closest inspected same-object and same-architecture sources do not state the bounded-complete-trajectory or invariant-measure conclusions.

## References
1. L. Zhou, Z. You, X. Liang, X. Li, “A Memristor-Based Colpitts Oscillator Circuit,” *Mathematics* 10 (2022), 4820. DOI: 10.3390/math10244820.
2. L. Lu, C. Li, Z. Zhao, B. Bao, Q. Xu, “Colpitts Chaotic Oscillator Coupling with a Generalized Memristor,” *Mathematical Problems in Engineering* (2015), 249102. DOI: 10.1155/2015/249102.
3. M. Chen, J. Yu, Q. Yu, C. Li, B. Bao, “A Memristive Diode Bridge-Based Canonical Chua’s Circuit,” *Entropy* 16 (2014), 6464–6476. DOI: 10.3390/e16126464.
4. H. Deng, D. Wang, “Circuit simulation and physical implementation for a memristor-based colpitts oscillator,” *AIP Advances* 7 (2017), 035118. DOI: 10.1063/1.4979175.
