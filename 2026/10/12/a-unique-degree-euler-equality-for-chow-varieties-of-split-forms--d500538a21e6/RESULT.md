# A unique degree–Euler equality for Chow varieties of split forms
## Finding
Let
\[
\operatorname{Split}_d(\mathbb P^n)
\subset
\mathbb P(\operatorname{Sym}^d\mathbb C^{n+1})
\]
be the Chow variety of completely decomposable degree-\(d\) forms, with
\[
n,d\ge1.
\]
Equivalently, it parametrizes hypersurfaces that are unions of \(d\) hyperplanes.

Then
\[
\boxed{
\deg\operatorname{Split}_d(\mathbb P^n)
=
\frac{(nd)!}{d!(n!)^d}
}
\]
and
\[
\boxed{
\chi_{\mathrm{top}}\!\left(\operatorname{Split}_d(\mathbb P^n)\right)
=
\binom{n+d}{d}.
}
\]

Write
\[
R(n,d)
=
\frac{
\deg\operatorname{Split}_d(\mathbb P^n)
}{
\chi_{\mathrm{top}}(\operatorname{Split}_d(\mathbb P^n))
}.
\]
For
\[
n,d\ge2,
\]
this ratio is strictly increasing in each parameter.

Consequently,
\[
\boxed{
\deg\operatorname{Split}_d(\mathbb P^n)
<
\chi_{\mathrm{top}}(\operatorname{Split}_d(\mathbb P^n))
}
\]
exactly when
\[
n=1,
\qquad\text{or}\qquad
d=1,
\qquad\text{or}\qquad
(n,d)=(2,2).
\]

Equality occurs exactly once outside the trivial boundary:
\[
\boxed{
\deg\operatorname{Split}_2(\mathbb P^3)
=
\chi_{\mathrm{top}}(\operatorname{Split}_2(\mathbb P^3))
=
10.
}
\]

In every remaining case,
\[
\boxed{
\deg\operatorname{Split}_d(\mathbb P^n)
>
\chi_{\mathrm{top}}(\operatorname{Split}_d(\mathbb P^n)).
}
\]

Thus the Chow variety of reducible quadrics in
\[
\mathbb P^3,
\]
viewed inside
\[
\mathbb P(\operatorname{Sym}^2\mathbb C^4)=\mathbb P^9,
\]
is the unique nontrivial split-form Chow variety where the projective intersection count equals the topological cell-count invariant.

## Assumptions and scope
The base field is \(\mathbb C\). The projective degree is taken in the natural embedding by coefficients of degree-\(d\) forms.

The notation
\[
\operatorname{Split}_d(\mathbb P^n)
\]
follows the literature on completely decomposable forms. It is also the Chow variety of effective zero-cycles of degree \(d\) on the dual projective space, realized by multiplying the corresponding linear forms.

The cases \(n=1\) or \(d=1\) are included in the classification but are geometrically degenerate for the comparison: the split variety is itself a projective space and has degree \(1\).

## Proof
Arrondo and Bernardi identify
\[
\operatorname{Split}_d(\mathbb P^n)
\]
as the image of the finite map
\[
\phi:(\mathbb P^n)^d
\longrightarrow
\mathbb P(\operatorname{Sym}^d\mathbb C^{n+1}),
\qquad
([L_1],\ldots,[L_d])
\longmapsto
[L_1\cdots L_d],
\]
and state that this map has degree
\[
d!.
\]
The pullback of the ambient hyperplane class is
\[
H_1+\cdots+H_d.
\]
Since the source has dimension
\[
nd,
\]
the projection formula gives
\[
d!\,
\deg\operatorname{Split}_d(\mathbb P^n)
=
\int_{(\mathbb P^n)^d}
(H_1+\cdots+H_d)^{nd}.
\]
Only the monomial
\[
H_1^n\cdots H_d^n
\]
survives. Its coefficient is
\[
\frac{(nd)!}{(n!)^d},
\]
so
\[
\deg\operatorname{Split}_d(\mathbb P^n)
=
\frac{(nd)!}{d!(n!)^d}.
\]

The multiplication map is invariant under the symmetric group \(S_d\), hence factors through
\[
\operatorname{Sym}^d(\mathbb P^n).
\]
Unique factorization of homogeneous polynomials into linear factors makes the induced finite map
\[
\operatorname{Sym}^d(\mathbb P^n)
\longrightarrow
\operatorname{Split}_d(\mathbb P^n)
\]
bijective on complex points. Because it is a continuous bijection from a compact complex space to a Hausdorff space, it is a homeomorphism on the associated analytic spaces.

The Macdonald symmetric-power identity therefore gives
\[
\sum_{d\ge0}
\chi_{\mathrm{top}}\!\left(\operatorname{Split}_d(\mathbb P^n)\right)t^d
=
(1-t)^{-\chi_{\mathrm{top}}(\mathbb P^n)}
=
(1-t)^{-(n+1)}.
\]
Extracting the coefficient of \(t^d\) yields
\[
\chi_{\mathrm{top}}\!\left(\operatorname{Split}_d(\mathbb P^n)\right)
=
\binom{n+d}{d}.
\]

Now set
\[
R(n,d)
=
\frac{(nd)!}{d!(n!)^d}
\bigg/
\binom{n+d}{d}.
\]
For
\[
n,d\ge2,
\]
incrementing \(d\) gives
\[
\frac{R(n,d+1)}{R(n,d)}
=
\frac{
\prod_{j=1}^{n}(nd+j)
}{
n!(n+d+1)
}.
\]
Rewrite this as
\[
\frac{nd+1}{n+d+1}
\prod_{j=2}^{n}\frac{nd+j}{j}.
\]
The first factor is at least \(1\), with equality only at
\[
(n,d)=(2,2),
\]
and every factor in the remaining product is strictly greater than \(1\). Hence
\[
R(n,d+1)>R(n,d).
\]

Similarly,
\[
\frac{R(n+1,d)}{R(n,d)}
=
\frac{
\prod_{j=1}^{d}(nd+j)
}{
(n+1)^{d-1}(n+d+1)
}
=
\frac{nd+1}{n+d+1}
\prod_{j=2}^{d}\frac{nd+j}{n+1},
\]
and this is again strictly greater than \(1\) for
\[
n,d\ge2.
\]

The base values are
\[
R(2,2)=\frac12,
\qquad
R(3,2)=1,
\qquad
R(2,3)=\frac32.
\]
Strict coordinate growth now proves the entire interior classification.

On the boundary,
\[
\deg\operatorname{Split}_d(\mathbb P^1)=1,
\qquad
\chi_{\mathrm{top}}\!\left(\operatorname{Split}_d(\mathbb P^1)\right)=d+1,
\]
and
\[
\deg\operatorname{Split}_1(\mathbb P^n)=1,
\qquad
\chi_{\mathrm{top}}\!\left(\operatorname{Split}_1(\mathbb P^n)\right)=n+1.
\]
This completes the proof.

## Verification
The bundled checker independently evaluates both closed formulas for every
\[
1\le n,d\le60.
\]
It verifies the complete below/equal/above classification and checks both exact coordinate-growth identities by rational arithmetic.

It also reconstructs the degree numerator as the top multinomial coefficient of
\[
(H_1+\cdots+H_d)^{nd}
\]
and divides by the generic degree
\[
d!
\]
of the multiplication map.

These finite computations are regression evidence only. The infinite theorem follows from the finite-map degree calculation, the Macdonald symmetric-power formula, and the two exact ratio identities.

## Relationship to prior work
Arrondo and Bernardi introduce the split variety in the form used here and explicitly record the finite degree-\(d!\) multiplication map from a product of projective spaces. Later work on Chow rank and secant varieties treats the same Chow variety as a central projective model for products of linear forms.

The symmetric-product Euler formula is classical and follows from the Macdonald identity. Combining these ingredients gives explicit closed formulas for both invariants.

The new point is the sharp global comparison: throughout the two-parameter family, the quotient of degree by Euler characteristic is strictly coordinate-increasing away from the boundary, producing a unique nontrivial equality at
\[
\operatorname{Split}_2(\mathbb P^3).
\]
Targeted searches using split variety, Chow variety, completely decomposable forms, symmetric products, degree, Euler characteristic, and the exact factorial/binomial formulas did not locate this crossover theorem.

## Limitations
The theorem compares only the natural projective degree and ordinary topological Euler characteristic. It does not determine singular cohomology groups, intersection cohomology, or degrees of secant and dual varieties.

The split variety is generally singular, and the homeomorphism with the symmetric product is topological rather than an assertion that the induced finite birational morphism is an isomorphism of schemes.

The ingredients are classical and the comparison is elementary once the two closed formulas are juxtaposed. An older or unindexed source may contain the same factorial-versus-binomial observation.

## References
Enrique Arrondo and Alessandra Bernardi, *On the variety parametrizing completely decomposable polynomials*, arXiv:0903.2757, first submitted 16 March 2009; *Journal of Pure and Applied Algebra* 215 (2011), 201--220, DOI 10.1016/j.jpaa.2010.04.008.

Sabir M. Gusein-Zade, Ignacio Luengo, and Alejandro Melle-Hernández, *Power structure over the Grothendieck ring of varieties and generating series of Hilbert schemes of points*, arXiv:math/0407204, first submitted 12 July 2004.

Douglas A. Torrance, *Generic forms of low Chow rank*, arXiv:1508.05546, first submitted 25 August 2015; *Journal of Algebra and Its Applications* 16 (2017), 1750047.
