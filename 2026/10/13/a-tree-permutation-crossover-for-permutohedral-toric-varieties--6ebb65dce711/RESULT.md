# A tree–permutation crossover for permutohedral toric varieties
## Finding
Let
\[
X_{\Pi}^n
\]
be the \(n\)-dimensional type-\(A_n\) permutohedral toric variety, and let
\[
L_{\Pi_n}
\]
be the ample toric line bundle corresponding to the regular permutohedron
\[
\Pi_n
=
\operatorname{conv}
\left\{
\sigma(0,1,\ldots,n):
\sigma\in S_{n+1}
\right\}.
\]

Then
\[
\boxed{
\deg_{L_{\Pi_n}}(X_{\Pi}^n)
=
n!(n+1)^{n-1}
}
\]
and
\[
\boxed{
\chi_{\mathrm{top}}(X_{\Pi}^n)
=
(n+1)!.
}
\]
Therefore
\[
\boxed{
\frac{
\deg_{L_{\Pi_n}}(X_{\Pi}^n)
}{
\chi_{\mathrm{top}}(X_{\Pi}^n)
}
=
(n+1)^{n-2}.
}
\]

This yields the complete crossover:
\[
\deg_{L_{\Pi_1}}(X_{\Pi}^1)<\chi_{\mathrm{top}}(X_{\Pi}^1),
\]
\[
\deg_{L_{\Pi_2}}(X_{\Pi}^2)=\chi_{\mathrm{top}}(X_{\Pi}^2)=6,
\]
and
\[
\deg_{L_{\Pi_n}}(X_{\Pi}^n)>\chi_{\mathrm{top}}(X_{\Pi}^n)
\qquad(n\ge3).
\]

Thus the unique equality case is the two-dimensional permutohedral toric variety, the degree-six del Pezzo surface.

After division by \(n!\), the projective degree is
\[
(n+1)^{n-1},
\]
the number of labeled trees on \(n+1\) vertices, while the Euler characteristic is
\[
(n+1)!,
\]
the number of permutations. The geometric crossover is therefore an exact tree-versus-permutation comparison.

## Assumptions and scope
The base field is \(\mathbb C\). The toric variety is the smooth projective variety whose fan is the type-\(A_n\) braid fan.

The polarization is the standard toric polarization associated with
\[
\Pi_n
=
\operatorname{conv}
\left\{
\sigma(0,1,\ldots,n)
\right\}.
\]

The lattice lies in the affine hyperplane containing \(\Pi_n\), with the induced type-\(A_n\) lattice. The volume convention assigns volume \(1\) to a fundamental lattice parallelepiped. With this convention the toric projective degree is \(n!\) times polytope volume.

The theorem does not concern arbitrary generalized permutohedra or other toric polarizations on the same variety.

## Proof
The regular permutohedron of order \(n+1\) has lattice-covolume volume
\[
(n+1)^{n-1}.
\]
This is the classical Cayley-tree volume formula.

For a lattice polytope \(P\) of dimension \(n\), the degree of the associated polarized projective toric variety is
\[
n!\operatorname{Vol}(P)
\]
with the stated lattice-covolume convention. Hence
\[
\deg_{L_{\Pi_n}}(X_{\Pi}^n)
=
n!(n+1)^{n-1}.
\]

The braid fan has one maximal cone for each permutation in
\[
S_{n+1}.
\]
Equivalently, the torus-fixed points of \(X_{\Pi}^n\) are indexed by \(S_{n+1}\). A smooth complete toric variety has Euler characteristic equal to its number of torus fixed points, so
\[
\chi_{\mathrm{top}}(X_{\Pi}^n)
=
(n+1)!.
\]

Therefore
\[
\frac{
\deg_{L_{\Pi_n}}(X_{\Pi}^n)
}{
\chi_{\mathrm{top}}(X_{\Pi}^n)
}
=
\frac{n!(n+1)^{n-1}}{(n+1)!}
=
(n+1)^{n-2}.
\]

At \(n=1\) this ratio is \(1/2\), at \(n=2\) it is \(1\), and for every \(n\ge3\) it is greater than \(1\). This proves the classification.

## Verification
The bundled checker evaluates the tree-volume, toric-degree, and Euler formulas for every
\[
1\le n\le200.
\]

It verifies the exact cross-multiplied identity
\[
D_n(n+1)=E_n(n+1)^{n-1}
\]
and the strict/equality pattern at \(n=1,2,\ge3\).

These finite computations are regression evidence only. The all-dimensional theorem follows from the published permutohedron volume formula, the standard toric degree-volume dictionary, and the braid-fan fixed-point count.

## Relationship to prior work
Postnikov records the regular permutohedron volume
\[
(n+1)^{n-1}
\]
in lattice-covolume normalization and identifies it with Cayley's labeled-tree count.

Henderson and Lehrer study the complex toric variety associated with a Coxeter fan and express its Poincaré polynomial through Weyl-group statistics. In type \(A_n\), evaluation at \(1\) gives
\[
|S_{n+1}|=(n+1)!.
\]

These ingredients separately determine the degree and Euler characteristic. The result here compares them exactly for the standard permutohedral polarization, giving the closed ratio
\[
(n+1)^{n-2}
\]
and the unique equality in dimension two.

Targeted searches for the permutohedral projective degree versus Euler characteristic, the tree-versus-permutation ratio, and the equality case did not locate an equivalent all-dimensional comparison.

## Limitations
The projective degree depends on the polarization. The formula here is specific to the standard regular-permutohedron polarization.

The comparison is elementary once the classical volume and toric fixed-point formulas are juxtaposed. An older or unindexed source may contain the same ratio without emphasizing the crossover.

No claim is made about dual degree, Euclidean-distance degree, or other projective invariants.

## References
Alexander Postnikov, *Permutohedra, associahedra, and beyond*, arXiv:math/0507163, first submitted 7 July 2005; *International Mathematics Research Notices* 2009, no. 6, 1026--1106.

Anthony Henderson and Gustav I. Lehrer, *The equivariant Euler characteristic of real Coxeter toric varieties*, arXiv:0806.0680, first submitted 4 June 2008; *Bulletin of the London Mathematical Society* 41 (2009), 555--562.

Martin Helmer and Bernd Sturmfels, *Nearest points on toric varieties*, arXiv:1603.06544, first submitted 21 March 2016; *Mathematica Scandinavica* 122 (2018), 213--239.
