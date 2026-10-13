# Euler characteristic of a higher Veronese tangential variety
## Finding
Let \(V\) be a complex vector space of dimension
\[
n\ge2,
\]
let
\[
d\ge3,
\]
and let
\[
X=v_d(\mathbb P(V))
\subset
\mathbb P(\operatorname{Sym}^d V)
\]
be the degree-\(d\) Veronese variety.

Then its tangential variety satisfies
\[
\boxed{
\chi_{\mathrm{top}}\!\left(\tau(X)\right)=n^2.
}
\]

More precisely, after choosing coordinates
\[
x_1,\ldots,x_n
\]
and a generic diagonal one-parameter subgroup with distinct weights on all degree-\(d\) monomials, the fixed locus is exactly
\[
\boxed{
\tau(X)^{\mathbb C^*}
=
\{[x_i^d]:1\le i\le n\}
\sqcup
\{[x_i^{d-1}x_j]:i\ne j\}.
}
\]
It therefore has exactly
\[
n+n(n-1)=n^2
\]
points.

In particular, for fixed \(n\), the ordinary Euler characteristic of the tangential Veronese variety is independent of the embedding degree throughout the entire range \(d\ge3\).

## Assumptions and scope
The base field is \(\mathbb C\).

The tangential variety is the union of the embedded tangent spaces to the Veronese variety. At a point
\[
[\ell^d]\in v_d(\mathbb P(V)),
\]
the affine tangent space is
\[
\ell^{d-1}V.
\]
Consequently
\[
\tau(X)
=
\{[\ell^{d-1}m]:0\ne\ell,m\in V\}.
\]
This set is closed because it is the image of a projective parameter space under the natural morphism.

The restriction \(d\ge3\) is part of the theorem. The quadratic case has a different fixed-point pattern and is not included in the claim.

No smoothness assumption is made on \(\tau(X)\).

## Proof
Choose a basis
\[
x_1,\ldots,x_n
\]
of \(V\), and put
\[
B=d+1.
\]
Let
\[
\lambda:\mathbb C^*\longrightarrow \operatorname{GL}(V)
\]
be the one-parameter subgroup
\[
\lambda(t)\cdot x_i=t^{B^{i-1}}x_i.
\]

For a degree-\(d\) monomial
\[
x^\alpha=x_1^{\alpha_1}\cdots x_n^{\alpha_n},
\qquad
\sum_i\alpha_i=d,
\]
the induced weight is
\[
w(\alpha)=\sum_i\alpha_i B^{i-1}.
\]
Because
\[
0\le\alpha_i\le d<B,
\]
base-\(B\) uniqueness shows that all degree-\(d\) monomials have distinct weights. Hence the fixed locus of the ambient projective space consists precisely of the monomial coordinate points.

The Veronese variety and its tangential variety are invariant under the diagonal torus, so every fixed point of
\[
\tau(X)
\]
is represented by a degree-\(d\) monomial.

We now classify those monomials. Suppose
\[
[x^\alpha]\in\tau(X).
\]
Then
\[
x^\alpha=c\,\ell^{d-1}m
\]
for some nonzero scalar \(c\) and nonzero linear forms \(\ell,m\).

The polynomial ring
\[
\mathbb C[x_1,\ldots,x_n]
\]
is a unique-factorization domain. Since the irreducible linear form \(\ell\) divides the monomial \(x^\alpha\), it is associated to one of the coordinate variables, say
\[
\ell\sim x_i.
\]
Therefore
\[
x_i^{d-1}\mid x^\alpha.
\]
Because \(x^\alpha\) has total degree \(d\), only one degree remains. Thus either
\[
x^\alpha=x_i^d
\]
or
\[
x^\alpha=x_i^{d-1}x_j
\qquad
(j\ne i).
\]

Conversely, each of these monomials has the form
\[
\ell^{d-1}m,
\]
so each lies on the embedded tangent space at
\[
[x_i^d].
\]
This proves the fixed-locus description and gives exactly
\[
n^2
\]
fixed points.

For any complex algebraic variety \(Y\) with an algebraic \(\mathbb C^*\)-action,
\[
\chi_c(Y)=\chi_c(Y^{\mathbb C^*}).
\]
One way to see this is to remove the fixed locus and stratify the remainder into locally trivial pieces with fibers finite quotients of \(\mathbb C^*\), each having compactly supported Euler characteristic zero.

Since
\[
\tau(X)
\]
is projective,
\[
\chi_{\mathrm{top}}(\tau(X))
=
\chi_c(\tau(X))
=
\chi_c(\tau(X)^{\mathbb C^*})
=
n^2.
\]

## Verification
The bundled checker enumerates every degree-\(d\) exponent vector for
\[
2\le n\le8,
\qquad
3\le d\le10.
\]

For every pair \((n,d)\), it verifies:
1. the base-\((d+1)\) one-parameter-subgroup weights are distinct on all degree-\(d\) monomials;
2. the monomials divisible by a \((d-1)\)-st power of a coordinate variable are exactly the predicted
\[
n^2
\]
fixed monomials;
3. the quadratic boundary \(d=2\) has the distinct count
\[
\binom{n+1}{2},
\]
confirming that the theorem's \(d\ge3\) range is a genuine phase change in the fixed-point pattern.

The finite computation is regression evidence only. The all-\(n\), all-\(d\ge3\) statement follows from unique factorization and Euler localization.

## Relationship to prior work
Oeding and Raicu study exactly the tangential varieties of Segre--Veronese varieties. They determine minimal generators of the defining ideal and decompose the homogeneous coordinate ring into irreducible representations. Their Veronese specialization is therefore directly about the same projective family.

Targeted inspection of that source found no occurrence of “Euler” or “fixed point.” The coordinate-ring and ideal descriptions do not by themselves state the ordinary topological Euler characteristic of this singular projective variety.

Khadam and Vodička later classify which Segre--Veronese tangential varieties are Cohen--Macaulay or Gorenstein. Targeted full-text searches again found no “Euler” or “fixed point” occurrence.

Searches for Euler-characteristic, Poincaré-polynomial, motivic, tangent-developable, and torus-fixed formulations did not locate the degree-independent formula above.

## Limitations
The result computes only ordinary Euler characteristic. It does not determine the individual Betti numbers, intersection cohomology, singular locus, degree, or mixed Hodge structure.

The quadratic case is deliberately excluded: its tangential variety is the symmetric rank-at-most-two locus, whose fixed monomials include every quadratic coordinate monomial rather than only the ordered tangent directions occurring for \(d\ge3\).

The torus-localization argument is short, so an older unindexed or folklore statement remains a residual originality risk.

## References
Luke Oeding and Claudiu Raicu, *Tangential varieties of Segre--Veronese varieties*, arXiv:1111.6202, first submitted 26 November 2011; *Collectanea Mathematica* 65 (2014), 303--330, DOI 10.1007/s13348-014-0111-1.

M. Azeem Khadam and Martin Vodička, *Cohen--Macaulay and Gorenstein tangential varieties of the Segre--Veronese varieties*, *Bulletin of the London Mathematical Society* 54 (2022), 1721--1740, DOI 10.1112/blms.12652.
