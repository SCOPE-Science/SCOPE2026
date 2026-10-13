# Euler characteristic of the third Veronese secant has three degree regimes
## Finding
Let
\[
n\ge2,\qquad d\ge3,
\]
and let
\[
S^{(3)}_{n,d}
=
\sigma_3\!\left(v_d(\mathbb P^n_{\mathbb C})\right)
\subset
\mathbb P\!\left(\operatorname{Sym}^d\mathbb C^{n+1}\right)
\]
be the projective variety of symmetric tensors of border rank at most three.

Then
\[
\boxed{
\chi_{\mathrm{top}}\!\left(S^{(3)}_{n,3}\right)
=
(n+1)^2,
}
\]
\[
\boxed{
\chi_{\mathrm{top}}\!\left(S^{(3)}_{n,4}\right)
=
(n+1)^2+\binom{n+1}{2}
=
\frac{(n+1)(3n+2)}2,
}
\]
and, for every
\[
d\ge5,
\]
\[
\boxed{
\chi_{\mathrm{top}}\!\left(S^{(3)}_{n,d}\right)
=
(n+1)(2n+1).
}
\]

If
\[
E^{(3)}_{n,d}
=
S^{(3)}_{n,d}
\setminus
\sigma_2\!\left(v_d(\mathbb P^n)\right)
\]
is the locally closed exact border-rank-three layer, then
\[
\boxed{
\chi_c(E^{(3)}_{n,3})=0,
\qquad
\chi_c(E^{(3)}_{n,4})=\binom{n+1}{2},
\qquad
\chi_c(E^{(3)}_{n,d})=n(n+1)\quad(d\ge5).
}
\]

Thus the third secant has three distinct degree regimes: cubic degree contributes no new Euler mass beyond the second secant, quartic degree contributes one fixed point for every unordered variable pair, and degrees at least five contribute one fixed point for every ordered variable pair.

## Assumptions and scope
The base field is
\[
\mathbb C.
\]
The theorem concerns
\[
n\ge2,\qquad d\ge3.
\]
The secant convention is that
\[
\sigma_r(v_d(\mathbb P^n))
\]
is the Zariski closure of spans of \(r\) Veronese points, equivalently the projective symmetric-border-rank-\(\le r\) locus.

No smoothness or expected-dimension assumption is used. The varieties involved may be singular.

The exact-layer statements use compactly supported Euler characteristic, which is additive for a closed subvariety and its open complement.

## Proof
Write
\[
m=n+1
\]
and choose coordinates
\[
x_0,\ldots,x_n.
\]
Let a one-parameter subgroup act diagonally on the variables with weights
\[
1,B,B^2,\ldots,B^n,
\qquad
B>d.
\]
Every degree-\(d\) monomial
\[
x^\alpha=x_0^{\alpha_0}\cdots x_n^{\alpha_n},
\qquad
|\alpha|=d,
\]
then has weight
\[
\sum_i\alpha_iB^i.
\]
Because
\[
0\le\alpha_i\le d<B,
\]
base-\(B\) uniqueness makes these monomial weights pairwise distinct. Hence the fixed points of the ambient projective symmetric power are exactly its monomial coordinate points. The Veronese secants are invariant under this action, so their fixed loci are obtained by deciding which monomials have border rank at most the required threshold.

We first classify the fixed monomials of border rank at most three.

A monomial supported on one variable is a pure \(d\)-th power and has border rank one.

Now suppose the support has exactly two variables. After relabeling, write it as
\[
x^ay^b,
\qquad
a+b=d,
\qquad
a\ge b\ge1.
\]
Its degree-\(b\) catalecticant has image spanned by
\[
x^b,x^{b-1}y,\ldots,y^b,
\]
so its rank is
\[
b+1.
\]
Since every catalecticant rank is a lower bound for symmetric border rank,
\[
\underline{\operatorname{rank}}(x^ay^b)\ge b+1.
\]
For
\[
b=1,
\]
the limit
\[
\lim_{t\to0}
\frac{(x+ty)^d-x^d}{dt}
=
x^{d-1}y
\]
shows border rank at most two. For
\[
b=2,
\]
the limit
\[
\lim_{t\to0}
\frac{(x+ty)^d+(x-ty)^d-2x^d}{d(d-1)t^2}
=
x^{d-2}y^2
\]
shows border rank at most three. Thus a two-variable monomial has border rank at most three exactly when its smaller exponent is at most two.

Suppose next that a degree-\(d\) monomial has at least four variables in its support. Its first catalecticant has rank equal to the support size, hence at least four. Such a monomial cannot have border rank at most three.

Suppose the support has exactly three variables and
\[
d\ge4.
\]
At least one exponent is at least two. The quadratic catalecticant then has at least four distinct monomials in its image: the square of that variable, its products with each of the other two support variables, and the product of those other two variables. Hence this catalecticant has rank at least four, so again the monomial is outside the third secant.

It remains to treat
\[
d=3
\]
with three-variable support. Up to relabeling the only monomial is
\[
x_0x_1x_2.
\]
For a ternary cubic written in Han's normalization, the Aronhold quartic defining
\[
\sigma_3(v_3(\mathbb P^2))
\]
contains the term
\[
\phi_{012}^4
\]
and every other term vanishes when only the coefficient of
\[
x_0x_1x_2
\]
is nonzero. Therefore the Aronhold invariant is nonzero at this monomial. By the inherited Aronhold equations in higher ambient dimension, no three-support cubic monomial belongs to
\[
\sigma_3(v_3(\mathbb P^n)).
\]

We can now count the fixed points.

For
\[
d=3,
\]
only pure powers and monomials of type
\[
x_i^2x_j
\qquad(i\ne j)
\]
occur. Their number is
\[
m+m(m-1)=m^2.
\]

For
\[
d=4,
\]
we additionally have monomials
\[
x_i^2x_j^2,
\]
indexed by unordered pairs. Thus the count is
\[
m^2+\binom m2.
\]

For
\[
d\ge5,
\]
the new monomials are
\[
x_i^{d-2}x_j^2
\qquad(i\ne j),
\]
and the two exponents are unequal, so they are indexed by ordered pairs. Thus the count is
\[
m^2+m(m-1)=m(2m-1).
\]

For a complex projective algebraic variety with an algebraic
\[
\mathbb C^*
\]
action, ordinary Euler characteristic equals the Euler characteristic of the fixed locus. Applying this to the finite fixed loci above yields the three formulas.

Finally, the same argument at border rank at most two gives, for every
\[
d\ge3,
\]
only pure powers and monomials
\[
x_i^{d-1}x_j
\qquad(i\ne j),
\]
hence
\[
\chi_{\mathrm{top}}\!\left(\sigma_2(v_d(\mathbb P^n))\right)=m^2.
\]
Subtracting this closed subvariety from the third secant gives the compactly supported Euler characteristics of the exact border-rank-three layers.

## Verification
The bundled checker enumerates every degree-\(d\) monomial for
\[
2\le n\le8,
\qquad
3\le d\le12.
\]
It classifies each monomial by support and exponent pattern and independently computes the relevant catalecticant ranks as counts of divisors of the prescribed degree.

For every case it verifies the fixed-point counts
\[
(n+1)^2,
\qquad
(n+1)^2+\binom{n+1}{2},
\qquad
(n+1)(2n+1)
\]
in the three degree regimes, together with the exact-layer differences.

It also verifies separation of all degree-\(d\) monomial weights for the base choice
\[
B=d+1
\]
over the same grid.

These finite computations are regression evidence only. The theorem for arbitrary
\[
n\ge2,\qquad d\ge3
\]
is proved by the symbolic catalecticant, Aronhold, and fixed-point arguments above.

## Relationship to prior work
Landsberg and Ottaviani study equations for secant varieties of Veronese varieties and establish the catalecticant framework used to detect low symmetric border rank. Their archival paper lists algebraic geometry classification \(14M12\) and develops defining equations, degree questions, and flattening methods, but the inspected full text does not give the Euler-characteristic formulas above.

Buczyński and Landsberg determine normal forms for tensors of border rank at most three in the general secant setting. Their full text contains no Euler- or Poincaré-type calculation.

Han studies exactly the third secant varieties
\[
\sigma_3(v_d(\mathbb P^n)),
\]
identifies them with symmetric tensors of border rank at most three, records the relevant catalecticants for
\[
d\ge4,
\]
and writes an explicit Aronhold equation for the cubic case. The inspected full text contains no occurrence of “Euler” or “Poincaré”.

Targeted semantic-index and web searches combining “third secant”, “Veronese”, “border rank three”, “Euler characteristic”, “Poincaré”, “topology”, “torus fixed points”, and the notation
\[
\sigma_3(v_d(\mathbb P^n))
\]
did not locate an equivalent formula.

The border-rank-two Euler formula is prior coverage and is used only as the baseline for the exact third layer. The new claim is the complete third-secant fixed-monomial classification and the resulting cubic/quartic/stable degree trichotomy.

## Limitations
The theorem computes ordinary Euler characteristic and compactly supported Euler characteristic only. It does not determine Betti numbers, Hodge numbers, motives, intersection cohomology, singularity types, or projective degrees.

No claim is made here for fourth or higher secant varieties.

The localization proof reduces the global invariant to a short monomial classification. An equivalent computation under different terminology or in unindexed literature remains a residual originality risk.

## References
J. M. Landsberg and G. Ottaviani, *Equations for secant varieties of Veronese and other varieties*, arXiv:1111.4567, first submitted 19 November 2011.

J. Buczyński and J. M. Landsberg, *On the third secant variety*, arXiv:1111.7005, first submitted 29 November 2011; *Journal of Algebraic Combinatorics* 40 (2014), 475--502.

K. Han, *On singularities of third secant varieties of Veronese embeddings*, arXiv:1411.5063, first submitted 18 November 2014; *Linear Algebra and its Applications* 544 (2018), 391--406.
