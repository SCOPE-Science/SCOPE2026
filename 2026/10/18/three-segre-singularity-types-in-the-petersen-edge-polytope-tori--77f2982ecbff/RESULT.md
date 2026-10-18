# Three Segre singularity types in the Petersen edge-polytope toric ninefold

## Finding

Let \(G=KG(5,2)\) be the Petersen graph: its vertices are the ten two-element subsets of \(\{1,2,3,4,5\}\), with edges joining disjoint subsets. Let
\[
P_G=\operatorname{conv}\{e_u+e_v:\{u,v\}\in E(G)\}\subset\{x\in\mathbb R^{10}:\sum_u x_u=2\},
\]
and let \(X_G\) be the normal projective toric variety of its **normal fan**, over any algebraically closed field. Then \(\dim X_G=9\). Its **reduced singular locus** has exactly **115 irreducible components**, in three classes:

| Number | Component dimension | Codimension in \(X_G\) | Generic transverse affine toric singularity | Hilbert--Samuel multiplicity | Generic \(\mathbb Q\)-Gorenstein? |
|:--:|:--:|:--:|:--|:--:|:--:|
| 60 | 5 | 4 | Rank-one \(2\times3\) determinantal cone | 3 | No |
| 45 | 4 | 5 | Rank-one \(2\times4\) determinantal cone | 4 | No |
| 10 | 4 | 5 | Rank-one \(3\times3\) determinantal cone | 6 | Yes |

Under the natural \(S_5=\operatorname{Aut}(G)\) action these three classes split, respectively, into component orbits of sizes \((10,20,30)\), \((15,30)\), and \((10)\). Every one of the 15 torus-fixed points is singular. Every simplicial normal cone is unimodular, so singular support equals non-\(\mathbb Q\)-factorial support. The singular locus is not equidimensional. The statements concern support and *generic transverse* singularities, not a description of the entire nonreduced singular scheme.

## Assumptions and scope

The ambient lattice of \(P_G\) is the integer affine hyperplane \(\sum_u x_u=2\). Deleting the tenth coordinate identifies its difference lattice with \(\mathbb Z^9\). The normal fan lives in the dual rank-nine lattice. A component is the closure \(V(\sigma)\) of an orbit of a cone \(\sigma\) minimal among nonsmooth cones. A transverse chart at the generic point of \(V(\sigma)\) is the affine toric variety of \(\sigma\), up to a split torus factor. A rank-one \(a\times b\) determinantal cone means the affine variety cut out by every \(2\times2\) minor in an \(a\times b\) matrix of variables.

## Proof

**1. Exhaustive facets and face lattice.** Express every edge vector after deleting coordinate ten; the 15 points have full affine rank nine and their differences span the entire integer difference lattice (a unit \(9\times9\) minor exists). A facet of a nine-dimensional polytope must contain nine affinely independent vertices. The bundled exact program examines *every* nine-element vertex subset, determines primitive integer supporting hyperplanes by exact rational elimination, rejects planes with vertices on both sides, and deduplicates supporting hyperplanes. It finds precisely 25 facets. Intersecting their vertex masks gives *every* face, including the empty face and full polytope, with face vector by dimensions \((-1,0,\ldots,9)\)
\[
(1,15,105,435,1095,1657,1470,735,195,25,1).
\]
This is an exhaustive proof for this fixed ten-vertex graph, not a sample or floating-point computation.

**2. Smooth versus singular cones.** For every nonempty proper face \(F\), the primitive normals of facets containing \(F\) generate the rays of its normal cone \(\sigma_F\); its dimension is \(9-\dim F\). Exact comparison finds 1,645 faces whose normal cones possess more rays than their dimensions. Of the other 4,087 proper faces, every corresponding normal cone has exactly \(9-\dim F\) rays and has an integral maximal minor of absolute value one. Those cones are unimodular. Consequently singular cones are **precisely** the 1,645 nonsimplicial cones, and the irreducible components are the orbit closures of their inclusion-minimal cones, equivalently the inclusion-maximal faces among those 1,645 faces.

**3. Exhaustive minimal-cone classification.** The program compares every nonsimplicial face mask by set inclusion, obtaining exactly 115 maximal such faces. Each one has a normal cone of dimension \(r\) with \(r+1\) rays, the ray matrix has a unit \(r\times r\) minor, and its single primitive integral relation has only \(+1\) and \(-1\) coefficients. Sorting the numbers \((a,b)\) of signs gives precisely the following finite certificate:
\[
(\dim F,(a,b),\#F)=(5,(2,3),60),\ (4,(2,4),45),\ (4,(3,3),10).
\]
The unit minor excludes any hidden finite quotient of the transverse lattice. For a saturated cone with one primitive ray relation consisting of \(a\) plus signs and \(b\) minus signs, the Cox quotient by a one-dimensional torus is the rank-one \(a\times b\) determinantal cone: invariant generators are the products of a positive-weight and a negative-weight coordinate; their defining binomials are the \(2\times2\) minors. The generic transverse multiplicity is the degree \(\binom{a+b-2}{a-1}\) of the Segre variety \(\mathbb P^{a-1}\times\mathbb P^{b-1}\). The toric canonical divisor is \(\mathbb Q\)-Cartier on this cone precisely if the primitive relation has equally many plus and minus signs, i.e. \(a=b\).

**4. Symmetry and completeness.** Each of the 120 permutations of the underlying five-element set permutes Petersen vertices and its 15 edge-polytope vertices. Applying all these permutations to all 115 maximal nonsimplicial face masks gives orbits of sizes \((10,20,30)\), \((15,30)\), and \((10)\), without unidentified residual masks. Each of the 15 vertices of \(P_G\) is incident with 18 facets, hence has a nonsimplicial nine-dimensional normal cone; its torus-fixed point is singular. Every nonsmooth cone contains at least one minimal nonsmooth cone; accordingly there can be no other irreducible components of singular support.

## Verification

Run `python3 petersen_edge_toric_check.py` using Python 3.10 or newer; it requires only the standard library and prints a summary followed by the literal line `VERIFY_OK`. All polyhedral predicates, ranks, facets, determinants, inclusion tests, and symmetry actions use integers or exact rational arithmetic. The checker enumerates all \(\binom{15}{9}=5005\) possible nine-vertex facet witnesses, verifies all 25 facets, builds every face as an intersection, checks **all 4,087** simplicial normal cones for a unimodular minor, classifies **all 115** irreducible component cones, and computes their complete \(S_5\) orbit decomposition. Its valid conclusions do not depend on finite sampling from a parametrized infinite family.

## Relationship to prior work

Ohsugi--Hibi [1] establish general definitions and criteria relating simple edge polytopes and smoothness. Tran--Ziegler [2] develop general face and extremal combinatorics of graph edge polytopes. In particular, the easy count of 105 edges in this girth-five graph is **not** claimed here as a new general criterion. The present claim is the fixed Petersen **normal-fan toric variety's complete reduced singular-component census, the three transverse Segre models, and their six symmetry orbits**. The unsigned graph edge polytope here is not the centrally symmetric edge polytope or graphical zonotope of the Petersen graph; results for those different polytopes do not imply this claim without a further argument.

## Limitations

The result gives only the reduced singular support, component dimensions, generic transverse cones and their multiplicities/canonical behavior. It does not identify the scheme-theoretic singular ideal or all local analytic germs on intersections of components. The novelty comparison is against checked sources and accessible records, not a proof that no equivalent result exists in unindexed literature. The integer certificate is exact, but independent audit has not been performed.

## References

[1] Hidefumi Ohsugi and Takayuki Hibi, *Simple polytopes arising from finite graphs*, arXiv:0804.4287v1 (public 2008-04-27), https://arxiv.org/abs/0804.4287.

[2] Tuan Tran and Günter M. Ziegler, *Extremal edge polytopes*, arXiv:1307.6708v1 (public 2013-07-25), https://arxiv.org/abs/1307.6708.
