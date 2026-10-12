# Euler characteristic of every secant variety of a smooth rational normal scroll
## Finding
Let
\[
k\ge2,
\qquad
d_1,\ldots,d_k\ge1,
\]
and let
\[
S(d_1,\ldots,d_k)
=
\mathbb P\!\left(
\bigoplus_{i=1}^{k}\mathcal O_{\mathbb P^1}(d_i)
\right)
\]
be the smooth rational normal scroll in its tautological embedding
\[
S(d_1,\ldots,d_k)
\subset
\mathbb P^{\,\sum_i(d_i+1)-1}.
\]

For every
\[
r\ge1,
\]
let
\[
\sigma_r(S)
\]
be the projective secant variety of border rank at most \(r\).

Then
\[
\boxed{
\chi_{\mathrm{top}}(\sigma_r(S))
=
\sum_{i=1}^{k}\min\{d_i+1,2r\}.
}
\]

More precisely, use coordinates
\[
x_{i,j},
\qquad
1\le i\le k,
\qquad
0\le j\le d_i,
\]
where the \(i\)-th coordinate block is the degree-\(d_i\) binary-form space. The coordinate point
\[
[x_{i,j}]
\]
lies in \(\sigma_r(S)\) exactly when
\[
\boxed{
\min\{j,d_i-j\}+1\le r.
}
\]

Thus the \(i\)-th directrix contributes
\[
\min\{d_i+1,2r\}
\]
fixed points. At every secant step it contributes two new coordinate points, one from each end of its binary-monomial string, until that block is exhausted.

In particular,
\[
\chi_{\mathrm{top}}(S)=2k,
\]
and once
\[
2r\ge \max_i(d_i+1),
\]
the Euler characteristic has already reached the ambient value
\[
\sum_i(d_i+1).
\]

## Assumptions and scope
The base field is
\[
\mathbb C.
\]

All
\[
d_i\ge1,
\]
so the scroll is smooth and nondegenerate. The dimension of the scroll is \(k\).

The secant convention is
\[
\sigma_r(S)
=
\overline{
\bigcup_{p_1,\ldots,p_r\in S}
\langle p_1,\ldots,p_r\rangle
}.
\]
Thus \(\sigma_1(S)=S\).

No assumption is made that the secant variety has expected dimension. The formula remains valid for defective secant varieties and after the secant tower fills its ambient projective space.

## Proof
Write
\[
E
=
\bigoplus_{i=1}^{k}\mathcal O_{\mathbb P^1}(d_i).
\]
The tautological embedding has ambient vector space
\[
W
=
\bigoplus_{i=1}^{k}\operatorname{Sym}^{d_i}\mathbb C^2.
\]

The natural torus scales the summands of \(E\) and acts diagonally on the base \(\mathbb P^1\). Choose a one-parameter subgroup for which all coordinate weights
\[
x_{i,j}
\]
are pairwise distinct. For example, if
\[
D=\max_i d_i,
\]
one may use block offsets separated by more than \(D\), together with the base weight \(j\).

Hence the fixed locus of the ambient projective space consists exactly of the coordinate points
\[
[x_{i,j}].
\]
Every secant variety
\[
\sigma_r(S)
\]
is invariant under this action.

We determine which coordinate points lie in a given secant variety.

Fix a block \(i\). Projection to the \(i\)-th summand
\[
W\longrightarrow \operatorname{Sym}^{d_i}\mathbb C^2
\]
sends the affine cone over the scroll to the affine cone over the degree-\(d_i\) rational normal curve, together with the origin. Therefore a coordinate vector
\[
x_{i,j}
\]
has the same border rank with respect to the scroll as the binary monomial
\[
s^{d_i-j}t^j
\]
has with respect to the rational normal curve.

Indeed, any border decomposition by \(r\) scroll points projects to a border decomposition by at most \(r\) pure degree-\(d_i\) powers, giving one inequality. Conversely, the \(i\)-th directrix rational normal curve is contained in the scroll, giving the reverse inequality.

It remains to compute the symmetric border rank of a binary monomial. Put
\[
d=d_i,
\qquad
q=\min\{j,d-j\}.
\]
The \(q\)-th catalecticant of
\[
s^{d-j}t^j
\]
has rank exactly
\[
q+1.
\]
If, for example,
\[
j\le d-j,
\]
then the derivatives
\[
\partial_s^{\,j-a}\partial_t^{\,a}
\left(s^{d-j}t^j\right),
\qquad
0\le a\le j,
\]
are \(j+1\) nonzero distinct monomials. Since catalecticant rank is at most border rank,
\[
\operatorname{brank}\!\left(s^{d-j}t^j\right)\ge q+1.
\]

For the reverse inequality, again suppose
\[
q=j\le d-j.
\]
The finite-difference identity gives
\[
\varepsilon^{-j}
\sum_{h=0}^{j}
(-1)^{j-h}\binom{j}{h}
(s+h\varepsilon t)^d
\longrightarrow
j!\binom dj\,s^{d-j}t^j
\]
as
\[
\varepsilon\longrightarrow0.
\]
For every nonzero \(\varepsilon\), the left side is a sum of \(j+1\) pure powers. Thus the border rank is at most \(j+1\). When
\[
d-j<j,
\]
interchange \(s\) and \(t\).

Consequently
\[
\operatorname{brank}_S(x_{i,j})
=
\min\{j,d_i-j\}+1.
\]

The fixed points in block \(i\) belonging to
\[
\sigma_r(S)
\]
are therefore those with
\[
j\le r-1
\quad\text{or}\quad
d_i-j\le r-1.
\]
Their number is
\[
\min\{d_i+1,2r\}.
\]

Hence
\[
\left(\sigma_r(S)\right)^{\mathbb C^*}
\]
is a finite set of
\[
\sum_{i=1}^{k}\min\{d_i+1,2r\}
\]
points.

For any complex algebraic variety \(Y\) with an algebraic
\[
\mathbb C^*
\]
action,
\[
\chi_c(Y)=\chi_c(Y^{\mathbb C^*}).
\]
Since \(\sigma_r(S)\) is projective,
\[
\chi_{\mathrm{top}}(\sigma_r(S))
=
\chi_c(\sigma_r(S))
=
\chi_c\!\left((\sigma_r(S))^{\mathbb C^*}\right),
\]
which is the stated fixed-point count.

## Verification
The bundled checker tests all scroll types with
\[
2\le k\le5,
\qquad
1\le d_i\le9,
\]
on a deterministic finite sample.

For every degree
\[
1\le d\le18
\]
and every monomial
\[
s^{d-j}t^j,
\]
it computes the relevant catalecticant rank by exact rational Gaussian elimination and verifies
\[
\operatorname{rank}= \min\{j,d-j\}+1.
\]

It also verifies the finite-difference cancellation identities
\[
\sum_{h=0}^{q}(-1)^{q-h}\binom qh h^a=0
\quad
(0\le a<q)
\]
and
\[
\sum_{h=0}^{q}(-1)^{q-h}\binom qh h^q=q!
\]
through
\[
q=12.
\]

Finally, it checks the fixed-coordinate count against
\[
\sum_i\min\{d_i+1,2r\}
\]
for every tested scroll and secant level.

These finite computations are regression evidence only. The theorem for all parameters is the symbolic projection, catalecticant, finite-difference, and torus-localization argument above.

## Relationship to prior work
Catalano-Johnson studies higher secant varieties of rational normal scrolls, gives their higher secant ideals by determinantal methods, and determines their possible dimensions. This supplies an archival algebraic-geometric setting for the full secant tower.

De Poi likewise studies higher secant varieties of rational normal scrolls and determinantal descriptions of their defects.

Lin and Shen study blow-up algebras of secant varieties of balanced rational normal scrolls. Their full text treats defining equations, Rees algebras, fiber cones, Cohen--Macaulayness, rational singularities, Gorensteinness, regularity, and reduction numbers.

The inspected literature does not state the ordinary Euler characteristic of the secant varieties or the directrix-by-directrix formula above. Targeted searches for Euler, Poincaré, torus-fixed, and binary-monomial formulations did not locate an equivalent theorem.

The rational-normal-curve special case is consistent with the same binary-monomial border-rank mechanism, but the result here treats every higher-dimensional smooth rational normal scroll and shows that the contributions of its directrices add independently.

## Limitations
Euler characteristic is a coarse invariant. The formula does not determine secant dimensions, defectivity, degree, singularities, equations, or individual Betti numbers.

The theorem concerns the standard tautological embedding of a smooth rational normal scroll with positive splitting degrees. Conical scrolls with zero splitting degrees require separate treatment because the fixed-point geometry changes.

The proof reduces fixed-point membership to binary monomial border rank, so an older unindexed or folklore formulation may exist even though it was not located in the inspected secant-scroll literature.

## References
Michael L. Catalano-Johnson, *The Possible Dimensions of the Higher Secant Varieties*, *American Journal of Mathematics* 118 (1996), 355--361, DOI 10.1353/AJM.1996.0012.

Pietro De Poi, *On higher secant varieties of rational normal scrolls*, *Le Matematiche* 51 (1996), 3--21.

Kuei-Nuan Lin and Yi-Huang Shen, *Blow-up algebras of secant varieties of rational normal scrolls*, arXiv:2107.04168, first submitted 9 July 2021; *Collectanea Mathematica* 74 (2023), 247--278, DOI 10.1007/s13348-021-00345-2.
