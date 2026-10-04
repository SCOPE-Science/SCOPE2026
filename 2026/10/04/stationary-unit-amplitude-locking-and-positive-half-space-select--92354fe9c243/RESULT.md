# Stationary unit-amplitude locking and positive-half-space selection in the Bouali Type III flow
## Finding
Consider the Bouali Type III system
\[
\dot x=\alpha x(1-y)-\beta z,\qquad
\dot y=\gamma y(x^2-1),\qquad
\dot z=\mu x,
\]
with
\[
\alpha,\beta,\gamma,\mu>0.
\]

Every compactly supported invariant probability measure \(\nu\) is supported in the closed half-space
\[
y\ge0.
\]
It satisfies the conditional stationary laws
\[
\mathbb E_\nu[x\mid z]=0
\]
and, for \(\nu\)-almost every positive value of \(y\),
\[
\mathbb E_\nu[x^2\mid y]=1.
\]

Let
\[
w=\nu(\{(0,0,0)\}).
\]
Then the entire stationary mass on the invariant plane \(y=0\) is the origin atom,
\[
\nu(y=0)=w,
\]
and the exact mass-amplitude locking law is
\[
\mathbb E_\nu[x^2]
=
\mathbb E_\nu[y]
=
1-w.
\]

If \(w<1\), normalize the restriction of \(\nu\) to \(y>0\). That non-origin stationary component gives positive mass to both sides of the unit-amplitude cylinder:
\[
|x|<1
\qquad\text{and}\qquad
|x|>1.
\]

Every nonconstant periodic orbit therefore lies entirely in \(y>0\) and satisfies
\[
\langle x^2\rangle=\langle y\rangle=1.
\]
In each least period it crosses \(|x|=1\) at least twice. It also crosses \(x=0\) at least twice.

For the parameter set used for the paper's displayed chaotic attractor,
\[
(\alpha,\beta,\gamma,\mu)=(3,2.2,1,0.001),
\]
these identities are unchanged: every non-equilibrium compact recurrent statistical state has mean \(y\) exactly one and mean-square \(x\) exactly one after removal of any origin atom.

## Assumptions and scope
The measure statements concern Borel probability measures invariant under the complete flow and supported on compact subsets of \(\mathbb R^3\). Compact support makes all polynomial generator identities and one-variable test-function identities below integrable.

All four parameters are positive. The periodic-orbit statement concerns a nonconstant classical periodic solution and its least positive period.

The source system is the three-dimensional model introduced by Bouali in 2013. The original presentation studies its unique equilibrium, Lyapunov exponents, parameter-driven toroidal regimes, and sensitivity of coexisting attractors to initial conditions. The result here concerns stationary recurrence shared by every compact invariant probability measure, not only the numerically displayed attractors.

## Proof
Let \(L\) be the generator of the flow. For every continuously differentiable test function \(H\), compact invariance gives
\[
\int LH\,d\nu=0.
\]

First take \(H\) to depend only on \(z\). Given any continuous \(\phi\) on the compact \(z\)-range, choose \(H'(z)=\phi(z)\). Then
\[
LH=\mu\phi(z)x.
\]
Hence
\[
\mathbb E_\nu[x\mid z]=0.
\]
In particular,
\[
\mathbb E_\nu[x]=0.
\]

Next take a test function depending only on \(y\). For arbitrary continuous \(\psi\) on the compact \(y\)-range, choose \(K'(y)=\psi(y)\). Then
\[
LK=\gamma\psi(y)y(x^2-1).
\]
Therefore
\[
y\left(\mathbb E_\nu[x^2\mid y]-1\right)=0
\]
almost surely. On \(y>0\),
\[
\mathbb E_\nu[x^2\mid y]=1.
\]

The sign of \(y\) is invariant because every trajectory satisfies
\[
y(t)=y(0)\exp\!\left(\gamma\int_0^t(x(s)^2-1)\,ds\right).
\]
Suppose an invariant probability measure assigned positive mass to \(y<0\). Because \(y<0\) is invariant, the normalized restriction to that set would again be an invariant probability measure. For any invariant measure, however, the identities
\[
L(z^2)=2\mu xz,
\]
\[
L(x^2)=2\alpha x^2(1-y)-2\beta xz,
\]
and
\[
Ly=\gamma y(x^2-1)
\]
give successively
\[
\mathbb E[xz]=0,
\]
\[
\mathbb E[x^2]=\mathbb E[x^2y],
\]
and
\[
\mathbb E[x^2y]=\mathbb E[y].
\]
Thus
\[
\mathbb E[y]=\mathbb E[x^2]\ge0,
\]
contradicting a probability measure supported in \(y<0\). Hence every compact invariant probability measure is supported in \(y\ge0\).

It remains to understand the invariant plane \(y=0\). On that plane the \((x,z)\)-subsystem is linear:
\[
\begin{pmatrix}\dot x\\ \dot z\end{pmatrix}
=
\begin{pmatrix}\alpha&-\beta\\ \mu&0\end{pmatrix}
\begin{pmatrix}x\\z\end{pmatrix}.
\]
Its characteristic polynomial is
\[
\lambda^2-\alpha\lambda+\beta\mu.
\]
Because \(\alpha,\beta,\mu>0\), both roots have positive real part. Thus the only bounded complete trajectory in \(y=0\) is the origin. Consequently the restriction of any compact invariant probability measure to \(y=0\) is an origin atom. Writing its mass as \(w\),
\[
\nu(y=0)=w.
\]

The conditional law on \(y>0\) now gives
\[
\mathbb E_\nu[x^2]
=
\int_{y>0}\mathbb E_\nu[x^2\mid y]d\nu
=
\nu(y>0)
=
1-w.
\]
Combining this with \(\mathbb E[y]=\mathbb E[x^2]\) yields
\[
\mathbb E_\nu[y]=1-w.
\]

Assume \(w<1\), and normalize the invariant restriction to \(y>0\), calling it \(\widehat\nu\). Then
\[
\mathbb E_{\widehat\nu}[x^2]=1.
\]
If \(\widehat\nu\) gave no mass to \(|x|>1\), this equality would force \(x^2=1\) almost surely. The same conclusion follows if it gave no mass to \(|x|<1\). But no compact invariant probability measure can be supported on \(x^2=1\) inside \(y>0\): an invariant trajectory there would have constant \(x=1\) or \(x=-1\), hence \(y'=0\), while \(z'=\mu x\ne0\), contradicting compactness. Therefore
\[
\widehat\nu(|x|<1)>0,
\qquad
\widehat\nu(|x|>1)>0.
\]

A nonconstant periodic orbit cannot lie in \(y=0\), because that plane has no nonzero bounded complete trajectory. It also cannot lie in \(y<0\), by the stationary half-space result applied to its normalized orbit measure. Thus it lies in \(y>0\), has no origin atom, and obeys
\[
\langle x^2\rangle=\langle y\rangle=1.
\]
The continuous periodic function \(x^2-1\) is not identically zero and has zero mean, so it takes both signs and has at least two zeros on the periodic circle. Hence the orbit crosses \(|x|=1\) at least twice. Finally, periodicity of \(z\) gives \(\langle x\rangle=0\); since \(x\) is not identically zero, it takes both signs and crosses \(x=0\) at least twice.

## Verification
The accompanying checker uses exact sparse-polynomial arithmetic over rational coefficients.

It verifies the generator identities
\[
Lz=\mu x,
\qquad
Ly=\gamma y(x^2-1),
\]
\[
L(z^2)=2\mu xz,
\]
and
\[
L(x^2)=2\alpha x^2(1-y)-2\beta xz.
\]
It also verifies the characteristic polynomial of the \(y=0\) linear subsystem,
\[
\lambda^2-\alpha\lambda+\beta\mu.
\]

The stored checker output is `VERIFY_OK`.

The conditional laws are exact weak generator consequences for arbitrary one-variable test functions; they are not inferred from finite samples. The half-space selection and mass-amplitude law use only those identities, invariance of the sign regions, and the elementary spectrum of the invariant linear plane.

## Relationship to prior work
Bouali's 2013 source gives exactly
\[
\dot x=\alpha x(1-y)-\beta z,
\qquad
\dot y=-\gamma y(1-x^2),
\qquad
\dot z=\mu x,
\]
with positive parameters. The paper identifies the origin as the unique equilibrium, studies the displayed chaotic parameter set \((3,2.2,1,0.001)\), computes Lyapunov quantities, varies \(\mu\) through toroidal regimes, and emphasizes strong dependence of coexisting attractors on initial conditions.

The inspected full text contains no invariant-measure, stationary-average, or moment formulation. Its final remarks explicitly call for further analytical descriptions. The theorem above supplies one such global description: all compact recurrent statistics select the nonnegative \(y\)-half-space, and every non-origin stationary component is locked to unit mean-square \(x\)-amplitude and unit mean \(y\), independently of the four positive parameter values.

Targeted published searches were run for the exact system title and equations together with invariant-measure, stationary-moment, unit-amplitude, half-space, and periodic-crossing formulations. No same-object statement implying the theorem was found. The closest indexed exact stationary identities concern different chaotic flows and do not transfer by a coordinate or parameter reduction identified here.

## Limitations
The result concerns compactly supported invariant probability measures and periodic orbits. It does not prove that a nontrivial compact recurrent set exists for every positive parameter quadruple, nor does it classify the multiple attractor basins observed numerically in the source.

The theorem constrains recurrent statistics but does not provide Lyapunov exponents, entropy, fractal dimension, or a least-period bound.

The original 2013 preprint was inspected in full through a public text rendering and checked against its arXiv record for the first public date. Targeted search cannot exclude a differently phrased or unindexed later statement of the same identities.

## References
1. S. Bouali, “A 3D Strange Attractor with a Distinctive Silhouette. The Butterfly Effect Revisited,” arXiv:1311.6128, first public version 2013-11-24.
2. Mathematics Subject Classification 2020, class \(37D45\): strange attractors and chaotic dynamics.
