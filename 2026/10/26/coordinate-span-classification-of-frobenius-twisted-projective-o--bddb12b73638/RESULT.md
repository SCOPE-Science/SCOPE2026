# Coordinate-span classification of Frobenius-twisted projective orbits

## Finding

Let \(k\) be a field of characteristic \(p>0\), let \(n\ge 2\), and let \(G=\mathrm{PGL}_n\) act on \(\mathbb P^{n-1}\) through the entrywise Frobenius endomorphism \(F([A])=[A^{(p)}]\). Write \(k^p=\{a^p:a\in k\}\). For a point \(x=[x_1:\cdots:x_n]\in\mathbb P^{n-1}(k)\), define

\[
V_x=\operatorname{span}_{k^p}\{x_1,\ldots,x_n\}\subset k.
\]

Then \(x\) and \(y\) lie in the same \(G(k)\)-orbit if and only if \(V_y=cV_x\) for some \(c\in k^\times\). Thus the orbit set is in bijection with homothety classes of nonzero finite-dimensional \(k^p\)-linear subspaces \(V\subset k\) satisfying \(\dim_{k^p}V\le n\). Consequently, this action is transitive exactly when \(k\) is perfect.

## Assumptions and scope

The field \(k\) is arbitrary of characteristic \(p>0\); no perfectness or algebraic-closedness assumption is imposed. The integer \(n\) is at least \(2\). The action is the standard projective action precomposed with the Frobenius endomorphism. The notation \(V\sim cV\) means that two subspaces are identified when they differ by multiplication by a nonzero element \(c\in k\). The statement classifies the orbits for this specific action, not for arbitrary parabolic varieties.

## Proof

First, the image of the map \(F:G(k)\to G(k)\) is \(\mathrm{PGL}_n(k^p)\). Indeed, entrywise pth powers have entries in \(k^p\). Conversely, if a projective matrix has a representative \(A\in\mathrm{GL}_n(k^p)\), choose pth roots in \(k\) of its entries to form a matrix \(B\). Since \(\det(B)^p=\det(A)\ne0\), the matrix \(B\) is invertible and \(F([B])=[A]\). Hence the orbits in question are exactly the orbits of \(\mathrm{PGL}_n(k^p)\) on \(\mathbb P^{n-1}(k)\).

If \(y=A x\) for an invertible matrix \(A\) over \(k^p\), then the coordinates of \(y\) are \(k^p\)-linear combinations of those of \(x\), and the inverse matrix gives the reverse inclusion. Therefore \(V_y=V_x\). Replacing a homogeneous representative by \(c x\), with \(c\in k^\times\), replaces \(V_x\) by \(cV_x\). Thus the homothety class \([V_x]\) is an orbit invariant.

For the converse, suppose \(V_y=cV_x\) for some \(c\in k^\times\). Rescale the representative of \(y\) so that \(V_y=V_x=:V\). The maps

\[
\phi_x,\phi_y:(k^p)^n\longrightarrow V,\qquad e_i\longmapsto x_i\text{ or }y_i,
\]

are surjective \(k^p\)-linear maps. Any two surjections from the same finite-dimensional vector space onto \(V\) differ by precomposition with an automorphism of the domain: choose bases of their kernels and lifts of a basis of \(V\). Hence there is \(B\in\mathrm{GL}_n(k^p)\) such that \(\phi_y=\phi_x\circ B\). In coordinates this says \(y=B^{\mathsf T}x\), so the two projective points lie in the same orbit.

Every nonzero finite-dimensional \(k^p\)-subspace \(V\subset k\) of dimension \(r\le n\) occurs: choose a \(k^p\)-basis \(v_1,\ldots,v_r\) and take the point \([v_1:\cdots:v_r:0:\cdots:0]\). This proves the asserted bijection.

If \(k\) is perfect, then \(k^p=k\), so every nonzero coordinate tuple spans the same one-dimensional \(k\)-space and there is one orbit. If \(k\) is imperfect, choose \(t\in k\setminus k^p\). The points \([1:0:\cdots:0]\) and \([1:t:0:\cdots:0]\) have coordinate spans of dimensions one and two over \(k^p\), respectively. These spans cannot be homothetic, so the action is not transitive. This proves the final assertion.

## Verification

The orbit invariant is independent of the choice of homogeneous representative by construction. The converse uses only the elementary fact that two surjections from a fixed finite-dimensional vector space to the same target are related by an automorphism of the source. The image of Frobenius is checked by taking pth roots of a matrix representative and verifying that its determinant remains nonzero. No numerical experiment or external certificate is required; the proof is self-contained.

## Relationship to prior work

Brion, Maccan, and Srimathy study complete homogeneous varieties and non-smooth parabolic stabilizers in positive characteristic. Their introduction discusses failures of transitivity over imperfect fields, gives examples with infinitely many rational-point orbits, and identifies the description of such orbits as a broader open direction. The result here supplies an exact orbit parameter for the specific Frobenius-twisted projective-space action. The inspected portions of the source do not state this coordinate-span classification; the detailed example section was not available for inspection, so a possible special-case overlap remains recorded as a residual risk.

## Limitations

The theorem does not compute the number of homothety classes for every imperfect field, and it does not classify rational-point orbits on general twisted parabolic varieties. It proves nontransitivity for every imperfect field when \(n\ge2\), but it does not claim that the orbit set is infinite in every such field.

## References

- Michel Brion, Matilde Maccan, and Srinivasan Srimathy, *Complete homogeneous varieties over a field*, arXiv:2610.21497v1, submitted 2026-10-15. The introduction discusses non-smooth parabolic varieties over imperfect fields and the open problem of describing rational-point orbits.
