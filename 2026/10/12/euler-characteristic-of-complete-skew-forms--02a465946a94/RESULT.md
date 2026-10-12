# Euler characteristic of complete skew forms
## Finding
Let \(V\) be a complex vector space with
\[
\dim V=n\ge2,
\]
and put
\[
m=\left\lfloor\frac n2\right\rfloor.
\]
Let \(\mathcal A(V)\) be the projective moduli space of complete skew forms: a point is a finite sequence
\[
(\omega_1,\ldots,\omega_m)
\]
of nonzero two-forms such that \(\omega_1\) is defined on \(V\), each \(\omega_{i+1}\) is defined on the kernel of \(\omega_i\), and the final form is nondegenerate when its domain has even dimension and has one-dimensional kernel when its domain has odd dimension.

Then
\[
\boxed{
\chi_{\mathrm{top}}(\mathcal A(V))
=
\frac{n!}{2^{\lfloor n/2\rfloor}}.
}
\]

Equivalently, if \(n=2m\), then
\[
\boxed{
\chi_{\mathrm{top}}(\mathcal A(V))
=
\frac{(2m)!}{2^m}
=
m!(2m-1)!!,
}
\]
while if \(n=2m+1\), then
\[
\boxed{
\chi_{\mathrm{top}}(\mathcal A(V))
=
\frac{(2m+1)!}{2^m}.
}
\]

The Euler characteristic therefore counts ordered matchings of the coordinate labels: ordered perfect matchings in even dimension, and ordered matchings with one residual singleton in odd dimension.

The first values, beginning with \(n=2\), are
\[
1,\ 3,\ 6,\ 30,\ 90,\ 630,\ 2520,\ldots.
\]

## Assumptions and scope
The base field is \(\mathbb C\).

The space \(\mathcal A(V)\) is the classical space of complete skew forms. Thaddeus identifies it with the iterated blow-up of
\[
\mathbb P(\Lambda^2V^*)
\]
along the Pluecker Grassmannian of decomposable two-forms and then along the proper transforms of its secant varieties. In particular, the construction is projective, and the blow-up centers are smooth at the stages where they occur.

The statement concerns ordinary topological Euler characteristic of this smooth projective compactification. It does not concern the open locus of maximal-rank skew forms by itself.

## Proof
Choose a basis
\[
e_1,\ldots,e_n
\]
of \(V\). Let \(\mathbb C^*\) act diagonally with weights
\[
2,\ 2^2,\ldots,2^n.
\]
On \(\Lambda^2V^*\), the coordinate two-form
\[
e_i^*\wedge e_j^*
\]
has a weight determined, up to a common sign convention, by
\[
2^i+2^j.
\]
These pair sums are all distinct by uniqueness of binary expansion.

Consider a fixed complete skew form
\[
(\omega_1,\ldots,\omega_m).
\]
Because its first projective two-form is fixed and all weights on \(\Lambda^2V^*\) are distinct, there is a unique unordered pair
\[
\{i_1,j_1\}
\]
such that
\[
[\omega_1]
=
[e_{i_1}^*\wedge e_{j_1}^*].
\]
This form has rank two, and its kernel is the coordinate subspace spanned by all basis vectors except
\[
e_{i_1},e_{j_1}.
\]

The same argument now applies on that invariant kernel. The next projective two-form must be one coordinate wedge on the remaining labels. Iterating, every fixed complete skew form determines an ordered list of pairwise disjoint unordered pairs
\[
(\{i_1,j_1\},\ldots,\{i_m,j_m\}).
\]
If \(n\) is even, the pairs exhaust all labels. If \(n\) is odd, exactly one label remains, and the final two-form is on a three-dimensional coordinate subspace with that label as its one-dimensional kernel.

Conversely, any such ordered matching determines a complete skew form fixed by the chosen one-parameter subgroup: at each stage take the coordinate wedge belonging to the next pair. Hence the fixed locus is finite and is naturally identified with the set of ordered matchings described above.

Its cardinality is
\[
\binom n2
\binom{n-2}2
\binom{n-4}2
\cdots
=
\frac{n!}{2^m(n-2m)!}.
\]
Since
\[
n-2m\in\{0,1\},
\]
one has
\[
(n-2m)!=1,
\]
so the fixed-point count is
\[
\frac{n!}{2^m}.
\]

The space \(\mathcal A(V)\) is smooth and projective. Bialynicki--Birula decomposition for this \(\mathbb C^*\)-action expresses it as a disjoint union of attracting cells over the fixed components. Here every fixed component is a point. Therefore
\[
\chi_{\mathrm{top}}(\mathcal A(V))
=
\#\mathcal A(V)^{\mathbb C^*}
=
\frac{n!}{2^m}.
\]
This proves the theorem.

## Verification
The bundled checker performs two independent finite regressions.

First, it constructs all ordered matchings recursively for
\[
2\le n\le10
\]
and verifies that the resulting sets have cardinality
\[
\frac{n!}{2^{\lfloor n/2\rfloor}}.
\]

Second, it evaluates the recurrence
\[
F(n)=\binom n2F(n-2),
\qquad
F(0)=F(1)=1,
\]
through
\[
n=80
\]
and verifies the same factorial closed form exactly.

The finite computations are regression evidence only. The theorem for every \(n\) is proved by the fixed-point classification and Bialynicki--Birula decomposition.

## Relationship to prior work
Thaddeus gives the definition of a complete skew form and proves that its moduli space is the successive blow-up of projective skew forms along the Pluecker Grassmannian and the proper transforms of its secant varieties. Massarenti later develops the same space as a wonderful spherical variety and studies its cones, Cox ring, and birational geometry.

A related paper of Can, Howe, and Joyce computes the Poincare polynomial of the fixed locus of a regular unipotent operator on the wonderful compactifications of complete quadrics and complete skew forms. That is a different space from the whole complete-skew-form compactification considered here.

Targeted searches for the Euler characteristic of the complete-skew-form variety, its Poincare polynomial, torus-fixed-point counts, factorial formulas, and ordered-matching descriptions did not locate the formula above. The result also contrasts with the behavior of the companion compactifications: complete quadrics have a substantially different Euler sequence, whereas complete collineations have a different factorial-square law.

## Limitations
Euler characteristic is coarse. The formula does not determine the Betti numbers, the Poincare polynomial, the Chow ring, or the cohomology-ring multiplication of \(\mathcal A(V)\).

The fixed-point proof uses the standard complete-skew-form compactification. It does not assert the same value for arbitrary compactifications of the maximal-rank skew-form locus.

The fixed-point classification is elementary after the classical compactification is in place. An older cell-decomposition or wonderful-compactification computation could therefore imply the same formula without using the ordered-matching language.

## References
Michael Thaddeus, *Complete collineations revisited*, arXiv:math/9808114, first submitted 27 August 1998; *Mathematische Annalen* 315 (1999), 469--495, DOI 10.1007/s002080050324.

Alex Massarenti, *On the birational geometry of spaces of complete forms II: skew-forms*, arXiv:1803.09011, first submitted 23 March 2018; *Journal of Algebra* 546 (2020), 178--200, DOI 10.1016/j.jalgebra.2019.10.047.

Mahir Bilen Can, Roger Howe, and Michael Joyce, *An analogue of Springer fibers in certain wonderful compactifications*, *Journal of Algebra and Its Applications* 16 (2017), 1750172, DOI 10.1142/S0219498817501729.
