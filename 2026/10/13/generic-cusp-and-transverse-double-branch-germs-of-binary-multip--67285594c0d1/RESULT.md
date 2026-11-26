# Transverse two-branch germs and depth on binary multiple-root loci

## Finding

Let \(m\ge 3\) and \(d\ge 2m\), and let \(\Delta_{m,d}\subset \mathbb P(\operatorname{Sym}^d\mathbb C^2)\) be the reduced locus of binary forms having a root of multiplicity at least \(m\). Let \(S\) be the stratum of forms with exactly two distinct roots of multiplicity \(m\) and \(d-2m\) other, all simple, roots. Put \(q=d-2m+2\) and \(c=m-1\).

At every closed point \(s\in S\), the completed local ring of \(\Delta_{m,d}\) is
\[
\mathbb C[[u_1,\ldots,u_q,a_1,\ldots,a_c,b_1,\ldots,b_c]]/
(a_i b_j : 1\le i,j\le c).
\]
The stratum is the transverse intersection of the two smooth local branches. The Hilbert–Samuel multiplicity is \(2\), the local dimension is \(d-m+1\), and the depth is \(d-2m+3\). In particular the depth defect is \(m-2\) at every closed point of \(S\). At the generic point of \(\overline S\) the local ring has dimension \(m-1\) and depth \(1\); hence \(\Delta_{m,d}\) fails Serre's \(S_2\) condition.

## Proof

Move the roots away from infinity and work in the monic coefficient chart. Near the chosen form \(Q_1 Q_2 H\), use a product of coefficient spaces with two monic degree-\(m\) factors \(Q_1,Q_2\) and a monic degree-\(d-2m\) factor \(H\). These factors are pairwise coprime at the chosen point, and \(H\) is squarefree. Restrict to that open condition. The product map to the monic degree-\(d\) space is étale there: its derivative is
\[
(\dot Q_1,\dot Q_2,\dot H)\longmapsto \dot Q_1 Q_2 H+Q_1\dot Q_2 H+Q_1Q_2\dot H,
\]
and reducing modulo each of the three coprime factors gives injectivity, since the variations have degrees strictly smaller than those of their factors. Domain and codomain have dimension \(d\). If \(d=2m\), omit \(H\) (it is the constant \(1\)). At a complex closed point the étale map induces an isomorphism on completed local rings.

In the product chart a root of multiplicity at least \(m\) occurs just when one of \(Q_1\) and \(Q_2\) is a pure \(m\)-th power. Indeed distinct factors share no roots, and the residual factor has only simple roots. In each degree-\(m\) coefficient space the pure-power curve is smooth and can be straightened by polynomial coordinates: for \((z-t)^m\) the coefficient of \(z^{m-1}\) is \(-mt\), and subtracting the corresponding pure-power values from the other coefficients leaves \(c\) normal coordinates. Write \(a_i\) for these coordinates in the first block and \(b_j\) in the second. The two curve coordinates together with the coefficients of \(H\) give \(q\) coordinates \(u\) (center them at the point when taking its completion).

The pullback of the reduced locus is reduced under the étale map; set-theoretically it is the union of \(a=0\) and \(b=0\) just described. Thus its ideal is \((a)\cap (b)=(a_i b_j)\). The intersection \(a=b=0\) maps to \(S\) in this chart, with the two blocks distinguished by their order. This proves the ring formula and transversality.

For the displayed complete ring \(R\) there is an exact sequence
\[
0\longrightarrow R\longrightarrow
\mathbb C[[u,a]]\oplus\mathbb C[[u,b]]
\xrightarrow{\,\mathrm{res}_a-\mathrm{res}_b\,}\mathbb C[[u]]\longrightarrow 0,
\]
where the map takes the difference of the two restrictions to the intersection. The two middle summands are regular of dimension \(q+c\), and the last has depth \(q\). The depth lemma gives \(\operatorname{depth}R=q+1\) since \(c\ge 2\). Both branches have dimension \(q+c\) and multiplicity one, so by multiplicity associativity the multiplicity of their union is two. Dimension, depth and multiplicity agree with those of the algebraic local ring by completion.

For the generic-point assertion use the same étale chart before completion. Its ordered intersection \(a=b=0\) is irreducible on the coprime, residual-squarefree open and dominates \(S\). Localize the coordinate union at the generic point of that intersection. The two regular branch local rings have dimension \(c\) and their intersection ring is the function field of the ordered stratum. The same restriction exact sequence now gives depth \(1\). The local map from \(\mathcal O_{\Delta_{m,d},\eta}\), where \(\eta\) is the generic point of \(\overline S\), to this local ring is étale with field fiber, so dimension and depth agree. Since \(c\ge 2\), this violates \(S_2\) at \(\eta\).

## Relationship to prior work

Chipalkatti's Theorem 5.4 gives the set-theoretic singular support for coincident-root loci. Kurmann's Proposition 2.1 identifies the two normalization preimages in this exact partition, and its tangent criterion accounts for the qualitative nodal-type picture. The result here identifies the simultaneous normal-coordinate blocks and reduced union ideal, and obtains the precise closed-point and generic-point depths. Knowing the number of preimages alone does not specify the intersection or its completed local ring.

The ordinary discriminant case \(m=2\) and the germ at a merger to a single \((m+1)\)-fold root are not contributions here. In particular Chipalkatti's Theorem 4.1 and its proof identify the square of the diagonal ideal in the normalization of an unequal two-part coincident-root locus, giving the characteristic-zero cusp in the two-part case; separating the disjoint simple factors gives the corresponding smooth-factor version.

## Scope and verification

The result concerns the reduced complex locus and only the exact stratum \(S\), not deeper collisions or the full singular scheme. It proves local failure of Cohen–Macaulayness on this stratum, not an exhaustive global classification. The étale coordinate and depth arguments above are uniform. Bounded tangent-rank and monomial checks are described in `VERIFICATION.md`; they are not needed for the theorem. Exact overlap with the full 1993 multiplicity-ideal treatment below could not be checked.

## References

1. J. V. Chipalkatti, *On equations defining coincident root loci*, Journal of Algebra 267 (2003), 246–271, §§4–6; [arXiv:math/0110224](https://arxiv.org/abs/math/0110224).
2. S. Kurmann, *Some remarks about equations defining coincident root loci*, Journal of Algebra 352 (2012), 223–231, §2; [arXiv:1108.4532](https://arxiv.org/abs/1108.4532).
3. J. Weyman, *On the Hilbert functions of multiplicity ideals*, Journal of Algebra 161 (1993), 358–369, [DOI:10.1006/jabr.1993.1224](https://doi.org/10.1006/jabr.1993.1224).
