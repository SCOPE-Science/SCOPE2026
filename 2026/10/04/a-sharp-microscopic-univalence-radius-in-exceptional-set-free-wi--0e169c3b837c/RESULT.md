# A sharp microscopic univalence radius in exceptional-set-free Wiman–Valiron scaling

## Finding

Let \(F\in\mathcal S_0^p\) be an entire function in the exceptional-set-free Wiman–Valiron class for polylinear exhaustion, and let \(A\in\mathbb R^p\) satisfy
\[
L_F(r,A)\longrightarrow\infty.
\]
For each sufficiently large \(r\), let
\[
w_r\in\partial\mathbf G(r,A)
\]
obey
\[
|F(w_r)|
\ge
\frac{S_F(r,A)}{1+\varepsilon(r)},
\qquad
\varepsilon(r)\to0.
\]
Put
\[
L_r=L_F(r,A)
\]
and define
\[
G_r(\zeta)
=
\frac{F(w_r+A\zeta/L_r)}{F(w_r)}.
\]

Then
\[
G_r\longrightarrow e^\zeta
\]
locally uniformly on \(\mathbb C\). In particular, for every fixed
\[
R<\pi,
\]
the map \(G_r\) is univalent on
\[
\{|\zeta|<R\}
\]
for all sufficiently large \(r\).

The constant \(\pi\) is optimal as a universal asymptotic centered univalence radius. For the one-variable iterated exponential
\[
F(z)=\exp(e^z),
\]
one has exact collisions at rescaled radius
\[
R_r
=
e^r\arcsin(\pi e^{-r}),
\]
and
\[
R_r\longrightarrow\pi.
\]
Thus every proposed universal radius strictly larger than \(\pi\) eventually contains a collision for this admissible function.

## Assumptions and scope

The class \(\mathcal S_0^p\), the boundary supremum \(S_F(r,A)\), and the directional logarithmic growth \(L_F(r,A)\) are those in the exceptional-set-free polylinear Wiman–Valiron theory.

The source theorem supplies a function
\[
\delta(r)\longrightarrow\infty
\]
such that, uniformly for
\[
|\eta|
\le
\frac{\delta(r)}{L_r},
\]
one has
\[
\left|
\frac{F(w_r+A\eta)}{F(w_r)}
e^{-\eta L_r}
-
1
\right|
\le
\frac{
|\eta|\,\varkappa(r)L_r
}{
\delta(r)
},
\]
where
\[
\varkappa(r)
=
1+e(1+\varepsilon(r))
\]
is bounded as \(r\to\infty\).

The statement concerns injectivity of the one-complex-dimensional directional slice after the natural Wiman–Valiron scaling. It is not a global univalence theorem for \(F\) on \(\mathbb C^p\).

The sharpness statement means that \(\pi\) is the supremum of universal fixed radii for which eventual univalence follows for every admissible function and every admissible near-maximum family. It does not assert a universal failure exactly at the open radius \(\pi\).

## Proof

Fix a compact disk
\[
|\zeta|\le R.
\]
Set
\[
\eta=\frac{\zeta}{L_r}.
\]
Because
\[
\delta(r)\to\infty,
\]
the source neighborhood condition
\[
|\eta|\le\frac{\delta(r)}{L_r}
\]
holds for all sufficiently large \(r\).

The source estimate becomes
\[
\left|
G_r(\zeta)e^{-\zeta}-1
\right|
\le
\frac{
|\zeta|\varkappa(r)
}{
\delta(r)
}.
\]
The right side tends to zero uniformly for
\[
|\zeta|\le R.
\]
Therefore
\[
G_r(\zeta)\to e^\zeta
\]
locally uniformly on \(\mathbb C\).

We next transfer injectivity from the limit. Fix
\[
R<R_1<\pi.
\]
The exponential function is injective on
\[
|\zeta|<R_1,
\]
because two equal exponential values differ by an integer multiple of
\[
2\pi i,
\]
whereas two points in that disk have distance strictly less than
\[
2\pi.
\]

Local uniform convergence on the larger disk implies, by Cauchy's theorem for derivatives,
\[
G_r'\to e^\zeta
\]
uniformly on
\[
|\zeta|\le R.
\]
Suppose eventual injectivity on
\[
|\zeta|<R
\]
failed. Then there would be a sequence \(r_n\to\infty\) and distinct points
\[
\zeta_n,\omega_n\in\{|\zeta|<R\}
\]
such that
\[
G_{r_n}(\zeta_n)=G_{r_n}(\omega_n).
\]
After passing to a subsequence,
\[
\zeta_n\to\zeta,
\qquad
\omega_n\to\omega,
\]
with both limits in the closed radius-\(R\) disk.

If
\[
\zeta\ne\omega,
\]
local uniform convergence gives
\[
e^\zeta=e^\omega,
\]
contradicting injectivity of \(e^\zeta\) on the radius-\(R_1\) disk.

If
\[
\zeta=\omega,
\]
then
\[
0
=
\frac{
G_{r_n}(\zeta_n)-G_{r_n}(\omega_n)
}{
\zeta_n-\omega_n
}
=
\int_0^1
G_{r_n}'\!\left(
\omega_n+t(\zeta_n-\omega_n)
\right)\,dt.
\]
The line segment lies in the radius-\(R\) disk. Uniform derivative convergence makes the right side tend to
\[
e^\zeta\ne0,
\]
again a contradiction. Hence \(G_r\) is eventually univalent on every fixed disk of radius less than \(\pi\).

For sharpness, consider
\[
F(z)=\exp(e^z)
\]
in one variable with direction
\[
A=1.
\]
It is bounded on every half-plane
\[
\operatorname{Re}z<r,
\]
because
\[
|F(x+iy)|
=
\exp(e^x\cos y)
\le
\exp(e^r).
\]
On the boundary line
\[
\operatorname{Re}z=r,
\]
the maximum is attained at
\[
w_r=r,
\]
and
\[
S_F(r,1)=\exp(e^r),
\qquad
L_F(r,1)=e^r.
\]

This function satisfies the source regularity condition. For example, choose
\[
\delta(r)=\frac12e^{r/2}.
\]
Then
\[
\frac{L_F(r,1)}{\delta(r)}
=
2e^{r/2}\to\infty,
\]
and with
\[
h_r
=
\frac{\delta(r)}{L_F(r,1)}
=
\frac12e^{-r/2},
\]
the elementary inequalities
\[
e^{h_r}-1\le2h_r,
\qquad
1-e^{-h_r}\le h_r
\]
for large \(r\) give
\[
\left|
L_F(r\pm h_r,1)-L_F(r,1)
\right|
\le
\frac{L_F(r,1)}{\delta(r)}.
\]
Thus the iterated exponential is an admissible sharpness witness.

Write
\[
L_r=e^r
\]
and, for large \(r\), define
\[
a_r
=
\arcsin\!\left(\frac{\pi}{L_r}\right),
\qquad
R_r=L_ra_r.
\]
Then
\[
F(r+ia_r)
=
\exp\!\left(
L_re^{ia_r}
\right),
\]
while
\[
F(r-ia_r)
=
\exp\!\left(
L_re^{-ia_r}
\right).
\]
The two inner exponents differ by
\[
L_r
\left(
e^{ia_r}-e^{-ia_r}
\right)
=
2iL_r\sin a_r
=
2\pi i.
\]
Therefore
\[
F(r+ia_r)=F(r-ia_r),
\]
or, equivalently,
\[
G_r(iR_r)=G_r(-iR_r).
\]

Finally,
\[
R_r
=
L_r
\arcsin\!\left(
\frac{\pi}{L_r}
\right)
\longrightarrow
\pi.
\]
Hence for every
\[
R>\pi,
\]
both collision points eventually lie in
\[
|\zeta|<R.
\]
No larger universal fixed radius can be guaranteed.

## Verification

The full primary source was inspected at the class definition, the local near-maximum estimate, the exceptional-set-free asymptotic theorem, and the derivative discussion. Its local estimate is stronger than the derivative statement: after the scale change
\[
\eta=\frac{\zeta}{L_r},
\]
the error is
\[
O_R\!\left(
\frac1{\delta(r)}
\right),
\]
which gives local uniform convergence to the exponential function on every fixed rescaled disk.

The injectivity step uses only local uniform convergence on a slightly larger disk and the fact that
\[
e^\zeta
\]
is injective in every centered disk of radius less than \(\pi\).

The sharpness witness is exact. The source discussion explicitly includes iterated exponentials among the regular-growth examples. Independently, the displayed choice of \(\delta(r)\) verifies the defining variation condition for
\[
L_F(r,1)=e^r.
\]
The collision is certified by the exact identity
\[
L_r
\left(
e^{ia_r}-e^{-ia_r}
\right)
=
2\pi i.
\]

No finite experiment is used as evidence for the infinite statement.

## Relationship to prior work

Classical Wiman–Valiron theory describes local behavior near maximum-modulus points on Wiman–Valiron disks, usually outside an exceptional set. Hayman's survey and later work on the size of Wiman–Valiron disks emphasize this local asymptotic structure and its use for inverse branches.

The 2026 source removes exceptional sets for its regular polylinear class and proves an explicit local exponential approximation along the exhaustion direction. It does not state the resulting sharp centered univalence constant \(\pi\), nor does it give the iterated-exponential collision showing that no larger universal fixed constant is possible.

Related applications of classical Wiman–Valiron theory often pass to a local logarithm and prove univalence of that logarithm on suitable Wiman–Valiron regions. That is different from injectivity of the original function: exponentiation introduces the precise \(2\pi i\) periodic obstruction responsible for the constant \(\pi\) here.

Targeted searches for Wiman–Valiron local univalence, exponential scaling, injectivity near maximum-modulus points, and a radius-\(\pi\) statement did not locate a published theorem equivalent to this exceptional-set-free sharp radius.

## Limitations

The theorem controls only the directional one-variable slice
\[
\zeta
\mapsto
F(w_r+A\zeta/L_r).
\]
It does not give multivariable injectivity of \(F\).

The result guarantees every fixed radius
\[
R<\pi.
\]
It deliberately does not claim eventual univalence on the exact open disk of radius \(\pi\) for every admissible function.

The sharpness witness proves that no fixed radius
\[
R>\pi
\]
works uniformly. It does not classify all possible collision scales for general members of the class.

## References

1. O. Skaskiv, A. Bandura, T. Salo, S. Dubei, and L. Kryshtopa, *Entire Functions of Several Variables: Wiman–Valiron-Type Results Without Exceptional Sets*, Axioms 15 (2026), 667. DOI: 10.3390/axioms15090667.
2. W. K. Hayman, *The Local Growth of Power Series: A Survey of the Wiman–Valiron Method*, Canadian Mathematical Bulletin 17 (1974), 317–358. DOI: 10.4153/CMB-1974-064-0.
3. P. C. Fenton and E. F. Lingham, *The size of Wiman–Valiron discs for subharmonic functions of a certain type*, Complex Variables and Elliptic Equations 61 (2016), 456–468. DOI: 10.1080/17476933.2015.1095186.
