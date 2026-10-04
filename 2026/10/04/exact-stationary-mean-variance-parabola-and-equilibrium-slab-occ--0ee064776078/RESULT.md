# Exact stationary mean–variance parabola and equilibrium-slab occupation in Sprott P
## Finding
Consider the generalized Sprott P family
\[
\dot x=a y+z,\qquad
\dot y=-x+y^2,\qquad
\dot z=x+b y,
\]
with
\[
a\in\mathbb R,\qquad b>0.
\]

Every compactly supported invariant probability measure \(\mu\) satisfies the conditional stationary laws
\[
\mathbb E_\mu[x\mid y]=y^2,
\]
\[
\mathbb E_\mu[x+b y\mid z]=0,
\]
and
\[
\mathbb E_\mu[a y+z\mid x]=0.
\]

Its first two \(y\)-moments obey
\[
\mathbb E_\mu[y^2]+b\,\mathbb E_\mu[y]=0,
\]
or equivalently the exact stationary circle law
\[
\mathbb E_\mu\!\left[\left(y+\frac b2\right)^2\right]=\frac{b^2}{4}.
\]

Define
\[
\theta=\frac{\mathbb E_\mu[x]}{b^2}
      =-\frac{\mathbb E_\mu[y]}{b}.
\]
Then
\[
0\le\theta\le1
\]
and
\[
\operatorname{Var}_\mu(y)=b^2\theta(1-\theta).
\]
The endpoint cases are rigid:
\[
\theta=0
\]
holds exactly for the atom at
\[
e_0=(0,0,0),
\]
while
\[
\theta=1
\]
holds exactly for the atom at
\[
e_1=(b^2,-b,ab).
\]

There is a stronger support consequence. Every compact invariant probability measure that is not a convex mixture of the two equilibrium atoms gives positive mass both to the open equilibrium slab
\[
-b<y<0
\]
and to its exterior
\[
y<-b\qquad\text{or}\qquad y>0.
\]
Thus no non-equilibrium compact recurrent statistical state can be supported entirely between the two equilibrium \(y\)-levels, and none can be supported entirely outside them.

For the original Sprott P parameters
\[
a=2.7,\qquad b=1,
\]
this becomes
\[
\mathbb E_\mu\!\left[\left(y+\frac12\right)^2\right]=\frac14,
\]
with equilibrium points
\[
(0,0,0),\qquad (1,-1,2.7).
\]
Every non-equilibrium compact stationary state therefore gives positive mass both to \(-1<y<0\) and to \(y<-1\) or \(y>0\).

## Assumptions and scope
A compactly supported invariant probability measure means a Borel probability invariant under the flow whose support is a compact subset of \(\mathbb R^3\). Compactness makes all polynomial coordinate functions and the one-variable antiderivative test functions used below integrable.

The parameterization is the two-parameter rescaling of Sprott P used in the later parameter-region study. The original chaotic parameter choice is \(a=2.7\), \(b=1\). The proof only needs \(b>0\); no sign restriction on \(a\) is required.

The primary source introducing the Sprott flows was published on 1 August 1994. A later same-author parameter study identifies Case P as a particularly strong candidate for coexistence of strange attractors and limit cycles, which makes invariant statistical constraints across possible coexisting recurrent components especially natural.

## Proof
Let \(L\) denote the generator. For every continuously differentiable test function \(H\) on a neighborhood of the compact support,
\[
\int LH\,d\mu=0.
\]

Take a continuous function \(\phi\) on the compact \(y\)-range and choose an antiderivative \(H\) satisfying \(H'(y)=\phi(y)\). Then
\[
LH=\phi(y)(-x+y^2).
\]
Therefore
\[
\mathbb E_\mu[\phi(y)(x-y^2)]=0
\]
for every such \(\phi\), which is exactly
\[
\mathbb E_\mu[x\mid y]=y^2.
\]

The same argument with one-variable antiderivatives in \(z\) and \(x\) gives
\[
\mathbb E_\mu[x+b y\mid z]=0
\]
and
\[
\mathbb E_\mu[a y+z\mid x]=0.
\]

Stationarity of the coordinate functions \(y\) and \(z\) gives
\[
\mathbb E_\mu[x]=\mathbb E_\mu[y^2]
\]
and
\[
\mathbb E_\mu[x]=-b\,\mathbb E_\mu[y].
\]
Hence
\[
\mathbb E_\mu[y(y+b)]=0.
\]
Completing the square yields
\[
\mathbb E_\mu\!\left[\left(y+\frac b2\right)^2\right]=\frac{b^2}{4}.
\]

Now set
\[
\theta=\frac{\mathbb E_\mu[y^2]}{b^2}
      =-\frac{\mathbb E_\mu[y]}{b}.
\]
Because \(\mathbb E[y^2]\ge0\), one has \(\theta\ge0\). Jensen's inequality gives
\[
b^2\theta=\mathbb E[y^2]
\ge \mathbb E[y]^2
=b^2\theta^2,
\]
so \(\theta\le1\). Subtracting the squared mean from the second moment gives
\[
\operatorname{Var}(y)=b^2\theta(1-\theta).
\]

If \(\theta=0\), then \(y=0\) almost surely. Invariance of the support then forces \(\dot y=0\), hence \(x=0\), and next \(\dot x=0\), hence \(z=0\). Thus \(\mu\) is the atom at \(e_0\).

If \(\theta=1\), then the variance formula gives \(y=-b\) almost surely. Support invariance gives
\[
0=\dot y=-x+b^2,
\]
so \(x=b^2\), and
\[
0=\dot x=-ab+z,
\]
so \(z=ab\). Thus \(\mu\) is the atom at \(e_1\).

For the support statement, define
\[
q(y)=y(y+b).
\]
Because \(b>0\),
\[
q(y)<0\quad\text{for }-b<y<0,
\]
while
\[
q(y)>0\quad\text{for }y<-b\text{ or }y>0,
\]
and \(q\) vanishes only at \(-b\) and \(0\).

Suppose first that \(\mu\) gives no mass to the exterior. Then \(q\le0\) almost surely, while \(\mathbb E[q]=0\); hence \(q=0\) almost surely. Thus the invariant support is contained in the two planes \(y=0\) and \(y=-b\). A continuous trajectory lying in this support has constant \(y\), because its image in the discrete set \(\{0,-b\}\) is connected. The equation \(\dot y=0\) gives \(x=y^2\), the equation \(\dot z=0\) gives \(x+b y=y(y+b)=0\), and \(\dot x=0\) gives \(z=-a y\). Therefore the support is contained in \(\{e_0,e_1\}\).

If instead \(\mu\) gives no mass to the open slab, then \(q\ge0\) almost surely. Again \(\mathbb E[q]=0\) forces \(q=0\) almost surely, and the same invariant-support argument gives a convex mixture of \(e_0\) and \(e_1\).

Taking contrapositives proves that every non-equilibrium-mixture invariant measure has positive mass in both regions.

## Verification
The accompanying checker uses exact sparse-polynomial arithmetic over rational coefficients and only the Python standard library.

It verifies the vector field and the exact generator identity
\[
L(y+z)=y(y+b),
\]
as well as the complete-square identity
\[
y(y+b)=\left(y+\frac b2\right)^2-\frac{b^2}{4}.
\]
It also verifies symbolically that
\[
e_0=(0,0,0),\qquad e_1=(b^2,-b,ab)
\]
are equilibria for arbitrary \(a\) and \(b\), and checks the original parameter values \(a=27/10\), \(b=1\).

The stored checker output is `VERIFY_OK`.

The conditional-expectation statements rely on arbitrary one-variable test functions, and the support classification uses invariance and continuity; these analytic steps are not finite experiments.

## Relationship to prior work
Sprott's 1994 paper introduced nineteen exceptionally simple three-dimensional chaotic flows and reported their critical points, Lyapunov exponents, and fractal dimensions. The later two-parameter study writes Case P as
\[
\dot x=a y+z,\qquad \dot y=-x+y^2,\qquad \dot z=x+b y,
\]
and identifies it as the strongest candidate in that family for coexistence of strange attractors and limit cycles.

Dimitrova and Yordanov studied approximate second-order, two-point statistical functions for generalized low-dimensional chaotic flows, including systems drawn from Sprott's collection. Their accessible abstract focuses on power-law spectral segments, quasi-periodic slow behavior, and approximate self-affinity; it does not state the exact one-point invariant-measure circle law or the support classification proved here.

Panchev systematically examined all nineteen Sprott systems using an asymptotic reformulation method. The accessible abstract states that thirteen systems can be rewritten as second-order oscillators with memory, that two of the remaining systems admit asymptotic nondifferential relations, and that statistical treatment is discussed. The complete article was not available in the inspected lawful sources, so it remains a specific prior-coverage risk rather than a basis for a whole-document noncoverage claim.

Starkov and Coria studied localization of periodic orbits for the Sprott systems and explicitly included Case P among systems for which algebraic localization conditions are obtained. For that reason no periodic-orbit localization or crossing theorem is claimed here. The accepted result instead concerns all compactly supported invariant probability measures, their exact conditional regressions, the full mean–variance parabola, and a two-sided occupation necessity across the equilibrium slab.

Targeted semantic searches for the exact circle law, the mean–variance parabola, the conditional regression \(\mathbb E[x\mid y]=y^2\), and the two-sided equilibrium-slab occupation statement returned no same-object result implying the theorem above.

## Limitations
The theorem concerns compactly supported invariant probability measures. It does not prove that a non-equilibrium compact invariant measure exists for every parameter pair, classify unbounded trajectories, or distinguish chaotic from periodic invariant measures.

The full texts of the 2001 statistics paper, the 2004 analytical-properties paper, and the 2005 periodic-localization paper were not all available in the inspected lawful sources. Their accessible abstracts were compared at the implication level, and they remain explicit bibliographic risks.

The support theorem is qualitative: it forces positive mass on both sides of the equilibrium-slab partition but does not give a lower bound on either occupation fraction.

## References
1. J. C. Sprott, “Some simple chaotic flows,” Physical Review E 50, R647–R650 (1994), DOI 10.1103/PhysRevE.50.R647.
2. J. C. Sprott, “Dynamic Regions in Simple Chaotic Flows,” technical note dated 27 April 2013, last modified 1 September 2014.
3. E. S. Dimitrova and O. I. Yordanov, “Statistics of Some Low-Dimensional Chaotic Flows,” International Journal of Bifurcation and Chaos 11, 2675–2682 (2001), DOI 10.1142/S0218127401003735.
4. S. Panchev, “Analytical properties of the Sprott's chaotic flows,” Chaos, Solitons & Fractals 21, 721–728 (2004), DOI 10.1016/j.chaos.2003.12.054.
5. K. E. Starkov and L. N. Coria, “Localization of Periodic Orbits of Polynomial Sprott Systems with One or Two Quadratic Monomials,” International Journal of Nonlinear Sciences and Numerical Simulation 6, 271–278 (2005), DOI 10.1515/IJNSNS.2005.6.3.271.
