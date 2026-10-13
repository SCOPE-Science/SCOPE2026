# Factorization type is invisible to Euler characteristic for reducible-form varieties
## Finding
Let \(V\) be a complex vector space of dimension
\[
m\ge2,
\]
let
\[
d\ge2,
\]
and let
\[
\lambda=(d_1,\ldots,d_r),
\qquad
r\ge2,
\qquad
d_i\ge1,
\qquad
d_1+\cdots+d_r=d.
\]
Let
\[
X_\lambda(V)
\subset
\mathbb P(\operatorname{Sym}^dV^*)
\]
be the projective variety of degree-\(d\) forms that admit a factorization
\[
F=F_1\cdots F_r,
\qquad
\deg F_i=d_i.
\]

Then
\[
\boxed{
\chi_{\mathrm{top}}\!\left(X_\lambda(V)\right)
=
\binom{d+m-1}{m-1}.
}
\]

This number is independent of the partition \(\lambda\), and it is exactly the Euler characteristic of the ambient projective space:
\[
\boxed{
\chi_{\mathrm{top}}\!\left(X_\lambda(V)\right)
=
\chi_{\mathrm{top}}\!\left(
\mathbb P(\operatorname{Sym}^dV^*)
\right).
}
\]

For \(m=2\), every binary form splits over \(\mathbb C\), so this agrees with the fact that \(X_\lambda(V)\) is the whole ambient projective space.

For \(m\ge3\), the generic degree-\(d\) form is irreducible, so \(X_\lambda(V)\) is a proper subvariety; nevertheless its Euler characteristic is still the full ambient value, for every factorization type.

## Assumptions and scope
The base field is \(\mathbb C\).

The partition is unordered mathematically, although an ordering of the parts may be used in the multiplication parameterization
\[
\prod_{i=1}^{r}\mathbb P(\operatorname{Sym}^{d_i}V^*)
\longrightarrow
\mathbb P(\operatorname{Sym}^{d}V^*).
\]

The statement concerns ordinary topological Euler characteristic of the projective image. It does not claim that different factorization loci have the same Betti numbers, singularities, dimensions, or intersection theory.

## Proof
Choose coordinates
\[
x_0,\ldots,x_{m-1}
\]
on \(V\), and choose an integer
\[
B>d.
\]
Let \(\mathbb C^*\) act diagonally by
\[
z\cdot x_j=z^{B^j}x_j.
\]
A degree-\(d\) monomial
\[
x^\alpha=x_0^{\alpha_0}\cdots x_{m-1}^{\alpha_{m-1}},
\qquad
\sum_j\alpha_j=d,
\]
has weight
\[
w(\alpha)=\sum_{j=0}^{m-1}\alpha_jB^j.
\]

Because
\[
0\le\alpha_j\le d<B,
\]
the base-\(B\) expansion is unique. Hence distinct degree-\(d\) monomials have distinct weights. Therefore the fixed locus of the induced action on
\[
\mathbb P(\operatorname{Sym}^dV^*)
\]
consists exactly of the monomial coordinate points.

There are
\[
N=\binom{d+m-1}{m-1}
\]
degree-\(d\) monomials.

Now every degree-\(d\) monomial belongs to \(X_\lambda(V)\). Indeed, view
\[
x^\alpha
\]
as a multiset of \(d\) coordinate variables, with \(x_j\) repeated \(\alpha_j\) times. Partition these \(d\) factors into ordered blocks of sizes
\[
d_1,\ldots,d_r.
\]
The product inside each block is a monomial \(M_i\) of degree \(d_i\), and
\[
x^\alpha=M_1\cdots M_r.
\]
Thus every ambient fixed point lies in \(X_\lambda(V)\).

Conversely, a fixed point of the restricted action on \(X_\lambda(V)\) is a fixed point of the ambient projective action. Therefore
\[
X_\lambda(V)^{\mathbb C^*}
\]
is exactly the set of all \(N\) degree-\(d\) monomial points.

For a complex projective algebraic variety \(Y\) with an algebraic \(\mathbb C^*\)-action,
\[
\chi_{\mathrm{top}}(Y)
=
\chi_{\mathrm{top}}(Y^{\mathbb C^*}).
\]
One way to see this, without assuming smoothness, is to remove the fixed locus and use a finite Rosenlicht stratification of the complement. After refining by stabilizer type, every nonfixed stratum is a locally trivial bundle whose fiber is a finite quotient of \(\mathbb C^*\), hence isomorphic to \(\mathbb C^*\) and has compactly supported Euler characteristic zero. Additivity leaves only the fixed locus. Projectivity identifies compactly supported and ordinary Euler characteristic.

Applying this to \(Y=X_\lambda(V)\) gives
\[
\chi_{\mathrm{top}}\!\left(X_\lambda(V)\right)
=
\#X_\lambda(V)^{\mathbb C^*}
=
N
=
\binom{d+m-1}{m-1}.
\]
This is also the Euler characteristic of the ambient projective space
\[
\mathbb P^{N-1}.
\]

## Verification
The bundled checker tests the two finite ingredients used in the proof.

For
\[
2\le m\le5,
\qquad
2\le d\le8,
\]
it enumerates every degree-\(d\) monomial and every integer partition of \(d\) with at least two parts. It verifies that the base-\(B\) weights are pairwise distinct and constructs, for every monomial and every partition, a factorization into monomials with the prescribed degrees.

It separately verifies that the number of fixed monomial points equals
\[
\binom{d+m-1}{m-1}.
\]

These finite checks are regression evidence only. The all-parameter theorem is proved by uniqueness of base-\(B\) expansion, the elementary prescribed-degree factorization of a monomial, and Euler localization.

## Relationship to prior work
The varieties \(X_\lambda(V)\) are classical varieties of reducible forms. Modern secant-variety treatments define them for an arbitrary partition
\[
\lambda=(d_1,\ldots,d_r)
\]
and study how their dimensions, secant dimensions, defectivity, and singular behavior depend on the partition.

The all-linear partition is the familiar variety of completely decomposable forms. The present statement shows that the ordinary Euler characteristic does not merely simplify in that special case: it is completely independent of every factorization type.

The inspected primary full text devoted to arbitrary reducible-form varieties contains no Euler-characteristic, torus-fixed-point, or monomial-localization statement. Targeted searches using reducible-form, factorization-variety, Euler-characteristic, torus-fixed-point, and ambient-Euler language did not locate the theorem above.

## Limitations
Euler characteristic is coarse. Equality with the ambient Euler characteristic does not imply that \(X_\lambda(V)\) has the homology, homotopy type, singularities, or dimension of the ambient projective space.

The theorem concerns the closed projective locus of forms admitting the prescribed factorization. It does not compute the Euler characteristic of the locally closed locus whose irreducible factor degrees are exactly \(\lambda\).

The fixed-point proof is short once the classical reducible-form parameter space is combined with Euler localization. An unindexed observation in transformation-group or factorization-variety literature therefore remains a residual novelty risk.

## References
M. V. Catalisano, A. V. Geramita, A. Gimigliano, B. Harbourne, J. Migliore, U. Nagel, and Y. S. Shin, *Secant Varieties of the Varieties of Reducible Hypersurfaces in \(\mathbb P^n\)*, arXiv:1502.00167, first submitted 31 January 2015; *Journal of Algebra* 528 (2019), 381--438.
