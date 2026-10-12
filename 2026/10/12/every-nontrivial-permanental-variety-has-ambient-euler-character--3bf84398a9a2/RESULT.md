# Every nontrivial permanental variety has ambient Euler characteristic
## Finding
Let
\[
2\le r\le m\le n,
\]
and let
\[
P_{m,n}^r
\subset
\mathbb P^{mn-1}
\]
be the complex projective permanental variety defined by the vanishing of every
\[
r\times r
\]
permanent of a generic
\[
m\times n
\]
matrix.

Then
\[
\boxed{
\chi_{\mathrm{top}}(P_{m,n}^r)
=
mn
=
\chi_{\mathrm{top}}(\mathbb P^{mn-1}).
}
\]

Equivalently, if
\[
U_{m,n}^r
=
\mathbb P^{mn-1}\setminus P_{m,n}^r,
\]
then
\[
\boxed{
\chi_c(U_{m,n}^r)=0.
}
\]

Thus every nontrivial permanental rank condition is invisible to ordinary Euler characteristic. In particular, the square permanent hypersurface has the same Euler characteristic as its ambient projective space.

## Assumptions and scope
The base field is
\[
\mathbb C.
\]

The notation
\[
P_{m,n}^r
\]
denotes the projective locus cut out by all permanents of
\[
r\times r
\]
submatrices of the generic matrix.

Topological Euler characteristic depends only on the underlying reduced complex analytic space. Therefore the statement applies to the underlying projective variety even when the defining permanental scheme has nilpotent or embedded structure.

The range
\[
r\ge2
\]
is essential. For
\[
r=1,
\]
all matrix coordinates vanish, so the projectivized locus is empty.

## Proof
Let the matrix coordinates be
\[
x_{ij},
\qquad
1\le i\le m,
\qquad
1\le j\le n.
\]

Choose row and column weights
\[
a_i=2^i,
\qquad
b_j=2^{m+j}.
\]
Let
\[
\mathbb C^*
\]
act by
\[
z\cdot x_{ij}
=
z^{a_i+b_j}x_{ij}.
\]

The weights
\[
a_i+b_j
\]
are pairwise distinct: their binary expansions have one nonzero digit in the row block and one in the column block. Hence the fixed locus of the ambient projective space consists exactly of the
\[
mn
\]
coordinate points
\[
[E_{ij}].
\]

Fix row and column sets
\[
I=\{i_1,\ldots,i_r\},
\qquad
J=\{j_1,\ldots,j_r\}.
\]
The corresponding permanent is
\[
\operatorname{perm}(X_{I,J})
=
\sum_{\sigma\in S_r}
\prod_{q=1}^{r}x_{i_q,j_{\sigma(q)}}.
\]
Every monomial in this sum has the same torus weight
\[
\sum_{i\in I}a_i+\sum_{j\in J}b_j.
\]
Thus every defining permanent is a semi-invariant, and
\[
P_{m,n}^r
\]
is invariant.

At a coordinate point
\[
[E_{ij}],
\]
only one matrix entry is nonzero. Since
\[
r\ge2,
\]
every monomial in every
\[
r\times r
\]
permanent uses at least two distinct matrix entries, so every defining permanent vanishes. Therefore
\[
(P_{m,n}^r)^{\mathbb C^*}
=
\{[E_{ij}]:1\le i\le m,\ 1\le j\le n\}.
\]

For a complex algebraic variety \(Y\) with an algebraic
\[
\mathbb C^*
\]
action,
\[
\chi_c(Y)=\chi_c(Y^{\mathbb C^*}).
\]
A direct argument removes the fixed locus and uses a finite Rosenlicht stratification; after refinement by stabilizer type, each nonfixed stratum is a locally trivial bundle whose fiber is a finite quotient of
\[
\mathbb C^*,
\]
and hence has compactly supported Euler characteristic zero.

Applying this to the projective permanental variety gives
\[
\chi_{\mathrm{top}}(P_{m,n}^r)
=
\chi_c(P_{m,n}^r)
=
mn.
\]

Finally,
\[
\mathbb P^{mn-1}
=
P_{m,n}^r
\sqcup
U_{m,n}^r,
\]
and
\[
\chi_{\mathrm{top}}(\mathbb P^{mn-1})=mn.
\]
Constructible additivity yields
\[
\chi_c(U_{m,n}^r)=0.
\]

## Verification
The bundled checker tests every format with
\[
2\le m\le5,
\qquad
m\le n\le6,
\qquad
2\le r\le m.
\]

For each format it verifies that all ambient coordinate weights are distinct. It then evaluates every defining permanent at every coordinate point by explicit permutation expansion and verifies vanishing.

Separately, it checks term by term that all monomials of each tested permanent have the same torus weight.

The checker covers
\[
30
\]
formats,
\[
548
\]
coordinate-point tests, and
\[
202968
\]
explicit permanent-term evaluations.

These finite computations are regression evidence only. The theorem for all parameters follows from the symbolic weight and fixed-point argument.

## Relationship to prior work
Chan and Ilten define the same projective permanental schemes and study their Fano schemes, including torus-fixed-point methods on the Fano schemes. Their paper emphasizes smoothness, irreducibility, connectedness, tangent spaces, and components of spaces of linear subspaces lying on permanental varieties.

Boralevi, Carlini, Michałek, and Ventura later emphasize that the geometry of permanental varieties remains poorly understood, and use a
\[
\mathbb C^*
\]
action to study codimension, irreducible components, and singular loci.

The statement here concerns a different invariant of the permanental variety itself: its global ordinary Euler characteristic. Targeted searches for Euler characteristics, Poincaré polynomials, motivic formulas, and torus-fixed Euler formulas did not locate the all-parameter identity above.

For
\[
r=2,
\]
the known component description of the permanental variety is compatible with the formula, but the theorem does not depend on that decomposition.

## Limitations
Euler characteristic is extremely coarse. Permanental varieties may be reducible, singular, and scheme-theoretically nonreduced while still having the ambient Euler value.

The theorem does not compute individual Betti numbers, intersection cohomology, mixed Hodge structure, irreducible components, codimension, or degree.

The proof is short once one chooses a one-parameter subgroup with distinct matrix-coordinate weights, so an older or unindexed observation remains a residual novelty risk.

## References
Melody Chan and Nathan Ilten, *Fano schemes of determinants and permanents*, arXiv:1312.2577, first submitted 9 December 2013; *Algebra & Number Theory* 9 (2015), 629--679, DOI 10.2140/ant.2015.9.629.

Ada Boralevi, Enrico Carlini, Mateusz Michałek, and Emanuele Ventura, *On the codimension of permanental varieties*, arXiv:2402.17839, first submitted 27 February 2024.
