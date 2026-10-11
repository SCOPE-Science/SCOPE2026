# Exact quadratic stability identity for Morley reflection defects

## Finding

Let \(\Delta\) be an \(n\)-simplex with \(n\ge3\), and suppose its Morley simplex
\[
\mathcal M(\Delta)=\operatorname{conv}\{M_1,\ldots,M_{n+1}\}
\]
is regular with edge length \(L\).

Use the notation of Tran's reflection-defect criterion:
\[
q_{ij}=2\cos\!\left(\frac{\theta_{ij}}3\right),
\qquad
t_i>0,
\]
and, for \(i\ne j\),
\[
\varepsilon_{ij}
=
q_{ij}+2-\frac{(t_i+t_j)^2}{L^2}.
\]
Fix \(i\ne j\), write
\[
q=q_{ij},
\]
and, for every \(k\notin\{i,j\}\), define the centered weighted row difference
\[
r_k
=
t_k(q_{ki}-q_{kj})
-
\frac{q-1}{2}(t_j-t_i).
\]

Then
\[
\boxed{
\sum_{k\ne i,j}r_k^2
-
\frac1{n+1}
\left(\sum_{k\ne i,j}r_k\right)^2
=
\frac{L^2}{2}(q-1)^2\varepsilon_{ij}.
}
\]

This identity gives an exact quantitative version of the source's reflection test. In addition,
\[
\boxed{
|t_i-t_j|
\le
L\sqrt{\frac{2-q}{q+2}}\,
\sqrt{\varepsilon_{ij}}.
}
\]
Consequently, for each \(k\notin\{i,j\}\),
\[
\boxed{
|t_k(q_{ki}-q_{kj})|
\le
\frac{(q-1)L}{2}
\left(
\sqrt3+
\sqrt{\frac{2-q}{q+2}}
\right)
\sqrt{\varepsilon_{ij}}.
}
\]

The quadratic form on the left has eigenvalues \(1\) and \(2/(n+1)\). Hence the identity also gives the two-sided aggregate estimate
\[
\frac{L^2}{2}(q-1)^2\varepsilon_{ij}
\le
\sum_{k\ne i,j}r_k^2
\le
\frac{(n+1)L^2}{4}(q-1)^2\varepsilon_{ij}.
\]

At \(\varepsilon_{ij}=0\), the estimates force
\[
t_i=t_j
\quad\text{and}\quad
q_{ki}=q_{kj}
\quad(k\notin\{i,j\}),
\]
recovering the exact transposition-reflection criterion. For small positive defect, they quantify how close the same algebraic data are to that symmetry locus.

## Assumptions and scope

The notation is exactly the one used in the primary source. The vectors \(n_i\) are the inward unit facet normals of \(\Delta\), the affine functions \(\ell_i\) have gradient \(n_i\), and the Morley vertices satisfy
\[
\ell_j(M_i)=t_iq_{ij}.
\]
For genuine simplex dihedral angles,
\[
1<q_{ij}<2.
\]

The theorem assumes that the Morley simplex is exactly regular. It does not provide a stability theorem when \(\mathcal M(\Delta)\) itself is only approximately regular.

The conclusion is a quantitative statement about one candidate transposition \(i\leftrightarrow j\). It does not assert that a small reflection defect must occur in every regular-Morley simplex.

## Proof

Set
\[
v=M_j-M_i,
\qquad
m=\frac{M_i+M_j}{2},
\qquad
a=n_i-n_j.
\]
Because \(\mathcal M(\Delta)\) is regular,
\[
|v|=L.
\]

The source's affine-coordinate formula gives
\[
(\ell_i-\ell_j)(M_i)=(1-q)t_i,
\]
and
\[
(\ell_i-\ell_j)(M_j)=(q-1)t_j.
\]
Since \(\nabla(\ell_i-\ell_j)=a\),
\[
a\cdot v
=
(q-1)(t_i+t_j).
\]
Tran's normal-vector computation gives
\[
|a|^2=(q-1)^2(q+2).
\]

Let \(a_\perp\) be the orthogonal projection of \(a\) onto \(v^\perp\). Then
\[
|a_\perp|^2
=
|a|^2-\frac{(a\cdot v)^2}{L^2}
=
(q-1)^2
\left(
q+2-\frac{(t_i+t_j)^2}{L^2}
\right),
\]
so
\[
\boxed{
|a_\perp|^2=(q-1)^2\varepsilon_{ij}.
}
\]

For every \(k\notin\{i,j\}\), put
\[
w_k=M_k-m.
\]
The regular-simplex edge equalities imply
\[
w_k\cdot v=0,
\qquad
|w_k|^2=\frac{3L^2}{4},
\]
and, for distinct \(k,\ell\notin\{i,j\}\),
\[
w_k\cdot w_\ell=\frac{L^2}{4}.
\]
There are \(n-1\) such vectors, so they form a basis of the \((n-1)\)-dimensional space \(v^\perp\). Their Gram matrix is
\[
G=\frac{L^2}{4}(2I+J),
\]
where \(J\) is the all-ones matrix. Therefore
\[
G^{-1}
=
\frac2{L^2}
\left(
I-\frac1{n+1}J
\right).
\]

Now
\[
(\ell_i-\ell_j)(m)
=
\frac{q-1}{2}(t_j-t_i),
\]
while
\[
(\ell_i-\ell_j)(M_k)
=
t_k(q_{ki}-q_{kj}).
\]
Hence
\[
a_\perp\cdot w_k
=
a\cdot w_k
=
r_k.
\]
If \(r\) denotes the column vector of the \(r_k\), the basis Gram identity gives
\[
|a_\perp|^2=r^TG^{-1}r.
\]
Substituting the inverse of \(G\) yields
\[
|a_\perp|^2
=
\frac2{L^2}
\left[
\sum r_k^2
-
\frac1{n+1}
\left(\sum r_k\right)^2
\right].
\]
Combining this with
\[
|a_\perp|^2=(q-1)^2\varepsilon_{ij}
\]
proves the exact quadratic formula.

For the scale-parameter estimate, the two orthogonal projections used in the source's proof of Proposition 3.2 give
\[
\frac{(t_i+t_j)^2}{L^2(q+2)}
+
\frac{(t_i-t_j)^2}{L^2(2-q)}
\le1.
\]
Since
\[
\frac{(t_i+t_j)^2}{L^2}
=
q+2-\varepsilon_{ij},
\]
one obtains
\[
\frac{(t_i-t_j)^2}{L^2(2-q)}
\le
\frac{\varepsilon_{ij}}{q+2},
\]
which is the claimed bound.

Finally,
\[
|r_k|
=
|a_\perp\cdot w_k|
\le
|a_\perp|\,|w_k|
=
\frac{\sqrt3}{2}(q-1)L\sqrt{\varepsilon_{ij}}.
\]
Adding
\[
\frac{q-1}{2}|t_j-t_i|
\]
and using the preceding scale estimate gives the pointwise weighted-row bound.

The eigenvalues of
\[
I-\frac1{n+1}J
\]
on \(\mathbb R^{n-1}\) are \(1\) on the orthogonal complement of the all-ones vector and \(2/(n+1)\) on that vector. This gives the stated two-sided aggregate estimate.

## Verification

The proof is exact and does not depend on finite sampling.

The bundled checker reconstructs, with rational arithmetic, the Gram matrix
\[
G=\frac{L^2}{4}(2I+J)
\]
and its claimed inverse for dimensions \(3\) through \(80\). It then tests the quadratic identity on a deterministic family of exact rational coordinate vectors in every checked dimension and verifies the eigenvalue bounds algebraically.

The primary source was inspected through Proposition 3.2 and its proof. The source proves nonnegativity of \(\varepsilon_{ij}\), characterizes the zero case by reflection symmetry, and derives the two projection identities used above. It does not state the exact quadratic row-difference representation or the resulting square-root stability estimates.

## Relationship to prior work

Tran introduces
\[
\varepsilon_{ij}
=
q_{ij}+2-\frac{(t_i+t_j)^2}{L^2}
\]
as a reflection defect. Proposition 3.2 proves
\[
\varepsilon_{ij}\ge0
\]
and shows that equality is equivalent to the reflection interchanging \(A_i\) and \(A_j\). In the equality case, the proof obtains
\[
t_i=t_j
\]
and then
\[
q_{ik}=q_{jk}
\]
for all remaining indices.

The new identity quantifies exactly how the latter row-equality argument fails away from zero defect. The regular Morley simplex itself supplies a canonical Gram matrix on the perpendicular bisector of \(M_iM_j\), which turns the orthogonal component of \(n_i-n_j\) into the displayed positive-definite quadratic form.

The companion tetrahedron paper studies converse questions, counterexamples, and symmetry classes in dimension three. The inspected result summary does not state an all-dimensional quantitative reflection-defect identity.

Searches for approximate reflection symmetry, small reflection defect, weighted Morley-row differences, and the exact variables from Proposition 3.2 found no prior statement of this formula or its explicit square-root estimates.

## Limitations

The result is conditional on exact regularity of the Morley simplex. Extending it to a quantitatively near-regular Morley simplex would require controlling perturbations of the regular-simplex Gram matrix and is not proved here.

The weighted row difference
\[
t_k(q_{ki}-q_{kj})
\]
is the natural quantity directly controlled by the affine Morley coordinates. An unweighted bound on
\[
q_{ki}-q_{kj}
\]
would additionally require lower bounds on the relevant \(t_k\).

The theorem controls one transposition defect at a time. It does not resolve the source's open reflection conjectures in dimensions four and five, nor the existence problem in the remaining higher dimensions.

The main residual bibliographic risk is a lower-dimensional equivalent hidden in earlier Morley-tetrahedron literature under different notation; no such statement was located, and such a specialization would not by itself cover the all-dimensional identity proved here.

## References

1. Quang Hung Tran, *Morley Simplices in Higher Dimensions: Regularity, Reflections, and Counterexamples*, arXiv:2610.01216v1, 1 October 2026.
2. Quang Hung Tran, *The Converse Problem for the Morley Tetrahedron: Counterexamples, Conjectures, and Partial Results*, arXiv:2609.06553v2, 1 October 2026 revision.
