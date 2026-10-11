# Measure-theoretic sharpness of almost-everywhere harmonic-slice rigidity

## Finding

Fix
\[
n\ge2.
\]
A recent Forelli-type theorem states that a finite plurisubharmonic function on
\[
\mathbb B^n
\]
is pluriharmonic if its restrictions to complex lines through the origin are harmonic outside a zero-measure set of directions.

That zero-measure threshold is sharp in a strong quantitative sense.

For every
\[
\varepsilon\in(0,1)
\]
there exists a bounded continuous finite plurisubharmonic function
\[
\phi:\mathbb B^n\to\mathbb R
\]
which is not pluriharmonic, although
\[
w\longmapsto\phi(w\xi)
\]
is harmonic on
\[
\mathbb D
\]
for a set of directions
\[
\xi\in S^{2n-1}
\]
of normalized surface measure greater than
\[
1-\varepsilon.
\]

More precisely, for
\[
a>0
\]
define
\[
\phi_a(z)
=
\max\{0,\log|z_1|+a\}.
\]
Then the exceptional set of nonharmonic directions is exactly
\[
E_a
=
\{\xi\in S^{2n-1}:|\xi_1|>e^{-a}\},
\]
and its normalized surface measure is
\[
\sigma(E_a)
=
(1-e^{-2a})^{n-1}.
\]
Consequently
\[
\sigma(E_a)\downarrow0
\qquad
(a\downarrow0),
\]
while every
\[
\phi_a
\]
remains nonpluriharmonic.

## Assumptions and scope

The unit ball is
\[
\mathbb B^n
=
\{z\in\mathbb C^n:|z|<1\},
\]
and
\[
S^{2n-1}=\partial\mathbb B^n.
\]
Surface measure
\[
\sigma
\]
is normalized to have total mass one.

The comparison theorem is Theorem 4.1 of arXiv:2609.32402v1: a finite plurisubharmonic function on
\[
\mathbb B^n
\]
whose slices are harmonic outside a zero-measure set of directions is pluriharmonic.

The present result asserts sharpness only with respect to the measure size of the exceptional direction set. It does not classify which positive-measure sets can occur as exceptional sets.

## Proof

Fix
\[
a>0
\]
and set
\[
\phi_a(z)
=
\max\{0,\log|z_1|+a\}.
\]

The functions
\[
0
\]
and
\[
\log|z_1|+a
\]
are plurisubharmonic, so their pointwise maximum is plurisubharmonic. Moreover,
\[
\phi_a(z)=0
\]
whenever
\[
|z_1|\le e^{-a},
\]
and otherwise
\[
\phi_a(z)=\log|z_1|+a.
\]
Thus
\[
0\le\phi_a\le a
\]
on
\[
\mathbb B^n,
\]
and the two formulas agree on
\[
|z_1|=e^{-a}.
\]
Hence
\[
\phi_a
\]
is finite, bounded, and continuous.

It is not pluriharmonic. Indeed, on the first coordinate line,
\[
\phi_a(we_1)
=
\max\{0,\log|w|+a\}.
\]
This function is constant on
\[
|w|<e^{-a}
\]
and equals
\[
\log|w|+a
\]
on
\[
e^{-a}<|w|<1.
\]
Its radial derivative jumps at
\[
|w|=e^{-a},
\]
so it is not harmonic on
\[
\mathbb D.
\]
A pluriharmonic function would restrict harmonically to every complex line.

Now fix a unit vector
\[
\xi\in S^{2n-1}.
\]
For
\[
w\in\mathbb D,
\]
\[
\phi_a(w\xi)
=
\max\{0,\log|w|+\log|\xi_1|+a\}.
\]

If
\[
|\xi_1|\le e^{-a},
\]
then
\[
\log|w|+\log|\xi_1|+a\le0
\]
for every
\[
|w|<1,
\]
so the slice is identically zero and therefore harmonic.

If
\[
|\xi_1|>e^{-a},
\]
then
\[
r_\xi
=
\frac{e^{-a}}{|\xi_1|}
\]
lies in
\[
(0,1).
\]
The slice is zero on
\[
|w|\le r_\xi
\]
and is
\[
\log|w|+\log|\xi_1|+a
\]
on
\[
r_\xi<|w|<1.
\]
The radial derivative jumps across
\[
|w|=r_\xi,
\]
so the slice is not harmonic.

Therefore the bad-direction set is exactly
\[
E_a
=
\{|\xi_1|>e^{-a}\}.
\]

It remains to compute its measure. For a uniformly distributed point
\[
\xi\in S^{2n-1}\subset\mathbb C^n,
\]
the random variable
\[
X=|\xi_1|^2
\]
has density
\[
(n-1)(1-x)^{n-2}
\]
on
\[
[0,1].
\]
Equivalently,
\[
\sigma\{|\xi_1|>c\}
=
(1-c^2)^{n-1},
\qquad
0\le c\le1.
\]
Taking
\[
c=e^{-a}
\]
gives
\[
\sigma(E_a)
=
(1-e^{-2a})^{n-1}.
\]

Given
\[
\varepsilon\in(0,1),
\]
choose
\[
0<a<
-\frac12
\log\!\left(
1-\varepsilon^{1/(n-1)}
\right).
\]
Then
\[
(1-e^{-2a})^{n-1}<\varepsilon.
\]
Hence the harmonic slices occupy measure greater than
\[
1-\varepsilon,
\]
yet
\[
\phi_a
\]
is not pluriharmonic.

## Verification

The fresh primary source was inspected at its original Forelli-type theorem, at Theorem 4.1, and at the proof of Theorem 4.1. The theorem explicitly assumes that the exceptional set of directions has measure zero, and the proof uses that hypothesis when integrating the slicewise mean-value inequality over the unit sphere.

The counterexample was checked directly.

The plurisubharmonicity is exact: finite maxima of plurisubharmonic functions are plurisubharmonic.

The harmonic and nonharmonic direction sets were determined from the explicit one-variable restriction
\[
\max\{0,\log|w|+\log|\xi_1|+a\}.
\]

The sphere-measure computation is exact. Using the standard complex-sphere Gaussian representation, the squared coordinate moduli have Dirichlet distribution with all parameters equal to one, so
\[
|\xi_1|^2
\]
has beta distribution
\[
\operatorname{Beta}(1,n-1).
\]
Integrating its density gives the displayed exceptional-set measure.

No numerical experiment is used.

## Relationship to prior work

Forelli's classical theorem assumes harmonicity on every complex line through the origin together with smoothness at the origin.

The recent paper replaces the smoothness hypothesis by plurisubharmonicity and proves a stronger almost-everywhere statement: a zero-measure exceptional family of nonharmonic directions is allowed.

The present example determines the measure-theoretic boundary of that improvement. No positive exceptional-measure threshold can replace zero: for every positive tolerance, however small, there is a bounded continuous plurisubharmonic counterexample with fewer bad directions than that tolerance.

Later generalizations of Forelli's theorem study holomorphicity along pencils of discs or integral curves of holomorphic vector fields. Their hypotheses concern the geometry and regularity of the foliation rather than a positive-measure exceptional set of radial directions.

Targeted searches under almost-everywhere harmonic slices, positive-measure exceptional directions, the explicit logarithmic ridge, and the source theorem did not locate this sharpness construction.

## Limitations

The result is measure-theoretic. It does not characterize exceptional direction sets by capacity, category, Hausdorff dimension, or projective geometry.

The construction is nonsmooth across the real hypersurface
\[
|z_1|=e^{-a}.
\]
It is nevertheless bounded, continuous, finite, and plurisubharmonic, exactly matching the regularity allowed by the recent theorem.

The theorem does not claim that every prescribed small positive-measure subset of the sphere can occur as the bad-direction set.

## References

1. W. Xu, *A Characterization of Pluriharmonic Functions via \(p\)-Bergman Kernels and A Forelli-type Result*, arXiv:2609.32402v1, 2026.
2. F. Forelli, *Pluriharmonicity in terms of harmonic slices*, Mathematica Scandinavica 41 (1977), 358--364. DOI: 10.7146/math.scand.a-11728.
3. J.-C. Joo, K.-T. Kim, and G. Schmalz, *A generalization of Forelli's theorem*, Mathematische Annalen 355 (2013), 1171--1176; arXiv:1109.2987.
4. J.-C. Joo, K.-T. Kim, and G. Schmalz, *On the generalization of Forelli's theorem*, Mathematische Annalen 365 (2016), 1187--1200; arXiv:1402.6390.
