# Stationary investment ceiling and price-adjustment defect in the Huang–Li finance model
## Finding
Consider the positive-parameter finance system
\[
\dot x=z+x(y-a),\qquad
\dot y=1-by-x^2,\qquad
\dot z=-x-cz,
\]
with
\[
a>0,\qquad b>0,\qquad c>0.
\]

Every compactly supported invariant probability measure \(\mu\) satisfies the exact conditional laws
\[
\mathbb E_\mu[x^2\mid y]=1-by
\]
and
\[
\mathbb E_\mu[x\mid z]=-cz.
\]
Because a conditional expectation of \(x^2\) is nonnegative,
\[
y\le \frac1b
\]
holds \(\mu\)-almost surely and therefore on the support.

Define the two equilibrium investment-demand levels
\[
y_0=\frac1b,
\qquad
y_1=a+\frac1c.
\]
Then the stationary mean-square price-adjustment speed has the exact defect representation
\[
\mathbb E_\mu[\dot z^2]
=
bc\,\mathbb E_\mu[(y_0-y)(y_1-y)]
=
c\,\mathbb E_\mu[x^2(y_1-y)]
\ge0.
\]

The defect vanishes exactly for probability measures supported on the equilibrium set.

For every invariant measure other than the central equilibrium atom, define the \(x^2\)-weighted probability measure
\[
d\nu
=
\frac{x^2}{\mathbb E_\mu[x^2]}\,d\mu.
\]
Then
\[
\mathbb E_\nu[y]
=
y_1-
\frac{\mathbb E_\mu[\dot z^2]}
{c\,\mathbb E_\mu[x^2]},
\]
and consequently
\[
a<\mathbb E_\nu[y]\le a+\frac1c.
\]
The upper equality holds exactly for equilibrium-supported measures.

When the two nonzero equilibria exist,
\[
a+\frac1c<\frac1b,
\]
every compact invariant probability measure that is not supported on equilibria satisfies
\[
\mu\!\left\{y<a+\frac1c\right\}>0.
\]
In particular every nonconstant periodic orbit undershoots the nonzero-equilibrium investment-demand level \(a+1/c\).

## Assumptions and scope
The measure \(\mu\) is a Borel probability measure invariant under the flow and supported on a compact subset of \(\mathbb R^3\). Compact support ensures integrability of the polynomial and antiderivative test functions used below and makes every support trajectory bounded and complete.

The variables are the standard interest-rate, investment-demand, and price-index coordinates of the model. The parameter assumptions are the standard positive regime.

The equilibrium set consists of
\[
P_0=\left(0,\frac1b,0\right)
\]
and, when
\[
1-b\left(a+\frac1c\right)>0,
\]
two additional equilibria \(P_\pm\) whose investment-demand coordinate is
\[
y_1=a+\frac1c.
\]

The earliest verified public source date is 15 November 2001, as recorded by the original-language publisher page for the first Ma–Chen article. A later English-edition archive page lists 18 November 2001; the earlier explicit publisher date is used here.

A later mathematical treatment classifies the same polynomial system with primary MSC \(34A05\).

## Proof
Let \(L\) denote the generator.

For any continuous function \(\phi\) on the compact \(y\)-range, choose an antiderivative \(H\) with
\[
H'(y)=\phi(y).
\]
Then
\[
LH
=
\phi(y)(1-by-x^2).
\]
Invariance gives
\[
\mathbb E_\mu[\phi(y)(1-by-x^2)]=0
\]
for every such \(\phi\). Hence
\[
\mathbb E_\mu[x^2\mid y]=1-by.
\]
Since the left side is nonnegative,
\[
y\le y_0=\frac1b
\]
almost surely.

Likewise, for any continuous function \(\psi\) on the compact \(z\)-range and an antiderivative \(K\),
\[
LK
=
\psi(z)(-x-cz),
\]
so
\[
\mathbb E_\mu[x\mid z]=-cz.
\]

Stationarity of \(z^2/2\) gives
\[
\mathbb E_\mu[xz]
=
-c\,\mathbb E_\mu[z^2].
\]
Therefore
\[
\mathbb E_\mu[\dot z^2]
=
\mathbb E_\mu[(x+cz)^2]
=
\mathbb E_\mu[x^2]-c^2\mathbb E_\mu[z^2].
\]

Next,
\[
L\left(\frac{x^2+z^2}{2}\right)
=
x^2(y-a)-cz^2.
\]
Thus
\[
c\,\mathbb E_\mu[z^2]
=
\mathbb E_\mu[x^2(y-a)].
\]
Using the conditional law,
\[
\mathbb E_\mu[x^2(y-a)]
=
\mathbb E_\mu[(1-by)(y-a)].
\]

It is useful first to keep the \(x^2\)-weighted form. Since
\[
y_1=a+\frac1c,
\]
we obtain
\[
\mathbb E_\mu[\dot z^2]
=
\mathbb E_\mu[x^2]
-
c\,\mathbb E_\mu[x^2(y-a)]
=
c\,\mathbb E_\mu[x^2(y_1-y)].
\]
Applying
\[
\mathbb E_\mu[x^2\mid y]
=
1-by
=
b(y_0-y)
\]
then gives
\[
\mathbb E_\mu[\dot z^2]
=
bc\,\mathbb E_\mu[(y_0-y)(y_1-y)].
\]

We now classify the zero defect. If
\[
\mathbb E_\mu[\dot z^2]=0,
\]
then \(\dot z=0\) on the invariant support, so
\[
x=-cz
\]
there. Along each support trajectory \(z\) is constant, hence \(x\) is constant.

If \(x=0\), then \(z=0\) and
\[
\dot y=1-by.
\]
The only bounded complete solution is
\[
y=\frac1b,
\]
giving \(P_0\).

If \(x\ne0\), the equation \(\dot x=0\) gives
\[
0=z+x(y-a)
=
x\left(y-a-\frac1c\right),
\]
so
\[
y=y_1.
\]
Then \(\dot y=0\) gives
\[
x^2=1-by_1,
\]
which yields exactly \(P_\pm\) when they exist. Therefore zero defect is equivalent to support on the equilibrium set. The converse is immediate.

Now assume
\[
\mathbb E_\mu[x^2]>0
\]
and define \(\nu\) as above. Dividing
\[
\mathbb E_\mu[\dot z^2]
=
c\,\mathbb E_\mu[x^2(y_1-y)]
\]
by \(c\mathbb E_\mu[x^2]\) gives
\[
\mathbb E_\nu[y]
=
y_1-
\frac{\mathbb E_\mu[\dot z^2]}
{c\,\mathbb E_\mu[x^2]}
\le y_1.
\]

Also
\[
\mathbb E_\mu[\dot z^2]
=
\mathbb E_\mu[x^2]-c^2\mathbb E_\mu[z^2].
\]
If \(\mathbb E_\mu[x^2]>0\), then \(\mathbb E_\mu[z^2]>0\): otherwise \(z=0\) on the invariant support and tangency would force \(x=0\), a contradiction. Hence
\[
\mathbb E_\mu[\dot z^2]
<
\mathbb E_\mu[x^2].
\]
It follows that
\[
\mathbb E_\nu[y]
>
y_1-\frac1c
=
a.
\]
Upper equality is exactly the zero-defect case, hence exactly equilibrium support.

Finally assume
\[
y_1<y_0
\]
and that \(\mu\) is not equilibrium-supported. Then the defect is strictly positive. If \(\mu\{y<y_1\}=0\), the support ceiling gives
\[
y_1\le y\le y_0
\]
almost surely, so
\[
(y_0-y)(y_1-y)\le0
\]
almost surely. This contradicts
\[
bc\,\mathbb E_\mu[(y_0-y)(y_1-y)]
=
\mathbb E_\mu[\dot z^2]
>0.
\]
Therefore
\[
\mu\{y<y_1\}>0.
\]
A normalized orbit measure of a nonconstant periodic orbit is not equilibrium-supported, so the periodic-orbit statement follows.

## Verification
The accompanying checker uses exact sparse-polynomial arithmetic over rational coefficients and formal variables.

It verifies
\[
L\left(\frac{z^2}{2}\right)
=
-xz-cz^2,
\]
\[
L\left(\frac{x^2+z^2}{2}\right)
=
x^2(y-a)-cz^2,
\]
and the exact algebraic reduction
\[
c x^2\left(a+\frac1c-y\right)
=
x^2-cx^2(y-a).
\]

It also verifies that the nonzero-equilibrium relations
\[
y=a+\frac1c,\qquad
z=-\frac{x}{c},\qquad
x^2=1-b\left(a+\frac1c\right)
\]
annihilate the vector field after clearing denominators.

The stored checker output is `VERIFY_OK`.

The conditional-expectation statements and equality classification use analytic stationarity and invariant-support arguments and are not inferred from finite experiments.

## Relationship to prior work
Ma and Chen's 2001 papers introduced and analyzed the nonlinear finance system through equilibria, bifurcations, periodic behavior, fractal structure, and chaos.

A later full mathematical preprint by Cândido, Llibre, and Valls writes the same positive-parameter polynomial system, lists the central and two possible nonzero equilibria, proves Hopf-bifurcation results, and proves absence of invariant algebraic surfaces. Its primary MSC classification is \(34A05\). Document-wide searches of the inspected preprint did not locate invariant-measure, average, or moment statements.

Szumiński's full 2018 article is especially relevant because it studies the same system's integrability and numerical recurrent dynamics. It explicitly asks whether the zero-parameter system has an invariant measure and leaves that question open after unsuccessful direct calculations. For positive parameters it exhibits a strange attractor numerically and proves broad meromorphic nonintegrability results. The article does not state the stationary conditional laws or the price-adjustment defect above.

Gao and Ma's 2009 paper studies the same finance system through numerical routes to chaos, strange nonchaotic attractors, delayed feedback, stability, and Hopf bifurcation. Only its abstract and bibliographic material were securely available in the inspected sources, so no whole-document noncoverage claim is made for it.

The accepted theorem is not an invariant-density existence theorem. It instead gives identities that every compactly supported invariant probability measure must satisfy, including equilibrium atoms, periodic-orbit measures, and chaotic stationary measures.

## Limitations
The theorem assumes positive \(a\), \(b\), and \(c\). The zero-parameter Nosé–Hoover limit discussed in the integrability literature is outside the accepted claim.

The result does not prove existence or uniqueness of a chaotic invariant measure, nor does it determine a density or Lyapunov spectrum.

The support ceiling
\[
y\le\frac1b
\]
is a stationary-support statement, not a claim that every transient solution remains below that level.

The complete Gao–Ma 2009 article was not securely available for full-text comparison. A differently phrased stationary balance could also remain in unindexed finance-system literature.

The novelty claim is restricted to the conditional stationary laws, the exact mean-square price-adjustment defect with its equilibrium equality class, the \(x^2\)-weighted investment interval, and the non-equilibrium undershoot consequence.

## References
1. J. Ma and Y. Chen, “Study for the bifurcation topological structure and the global complicated character of a kind of nonlinear finance system (I),” Applied Mathematics and Mechanics 22, 1240–1251 (2001), DOI 10.1007/BF02437847.
2. Q. Gao and J. Ma, “Chaos and Hopf bifurcation of a finance system,” Nonlinear Dynamics 58, 209–216 (2009), DOI 10.1007/s11071-009-9472-5.
3. M. R. Cândido, J. Llibre, and C. Valls, “Invariant algebraic surfaces and Hopf bifurcation of a finance model,” International Journal of Bifurcation and Chaos 28, 1850150 (2018), DOI 10.1142/S021812741850150X.
4. W. Szumiński, “Integrability analysis of chaotic and hyperchaotic finance systems,” Nonlinear Dynamics 94, 443–459 (2018), DOI 10.1007/s11071-018-4370-3.
