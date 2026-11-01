# Coordinate-swap fixed Vietoris–Rips complexes of torus grids form annuli

## Finding
For every integer \(n\ge 7\), let \(T_n=(\mathbb Z/n\mathbb Z)^2\) carry the shortest-path \(\ell^1\) torus metric, and let \(\tau(i,j)=(j,i)\). With \(K_{n,r}=\operatorname{VR}_{\le r}(T_n)\), define the **geometric**, rather than vertexwise, fixed locus \(F_{n,r}=|K_{n,r}|^{\langle\tau\rangle}\). Then
\[
F_{n,r}\cong\bigsqcup_{i=0}^{n-1}\{\mathrm{pt}\}\quad(0\le r<2),
\qquad
F_{n,2}\cong_{\mathrm{PL}} S^1\times[0,1].
\]
In particular, the scale-two fixed-point space is an annulus with exactly \(2n\) vertices, \(4n\) edges, and \(2n\) triangles in a canonical triangulation. Its integral homology is \(H_0\cong\mathbb Z\), \(H_1\cong\mathbb Z\), and zero in every higher degree. The inclusion from every \(0\le r<2\) induces a rank-one map on degree-zero homology and the zero map into degree-one homology; the circle appears precisely at the scale-two threshold. This statement does not determine behavior for \(r>2\).

## Assumptions and scope
Write \(\delta_n(a,b)=\min\{|a-b|,n-|a-b|\}\) after choosing representatives \(0,\ldots,n-1\), and \(d((a,b),(c,d))=\delta_n(a,c)+\delta_n(b,d)\). A simplex of \(K_{n,r}\) is a nonempty subset of pairwise distances at most \(r\). The coordinate swap \(\tau\) is a simplicial involution; \(F_{n,r}\) consists of all fixed geometric points in the usual affine realization. The conclusion concerns all integers \(n\ge7\), all real \(r\in[0,2]\), and the integral homology of the scale-two fixed locus.

## Proof
**Orbit-barycenter lemma.** For any simplicial involution acting by vertex permutations, a geometric point is fixed exactly when, on its unique supporting simplex, the barycentric weights are constant on each vertex orbit. Hence the fixed set is canonically PL-homeomorphic to the simplicial complex with one vertex for every admissible vertex orbit (an orbit whose union is a simplex), and with a face whenever the union of its orbits is a simplex. This is a genuine triangulation of the fixed set, not the subcomplex spanned by individually fixed original vertices.

The singleton orbits of \(\tau\) are \(D_i=\{(i,i)\}\). A two-vertex orbit \(\{(i,j),(j,i)\}\) has intrapair distance \(2\delta_n(i,j)\). Thus when \(0\le r<2\), no two-vertex orbit is admissible, and distinct \(D_i,D_j\) have distance \(2\delta_n(i,j)\ge2>r\). The fixed locus is precisely the stated discrete collection of \(n\) points.

At \(r=2\), the admissible nonsingleton orbits are exactly \(E_i=\{(i,i+1),(i+1,i)\}\), with indices modulo \(n\). Because Vietoris–Rips complexes are flag, an edge between two orbit-vertices exists precisely when all cross-distances between the corresponding original vertices are at most two. The distances give the following **complete** adjacency relations:
\[
D_i\!\sim D_j\iff j=i\pm1,\qquad
E_i\!\sim E_j\iff j=i\pm1,\qquad
D_i\!\sim E_j\iff j\in\{i,i-1\}.
\]
Indeed, \(d((i,i),(j,j))=2\delta_n(i,j)\), and the cross-distance from \((i,i)\) to either member of \(E_j\) equals \(\delta_n(i,j)+\delta_n(i,j+1)\). For two distinct \(E\)-orbits, comparing the same-orientation members first forces \(\delta_n(i,j)\le1\); for their two adjacent possibilities, the reversed cross-distances equal two, so these are all the edges. The bound \(n\ge7\) rules out identifications among the cyclic neighbors used here.

The only three-vertex cliques are
\[
\{D_i,D_{i+1},E_i\},\qquad \{D_{i+1},E_i,E_{i+1}\},\qquad i\in\mathbb Z/n\mathbb Z.
\]
There are no four-vertex cliques: every triangle has no common neighbor outside its three vertices, as follows directly from the adjacency list. These \(2n\) triangles subdivide the rectangular cells between two cyclic length-\(n\) vertex rings: map \(D_i\) to \((i,0)\) and \(E_i\) to \((i,1)\) in \((\mathbb R/n\mathbb Z)\times[0,1]\), and linearly extend over the two triangles in each unit strip. This is a bijective PL map onto the annulus. The boundary rings are \(D_0D_1\cdots D_{n-1}D_0\) and \(E_0E_1\cdots E_{n-1}E_0\). The asserted integral homology and degree-zero inclusion rank follow immediately; there are no positive-dimensional source classes before scale two.

## Verification
Run `python3 verify.py`. This standalone program enumerates all original vertex-orbits and their diameter conditions, independently constructs the exact compatibility graph and its three- and four-cliques, and checks the displayed orbit types, complete edge and triangle lists, and absence of four-cliques for every integer \(7\le n\le25\) at scales one and two. It performs thirty-eight finite parameter checks. The infinite-family proof above relies on the distance inequalities and is not inferred from this finite range.

## Relationship to prior work
Adams, Adetowubo, Barriga-Acosta, Feng and Sterling (2025) investigate the same graph-metric torus grids and establish nonequivariant homotopy types of their Vietoris–Rips complexes, including the torus homotopy type at scale two for \(n\ge7\). Their results do not, as stated in the examined sections, identify the actual coordinate-swap fixed-point locus. A later thesis by Sterling gives further nonequivariant calculations. A prior classification of **rectangular** scale-two torus-grid complexes likewise gives nonequivariant homotopy but does not imply this fixed-space PL type. The annular locus has boundary, whereas the ambient scale-two complex has torus homotopy type; ordinary homotopy type alone cannot determine fixed-point spaces.

## Limitations
Only the specified coordinate-transposition action and real scales \(0\le r\le2\) are treated; the complete equivariant homotopy type, other involutions, and persistence beyond scale two are not determined. A search does not exclude unindexed equivalent research. The cited primary article was read in its public full-text HTML, and relevant thesis portions were inspected; originality remains a literature-based assessment rather than an independence guarantee. Finite enumeration supplements, but does not replace, the all-\(n\) proof.

## References
1. H. Adams, A. Y. Adetowubo, H. Barriga-Acosta, Z. Feng, J. Sterling, *Vietoris–Rips complexes of torus grids*, arXiv:2502.07134v1, publicly posted 2025-02-10. https://arxiv.org/html/2502.07134v1
2. J. Sterling, *Vietoris–Rips Complexes of Torus Grids*, Master's thesis, Auburn University, 2025. https://etd.auburn.edu/handle/10415/9659
