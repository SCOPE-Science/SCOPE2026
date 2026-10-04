# Independent corner truncations realize the high illumination spectrum near the cube

## Finding

Let
\[
C_n=[-1,1]^n,
\qquad n\ge3,
\]
and regard its vertices \(\{-1,1\}^n\) as the vertex set of the hypercube graph. Let \(T\) be any independent set in that graph, so no two vertices of \(T\) are adjacent. Assign an arbitrary truncation depth
\[
0<\tau_t<1
\]
to every \(t\in T\), and define
\[
K(T,\tau)
=
C_n\cap
\bigcap_{t\in T}
\{x\in\mathbb R^n:\langle t,x\rangle\le n-\tau_t\}.
\]
Thus each selected cube corner is cut off by a shallow hyperplane perpendicular to its sign vector.

Then the illumination number is exactly
\[
\boxed{I(K(T,\tau))=2^n-|T|}.
\]

If \(T\ne\varnothing\) and
\[
\tau_{\max}=
\max_{t\in T}\tau_t,
\]
then
\[
\left(1-\frac{\tau_{\max}}n\right)C_n
\subset
K(T,\tau)
\subset C_n,
\]
so
\[
d_{BM}(K(T,\tau),C_n)
\le
\left(1-\frac{\tau_{\max}}n\right)^{-1}.
\]
Hence these exact illumination numbers persist for polytopes arbitrarily close to the cube.

A parity class of \(\{-1,1\}^n\) is an independent set of size \(2^{n-1}\). Therefore, for every integer \(q\) satisfying
\[
2^{n-1}\le q\le2^n
\]
and every \(\varepsilon>0\), there is a polytope \(K\) with
\[
d_{BM}(K,C_n)<1+\varepsilon
\]
and
\[
I(K)=q.
\]
For \(q<2^n\), the example can be chosen nonparallelotopal.

In particular, arbitrarily small corner perturbations can drop the illumination number of the cube from \(2^n\) all the way to \(2^{n-1}\). In dimension three, arbitrarily small alternating truncations already drop the value from \(8\) to the universal lower bound \(4\).

## Assumptions and scope

Illumination is in the classical Levi--Hadwiger--Boltyanski sense: a nonzero vector \(d\) illuminates a boundary point \(x\) of a convex body \(K\) if
\[
x+\eta d\in\operatorname{int}K
\]
for all sufficiently small positive \(\eta\). The illumination number \(I(K)\) is the minimum number of directions illuminating the whole boundary.

The independence hypothesis on \(T\) means that every neighbor of every truncated cube vertex remains an untruncated cube vertex. It is sufficient for the exact formula. No claim is made here that it is necessary for arbitrary simultaneous corner truncations.

The restriction \(n\ge3\) is essential to the stated illuminating directions: at a new cut vertex the key truncation inequality has directional derivative \(-(n-2)\), which is strict exactly from dimension three onward.

## Proof

Write
\[
U=\{-1,1\}^n\setminus T.
\]
We first identify the vertices of \(K(T,\tau)\).

Fix \(t\in T\). The truncating hyperplane is
\[
H_t=\{x:\langle t,x\rangle=n-\tau_t\}.
\]
If \(s\ne t\) also belongs to \(T\), then their Hamming distance is at least two. For every \(x\in C_n\),
\[
\langle t+s,x\rangle
\le 2(n-d_H(t,s))
\le2n-4.
\]
But a point lying on both truncating hyperplanes would satisfy
\[
\langle t+s,x\rangle
=2n-(\tau_t+\tau_s)>2n-2,
\]
a contradiction. Thus two truncating hyperplanes never meet inside the cube.

A vertex on \(H_t\) must therefore be obtained by intersecting \(H_t\) with \(n-1\) cube facets. If one of those fixed coordinate signs disagreed with \(t\), the remaining coordinate would have to have absolute value greater than one. Hence the only new vertices are
\[
v_{t,i}=t-\tau_t t_i e_i,
\qquad i=1,\ldots,n.
\]
All cube vertices outside \(T\) remain vertices. Consequently,
\[
\operatorname{vert}K(T,\tau)
=
U\cup\{v_{t,i}:t\in T,\ 1\le i\le n\}.
\]

For the lower bound, take \(w\in U\). Every truncation inequality is strict at \(w\), because for \(t\in T\), \(t\ne w\),
\[
\langle t,w\rangle\le n-2<n-\tau_t.
\]
Thus the local tangent cone at \(w\) is exactly the cube tangent cone. A direction \(d\) illuminates \(w\) precisely when
\[
w_i d_i<0
\qquad
(1\le i\le n).
\]
These open sign orthants are disjoint for distinct \(w\). Therefore no one direction can illuminate two different vertices in \(U\), and
\[
I(K(T,\tau))\ge |U|=2^n-|T|.
\]

For the matching upper bound, use the directions
\[
\mathcal D=\{-w:w\in U\}.
\]
Each \(-w\) plainly illuminates its own untruncated cube vertex \(w\).

Now take a new vertex \(v_{t,i}\). Let \(w\) be the cube neighbor of \(t\) obtained by flipping coordinate \(i\). Since \(T\) is independent,
\[
w\notin T,
\]
so \(-w\in\mathcal D\). At \(v_{t,i}\), the active cube facets are exactly the coordinate facets indexed by \(j\ne i\). For each such \(j\),
\[
t_j(-w_j)=-1<0.
\]
The active truncation facet also decreases strictly because
\[
\langle t,-w\rangle=-(n-2)<0.
\]
All other truncation inequalities are strict at \(v_{t,i}\). Hence \(-w\) illuminates \(v_{t,i}\).

Thus every vertex is illuminated by \(\mathcal D\). Illuminating every vertex of a polytope illuminates the whole boundary: if a boundary point lies in a face \(F\), any direction strictly entering through all facets incident to a vertex of \(F\) also strictly enters through every facet incident to that boundary point. Therefore
\[
I(K(T,\tau))\le |\mathcal D|=2^n-|T|.
\]
Together with the lower bound, this proves the exact formula.

For the metric estimate, put
\[
\alpha=1-\frac{\tau_{\max}}n.
\]
If \(x\in\alpha C_n\), then for every \(t\in T\),
\[
\langle t,x\rangle
\le n\alpha
=n-\tau_{\max}
\le n-\tau_t.
\]
Hence
\[
\alpha C_n\subset K(T,\tau)\subset C_n.
\]
It follows directly from the definition of Banach--Mazur distance that
\[
d_{BM}(K(T,\tau),C_n)\le\alpha^{-1}.
\]

Finally, each parity class of cube vertices has cardinality \(2^{n-1}\) and contains no adjacent pair. Given
\[
2^{n-1}\le q\le2^n,
\]
choose any
\[
|T|=2^n-q
\]
vertices from one parity class and take all depths sufficiently small. This realizes the announced spectrum arbitrarily close to the cube.

## Verification

The accompanying `verify.py` checks the local facet inequalities using exact rational arithmetic. It exhausts every subset of one parity class in dimensions three and four, verifies the full parity-class construction through dimension eight, checks that every new cut vertex is illuminated by the direction attached to its untruncated cube neighbor, and checks the Banach--Mazur sandwich algebra.

The replay output is:

`VERIFY_OK independent cube-corner illumination spectrum`

These finite checks are consistency tests. The theorem for every dimension, every independent set, and arbitrary depths in \((0,1)\) is proved analytically above.

## Relationship to prior work

Livshyts and Tikhomirov prove that the cube is a strict local maximizer for illumination: every sufficiently close nonparallelotope in dimension at least three can be illuminated by at most \(2^n-1\) directions. Their Remark 1.2 also gives a sharp one-corner perturbation with illumination number exactly \(2^n-1\).

That one-corner example does not determine what happens when many corners are modified simultaneously. The general local theorem likewise gives only the common upper bound \(2^n-1\); it does not imply any of the exact smaller values in the interval from \(2^{n-1}\) through \(2^n-2\).

The construction here replaces the one-defect sharpness witness by a combinatorial family indexed by independent sets of the cube graph. The exact count is controlled by the untruncated vertices, while independence supplies an untruncated neighbor direction for every new cut vertex. This yields a complete high-half illumination spectrum arbitrarily close to the cube.

Targeted searches using corner truncation, deleted or truncated cube vertices, independent sets, parity classes, illumination spectra, and the expression \(2^n-|T|\) did not locate an equivalent theorem. A published exact computation for several three-dimensional parallelohedra gives isolated illumination numbers, including value \(4\) for one truncated-octahedron representative, but does not imply the near-cube all-dimensional spectrum above.

## Limitations

The exact formula is proved for independent sets of truncated corners. Adjacent simultaneous truncations are not classified here.

The theorem concerns classical real illumination and does not address fractional illumination or optimal homothety ratios in the equivalent covering formulation.

The primary near-cube source already contains the one-corner sharpness case. Originality is therefore claimed only for the simultaneous independent-truncation law, the resulting complete high-half spectrum, and the arbitrarily-near-cube realization of that spectrum. Because the proof is elementary once the right family is chosen, an unindexed or folklore observation remains a residual risk.

## References

G. Livshyts and K. Tikhomirov, “Cube is a strict local maximizer for the illumination number,” arXiv:1710.05070, first submitted 2017-10-13; Discrete & Computational Geometry 63 (2020), 209–228, DOI 10.1007/s00454-019-00115-9.
