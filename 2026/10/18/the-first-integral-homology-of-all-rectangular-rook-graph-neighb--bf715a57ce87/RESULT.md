# The first integral homology of all rectangular rook-graph neighborhood complexes

## Finding
Let \(m,n\ge3\) be integers and let \(R_{m,n}=K_m\square K_n=L(K_{m,n})\), the rook graph on \([m]\times[n]\). For the **open** Lovász neighborhood complex \(K=\mathcal N(R_{m,n})\), the complete first integral homology is
\[
H_1(K;\mathbb Z)\cong
\begin{cases}
\mathbb Z^2,&m=n=3,\\
\mathbb Z,&\min(m,n)=3<\max(m,n),\\
\mathbb Z/2\mathbb Z,&m,n\ge4.
\end{cases}
\]
In particular, order-two torsion occurs **if and only if both side lengths are at least four**. The theorem concerns the first homology of the full neighborhood complex for every pair of parameters, not its higher homology or complete homotopy type.

## Assumptions and scope
The vertices of \(R_{m,n}\) are cells \((i,j)\), with distinct cells adjacent exactly when they share one coordinate. The *open* neighborhood \(N(i,j)\) comprises every other cell in row \(i\) together with every other cell in column \(j\). The simplices of \(K\) are precisely the subsets of some \(N(i,j)\). All cohomology below is simplicial cohomology; arbitrary abelian coefficient groups \(A\) are allowed, with no restriction on torsion or divisibility. We use oriented 1-cochains \(u(x,y)=-u(y,x)\); a cocycle obeys \(u(x,y)+u(y,z)+u(z,x)=0\) on each triangular face.

## Proof
**1. Normalization.** Any two distinct cells \(x,y\) have a common neighbor in \(R_{m,n}\): for cells in the same row/column use a third cell on that line, and otherwise use an opposite rectangle corner. Thus the 1-skeleton of \(K\) is complete and \(K\) is connected. Fix \(o=(1,1)\). Subtracting a unique coboundary with value zero at \(o\), every cocycle has a unique normalized representative satisfying \(u(o,x)=0\) for all \(x\ne o\). Consequently \(H^1(K;A)\) is exactly the group of normalized cocycles.

Write \(a_j=(1,j)\), \(b_i=(i,1)\), \(c_{ij}=(i,j)\) for \(i,j\ge2\). Put
\[
t_{ij}=u(a_j,b_i),\qquad p_{j\ell}=u(a_j,a_\ell)\ (j<\ell),\qquad q_{ik}=u(b_i,b_k)\ (i<k).
\]

**2. Triangle relations.** A triangular face is exactly a triple lying in one open neighborhood \(N(r,c)\), which is the union of two disjoint legs: row \(r\) except column \(c\), and column \(c\) except row \(r\). The triangles through \(o\) show that \(p_{j\ell}=0\) whenever \(n\ge4\), and \(q_{ik}=0\) whenever \(m\ge4\). (A triple consisting of all three cells of a three-cell row or column is **not** a face.) They also imply
\[
 u(a_j,c_{i\ell})=0\ (j\ne\ell),\quad
 u(b_i,c_{k\ell})=0\ (i\ne k),\quad
 u(c_{ij},c_{k\ell})=0\ (i=k\text{ or }j=\ell).
\]
Triangles \(\{a_j,a_\ell,b_i\}\) and \(\{a_j,b_i,b_k\}\) respectively give, for increasing indices,
\[
t_{ij}-t_{i\ell}=p_{j\ell},\qquad t_{kj}-t_{ij}=q_{ik}.
\tag{1}
\]
For \(k\ne i\) and \(h\ne j\), mixed triangles \(\{a_j,b_k,c_{ij}\}\) and \(\{a_h,b_i,c_{ij}\}\) give
\[
 u(a_j,c_{ij})=t_{kj},\qquad u(b_i,c_{ij})=-t_{ih}.
\tag{2}
\]
The left sides do not depend on the choices of \(k\) and \(h\), respectively; this is an additional equality whenever more than one choice exists. Finally, for \(i\ne k\), \(j\ne\ell\), triangles using \(a_j\) and \(a_\ell\), respectively, show
\[
 u(c_{ij},c_{k\ell})=-t_{kj}=t_{i\ell},\qquad t_{kj}+t_{i\ell}=0.
\tag{3}
\]
Every edge joins one of the four vertex types \(o,a,b,c\). Equations (1)–(3), antisymmetry, and normalization determine every value of \(u\). Thus they give an *upper bound* on normalized cocycles; we establish realization next, not merely count formal parameters.

**3. Both dimensions at least four.** Here \(p=q=0\). By (1) all \(t_{ij}\) equal a single \(t\in A\), and (3) imposes \(2t=0\). Conversely for every element \(t\in A\) with \(2t=0\), assign value \(t\) to an oriented edge when its endpoints differ in **both** coordinates, and zero otherwise. Since \(-t=t\), this is alternating. Every triangular face lies in a neighborhood with two coordinate legs; it has either zero or two cross-leg edges. Its cocycle sum is therefore zero. The normalized parameter \(t\) is attained, so \(H^1(K;A)\cong A[2]\), where \(A[2]=\{a\in A:2a=0\}\).

**4. Exactly three rows.** Suppose \(m=3\) and \(n\ge4\), the transposed situation being symmetric. Equation (1) gives \(t_{2j}=t\) and \(t_{3j}=t+s\) for all \(j\ge2\), where \(s=q_{23}\). Equation (3) forces \(2t+s=0\), so there is at most one free parameter \(t\in A\). Every such \(t\) is realized by the following explicit alternating cocycle. All edges at \(o\) and all edges between two \(a\)'s have value zero. With \(\alpha_2=t\) and \(\alpha_3=-t\), put
\[
\begin{aligned}
 u(b_2,b_3)&=-2t,&u(a_j,b_i)&=\alpha_i,\\
 u(a_j,c_{i\ell})&=-\alpha_i\,[j=\ell],&
 u(b_i,c_{k\ell})&=-\alpha_i\,[i=k],\\
 u(c_{2j},c_{3\ell})&=t\,[j\ne\ell].
\end{aligned}
\]
Here \([P]\) denotes one or zero according as \(P\) is true or false. Values between two \(c\)'s sharing a row or column are zero, and reverse orientations carry the negative value. One verifies the cocycle identity **on every neighborhood simplex** by grouping its three vertices according to the two coordinate legs; a triangle in a single leg or of type two-plus-one gives zero in the above formulas. In particular, no nonexistent full-three-cell-column triangle is imposed. Thus \(H^1(K;A)\cong A\), for all \(A\).

**5. The three-by-three board.** Both \(p=p_{23}\) and \(s=q_{23}\) may now be nonzero. Equations (1)–(3) give \(p=2t+s\) and
\[
(t_{ij})_{i,j=2,3}=
\begin{pmatrix}t&-t-s\\t+s&-t\end{pmatrix},\qquad t,s\in A.
\]
Again these constraints are sufficient. Set the values on \(o\)-edges to zero, \(u(a_2,a_3)=2t+s\), \(u(b_2,b_3)=s\), and \(u(a_j,b_i)=t_{ij}\). For \(i,j,\ell,k\in\{2,3\}\), set
\[
\begin{aligned}
 u(a_j,c_{i\ell})&=[j=\ell]t_{(5-i),j},\\
 u(b_i,c_{k\ell})&=-[i=k]t_{i,(5-\ell)},\\
 u(c_{2j},c_{3\ell})&=-[j\ne\ell]t_{3j},
\end{aligned}
\]
with zero values for same-row/same-column \(c\)-edges and negative values on reversed edges. Direct substitution into the nine neighborhood four-vertex simplices checks all their triangular faces for every \(t,s\in A\); the 36 triangle identities involve only integer-linear cancellations, so this works for arbitrary abelian \(A\). Therefore \(H^1(K;A)\cong A^2\).

**6. Integral homology.** The integral universal coefficient theorem for a connected complex gives a natural isomorphism
\[
H^1(K;A)\cong\operatorname{Hom}(H_1(K;\mathbb Z),A).
\]
All chain groups are finitely generated because \(K\) is finite. The three coefficient-functor descriptions \(A^2\), \(A\), and \(A[2]\) for **every** abelian \(A\) imply, respectively, \(H_1\cong\mathbb Z^2\), \(H_1\cong\mathbb Z\), and \(H_1\cong\mathbb Z/2\mathbb Z\). This proves the stated classification over the integers, without inferring torsion information merely from a finite selection of fields.

## Verification
The accompanying executable `verify_rook_h1.py` uses only the Python 3 standard library. It generates all neighborhoods, checks the complete 1-skeleton, enumerates all triangles, verifies the explicit integer cocycle generators for three-row cases and the mod-two generator for boards with both dimensions at least four, and computes first cohomology dimensions over \(\mathbb F_2,\mathbb F_3,\mathbb F_5\) by exact elimination. It checks boards \((3,3),(3,4),(3,5),(3,6),(4,4),(4,5),(5,5)\), reproducing `verification_output.txt`. Run `python3 verify_rook_h1.py`. The optional `integer_smith_check.py` (using SymPy) independently reconstructs the normalized triangle-relation lattice and checks exact invariant factors for \((3,3),(3,4),(4,4)\), respectively two free factors, one free factor, and one factor of order two (`smith_output.txt`). These computations are finite consistency checks; **the all-parameter conclusion rests on the preceding symbolic proof**.

## Relationship to prior work
Shukla's work [1] develops the same open-neighborhood functor but treats graphs of maximum degree at most three and certain four-regular circulants; it does not imply this arbitrary rectangular rook-graph classification. Matsushita's fundamental-group work [2] gives a general correspondence, not the explicit first integral homology of the entire rook family. A closely related calculation [3] fully determines the first homology for the single four-by-four rook graph (including its order-two torsion); the present theorem subsumes that **known case**, and adds the natural all-parameter torsion threshold and the low-width free cases. Another exact-family result [4] computes the rook neighborhood *cofiber over its row-column core* and higher integral homology for degrees at least three, expressly leaving \(H_1\) unresolved. The two-row family [5] has a distinct wedge classification, outside the hypotheses \(m,n\ge3\). Results on **closed** neighborhood complexes, 3-cut complexes and clique complexes concern different simplices and do not supply the present result.

## Limitations
The conclusion determines first **abelianized** homology only; it does not identify the fundamental group, higher homology, a full homotopy type, or natural maps between different board sizes. The proof is valid for all integer \(m,n\ge3\); boards with one or two rows lie outside this classification. Finite computations cannot replace the symbolic all-coefficient argument. As with any literature search, unindexed equivalent results or reductions not identified in the checked publications remain a residual originality risk.

## References
[1] S. Shukla, *Homotopy type of the neighborhood complexes of graphs of maximal degree at most 3 and 4-regular circulant graphs*, arXiv:1802.04526, first posted 2018-02-13; *Electronic Journal of Combinatorics* 26(2) (2019), P2.4.

[2] T. Matsushita, *Fundamental Groups of Neighborhood Complexes*, arXiv:1210.2803 (first posted 2012-10-10), *Journal of Mathematical Sciences, University of Tokyo* 24 (2017), 321–353.

[3] *Integral homology of the rook-graph neighborhood complex*, public mathematical result record `2026/10/11/SCOPE-integral-homology-of-the-rook-graph-neighborhood-complex--00c7d8853dcb`; exact four-by-four integral calculation.

[4] *Row–column boundary spheres control higher neighborhood homology of rook graphs*, public mathematical result record `2026/10/11/SCOPE-row-column-boundary-spheres-control-higher-neighborhood-homology--f09a20a3ee45`; cofiber and high-degree comparison.

[5] *Neighborhood complexes of two-row rook graphs split into two spheres and a crown suspension*, public mathematical result record `2026/10/11/SCOPE-neighborhood-complexes-of-two-row-rook-graphs-split-into-two-sph--9b16e10ce620`; separate width-two classification.
