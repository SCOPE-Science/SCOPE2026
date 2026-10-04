# Compact-recurrence threshold, amplitude barrier, and strict period floor in the generalized Sprott I flow
## Finding
Consider the generalized Sprott I system
\[
\dot x=-a y,\qquad
\dot y=x+z,\qquad
\dot z=x+y^2-bz,
\]
with \(b>0\) and \(a\in\mathbb R\).

Compact recurrence has a sharp boundary at \(a=0\).

If \(a<0\), the only compactly supported invariant probability measure is the Dirac mass at the origin.

If \(a=0\), the compactly supported invariant probability measures are exactly the compactly supported probabilities on the equilibrium parabola
\[
\mathcal E_b=
\left\{
\left(-\frac{s^2}{b+1},\,s,\,\frac{s^2}{b+1}\right):s\in\mathbb R
\right\}.
\]

If \(a>0\), every compactly supported invariant probability measure \(\mu\) satisfies
\[
b\,\mathbb E_\mu[(x+z)^2]
=
a(b+1)\,\mathbb E_\mu[y^2]
\]
and
\[
\mathbb E_\mu\!\left[y^2\left(y+\frac ab\right)\right]=0.
\]
Writing
\[
q=\mathbb E_\mu[y^2],
\]
one also has
\[
\mathbb E_\mu[y]=0,\qquad
\mathbb E_\mu[x]=-\frac{q}{b+1},\qquad
\mathbb E_\mu[z]=\frac{q}{b+1}.
\]

Every non-origin compact invariant measure for \(a>0\) assigns positive mass to both
\[
y<-\frac ab
\qquad\text{and}\qquad
y>0.
\]
Thus recurrent dynamics cannot remain inside the closed amplitude slab
\[
-\frac ab\le y\le0.
\]

Every nonconstant periodic orbit with least period \(P\) obeys the strict universal bound
\[
P>
2\pi\sqrt{\frac{b}{a(b+1)}}.
\]
It crosses each level
\[
y=-\frac ab
\qquad\text{and}\qquad
y=0
\]
at least twice per least period.

For the canonical Sprott I parameters \(a=0.2\) and \(b=1\),
\[
P>9.934588265796101\ldots,
\qquad
y<-0.2
\]
occurs on every nonconstant periodic orbit.

## Assumptions and scope
The measure statements concern Borel probability measures invariant under the flow and supported on compact subsets of \(\mathbb R^3\). Compact support guarantees integrability of all polynomial test functions used below. The periodic-orbit statement concerns a nonconstant classical periodic solution and its least positive period.

The two-parameter normalization is the Case I normalization in J. C. Sprott's primary-author parameter survey. Its canonical chaotic choice is \(a=0.2\), \(b=1\). The earliest verified public source for Case I used here is Sprott's 1994 paper.

## Proof
Let
\[
v=x+z=\dot y.
\]
For every polynomial \(h\), invariance gives
\[
\int Lh\,d\mu=0,
\]
where \(L\) is the generator of the flow.

The first exact polynomial certificate is
\[
H_1=(b+1)xy+\frac13y^3-\frac a2y^2-\frac12(x+z)^2.
\]
Direct differentiation gives
\[
L H_1
=
b(x+z)^2-a(b+1)y^2.
\]
Hence every compact invariant probability measure satisfies
\[
b\,\mathbb E[v^2]
=
a(b+1)\,\mathbb E[y^2].
\tag{1}
\]

If \(a<0\), the two sides of (1) have opposite signs unless both vanish. Thus \(y=0\) and \(v=0\) almost surely. Since \(v=0\) means \(z=-x\), stationarity of \(z^2\) gives
\[
0
=
\mathbb E[L(z^2)]
=
-2(b+1)\mathbb E[x^2],
\]
so \(x=z=0\) almost surely. Only the origin measure remains.

If \(a=0\), (1) gives \(v=0\) almost surely. The support of an invariant measure is invariant under the continuous flow. On the hyperplane \(v=0\), tangency requires
\[
0=L v=(b+1)x+y^2.
\]
Together with \(z=-x\), this is exactly the equilibrium parabola \(\mathcal E_b\). Conversely every compactly supported probability on \(\mathcal E_b\) is invariant because every point of \(\mathcal E_b\) is an equilibrium.

Now assume \(a>0\). From the coordinate generators,
\[
0=\mathbb E[Lx]=-a\,\mathbb E[y],
\]
\[
0=\mathbb E[Ly]=\mathbb E[x]+\mathbb E[z],
\]
and
\[
0=\mathbb E[Lz]
=\mathbb E[x]+\mathbb E[y^2]-b\,\mathbb E[z].
\]
Therefore
\[
\mathbb E[y]=0,\qquad
\mathbb E[z]=\frac{q}{b+1},\qquad
\mathbb E[x]=-\frac{q}{b+1}.
\tag{2}
\]
If \(q=0\), then \(y=0\) almost surely and (1) gives \(v=0\) almost surely; the same rigidity argument as above gives the origin measure. Hence every non-origin compact invariant measure has \(q>0\).

A second exact certificate can be written without denominators as
\[
\begin{aligned}
K={}&6ab\,yz-6a\,xy-2a\,y^3
+3a(a+b^2)y^2\\
&+3a(x+z)^2+3b(b+1)x^2.
\end{aligned}
\]
Exact differentiation gives
\[
L K
=
6a\,y^2(a+by).
\]
For \(a>0\), invariance therefore yields
\[
\mathbb E\!\left[y^2\left(y+\frac ab\right)\right]=0.
\tag{3}
\]

Suppose a non-origin invariant measure had no mass in \(y<-a/b\). Then
\[
y^2\left(y+\frac ab\right)\ge0
\]
almost surely. Equality in (3) would force
\[
y\in\left\{0,-\frac ab\right\}
\]
almost surely. But \(\mathbb E[y]=0\) and \(-a/b<0\), so the atom at \(-a/b\) must have zero mass, giving \(y=0\) almost surely and hence the origin measure, a contradiction. Thus
\[
\mu\!\left(y<-\frac ab\right)>0.
\]
Because \(\mathbb E[y]=0\) and \(q>0\), one also has
\[
\mu(y>0)>0.
\]

For a nonconstant periodic orbit, normalized orbit measure is compact and invariant. Since \(\mathbb E[y]=0\) and \(v=\dot y\), (1) gives
\[
\int_0^P \dot y(t)^2\,dt
=
\frac{a(b+1)}{b}
\int_0^P y(t)^2\,dt.
\tag{4}
\]
Wirtinger's inequality gives
\[
\int_0^P \dot y^2\,dt
\ge
\left(\frac{2\pi}{P}\right)^2
\int_0^P y^2\,dt.
\]
The orbit is nonconstant, so the integral of \(y^2\) is positive. Combining with (4) yields
\[
P\ge
2\pi\sqrt{\frac{b}{a(b+1)}}.
\tag{5}
\]

It remains to exclude equality. Eliminating \(x\) and \(z\) gives the exact scalar equation
\[
y'''+b y''+a y'+a(b+1)y-2y y'=0.
\tag{6}
\]
Equality in Wirtinger's inequality would make \(y\) a nonzero first harmonic with
\[
y''=-\omega^2y,\qquad
y'''=-\omega^2y',
\qquad
\omega^2=\frac{a(b+1)}b.
\]
Substitution into (6) reduces it to
\[
\left(\frac ab+2y\right)y'=0.
\]
A nonconstant first harmonic has \(y'\ne0\) on open intervals, which would force \(y=-a/(2b)\) there, a contradiction. Hence equality in (5) is impossible.

Finally, the orbit measure has positive time in both \(y<-a/b\) and \(y>0\). Continuity on the periodic circle therefore forces at least two crossings of each intermediate boundary \(y=-a/b\) and \(y=0\) in a least period.

## Verification
The accompanying dependency-free checker uses exact sparse-polynomial arithmetic over rational coefficients. It verifies
\[
L H_1=b(x+z)^2-a(b+1)y^2,
\]
the denominator-free cubic certificate
\[
L K=6a\,y^2(a+by),
\]
and the eliminated jerk equation
\[
y'''+b y''+a y'+a(b+1)y-2y y'=0.
\]
The stored output is `VERIFY_OK`.

The measure-theoretic deductions are exact and use only the standard identity \(\int Lh\,d\mu=0\), invariance of the support, and nonnegativity. The period proof uses the classical equality case of Wirtinger's inequality; no finite experiment is used as a proof of an infinite statement.

## Relationship to prior work
Sprott's primary-author parameter survey gives exactly
\[
\dot x=-a y,\qquad
\dot y=x+z,\qquad
\dot z=x+y^2-bz,
\]
with canonical chaotic parameters \(a=0.2\), \(b=1\), and numerically maps stable, periodic, chaotic, and unbounded parameter regions.

Vaidyanathan's full author-upload paper studies adaptive synchronization of Sprott H and Sprott I systems. Its Sprott I section uses the canonical coefficients \(0.2\) and \(1\), introduces uncertain parameters in a controller-oriented embedding, and proves convergence of synchronization and parameter-estimation errors. It does not state an invariant-measure energy identity, a compact-recurrence threshold at \(a=0\), the amplitude barrier \(y<-a/b\), or a universal least-period lower bound in the inspected text.

Dimitrova and Yordanov study approximate second-order, two-point statistics for low-dimensional chaotic flows. The accessible publisher preview emphasizes power spectra, autocovariance models, and explicitly names Sprott N and B in the displayed application material. This statistical program does not imply the exact compact-invariant-measure theorem proved here from the inspected material.

Panchev's later analytical study systematically considers all nineteen Sprott flows and discusses asymptotic reformulations and possible statistical treatment. Only its abstract and indexed metadata were accessible here, so no whole-document noncoverage claim is made for that paper. It remains an explicit residual bibliographic risk.

Targeted semantic searches using Sprott I, compact invariant measures, stationary moments, the exact \((x+z)^2\)-to-\(y^2\) balance, the cubic \(y\)-moment law, recurrence thresholds, amplitude barriers, and period bounds returned no same-object statement implying the theorem above. The closest indexed findings are analogous balance and period laws for different vector fields.

## Limitations
The theorem concerns compactly supported invariant probability measures and periodic orbits. It does not classify unbounded trajectories, prove existence of chaos for any parameter, or determine whether the strict period floor is approached by a sequence of cycles.

For \(a>0\), the amplitude result is one-sided beyond the lower level \(y=-a/b\) and uses the zero mean to force positive excursions; it is not a complete description of the \(y\)-marginal distribution.

The full text of Panchev's 2004 analytical paper was not available for line-by-line comparison. The 1994 source was inspected through its publisher record and primary-author parameter survey rather than through a complete publisher-PDF comparison. A differently phrased or unindexed older result can therefore remain undetected.

## References
1. J. C. Sprott, “Some simple chaotic flows,” Physical Review E 50, R647–R650 (1994), DOI 10.1103/PhysRevE.50.R647. Published 1994-08-01.
2. J. C. Sprott, “Dynamic Regions in Simple Chaotic Flows,” technical note, 2013, https://sprott.physics.wisc.edu/technote/regions.htm.
3. V. Sundarapandian, “Adaptive Synchronization of Uncertain Sprott H and I Chaotic Systems,” International Journal of Computer Information Systems 2(5) (2011).
4. E. S. Dimitrova and O. I. Yordanov, “Statistics of Some Low-Dimensional Chaotic Flows,” International Journal of Bifurcation and Chaos 11, 2675–2682 (2001), DOI 10.1142/S0218127401003735.
5. S. Panchev, “Analytical properties of the Sprott's chaotic flows,” Chaos, Solitons & Fractals 21, 721–728 (2004), DOI 10.1016/j.chaos.2003.12.054.
