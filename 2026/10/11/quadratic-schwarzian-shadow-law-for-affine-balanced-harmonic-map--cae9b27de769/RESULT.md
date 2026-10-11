# Quadratic Schwarzian shadow law for affine-balanced harmonic maps

## Finding

Let
\[
F=H+\overline G
\]
be an orientation-preserving affine-balanced harmonic mapping of the unit disk, with analytic dilatation
\[
\Omega=\frac{G'}{H'}.
\]
For a quadratic differential \(T\), put
\[
\|T\|_2
=
\sup_{z\in\mathbb D}
(1-|z|^2)^2|T(z)|.
\]
For
\[
0\le k<1,
\qquad
M\ge0,
\]
define
\[
\mathcal S_*(k,M)
=
\sup\left\{
\|S_H-S_F\|_2:
\|\Omega\|_\infty\le k,
\ \|P_F\|\le M
\right\},
\]
where the supremum ranges over affine-balanced orientation-preserving harmonic mappings.

Let \(\mathcal C(k)\) be the sharp pre-Schwarzian analytic-shadow constant
\[
x_k
=
\frac{3-k^2-\sqrt{(1-k^2)(9-k^2)}}2,
\]
\[
\mathcal C(k)
=
\frac{2x_k^{3/2}}{k(1+x_k)}
\quad(k>0),
\qquad
\mathcal C(0)=0.
\]
Then
\[
\boxed{
\mathcal S_*(k,M)
\le
\frac{8}{3\sqrt3}\frac{k^2}{1-k^2}
+M\mathcal C(k)
+\frac12\mathcal C(k)^2
}.
\]

At the zero pre-Schwarzian endpoint,
\[
\mathcal S_*(k,0)=0.
\]
For every fixed
\[
M>0,
\]
the optimal small-dilatation order is exactly quadratic:
\[
\frac8{27}
\le
\liminf_{k\downarrow0}
\frac{\mathcal S_*(k,M)}{k^2}
\le
\limsup_{k\downarrow0}
\frac{\mathcal S_*(k,M)}{k^2}
\le
\frac{8+2M}{3\sqrt3}.
\]

Thus the Schwarzian analytic-shadow problem has a genuine second-order law in the affine-balanced regime. The leading constant is not determined here, but the exponent \(2\) is sharp.

## Assumptions and scope

The harmonic pre-Schwarzian and Schwarzian are
\[
P_F=(\log J_F)_z,
\qquad
S_F=(P_F)_z-\frac12P_F^2.
\]
The pre-Schwarzian norm is
\[
\|P_F\|
=
\sup_{z\in\mathbb D}
(1-|z|^2)|P_F(z)|.
\]

The recent affine-balancing theory proves the sharp first-order analytic-shadow estimate
\[
\|P_H-P_F\|
\le
\mathcal C(k),
\qquad
k=\|\Omega\|_\infty,
\]
and poses the corresponding Schwarzian problem because second derivatives of \(\Omega\) enter.

The present result determines the optimal power of \(k\) for every fixed positive pre-Schwarzian budget \(M\). It does not determine the sharp function \(\mathcal S_*(k,M)\) or its exact leading coefficient.

## Proof

Set
\[
Q
=
P_H-P_F
=
\frac{\overline\Omega\,\Omega'}{1-|\Omega|^2}.
\]
Since
\[
P_H=P_F+Q,
\]
we have
\[
S_H-S_F
=
Q_z-P_FQ-\frac12Q^2.
\]
Differentiating \(Q\) with respect to \(z\) gives
\[
Q_z
=
\frac{\overline\Omega\,\Omega''}{1-|\Omega|^2}
+Q^2.
\]
Therefore
\[
S_H-S_F
=
\frac{\overline\Omega\,\Omega''}{1-|\Omega|^2}
-P_FQ
+\frac12Q^2.
\]

We first control the second-derivative term. Let
\[
\psi:\mathbb D\to\mathbb D
\]
be analytic. Fix \(z\in\mathbb D\), and let
\[
\phi_z(\zeta)
=
\frac{z+\zeta}{1+\overline z\zeta}.
\]
For
\[
\Psi=\psi\circ\phi_z,
\]
the second-order Schwarz--Pick estimate at the origin gives
\[
|\Psi''(0)|
\le
2(1-|\Psi(0)|^2).
\]
Indeed, after applying the disk automorphism that sends \(\Psi(0)\) to zero, one writes the resulting Schur function as \(\zeta u(\zeta)\) and applies Schwarz--Pick to \(u\) at zero.

The chain rule yields
\[
\Psi''(0)
=
(1-|z|^2)^2\psi''(z)
-2\overline z(1-|z|^2)\psi'(z).
\]
Ordinary Schwarz--Pick also gives
\[
(1-|z|^2)|\psi'(z)|
\le
1-|\psi(z)|^2.
\]
Hence
\[
(1-|z|^2)^2|\psi''(z)|
\le
2(1+|z|)(1-|\psi(z)|^2)
\le
4(1-|\psi(z)|^2).
\]

For \(k>0\), write
\[
\Omega=k\psi,
\qquad
|\psi|\le1.
\]
With
\[
t=|\psi(z)|,
\]
the preceding estimate gives
\[
(1-|z|^2)^2
\frac{|\overline\Omega\,\Omega''|}{1-|\Omega|^2}
\le
4k^2
\frac{t(1-t^2)}{1-k^2t^2}.
\]
Since
\[
\max_{0\le t\le1}t(1-t^2)
=
\frac{2}{3\sqrt3},
\]
and
\[
1-k^2t^2\ge1-k^2,
\]
we obtain
\[
\left\|
\frac{\overline\Omega\,\Omega''}{1-|\Omega|^2}
\right\|_2
\le
\frac{8}{3\sqrt3}
\frac{k^2}{1-k^2}.
\]

The sharp pre-Schwarzian shadow theorem gives
\[
\|Q\|
\le
\mathcal C(k).
\]
Therefore
\[
\|P_FQ\|_2
\le
M\mathcal C(k),
\]
and
\[
\frac12\|Q^2\|_2
\le
\frac12\mathcal C(k)^2.
\]
Combining these three bounds proves
\[
\mathcal S_*(k,M)
\le
\frac{8}{3\sqrt3}\frac{k^2}{1-k^2}
+M\mathcal C(k)
+\frac12\mathcal C(k)^2.
\]

The source proves
\[
\mathcal C(k)
=
\frac{2}{3\sqrt3}k^2+O(k^4).
\]
Consequently,
\[
\limsup_{k\downarrow0}
\frac{\mathcal S_*(k,M)}{k^2}
\le
\frac{8+2M}{3\sqrt3}.
\]

For the lower bound, take
\[
F_k(z)
=
z+\frac{k}{3}\overline z^{\,3}.
\]
Then
\[
H(z)=z,
\qquad
\Omega_k(z)=kz^2.
\]
Its dilatation image is the Euclidean disk \(k\mathbb D\), so it is affine-balanced. The standard realization argument gives global univalence for every
\[
0<k<1.
\]
Here
\[
Q(z)
=
\frac{2k^2z\overline z^{\,2}}
{1-k^2|z|^4},
\qquad
P_{F_k}=-Q.
\]
Thus
\[
\|P_{F_k}\|
\le
\frac{2k^2}{1-k^2},
\]
so for every fixed \(M>0\) this family is admissible for all sufficiently small \(k\).

A direct differentiation gives
\[
S_H-S_{F_k}
=
\frac{2k^2\overline z^{\,2}}
{1-k^2|z|^4}
+
\frac{6k^4z^2\overline z^{\,4}}
{(1-k^2|z|^4)^2}.
\]
At
\[
|z|^2=\frac13,
\]
we therefore have
\[
(1-|z|^2)^2|S_H-S_{F_k}|
=
\frac8{27}k^2+O(k^4).
\]
Hence
\[
\liminf_{k\downarrow0}
\frac{\mathcal S_*(k,M)}{k^2}
\ge
\frac8{27}.
\]

Finally, if
\[
\|P_F\|=0,
\]
then
\[
P_F\equiv0.
\]
From
\[
(P_F)_{\overline z}
=
-\frac{|\Omega'|^2}{(1-|\Omega|^2)^2}
\]
we obtain
\[
\Omega'\equiv0.
\]
Because \(F\) is balanced, the constant dilatation is zero. Then
\[
P_H=P_F=0,
\]
so \(H\) is affine and
\[
S_H=S_F=0.
\]
Thus
\[
\mathcal S_*(k,0)=0.
\]

## Verification

The primary 2026 source was checked through its definitions of the harmonic pre-Schwarzian and Schwarzian, the affine-balancing normalization, the realization lemma for prescribed analytic dilatations, the sharp pre-Schwarzian analytic-shadow theorem, and the stated Schwarzian open problem.

The only extra analytic input is the second-order Schwarz--Pick estimate used above. Its short proof is included, so no unquoted higher-order theorem is required.

The lower witness is exact. Its dilatation is
\[
kz^2,
\]
its image is exactly \(k\mathbb D\), and its global univalence follows from the source realization lemma. The coefficient
\[
\frac8{27}
\]
comes from evaluating the exact Schwarzian difference at the natural maximizer of the leading profile
\[
2r^2(1-r^2)^2.
\]

No numerical sampling, finite enumeration, or unproved limiting interchange is used.

## Relationship to prior work

Wang and Zhong introduce affine balancing and prove the sharp first-order estimate
\[
\|P_H-P_F\|
\le
\mathcal C(k).
\]
They then ask for a sharp Schwarzian analogue under a bound on
\[
\|P_F\|
\]
and explicitly note that second derivatives of the dilatation enter and that no second-order conclusion is asserted there.

Hernández and Martín developed the affine-invariant harmonic pre-Schwarzian and Schwarzian framework used here, including their chain rules and univalence applications. Their work does not contain affine balancing or a small-dilatation analytic-shadow comparison.

Earlier harmonic Schwarzian literature gives univalence, valence, extension, and norm criteria for \(S_F\) itself. Those results do not compare \(S_F\) with the classical Schwarzian of the analytic part under a globally optimized affine gauge.

The present theorem supplies an explicit finite candidate bound for the open affine-balanced Schwarzian problem and proves that the optimal small-\(k\) exponent is exactly \(2\) for every fixed positive pre-Schwarzian budget.

## Limitations

The exact sharp function
\[
\mathcal S_*(k,M)
\]
is not determined.

The upper and lower leading constants do not match. The theorem establishes the sharp exponent, not the sharp coefficient.

For \(M\) depending on \(k\), the displayed fixed-\(M\) asymptotic conclusion must be reinterpreted from the explicit nonasymptotic upper bound.

## References

1. Z.-G. Wang and D. Zhong, *Affine balancing of complex dilatations: affine invariants and optimal distortion of harmonic quasiconformal mappings*, arXiv:2609.37606v1, 2026.
2. R. Hernández and M. J. Martín, *Pre-Schwarzian and Schwarzian derivatives of harmonic mappings*, Journal of Geometric Analysis 25 (2015), 64--91; arXiv:1210.2330.
3. M. Chuaqui, P. Duren and B. Osgood, *Schwarzian derivative criteria for valence of analytic and harmonic mappings*, Mathematical Proceedings of the Cambridge Philosophical Society 143 (2007), 473--486.
