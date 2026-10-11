# Higher Hochschild polytopes have an exact permutahedral facet-shell law
## Finding
Let
\[
m\ge2,\qquad n\ge1,\qquad d=m+n,
\]
and let
\[
\mathrm{Hoch}(m,n)\subset\mathbb R^d
\]
be the standard deformed-permutahedron realization of the \((m,n)\)-Hochschild polytope of Pilaud and Poliakova.

The affine hull is
\[
\sum_{i=1}^d x_i=\binom{d+1}{2}.
\tag{1}
\]
For any nonempty proper subset
\[
J\subset[d],
\]
write
\[
A=J\cap[m].
\]
Decompose
\[
J\setminus[m]=B\sqcup C
\]
as in the source, where \(C\) is the largest interval of \(J\setminus[m]\) containing \(d\). Put
\[
u=|A|+|C|,
\qquad
b=|B|,
\qquad
s=|J|=u+b.
\tag{2}
\]
The source's tight subset-sum right-hand side is
\[
z_J=\binom{u+1}{2}+b.
\tag{3}
\]

Let
\[
c=\frac{d+1}{2}\mathbf1.
\tag{4}
\]
Then the intrinsic Euclidean distance from \(c\) to the tight supporting hyperplane
\[
x(J)=z_J
\]
is
\[
\boxed{
\delta_J
=
\frac12\sqrt{d\,s(d-s)}
+
\frac{b(s+u-1)}2
\sqrt{\frac{d}{s(d-s)}}.
}
\tag{5}
\]

The first term in (5) is exactly the corresponding centered facet-shell distance of the classical \(d\)-permutahedron. The second term is a nonnegative Hochschild correction. It vanishes exactly when
\[
b(s+u-1)=0.
\tag{6}
\]

Consequently,
\[
\boxed{
r_{\mathrm{in}}\bigl(\mathrm{Hoch}(m,n)\bigr)
=
\frac12\sqrt{d(d-1)}.
}
\tag{7}
\]
The incenter is unique and is precisely the uniform point \(c\).

Among all tight subset inequalities, equality
\[
\delta_J=r_{\mathrm{in}}
\]
holds exactly in the following cases:
\[
\boxed{
s=1,
\quad\text{or}\quad
s=d-1\text{ and }b=0.
}
\tag{8}
\]
In particular every singleton supporting hyperplane is tangent to the maximal ball, while every tight subset hyperplane with
\[
2\le s\le d-2
\]
is strictly farther away.

## Assumptions and scope
The theorem concerns the standard realization in the cited paper and the Euclidean metric inherited from the standard coordinates of \(\mathbb R^d\).

The parameter range begins at \(m=2\). This isolates the genuinely higher-light Hochschild family and does not restate the one-light specialization.

The formula concerns every tight subset inequality, whether or not that inequality is irredundant in a particular small parameter case. Therefore the inradius conclusion does not require a separate classification of all irredundant facets.

## Proof
The source defines deformed permutahedra by their tight right-hand sides
\[
z_J=\min\{x(J):x\in P\}
\]
for nonempty \(J\subseteq[d]\). Its Hochschild formula gives (3).

At the uniform point \(c\),
\[
x(J)=\frac{d+1}{2}s.
\]
Hence the slack of the tight \(J\)-inequality is
\[
L_J
=
\frac{d+1}{2}s-\binom{u+1}{2}-b.
\tag{9}
\]
Using \(s=u+b\),
\[
\begin{aligned}
2L_J
&=(d+1)(u+b)-u(u+1)-2b\\
&=u(d-u)+b(d-1)\\
&=s(d-s)+b(s+u-1).
\end{aligned}
\tag{10}
\]

Inside the tangent space
\[
\mathbf1^\perp
\]
of (1), the normal \(\mathbf1_J\) projects to
\[
\mathbf1_J-\frac{s}{d}\mathbf1,
\]
whose squared norm is
\[
\frac{s(d-s)}d.
\tag{11}
\]
Dividing (10) by twice the norm in (11) yields exactly (5).

Now
\[
b(s+u-1)\ge0,
\]
so (5) gives
\[
\delta_J
\ge
\frac12\sqrt{d\,s(d-s)}.
\tag{12}
\]
For every
\[
1\le s\le d-1,
\]
\[
s(d-s)\ge d-1,
\tag{13}
\]
with equality exactly for
\[
s=1
\quad\text{or}\quad
s=d-1.
\]
Therefore
\[
\delta_J
\ge
\frac12\sqrt{d(d-1)}.
\tag{14}
\]
This proves that the ball centered at \(c\) with the radius in (7) satisfies every tight subset halfspace, hence lies in the Hochschild polytope.

For the reverse inequality, (3) gives
\[
z_{\{i\}}=1
\]
for every coordinate \(i\). Thus every point of the polytope satisfies
\[
x_i\ge1.
\tag{15}
\]
The intrinsic norm of the singleton normal in the affine hyperplane (1) is
\[
\sqrt{\frac{d-1}{d}}.
\]
If a Euclidean ball of radius \(\rho\), centered at \(q\) in the affine hull, is contained in the polytope, then (15) gives
\[
q_i-1
\ge
\rho\sqrt{\frac{d-1}{d}}
\]
for all \(i\). Summing over \(i\) and using (1),
\[
\binom{d+1}{2}-d
\ge
d\rho\sqrt{\frac{d-1}{d}}.
\]
Hence
\[
\rho
\le
\frac12\sqrt{d(d-1)}.
\tag{16}
\]
This matches the feasible centered ball and proves (7).

If equality holds in (16), every singleton inequality used in the sum must itself be an equality. Therefore all \(q_i\) are equal, and (1) forces
\[
q=c.
\]
Thus the incenter is unique.

Finally, equality in (14) requires equality both in (12) and (13). If \(s=1\), the correction in (5) is always zero. If \(s=d-1\ge2\), the correction vanishes exactly when \(b=0\). This proves (8).

## Verification
The proof is symbolic for all
\[
m\ge2,\qquad n\ge1.
\]

The source-dependent inputs were inspected directly in the arXiv full text: the affine hyperplane, the deformed-permutahedron tight-right-hand-side convention, and the explicit Hochschild formula
\[
z_J=\binom{|A|+|C|+1}{2}+|B|.
\]

The accompanying `verify.py` uses exact rational arithmetic for
\[
2\le m\le7,\qquad 1\le n\le7.
\]
It enumerates every nonempty proper subset, reconstructs \(A,B,C\), verifies (10), verifies the squared form of (5), and checks the complete equality classification (8). The finite computation is corroborative only.

## Relationship to prior work
Pilaud and Poliakova introduce the full \((m,n)\)-Hochschild family as deformed permutahedra obtained by deleting selected multiplihedron inequalities. They give vertex, facet, Minkowski-sum, normal-fan, and tight-right-hand-side descriptions. Their paper does not discuss Euclidean inradii, Chebyshev centers, or normalized facet-distance shells.

The formula (5) is stronger than the radius statement alone. It identifies an exact nonnegative penalty
\[
\frac{b(s+u-1)}2
\sqrt{\frac{d}{s(d-s)}}
\]
measuring how the nonterminal part \(B\) pushes a tight Hochschild hyperplane outward relative to the classical permutahedral shell of the same cardinality.

This explains why the entire higher-light family preserves the permutahedral inradius even though its normal fan and combinatorial structure vary with \(m\) and \(n\).

Targeted searches under “Hochschild polytope”, “inradius”, “Chebyshev center”, “facet distance”, “uniform center”, and “deformed permutahedron” did not locate a theorem implying (5)--(8).

## Limitations
The theorem is realization-specific and is not invariant under arbitrary affine transformations.

It determines the exact tight-subset shell distances and the inball, but not the circumradius, John ellipsoid, or full vertex metric.

The equality classification is stated for all tight subset inequalities. Some tight inequalities can be redundant as facets; no claim is made that every equality hyperplane in (8) is necessarily an irredundant facet for every parameter pair.

A residual originality risk remains for a general deformed-permutahedron metric lemma under different terminology. Search nonappearance is not treated as a formal novelty certificate.

## References
1. Vincent Pilaud and Daria Poliakova, *Hochschild polytopes*, arXiv:2307.05940, first public version 2023-07-12; later published in *Mathematische Annalen*, DOI 10.1007/s00208-025-03120-x.
2. Frédéric Chapoton and Vincent Pilaud, *Shuffles of deformed permutahedra, multiplihedra, constrainahedra, and biassociahedra*, arXiv:2201.06896; *Annales Henri Lebesgue* 7 (2024), 1535--1601.
