# Equilibrium-amplitude excursion law for the Chua double-scroll system
## Finding
Consider the normalized Chua system
\[
\dot x=\alpha\bigl(y-h(x)\bigr),\qquad
\dot y=x-y+z,\qquad
\dot z=-\beta y,
\]
where
\[
\alpha>0,\qquad \beta>0,
\]
and the odd three-segment piecewise-linear function is
\[
h(x)=
\begin{cases}
m_1x+(m_0-m_1),&x\ge1,\\
m_0x,&|x|\le1,\\
m_1x-(m_0-m_1),&x\le-1,
\end{cases}
\]
with
\[
m_0<0<m_1.
\]
Define
\[
r=\frac{m_1-m_0}{m_1}>1.
\]

Every compactly supported invariant probability measure \(\mu\) satisfies
\[
\mathbb E_\mu[y\mid z]=0,
\]
\[
\mathbb E_\mu[x+z\mid y]=y,
\]
\[
\mathbb E_\mu[h(x)]=0,
\]
and the exact stationary defect
\[
\mathbb E_\mu[y^2]
=
\mathbb E_\mu[xh(x)]
\ge0.
\]

Equality holds exactly for convex mixtures of the three equilibrium atoms
\[
e_0=(0,0,0),
\qquad
e_\pm=(\pm r,0,\mp r).
\]

Every compact invariant probability measure that is not such an equilibrium mixture gives positive mass to
\[
|x|>r.
\]
Thus \(r\), the voltage amplitude of the two nonzero equilibria, is a universal excursion threshold for non-equilibrium compact recurrence.

Every nonconstant periodic orbit visits both
\[
|x|<r
\]
and
\[
|x|>r,
\]
so it crosses
\[
|x|=r
\]
at least twice in each least period.

For the canonical double-scroll slopes
\[
m_0=-\frac17,\qquad m_1=\frac27,
\]
one has
\[
r=\frac32.
\]
Hence every non-equilibrium compact stationary state in that canonical family gives positive mass to
\[
|x|>\frac32,
\]
and every nonconstant periodic orbit crosses
\[
|x|=\frac32
\]
at least twice per least period.

## Assumptions and scope
The measure statements concern Borel probability measures invariant under the Chua flow and supported on compact subsets of \(\mathbb R^3\). Compact support ensures integrability of the test functions used below.

The function \(h\) is written in the normalization used in the rigorous double-scroll analysis, where \(h=x+f(x)\) relative to the common circuit notation
\[
\dot x=\alpha\bigl(y-x-f(x)\bigr).
\]
The assumptions
\[
m_0<0<m_1
\]
are exactly the inner-negative and outer-positive slope geometry used for the classical three-equilibrium double-scroll family.

The earliest verified public source for the circuit is the Berkeley technical report dated 17 April 1984. The later rigorous double-scroll report explicitly adopts the dimensionless system above and gives the canonical double-scroll parameter neighborhood
\[
\left(
\alpha,\beta,m_0,m_1
\right)
=
\left(
9,\frac{100}{7},-\frac17,\frac27
\right).
\]

The periodic-orbit conclusion concerns a nonconstant classical periodic solution and its least positive period.

## Proof
Let \(L\) be the generator of the flow. For every continuously differentiable test function \(H\) on a neighborhood of the compact support,
\[
\int LH\,d\mu=0.
\]

Take any continuous function \(\phi\) on the compact \(z\)-range and choose an antiderivative \(H\) with
\[
H'(z)=\phi(z).
\]
Then
\[
LH=-\beta\phi(z)y.
\]
Since \(\beta>0\),
\[
\mathbb E_\mu[y\mid z]=0.
\]
In particular,
\[
\mathbb E_\mu[y]=0.
\]

Similarly, for any continuous \(\psi\) on the compact \(y\)-range, choose \(K\) with
\[
K'(y)=\psi(y).
\]
Then
\[
LK=\psi(y)(x-y+z),
\]
hence
\[
\mathbb E_\mu[x+z\mid y]=y.
\]

Stationarity of the coordinate \(x\) gives
\[
0
=
\mathbb E_\mu[\dot x]
=
\alpha\,\mathbb E_\mu[y-h(x)].
\]
Using
\[
\mathbb E_\mu[y]=0,
\]
we obtain
\[
\mathbb E_\mu[h(x)]=0.
\]

Next,
\[
L\left(\frac{x^2}{2}\right)
=
\alpha x\bigl(y-h(x)\bigr),
\]
so stationarity gives
\[
\mathbb E_\mu[xy]
=
\mathbb E_\mu[xh(x)].
\]

Also,
\[
L\left(
\frac{\beta y^2+z^2}{2}
\right)
=
\beta y(x-y+z)-\beta zy
=
\beta(xy-y^2).
\]
Therefore
\[
\mathbb E_\mu[xy]
=
\mathbb E_\mu[y^2].
\]
Combining the last two identities proves
\[
\mathbb E_\mu[y^2]
=
\mathbb E_\mu[xh(x)]
\ge0.
\]

The piecewise geometry is explicit. Since
\[
r=\frac{m_1-m_0}{m_1},
\]
one has
\[
h(x)=m_1(x-r)
\qquad
\text{for }x\ge1,
\]
\[
h(x)=m_0x
\qquad
\text{for }|x|\le1,
\]
and
\[
h(x)=m_1(x+r)
\qquad
\text{for }x\le-1.
\]
Because
\[
m_0<0<m_1,
\]
it follows that
\[
xh(x)\le0
\quad\text{for }|x|\le r,
\]
with equality there only at
\[
x\in\{-r,0,r\},
\]
while
\[
xh(x)>0
\quad\text{for }|x|>r.
\]

Suppose
\[
\mu\{|x|>r\}=0.
\]
Then
\[
\mathbb E_\mu[xh(x)]\le0.
\]
The defect identity gives
\[
0\le\mathbb E_\mu[y^2]
=
\mathbb E_\mu[xh(x)]
\le0.
\]
Hence
\[
y=0
\]
almost surely and
\[
xh(x)=0
\]
almost surely.

The support of an invariant probability measure is invariant. Along a trajectory in that support, \(y\) remains zero, so
\[
0=\dot y=x+z.
\]
Thus
\[
z=-x.
\]
Since
\[
\dot z=-\beta y=0,
\]
the coordinate \(z\), and hence \(x=-z\), is constant. Then
\[
0=\dot x=-\alpha h(x),
\]
so
\[
h(x)=0.
\]
The only zeros of \(h\) are
\[
-r,\quad0,\quad r.
\]
Therefore the support is contained in
\[
\{e_-,e_0,e_+\}.
\]
Conversely, every convex mixture of these three equilibrium atoms is invariant and realizes equality.

Thus every non-equilibrium compact invariant measure must give positive mass to
\[
|x|>r.
\]

Now let a nonconstant periodic orbit have least period \(P\). Its normalized orbit measure is not an equilibrium mixture, so
\[
|x(t)|>r
\]
for some \(t\).

It must also have
\[
|x(t)|<r
\]
for some \(t\). Indeed, suppose instead that
\[
|x(t)|\ge r
\]
for all \(t\). The continuous image of the periodic circle under \(x\) is connected, so it lies entirely in one of
\[
[r,\infty)
\qquad\text{or}\qquad
(-\infty,-r].
\]
On either component \(h(x)\) has one fixed sign. But the orbit measure satisfies
\[
\mathbb E[h(x)]=0.
\]
Hence
\[
h(x(t))=0
\]
for all \(t\), forcing
\[
x(t)\equiv r
\]
or
\[
x(t)\equiv-r,
\]
and then the equations force an equilibrium, a contradiction.

Therefore the continuous periodic function
\[
|x(t)|-r
\]
takes both signs. On a periodic circle it must have at least two sign-changing zeros, proving the crossing statement.

## Verification
The accompanying checker uses exact rational sparse-polynomial arithmetic.

For each affine branch of \(h\), it verifies the generator identities
\[
L\left(\frac{x^2}{2}\right)
=
\alpha x\bigl(y-h(x)\bigr)
\]
and
\[
L\left(
\frac{\beta y^2+z^2}{2}
\right)
=
\beta(xy-y^2).
\]

It also verifies the canonical source parameters
\[
m_0=-\frac17,\qquad
m_1=\frac27,\qquad
r=\frac32,
\]
and the three canonical equilibria
\[
(0,0,0),
\qquad
\left(\frac32,0,-\frac32\right),
\qquad
\left(-\frac32,0,\frac32\right).
\]

The stored checker output is `VERIFY_OK`.

The conditional-expectation statements use arbitrary one-variable test functions through antiderivatives on compact coordinate ranges. The equality classification additionally uses invariance of the compact support. The checker is not a substitute for those analytic arguments.

## Relationship to prior work
Matsumoto's 17 April 1984 technical report introduced the chaotic attractor from the circuit and wrote the physical third-order equations with a three-segment piecewise-linear nonlinear resistor. The report emphasizes the observed chaotic attractor and an exterior hyperbolic periodic orbit.

The 4 December 1985 Chua–Komuro–Matsumoto report gives a rigorous mathematical treatment of the double-scroll family. It explicitly rewrites the dimensionless dynamics as
\[
\dot x=\alpha(y-h(x)),\qquad
\dot y=x-y+z,\qquad
\dot z=-\beta y,
\]
with an odd three-segment \(h\), inner slope negative, outer slope positive, and three equilibria. It develops linear conjugacy, Poincaré maps, homoclinic orbits, bifurcation geometry, and a rigorous proof of chaos. Full-text searches of that report for invariant-measure, stationary, average, mean-square, energy, and probability language did not locate the stationary defect above.

Later work gives analytical predictions of periodic flows in Chua's circuit using regionwise solutions, switching boundaries, mappings, grazing conditions, and local stability. Only abstract and preview material were available for that 2009 article, so possible overlap with the periodic-crossing corollary remains a bibliographic risk. Its accessible description does not state the invariant-measure identity or the equilibrium-amplitude excursion law.

A 2003 mathematical treatment of homoclinic loops in Chua circuits is indexed under MSC \(34C28\), \(34C37\), and \(34C60\). This supports \(34C28\) as the primary classification for the present recurrence theorem.

Targeted searches for invariant probability measures, stationary averages, the exact quantity \(xh(x)\), the equilibrium amplitude \(r\), and periodic crossing of the nonzero-equilibrium voltage found no same-object statement implying the theorem above.

## Limitations
The theorem concerns compactly supported invariant probability measures and periodic orbits. It does not prove existence of a chaotic attractor for every parameter choice satisfying
\[
m_0<0<m_1,
\]
nor does it classify unbounded trajectories.

The positive-mass conclusion is one-sided: it forces excursions beyond the nonzero-equilibrium amplitude but does not specify how much stationary mass lies there.

The full 2009 periodic-flow article was not available in the inspected lawful sources; its abstract indicates a potentially related analytical treatment of periodic trajectories, and this remains the main residual literature risk.

The result is stated in the three-segment dimensionless normalization. Physical circuit variables are related to it by the standard nondimensionalization used in the Chua literature.

## References
1. T. Matsumoto, “A Chaotic Attractor From Chua's Circuit,” UCB/ERL Memorandum M84/36, 17 April 1984.
2. L. O. Chua, M. Komuro, and T. Matsumoto, “Double Scroll Family: Part I — Rigorous Proof of Chaos; Part II — Rigorous Analysis of Bifurcation Phenomena,” UCB/ERL Memorandum M85/102, 4 December 1985; later published in IEEE Transactions on Circuits and Systems.
3. A. C. J. Luo and B. Xue, “An Analytical Prediction of Periodic Flows in the Chua Circuit System,” International Journal of Bifurcation and Chaos 19(7), 2165–2180 (2009), DOI 10.1142/S0218127409023998.
4. A. F. Gribov and A. P. Krishchenko, “Analytical conditions for the existence of a homoclinic loop in Chua circuits,” Computational Mathematics and Modeling (2003), DOI 10.1023/A:1013885803890.
