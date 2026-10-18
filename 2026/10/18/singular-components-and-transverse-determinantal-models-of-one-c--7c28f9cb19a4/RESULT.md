# Singular components and transverse determinantal models of one-circuit-hyperplane matroid toric varieties

## Finding
Fix integers \(r,s\ge3\), set \(n=r+s\), and choose an \(r\)-element subset \(H\subseteq[n]\); write \(O=[n]\setminus H\). Let \(M\) be the rank-\(r\) matroid whose bases are all \(r\)-subsets except \(H\). Let \(P\) be its base polytope and \(X\) the normal projective toric variety over an algebraically closed field associated to the normal fan of \(P\), with torus of dimension \(n-1\). The reduced singular locus of \(X\) has exactly
\[
 r+s+\binom nr-1-rs
\]
irreducible components, in three types:

1. For each \(h\in H\), a torus-invariant component \(A_h\cong\mathbb P^{s-1}\), of codimension \(r\). Its generic transverse affine toric singularity is the rank-at-most-one \(2\times(r-1)\) matrix variety, of multiplicity \(r-1\).
2. For each \(j\in O\), a torus-invariant component \(B_j\cong\mathbb P^{r-1}\), of codimension \(s\). Its generic transverse singularity is the rank-at-most-one \(2\times(s-1)\) matrix variety, of multiplicity \(s-1\).
3. For every \(r\)-subset \(T\) with \(|T\cap H|\le r-2\), an isolated irreducible component consisting of one torus-fixed point. Its entire affine toric chart is the rank-at-most-one \(r\times s\) matrix variety, with Hilbert--Samuel multiplicity \(\binom{n-2}{r-1}\).

Distinct \(A_h\)'s are disjoint; distinct \(B_j\)'s are disjoint. Each \(A_h\) meets each \(B_j\) in exactly the single torus-fixed point corresponding to the basis \((H\setminus\{h\})\cup\{j\}\). The isolated components do not meet any others. These are **all** intersections. Every torus-fixed point is singular; indeed the non-\(\mathbb Q\)-factorial support equals the singular support. In the balanced example \(r=s=3\), the six positive-dimensional components are copies of \(\mathbb P^2\) with \(K_{3,3}\) pairwise-incidence pattern, and there are ten additional isolated singular components.

## Assumptions and scope
The base polytope lies in the affine lattice \(\sum_i x_i=r\). The cocharacter lattice of the dense torus is \(N=\mathbb Z^n/\mathbb Z(1,\ldots,1)\), and its character lattice is \(M=\{u\in\mathbb Z^n:\sum_i u_i=0\}\). Normal fans and toric varieties are taken with their usual *outward* normal convention. The field is algebraically closed of arbitrary characteristic. The named transverse affine models are valid at generic points of the corresponding torus orbits and, by toric product structure, at generic points of their closures. No assertion about the scheme structure of the nonreduced singular locus or the analytic type at intersections of distinct components is made.

## Proof
**1. Polytope and facet data.** The convex hull of the integer vertices \(\mathbf1_T\), with \(|T|=r\) and \(T\ne H\), is
\[
 P=\left\{x\in[0,1]^n:\sum_{i=1}^n x_i=r,\quad\sum_{h\in H}x_h\le r-1\right\}.
\]
The cutting hyperplane is integral and passes through the \(rs\) neighbors of \(\mathbf1_H\) in the hypersimplex; no new fractional vertices arise. Equivalently, any one-dimensional edge of the hypersimplex changes exactly one selected coordinate into one unselected coordinate, so the deleted vertex has precisely these \(rs\) neighbors and the truncating inequality is a supporting hyperplane through them. For \(r,s\ge3\), all original \(2n\) coordinate inequalities remain facets, and the new inequality is a facet. Thus their primitive outward normal rays in \(N\) are \(\pm[e_i]\), plus \([e_H]\) with \(e_H=\sum_{h\in H}e_h\). Coordinate facet persistence follows by fixing any chosen coordinate to zero or one and varying other bases away from the excluded \(H\); each resulting face has affine dimension \(n-2\).

**2. The new facet and its faces.** Let \(C=P\cap\{\sum_Hx_h=r-1\}\). Its vertices are indexed by \((h,j)\in H\times O\), representing \(T_{h,j}=(H\setminus\{h\})\cup\{j\}\). Its affine coordinates satisfy \(\sum_{h\in H}(1-x_h)=1\) and \(\sum_{j\in O}x_j=1\); hence
\[
 C\cong\Delta_{r-1}\times\Delta_{s-1}.
\]
Every nonempty face of \(C\) is \(F_{I,J}\cong\Delta_{|I|-1}\times\Delta_{|J|-1}\), indexed by nonempty \(I\subseteq H\), \(J\subseteq O\); its vertices are \(T_{h,j}\) for \(h\in I,j\in J\). Such a face has dimension \(|I|+|J|-2\). Besides the new-facet normal, the coordinate normals active on it are \(+e_i\) for \(i\in H\setminus I\), \(-e_j\) for \(j\in O\setminus J\), together with \(-e_h\) when \(I=\{h\}\) and \(+e_j\) when \(J=\{j\}\). This list is exact: on a product of two nontrivial simplices, none of the remaining coordinates is constant.

If \(|I|,|J|\ge2\), the number of these rays is \(n-|I|-|J|+1\), equal to the codimension of \(F_{I,J}\). They are an integral lattice basis for their saturated span: all coordinate normals are distinct signed classes, and \(e_H\) completes their independent list with a unit minor (one coordinate from each nontrivial factor may be eliminated along with the diagonal relation). Hence these cones are smooth. Conversely, when \(I=\{h\}\), the cone contains all three sets \(\{+e_i:i\in H\setminus\{h\}\}\), \(\{-e_h\}\), and \(\{e_H\}\) with the positive relation
\[
 [e_H]+[-e_h]=\sum_{i\in H\setminus\{h\}}[e_i],
\]
which involves \(r+1\) distinct extreme rays in a rank-\(r\) subcone. Thus the cone is nonsimplicial; the remaining active outside-coordinate rays are independent smooth factors. The symmetric statement holds when \(J=\{j\}\). Therefore the nonsmooth faces contained in \(C\) are precisely those with \(|I|=1\) **or** \(|J|=1\). Their maximal members under face inclusion are \(F_{\{h\},O}\) and \(F_{H,\{j\}}\).

**3. Faces not contained in the new facet.** Such a face has no new-facet normal. Its normal cone is generated by a subset of coordinate rays \(\pm[e_i]\). If the face has positive dimension, at least two coordinates vary, so at most \(n-2\) coordinate hyperplanes can be simultaneously active; the resulting primitive normals are a subset of an integral basis for their span and are independent. Thus all such positive-dimensional faces are smooth. At any vertex indexed by a basis \(T\) with \(T\notin C\), all \(n\) coordinate inequalities are active. They give \(n\) extreme rays in dimension \(n-1\), hence are nonsimplicial. These are exactly the vertices with \(|T\cap H|\le r-2\), in number \(\binom nr-1-rs\). Their singular orbits are closed points, not contained in any positive-dimensional singular stratum.

**4. Components, incidence and orbit closures.** For a face \(F\subseteq P\), write \(V(F)\) for the closure in \(X\) of the orbit associated to its normal cone. Inclusion of such orbit closures reverses inclusion of faces: \(V(F_1)\subseteq V(F_2)\) iff \(F_1\subseteq F_2\). Smoothness is invariant along torus orbits, and singular support is a closed torus-invariant union of orbit closures. By steps 2--3, its maximal irreducible components are precisely \(V(F_{\{h\},O})\), \(V(F_{H,\{j\}})\), and the closed points indexed by bases not in \(C\). The faces \(F_{\{h\},O}\) and \(F_{H,\{j\}}\) are standard integral simplices, with smooth simplex normal fans in the quotient lattice; hence their orbit closures are respectively \(\mathbb P^{s-1}\) and \(\mathbb P^{r-1}\). Two distinct first-family faces have no common vertex, likewise for the second family; a first and a second meet in exactly \(T_{h,j}\). This proves the stated intersection pattern and component count. Codimensions equal the dimensions of their normal cones, namely \(r\) and \(s\).

**5. Affine transverse models and multiplicities.** At the generic orbit of \(F_{\{h\},O}\), its transverse normal cone is the rank-\(r\) cone with primitive rays \(e_i\) for \(i\in H\setminus\{h\}\), \(-e_h\), and \(e_H\). Its dual semigroup, in integral coordinates \(a_i=u_i\ge0\) for \(i\ne h\) and \(b=-u_h\ge0\), is
\[
 \left\{(a_1,\ldots,a_{r-1},b)\in\mathbb Z_{\ge0}^{r}:\ b\le\sum_i a_i\right\}.
\]
It is generated by the \(2(r-1)\) lattice vectors \((e_i,0)\) and \((e_i,1)\). The sole defining toric ideal of these generators is the ideal of all \(2\times2\) minors of a generic \(2\times(r-1)\) matrix (any two factorizations correspond to rearranging which factors carry the last coordinate). This is the normal affine cone over \(\mathbb P^1\times\mathbb P^{r-2}\). The opposite-family computation exchanges \(r\) and \(s\). The multiplicity of the rank-one \(a\times b\) determinantal cone is its projective degree \(\binom{a+b-2}{a-1}\), so the two cases have multiplicities \(r-1\) and \(s-1\).

At an old vertex \(T\notin C\), the character semigroup of its normal cone is
\[
 \{u\in\mathbb Z^n:\sum u_i=0,\ u_i\ge0\ (i\in T),\ u_j\le0\ (j\notin T)\}.
\]
Every such \(u\) decomposes into nonnegative elementary transfers \(e_i-e_j\), for \(i\in T\), \(j\notin T\). Their toric ideal consists of all \(2\times2\) minors of a generic \(r\times s\) matrix, giving the claimed affine chart and multiplicity \(\binom{r+s-2}{r-1}\). Every these three determinantal cones is nonsimplicial since both matrix dimensions are at least two (indeed at least two-by-two and, for old vertices, at least three-by-three). The positive-dimensional cone check showed the other cones are unimodular whenever simplicial. Thus the singular and non-\(\mathbb Q\)-factorial supports coincide, and every fixed point is singular.

## Verification
Run `python3 CHECKER.py` with SymPy available. The checker derives vertices and the \(2n+1\) claimed facets, enumerates every nonempty polytope face as an intersection of facet-vertex sets, computes face ranks and signed primitive outward active normal rays, and checks smoothness by Smith normal form when simplicial. It independently compares every nonsmooth face with the proposed component faces. The exhaustively checked pairs \((n,r)\) are \((6,3)\), \((7,3)\), \((7,4)\), \((8,3)\), and \((8,4)\); output terminates `VERIFY_OK`. This is a finite sanity check, not a substitute for the all-parameter proof in steps 1--5. The semigroup-generation and determinantal ideal arguments are symbolic and do not require a checker.

## Relationship to prior work
This object is the unique-circuit-hyperplane sparse-paving matroid, equivalently the one-vertex-deleted hypersimplex or an elementary split matroid polytope. Ardila--Benedetti--Doker treat matroid polytope volume and Grassmannian torus-orbit degree, not singular-support decomposition. Chatelain--Ramírez Alfonsín study matroid base-polytope decomposition and faces; Bonin describes sparse paving circuit-hyperplanes. Ferroni--Schröter's work on face enumeration for split matroid polytopes explicitly includes this same one-missing-basis example (\(r=3,n=6\)) and determines its face vector, but face numbers do not imply the classification of singular orbit closures, incidence of irreducible components, or generic determinantal analytic models. Lasoń--Michałek discuss global algebraic and Gorenstein properties of matroid polytopes, not the stated local models. No claim is made that the polytope description, facet enumeration, toric orbit-face correspondence, or determinantal ideals themselves are new. The proposed contribution is their complete geometric assembly for this specific family, including the precise singular components, intersections and transverse types.

## Limitations
Only the *reduced* singular support is classified. Singular scheme multiplicities and local analytic types at the \(rs\) intersections of positive-dimensional components are not determined. Originality is based on the inspected accessible literature and searches; unindexed or differently phrased earlier classifications remain possible. The explicit formulas are restricted to \(r,s\ge3\) and are not asserted for low rank/corank. Independent validation has not been performed.

## References
- F. Ardila, C. Benedetti, J. Doker, “Matroid polytopes and their volumes,” arXiv:0810.3947, initial public version 2008-10-22, https://arxiv.org/abs/0810.3947.
- V. Chatelain, J. L. Ramírez Alfonsín, “Matroid base polytope decomposition,” arXiv:0909.0840, https://arxiv.org/abs/0909.0840.
- J. Bonin, “Sparse paving matroids, basis-exchange properties, and cyclic flats,” arXiv:1011.1010, https://arxiv.org/abs/1011.1010.
- L. Ferroni and B. Schröter, “Face enumeration for split matroid polytopes,” Combinatorics, Probability and Computing, https://www.cambridge.org/core/journals/combinatorics-probability-and-computing/article/face-enumeration-for-split-matroid-polytopes/8AB800A4A0AAB1AEF4720C07899107AF.
- M. Lasoń and M. Michałek, “On algebraic properties of matroid polytopes,” arXiv:2005.08359, https://arxiv.org/abs/2005.08359.
