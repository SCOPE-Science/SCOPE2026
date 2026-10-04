# Every imbalanced orthogonal Herglotz mixture is nonstarlike

## Finding

Define
\[
R(z)
=
-z-2\log(1-z)
\]
and its quarter-turn rotation
\[
R_{\pi/2}(z)
=
iR(-iz)
=
-z-2i\log(1+iz).
\]
For
\[
0<s<1,
\]
put
\[
F_s(z)
=
sR(z)+(1-s)R_{\pi/2}(z).
\]

Then
\[
F_s\in\mathcal R\setminus\mathcal S^*
\]
for every
\[
s\ne\frac12.
\]

In other words, every unequal convex mixture of these two orthogonal Herglotz extremals has positive real derivative but fails to be starlike. The only parameter not decided by the present argument is the balanced midpoint
\[
s=\frac12.
\]

For each \(s\in(0,1)\), let \(t_s\in(0,\pi/2)\) be the unique angle satisfying
\[
\cos t_s-\sin t_s
=
1-2s.
\]
Then
\[
F_s'(e^{it_s})=0.
\]
When
\[
s\ne\frac12,
\]
the boundary starlikeness quantity changes sign at this derivative zero. Thus the failure of starlikeness is forced by a boundary turning mechanism rather than by the singular endpoints used in the original small-\(s\) argument.

## Assumptions and scope

The Noshiro–Warschawski class is
\[
\mathcal R
=
\left\{
f\in\mathcal A:
\operatorname{Re}f'(z)>0
\text{ for }z\in\mathbb D
\right\},
\]
and the starlike class is
\[
\mathcal S^*
=
\left\{
f\in\mathcal A:
\operatorname{Re}\frac{zf'(z)}{f(z)}>0
\text{ for }z\in\mathbb D
\right\}.
\]

The logarithms are the branches analytic in the unit disk and normalized by
\[
\log1=0.
\]

The result is specific to the orthogonal two-atom family \(F_s\). It does not classify arbitrary positive-real-derivative functions, arbitrary angular separations of two Herglotz atoms, or the midpoint \(F_{1/2}\).

## Proof

Differentiation gives
\[
R'(z)
=
\frac{1+z}{1-z},
\qquad
R_{\pi/2}'(z)
=
\frac{1-iz}{1+iz}.
\]
Both functions have positive real part in the disk, so every convex mixture satisfies
\[
\operatorname{Re}F_s'(z)>0.
\]
Hence
\[
F_s\in\mathcal R
\]
for all \(0<s<1\).

Now restrict temporarily to the first-quadrant boundary arc
\[
z=e^{it},
\qquad
0<t<\frac{\pi}{2}.
\]
The two Herglotz kernels have purely imaginary boundary values:
\[
\frac{1+e^{it}}{1-e^{it}}
=
i\cot\frac t2
\]
and
\[
\frac{1-ie^{it}}{1+ie^{it}}
=
-i\tan\left(\frac t2+\frac{\pi}{4}\right).
\]
Therefore
\[
F_s'(e^{it})
=
iY_s(t),
\]
where
\[
Y_s(t)
=
s\cot\frac t2
-
(1-s)
\tan\left(\frac t2+\frac{\pi}{4}\right).
\]
Furthermore,
\[
Y_s'(t)
=
-\frac{s}{2}\csc^2\frac t2
-
\frac{1-s}{2}
\sec^2\left(\frac t2+\frac{\pi}{4}\right)
<
0.
\]
Since \(Y_s(t)\to+\infty\) as \(t\downarrow0\) and \(Y_s(t)\to-\infty\) as \(t\uparrow\pi/2\), there is a unique zero \(t_s\).

A direct trigonometric simplification of \(Y_s(t_s)=0\) gives
\[
\cos t_s-\sin t_s
=
1-2s.
\]

We next determine the side on which the starlikeness quantity becomes negative. Put
\[
W_s(t)
=
e^{-it}F_s(e^{it}).
\]
Using
\[
F_s(e^{it})
=
e^{it}
\int_0^1
F_s'(re^{it})\,dr,
\]
we have
\[
\operatorname{Im}W_s(t)
=
\int_0^1
\operatorname{Im}F_s'(re^{it})\,dr.
\]

Write
\[
c=\cos t_s,
\qquad
q=\sin t_s.
\]
For \(0<r<1\),
\[
\operatorname{Im}F_s'(re^{it_s})
=
2r
\left[
\frac{sq}
{1-2rc+r^2}
-
\frac{(1-s)c}
{1-2rq+r^2}
\right].
\]
After putting the two terms over a common denominator, the numerator is
\[
sq(1-2rq+r^2)
-
(1-s)c(1-2rc+r^2).
\]
The root relation
\[
c-q=1-2s
\]
is equivalent to
\[
s=\frac{1-c+q}{2}.
\]
Using
\[
c^2+q^2=1,
\]
the numerator factors exactly as
\[
\frac12
(q-c)(1+c+q)(1-r)^2.
\]
All denominator factors are positive. Therefore, for every \(0<r<1\),
\[
\operatorname{sgn}
\operatorname{Im}F_s'(re^{it_s})
=
\operatorname{sgn}(q-c)
=
\operatorname{sgn}(2s-1).
\]
It follows that, whenever
\[
s\ne\frac12,
\]
\[
\operatorname{sgn}
\operatorname{Im}W_s(t_s)
=
\operatorname{sgn}(2s-1).
\]

Also,
\[
\operatorname{Re}W_s(t_s)
=
\int_0^1
\operatorname{Re}F_s'(re^{it_s})\,dr
>
0,
\]
so
\[
F_s(e^{it_s})\ne0.
\]
Thus the boundary starlikeness quotient is continuous near \(t_s\).

Since
\[
F_s'(e^{it})
=
iY_s(t),
\]
we obtain
\[
\frac{e^{it}F_s'(e^{it})}{F_s(e^{it})}
=
\frac{iY_s(t)}{W_s(t)},
\]
and hence
\[
\operatorname{Re}
\frac{e^{it}F_s'(e^{it})}{F_s(e^{it})}
=
\frac{
Y_s(t)\operatorname{Im}W_s(t)
}{
|W_s(t)|^2
}.
\]

If
\[
s<\frac12,
\]
then
\[
\operatorname{Im}W_s(t_s)<0.
\]
Because \(Y_s\) is strictly decreasing, \(Y_s(t)>0\) for \(t<t_s\). By continuity, for \(t<t_s\) sufficiently close to \(t_s\),
\[
\operatorname{Re}
\frac{e^{it}F_s'(e^{it})}{F_s(e^{it})}
<
0.
\]

If
\[
s>\frac12,
\]
then
\[
\operatorname{Im}W_s(t_s)>0,
\]
while \(Y_s(t)<0\) for \(t>t_s\). Thus for \(t>t_s\) sufficiently close to \(t_s\), the same strict negativity holds.

The relevant boundary arcs avoid the logarithmic singularities at \(1\) and \(-i\), so \(F_s\) and its derivative extend analytically across them. Radial continuity therefore moves each negative boundary value to nearby points inside the unit disk. Hence
\[
F_s\notin\mathcal S^*
\]
for every
\[
0<s<1,
\qquad
s\ne\frac12.
\]

## Verification

The primary paper was inspected in full around its Section 4 family. It defines the same functions
\[
R,
\quad
R_{\pi/2},
\quad
F_s,
\]
and proves
\[
F_s\in\mathcal R\setminus\mathcal S^*
\]
only for
\[
0<s<
\frac{\log2}{\pi+\log2}.
\]
Its proof detects negativity through an asymptotic calculation as \(z\to1\).

The present proof uses a different mechanism. It finds the unique zero of \(F_s'\) on the first-quadrant boundary arc and proves that the boundary starlikeness quantity must change sign there whenever the two Herglotz weights are unequal.

The packaged symbolic checker verifies the derivative identities, the root relation, and the exact factorization
\[
sqD_2-(1-s)cD_1
=
\frac12(q-c)(1+c+q)(1-r)^2
\]
under
\[
c^2+q^2=1
\]
and the root condition. The sign argument itself is analytic and does not depend on finite sampling.

## Relationship to prior work

Hoshinaga, Hotta and Wang introduced this particularly simple two-rotation family in 2026 to illustrate that the Noshiro–Warschawski class is not contained in the starlike class. Their theorem proves nonstarlikeness on the small interval
\[
0<s<
\frac{\log2}{\pi+\log2}
=
0.18075\ldots .
\]
The finding above expands that conclusion to every imbalanced parameter
\[
s\in(0,1)\setminus\left\{\frac12\right\}.
\]

Classical examples of Krzyż and later authors already show that positive real derivative does not imply starlikeness, but they use different functions and do not imply the parameter classification of this new orthogonal two-atom family.

Recent work on sector restrictions for the derivative asks how much narrower than a half-plane the derivative image must be in order to force starlikeness. That is a class-wide sufficient-condition problem and does not determine the behavior of this explicit family.

Targeted searches using the source identifier, the exact family, the orthogonal Herglotz description, and parameter-threshold formulations did not locate a published statement covering all unequal weights.

## Limitations

The midpoint
\[
s=\frac12
\]
is not decided here.

The proof uses the right-angle separation of the two Herglotz atoms. It does not assert the same all-imbalanced conclusion for arbitrary pairs of rotations.

The result concerns starlikeness with respect to the origin and does not quantify other geometric properties of the image domains.

## References

1. S. Hoshinaga, I. Hotta and L.-M. Wang, *Boundary geometry and linear accessibility of functions with positive real derivative*, arXiv:2609.20988v1, 2026.
2. J. G. Krzyż, classical counterexample showing that positive real derivative need not imply starlikeness, as cited and discussed in the primary source.
3. M. Nunokawa, K. Piejko and J. Sokół, *On a sector for derivative which implies the starlikeness*, Canadian Mathematical Bulletin, 2026. DOI: 10.4153/S0008439526101702.
