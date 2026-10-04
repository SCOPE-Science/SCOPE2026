# Universal stationary correlation and deep height excursion in Sprott N
## Finding
Consider the canonical Sprott N system
\[
\dot x=-2y,\qquad
\dot y=x+z^2,\qquad
\dot z=1+y-2z.
\]

Every compactly supported invariant probability measure \(\mu\) satisfies the exact conditional laws
\[
\mathbb E_\mu[y\mid x]=0,
\]
\[
\mathbb E_\mu[x+z^2\mid y]=0,
\]
and
\[
\mathbb E_\mu[y\mid z]=2z-1.
\]

Let
\[
V=\operatorname{Var}_\mu(z).
\]
Then
\[
\mathbb E_\mu[z]=\frac12,
\qquad
\mathbb E_\mu[x]=-\frac14-V,
\]
\[
\mathbb E_\mu[y^2]=6V,
\qquad
\operatorname{Cov}_\mu(y,z)=2V,
\]
and
\[
\mathbb E_\mu\!\left[\left(z-\frac12\right)^3\right]
=
-V.
\]

The zero-defect case is rigid:
\[
V=0
\]
if and only if
\[
\mu=\delta_{(-1/4,\,0,\,1/2)}.
\]

Hence every non-equilibrium compact invariant probability measure has the same nonzero Pearson correlation
\[
\operatorname{Corr}_\mu(y,z)
=
\sqrt{\frac23}.
\]

It also has a forced deep excursion:
\[
\mu\{z<-\tfrac12\}>0
\]
and, simultaneously,
\[
\mu\{z>\tfrac12\}>0.
\]
Thus no genuinely recurrent compact stationary state can remain in the half-space
\[
z\ge-\frac12,
\]
even though the unique equilibrium lies at height
\[
z=\frac12.
\]

## Assumptions and scope
The measure \(\mu\) is a Borel probability measure invariant under the polynomial flow and supported on a compact subset of \(\mathbb R^3\). Compact support guarantees integrability of all polynomial and one-variable antiderivative test functions used below.

The equations are exactly Case N in the original Sprott list. The unique equilibrium is
\[
e=
\left(
-\frac14,0,\frac12
\right).
\]

The earliest verified public source date is 1 August 1994.

The correlation statement is made only for non-equilibrium invariant measures. In that case
\[
V>0
\]
and
\[
\operatorname{Var}(y)=6V>0,
\]
so the Pearson correlation is well-defined.

## Proof
Let \(L\) denote the generator of the flow.

For any continuous function \(\phi\) on the compact \(x\)-range, choose an antiderivative \(H\) with
\[
H'(x)=\phi(x).
\]
Then
\[
LH=-2\phi(x)y.
\]
Invariance gives
\[
\mathbb E_\mu[\phi(x)y]=0
\]
for every such \(\phi\), hence
\[
\mathbb E_\mu[y\mid x]=0.
\]

For any continuous function \(\psi\) on the compact \(y\)-range, choose an antiderivative \(K\) with
\[
K'(y)=\psi(y).
\]
Then
\[
LK=\psi(y)(x+z^2),
\]
so
\[
\mathbb E_\mu[x+z^2\mid y]=0.
\]

Likewise, for any continuous function \(\chi\) on the compact \(z\)-range and an antiderivative \(G\),
\[
LG=\chi(z)(1+y-2z).
\]
Therefore
\[
\mathbb E_\mu[y\mid z]=2z-1.
\]

Taking expectations in the first and third coordinate equations gives
\[
\mathbb E[y]=0
\]
and then
\[
\mathbb E[z]=\frac12.
\]
Taking expectations in the second equation gives
\[
\mathbb E[x]
=
-\mathbb E[z^2]
=
-\frac14-V.
\]

Stationarity of
\[
\frac{y^2}{2}
\]
gives
\[
0
=
\mathbb E[y(x+z^2)].
\]
The first conditional law gives
\[
\mathbb E[xy]=0.
\]
The third conditional law gives
\[
\mathbb E[yz^2]
=
\mathbb E[(2z-1)z^2].
\]
Hence
\[
2\mathbb E[z^3]
=
\mathbb E[z^2].
\]
Since
\[
\mathbb E[z]=\frac12,
\]
this is equivalent to
\[
\mathbb E\!\left[\left(z-\frac12\right)^3\right]
=
-\operatorname{Var}(z)
=
-V.
\]

The third conditional law also gives
\[
\operatorname{Cov}(y,z)
=
\mathbb E[yz]
=
\mathbb E[(2z-1)z]
=
2V.
\]

To obtain the \(y\)-variance, first use stationarity of \(xz\):
\[
0
=
\mathbb E[-2yz+x+xy-2xz].
\]
Because
\[
\mathbb E[xy]=0
\]
and
\[
\mathbb E[yz]=2V,
\]
we obtain
\[
\mathbb E[xz]
=
-\frac18-\frac52V.
\]

Now stationarity of \(yz\) gives
\[
0
=
\mathbb E[xz+z^3+y+y^2-2yz].
\]
Using
\[
\mathbb E[z^3]
=
\frac12\mathbb E[z^2]
=
\frac18+\frac12V,
\]
\[
\mathbb E[y]=0,
\qquad
\mathbb E[yz]=2V,
\]
and the formula for \(\mathbb E[xz]\), we obtain
\[
\mathbb E[y^2]=6V.
\]

If
\[
V>0,
\]
then
\[
\operatorname{Corr}(y,z)
=
\frac{2V}{\sqrt{6V}\sqrt V}
=
\sqrt{\frac23}.
\]

If
\[
V=0,
\]
then \(z=1/2\) almost surely. The invariant support is therefore contained in the plane \(z=1/2\). Tangency of this plane gives
\[
0=\dot z=y,
\]
hence \(y=0\). Then
\[
0=\dot y=x+\frac14,
\]
so
\[
x=-\frac14.
\]
Thus the support is the single equilibrium \(e\). Conversely its atom plainly has \(V=0\).

Finally, the central third-moment identity can be rewritten as
\[
\mathbb E\!\left[
\left(z-\frac12\right)^2
\left(z+\frac12\right)
\right]
=
0.
\]
Suppose that
\[
\mu\{z<-\tfrac12\}=0.
\]
The integrand is then nonnegative, so it must vanish on the support. Hence the support lies in
\[
z\in\left\{-\frac12,\frac12\right\}.
\]
Because each support trajectory is continuous, its \(z\)-coordinate must be constant.

The level
\[
z=-\frac12
\]
cannot support a complete trajectory: tangency requires \(y=-2\), while keeping \(y\) constant requires \(x=-1/4\), but then
\[
\dot x=4.
\]
The only possible invariant level is therefore \(z=1/2\), which gives the equilibrium as above. Thus every non-equilibrium invariant measure has
\[
\mu\{z<-\tfrac12\}>0.
\]

Since every invariant measure has mean
\[
\mathbb E[z]=\frac12,
\]
the same non-equilibrium measure must also satisfy
\[
\mu\{z>\tfrac12\}>0.
\]

## Verification
The accompanying checker uses exact rational arithmetic.

It verifies the generator identities
\[
L\left(\frac{y^2}{2}\right)
=
xy+yz^2,
\]
\[
L(xz)
=
-2yz+x+xy-2xz,
\]
and
\[
L(yz)
=
xz+z^3+y+y^2-2yz.
\]

It then replays the exact stationary algebra from
\[
\mathbb E[z]=\frac12,
\qquad
\mathbb E[z^2]=\frac14+V,
\qquad
2\mathbb E[z^3]=\mathbb E[z^2],
\]
to obtain
\[
\mathbb E\!\left[\left(z-\frac12\right)^3\right]=-V,
\]
\[
\mathbb E[yz]=2V,
\]
\[
\mathbb E[xz]=-\frac18-\frac52V,
\]
and
\[
\mathbb E[y^2]=6V.
\]

It also verifies the unique equilibrium exactly.

The stored checker output is `VERIFY_OK`.

The conditional laws themselves use arbitrary one-variable test functions. The excursion and equality arguments use invariance of the compact support. These are analytic steps, not finite numerical experiments.

## Relationship to prior work
Sprott's original 1994 paper introduces Case N exactly as
\[
\dot x=-2y,\qquad
\dot y=x+z^2,\qquad
\dot z=1+y-2z.
\]
It lists the unique equilibrium, Lyapunov spectrum, Lyapunov dimension, and a stereoscopic plot of the chaotic attractor. The article is numerical and classificatory; it does not formulate invariant probability measures or exact stationary moment relations.

Panchev's 2004 paper systematically examines all nineteen Sprott flows by asymptotic analytical reduction and explicitly discusses the possibility of statistical treatment. Its accessible abstract therefore makes it a strong comparison source. A secure complete-text comparison was not available, so no whole-document noncoverage claim is made.

Starkov and Coria's 2005 paper studies localization of periodic orbits for all nineteen polynomial Sprott systems and obtains semispace localization in many cases. Its abstract and accessible first page were inspected. Because that work is periodic-orbit specific and the complete Case N section was not available, the present claim is deliberately stated for arbitrary compact invariant probability measures and does not include a periodic-orbit localization corollary.

Targeted searches for the exact conditional laws, the universal correlation
\[
\sqrt{\frac23},
\]
the central third-moment law, and the forced excursion below
\[
z=-\frac12
\]
did not locate a same-object statement implying the theorem above.

## Limitations
The theorem concerns compactly supported invariant probability measures. It does not prove existence or uniqueness of the chaotic attractor, determine a complete invariant density, or classify unbounded trajectories.

The exact correlation is a stationary constraint and does not imply joint Gaussianity or statistical independence.

The complete Panchev 2004 paper and the complete Case N section of the Starkov–Coria 2005 localization paper were not securely available for full-text comparison. Both remain explicit literature risks.

The novelty claim is restricted to the invariant-measure conditional laws, exact correlation and moment identities, and the all-measures deep-excursion obstruction. It does not claim novelty for the Sprott N equations, equilibrium, Lyapunov data, or prior periodic-orbit localization results.

## References
1. J. C. Sprott, “Some simple chaotic flows,” Physical Review E 50, R647–R650 (1994), DOI 10.1103/PhysRevE.50.R647.
2. S. Panchev, “Analytical properties of the Sprott's chaotic flows,” Chaos, Solitons & Fractals 21, 721–728 (2004), DOI 10.1016/j.chaos.2003.12.054.
3. K. E. Starkov and L. Coria, “Localization of Periodic Orbits of Polynomial Sprott Systems with One or Two Quadratic Monomials,” International Journal of Nonlinear Sciences and Numerical Simulation 6, 271–277 (2005), DOI 10.1515/IJNSNS.2005.6.3.271.
