# Superquadratic Phelps–Rodrigues rigidity for Borcea variance

## Finding

Let \(F\) be a complex polynomial of degree
\[
n\ge2.
\]
Write its zeros, counted with multiplicity, as
\[
z_1,\ldots,z_n,
\]
and define
\[
h(F,F')
=
\max_{F(z)=0}
\min_{F'(\zeta)=0}
|z-\zeta|.
\]
For
\[
2<p<\infty,
\]
define
\[
\sigma_p(F)
=
\min_{c\in\mathbb C}
\left(
\frac1n
\sum_{j=1}^n
|z_j-c|^p
\right)^{1/p}.
\]

Then
\[
h(F,F')=\sigma_p(F)
\]
if and only if
\[
F(z)=A(z-c)^n-B
\]
for some
\[
A\ne0,
\qquad
B,c\in\mathbb C.
\]

Consequently, the Phelps–Rodrigues extremal conjecture for Borcea's variance inequality is valid for every finite exponent
\[
p>2.
\]

The case \(p=\infty\) is the already resolved Phelps–Rodriguez equality theorem for Sendov's conjecture. The argument below does not classify equality for \(p=2\), and it does not settle the still stronger range \(1<p<2\).

## Assumptions and scope

The fresh \(2\)-variance theorem states that for every polynomial of degree at least two,
\[
h(F,F')
\le
\sigma_2(F).
\]
The normalized power means are monotone, so for every
\[
p>2,
\]
\[
\sigma_2(F)\le\sigma_p(F).
\]

The second external ingredient is the boundary equality case of the Phelps–Rodriguez theorem, often called Rubinstein's theorem: if all zeros of a degree-\(n\) polynomial lie in the closed unit disk and \(1\) is a zero, then some critical point lies at distance strictly less than \(1\) from \(1\), unless the polynomial is a scalar multiple of
\[
z^n-1.
\]
By rotation, the same statement holds for any prescribed zero on the unit circle.

No equality statement for the fresh \(2\)-variance theorem itself is assumed.

## Proof

Assume first that
\[
h(F,F')=\sigma_p(F)
\]
for some
\[
2<p<\infty.
\]
The fresh \(2\)-variance theorem and monotonicity give
\[
h(F,F')
\le
\sigma_2(F)
\le
\sigma_p(F).
\]
The two endpoints are equal, so
\[
h(F,F')
=
\sigma_2(F)
=
\sigma_p(F).
\]

Choose a minimizing center \(c_p\) for \(\sigma_p(F)\), and set
\[
r_j=|z_j-c_p|.
\]
Then
\[
\sigma_2(F)
\le
\left(
\frac1n
\sum_{j=1}^n
r_j^2
\right)^{1/2}
\le
\left(
\frac1n
\sum_{j=1}^n
r_j^p
\right)^{1/p}
=
\sigma_p(F).
\]
Again the endpoints coincide, so equality holds in the normalized power-mean inequality
\[
\left(
\frac1n\sum r_j^2
\right)^{1/2}
\le
\left(
\frac1n\sum r_j^p
\right)^{1/p}.
\]
Because
\[
p>2,
\]
equality occurs only when
\[
r_1=\cdots=r_n.
\]
Denote this common value by \(R\).

If
\[
R=0,
\]
then every zero equals \(c_p\), hence
\[
F(z)=A(z-c_p)^n,
\]
which is already of the claimed form.

Suppose
\[
R>0.
\]
Define
\[
Q(w)=F(c_p+Rw).
\]
Every zero of \(Q\) lies on
\[
|w|=1.
\]
Critical points transform by the same affine map, and distances are divided by \(R\). Since
\[
h(F,F')=R,
\]
we obtain
\[
h(Q,Q')=1.
\]

The zero set is finite, so there is a zero \(a\) of \(Q\) for which
\[
\min_{Q'(\xi)=0}|a-\xi|=1.
\]
Rotate by \(\overline a\). The resulting polynomial has all zeros in the closed unit disk, has \(1\) as a zero, and has no critical point at distance less than \(1\) from that zero. Rubinstein's boundary rigidity theorem therefore forces it to be a scalar multiple of
\[
z^n-1.
\]
Undoing the rotation gives
\[
Q(w)=C(w^n-\omega)
\]
for some
\[
C\ne0,
\qquad
|\omega|=1.
\]
Undoing the affine normalization gives
\[
F(z)=A(z-c_p)^n-B.
\]

Conversely, let
\[
F(z)=A(z-c)^n-B,
\qquad
A\ne0.
\]
If \(B=0\), then all zeros and all critical points are at \(c\), so
\[
h(F,F')=\sigma_p(F)=0.
\]

If \(B\ne0\), the zeros form a regular \(n\)-gon centered at \(c\), all at radius
\[
\rho
=
\left|\frac BA\right|^{1/n}.
\]
The derivative is
\[
F'(z)=nA(z-c)^{n-1},
\]
so \(c\) is the unique critical point and
\[
h(F,F')=\rho.
\]

For
\[
p>1,
\]
the map
\[
u\longmapsto
\frac1n\sum_{j=1}^n|z_j-u|^p
\]
is strictly convex and is invariant under the rotations preserving the regular \(n\)-gon. Its unique minimizer must therefore be the fixed point \(c\). Hence
\[
\sigma_p(F)=\rho.
\]
Thus
\[
h(F,F')=\sigma_p(F),
\]
completing both directions.

## Verification

The fresh primary source was inspected through the definition and monotonicity of \(\sigma_p\), the statement of Borcea's \(p\)-variance conjectures, the new \(2\)-variance theorem, and the sharp regular-polygon example.

The older primary source defining the extremal conjecture was inspected through its variance definitions, the monotonicity lemma, the definition of \(h(F,F')\), the Phelps–Rodrigues equality conjecture, and its low-complexity equality result.

The boundary rigidity ingredient was checked in a full public proof of Rubinstein's theorem. It states precisely that a polynomial with all zeros in the unit disk and a zero at \(1\) has a critical point at distance less than \(1\), unless it is a scalar multiple of
\[
z^n-1.
\]

The only new bridge is strict power-mean equality. Once
\[
\sigma_2(F)=\sigma_p(F)
\]
with
\[
p>2,
\]
all distances from a \(p\)-minimizing center to the roots must be equal. This puts the entire zero configuration on one circle, exactly the setting where boundary Phelps–Rodriguez rigidity applies after normalization.

No numerical experiment or finite computation is used.

## Relationship to prior work

Khavinson, Pereira, Putinar, Saff and Shimorin formulated the Phelps–Rodrigues extremal conjecture: for
\[
p>1,
\]
equality in Borcea's variance inequality should occur exactly for polynomials of the form
\[
A(z-c)^n-B.
\]
They proved the \(2\)-variance inequality, with the corresponding equality form, for polynomials having at most three distinct zeros, but not in arbitrary degree.

The Phelps–Rodriguez equality theorem for Sendov's unit-disk problem is now resolved. That result handles the limiting radius case \(p=\infty\), but by itself does not imply a finite-\(p\) Borcea inequality because an average moment bound does not place all roots in a disk.

Zhang's 2026 theorem newly proves the missing \(p=2\) inequality in all degrees. Monotonicity immediately gives the inequality for all \(p>2\), but monotonicity alone does not classify equality. The strict equality case of the power-mean step is what converts a superquadratic extremizer into a unit-circle configuration, after which boundary Phelps–Rodriguez rigidity becomes applicable.

Targeted searches for Borcea variance equality, the Phelps–Rodrigues extremal conjecture, superquadratic equality cases, and regular-polygon rigidity did not locate a published statement of this all-degree finite-\(p>2\) classification.

## Limitations

The argument is genuinely superquadratic. At
\[
p=2,
\]
equality in the moment comparison provides no circularity of the root configuration, so the proof does not classify equality in the newly proved \(2\)-variance theorem.

For
\[
1<p<2,
\]
the fresh \(2\)-variance theorem does not imply Borcea's stronger \(p\)-variance inequality.

The result concerns exact equality. No quantitative stability estimate is claimed for near-extremizers.

## References

1. T. Zhang, *Borcea's \(2\)-variance conjecture*, arXiv:2610.02035v1, 2026.
2. D. Khavinson, R. Pereira, M. Putinar, E. B. Saff and S. Shimorin, *Borcea's variance conjectures on the critical points of polynomials*, in *Notions of Positivity and the Geometry of Polynomials*, Birkhäuser, 2011, 283–309. DOI: 10.1007/978-3-0348-0142-3_16.
3. T. Tao, *A digestion of the proof of Sendov's conjecture*, 12 August 2026, including a proof of Rubinstein's boundary theorem.
4. D. Phelps and R. S. Rodriguez, *Some properties of extremal polynomials for the Ilieff conjecture*, Kodai Mathematical Seminar Reports 24 (1972), 172–175. DOI: 10.2996/kmj/1138846519.
