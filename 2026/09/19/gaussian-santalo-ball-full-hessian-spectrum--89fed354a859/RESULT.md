\
# Quartic stabilization of the critical translation mode in the Gaussian Santaló product

## Corrected scope

For
\[
G_\sigma^n(K)=\gamma_\sigma^n(K)\gamma_\sigma^n(K^\circ)
\]
at the Euclidean unit ball, the full support-function Hessian and its spherical-harmonic
diagonalization were already present in earlier SCOPE records on 17 and 18 September 2026.
This corrected record therefore does **not** claim that Hessian spectrum as new.

The surviving contribution is the first nonzero term on the translation branch exactly at the
quadratic threshold.

## Theorem

Let \(B=B_2^n\), \(n\ge2\), and set
\[
q=\sigma^{-2}=\frac{n+1}{2},
\qquad
m=\gamma_\sigma^n(B),
\qquad
R=\frac{c_{n,\sigma}e^{-q/2}|\mathbb S^{n-1}|}{m}.
\]
For a unit vector \(e\) and the actual translated balls \(K_t=B+te\),
\[
\boxed{
\frac{G_\sigma^n(B+te)}{m^2}
=
1-C_n t^4+O(t^6),
}
\tag{1}
\]
where
\[
\boxed{
C_n=
\frac{R(n+1)}{32n^2(n+2)}
\left(
2R(n+1)(n+2)+n(17-n^2)
\right)>0.
}
\tag{2}
\]
Thus the degree-one translation modes, which are exactly quadratic null directions at
\(\sigma^2=2/(n+1)\), bend downward at fourth order along the genuine translation family.

This does not by itself prove a complete fourth-order normal form or a topology-uniform local
maximality theorem at the endpoint.

## Independent derivation

Write
\[
A(t)=\gamma_\sigma^n(B+te),
\qquad
B_*(t)=\gamma_\sigma^n((B+te)^\circ).
\]
Let \(Y(u)=\langle u,e\rangle\) for \(u\) uniform on the sphere.  Then
\[
\mathbb E Y^2=\frac1n,
\qquad
\mathbb E Y^4=\frac{3}{n(n+2)}.
\tag{3}
\]

For the translated Gaussian ball, shifting the integration variable and expanding
\(\exp(-qtrY)\) together with \(\exp(-qt^2/2)\) gives, after the two radial integration-by-parts
recurrences,
\[
\frac{A(t)}m
=
1-\frac{R(n+1)}{4n}t^2
+
\frac{R(n+1)^2(n+3)}{64n(n+2)}t^4
+O(t^6).
\tag{4}
\]

For the polar body,
\[
\rho_{(B+te)^\circ}(u)=\frac1{1+tY(u)}.
\]
If
\[
F(r)=c_{n,\sigma}\int_0^r e^{-qs^2/2}s^{n-1}\,ds,
\]
then spherical averaging of
\(F((1+tY)^{-1})\) and differentiation of \(F\) at \(1\) yield
\[
\frac{B_*(t)}m
=
1+\frac{R(n+1)}{4n}t^2
+
\frac{R(n+1)(n^2-4n-37)}{64n(n+2)}t^4
+O(t^6).
\tag{5}
\]
The quadratic terms cancel, as required by the known Hessian kernel.  Multiplying (4) and (5)
gives (1)-(2).

To prove positivity, let
\[
I_0=\int_0^1e^{-qr^2/2}r^{n-1}\,dr,
\qquad
I_2=\int_0^1e^{-qr^2/2}r^{n+1}\,dr.
\]
The identity obtained from differentiating \(r^ne^{-qr^2/2}\) is
\[
R=n-q\frac{I_2}{I_0}>n-q=\frac{n-1}{2}.
\tag{6}
\]
Consequently the bracket in (2) is strictly larger than
\[
(n-1)(n+1)(n+2)+n(17-n^2)
=
2n^2+16n-2>0.
\]

## Relation to prior work

Artstein-Avidan, Fradelizi and Wyczesany identify the translated-ball threshold
\(\sigma^2=2/(n+1)\) in the uncentered Gaussian volume-product problem.  Earlier SCOPE records
`2026/09/17/gaussian-volume-product-hessian-spectrum--714d3bdc8013` and
`2026/09/18/gaussian-volume-product-hessian-instability-index--adb76edfac12`
already computed the full second variation and proved that translations are the only modes that
can lose quadratic stability.  Those facts are prior to this record and are not re-claimed.

The retained result resolves the next term on that critical branch: actual translations decrease
the product quartically at equality.

## Limitations

The theorem treats only the genuine translation family at the critical variance.  It does not
compute the complete fourth-order form on arbitrary perturbations coupled to the translation
kernel, and it does not settle the global maximization problem for
\(1/n<\sigma^2\le2/(n+1)\) in dimensions \(n\ge3\).
