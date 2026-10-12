# Euler characteristic of the multiprojective variety of complexes
## Finding
Let
\[
V_0,\ldots,V_n
\]
be nonzero complex vector spaces, with
\[
d_i=\dim V_i.
\]
Consider the multiprojective variety of complexes
\[
\mathbb P\mathcal C(V_0,\ldots,V_n)
\subset
\prod_{i=1}^{n}
\mathbb P\operatorname{Hom}(V_{i-1},V_i),
\]
defined by
\[
f_{i+1}\circ f_i=0
\qquad
(1\le i<n).
\]

Then
\[
\boxed{
\chi_{\mathrm{top}}\!\left(
\mathbb P\mathcal C(V_0,\ldots,V_n)
\right)
=
d_0d_n
\prod_{i=1}^{n-1}d_i(d_i-1).
}
\]

The ambient product has Euler characteristic
\[
\prod_{i=1}^{n}d_{i-1}d_i
=
d_0d_n\prod_{i=1}^{n-1}d_i^2.
\]
Hence, whenever the variety is nonempty,
\[
\boxed{
\frac{
\chi_{\mathrm{top}}(\mathbb P\mathcal C)
}{
\chi_{\mathrm{top}}\!\left(
\prod_{i=1}^{n}\mathbb P\operatorname{Hom}(V_{i-1},V_i)
\right)
}
=
\prod_{i=1}^{n-1}
\left(1-\frac1{d_i}\right).
}
\]

In particular, if some intermediate dimension satisfies
\[
d_i=1
\qquad
(1\le i<n),
\]
then the multiprojective variety of complexes is empty.

## Assumptions and scope
The base field is
\[
\mathbb C.
\]

Every projective factor parametrizes a nonzero map up to scalar. Thus the object differs from the ordinary projectivization of the affine cone of complexes inside a direct sum of matrix spaces.

The theorem allows arbitrary positive endpoint dimensions and arbitrary positive intermediate dimensions. For
\[
n=1,
\]
there is no composition constraint and the empty product convention gives
\[
\chi_{\mathrm{top}}
\left(
\mathbb P\operatorname{Hom}(V_0,V_1)
\right)
=
d_0d_1.
\]

No irreducibility, smoothness, rank condition, or expected-dimension hypothesis is required.

## Proof
Choose bases of all
\[
V_i.
\]
Let
\[
T=\prod_{i=0}^{n}(\mathbb C^*)^{d_i}
\]
be the diagonal change-of-basis torus.

The action of
\[
T
\]
preserves the complex equations because
\[
(g_{i+1}f_{i+1}g_i^{-1})
(g_if_ig_{i-1}^{-1})
=
g_{i+1}(f_{i+1}f_i)g_{i-1}^{-1}.
\]

Choose a one-parameter subgroup
\[
\lambda:\mathbb C^*\longrightarrow T
\]
generically so that, for every
\[
i,
\]
all weights on the matrix coordinates of
\[
\operatorname{Hom}(V_{i-1},V_i)
\]
are pairwise distinct. Such a choice exists because equalities between two coordinate weights give only finitely many proper integral hyperplanes in the cocharacter lattice.

Therefore the fixed locus of each projective factor consists precisely of its matrix-coordinate points, and the fixed locus of the ambient product consists of tuples
\[
([E^{(1)}_{t_1s_1}],\ldots,[E^{(n)}_{t_ns_n}]).
\]

For coordinate matrix units,
\[
E^{(i+1)}_{t_{i+1}s_{i+1}}
E^{(i)}_{t_is_i}
\neq0
\]
if and only if
\[
s_{i+1}=t_i.
\]
Hence a coordinate tuple is a complex exactly when
\[
s_{i+1}\neq t_i
\qquad
(1\le i<n).
\]

The first matrix unit can be chosen in
\[
d_0d_1
\]
ways. Once its target index
\[
t_1
\]
has been chosen, the source index
\[
s_2
\]
has
\[
d_1-1
\]
allowable choices and the next target index has
\[
d_2
\]
choices. Continuing inductively gives
\[
\#\left(
\mathbb P\mathcal C(V_0,\ldots,V_n)
\right)^{\mathbb C^*}
=
d_0d_1
\prod_{i=2}^{n}(d_{i-1}-1)d_i.
\]
Rearranging,
\[
\#\left(
\mathbb P\mathcal C
\right)^{\mathbb C^*}
=
d_0d_n
\prod_{i=1}^{n-1}d_i(d_i-1).
\]

For a complex algebraic variety
\[
Y
\]
with an algebraic
\[
\mathbb C^*
\]
action,
\[
\chi_c(Y)=\chi_c(Y^{\mathbb C^*}).
\]
One may prove this by removing the fixed locus and applying a finite Rosenlicht stratification refined by stabilizer type; every nonfixed stratum has compactly supported Euler characteristic zero.

The multiprojective variety of complexes is projective, so
\[
\chi_{\mathrm{top}}(\mathbb P\mathcal C)
=
\chi_c(\mathbb P\mathcal C).
\]
Its fixed locus is finite, and the displayed count proves the theorem.

If some intermediate
\[
d_i=1,
\]
the formula is zero. This also has a direct explanation: two nonzero maps through a one-dimensional intermediate space cannot have zero composition.

## Verification
The bundled checker exhaustively enumerates coordinate fixed points for every dimension vector
\[
(d_0,\ldots,d_n)
\]
with
\[
1\le d_i\le4
\]
and
\[
1\le n\le5,
\]
subject to a cap that keeps each explicit product finite.

For each coordinate tuple it multiplies consecutive matrix units combinatorially and retains the tuple exactly when every composition is zero. It then compares the surviving count with
\[
d_0d_n\prod_{i=1}^{n-1}d_i(d_i-1).
\]

The checker also verifies the ambient Euler ratio and the emptiness criterion when an intermediate dimension equals one.

These finite computations are regression evidence only. The theorem for arbitrary dimensions and arbitrary length follows from the symbolic fixed-point argument above.

## Relationship to prior work
Cukierman defines exactly the affine variety of differential complexes
\[
f_{i+1}f_i=0
\]
and, because the equations are bilinear, explicitly introduces the multiprojective variety
\[
\mathbb P\mathcal C
\subset
\prod_i\mathbb P\operatorname{Hom}(V_{i-1},V_i).
\]
The same paper studies rank strata, irreducible components, dimensions, resolutions of rank closures, tangent spaces, and applications to foliations.

The inspected full text does not state the topological Euler characteristic of this multiprojective variety. Its occurrence of the phrase “Euler characteristic” refers instead to the alternating dimension sum of a finite complex of vector spaces, not to the topology of the parameter variety. Targeted searches found no Poincaré-polynomial or fixed-point formula for the multiprojective space.

Classical work on varieties of complexes identifies affine components with Schubert-type geometry and studies their singularities. Later derived work treats the same affine varieties as prototypical singular moduli spaces. Those results concern affine or derived geometry and do not imply the multiprojective Euler formula above.

A related projectivized type-\(A\) quiver-locus formula concerns one projectivization of a direct sum of arrow spaces. The object here is different: every arrow is separately projectivized, so all maps are forced to be nonzero and the composition constraints produce the multiplicative factors
\[
d_i-1.
\]

## Limitations
Ordinary Euler characteristic is coarse and does not determine the number of irreducible components, singularity type, Betti numbers, intersection cohomology, multidegree, or Chow class.

The theorem concerns the full multiprojective variety cut out only by the consecutive-composition equations. Additional rank bounds would change the fixed-point count.

The fixed-point proof is short once the multiprojective model is isolated, so an older unindexed or folklore observation remains a residual originality risk.

## References
Fernando Cukierman, *Varieties of complexes and foliations*, arXiv:1111.5514, first submitted 23 November 2011; *Journal of Singularities* 9 (2014), 56--67, DOI 10.5427/jsing.2014.9e.

V. Lakshmibai and P. Magyar, *Degeneracy schemes, quiver schemes, and Schubert varieties*, *International Mathematics Research Notices* 1998, no. 12, 627--640.

Mikhail Kapranov and Svyatoslav Pimenov, *Derived varieties of complexes and Kostant's theorem for \(\mathfrak{gl}(m|n)\)*, arXiv:1504.00339, first submitted 1 April 2015.
