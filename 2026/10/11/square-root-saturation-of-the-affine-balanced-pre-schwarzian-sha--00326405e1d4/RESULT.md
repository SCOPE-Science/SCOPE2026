# Square-root saturation of the affine-balanced pre-Schwarzian shadow

## Finding

For
\[
0<k<1,
\]
let
\[
x_k
=
\frac{
3-k^2-\sqrt{(1-k^2)(9-k^2)}
}{2}
\]
and
\[
C(k)
=
\frac{2x_k^{3/2}}{k(1+x_k)}.
\]
This is the sharp pre-Schwarzian shadow constant in the recent affine-balancing theorem for harmonic quasiconformal mappings.

Introduce the optimal affine quasiconformal constant
\[
K=\frac{1+k}{1-k}.
\]
For a canonically balanced mapping this is exactly
\[
K_{\mathrm{aff}}=e^{r_{\mathrm{aff}}},
\]
where
\[
r_{\mathrm{aff}}
\]
is the affine hyperbolic circumradius.

Then, in the high-distortion regime
\[
K\to\infty,
\]
the sharp constant has the expansion
\[
C(k)
=
1
-
2\sqrt2\,K^{-1/2}
+
3K^{-1}
+
O(K^{-3/2}).
\]

The source's one-variable Schwarz-Pick extremum occurs at
\[
t_k=\sqrt{x_k}.
\]
For the sharp model
\[
\Omega(z)=kz,
\]
the maximizing disk radius is
\[
r_k=\frac{t_k}{k}.
\]
It satisfies
\[
r_k
=
1
-
\sqrt2\,K^{-1/2}
+
2K^{-1}
+
O(K^{-3/2}).
\]

Hence
\[
1-C(k)
\sim
2\sqrt2\,K^{-1/2},
\]
\[
1-r_k
\sim
\sqrt2\,K^{-1/2},
\]
and
\[
\frac{1-C(k)}{1-r_k}\longrightarrow2.
\]

Equivalently, with
\[
R=r_{\mathrm{aff}}=\log K,
\]
\[
1-C(k)
=
2\sqrt2\,e^{-R/2}
-
3e^{-R}
+
O(e^{-3R/2}),
\]
and
\[
1-r_k
=
\sqrt2\,e^{-R/2}
-
2e^{-R}
+
O(e^{-3R/2}).
\]

Thus the affine-optimal analytic-shadow estimate saturates at a square-root rate in the optimal quasiconformal distortion, and the sharpness mechanism simultaneously moves into a matched boundary layer in the source disk.

## Assumptions and scope

The source considers orientation-preserving harmonic mappings in the unit disk and associates to the image of the complex dilatation an affine hyperbolic circumradius
\[
r_{\mathrm{aff}}.
\]
For the canonical balanced representative
\[
F=H+\overline G,
\]
the balanced dilatation norm is
\[
k=\left\|\frac{G'}{H'}\right\|_\infty
=
\tanh\frac{r_{\mathrm{aff}}}{2},
\]
and the least quasiconformal distortion along the target-affine orbit is
\[
K_{\mathrm{aff}}
=
e^{r_{\mathrm{aff}}}
=
\frac{1+k}{1-k}.
\]

The source proves the sharp estimate
\[
\|P_H-P_F\|\le C(k)
\]
and proves that
\[
C(k)\uparrow1
\]
as
\[
k\uparrow1.
\]
The present result quantifies that endpoint and simultaneously tracks the maximizing point in the sharp Schwarz-Pick reduction.

No new assertion is made about the small-\(k\) regime; the source already gives its quadratic expansion. No Schwarzian-derivative estimate is claimed here.

## Proof

Put
\[
u=K^{-1/2}.
\]
Since
\[
K=\frac{1+k}{1-k},
\]
we have the exact identity
\[
k=\frac{1-u^2}{1+u^2}.
\]
Consequently,
\[
1-k^2
=
\frac{4u^2}{(1+u^2)^2}
\]
and
\[
9-k^2
=
\frac{
4(2+5u^2+2u^4)
}{
(1+u^2)^2
}.
\]

Substitution into the exact formula for
\[
x_k
\]
gives
\[
x_k
=
\frac{
1+4u^2+u^4
-
2u\sqrt{2+5u^2+2u^4}
}{
(1+u^2)^2
}.
\]
The right-hand side is analytic in
\[
u
\]
near
\[
u=0.
\]
Expanding its elementary square root yields
\[
x_k
=
1
-
2\sqrt2\,u
+
2u^2
+
\frac{3\sqrt2}{2}u^3
+
O(u^4).
\]

Taking the positive square root,
\[
t_k=\sqrt{x_k}
=
1
-
\sqrt2\,u
+
\frac{3\sqrt2}{4}u^3
+
O(u^4).
\]

Since
\[
\frac1k
=
\frac{1+u^2}{1-u^2}
=
1+2u^2+O(u^4),
\]
the maximizing source radius is
\[
r_k
=
\frac{t_k}{k}
=
1
-
\sqrt2\,u
+
2u^2
+
O(u^3).
\]

For the sharp constant,
\[
C(k)
=
\frac{2x_k^{3/2}}{k(1+x_k)}.
\]
Substitution of the preceding series, together with
\[
k
=
1-2u^2+O(u^4),
\]
gives
\[
C(k)
=
1
-
2\sqrt2\,u
+
3u^2
+
O(u^3).
\]
Returning to
\[
u=K^{-1/2}
\]
proves
\[
C(k)
=
1
-
2\sqrt2\,K^{-1/2}
+
3K^{-1}
+
O(K^{-3/2}),
\]
and
\[
r_k
=
1
-
\sqrt2\,K^{-1/2}
+
2K^{-1}
+
O(K^{-3/2}).
\]

The quotient conclusion follows immediately:
\[
\frac{1-C(k)}{1-r_k}
=
\frac{
2\sqrt2\,K^{-1/2}+O(K^{-1})
}{
\sqrt2\,K^{-1/2}+O(K^{-1})
}
\longrightarrow2.
\]

Finally,
\[
K=e^R
\]
for
\[
R=r_{\mathrm{aff}},
\]
so replacing
\[
K^{-1/2}
\]
by
\[
e^{-R/2}
\]
gives the intrinsic affine-radius formulation.

## Verification

The proof uses only exact identities from the source theorem and elementary expansion of radicals.

The change of variables
\[
u=K^{-1/2}
\]
was chosen because the exact affine relation becomes rational:
\[
k=(1-u^2)/(1+u^2).
\]
This makes the square-root endpoint at
\[
k=1
\]
an ordinary Taylor expansion at
\[
u=0.
\]

The expansion of
\[
x_k
\]
was independently checked by substituting it into the source critical-point equation
\[
x^2+(k^2-3)x+k^2=0.
\]
The expansions for
\[
r_k
\]
and
\[
C(k)
\]
were then replayed from their source formulas.

Representative numerical evaluations at large
\[
K
\]
agree with the first two asymptotic terms, but no numerical calculation is used as proof.

## Relationship to prior work

Wang and Zhong introduce the affine-balanced parameter
\[
k_{\mathrm{aff}},
\]
identify
\[
K_{\mathrm{aff}}=(1+k_{\mathrm{aff}})/(1-k_{\mathrm{aff}})=e^{r_{\mathrm{aff}}},
\]
and prove the exact sharp pre-Schwarzian shadow constant
\[
C(k).
\]
They establish strict monotonicity, the endpoint limit
\[
C(k)\to1
\]
as
\[
k\to1^-,
\]
and a quadratic expansion as
\[
k\to0.
\]
In the inspected full text, no rate is stated at the high-distortion endpoint and no asymptotic location of the maximizing disk point is derived.

Earlier harmonic pre-Schwarzian and quasiconformal-extension literature controls pre-Schwarzian quantities for fixed quasiconformal distortion, but does not contain the affine-balancing invariant or this source-specific sharp constant.

A separate recent analysis of the same affine-balancing paper studies a Schwarzian shadow gap in the opposite small-dilatation regime. That result concerns a different functional and does not imply the present high-distortion asymptotics for the sharp pre-Schwarzian constant or its maximizing location.

## Limitations

The result analyzes the high-distortion endpoint of the exact sharp constant already proved by the source. It does not improve the numerical value of that constant at fixed
\[
k.
\]

The maximizing radius
\[
r_k
\]
belongs to the source's sharp Schwarz-Pick model. The theorem does not claim that every extremizing realization has a unique physical point with exactly that Euclidean modulus.

Only the first two nontrivial terms are stated. Further powers of
\[
K^{-1/2}
\]
follow mechanically from the same algebraic formulas.

## References

1. Z.-G. Wang and D. Zhong, *Affine balancing of complex dilatations: affine invariants and optimal distortion of harmonic quasiconformal mappings*, arXiv:2609.37606v1, first posted 29 September 2026.
2. X. Wang, J. Fan, Z. Hu, and Z. Wang, *On the Univalence and Quasiconformal Extensions Criterion for Harmonic Mappings Associated with Pre-Schwarzian Derivative*, Chinese Annals of Mathematics, Series B 47 (2026), 475--490, DOI: 10.1007/s11401-026-0021-z.
3. Z.-G. Wang, X.-Y. Wang, A. Rasila, and J.-L. Qiu, *On a problem of Pavlović involving harmonic quasiconformal mappings*, arXiv:2405.19852.
