# Row–column boundary spheres control higher neighborhood homology of rook graphs

## Finding
For integers \(m,n\ge3\), let \(R_{m,n}=K_m\square K_n=L(K_{m,n})\) be the rook graph on \([m]\times[n]\): distinct cells are adjacent exactly when they share a row or a column. Let \(K=\mathcal N(R_{m,n})\) be the **open** Lovász neighborhood complex. Thus a nonempty set \(\sigma\) is a simplex if and only if there is a vertex \(c\notin\sigma\) adjacent to every member of \(\sigma\).

Let \(K_0\) be the subcomplex consisting of all vertices and edges and all **proper** faces of each full row simplex and full column simplex. The complete 1-skeleton is indeed contained in \(K\), and the full rows and columns are not. The quotient admits the explicit homotopy classification
\[
K/K_0\simeq\bigvee^{\,mn((m-1)(n-1)-1)}S^2.\tag{1}
\]
For every integer \(k\ge3\), \(\widetilde H_k(K_0;\mathbb Z)\to\widetilde H_k(K;\mathbb Z)\) is an isomorphism. The induced action of row and column permutations is
\[
\widetilde H_k(K;\mathbb Z)\cong
\left(\mathbb Z^m_{\mathrm{perm}}\otimes\operatorname{sgn}_{S_n}\right)^{[k=n-2]}
\oplus
\left(\operatorname{sgn}_{S_m}\otimes\mathbb Z^n_{\mathrm{perm}}\right)^{[k=m-2]},
\quad k\ge3.\tag{2}
\]
A summand with a false condition in brackets is defined to be zero. The first permutation lattice is the row-indexed free abelian group, and the second is its column-indexed analogue. In particular all integral homology above dimension two is free. If both dimensions coincide and are at least three, the rank is \(m+n\); otherwise the two potentially nonzero ranks are \(m\) in dimension \(n-2\) and \(n\) in dimension \(m-2\), subject to the degree restriction.

## Assumptions and scope
Both dimensions are at least three; no assumption of equality or primality is made. Edges of \(R_{m,n}\) connect distinct cells sharing **one coordinate**. The *open* neighborhood of \((i,j)\) is
\[
 N(i,j)=A_{ij}\sqcup B_{ij},\quad
 A_{ij}=\{(i,t):t\ne j\},\quad B_{ij}=\{(s,j):s\ne i\}.
\]
These sets have sizes \(n-1\) and \(m-1\). The complex is the union of the closed simplices \(\Delta N(i,j)\) over all cell centers. The notation \(K/K_0\) denotes the geometric realization of the quotient of these finite CW complexes (equivalently the homotopy cofiber of the simplicial inclusion).

## Proof
**1. Pure and mixed faces.** Every proper row subset is witnessed by an omitted cell of that row; the full row has no common neighbor, since a vertex outside the row can be adjacent to at most one of its cells and a vertex inside the row cannot be adjacent to itself. The corresponding assertion holds for columns. Every unordered pair is witnessed: two cells sharing a row (respectively column) have a third cell in that row (respectively column) as a common neighbor; cells in different rows and columns have either opposite corner as a common neighbor. Thus the full 1-skeleton is in \(K\).

Call a face *mixed* if it has at least three cells and is contained neither in a single row nor in a single column. Each such face has precisely one common neighbor. To see this, its first common neighbor \((i,j)\) forces the face into \(A_{ij}\sqcup B_{ij}\). It must meet both legs, and since it has at least three cells, one leg contains at least two. Two cells on the horizontal leg identify \(i\) and one on the vertical leg identifies \(j\); the other case is symmetric. Hence \((i,j)\) is determined. This proves that the distinct center simplices \(\Delta N(i,j)\) meet one another only within \(K_0\), once pure faces and edges are removed.

**2. The common attaching complex.** Fix a center \((i,j)\) and let \(J_{ij}=\Delta N(i,j)\cap K_0\). The only faces in \(J_{ij}\) are the faces of the two simplices \(\Delta A_{ij}\) and \(\Delta B_{ij}\), and every cross edge between a vertex of \(A_{ij}\) and a vertex of \(B_{ij}\). There are no mixed triangles in \(J_{ij}\). Contract the two disjoint, nonempty simplex subcomplexes to distinct points; these contractions are homotopy equivalences of the ambient attaching complex, and the \((m-1)(n-1)\) cross edges become parallel edges between the resulting points. Therefore
\[
J_{ij}\simeq\bigvee^{(m-1)(n-1)-1}S^1.
\]
The containing simplex \(\Delta N(i,j)\) is contractible, so its homotopy cofiber along \(J_{ij}\hookrightarrow\Delta N(i,j)\) is \(\Sigma J_{ij}\), a wedge of \((m-1)(n-1)-1\) two-spheres.

**3. The global quotient.** Each non-core face belongs to a unique center simplex by Step 1. Consequently, after identifying \(K_0\) to one point, the \(mn\) contractible center simplices attach independently: there is a homeomorphism of quotient CW spaces
\[
K/K_0\cong \bigvee_{(i,j)\in[m]\times[n]}
\bigl(\Delta N(i,j)/J_{ij}\bigr).
\]
Applying Step 2 yields equation (1). Because \(\widetilde H_k(K/K_0;\mathbb Z)=0\) for all \(k\ge3\) and also for all \(k\ge4\), the long exact relative homology sequence gives \(\widetilde H_k(K_0;\mathbb Z)\cong\widetilde H_k(K;\mathbb Z)\) for each \(k\ge3\).

**4. Integral classes and symmetry.** Every simplex of \(K_0\) of dimension at least two lies in exactly one row or one column. Thus, in chain degrees at least two, the corresponding simplicial chain groups split as direct sums of those of the row and column boundaries. Their boundary maps in degrees at least three have no mixed terms. For a row boundary \(\partial\Delta^{n-1}\), the unique top reduced homology group is \(\mathbb Z\) in degree \(n-2\). The same reasoning gives one \(\mathbb Z\) in degree \(m-2\) per column; when these dimensions are at least three there can be no interaction through the shared graph 1-skeleton. This gives the integral groups in (2).

A permutation of the \(n\) columns preserves each row but permutes its vertices, acting on its oriented boundary sphere by the permutation sign. Simultaneously, it permutes column boundaries without additional sign. A permutation of the \(m\) rows has the symmetric effect: it permutes row boundaries and acts by sign on each column boundary. These actions commute. The inclusion is equivariant, so (2) follows as an isomorphism of integral \(\mathbb Z[S_m\times S_n]\)-modules.

## Verification
The standalone standard-library script `verify_rook.py` reconstructs the **open** neighborhoods, generates every simplex of \(K\) and \(K_0\), checks uniqueness of each mixed-face center, checks the full edge skeleton and \(J_{ij}\) structure, checks the relative Euler characteristic, computes exact binary boundary ranks, compares high-dimensional Betti numbers for both complexes, and verifies the signed action of adjacent transpositions on explicit integral oriented row and column boundary cycles. Tested arrays are \((3,3),(3,4),(3,5),(3,6),(4,4),(4,5),(5,5),(5,6)\); their printed evidence is in `verification_output.txt`. For example, the \(5\)-by-\(5\) array has reduced third Betti number \(10\), and the \(5\)-by-\(6\) array has ranks \(6\) and \(5\) in degrees \(3\) and \(4\). The symbolic argument above, not these finite calculations, proves the general parameter statement.

## Relationship to prior work
Matsushita's work on fundamental groups of **open** neighborhood complexes [1] supplies the topological graph-complex setting but does not classify the higher integral homology of rook graphs. Shukla's calculations [2] concern graphs of maximum degree at most three and selected four-regular circulants; they do not give the all-parameter statement (1)–(2). The closest exact-graph calculation is Matsushita [3, Example 3.5], which proves a wedge-of-two-spheres formula for the **closed** neighborhood complex of the same rook graphs. Closed neighborhoods include their center, and that complex is mathematically distinct: [3] has no higher homology, whereas (2) gives, for example, nonzero degree-three homology on the \(5\)-by-\(5\) rook graph. The independence-complex calculation of Antolín Camarena–Carnero Bravo [4] is used in [3] to analyze the closed version; it does not establish (1)–(2) for the open complex.

## Limitations
This determines the homotopy cofiber of a natural subcomplex and all integral homology in degrees at least three, **not** the full homotopy type or the first and second homology of \(\mathcal N(R_{m,n})\). The formula for the relative quotient is non-equivariant; no equivariant splitting of that quotient is asserted. Computational examples are consistency checks only. The comparisons above do not eliminate the possibility that an earlier unindexed work contains an equivalent open-neighborhood statement.

## References
[1] T. Matsushita, *Fundamental Groups of Neighborhood Complexes*, first public arXiv version 2012-10-10, arXiv:1210.2803; *J. Math. Sci. Univ. Tokyo* **24** (2017), 321–353. Primary MSC 55Q05.

[2] A. Shukla, *Homotopy type of the neighborhood complexes of graphs of maximal degree at most 3 and 4-regular circulant graphs*, first public arXiv version 2018-02-13, arXiv:1802.04526.

[3] T. Matsushita, *Closed neighborhood complexes of graphs*, first public arXiv version 2025-11-16, arXiv:2511.12608, especially Example 3.5 and the distinction between open and closed neighborhoods.

[4] O. Antolín Camarena and M. Carnero Bravo, *Homotopy type of the independence complex of some categorical products of graphs*, first public arXiv version 2023-07-23, arXiv:2307.12401.
