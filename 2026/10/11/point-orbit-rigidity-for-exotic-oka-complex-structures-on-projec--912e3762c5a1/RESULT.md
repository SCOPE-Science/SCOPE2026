# Point-orbit rigidity for exotic Oka complex structures on projective three-space

## Finding

Let \(X_a\) be one of the compact torus-fibred complex threefolds of arXiv:2610.00250v1, and let
\[
p\in X_a.
\]
Write
\[
Y_{a,p}=\operatorname{Bl}_pX_a.
\]

For any two parameters \(a,a'\) and points
\[
p\in X_a,
\qquad
q\in X_{a'},
\]
one has
\[
Y_{a,p}\simeq Y_{a',q}
\]
if and only if there exists a biholomorphism
\[
g:X_a\longrightarrow X_{a'}
\]
such that
\[
g(p)=q.
\]

The recent source proves
\[
X_a\simeq X_{a'}
\quad\Longleftrightarrow\quad
a'-a\in2\mathbb Z.
\]
Consequently, after choosing any biholomorphism
\[
\iota:X_a\longrightarrow X_{a'}
\]
when
\[
a'-a\in2\mathbb Z,
\]
the point-blow-up classification becomes
\[
Y_{a,p}\simeq Y_{a',q}
\quad\Longleftrightarrow\quad
q\in
\operatorname{Aut}(X_{a'})
\cdot
\iota(p).
\]
The condition is independent of the chosen \(\iota\), since two choices differ by an automorphism of \(X_{a'}\).

For fixed \(a\), this gives a bijection
\[
X_a/\operatorname{Aut}(X_a)
\longrightarrow
\left\{
\text{biholomorphism classes of }
\operatorname{Bl}_pX_a
\right\}.
\]

The source also proves that every one-point blow-up is Oka and smoothly diffeomorphic to
\[
\mathbb P^3,
\]
while its first Chern class has divisibility \(2\), rather than the divisibility \(4\) of the standard projective complex structure. Thus every orbit class above gives an exotic Oka complex structure on the smooth manifold \(\mathbb P^3\).

There are uncountably many such classes for every fixed \(a\). The source computes
\[
H^0(X_a,T_{X_a})=\mathbb C V
\]
and
\[
\operatorname{Aut}^0(X_a)\simeq\mathbb C^*.
\]
Hence every automorphism orbit has complex dimension at most \(1\). Since the full automorphism group is a second-countable complex Lie group, it has at most countably many components; a full orbit is therefore a countable union of real two-dimensional immersed submanifolds and has zero six-dimensional measure in \(X_a\). Countably many such orbits cannot cover the compact real six-manifold \(X_a\).

## Assumptions and scope

The family \(X_a\), its parameter half-plane, and its point blow-ups are those of arXiv:2610.00250v1.

The result uses the following source facts:

\[
H^2(X_a,\mathbb Z)=0,
\]
every
\[
\operatorname{Bl}_pX_a
\]
is Oka and diffeomorphic to \(\mathbb P^3\),
\[
c_1(T\operatorname{Bl}_pX_a)
=
-2[E],
\]
the connected automorphism group is
\[
\operatorname{Aut}^0(X_a)\simeq\mathbb C^*,
\]
and
\[
X_a\simeq X_{a'}
\quad\Longleftrightarrow\quad
a'-a\in2\mathbb Z.
\]

No classification of the individual \(\operatorname{Aut}(X_a)\)-orbits is asserted. The theorem identifies the correct moduli quotient and proves that it has uncountably many points.

## Proof

Let
\[
\pi_{a,p}:Y_{a,p}\longrightarrow X_a
\]
be the point blow-down and let
\[
E_{a,p}=\pi_{a,p}^{-1}(p)\simeq\mathbb P^2.
\]

The standard canonical-bundle formula for the blow-up of a complex threefold at a point is
\[
K_{Y_{a,p}}
=
\pi_{a,p}^*K_{X_a}
+
2E_{a,p}.
\]
Because
\[
H^2(X_a,\mathbb Z)=0,
\]
the point blow-up has
\[
H^2(Y_{a,p},\mathbb Z)
=
\mathbb Z[E_{a,p}]
\]
and
\[
c_1(TY_{a,p})
=
-2[E_{a,p}].
\]
This is the Chern-class calculation used in the recent source to distinguish the blow-up from standard \(\mathbb P^3\).

Suppose now that
\[
\Phi:Y_{a,p}\longrightarrow Y_{a',q}
\]
is biholomorphic. Preservation of \(c_1\), together with torsion-freeness of the rank-one second cohomology, gives
\[
\Phi^*[E_{a',q}]
=
[E_{a,p}].
\]
Put
\[
D=\Phi^{-1}(E_{a',q}).
\]
Then \(D\) is an irreducible divisor and
\[
[D]=[E_{a,p}].
\]

We claim that
\[
D=E_{a,p}.
\]
If not, the canonical section defining \(D\) restricts to a nonzero holomorphic section of
\[
\mathcal O(D)|_{E_{a,p}}.
\]
Since
\[
E_{a,p}\simeq\mathbb P^2,
\]
a holomorphic line bundle on \(E_{a,p}\) is determined by its first Chern class. The equality
\[
[D]=[E_{a,p}]
\]
implies
\[
c_1\!\left(\mathcal O(D)|_{E_{a,p}}\right)
=
c_1\!\left(\mathcal O(E_{a,p})|_{E_{a,p}}\right).
\]
The normal bundle of a point-blow-up exceptional divisor is
\[
\mathcal O(E_{a,p})|_{E_{a,p}}
\simeq
\mathcal O_{\mathbb P^2}(-1).
\]
Therefore
\[
\mathcal O(D)|_{E_{a,p}}
\simeq
\mathcal O_{\mathbb P^2}(-1),
\]
but
\[
H^0(\mathbb P^2,\mathcal O(-1))=0,
\]
a contradiction. Thus \(\Phi\) carries the exceptional divisor to the exceptional divisor.

On the complements of the exceptional divisors, define
\[
g
=
\pi_{a',q}
\circ
\Phi
\circ
\pi_{a,p}^{-1}.
\]
This is a biholomorphism
\[
X_a\setminus\{p\}
\longrightarrow
X_{a'}\setminus\{q\}.
\]
Because \(\Phi(E_{a,p})=E_{a',q}\), the map
\[
\pi_{a',q}\circ\Phi
\]
is constant on the unique nontrivial fibre of \(\pi_{a,p}\). Equivalently, the standard analytic blow-down factorization extends \(g\) holomorphically across \(p\), sending
\[
p\longmapsto q.
\]
Applying the same argument to \(\Phi^{-1}\) shows that the extension is biholomorphic.

Conversely, any biholomorphism
\[
g:X_a\longrightarrow X_{a'}
\]
with
\[
g(p)=q
\]
lifts functorially to a biholomorphism of the point blow-ups.

This proves the classification.

For the final cardinality statement, the source gives
\[
\dim_{\mathbb C}\operatorname{Aut}^0(X_a)=1.
\]
Every component of \(\operatorname{Aut}(X_a)\) is therefore one-dimensional, and a second-countable Lie group has at most countably many components. Each full orbit in the complex threefold \(X_a\) is consequently a countable union of real submanifolds of dimension at most \(2\), hence has zero measure for any smooth positive six-dimensional volume form. If there were only countably many orbits, their union would have zero measure, contradicting the positive volume of \(X_a\). Thus there are uncountably many orbit classes and hence uncountably many pairwise non-biholomorphic Oka complex structures on the smooth \(\mathbb P^3\).

## Verification

The recent primary paper was inspected through its finite-point blow-up theorem, the one-point smooth-type and first-Chern calculation, the tangent-cohomology computation, the connected automorphism group, and the exact biholomorphism relation among the base threefolds.

The new rigidity argument uses only the actual point-blow-up geometry. The exceptional divisor has normal bundle
\[
\mathcal O_{\mathbb P^2}(-1),
\]
and the source Chern calculation forces any biholomorphism of two blow-ups to pull the target exceptional cohomology class to the source exceptional class. Restricting the canonical divisor section to the source exceptional plane rules out any distinct irreducible divisor in that class.

The descent step is the standard analytic factorization through the point blow-down. No numerical experiment, finite enumeration, or unproved classification of automorphism orbits is used.

## Relationship to prior work

The 2026 primary source proves that arbitrary finite point blow-ups remain Oka and, for one point, that the resulting manifold is smoothly \(\mathbb P^3\) but not biholomorphic to standard projective space. It also determines the base-family automorphism and biholomorphism data. It does not classify the one-point blow-ups as the centre varies.

The present statement adds that missing rigidity: the blown-up manifold remembers the centre exactly up to a base automorphism. The key new observation is that the first Chern class singles out the exceptional cohomology class, while the negative normal bundle makes the exceptional divisor itself unique in that class.

General blow-up theory supplies the local model, normal bundle, and blow-down factorization, but does not imply the orbit classification until this uniqueness is established for the specific non-Kähler threefolds \(X_a\).

Targeted searches for point-blow-up isomorphism classes, automorphism-orbit classifications, and exotic Oka structures on \(\mathbb P^3\) located the fresh source itself but no statement covering this result.

## Limitations

The theorem classifies one-point blow-ups. For simultaneous blow-ups of several points, an isomorphism can permute exceptional divisors, and a separate configuration-orbit analysis is required.

The result identifies the moduli set with
\[
X_a/\operatorname{Aut}(X_a)
\]
but does not give an explicit geometric parameterization of that quotient.

No assertion is made that the resulting complex structures are pairwise deformation-inequivalent; only biholomorphic inequivalence is proved.

## References

1. Y.-H. Du, B. Guo, Y. Kusakabe, and S.-Y. Xie, *Oka Geometry and Deformations of Torus-Fibred Complex Six-Spheres*, arXiv:2610.00250v1, 2026.
2. H. Grauert, *Über Modifikationen und exzeptionelle analytische Mengen*, Mathematische Annalen 146 (1962), 331–368.
3. F. Lárusson, *Oka-1 manifolds: New examples and properties*, Mathematische Zeitschrift 308 (2024), Article 57.
