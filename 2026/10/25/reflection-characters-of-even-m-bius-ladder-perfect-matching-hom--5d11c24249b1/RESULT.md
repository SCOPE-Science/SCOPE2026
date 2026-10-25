# Reflection characters of even Möbius-ladder perfect-matching homology

## Finding
For each **even integer** \(n\ge4\), let \(M_{2n}\) be the simple graph on \(\mathbb Z/(2n)\) whose edges are the perimeter edges \(c_i=\{i,i+1\}\) and the antipodal edges \(d_j=\{j,j+n\}\). Indices of perimeter edges are modulo \(2n\), and indices of antipodal edges modulo \(n\). Let \(X_n\) denote the perfect-matching simplicial complex: its vertices are edges of \(M_{2n}\), and its faces are the edge sets extendable to perfect matchings. The graph reflections \(s_a(i)=a-i\pmod{2n}\) act simplicially on \(X_n\).

The only nonzero reduced rational homology of \(X_n\) is two-dimensional in degree \(d=n/2-1\) (Agarwal–Basak, Theorem 18 in the first preprint, Theorem 21 in the revised version). The **complete reflection character** in that degree is
\[
\boxed{\operatorname{tr}\left(s_a\mid\widetilde H_d(X_n;\mathbb Q)\right)=
\begin{cases}
0,&a\text{ even},\\
0,&a\text{ odd and }n\equiv0\pmod4,\\
2(-1)^{(n-2)/4},&a\text{ odd and }n\equiv2\pmod4.
\end{cases}}
\]
Thus at widths \(n\equiv2\pmod4\), the two conjugacy classes of reflection axes have different homological actions, although the homology rank is always two.

As a representation-theoretic corollary, combine the new character with the previously determined one-step rotation \(r(i)=i+1\): if \(n\equiv0\pmod4\), the rational module is the unique two-dimensional irreducible representation factoring through the square dihedral group, with \(r^2=-I\); if \(n\equiv2\pmod4\), it is the sum of the two one-dimensional characters with \(r\) acting as \(+1\) and \(-1\), respectively, and with \(s_1\) acting as the common scalar \(\varepsilon=(-1)^{(n-2)/4}\). In particular, the full dihedral-invariant reduced rational homology has dimension one exactly when \(n\equiv2\pmod8\), and dimension zero otherwise. This corollary uses the published rotation theorem as a separate input; the new proof below establishes all reflection traces independently of it.

## Assumptions and scope
The dihedral group meant here is the natural group \(D_{2n}=\langle r,s_0\rangle\), acting on the labeled perimeter cycle, where \(r(i)=i+1\), \(s_0(i)=-i\), \(r^{2n}=s_0^2=1\), and \(s_0rs_0=r^{-1}\). This statement is about the **perfect-matching** complex, not the ordinary matching complex or the independence complex of \(M_{2n}\). The range excludes \(n=2\), where the graph is the exceptional complete graph on four vertices. Homology coefficients are \(\mathbb Q\); no integral lattice classification or equivariant homotopy equivalence is claimed.

The two 2026 source inputs are as follows. First, Agarwal–Basak prove that for even \(n\), \(X_n\) is the independence complex of an explicit incompatibility graph and has homotopy type \(S^{n/2-1}\vee S^{n/2-1}\). In the present indexing, this incompatibility graph has vertices \(c_i,d_j\) and an edge precisely in one of these cases: two graph edges share an endpoint; or they are two perimeter edges \(c_i,c_j\) with \(j-i\equiv n-1\) or \(n+1\pmod{2n}\). The extra incompatible perimeter pairs are the minimal disjoint nonextendable matchings. The source proves the matching-extension criterion in its Lemmas 13–15; direct independent finite tests of this exact criterion are included. Second, the previously published rotation calculation gives \(\operatorname{tr}(r_*)=0\) and \(r_*^2=(-1)^{n/2-1}I\); it is used only for the stated representation-theoretic corollary.

## Proof
**1. Fixed orbit subsets and signs.** Fix a reflection \(s=s_a\). Since the perfect-matching complex is the independence complex of the incompatibility graph, every invariant simplex is a disjoint union of full \(s\)-orbits of graph edges. Ignore an edge orbit if its two members are incompatible. Make a quotient *incompatibility* graph \(Q(s)\) whose vertices are the surviving orbits and whose distinct vertices are adjacent when any two represented graph edges are incompatible. Invariant simplices are then in bijection with independent sets of \(Q(s)\), including the empty set.

If an invariant nonempty simplex contains \(m\) vertices of \(X_n\), arranged in \(o\) cycles of the reflection on those vertices, the sign of the reflection on its oriented chain is \((-1)^{m-o}\). Its contribution in degree \(m-1\) to the Lefschetz alternating trace is \((-1)^{o-1}\). Including the augmented empty chain, which contributes \(-1\), gives the reduced Lefschetz number
\[
\widetilde L(s)=-I(Q(s);-1),\qquad
I(Q;z)=\sum_{U\subseteq V(Q)\text{ independent}}z^{|U|}.
\]
Since the only nonzero reduced rational homology is in degree \(d=n/2-1\), write \(k=n/2\) and obtain
\[
\operatorname{tr}(s\mid\widetilde H_d)=(-1)^{d+1}I(Q(s);-1)=(-1)^k I(Q(s);-1).\tag{1}
\]
Conjugating by a rotation changes \(s_a\) into \(s_{a+2t}\); hence only \(s_0\) and \(s_1\) need examination.

**2. Even-axis reflections.** Under \(s_0(i)=-i\), the antipodal edge \(d_0=\{0,n\}\) is fixed and represents a singleton vertex of \(Q(s_0)\). Every perimeter edge meeting either endpoint of \(d_0\) belongs to one of the orbit pairs \(\{c_0,c_{2n-1}\}\) and \(\{c_{n-1},c_n\}\). In each pair, its two perimeter edges share an endpoint, so that orbit is excluded from \(Q(s_0)\). Consequently every surviving perimeter orbit avoids \(d_0\), and all antipodal edges are pairwise compatible. Thus the vertex represented by \(d_0\) is **isolated in the incompatibility graph** \(Q(s_0)\). Its independence polynomial has a factor \(1+z\), and
\[
I(Q(s_0);-1)=0.\tag{2}
\]

**3. Odd-axis reflections and open twins.** Under \(s_1(i)=1-i\), the perimeter edges transform as \(c_i\mapsto c_{-i}\), and antipodal edges as \(d_j\mapsto d_{1-j}\). With \(n=2k\), the surviving orbits consist of
\[
A_i=\{c_i,c_{-i}\}\quad(0\le i\le n),\qquad
B_j=\{d_j,d_{1-j}\}\quad(1\le j\le k).
\]
At \(i=0,n\) the notation \(A_i\) represents a singleton. Every displayed orbit is internally compatible. The adjacency rules in \(Q(s_1)\), obtained by testing perimeter adjacency, the two extra forbidden perimeter offsets, and spoke incidence, are:
\[
\begin{split}
&A_i\sim A_j\iff i\ne j\text{ and }\bigl(|i-j|=1\text{ or }i+j\in\{n-1,n+1\}\bigr),\\
&B_j\sim A_i\iff i\in\{j-1,j,n-j,n-j+1\},\\
&B_j\not\sim B_h\quad\text{for all distinct }j,h.
\end{split}\tag{3}
\]
Here the listed indices belong to \(0,\ldots,n\); duplicates at endpoints count only once. Formula (3) implies that \(A_i\) and \(A_{n-i}\) have identical **open** neighborhoods and are nonadjacent, for every \(0\le i<k\).

If two nonadjacent vertices of any finite graph have identical open neighborhoods, then removing one does not change its independence polynomial evaluated at \(-1\): among independent sets containing the removed vertex, toggling the other vertex gives a sign-reversing involution. Remove \(A_n,A_{n-1},\ldots,A_{k+1}\) in this way. The remaining induced graph \(F_k\) has vertices \(A_0,\ldots,A_k,B_1,\ldots,B_k\); its edges form exactly the chain of \(k\) triangles on \(\{A_{j-1},A_j,B_j\}\), for \(1\le j\le k\). Therefore
\[
I(Q(s_1);-1)=I(F_k;-1).\tag{4}
\]
This is a finite symbolic graph reduction valid for all integers \(k\ge2\), not an extrapolation from samples.

**4. Signed independence recurrence for the triangular chain.** Let \(f_j(z)\) and \(g_j(z)\) count independent sets of the first \(j\) triangles, weighted by \(z\) per selected vertex, according as their terminal connecting vertex \(A_j\) is unselected or selected. Initially \(f_0(z)=1\) and \(g_0(z)=z\). The last triangle can contain at most one of its three vertices, so
\[
f_j(z)=(1+z)f_{j-1}(z)+g_{j-1}(z),\qquad
g_j(z)=z f_{j-1}(z).\tag{5}
\]
At \(z=-1\), the state transformation is \((f_j,g_j)=(g_{j-1},-f_{j-1})\), with initial state \((1,-1)\). Iteration proves
\[
I(F_k;-1)=f_k(-1)+g_k(-1)=
\begin{cases}
0,&k\text{ even},\\
2(-1)^{(k+1)/2},&k\text{ odd}.
\end{cases}\tag{6}
\]
Putting (2), (4), and (6) into (1) yields the claimed reflection character, including all congruence classes and both reflection axes.

**5. Rational dihedral module.** The separately published rotation theorem states that on the same two-dimensional homology, \(T=r_*\) has trace zero and \(T^2=(-1)^{k-1}I\). For even \(k\), \(T^2=-I\), so the rational representation factors through the square dihedral group and is the irreducible two-dimensional module; the traces in the theorem are zero. For odd \(k\), \(T^2=I\) and \(\operatorname{tr}(T)=0\), giving one \(+1\) and one \(-1\) rotation eigenline. The odd-axis involution has trace \(2\varepsilon\) and hence acts as the scalar \(\varepsilon I\) on these lines. This proves the direct sum and invariant-dimension conclusions. No unproved classification of other automorphisms is used.

## Verification
The standalone standard-library program `verify_reflections.py` independently enumerates all perfect matchings of the labeled graph, checks the exact incompatibility criterion for each pair of graph edges for even \(n\in\{4,6,8,10,12,14\}\), and exhaustively compares maximal flag faces to actual perfect matchings for \(n\in\{4,6,8,10\}\). It constructs both reflection-orbit incompatibility graphs for every even \(n\) from \(4\) through \(32\), checks the open-twin identities and the exact triangular-chain induced subgraph, and evaluates their independence polynomials at \(-1\). As a separate face-based check **not relying on the incompatibility-graph description**, it enumerates all perfect-matching subfaces and verifies the signed fixed-face sums for both reflection classes for \(n\in\{4,6,8,10\}\) (eight checks).

Reproduction: `python3 verify_reflections.py`. These finite computations corroborate the source input and the graph reduction. The all-width result is proved by the explicit orbit classification, the open-twin identity and recurrence (5), not by the finite tests.

## Relationship to prior work
Agarwal and Basak determine the **nonequivariant** homotopy type of the Möbius-ladder perfect-matching complex, including the rank-two even-width case and the pairwise incompatibility presentation. They do not state a reflection trace. The earlier published rotation result determines \(r_*\) but explicitly leaves reflections outside its scope; the earlier antipodal half-turn is a rotation, not an axis reflection. The published complete dihedral result for **odd** widths has a disjoint parameter range. None of those results implies the present parity-sensitive distinction between the two reflection classes when \(n\equiv2\pmod4\). For \(n\equiv0\pmod4\), the zero-reflection-trace component is compatible with group-theoretic consequences of the prior rotation theorem and is included only as part of the **complete** classification, not claimed to be novel on its own.

The separate finite ordinary-matching-complex calculations concern a different complex. The present argument is not a retabulation of known Betti numbers: the trace \(-2\) versus \(+2\) distinguishes the induced homology involution and determines exactly when the complete dihedral action admits a nonzero invariant vector. The search and implication comparisons appear in the accompanying structured scientific review.

## Limitations
This is a rational homology-character classification for the natural labeled dihedral action and all even \(n\ge4\). It does not supply an integral representation lattice, a full automorphism-group analysis at exceptional small graphs, or an equivariant homotopy model. The nonequivariant homology concentration and the two-element obstruction description are taken from the cited peer-available 2026 preprint, with independent finite verification but not an independent second proof of that preprint's global classification. Unindexed equivalent results remain possible; the revised preprint's abstract was checked but its entire revised body was not available for full comparison.

## References
1. A. Agarwal and B. Basak, *The Homotopy Types of the Independence and Perfect Matching Complexes of Möbius and Circular Ladder Graphs*, arXiv:2608.30601, first public version 31 August 2026; original §§2,4 and Lemmas 13–15/Theorem 18, revised version Theorem 21. https://arxiv.org/abs/2608.30601
2. *Rotation has order two or four on Möbius-ladder perfect-matching homology*, publicly indexed research result, 2026, especially its fixed-simplex proof and its explicit restriction to cyclic rotations. https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-rotation-has-order-two-or-four-on-m-bius-ladder-perfect-matching--3551187dd347
3. *The antipodal half-turn representation on Möbius-ladder perfect-matching homology*, publicly indexed research result, 2026. https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-the-antipodal-half-turn-representation-on-m-bius-ladder-perfect--317e26dcb314
4. *Complete dihedral rational homology representations of odd Möbius-ladder perfect-matching complexes*, publicly indexed research result, 2026. https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-complete-dihedral-rational-homology-representations-of-odd-m-biu--d5bba5f21863
