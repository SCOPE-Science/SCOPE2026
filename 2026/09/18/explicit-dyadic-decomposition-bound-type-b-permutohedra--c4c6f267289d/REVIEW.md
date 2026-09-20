# Review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

The argument was checked at three lattice levels.

First, for a linearly independent type \(B\) root subconfiguration, the Smith torsion is elementary \(2\)-torsion. After removing degree-one rows or columns by unimodular pivots, any remaining matrix has two nonzero \(\pm1\) entries in every row and column. Its support decomposes into cycle blocks. Independence forces each cycle block to have determinant \(\pm2\), and deleting a row and column gives a unit minor, so each block contributes one invariant factor \(2\) and no higher \(2\)-power.

Second, if independent type \(B\)-root-spanned subspaces \(V,W\) are combined, the saturation quotient
\[
((V+W)\cap\mathbb Z^n)/((V\cap\mathbb Z^n)\oplus(W\cap\mathbb Z^n))
\]
is killed by \(2\). The same conclusion passes to rational subspaces \(V'\subseteq V\), \(W'\subseteq W\) by uniqueness of the decomposition in \(V\oplus W\).

Third, in a join across consecutive coordinate slices, the bridge vector has first coordinate \(1\). Modulo that bridge, the simplex quotient is exactly the quotient of the saturated lattice in the sum of the two slice directions by the two child edge lattices. Thus a genuinely two-sided positive-dimensional join increases the binary annihilator exponent by at most one; joining to a point increases it by zero.

The dimension recurrence was checked separately:
\[
b(r)=\max\{0,\lfloor(r-1)/2\rfloor\},
\]
and for \(r_0,r_1\ge1\),
\[
1+\max\{b(r_0),b(r_1)\}\le b(r_0+r_1+1).
\]
This gives the claimed exponent bound throughout Vallée's deletion-contraction triangulation and survives the integer-coordinate dicing used for general type \(B\) generalized permutohedra.

Finally, the decomposition step needs only the exponent of the finite quotient, not its order. Multiplying \(x-kv_0\) by the quotient exponent places it in the edge lattice; affine independence then makes all scaled barycentric coefficients nonnegative integers. This exactly produces the required number of lattice-point summands.

The low-dimensional lower bound is also direct: \(111\in2T_\triangle\) for
\[
T_\triangle=\operatorname{conv}\{000,110,101,011\},
\]
but \(111\) is not a sum of two lattice points of \(T_\triangle\). Cartesian product with a cube preserves type \(B\) edge directions and preserves the obstruction under projection.

## Originality

The closest source inspected in full was Vallée, arXiv:2609.18331. Its Theorem 0.3 / Corollary 3.7 asserts existence of a dimension-uniform exponent. The proof chooses the exponent from the maximum normalized volume among finitely many simplices in the constructed triangulations. It does not state an explicit bound in the dimension and does not track quotient exponent through the recursive joins.

The half-integrality statement underlying the type \(B\) root lemma is not new in isolation. Bolker and Zaslavsky, *Networks* 48 (2006), prove for bidirected-graph incidence matrices that a column is a half-integral combination of any column basis and that nonsingular square submatrices have half-integral inverse. The type \(B\) roots are the corresponding link/half-edge columns up to signs. The record therefore treats Lemma 1 as a self-contained special-case proof of a classical ingredient; the originality claim is the explicit \(\lfloor(d-1)/2\rfloor\) dyadic-decomposition bound obtained by feeding this exponent-two structure through Vallée's triangulation recursion.

Morales, arXiv:2609.02778, supplies non-IDP delta-matroid examples and explicitly discusses the tetrahedral obstruction, but does not give a positive dyadic saturation bound for all type \(B\) generalized permutohedra.

Targeted searches for combinations of “delta-matroid”, “type B generalized permutohedron”, “dyadic decomposition”, “uniform exponent”, “Smith normal form”, “torsion exponent”, and equivalent semigroup/normality language did not locate the bound
\[
\lfloor(d-1)/2\rfloor
\]
or the simplex quotient-exponent estimate above. No overlapping SCOPE record was located under the motivating arXiv identifier, delta-matroid terminology, generalized-permutohedron terminology, or dyadic-decomposition terminology.

Residual originality risk is non-negligible because arXiv:2609.18331 was submitted on 16 September 2026 and is extremely recent.

## Value

The source theorem gives only existence of a uniform exponent through a finiteness argument. The new bound is explicit, depends on the intrinsic dimension \(d\) rather than ambient dimension, and is obtained from a structural mechanism: type \(B\) root complementarity has exponent \(2\), while each denominator-doubling join consumes at least two dimensions. It also determines the optimal universal exponents in dimensions three and four.

The bound is not shown optimal for \(d\ge5\). In particular, the argument leaves open whether the universal exponent can be bounded by \(1\), or by a smaller function than \(\lfloor(d-1)/2\rfloor\), in higher dimensions. The result is a dyadic decomposition statement and does not imply ordinary IDP or normality.
