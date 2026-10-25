# Exact symmetry windows for affine hyperplane sections of a cube

## Finding

Let \(d\ge 2\), \(C=[0,1]^d\), and \(H=\{x\in\mathbb R^d:\sum_{i=1}^d a_i x_i=b\}\), where \(a\ne0\) and \(H\) meets the interior of \(C\). Write
\[
w_i=|a_i|,\qquad W=\sum_{i=1}^d w_i,\qquad m=\max_i w_i,\qquad r=\#\{i:w_i>0\},\qquad t=b-\sum_{a_i<0}a_i.
\]
The scalar \(t\) is the offset after reflecting coordinates with negative normal coefficients; in particular \(0<t<W\). The \((d-1)\)-dimensional section \(P=C\cap H\) is centrally symmetric **if and only if**
\[
\boxed{\quad r\le2\quad\text{or}\quad t=W/2\quad\text{or}\quad W-m\le t\le m.\quad}
\]
The third alternative can hold away from \(t=W/2\) only if \(m>W/2\). Consequently, for \(r\ge3\) and a fixed normal direction, the full set of symmetric offsets is the center offset \(t=W/2\), together with the closed interval \([W-m,m]\) when it is nonempty. Its nontrivial length is \((2m-W)_+\).

Equivalently, **every centrally symmetric full-dimensional hyperplane section of a cube is either a section through the cube center or an affine \((d-1)\)-cube (a parallelotope)**. In particular, every noncentral symmetric section has precisely \(2(d-1)\) facets and \(2^{d-1}\) vertices. The same statement, with an affine change of coordinates, holds for any parallelotope.

## Assumptions and scope

Central symmetry means the existence of \(c\in H\) such that \(P=2c-P\). The hyperplane meets \(\operatorname{int}(C)\), excluding tangent cuts and sections of dimension less than \(d-1\). Reflections \(x_i\mapsto1-x_i\) where \(a_i<0\) replace the signed equation by \(\sum_i w_i y_i=t\); the section's symmetry is unaffected. Coordinates with \(w_i=0\) contribute a Cartesian cube factor, so it suffices to analyze the \(r\) positive coefficients. The last interval is understood literally: when \(W-m>m\), it is empty.

## Proof

Reflect negative-coordinate directions and discard the passive cube factor. We must classify \(S=[0,1]^r\cap\{\sum_i w_i y_i=t\}\), where all \(w_i>0\), \(0<t<W\), and \(S\) has dimension \(r-1\).

If \(r=1\), \(S\) is a point. If \(r=2\), \(S\) is a segment. Reinstating passive coordinates produces a parallelotope. Thus all such sections are centrally symmetric.

Assume \(r\ge3\). In the direction space \(L=\{v:\sum_iw_iv_i=0\}\), the restrictions of two distinct coordinate functionals are never proportional. Indeed, if \(e_i-\lambda e_j\) were in the span of \(w\), a positive coordinate \(w_k\) with \(k\notin\{i,j\}\) would force the multiple of \(w\) to be zero, and hence force the impossible identity \(e_i=\lambda e_j\).

Each facet of \(S\) arises from an active cube inequality \(y_i\ge0\) or \(y_i\le1\). If \(S\) is centrally symmetric, reflection in its center maps every facet to a parallel opposite facet. The nonproportionality just established forces each active \(y_i=0\) facet to be paired with an active \(y_i=1\) facet, and conversely. Call an index *active* if both of these coordinate facets occur. The center \(c\) then satisfies \(c_i=1/2\) at every active index.

The facet normals of a bounded \((r-1)\)-polytope span its \((r-1)\)-dimensional direction dual. Hence at least \(r-1\) coordinate indices are active. If all \(r\) are active, then \(c=(1/2,\ldots,1/2)\in S\), implying \(t=W/2\).

Otherwise, exactly one index \(j\) is inactive. An inequality that defines no facet in a full-dimensional polytope is redundant in its facet description. Therefore the \(2(r-1)\) inequalities \(0\le y_i\le1\) for \(i\ne j\), together with the hyperplane equation, already define \(S\). Solving for the remaining coordinate gives
\[
y_j=\frac{t-\sum_{i\ne j}w_i y_i}{w_j}.
\]
The right side lies in \([0,1]\) for **every** choice \((y_i)_{i\ne j}\in[0,1]^{r-1}\) exactly when
\[
W-w_j\le t\le w_j.
\]
This implies \(w_j\ge W/2\), hence \(w_j=m\). It also shows directly that \(S\) is an affine image of a full \((r-1)\)-cube.

Conversely, if \(t=W/2\), the involution \(y\mapsto\mathbf1-y\) preserves the section. If \(W-m\le t\le m\), pick \(j\) with \(w_j=m\) and use the displayed equation: every choice of the other \(r-1\) coordinates is feasible, making the section an affine cube and therefore centrally symmetric. Together with the cases \(r\le2\), this proves the criterion and the shape classification. A noncentral symmetric section must be an affine \((d-1)\)-cube after including passive coordinates, so its face and vertex counts follow. Finally, any parallelotope is an invertible affine image of a cube, preserving hyperplane sections, central symmetry, and being a parallelotope. \(\square\)

## Verification

The accompanying self-contained Python checker enumerates intersection vertices of each rational hyperplane with cube edges, computes the average vertex as the only possible symmetry center, and tests reflected vertex-set equality using exact rational arithmetic. It checked \(17{,}667\) sections from every nonzero coefficient vector in \(\{0,1,2,3\}^d\) and every half-integer interior offset, for \(d=3,4,5\). All agreed with the criterion. This is a finite regression check; the proof above covers all dimensions and real coefficients. Run `python3 verify_cube_slices.py` in the same directory.

For illustration, normal weights \((5,1,1)\) produce centrally symmetric, generally off-center sections precisely for offsets \(2\le t\le5\), while weights \((1,1,1)\) have only the central symmetric offset \(t=3/2\).

## Relationship to prior work

Brandenburg, Curtis, Giardino, Meroni, and Padrol proved that a cube hyperplane section's combinatorial type is determined by its graph (2026). Their reconstruction theorem is combinatorial, not an offset-by-offset criterion for geometric central symmetry. De Loera, Lopez-Campos, and Torres investigated attainable vertex counts and algorithms for cube slices (first preprint 2024); those counts do not determine the metric symmetry locus. Aichholzer and Aurenhammer classified vertex-spanned cube hyperplanes (1996), a different restriction on the cutting hyperplane. Their full text was not accessible during the comparison, so overlap with special vertex-spanned cases remains a priority risk. The statement here is the continuous, arbitrary-offset classification with a sharp coefficient-dominance boundary.

## Limitations

The theorem concerns codimension-one sections of parallelotopes, not higher-codimension sections of arbitrary centrally symmetric polytopes. It does not classify other isometries or affine automorphisms of sections. The stated source comparisons support priority only under the available evidence; absence of a discovered equivalent classification is not proof of historical uniqueness. One relevant older paper could be assessed only at its abstract, and the stronger implicit coverage by classical facet-description results is a residual risk.

## References

1. M.-C. Brandenburg, J. Curtis, C. Giardino, C. Meroni, and A. Padrol, *Reconstruction of slices of cubes*, arXiv:2610.09939, first posted 7 October 2026. https://arxiv.org/abs/2610.09939
2. J. A. De Loera, G. Lopez-Campos, and A. J. Torres, *On the Number of Vertices in Hyperplane Cross-Sections of Convex Polytopes*, arXiv:2412.12419, first posted 17 December 2024. https://arxiv.org/abs/2412.12419
3. O. Aichholzer and F. Aurenhammer, *Classifying Hyperplanes in Hypercubes*, SIAM Journal on Discrete Mathematics 9 (1996), 225–232, DOI:10.1137/S089548019426348X. https://doi.org/10.1137/S089548019426348X
