# Exact stationary current–speed disintegration and equilibrium-speed defect in the Hide–Skeldon–Acheson dynamo
## Finding
Consider the Hide–Skeldon–Acheson dynamo
\[
\dot x=x(y-1)-\beta z,\qquad
\dot y=\alpha(1-x^2)-\kappa y,\qquad
\dot z=x-\lambda z,
\]
with
\[
\alpha,\beta,\kappa,\lambda>0.
\]

Every compactly supported invariant probability measure \(\mu\) satisfies the two exact conditional laws
\[
\mathbb E_\mu[x^2\mid y]
=
1-\frac{\kappa}{\alpha}y,
\]
and
\[
\mathbb E_\mu[x\mid z]=\lambda z.
\]
In particular, the stationary support lies in the disk-speed half-space
\[
y\le \frac{\alpha}{\kappa}.
\]

The only compact invariant probability measure with
\[
\mathbb E_\mu[x^2]=0
\]
is the equilibrium atom at
\[
e_0=\left(0,\frac{\alpha}{\kappa},0\right).
\]

For every other compact invariant measure, write
\[
X_2=\mathbb E_\mu[x^2]>0,
\]
define the current-energy-weighted probability measure
\[
d\nu=\frac{x^2}{X_2}\,d\mu,
\]
and set
\[
y_*=1+\frac{\beta}{\lambda},
\qquad
D=\mathbb E_\mu[(x-\lambda z)^2].
\]
Then the exact defect law is
\[
\mathbb E_\nu[y]
=
y_*
-
\frac{\beta}{\lambda X_2}D.
\]
Consequently
\[
1<\mathbb E_\nu[y]\le y_*.
\]

The upper equality is rigid. It holds exactly when the support is contained in the equilibrium set. Besides \(e_0\), nonzero equilibria exist precisely when
\[
q^2
=
1-\frac{\kappa}{\alpha}\left(1+\frac{\beta}{\lambda}\right)
>0,
\]
in which case they are
\[
e_\pm
=
\left(
\pm q,
1+\frac{\beta}{\lambda},
\pm\frac{q}{\lambda}
\right).
\]
Thus every nontrivial invariant measure with
\[
\mathbb E_\nu[y]=y_*
\]
is a convex mixture of the available equilibrium atoms with positive total weight on \(e_+\) or \(e_-\). If the nonzero equilibria do not exist, every nontrivial compact invariant measure has the strict inequality
\[
\mathbb E_\nu[y]<y_*.
\]

## Assumptions and scope
The measure \(\mu\) is a Borel probability measure invariant under the flow and supported on a compact subset of \(\mathbb R^3\). Compact support guarantees integrability of all test functions used below and implies that every support point belongs to a bounded complete trajectory.

The positive-parameter normalization above is the standard Hide–Skeldon–Acheson form. In the physical interpretation, \(x\) is the dynamo current, \(y\) is the angular velocity of the disk, and \(z\) is the motor angular velocity or the corresponding third state in the capacitor variant. The parameters describe forcing and dissipation in the coupled electromechanical model.

The earliest verified public source for the model is dated 8 June 1996. The statement here concerns stationary compact recurrence. It does not assert existence of a chaotic attractor for arbitrary positive parameters.

## Proof
Let \(L\) be the generator of the flow.

For any continuous function \(\phi\) on the compact \(y\)-range, choose a continuously differentiable antiderivative \(H\) with
\[
H'(y)=\phi(y).
\]
Then
\[
LH
=
\phi(y)\bigl(\alpha(1-x^2)-\kappa y\bigr).
\]
Invariance gives
\[
\mathbb E_\mu\!\left[
\phi(y)\bigl(\alpha(1-x^2)-\kappa y\bigr)
\right]
=0
\]
for every such \(\phi\). Therefore
\[
\mathbb E_\mu[x^2\mid y]
=
1-\frac{\kappa}{\alpha}y.
\]
Because a conditional second moment is nonnegative,
\[
y\le\frac{\alpha}{\kappa}
\]
almost surely. A continuous function that is nonpositive almost surely on an invariant measure is nonpositive on its support, so the same bound holds on the support.

Likewise, for any continuous \(\psi\) on the compact \(z\)-range and any antiderivative \(K\) with \(K'(z)=\psi(z)\),
\[
LK=\psi(z)(x-\lambda z).
\]
Hence
\[
\mathbb E_\mu[x\mid z]=\lambda z.
\]

If
\[
\mathbb E_\mu[x^2]=0,
\]
then \(x=0\) on the support. Invariance of the support forces tangency to the plane \(x=0\), so
\[
0=\dot x=-\beta z.
\]
Thus \(z=0\) on the support. The remaining scalar equation is
\[
\dot y=\alpha-\kappa y.
\]
Its only solution bounded for all positive and negative time is
\[
y=\frac{\alpha}{\kappa}.
\]
Therefore the invariant measure is exactly \(\delta_{e_0}\).

Now assume
\[
X_2=\mathbb E_\mu[x^2]>0.
\]
Stationarity of \(x^2/2\) gives
\[
0
=
\mathbb E_\mu\!\left[
 x^2(y-1)-\beta xz
\right].
\]
Stationarity of \(z^2/2\) gives
\[
\mathbb E_\mu[xz]
=
\lambda\mathbb E_\mu[z^2].
\]
Consequently
\[
\mathbb E_\mu[x^2(y-1)]
=
\beta\lambda\mathbb E_\mu[z^2],
\]
and therefore
\[
\mathbb E_\nu[y]
=
1+rac{\beta\lambda\mathbb E_\mu[z^2]}{X_2}.
\]

The second conditional law implies the exact square defect
\[
D
=
\mathbb E_\mu[(x-\lambda z)^2]
=
X_2-\lambda^2\mathbb E_\mu[z^2].
\]
Substitution yields
\[
\mathbb E_\nu[y]
=
1+rac{\beta}{\lambda}
-
\frac{\beta}{\lambda X_2}D
=
y_*-\frac{\beta}{\lambda X_2}D.
\]
Since \(D\ge0\), this proves the upper bound.

For a nontrivial invariant measure one has
\[
\mathbb E_\mu[z^2]>0.
\]
Indeed, if \(z=0\) on the support then tangency to \(z=0\) gives \(x=0\), which is the already classified trivial equilibrium. Hence
\[
\mathbb E_\nu[y]
=
1+rac{\beta\lambda\mathbb E[z^2]}{X_2}
>1.
\]

Finally, upper equality is equivalent to
\[
D=0.
\]
Then the support lies in
\[
x=\lambda z.
\]
Along every support trajectory this makes
\[
\dot z=0,
\]
so both \(z\) and \(x=\lambda z\) are constant. The equation for \(y\) is then linear with constant forcing, and bounded completeness forces
\[
y=\frac{\alpha(1-x^2)}{\kappa}.
\]
The equation \(\dot x=0\) becomes
\[
x\left(y-1-\frac{\beta}{\lambda}\right)=0.
\]
If \(x=0\), the state is \(e_0\). Otherwise
\[
y=y_*=1+\frac{\beta}{\lambda}
\]
and
\[
x^2
=
1-\frac{\kappa}{\alpha}y_*.
\]
These are precisely \(e_+\) and \(e_-\) when the displayed square is positive. Therefore every equality measure is a convex mixture of the available equilibrium atoms, and every such mixture with nonzero current weight realizes equality.

## Verification
The accompanying checker symbolically verifies the generator identities
\[
L\left(\frac{x^2}{2}\right)
=
x^2(y-1)-\beta xz,
\]
\[
L\left(\frac{z^2}{2}\right)
=
xz-\lambda z^2,
\]
and the coordinate equations used for the two conditional laws.

It also verifies the algebraic defect identity
\[
1+\frac{\beta\lambda Z_2}{X_2}
=
1+\frac{\beta}{\lambda}
-
\frac{\beta}{\lambda X_2}
\left(X_2-\lambda^2 Z_2\right),
\]
and checks the formal nonzero-equilibrium relations.

The stored checker output is `VERIFY_OK`.

The conditional-expectation conclusions use arbitrary one-variable test functions, and the equality classification additionally uses invariance of compact support and bounded completeness. The checker is a verification of the algebraic certificates, not a finite simulation of the dynamical theorem.

## Relationship to prior work
Hide, Skeldon, and Acheson introduced the two single-disk homopolar dynamo models in 1996 and derived the coupled nonlinear equations from an electromechanical construction. Subsequent work analyzed bifurcations, chaotic regimes, and unstable periodic orbits in the same dynamo family.

A 2014 full treatment of the exact four-parameter system studies integrability. It classifies parameter values admitting first integrals and proves nonexistence of polynomial, rational, or Darboux first integrals in a broad nondegenerate regime. Direct full-text inspection did not locate invariant-probability or stationary-average statements.

A 2022 study proves boundedness, stability and Hopf-bifurcation results and exhibits equilibrium, hidden periodic, and hidden chaotic attractors. Its accessible description concerns orbit geometry and attractor coexistence rather than coordinatewise stationary disintegration.

A 2025 full treatment classifies invariant algebraic surfaces, polynomial and rational first integrals, Darboux invariants, and dynamics in the Poincaré ball. It uses the same equations and classifies the problem under MSC \(34C05\). Direct full-text inspection did not locate invariant-probability or stationary-average statements.

The present theorem is different in quantifier and content: it applies simultaneously to every compactly supported invariant probability measure and gives an exact current-intensity law at each disk speed together with an equality-rigid current-energy-weighted speed defect.

## Limitations
The theorem assumes
\[
\alpha,\beta,\kappa,\lambda>0.
\]
Degenerate or sign-indefinite parameter cases may have additional invariant subspaces and are not classified here.

The result gives necessary stationary identities and an equality classification. It does not determine a complete invariant density, prove ergodicity, or prove the existence of chaos for a given parameter choice.

The 2022 full article was not completely inspected through the available source path; its abstract and indexed material were compared, so an incidental differently phrased average identity there remains a residual literature risk. Short quadratic balance identities may also appear in older engineering literature under alternative physical notation.

The nonzero equilibrium coordinates and their existence condition are prior structural information and are not claimed as new. The novelty claim is restricted to the two conditional stationary laws, the current-energy-weighted defect, and its equality rigidity for arbitrary compact invariant measures.

## References
1. R. Hide, A. C. Skeldon, and D. J. Acheson, “A study of two novel self-exciting single-disk homopolar dynamos: Theory,” Proceedings of the Royal Society A 452, 1369–1395 (1996), DOI 10.1098/rspa.1996.0070.
2. I. M. Moroz, “The Hide, Skeldon, Acheson dynamo revisited,” Proceedings of the Royal Society A 463, 113–130 (2007), DOI 10.1098/rspa.2006.1758.
3. A. Mahdi and C. Valls, “Integrability of the Hide–Skeldon–Acheson dynamo,” arXiv:1404.1110 (2014).
4. X. Li, “New insights to the Hide-Skeldon-Acheson dynamo,” Discrete and Continuous Dynamical Systems - B 27, 6257–6267 (2022), DOI 10.3934/dcdsb.2021315.
5. É. Diz-Pita, J. Llibre, M. V. Otero-Espinar, and C. Valls, “On the integrability and dynamics of the Hide, Skeldon and Acheson differential system,” Electronic Journal of Qualitative Theory of Differential Equations 2025, No. 76, 1–29, DOI 10.14232/ejqtde.2025.1.76.
