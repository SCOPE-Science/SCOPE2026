# Exact frequency staircase for weighted harmonic Bergman circle traces

## Finding

Fix
\[
\alpha>-1,
\qquad
0<r<1.
\]
Let
\[
f(z)
=
c_0+
\sum_{n\ge1}
\left(
c_nz^n+d_n\overline z^n
\right)
\]
belong to the weighted harmonic Bergman space. Planar area is normalized as
\[
dA=\frac1\pi\,dx\,dy.
\]

Define the weighted area energy
\[
I_\alpha(f)
=
\int_{\mathbb D}
|f(z)|^2(1-|z|^2)^\alpha\,dA(z)
\]
and the weighted circle trace
\[
J_{\alpha,r}(f)
=
\int_{|z|=r}
|f(z)|^2(1-r^2)^{\alpha+1}\,|dz|.
\]

Then the exact sharp constant in
\[
J_{\alpha,r}(f)
\le
K_\alpha(r)I_\alpha(f)
\]
is
\[
K_\alpha(r)
=
2\pi r(1-r^2)^{\alpha+1}
\max_{n\ge0}
\frac{r^{2n}}{B(n+1,\alpha+1)},
\]
where \(B\) is the Euler beta function.

Put
\[
s_{\alpha,r}
=
\frac{(\alpha+1)r^2}{1-r^2}.
\]
If
\[
s_{\alpha,r}\notin\mathbb N,
\]
the unique maximizing degree is
\[
n_*=\lfloor s_{\alpha,r}\rfloor.
\]
If
\[
s_{\alpha,r}=m\in\mathbb N,
\]
exactly the two adjacent degrees
\[
m-1
\quad\text{and}\quad
m
\]
maximize.

Equivalently, the changes of maximizing degree occur exactly at
\[
r_m^2
=
\frac{m}{m+\alpha+1},
\qquad
m=1,2,\ldots.
\]

The complete extremizer family is therefore explicit. Define
\[
E_0=\operatorname{span}\{1\},
\]
and for
\[
n\ge1
\]
let
\[
E_n
=
\operatorname{span}\{z^n,\overline z^n\}.
\]
Away from a transition radius, the nonzero extremizers are precisely the elements of
\[
E_{n_*}\setminus\{0\}.
\]
At
\[
r=r_m,
\]
they are precisely the nonzero elements of
\[
E_{m-1}\oplus E_m.
\]

In the normalization used in the motivating weighted Bergman theorem,
\[
\|f\|_{a_\alpha^2}^2
=
(\alpha+1)I_\alpha(f),
\]
the exact coefficient is
\[
C_\alpha(r)
=
\frac{K_\alpha(r)}{\alpha+1}.
\]
Hence the source coefficient
\[
2\pi r
\]
is strictly nonsharp at every fixed radius
\[
0<r<1.
\]
It is nevertheless asymptotically sharp as a radius-uniform coefficient: for sufficiently small \(r\), constants are the unique maximizing frequency space and
\[
\frac{C_\alpha(r)}{2\pi r}
=
(1-r^2)^{\alpha+1}
\longrightarrow1
\qquad
(r\downarrow0).
\]

## Assumptions and scope

The space and normalization are those of the recent weighted harmonic Bergman circle theorem. In particular,
\[
dA=\pi^{-1}dx\,dy
\]
and the normalized weighted measure is
\[
dA_\alpha
=
(\alpha+1)(1-|z|^2)^\alpha\,dA.
\]

The result is the exact Hilbert-space case
\[
p=2
\]
for traces on centered circles. It does not claim a sharp constant for
\[
p\ne2
\]
or for arbitrary convex curves.

The sharp constant is radius-dependent. The statement that the source coefficient is asymptotically sharp means only that no fixed multiplicative factor smaller than one can improve it simultaneously for every sufficiently small positive radius.

## Proof

For
\[
n\ge0,
\]
polar coordinates and the normalization of \(dA\) give
\[
\int_{\mathbb D}
|z|^{2n}(1-|z|^2)^\alpha\,dA(z)
=
B(n+1,\alpha+1).
\]

Angular orthogonality of distinct harmonic Fourier modes therefore yields
\[
I_\alpha(f)
=
B(1,\alpha+1)|c_0|^2
+
\sum_{n\ge1}
B(n+1,\alpha+1)
\left(
|c_n|^2+|d_n|^2
\right).
\]

On the circle
\[
|z|=r,
\]
the modes are again orthogonal, and
\[
|dz|=r\,d\theta.
\]
Hence
\[
J_{\alpha,r}(f)
=
2\pi r(1-r^2)^{\alpha+1}
\left[
|c_0|^2
+
\sum_{n\ge1}
r^{2n}
\left(
|c_n|^2+|d_n|^2
\right)
\right].
\]

Both quadratic forms are diagonal in the same orthogonal decomposition. Their optimal comparison constant is therefore the largest diagonal quotient:
\[
K_\alpha(r)
=
2\pi r(1-r^2)^{\alpha+1}
\max_{n\ge0}
T_n,
\]
where
\[
T_n
=
\frac{r^{2n}}{B(n+1,\alpha+1)}.
\]

Using
\[
B(n+2,\alpha+1)
=
\frac{n+1}{n+\alpha+2}
B(n+1,\alpha+1),
\]
one obtains
\[
\frac{T_{n+1}}{T_n}
=
r^2
\frac{n+\alpha+2}{n+1}.
\]
Thus
\[
T_{n+1}>T_n
\]
exactly when
\[
n+1
<
\frac{(\alpha+1)r^2}{1-r^2},
\]
with equality exactly at equality of those two quantities.

It follows that if
\[
s_{\alpha,r}
=
\frac{(\alpha+1)r^2}{1-r^2}
\]
is not an integer, the sequence \(T_n\) increases up to
\[
n=\lfloor s_{\alpha,r}\rfloor
\]
and decreases afterwards. If
\[
s_{\alpha,r}=m\in\mathbb N,
\]
then
\[
T_{m-1}=T_m
\]
and these are the only two maximal entries.

Solving
\[
s_{\alpha,r}=m
\]
gives the transition radii
\[
r_m^2
=
\frac{m}{m+\alpha+1}.
\]

Because the two quadratic forms are diagonal with strictly smaller ratios off the maximizing eigenspaces, equality holds exactly on the claimed spaces
\[
E_{n_*}
\]
or
\[
E_{m-1}\oplus E_m.
\]

For the source-normalized norm,
\[
\|f\|_{a_\alpha^2}^2
=
(\alpha+1)I_\alpha(f),
\]
so the optimal coefficient is
\[
C_\alpha(r)
=
\frac{K_\alpha(r)}{\alpha+1}.
\]

To compare with the source theorem, observe that at any fixed radius
\[
0<r<1
\]
its proof bounds an increasing radial integral mean by replacing earlier means with their value at \(r\). For a nonzero harmonic function, strict radial growth occurs unless only the constant mode survives; even in the constant case the factor
\[
(1-r^2)^{\alpha+1}
\]
is strictly below one. The exact diagonal formula above therefore gives
\[
C_\alpha(r)<2\pi r.
\]

Finally, when \(r\) is small enough that
\[
s_{\alpha,r}<1,
\]
the constant mode is uniquely maximal. Since
\[
B(1,\alpha+1)=\frac1{\alpha+1},
\]
one then has
\[
\frac{C_\alpha(r)}{2\pi r}
=
(1-r^2)^{\alpha+1},
\]
which tends to one as
\[
r\downarrow0.
\]

## Verification

The motivating July 2026 primary paper was checked at its definition of the weighted harmonic Bergman norm, its centered-circle theorem, and the proof of that theorem. The source proves
\[
J_{\alpha,r}(f)
\le
2\pi r
\|f\|_{a_\alpha^2}^2
\]
in the case
\[
p=2,
\]
but does not state a fixed-radius sharp constant or classify equality cases.

The present computation was reconstructed directly from the harmonic Fourier expansion. Every constant is obtained from an exact beta integral and every extremizer statement follows from comparison of diagonal quadratic forms.

The transition law was checked algebraically from the exact consecutive ratio
\[
T_{n+1}/T_n.
\]
No finite sampling or numerical optimization is used.

## Relationship to prior work

The recent paper treats Gabriel and Frazer type inequalities in weighted harmonic Bergman spaces and gives a simple centered-circle estimate valid for all
\[
p>0.
\]
In the Hilbert case, the proof retains only monotonicity of radial means, so it does not use the complete Fourier diagonalization available at
\[
p=2.
\]

The exact diagonalization reveals a discrete frequency phase diagram that is invisible in the source bound: as the radius increases, the extremizing degree moves through successive integers, with two-degree degeneracy only at the explicitly listed transition radii.

General radial Toeplitz-operator theory explains why radial measures are diagonal on monomials and is compatible with the calculation. The literature inspected in that direction treats analytic Bergman spaces and general radial measures, or weighted pluriharmonic Toeplitz operators with bounded radial symbols. It does not state the present singular circle-trace norm, the exact beta-function maximum, or the full harmonic extremizer staircase.

Targeted searches under circle trace, weighted Bergman, exact norm, radial restriction, monomial extremizer, and transition-radius formulations did not locate a statement covering the result.

## Limitations

The result uses the Hilbert exponent
\[
p=2.
\]
For other exponents the Fourier modes do not diagonalize the norm comparison in this way.

Only centered circles are considered.

The result does not assert that the inspected radial-operator literature exhausts all possible older formulations of the same diagonal calculation. An unindexed equivalent corollary under operator-theoretic terminology remains a residual originality risk.

## References

1. H. Halder and R. Kumar, *Gabriel's and Frazer's problems for weighted Bergman spaces and their applications*, arXiv:2607.13543v1, 2026.
2. E. A. Maximenko and C. Pacheco, *Toeplitz operators in Bergman space induced by radial measures*, Complex Analysis and Operator Theory 19 (2025). DOI: 10.1007/s40590-025-00830-9.
3. S. Sun and Y. Lu, *Toeplitz operators on the weighted pluriharmonic Bergman space with radial symbols*, Journal of Function Spaces and Applications 2011 (2011), Article 210596.
