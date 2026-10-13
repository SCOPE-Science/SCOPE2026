# A quadratic phase break in Euler characteristic of rank-two Veronese secants
## Finding
Let
\[
X_{n,d}=v_d(\mathbb P^n_{\mathbb C})
\subset
\mathbb P(\operatorname{Sym}^d\mathbb C^{n+1}),
\qquad n\ge1,
\qquad d\ge2,
\]
and let
\[
S_{n,d}=\sigma_2(X_{n,d})
\]
be its second secant variety, equivalently the projective locus of symmetric tensors of border rank at most two.

Then
\[
\boxed{
\chi_{\mathrm{top}}(S_{n,2})=\binom{n+2}{2}
}
\]
and, for every
\[
d\ge3,
\]
\[
\boxed{
\chi_{\mathrm{top}}(S_{n,d})=(n+1)^2.
}
\]

Thus the Euler characteristic has a unique phase break at the quadratic Veronese and is independent of the Veronese degree from degree three onward.

Let
\[
B_{n,d}=S_{n,d}\setminus X_{n,d}
\]
be the exact symmetric border-rank-two stratum. Since
\[
\chi_{\mathrm{top}}(X_{n,d})=n+1,
\]
constructible additivity gives
\[
\boxed{
\chi_c(B_{n,2})=\frac{n(n+1)}2
}
\]
and
\[
\boxed{
\chi_c(B_{n,d})=n(n+1)
\qquad(d\ge3).
}
\]

## Assumptions and scope
The base field is \(\mathbb C\). The Veronese embedding is the complete degree-\(d\) embedding of projective space.

The variety \(S_{n,d}\) is the Zariski closure of secant lines to the Veronese variety, hence it is a border-rank locus. The locally closed complement \(B_{n,d}\) is therefore an exact border-rank-two stratum, not necessarily an exact symmetric-rank-two stratum.

The quadratic case is the familiar projective symmetric-matrix rank-at-most-two locus. Its value is included as the boundary case of the classification; the new structural point is the transition to the degree-independent value \((n+1)^2\) for every \(d\ge3\).

## Proof
Choose coordinates
\[
x_0,\ldots,x_n
\]
and an integer
\[
Q>d.
\]
Let \(\mathbb C^*\) act diagonally by
\[
z\cdot x_i=z^{Q^i}x_i.
\]
A degree-\(d\) monomial
\[
x^\alpha=x_0^{\alpha_0}\cdots x_n^{\alpha_n},
\qquad
\sum_i\alpha_i=d,
\]
has weight
\[
\sum_i\alpha_iQ^i.
\]
Because every digit satisfies
\[
0\le\alpha_i\le d<Q,
\]
uniqueness of base-\(Q\) expansion shows that all degree-\(d\) monomials have distinct weights. Hence the fixed points in the ambient projective space are exactly the monomial coordinate lines.

The Veronese variety and its secant variety are invariant under this action. It remains to determine which monomial coordinate points lie in \(S_{n,d}\).

Every pure power
\[
x_i^d
\]
lies on \(X_{n,d}\).

For \(d\ge3\), every tangent monomial
\[
x_i^{d-1}x_j,
\qquad i\ne j,
\]
lies in \(S_{n,d}\): it is a tangent direction at \([x_i^d]\), and the tangent variety is contained in the closure of secant lines.

Conversely, every point of \(S_{n,d}\) has rank at most two in every catalecticant flattening. For a monomial \(x^\alpha\), the first catalecticant has rank equal to the number of variables appearing in the monomial. Thus any monomial involving at least three variables is excluded from \(S_{n,d}\).

Suppose a monomial involves exactly two variables. If both exponents are at least two, then necessarily \(d\ge4\), and its second catalecticant has at least the three independent degree-two divisors
\[
x_i^2,
\qquad
x_ix_j,
\qquad
x_j^2.
\]
Its rank is therefore at least three, so the monomial is not in \(S_{n,d}\). Consequently, for \(d\ge3\), the only fixed monomials in \(S_{n,d}\) are
\[
x_i^d
\]
and
\[
x_i^{d-1}x_j
\qquad(i\ne j).
\]
Their number is
\[
(n+1)+n(n+1)=(n+1)^2.
\]

When \(d=2\), every quadratic monomial lies in \(S_{n,2}\). Pure squares have rank one, while for \(i\ne j\),
\[
x_ix_j
\]
is a linear combination of two squares. Therefore every ambient monomial fixed point lies in the quadratic secant, and their number is
\[
\binom{n+2}{2}.
\]

For any complex algebraic variety with an algebraic \(\mathbb C^*\)-action, compactly supported Euler characteristic equals that of the fixed locus. One proof removes the fixed locus and applies Rosenlicht stratification; after refinement, each nonfixed stratum is a locally trivial bundle with fiber a finite quotient of \(\mathbb C^*\), whose compactly supported Euler characteristic is zero. Since \(S_{n,d}\) is projective, ordinary and compactly supported Euler characteristic agree. Thus the fixed-point counts above prove the two cumulative formulas.

Finally, the Veronese variety is isomorphic to \(\mathbb P^n\), so
\[
\chi_{\mathrm{top}}(X_{n,d})=n+1.
\]
Subtracting this value from the corresponding secant Euler characteristic gives the formulas for \(B_{n,d}\).

## Verification
The bundled checker enumerates every degree-\(d\) monomial for
\[
1\le n\le7,
\qquad
2\le d\le10.
\]
For each monomial it computes the number of positive exponents, which is the first-catalecticant rank, and counts its degree-two monomial divisors, which gives the monomial second-catalecticant rank.

It verifies that the only monomial fixed points surviving the rank-two flattening tests are all quadratic monomials when \(d=2\), and exactly the pure powers plus tangent monomials when \(d\ge3\). It then verifies the two closed fixed-point counts and the exact-stratum Euler formulas.

Finite enumeration is regression evidence only. The all-parameter theorem follows from base-\(Q\) weight separation, the catalecticant rank obstruction, and Euler localization.

## Relationship to prior work
Ballico and Bernardi study low-border-rank strata of secant varieties of Veronese varieties and compute symmetric ranks of the resulting strata. Raicu studies the same second secant varieties within the Segre--Veronese family and proves that their ideals are generated by cubic flattening minors.

The flattening result is directly compatible with the obstruction used here: points of \(\sigma_2\) satisfy rank-at-most-two conditions in every flattening. The present theorem instead extracts a global topological invariant from the torus-fixed monomials and discovers a degree-two versus degree-at-least-three phase break.

For \(n=1\), the Veronese variety is a rational normal curve. Nogueira later computed topological Euler characteristics of secants to rational normal curves, so the one-dimensional specialization is prior-covered. The statement here is not based on that specialization: its uncovered content is the uniform formula for every higher-dimensional Veronese variety together with the all-\(n\) phase break.

Targeted searches for Euler characteristic of second Veronese secants, symmetric border-rank-two varieties, fixed-point formulas, and Chern--Schwartz--MacPherson formulations did not locate this classification. The quadratic boundary is a known symmetric-determinantal special case; it is included only to state the sharp transition. The archival Veronese-secant sources inspected in full text do not contain an Euler-characteristic statement.

## Limitations
The theorem treats only the second secant variety. Higher Veronese secants have substantially more complicated monomial membership and are not covered.

Euler characteristic is coarse. The degree-independent value for \(d\ge3\) does not imply that the secant varieties have the same Betti numbers, singularities, or intersection theory.

The proof uses standard torus localization and catalecticant rank conditions. A characteristic-class computation or an unindexed transformation-group observation could contain an equivalent Euler formula, so that remains a residual novelty risk.

## References
E. Ballico and A. Bernardi, *Partial stratification of secant varieties of Veronese varieties via curvilinear subschemes*, arXiv:1010.3546, first submitted 18 October 2010; *Sarajevo Journal of Mathematics* 8 (2012), 33--52.

Claudiu Raicu, *Secant Varieties of Segre--Veronese Varieties*, arXiv:1011.5867, first submitted 26 November 2010; *Algebra & Number Theory* 6 (2012), 1817--1868.
