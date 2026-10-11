# Barycenter-determined covariance anisotropy in the Tinkerbell map
## Finding
Consider the Tinkerbell map
\[
F_{a,b,c,d}(x,y)
=
\left(
x^2-y^2+ax+by,\,
2xy+cx+dy
\right).
\]

Let \(\mu\) be any compactly supported invariant Borel probability measure. Write its barycenter as
\[
m=(u,v)
=
\left(
\mathbb E_\mu[x],
\mathbb E_\mu[y]
\right)
\]
and its covariance matrix as
\[
\Sigma
=
\begin{pmatrix}
p&q\\
q&r
\end{pmatrix}.
\]

Then invariance forces the complete traceless part of \(\Sigma\):
\[
\boxed{
p-r
=
(1-a)u-bv-u^2+v^2
}
\]
and
\[
\boxed{
2q
=
-cu+(1-d)v-2uv
}.
\]

Define
\[
A(u,v)
=
(1-a)u-bv-u^2+v^2
\]
and
\[
B(u,v)
=
-cu+(1-d)v-2uv.
\]
Then the covariance-eigenvalue gap is exactly
\[
\boxed{
\lambda_{\max}(\Sigma)-\lambda_{\min}(\Sigma)
=
D(u,v)
:=
\sqrt{A(u,v)^2+B(u,v)^2}
}.
\]

If
\[
T=\operatorname{tr}\Sigma
=
\operatorname{Var}(x)+\operatorname{Var}(y),
\]
the two covariance eigenvalues are
\[
\boxed{
\lambda_\pm
=
\frac{T\pm D(u,v)}{2}
}.
\]
Consequently every compact stationary state obeys the sharp positive-semidefinite constraint
\[
\boxed{
T\ge D(u,v)
}.
\]

Equality holds exactly when
\[
\det\Sigma=0,
\]
equivalently when the covariance has rank at most one. In that equality case the measure is supported on an affine line unless it is a point mass.

There is a particularly rigid centered case:
\[
u=v=0
\quad\Longrightarrow\quad
A=B=0.
\]
Hence every centered compact stationary state is second-order isotropic:
\[
\boxed{
\operatorname{Var}_\mu(x)
=
\operatorname{Var}_\mu(y)
}
\]
and
\[
\boxed{
\operatorname{Cov}_\mu(x,y)=0
}.
\]

The same theorem has a compact complex form. Put
\[
Z=x+iy.
\]
Then
\[
\boxed{
\mathbb E_\mu
\left[
\left(
Z-\mathbb E_\mu Z
\right)^2
\right]
=
A(u,v)+iB(u,v)
}.
\]
Thus the mean of an invariant state determines its centered complex pseudocovariance exactly. The total centered energy
\[
\mathbb E_\mu
\left[
\left|
Z-\mathbb E_\mu Z
\right|^2
\right]
=
T
\]
may vary from one invariant state to another, but its anisotropic component is not free.

For the classical parameters
\[
(a,b,c,d)
=
\left(
\frac9{10},
-\frac{6013}{10000},
2,
\frac12
\right),
\]
the formulas become
\[
A(u,v)
=
\frac{u}{10}
+
\frac{6013}{10000}v
-u^2+v^2
\]
and
\[
B(u,v)
=
-2u+\frac{v}{2}-2uv.
\]
Therefore every invariant-state estimate at the classical chaotic parameters must satisfy
\[
\operatorname{Var}(x)+\operatorname{Var}(y)
\ge
\sqrt{
\left(
\frac{u}{10}
+
\frac{6013}{10000}v
-u^2+v^2
\right)^2
+
\left(
-2u+\frac{v}{2}-2uv
\right)^2
}.
\]

## Assumptions and scope
The map is the standard two-dimensional quadratic Tinkerbell map. Compact support guarantees the first and second moments used in the argument.

No ergodicity, uniqueness of a physical measure, or symmetry of \(\mu\) is assumed. The result applies to compactly supported periodic-orbit measures, chaotic invariant measures, fixed-point atoms, and convex mixtures.

A day-resolved 2001 publication uses the Tinkerbell map explicitly as a nonlinear two-dimensional state-space example. The model was already documented in the 1996 book *Chaos: An Introduction to Dynamical Systems*, but a day-level public date for that book was not used here. The structured date therefore uses 11 December 2001, the earliest checked day-resolved same-object publication.

A later rigorous paper proves chaos for the standard Tinkerbell map and lists primary MSC \(37D45\), with numerical-analysis classifications \(65G20\) and \(65G30\). The present invariant-measure statement is assigned primary MSC \(37D45\).

## Proof
Invariance of the first coordinate gives
\[
u
=
\mathbb E[x^2-y^2]+au+bv.
\]
Therefore
\[
\mathbb E[x^2-y^2]
=
(1-a)u-bv.
\]

Invariance of the second coordinate gives
\[
v
=
2\mathbb E[xy]+cu+dv.
\]
Therefore
\[
2\mathbb E[xy]
=
-cu+(1-d)v.
\]

Now
\[
p
=
\mathbb E[x^2]-u^2,
\qquad
r
=
\mathbb E[y^2]-v^2,
\]
so
\[
p-r
=
\mathbb E[x^2-y^2]-(u^2-v^2)
=
A(u,v).
\]
Likewise,
\[
q
=
\mathbb E[xy]-uv,
\]
hence
\[
2q
=
2\mathbb E[xy]-2uv
=
B(u,v).
\]

For a real symmetric covariance matrix
\[
\Sigma
=
\begin{pmatrix}
p&q\\
q&r
\end{pmatrix},
\]
the eigenvalue difference is
\[
\sqrt{(p-r)^2+4q^2}.
\]
Substituting the two stationary identities gives
\[
\lambda_{\max}-\lambda_{\min}
=
\sqrt{A^2+B^2}
=
D.
\]
Since the eigenvalue sum is
\[
T=p+r,
\]
the eigenvalues are
\[
\lambda_\pm
=
\frac{T\pm D}{2}.
\]
Covariance matrices are positive semidefinite, so
\[
\lambda_-\ge0,
\]
which is exactly
\[
T\ge D.
\]

Equality
\[
T=D
\]
holds exactly when
\[
\lambda_-=0,
\]
equivalently
\[
\det\Sigma=0.
\]
A zero covariance eigenvalue means that some nonzero linear functional has zero variance, so the measure is supported on the corresponding affine line. This also covers a point mass.

For the complex formulation,
\[
Z-\mathbb E Z
=
(x-u)+i(y-v).
\]
Squaring and taking expectations gives
\[
\mathbb E[(Z-\mathbb E Z)^2]
=
\operatorname{Var}(x)
-
\operatorname{Var}(y)
+
2i\operatorname{Cov}(x,y),
\]
which is exactly
\[
A+iB.
\]

If
\[
u=v=0,
\]
then
\[
A=B=0,
\]
so
\[
p=r,
\qquad
q=0.
\]
Thus the centered covariance matrix is a scalar multiple of the identity.

## Verification
The accompanying checker uses only the Python standard library and exact rational arithmetic.

It verifies the invariant first- and second-coordinate moment reductions symbolically at exact rational test data, the conversion from raw second moments to the covariance anisotropy pair
\[
(p-r,2q),
\]
the covariance eigenvalue identities, and
\[
4\det\Sigma=T^2-D^2.
\]

It also verifies the exact classical coefficients
\[
1-a=\frac1{10},
\qquad
-b=\frac{6013}{10000},
\qquad
1-d=\frac12,
\qquad
c=2.
\]

The stored checker output is `VERIFY_OK`.

No finite trajectory sample, numerical attractor image, or empirical covariance is used as proof.

## Relationship to prior work
Bremer and Kaplan use the Tinkerbell map as an explicit nonlinear state-space example for Markov-chain Monte Carlo reconstruction from noisy time series. Their complete manuscript writes the quadratic map and studies parameter inference, hidden-state reconstruction, measurement functions, and noise. It does not supply the stationary covariance relation proved here.

Goldsztejn, Hayes, and Collins give a rigorous computer-assisted proof of chaos for the standard Tinkerbell map. Their complete article writes
\[
F(x,y)
=
\left(
x^2-y^2+ax+by,\,
cx+2xy+dy
\right)
\]
and uses
\[
a=0.9,\qquad
b=-0.6013,\qquad
c=2,\qquad
d=0.5.
\]
Its main results concern containment shadowing, branching pseudo-orbits, and rigorous chaos. Full-text searches found no `covariance`, `moment`, `invariant measure`, `average`, or `mean` formulation matching the accepted result.

Later Tinkerbell work studies fractional difference variants, \(q\)-deformations, bifurcations, multistability, Lyapunov exponents, control, and encryption. Those modifications do not imply the exact invariant-measure covariance identities for the classical map.

The accepted statement is instead a second-order stationarity law. It says that the barycenter determines the full traceless covariance matrix, and in particular forces exact covariance isotropy whenever the invariant state is centered.

## Limitations
The theorem is a necessary stationary constraint. It does not prove existence or uniqueness of a physical invariant measure for arbitrary parameter values.

The barycenter determines covariance anisotropy but not the covariance trace
\[
T.
\]
Different invariant measures with the same barycenter can therefore still have different total second moments.

The equality
\[
T=D
\]
classifies rank-one covariance, not the invariant affine lines themselves.

The 1996 book predates the structured source date, but no day-level public date for that source was used. The date field therefore uses the earliest checked day-resolved same-object publication rather than inventing a day.

A short moment identity of this type could occur incidentally in unindexed literature under complex pseudocovariance or time-series terminology.

## References
1. C. L. Bremer and D. T. Kaplan, “Markov chain Monte Carlo estimation of nonlinear dynamics from time series,” *Physica D* 160, 116–126 (2001), DOI 10.1016/S0167-2789(01)00323-2.
2. K. T. Alligood, T. D. Sauer, and J. A. Yorke, *Chaos: An Introduction to Dynamical Systems*, Springer, 1996.
3. A. Goldsztejn, W. Hayes, and P. Collins, “Tinkerbell Is Chaotic,” *SIAM Journal on Applied Dynamical Systems* 10, 1480–1501 (2011), DOI 10.1137/100819011.
4. S. V. Iyengar and J. Balakrishnan, “The \(q\)-deformed Tinkerbell map,” *Chaos* 28, 113102 (2018), DOI 10.1063/1.5048798.
