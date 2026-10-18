# Sharp section-facet bound and generic equality classification for cyclic four-polytopes

## Finding
For every integer \(n\ge5\), put
\[
C(n,4)=\operatorname{conv}\{\gamma(t_i):1\le i\le n\},\qquad
\gamma(t)=(t,t^2,t^3,t^4),\qquad t_1<\cdots<t_n.
\]
For any affine hyperplane \(H\), let \(f_2(C(n,4)\cap H)\) count its two-dimensional polygonal facets when the intersection is three-dimensional (and count two-dimensional faces of a lower-dimensional section according to the usual convention). The sharp maximum is
\[
\max_H f_2(C(n,4)\cap H)=
\begin{cases}
5,&n=5,\\[2pt]
\left\lfloor n^2/4\right\rfloor+2n-12,&n\ge6.
\end{cases}
\]
For \(n\ge7\), **every generic maximizer** has exactly four cyclic sign changes, as balanced a positive/negative vertex split as possible, and precisely one singleton run of each sign; conversely every such sign word is realizable and maximizes. With \(p=\lfloor n/2\rfloor\) and \(q=\lceil n/2\rceil\), its complete face inventory is
\[
(f_0,f_1,f_2)=(pq,\,2pq+2n-14,\,pq+2n-12),
\]
with exactly \(4n-20\) triangular and \(pq-2n+8\) quadrilateral facets.

## Assumptions and scope
A **generic intersecting hyperplane** strictly separates all the original vertices into two nonempty sets: no \(\gamma(t_i)\) lies on \(H\). Its sign word \(w_i\in\{+,-\}\) is read in increasing order of the \(t_i\), with cyclic adjacency also between positions \(n\) and \(1\). A **run** is a maximal cyclic consecutive block of equal signs, and a **singleton run** has length one. The four-change hypothesis means exactly two runs of each sign.

The section has dimension three whenever the hyperplane intersects the polytope's interior. Since the four-polytope is simplicial, a generic three-dimensional section meets each crossed original tetrahedral facet in a triangle or quadrilateral. All claims are independent of the actual distinct parameter values \(t_i\). Nongeneric hyperplanes are included in the numerical maximum; their complete equality classification is not claimed.

## Proof
**1. Original tetrahedral facets.** The Gale-evenness criterion for a cyclic four-polytope says that its four-vertex facets are exactly the unions of two vertex-disjoint edges of the cycle \((1,2),\ldots,(n-1,n),(n,1)\). Indeed, for even moment-curve dimension four the facet indices occur in two adjacent pairs, with a possible pair wrapping around the ordered endpoints. There are \(n(n-3)/2\) such tetrahedral facets. Cyclic four-polytopes are two-neighborly, so every pair of distinct original vertices forms an edge.

**2. Admissible sign words.** A nonconstant affine functional evaluated at \(\gamma(t)\) is a real polynomial of degree at most four. Between successive ordered vertices with opposite signs it must have a real zero. Thus its vertex sign word has at most four cyclic sign changes; because the changes come in pairs, the number is \(2r\), with \(r\in\{1,2\}\) for a mixed word. Conversely, given any such mixed word, choose one root strictly between every consecutive pair having different signs, multiply the resulting linear factors, and choose the overall sign. This polynomial has degree at most four and realizes the word. (If the end signs differ, there are only three linear changes when the cyclic total is four.) A constant term is permitted in an affine hyperplane functional.

**3. Counting crossed tetrahedra.** Put \(p=\#\{i:w_i=+\}\), \(q=n-p\), and let \(s\) be the total number of singleton cyclic runs. There are \(2r\) bichromatic cycle edges, \(p-r\) wholly positive cycle edges, and \(q-r\) wholly negative cycle edges. A tetrahedron meets \(H\) in a polygon exactly when its four vertices carry both signs. Since it is uniquely a pair of vertex-disjoint cycle edges, such pairs have three disjoint types:

* One wholly positive and one wholly negative cycle edge: \((p-r)(q-r)\) pairs; opposite colors make disjointness automatic.
* One bichromatic and one monochromatic cycle edge: initially \(2r(n-2r)\) pairs, from which \(4r-2s\) pairs sharing an endpoint are subtracted. Each non-singleton run has two bichromatic-to-monochromatic incidences, whereas a singleton run contributes none.
* Two bichromatic cycle edges: \(\binom{2r}{2}-s\) disjoint pairs, since shared endpoints occur exactly at singleton runs.

Consequently, the exact generic section facet count is
\[
F(p,q,r,s)=(p-r)(q-r)+2r(n-2r)-(4r-2s)
+\binom{2r}{2}-s
=pq+rn-r^2-5r+s.
\tag{1}
\]
For a generic hyperplane, the section vertex count is \(pq\), one for each crossed original edge.

**4. Optimize the runs.** If \(r=1\) and both classes contain at least two vertices, then \(s=0\) and (1) gives \(F=pq+n-6\); with a singleton class it gives \(F=2n-6\). Neither reaches the claimed maximum when \(n\ge7\). If \(r=2\), then \(p,q\ge2\), and
\[
F=pq+2n-14+s.
\tag{2}
\]
When both \(p,q\ge3\), neither sign can have two singleton runs, so \(s\le2\). Hence
\[
F\le pq+2n-12\le\lfloor n^2/4\rfloor+2n-12.
\]
Equality forces balanced sign-class sizes and one singleton run of each sign. Conversely, the cyclic word \(+^{p-1}-+-^{q-1}\) meets all these requirements, and step 2 realizes it.

If instead \(p=2\) or \(q=2\), one class may have two singleton runs, but the other (of size at least five when \(n\ge7\)) has at most one, so \(s\le3\). Therefore \(F\le4n-15\), strictly below the balanced bound because \(\lfloor n^2/4\rfloor-2n+3>0\) for every \(n\ge7\). This completes the sharp bound and the generic equality classification for \(n\ge7\).

For \(n=5\) and \(n=6\), there are respectively five and nine original tetrahedral facets, trivially bounding any transverse section's number of facets. The mixed sign words \(++---\) and \(++-+--\), respectively, cross every one of these facets, and are realizable by step 2. Therefore the sharp maxima are respectively \(5\) and \(9\), the latter agreeing with the general formula.

**5. Face inventory at equality.** Among the maximizers for \(n\ge7\), there are \(p-2\) wholly positive and \(q-2\) wholly negative cycle edges and exactly two singleton runs. The quadrilaterals are precisely crossed tetrahedra with two vertices on each side, so their number is
\[
(p-2)(q-2)+\binom42-2=pq-2n+8.
\]
Subtracting from the total \(F=pq+2n-12\) gives exactly \(4n-20\) triangular facets. The section is a three-dimensional convex polytope. Euler's formula yields
\[
f_1=f_0+f_2-2=2pq+2n-14.
\]

**6. Nongeneric hyperplanes.** Let \(H\) intersect the interior of \(C(n,4)\), even if it contains some original vertices. Identify all nearby affine hyperplanes with a common three-space by smoothly varying orthogonal coordinate frames and an interior basepoint. Their sections converge in Hausdorff distance to the three-dimensional section \(Q=C(n,4)\cap H\), and contain a common small Euclidean ball about that basepoint. Their polars therefore also converge in Hausdorff distance. Every vertex of a polytope has a strictly exposing linear functional, with a small open neighborhood of functional directions still uniquely exposing that same vertex. By continuity of support functions, for sufficiently close polars there is at least one extremal point near each of the distinct original polar vertices. Thus the number of polar vertices, equivalently the number of section facets, cannot drop under sufficiently small generic perturbations. The generic upper bound therefore applies to \(Q\) as well. If \(H\) instead supports the original polytope, the section is a proper face of the original simplicial polytope: it is either of dimension at most two, with at most one two-dimensional face, or a tetrahedral facet having four polygonal facets. Both counts lie below the established maxima. This proves the assertion for all affine hyperplanes.

## Verification
Run the independent standard-library implementation included with this result:

```bash
python3 check_cyclic4_sections.py
```

The checker independently generates the tetrahedral facets by Gale's parity criterion for \(5\le n\le14\), checks them against the disjoint-cycle-edge formula, verifies moment-curve facet supporting determinants for \(5\le n\le10\), exhaustively visits all realizable nonconstant sign words with at most four cyclic changes for \(5\le n\le14\), and checks additional reproducible larger-dimensional-size instances. It also verifies equality cases, triangle/quadrilateral inventories and explicit polynomial sign realizations. Its passing marker is `CYCLIC4_SECTION_FACETS_OK`. The infinite-family theorem follows from the counted edge-pair identity and run bounds, not from extrapolation of the finite checks.

## Relationship to prior work
Gale's evenness criterion and neighborliness for cyclic polytopes are classical. Bayer and Bisztriczky present the combinatorial Gale-evenness setup; Oppermann and Thomas explicitly describe the disjoint-consecutive-pair facets of even-dimensional cyclic polytopes. The recent theorem of De Loera, López-Campos and Torres gives the maximum **number of section vertices** \(\lfloor n^2/4\rfloor\) for cyclic four-polytopes: that vertex bound is prior art and is not claimed as new here. Brandenburg, De Loera and Meroni establish general algorithms to optimize face numbers of sections of a given polytope; their results are broader computational machinery, but the inspected statements do not supply the present all-\(n\) closed facet formula or equality characterization. The distinct contribution assessed here is the exact facet bound, polygon-type inventory and maximizing cyclic sign-run characterization.

## Limitations
The classification of **all** maximizing cuts is established for generic hyperplanes only; nongeneric cuts are covered by the maximum inequality, not a separate equality classification. The theorem pertains to cyclic polytopes of dimension exactly four and their affine hyperplane sections, not arbitrary neighborly polytopes or higher codimension. Historical novelty beyond the inspected primary sources remains provisional, especially if a classical oriented-matroid enumeration contains an equivalent formula. No finite-sample statistical claim or independent external verification is asserted.

## References
1. M. Bayer and T. Bisztriczky, *On Gale and braxial polytopes* (2006), arXiv:math/0610940, https://arxiv.org/abs/math/0610940.
2. S. Oppermann and H. Thomas, *Triangulations of cyclic polytopes*, Discrete Mathematics & Theoretical Computer Science 14(2) (2012), DOI:10.46298/dmtcs.3068, https://doi.org/10.46298/dmtcs.3068.
3. J. A. De Loera, G. López-Campos, and M. Torres, *On the Number of Vertices in Hyperplane Cross-Sections of Convex Polytopes* (2024 preprint), arXiv:2412.12419, https://arxiv.org/abs/2412.12419.
4. M. Brandenburg, J. A. De Loera, and C. Meroni, *The Best Ways to Slice a Polytope* (2023 preprint), arXiv:2304.14239, https://arxiv.org/abs/2304.14239.
