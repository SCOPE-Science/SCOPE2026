# Universal first-homology two-torsion in rook-graph neighborhood complexes

## Finding
For all integers \(m,n\ge4\), let \(R_{m,n}=K_m\square K_n=L(K_{m,n})\) be the rook graph on \([m]\times[n]\), and let \(\mathcal N(R_{m,n})\) be the **open** Lovász neighborhood complex. Then
\[
\boxed{H_1(\mathcal N(R_{m,n});\mathbb Z)\cong\mathbb Z/2\mathbb Z.}
\]
More constructively, for **every** abelian coefficient group \(A\), its first simplicial cohomology is naturally isomorphic to the subgroup \(A[2]=\{a\in A:2a=0\}\). A class \(a\in A[2]\) is represented by the cochain that assigns \(a\) to an oriented edge between cells in distinct rows and distinct columns, and assigns zero to a same-row or same-column edge (antisymmetry is valid because \(a=-a\)). Thus each complex has genuine integral two-torsion and is not homotopy equivalent to a wedge of spheres. The case \((m,n)=(4,4)\) was already known; the all-parameter conclusion is the extension.

## Assumptions and scope
The graph has a vertex for each grid cell \((i,j)\). Distinct cells are adjacent in \(R_{m,n}\) exactly when they share a row or column. The open neighborhood of \((i,j)\) is
\[
S_{ij}=\{(i,t):t\ne j\}\cup\{(s,j):s\ne i\}.
\]
A finite subset is a face of \(K=\mathcal N(R_{m,n})\) iff it lies in some \(S_{ij}\). Every pair of distinct cells forms an edge of \(K\): for a common row or column use a third cell on it; for cells in different rows and columns use an opposite corner. Consequently \(K\) is connected and has complete one-skeleton. The proof requires \(m,n\ge4\) so that every three distinct cells of any single row or column have a common neighbor outside that triple. No assertion about either parameter below four or about complete homotopy type is made.

## Proof
Fix an arbitrary abelian group \(A\) and an arbitrary oriented simplicial one-cocycle \(c\) on \(K\), writing \(c(u,v)=-c(v,u)\). Its restriction to each row is a cocycle on the complete two-skeleton of that row, because any row triple is contained in a neighborhood \(S_{it}\) with its center outside the triple. Such a cocycle is a coboundary. Therefore there are row potentials \(r_{ij}\in A\) satisfying
\[
c((i,j),(i,l))=r_{il}-r_{ij}.
\]
Likewise there are column potentials \(s_{ij}\in A\) with
\[
c((i,j),(k,j))=s_{kj}-s_{ij}.
\]
Each family of potentials is unique up to adding a constant on its row or column, respectively.

For each center \((i,l)\), its entire open neighborhood \(S_{il}\) is a simplex. It is the disjoint union of the row leg \(U=\{(i,j):j\ne l\}\) and the column leg \(W=\{(k,l):k\ne i\}\). Since a cocycle on a simplex is exact and agrees with the row potentials on \(U\) and with the column potentials on \(W\), there is an element \(t_{il}\in A\) such that, for all \(i\ne k\) and \(j\ne l\),
\[
c((i,j),(k,l))=s_{kl}-r_{ij}+t_{il}.\tag{1}
\]
This is the first critical step: the same \(t_{il}\) works for **every** cross edge between the two legs of that neighborhood.

Put \(\delta_{ij}=r_{ij}-s_{ij}\). Apply (1) to an edge and to its reverse, using the opposite center \((k,j)\). Antisymmetry gives, for every \(i\ne k\) and \(j\ne l\),
\[
t_{il}+t_{kj}=\delta_{ij}+\delta_{kl}.\tag{2}
\]
Fix distinct columns \(j,p\) and choose a third column \(l\). Subtract (2) for \((i,k,j,l)\) and \((i,k,p,l)\) to obtain
\[
t_{kj}-t_{kp}=\delta_{ij}-\delta_{ip}\quad(i\ne k).\tag{3}
\]
For any two rows, a third row \(k\) may be chosen distinct from both. Equation (3) then shows that the column differences \(\delta_{ij}-\delta_{ip}\) do not depend on row \(i\). Consequently there are \(a_i,b_j\in A\) with \(\delta_{ij}=a_i+b_j\). Equation (3) also shows \(t_{ij}=d_i+b_j\) for some \(d_i\in A\). Substitution in (2) gives
\[
(d_i-a_i)+(d_k-a_k)=0\qquad(i\ne k).\tag{4}
\]
With at least three rows, all \(d_i-a_i\) equal a common element \(e\in A\) and \(2e=0\).

Replace the row potentials by \(r'_{ij}=r_{ij}-a_i\), and the column potentials by \(s'_{ij}=s_{ij}+b_j\). These replacements preserve their row and column edge differences, but now \(r'_{ij}=s'_{ij}=:f_{ij}\). In (1) the corresponding constant becomes \(t'_{il}=t_{il}-a_i-b_l=e\). Hence on every edge \(c=df+e\varepsilon\), where \(\varepsilon(u,v)=1\) if the endpoints differ in both coordinates and zero otherwise, interpreted with coefficient \(e=-e\). Therefore every cohomology class is represented by \(e\varepsilon\) for some \(e\in A[2]\).

Conversely, \(e\varepsilon\) is a cocycle for every \(2e=0\): each two-simplex lies in some \(S_{ij}\) and contains either zero or two cross-leg edges, so its signed sum is zero. To show injectivity, take distinct rows \(i,k\) and columns \(j,l\). The oriented three-edge loop
\[
(i,j)\longrightarrow(i,l)\longrightarrow(k,l)\longrightarrow(i,j)
\]
is a cycle in the complete one-skeleton, on which \(e\varepsilon\) evaluates to \(e\), because exactly its closing edge connects different rows and columns. It follows that
\[
H^1(K;A)\cong A[2]\quad\text{naturally in }A.\tag{5}
\]
Since \(K\) is finite and connected, the universal coefficient theorem gives \(H^1(K;A)\cong\operatorname{Hom}(H_1(K;\mathbb Z),A)\) for every \(A\). Taking \(A=\mathbb Z\), \(\mathbb Z/p\mathbb Z\) for each odd prime, and \(\mathbb Z/2^q\mathbb Z\) for arbitrary positive integers \(q\), equation (5) determines the finitely generated abelian group uniquely: it has no free part, no odd-primary torsion, and exactly one cyclic factor of order two. Thus \(H_1(K;\mathbb Z)\cong\mathbb Z/2\mathbb Z\), as claimed.

## Verification
The standalone `artifacts/verify.py` enumerates each full neighborhood simplex and constructs the exact one-, two- and three-element face sets for selected small parameter pairs. Over characteristics \(2,3,5\), it computes the rank of the triangle-boundary map, removes the connected-graph boundary rank \(mn-1\), and verifies first Betti numbers \((1,0,0)\) for \((m,n)=(4,4),(4,5),(5,5),(5,6),(6,6)\). It also checks the mod-two diagonal-edge cocycle on every triangle and evaluates it as one on an explicit L-shaped three-edge loop. These finite tests are independent consistency checks: the preceding cochain argument establishes all \(m,n\ge4\) and all abelian coefficients, without extrapolation from the tests.

## Relationship to prior work
Matsushita, *Closed neighborhood complexes of graphs* (first public 2025-11-16), Example 3.5, determines a wedge of two-spheres for the **closed** neighborhood complex of the same rook graphs. Its center-including simplices are different from the **open** neighborhoods used here, and its theorem does not imply their integral first homology. General results on fundamental groups of open neighborhood complexes provide a conceptual framework, but no checked primary statement supplies this all-parameter calculation. Previously published finite calculations show \(H_1\cong\mathbb Z/2\) for the \(4\)-by-\(4\) rook graph, including the Kummer-biplane identification. A separate all-parameter result identifies the high-degree integral homology and a relative quotient of open rook-graph neighborhood complexes, but explicitly does not determine their degree-one homology. Therefore the new assertion is persistence of **exactly one** order-two class across **all** rook-board sizes in the stated range, not a reassertion of the existing finite case or a calculation of an already-classified closed complex.

## Limitations
Only the first integral homology and its equivalent universal first-cohomology functor are determined; no complete homotopy classification or formula for higher integral homology is claimed. The exact statement does not include boards with fewer than four rows or columns. The complete finite computation is a consistency check rather than an infinite proof. An unindexed equivalent all-parameter result, or an implication from a prior fundamental-group classification not located in the inspected material, remains an originality risk. The result has not received independent scientific validation.

## References
1. T. Matsushita, *Closed neighborhood complexes of graphs*, arXiv:2511.12608 (first posted 2025-11-16), especially Example 3.5, https://arxiv.org/abs/2511.12608.
2. T. Matsushita, *Fundamental groups of neighborhood complexes*, arXiv:1210.2803 (first posted 2012-10-10), https://arxiv.org/abs/1210.2803.
3. S. Shukla, *Homotopy type of the neighborhood complexes of graphs of maximal degree at most 3 and 4-regular circulant graphs*, arXiv:1802.04526 (first posted 2018-02-13), https://arxiv.org/abs/1802.04526.
4. *The Kummer biplane block complex has an integral projective-plane summand*, public research record `2026/10/11/SCOPE-the-kummer-biplane-block-complex-has-an-integral-projective-plan--6184c6679525`, finite \(4\)-by-\(4\) case, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-the-kummer-biplane-block-complex-has-an-integral-projective-plan--6184c6679525.
5. *Row-column boundary spheres control higher neighborhood homology of rook graphs*, public research record `2026/10/11/SCOPE-row-column-boundary-spheres-control-higher-neighborhood-homology--f09a20a3ee45`, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-row-column-boundary-spheres-control-higher-neighborhood-homology--f09a20a3ee45.
