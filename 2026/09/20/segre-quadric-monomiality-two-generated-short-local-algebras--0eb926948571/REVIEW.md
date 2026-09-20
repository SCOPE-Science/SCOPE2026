# Review: Segre-quadric monomiality criterion for two-generated short local algebras

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

**PASS.**

The reduction to the multiplication tensor is valid because \(J^3=0\): products involving \(J^2\) vanish, so multiplication descends to a well-defined surjection
\[
\mu:(J/J^2)\otimes(J/J^2)\to J^2.
\]
A split local algebra in this class is recovered, up to isomorphism, from this tensor modulo a simultaneous change of basis on the two copies of \(V=J/J^2\) and an arbitrary change of basis on \(W=J^2\). Equivalently, the isomorphism invariant relevant here is the diagonal \(\operatorname{GL}(V)\)-orbit of \(K=\ker\mu\).

The equivalence between monomializability and \(K\) being a coordinate subspace in some basis follows from the one-vertex, two-loop Gabriel quiver and \(J^3=0\). No higher multiplication data survive.

The cases \(\dim W=1\) and \(\dim W=3\) reduce respectively to decomposability of a functional and of a tensor; for \(2\times2\) matrices this is exactly rank one.

For \(\dim W=2\), the decomposable tensors form the split Segre quadric \(Q\subset\mathbf P^3\). A projective line contained in \(Q\) is one of the two rulings, giving the common-left or common-right coordinate types. A coordinate line not contained in \(Q\) is one of the diagonal or crossed secants. Conversely, two distinct rational intersection points with matching unordered left and right factor-line sets can be carried by one basis change to one of those two coordinate secants. The use of the same basis change on both tensor factors is essential and is accounted for by the matching condition.

The proof does not divide by \(2\), use a discriminant, or require algebraic closure. The statement is therefore valid in characteristic \(2\) and over finite or nonclosed fields. Tangent lines and non-split secants are correctly excluded.

The count \(1+2+4+2+1=10\) follows from the diagonal-orbit types of coordinate subspaces. The proposed distinctions are invariant under the diagonal action, so no two listed types within the same Hilbert type collapse.

## Originality

**PASS, to the best of our knowledge.**

Bardzell--Green (1999) gives a broad invariant characterization of monomial algebras using gradings and Hochschild cohomology. Mojiri (2006) revisits the isomorphism-to-monomial problem using uniserial modules and gives a necessary condition together with a larger class for which isomorphic-to-monomial implies monomial. These are the most relevant older sources.

Green's 2017 lecture slides explicitly list as an open question: given \(KQ/I\), find a criterion deciding whether it is isomorphic to a monomial algebra. This supports the continuing relevance of explicit recognition criteria. Ringel (2023) develops the short-local setting and Hilbert-type terminology but addresses reflexive modules rather than monomial recognition.

Targeted searches for combinations of “isomorphic to a monomial algebra”, “two loops”, “short local”, “radical cube zero”, “Hilbert type (2,d)”, bilinear/tensor formulations, and Segre-quadric formulations did not locate the theorem above or its ten-type corollary. Searches of current monomial-algebra literature through 2026 likewise did not find direct coverage.

The main residual risk is that the general Bardzell--Green or Mojiri criteria, whose full texts were not inspected, may specialize to an equivalent test after nontrivial simplification. Their accessible abstracts do not state this low-dimensional Segre classification. Accordingly the originality claim is qualified rather than absolute.

## Value

**PASS.**

The result gives a complete and computationally elementary answer for the smallest genuinely nontrivial local recognition class: one vertex, two loops, and Loewy length at most three. It replaces general grading/cohomological recognition machinery by ranks and the incidence of a line with a split quadric, works over arbitrary fields, and isolates exactly why the middle Hilbert type has additional non-monomializable orbits. The ten-type corollary gives a compact classification of all monomial members of the class.

## Checked evidence and limitations

Checked primary or near-primary sources include the published abstracts of Bardzell--Green and Mojiri, Green's lecture slides containing the explicit recognition question, and the open-access Ringel paper for the short-local framework. Recent searches were also made for exact and synonymous formulations and for stronger low-dimensional classifications.

The full texts of Bardzell--Green (1999) and Mojiri (2006) were not inspected, so an equivalent specialization hidden there remains the principal originality uncertainty. No claim is made for embedding dimension at least three, nonsplit local algebras, or algebras with more than one simple module.
