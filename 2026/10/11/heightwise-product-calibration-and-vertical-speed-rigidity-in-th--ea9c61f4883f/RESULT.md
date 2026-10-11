# Heightwise product calibration and vertical-speed rigidity in the Rikitake dynamo
## Finding
Consider the classical Rikitake two-disc dynamo
\[
\dot x=-\mu x+yz,
\qquad
\dot y=-\mu y+x(z-a),
\qquad
\dot z=1-xy,
\]
with
\[
\mu>0,
\qquad
a\ge0.
\]

Let \(\nu\) be any compactly supported invariant Borel probability measure.

Every directed nonlinear input obeys an exact stationary fiber regression:
\[
\boxed{
\mathbb E_\nu[yz\mid x]=\mu x
},
\]
\[
\boxed{
\mathbb E_\nu[x(z-a)\mid y]=\mu y
},
\]
and, most notably,
\[
\boxed{
\mathbb E_\nu[xy\mid z]=1
}.
\]

The last identity says that the quadratic product which controls vertical motion has exactly unit conditional mean on every height fiber. Equivalently,
\[
\boxed{
\mathbb E_\nu[(xy-1)g(z)]=0
}
\]
for every bounded Borel function \(g\).

The three regression residuals are precisely the coordinate speeds:
\[
yz-\mu x=\dot x,
\]
\[
x(z-a)-\mu y=\dot y,
\]
and
\[
xy-1=-\dot z.
\]

Conditional orthogonality therefore gives the exact speed defects
\[
\boxed{
\operatorname{Var}_\nu(yz)
=
\mu^2\operatorname{Var}_\nu(x)
+
\mathbb E_\nu[\dot x^2]
},
\]
\[
\boxed{
\operatorname{Var}_\nu(x(z-a))
=
\mu^2\operatorname{Var}_\nu(y)
+
\mathbb E_\nu[\dot y^2]
},
\]
and
\[
\boxed{
\operatorname{Var}_\nu(xy)
=
\mathbb E_\nu[\dot z^2]
}.
\]

The heightwise calibration also gives the stronger orthogonality family
\[
\operatorname{Cov}_\nu(h(z),xy)=0
\]
for every square-integrable function \(h(z)\). In particular,
\[
\boxed{
\operatorname{Cov}_\nu(z,xy)=0
}.
\]

Define
\[
\Delta=\sqrt{a^2+4\mu^2},
\qquad
z_+=\frac{a+\Delta}{2}.
\]
The two real finite equilibria are
\[
E_\pm
=
\left(
\pm\sqrt{\frac{z_+}{\mu}},
\,
\pm\sqrt{\frac{\mu}{z_+}},
\,
z_+
\right).
\]

The vertical speed defect has the exact rigidity classification
\[
\boxed{
\mathbb E_\nu[\dot z^2]=0
\quad\Longleftrightarrow\quad
\operatorname{supp}\nu\subseteq\{E_+,E_-\}.
}
\]

Consequently, every compact stationary state not supported on those equilibria satisfies
\[
\operatorname{Var}_\nu(z)>0,
\qquad
\operatorname{Var}_\nu(xy)>0,
\]
and therefore the Pearson correlation is defined and obeys
\[
\boxed{
\operatorname{Corr}_\nu(z,xy)=0
}.
\]

Since
\[
\mathbb E_\nu[xy]=1
\]
but \(xy\) is not almost surely constant in a non-equilibrium stationary state, one also has
\[
\boxed{
\nu\{xy<1\}>0,
\qquad
\nu\{xy>1\}>0.
}
\]

Thus every nonconstant periodic orbit spends positive time in both vertical-motion regions
\[
\dot z>0
\qquad\text{and}\qquad
\dot z<0,
\]
and crosses the surface
\[
xy=1
\]
at least twice during each least period.

The already published global identities
\[
\int xy\,d\nu=1,
\qquad
\int xyz\,d\nu=\int z\,d\nu,
\]
the mean-height floor, and its equilibrium equality rigidity are prior coverage. The finding assessed here is the stronger all-height-fibers calibration, its companion coordinate regressions, and the exact speed-defect and decorrelation consequences.

## Assumptions and scope
The theorem uses the standard Rikitake normalization
\[
\dot x=-\mu x+yz,
\qquad
\dot y=-\mu y+x(z-a),
\qquad
\dot z=1-xy.
\]

The damping parameter satisfies
\[
\mu>0,
\]
and the asymmetry parameter satisfies
\[
a\ge0.
\]

Compact support guarantees integrability of the polynomial observables and arbitrary one-coordinate antiderivative tests used in the proof. No ergodicity assumption is made.

The foundational two-disc dynamo article appeared in January 1958; checked bibliographic metadata resolves the date to 1 January 1958. A later mathematical treatment of the exact system lists primary MSC \(34C05\), with additional ordinary-differential-equation classifications.

The theorem applies separately to periodic-orbit measures, compact chaotic invariant measures, the two equilibrium atoms, and convex mixtures.

## Proof
Let \(L\) denote the generator of the flow.

Fix a continuous function \(\phi\) on the compact \(x\)-range of the support and choose a continuously differentiable antiderivative \(H\) with
\[
H'(x)=\phi(x).
\]
Then
\[
LH
=
\phi(x)(-\mu x+yz).
\]
Invariance gives
\[
\mathbb E_\nu[\phi(x)(yz-\mu x)]=0
\]
for every such \(\phi\), hence
\[
\mathbb E_\nu[yz\mid x]=\mu x.
\]

Applying the same argument to arbitrary antiderivatives of \(y\) gives
\[
\mathbb E_\nu[x(z-a)\mid y]=\mu y.
\]

For the height variable, let \(K'(z)=\psi(z)\). Then
\[
LK
=
\psi(z)(1-xy).
\]
Invariance yields
\[
\mathbb E_\nu[\psi(z)(xy-1)]=0
\]
for every continuous \(\psi\). Therefore
\[
\mathbb E_\nu[xy\mid z]=1.
\]
A monotone-class extension gives the displayed orthogonality for every bounded Borel \(g\).

For the first regression, write
\[
R_x=yz-\mu x=\dot x.
\]
Because
\[
\mathbb E[R_x\mid x]=0,
\]
the residual \(R_x\) is orthogonal in \(L^2(\nu)\) to every square-integrable function of \(x\). Thus
\[
\operatorname{Var}(yz)
=
\operatorname{Var}(\mu x+R_x)
=
\mu^2\operatorname{Var}(x)+\mathbb E[R_x^2].
\]
This proves the first speed defect. The second is identical.

For the vertical equation,
\[
xy=1-\dot z
\]
and
\[
\mathbb E[\dot z\mid z]=0.
\]
Since the conditional predictor is the constant \(1\),
\[
\operatorname{Var}(xy)
=
\mathbb E[\dot z^2].
\]
The same conditional orthogonality gives
\[
\operatorname{Cov}(h(z),xy)=0
\]
for every square-integrable \(h(z)\), and in particular
\[
\operatorname{Cov}(z,xy)=0.
\]

We now classify equality in the vertical defect.

Suppose
\[
\mathbb E_\nu[\dot z^2]=0.
\]
The nonnegative continuous function \(\dot z^2\) vanishes on the support, so every support trajectory satisfies
\[
z(t)=c
\]
and
\[
x(t)y(t)=1
\]
for all time.

By Poincaré recurrence, \(\nu\)-almost every support point is recurrent under the time-one map.

On a recurrent trajectory with \(xy=1\), neither \(x\) nor \(y\) vanishes and
\[
y=\frac1x.
\]
Since \(z=c\), the first equation reduces to the scalar autonomous equation
\[
\dot x
=
-\mu x+\frac{c}{x}.
\]
Any non-equilibrium solution of a one-dimensional autonomous equation is strictly monotone on its sign component and cannot be recurrent. Hence every recurrent point in the support is an equilibrium of the full Rikitake system.

The real equilibria for
\[
\mu>0,\qquad a\ge0
\]
are exactly \(E_+\) and \(E_-\). Since recurrent points have full \(\nu\)-measure and the equilibrium set is closed,
\[
\operatorname{supp}\nu\subseteq\{E_+,E_-\}.
\]

Conversely, every probability measure supported on
\[
\{E_+,E_-\}
\]
is invariant and has
\[
\dot z=0.
\]
This proves the equality classification.

If
\[
\operatorname{Var}(z)=0,
\]
then the invariant support lies in a single height plane. Invariance of the support forces
\[
\dot z=0
\]
there, and the equality classification again gives equilibrium support. Therefore every non-equilibrium-supported compact invariant measure has
\[
\operatorname{Var}(z)>0.
\]
The vertical defect is also positive, so
\[
\operatorname{Var}(xy)>0.
\]
Together with
\[
\operatorname{Cov}(z,xy)=0,
\]
this proves the strict non-equilibrium decorrelation statement.

Finally,
\[
\mathbb E[xy]=1.
\]
If
\[
xy\le1
\]
almost surely, equality of the mean would force
\[
xy=1
\]
almost surely, contradicting positive variance; the same argument excludes
\[
xy\ge1
\]
almost surely. Hence both strict regions have positive measure.

For a nonconstant periodic orbit, its normalized orbit measure is non-equilibrium-supported. The continuous periodic function
\[
t\longmapsto x(t)y(t)-1
\]
takes both signs. A sign-changing continuous function on a circle has at least two zeros, proving the stated crossing consequence.

## Verification
The packaged checker uses only the Python standard library and exact rational arithmetic.

It verifies the three pointwise residual identities
\[
yz-\mu x=\dot x,
\]
\[
x(z-a)-\mu y=\dot y,
\]
and
\[
xy-1=-\dot z.
\]

It verifies the abstract variance and covariance decompositions for a conditional residual orthogonal to its predictor.

It verifies the equilibrium algebra through the defining relations
\[
z_+(z_+-a)=\mu^2,
\]
\[
x_\pm y_\pm=1,
\]
and
\[
z_+=\mu x_\pm^2.
\]

The stored checker output is `VERIFY_OK`.

The conditional-expectation identities, Poincaré-recurrence equality classification, and periodic crossing theorem are analytic arguments; they are not inferred from finite numerical trajectories.

## Relationship to prior work
Rikitake introduced the coupled two-disc dynamo in 1958 as a model exhibiting reversals of electric current and magnetic field.

A published stationary-law result for the same classical flow already proves
\[
\int xy\,d\nu=1,
\]
\[
\int xyz\,d\nu=\int z\,d\nu,
\]
an exact mean-height floor, and equilibrium equality rigidity. That result was inspected at full statement and proof level. Those scalar balances are prior coverage and are excluded from the originality claim.

The present heightwise law is strictly stronger:
\[
\mathbb E[xy\mid z]=1
\]
is equivalent to the infinite family
\[
\mathbb E[(xy-1)g(z)]=0
\]
for arbitrary bounded Borel \(g\). Choosing
\[
g(z)=1
\]
or
\[
g(z)=z
\]
recovers the two previously published integrated identities, but those two scalar moments cannot recover the full conditional law.

Llibre and Valls give a complete mathematical treatment of Darboux integrability for the exact Rikitake vector field. Their full eighteen-page article was inspected. It classifies invariant algebraic surfaces, exponential factors, and polynomial, rational, and Darboux first integrals; it does not state an invariant-measure conditional regression or stationary variance defect.

Llibre and Messias study global dynamics, Poincaré compactification, unbounded trajectories, invariant planes in special parameter regimes, and creation of the Rikitake attractor. Those orbit-geometric results do not imply the heightwise conditional product law.

Kono studies paleomagnetic reversal statistics generated by the Rikitake model, including field-intensity and reversal-interval distributions. Statistical reversal distributions likewise do not imply the exact conditional mean of \(xy\) on every height fiber.

The accepted statement therefore strengthens known global stationary balances to a full heightwise calibration and supplies new exact vertical-speed and decorrelation consequences.

## Limitations
The theorem is restricted to compactly supported invariant probability measures. The Rikitake system also has unbounded trajectories, so no statement is made about arbitrary noncompact dynamics.

The equality classification uses invariant-probability recurrence and does not classify arbitrary nonrecurrent complete trajectories contained in special algebraic sets.

The law
\[
\mathbb E[xy\mid z]=1
\]
determines a conditional first moment, not the full conditional distribution of \(xy\) given \(z\).

The original 1958 article was checked through bibliographic metadata and its published abstract rather than a complete searchable full text. A complete 2008 same-object mathematical article and the complete published prior stationary-law result were inspected in full.

Because the generator argument is short, a differently phrased equivalent heightwise identity could remain in unindexed dynamo literature.

## References
1. T. Rikitake, “Oscillations of a system of disk dynamos,” Mathematical Proceedings of the Cambridge Philosophical Society 54, 89–105 (1958), DOI 10.1017/S0305004100033223.
2. M. Kono, “Rikitake two-disk dynamo and paleomagnetism,” Geophysical Research Letters 14, 21–24 (1987), DOI 10.1029/GL014i001p00021.
3. J. Llibre and C. Valls, “Darboux integrability and algebraic invariant surfaces for the Rikitake system,” Journal of Mathematical Physics 49, 032702 (2008), DOI 10.1063/1.2897983.
4. J. Llibre and M. Messias, “Global dynamics of the Rikitake system,” Physica D 238, 241–252 (2009), DOI 10.1016/j.physd.2008.10.011.
5. J. Llibre and C. Valls, “Analytical integrability of the Rikitake system,” Zeitschrift für angewandte Mathematik und Physik 61, 627–634 (2010), DOI 10.1007/s00033-009-0044-9.
