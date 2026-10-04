# Ellipsoids satisfy the Funk Hanner ratio conjecture in every dimension

## Finding

Let \(n\ge2\), let \(E\subset\mathbb R^n\) be a centered ellipsoid, and let \(H\) be any centered \(n\)-dimensional Hanner polytope. Write
\[
V_K(R)=\operatorname{Vol}_K(B_K(R))
\]
for the Holmes--Thompson volume of the centered forward Funk ball of radius \(R>0\).

Then
\[
R\longmapsto \frac{V_E(R)}{V_H(R)}
\]
is strictly increasing. In particular, for every \(0<r<R\),
\[
\boxed{
\frac{V_E(R)}{V_E(r)}
>
\frac{V_H(R)}{V_H(r)}
}.
\]
Thus the reversed Bishop--Gromov-type comparison proposed as Conjecture 10.2 by Faifman, Vernicos, and Walsh holds strictly when the centrally symmetric body is an ellipsoid.

More explicitly, define
\[
z(R)=\frac12\log(2e^R-1).
\]
Then
\[
\boxed{
\frac{V_E(R)}{V_H(R)}
=
\frac{n\,n!\,\omega_n^2}{4^n}
\frac{\displaystyle\int_0^{z(R)}\sinh^{\,n-1}(s)\,ds}{z(R)^n}
},
\]
where \(\omega_n\) is the Euclidean volume of the unit ball in \(\mathbb R^n\).

For \(n=1\), every centered ellipsoid and every Hanner polytope is an interval up to a linear map, so equality holds identically.

## Assumptions and scope

The Funk balls are forward balls centered at the origin, as in the centrally symmetric formulation of the conjecture. Volumes are Holmes--Thompson volumes.

The statement is invariant under invertible linear maps, so a centered ellipsoid may be reduced to the Euclidean unit ball. The Hanner-ball volume is independent of the chosen Hanner polytope of a fixed dimension.

The result proves the conjectured ratio inequality only for ellipsoids. It does not establish Conjecture 10.2 for arbitrary centrally symmetric convex bodies.

## Proof

Let
\[
\rho=1-e^{-R}.
\]
A centered forward Funk ball in a convex body \(K\) is the dilate \(\rho K\).

For the Euclidean unit ball \(B^n\), the polar body with respect to a point \(x\in B^n\) has Euclidean volume
\[
\frac{\omega_n}{(1-\lVert x\rVert^2)^{(n+1)/2}}.
\]
Therefore the Holmes--Thompson formula gives
\[
V_E(R)
=
n\omega_n
\int_0^\rho
\frac{t^{n-1}}{(1-t^2)^{(n+1)/2}}\,dt.
\]
This is also the ellipsoid formula appearing in Faifman's Funk-volume calculation.

Now put
\[
z=\operatorname{artanh}\rho.
\]
Since
\[
\rho=1-e^{-R},
\]
one has
\[
z
=
\frac12\log\frac{1+\rho}{1-\rho}
=
\frac12\log(2e^R-1).
\]
With the substitution
\[
t=\tanh s,
\]
the ellipsoid integral becomes
\[
V_E(R)
=
n\omega_n\int_0^z\sinh^{\,n-1}(s)\,ds.
\]

Faifman, Vernicos, and Walsh compute the centered Funk-ball volume of every \(n\)-dimensional Hanner polytope as
\[
V_H(R)
=
\frac{2^n}{n!\,\omega_n}
\bigl(\log(2e^R-1)\bigr)^n.
\]
Because
\[
\log(2e^R-1)=2z,
\]
this is
\[
V_H(R)
=
\frac{4^n}{n!\,\omega_n}z^n.
\]
Hence
\[
\frac{V_E(R)}{V_H(R)}
=
\frac{n\,n!\,\omega_n^2}{4^n}
G_n(z),
\]
where
\[
G_n(z)
=
\frac1{z^n}
\int_0^z\sinh^{\,n-1}(s)\,ds.
\]

It remains to prove that \(G_n\) is strictly increasing for \(n\ge2\). Substitute \(s=zu\):
\[
G_n(z)
=
\int_0^1
u^{n-1}
\left(
\frac{\sinh(zu)}{zu}
\right)^{n-1}
du.
\]
The function
\[
x\longmapsto\frac{\sinh x}{x}
\]
is strictly increasing on \(x>0\), because
\[
\frac{d}{dx}\frac{\sinh x}{x}
=
\frac{x\cosh x-\sinh x}{x^2},
\]
and the numerator has derivative
\[
x\sinh x>0
\]
and vanishes at \(x=0\).

Thus for every fixed \(u\in(0,1]\), the integrand defining \(G_n(z)\) is strictly increasing in \(z\), and it is positive on a set of positive measure. Therefore \(G_n\) is strictly increasing.

Since \(z(R)\) is strictly increasing in \(R\), the quotient \(V_E(R)/V_H(R)\) is strictly increasing. For \(0<r<R\),
\[
\frac{V_E(R)}{V_H(R)}
>
\frac{V_E(r)}{V_H(r)}.
\]
Rearranging gives
\[
\frac{V_E(R)}{V_E(r)}
>
\frac{V_H(R)}{V_H(r)},
\]
which is the desired strict special case of Conjecture 10.2.

## Verification

The standalone checker evaluates the ellipsoid volume in two independent coordinates:
\[
t\in[0,\rho]
\]
and
\[
s\in[0,z],
\]
and verifies the change of variables numerically for dimensions \(2\) through \(8\) over several radii.

It also compares the direct ellipsoid/Hanner quotient with the closed normalized form, stress-tests strict monotonicity for dimensions \(2\) through \(12\), checks the identity
\[
\tanh z(R)=1-e^{-R},
\]
and checks the small-radius limit
\[
\lim_{R\downarrow0}\frac{V_E(R)}{V_H(R)}
=
\frac{n!\,\omega_n^2}{4^n},
\]
the ratio of the ellipsoid and Hanner Mahler products.

The replay output is:

`VERIFY_OK Funk ellipsoid Hanner ratio`

These finite computations are consistency checks only. Strict monotonicity for every dimension and every positive radius is proved analytically above.

## Relationship to prior work

Faifman derived the Holmes--Thompson volume formula for centered Funk balls and evaluated it for ellipsoids. That work studies an absolute upper-volume problem and contains no Hanner-polytope or Bishop--Gromov ratio comparison.

Faifman, Vernicos, and Walsh later computed the exact Hanner-polytope Funk-ball volume and proved the fixed-radius Hanner lower bound for unconditional bodies. In the same paper they proposed the strictly stronger two-radius comparison as Conjecture 10.2. Their current published version still states that conjecture. Immediately afterward they discuss the opposite, direct Bishop--Gromov comparison with an ellipsoid and explain that it fails in general; they do not state the Hanner-ratio monotonicity for ellipsoids.

The fixed-radius inequality
\[
V_E(R)\ge V_H(R)
\]
does not imply the two-radius inequality. The additional step here is the exact normalization of the ellipsoid/Hanner quotient and the proof that it increases with radius.

Targeted searches for the conjecture number, Funk ellipsoid/Hanner volume ratios, reversed Bishop--Gromov terminology, and the hyperbolic-sine integral form did not locate an equivalent statement.

## Limitations

This is a special-case resolution of an open comparison, not a proof for all centrally symmetric bodies.

The derivation is short once the two published volume formulas are placed in the same radial coordinate. Because of that simplicity, there remains a residual possibility that the observation appears in notes or discussions not indexed by the searches performed. The inspected preprint and current published paper do not state it.

No claim is made about the false direct Bishop--Gromov upper comparison with ellipsoids discussed by Faifman, Vernicos, and Walsh.

## References

D. Faifman, “A Funk perspective on billiards, projective geometry and Mahler volume,” arXiv:2012.12159, first submitted 2020-12-22.

D. Faifman, C. Vernicos, and C. Walsh, “Volume growth of Funk geometry and the flags of polytopes,” arXiv:2306.09268, first submitted 2023-06-15; Geometry & Topology 29 (2025), 3773–3811, DOI 10.2140/gt.2025.29.3773.
