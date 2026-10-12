# A type-C suppression law for line-plane flag degrees
## Finding
For every integer
\[
n\ge2,
\]
let
\[
A_n=F(1,2;2n)
\]
be the ordinary flag variety of a line contained in a two-plane in \(\mathbb C^{2n}\), and let
\[
C_n=SF(1,2;2n)\subset A_n
\]
be the symplectic isotropic partial flag variety for a nondegenerate skew-symmetric form.

Embed both varieties by the line bundle corresponding to
\[
\omega_1+\omega_2.
\]
Geometrically, this is the product of the projective line coordinate and the plane Pluecker coordinate, followed by the Segre embedding.

Their projective degrees are
\[
\boxed{
\deg A_n=
\frac{2^{2n-2}(4n-3)!}{(2n-1)!(2n-2)!}
}
\]
and
\[
\boxed{
\deg C_n=
\frac{3\,2^{2n-3}(4n-4)!}{(2n-1)!(2n-3)!}.
}
\]
Their ordinary topological Euler characteristics are
\[
\boxed{
\chi_{\mathrm{top}}(A_n)=2n(2n-1),
\qquad
\chi_{\mathrm{top}}(C_n)=4n(n-1).
}
\]

Therefore the codimension-one isotropy condition changes the two invariants by different exact factors:
\[
\boxed{
\frac{\deg C_n}{\deg A_n}=\frac{3(n-1)}{4n-3},
\qquad
\frac{\chi_{\mathrm{top}}(C_n)}{\chi_{\mathrm{top}}(A_n)}=
\frac{2(n-1)}{2n-1}.
}
\]
Equivalently,
\[
\boxed{
\frac{\deg C_n/\chi_{\mathrm{top}}(C_n)}
{\deg A_n/\chi_{\mathrm{top}}(A_n)}
=
\frac{3(2n-1)}{2(4n-3)}.
}
\]
This last factor is strictly decreasing in \(n\), begins at
\[
\frac{9}{10}
\]
for \(n=2\), and tends to
\[
\frac34.
\]
Thus the symplectic isotropy equation suppresses normalized degree more strongly than it suppresses Euler characteristic, with a universal asymptotic factor of \(3/4\).

## Assumptions and scope
The base field is \(\mathbb C\). The space \(A_n\) parametrizes flags
\[
L\subset U\subset\mathbb C^{2n},
\qquad
\dim L=1,
\qquad
\dim U=2.
\]
The space \(C_n\) is the closed subvariety for which \(U\) is isotropic. Since every line is automatically isotropic for a skew-symmetric form, this is exactly the symplectic partial flag variety with flag dimensions \((1,2)\).

The polarization is the natural Segre-Pluecker polarization
\[
\mathcal O(1,1),
\]
not either individual pullback separately.

## Proof
We compute the two degrees independently from the Weyl dimension formula and the two Euler characteristics from their Schubert cell decompositions.

For the ordinary flag \(A_n\), use type \(A_{2n-1}\). The relevant parabolic leaves a Levi subsystem of type \(A_{2n-3}\), so the complementary positive roots are
\[
e_1-e_2,
\quad
e_1-e_j,
\quad
e_2-e_j
\qquad(3\le j\le2n).
\]
There are
\[
1+2(2n-2)=4n-3
\]
such roots, hence
\[
\dim A_n=4n-3.
\]
For the weight \(\lambda=\omega_1+\omega_2\), the numerator pairings with these coroots are respectively
\[
1,
\quad
2,
\quad
1.
\]
The denominator pairings with \(\rho\) are
\[
1,
\quad
j-1,
\quad
j-2.
\]
Therefore the leading term in the Weyl dimension formula gives
\[
\deg A_n
=(4n-3)!
\frac{2^{2n-2}}
{(2n-1)!(2n-2)!}.
\]

For the symplectic flag \(C_n\), use type \(C_n\). The Levi subsystem is type \(C_{n-2}\), and the complementary positive roots are
\[
e_1-e_2,
\quad e_1+e_2,
\quad 2e_1,
\quad 2e_2,
\]
together with
\[
e_1-e_j,
\quad e_2-e_j,
\quad e_1+e_j,
\quad e_2+e_j
\qquad(3\le j\le n).
\]
There are
\[
4+4(n-2)=4n-4
\]
of them, so
\[
\dim C_n=4n-4.
\]

Write
\[
\lambda=\omega_1+\omega_2=2e_1+e_2,
\qquad
\rho=(n,n-1,\ldots,1).
\]
For the four exceptional roots, the numerator pairings with coroots are
\[
1,\ 3,\ 2,\ 1,
\]
and the denominator pairings are
\[
1,\ 2n-1,\ n,\ n-1.
\]
For every \(3\le j\le n\), the four remaining numerator pairings are
\[
2,\ 1,\ 2,\ 1,
\]
while their denominator pairings are
\[
j-1,
\quad j-2,
\quad 2n-j+1,
\quad 2n-j.
\]
Hence the total numerator is
\[
3\,2^{2n-3},
\]
and the denominator simplifies to
\[
(2n-1)!(2n-3)!.
\]
The Weyl leading coefficient therefore gives
\[
\deg C_n
=
\frac{3\,2^{2n-3}(4n-4)!}
{(2n-1)!(2n-3)!}.
\]

For Euler characteristic, a complex homogeneous space \(G/P\) has one Schubert cell for every coset in \(W/W_P\). Thus
\[
\chi_{\mathrm{top}}(A_n)
=
\frac{(2n)!}{(2n-2)!}
=
2n(2n-1),
\]
while
\[
\chi_{\mathrm{top}}(C_n)
=
\frac{2^n n!}{2^{n-2}(n-2)!}
=
4n(n-1).
\]

Dividing the closed formulas yields
\[
\frac{\deg C_n}{\deg A_n}
=
\frac{3(n-1)}{4n-3}
\]
and
\[
\frac{\chi_{\mathrm{top}}(C_n)}{\chi_{\mathrm{top}}(A_n)}
=
\frac{2(n-1)}{2n-1}.
\]
Dividing these two ratios gives
\[
q_n=
\frac{3(2n-1)}{2(4n-3)}.
\]
Finally,
\[
q_n-q_{n+1}
=
\frac{3}{(4n-3)(4n+1)}>0,
\]
so the suppression factor is strictly decreasing, and its limit is \(3/4\).

## Verification
The bundled checker reconstructs both Weyl products directly from their complementary positive roots for every
\[
2\le n\le100.
\]
It verifies the two factorial degree formulas, the two Weyl-coset Euler formulas, the exact type-C/type-A degree and Euler ratios, and the strict monotonicity of the normalized suppression factor.

The checks include the base cases
\[
(\deg A_2,\chi(A_2))=(40,12),
\qquad
(\deg C_2,\chi(C_2))=(24,8),
\]
so the first normalized suppression factor is indeed
\[
(24/8)/(40/12)=9/10.
\]

Finite calculations are regression evidence only. The all-parameter result is proved by the root-product calculation above.

## Relationship to prior work
Coskun explicitly studies the natural inclusion of a symplectic isotropic partial flag variety into the corresponding ordinary partial flag variety and develops the Schubert calculus of this inclusion. For the present flag dimensions, that inclusion is precisely
\[
C_n\subset A_n.
\]
His full text contains no occurrence of either “Euler” or geometric “degree”, and it does not state the displayed type-C/type-A ratio.

Tamvakis develops Schubert polynomials and the integral cohomology ring for symplectic flag varieties. His archival paper supplies a primary algebraic-geometry source for the type-C flag geometry. It contains no occurrence of “Euler”, and its occurrences of “degree” concern arithmetic intersection theory rather than the projective degree comparison here.

The ordinary line-plane flag degree formula by itself does not determine the symplectic degree: the isotropic flag is a different homogeneous space of one lower dimension, and the Segre-Pluecker degree requires a new type-\(C_n\) Weyl product. Likewise, formulas for symplectic Grassmannians do not determine the mixed \(\omega_1+\omega_2\) degree on the partial flag.

Targeted searches for the exact symplectic line-plane flag, the Segre-Pluecker polarization, projective degree, Euler characteristic, and the ratio \(3(n-1)/(4n-3)\) did not locate an equivalent published statement.

## Limitations
The theorem treats only the line-plane symplectic partial flag and the polarization \(\mathcal O(1,1)\). It does not give a formula for arbitrary symplectic flag dimensions or arbitrary dominant polarizations.

The result compares projective degree and ordinary topological Euler characteristic only. It does not determine the full cohomology ring, Hodge structure, or finer characteristic classes.

The calculation is short once the correct complementary roots are isolated, so an unindexed representation-theoretic or Schubert-calculus observation remains a residual originality risk.

## References
Harry Tamvakis, *Schubert polynomials and Arakelov theory of symplectic flag varieties*, arXiv:0808.1329, first submitted 9 August 2008; *Journal of the London Mathematical Society* 82 (2010), 89--109, DOI 10.1112/jlms/jdq015.

Izzet Coskun, *Symplectic restriction varieties and geometric branching rules II*, *Journal of Combinatorial Theory, Series A* 125 (2014), 47--97, DOI 10.1016/j.jcta.2014.02.004.
