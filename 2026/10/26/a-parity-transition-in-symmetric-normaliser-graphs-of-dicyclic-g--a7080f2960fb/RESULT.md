# A parity transition in symmetric normaliser graphs of dicyclic groups

## Finding
For an integer \(m\geq 3\), let
\[
Q_{4m}=\langle a,b\mid a^{2m}=1,\ b^2=a^m,\ bab^{-1}=a^{-1}\rangle
\]
be the dicyclic group of order \(4m\). Define the *symmetric normaliser graph* \(\mathcal N(Q_{4m})\) on all group elements, with distinct \(x,y\) adjacent exactly when \(x\in N_{Q_{4m}}(\langle y\rangle)\) and \(y\in N_{Q_{4m}}(\langle x\rangle)\). Let \(K_t\) denote a complete graph on \(t\) vertices, \(\sqcup\) disjoint union and \(\vee\) the graph join.

The following are exact graph isomorphisms:
\[
\mathcal N(Q_{4m})\cong
\begin{cases}
K_2\vee\bigl(K_{2m-2}\sqcup mK_2\bigr),&m\text{ odd},\\[2mm]
K_4\vee\bigl(K_{2m-4}\sqcup \frac m2 K_4\bigr),&m\text{ even}.
\end{cases}
\]
In particular, the number of universal vertices jumps from two to four on passing from odd to even \(m\), and the nonuniversal outside elements arrange into pairs or quadruples respectively.

The entire Laplacian spectrum, with a superscript in brackets indicating multiplicity, is
\[
\operatorname{Spec}L=\begin{cases}
\{0^{[1]},(4m)^{[2]},(2m)^{[2m-3]},4^{[m]},2^{[m]}\},&m\text{ odd},\\[2mm]
\{0^{[1]},(4m)^{[4]},(2m)^{[2m-5]},8^{[3m/2]},4^{[m/2]}\},&m\text{ even}.
\end{cases}
\]
Repeated numerical eigenvalues in this multiset must have their multiplicities added (for example, \(2m=8\) at \(m=4\)). The numbers of labelled spanning trees are
\[
\tau(\mathcal N(Q_{4m}))=\begin{cases}
(4m)(2m)^{2m-3}8^m,&m\text{ odd},\\[2mm]
(4m)^3(2m)^{2m-5}8^{3m/2}4^{m/2},&m\text{ even}.
\end{cases}
\]
Also \(\chi(\mathcal N(Q_{4m}))=2m\), and its independence number is \(m+1\) when \(m\) is odd and \(m/2+1\) when \(m\) is even. The exceptional dicyclic group \(Q_8\) (\(m=2\)) has \(\mathcal N(Q_8)=K_8\), and its Laplacian spectrum is \(\{0,8^{[7]}\}\) with \(8^6\) spanning trees.

## Assumptions and scope
The group is the finite dicyclic group with the displayed presentation and \(m\ge3\), not an arbitrary generalized dicyclic group over a noncyclic abelian kernel. Graphs are finite, simple and undirected. All Laplacian spectra refer to the ordinary combinatorial Laplacian \(L=D-A\). A spanning tree is counted with vertices labelled by group elements; graph isomorphisms preserve this count. The statements hold for all specified \(m\), with no asymptotic hypothesis.

## Proof
Every element has a unique form \(a^i\) or \(a^jb\), where \(i,j\in\mathbb Z/(2m)\). Put \(r_i=a^i\), \(s_j=a^jb\). Multiplication and inversion follow directly from the presentation; in particular \(s_j^2=a^m\) and \(\langle s_j\rangle=\{1,a^m,s_j,s_{j+m}\}\).

**(1) Adjacencies.** Every two distinct rotations are adjacent because they lie in the normal cyclic subgroup \(\langle a\rangle\). Every reflection-type element \(s_j\) normalises each cyclic subgroup \(\langle r_i\rangle\) by inversion. Conjugation gives \(r_i s_jr_i^{-1}=s_{j+2i}\). Thus \(r_i\) and \(s_j\) are mutually normalising precisely if
\[
2i\equiv 0\text{ or }m\pmod {2m}.
\]
Similarly \(s_k s_js_k^{-1}=s_{2k-j}\), so distinct \(s_j,s_k\) are adjacent precisely if
\[
2(k-j)\equiv 0\text{ or }m\pmod{2m}.
\]
These are necessary and sufficient conditions: a conjugate of a reflection-type element lies in its order-four cyclic subgroup exactly when it equals that element or its inverse.

**(2) Clique decomposition.** For odd \(m\), the first congruence has only \(i=0,m\) as solutions, and the second connects \(s_j\) only to \(s_{j+m}\). Removing the two universal rotations leaves the clique \(\{r_i:i\ne0,m\}\) of size \(2m-2\) and \(m\) disjoint reflection pairs. For even \(m\), the first congruence has exactly four solutions \(i=0,m/2,m,3m/2\), and the second connects reflection indices exactly when they are congruent modulo \(m/2\). Removing the four universal rotations leaves a clique on the other \(2m-4\) rotations and \(m/2\) disjoint cliques of size four. No edges cross the listed nonuniversal cliques. This proves both graph isomorphisms. For \(m=2\) the rotation remainder is empty and all eight vertices are universal.

**(3) Laplacian and tree count.** For positive integers \(u,r,s,t\), consider \(J=K_u\vee (K_r\sqcup tK_s)\). The subspaces of vectors summing to zero within each nonuniversal clique yield Laplacian eigenvalues \(r+u\) with multiplicity \(r-1\), and \(s+u\) with multiplicity \(t(s-1)\). Vectors constant on each of the \(t+1\) nonuniversal components and with aggregate zero yield eigenvalue \(u\) with multiplicity \(t\). The remaining subspace constant on all nonuniversal vertices and constant on the universal block has eigenvalues \(0\) and \(u+r+ts\); vectors of sum zero within the universal clique contribute this last eigenvalue another \(u-1\) times. Therefore, with \(N=u+r+ts\), the complete spectrum is
\[
\{0^{[1]},N^{[u]},(r+u)^{[r-1]},(s+u)^{[t(s-1)]},u^{[t]}\}.
\]
Substituting \((u,r,s,t)=(2,2m-2,2,m)\) in the odd case and \((4,2m-4,4,m/2)\) in the even case gives exactly the displayed spectra. By the matrix-tree theorem, the product of the nonzero Laplacian eigenvalues divided by \(N=4m\) is the displayed spanning-tree count. Finally, a coloring of each \(K_u\vee(K_r\sqcup tK_s)\) needs and achieves \(u+\max(r,s)\) colors, while the maximum independent set chooses one vertex from each nonuniversal clique. In both parity cases \(u+\max(r,s)=2m\) for \(m\ge3\). This proves the remaining claims.

## Verification
The independent implementation in `verify.py` constructs the multiplication law for \(Q_{4m}\), enumerates all cyclic subgroups, and checks mutual normalisation directly. For \(2\le m\le12\), it compares every pairwise adjacency with the congruence criteria and compares all predicted complete components after deleting universal vertices. For \(2\le m\le6\), exact symbolic integer Laplacian eigenvalues and Kirchhoff cofactors are compared with the claimed spectra and spanning-tree formulas. Running `python verify.py` with Python 3 and SymPy produces `VERIFY_OK`. These finite computations are checks, not the proof for arbitrary \(m\).

## Relationship to prior work
Surbhi and Geetha Venkataraman introduced symmetric normaliser graphs and characterized equality with commuting or nilpotent graphs in arXiv:2601.19569v1 (2026). Their full preprint contains the observation that \(Q_8\) has a complete symmetric normaliser graph, but does not present the above dicyclic all-parameter parity decomposition or Laplacian and tree formulas. Their earlier arXiv:2406.00710v1 (2024) determined power/enhanced-power graph correspondences for generalized quaternion/dicyclic groups and explicitly identified the graph \(K_2\vee(K_{2m-2}\sqcup mK_2)\) for enhanced power graphs. **The odd-\(m\) branch here is already implied** by that 2024 graph formula together with the 2026 criterion \(\mathrm{SNorm}=\mathrm{Com}\): when \(m\) is odd, no subgroup of \(Q_{4m}\) is isomorphic to \(Q_8\), and the other listed obstructions are also absent. It is included only to exhibit the parity transition. **The originality claim is the even-\(m\) graph identification and the resulting exact spectra and tree counts**. For even \(m\ge4\), four universal rotations and reflection cliques of size four differ from the known enhanced-power/commuting graph structure. Published graph descriptions for other edge predicates do not imply the even-case mutual-normalisation congruences without a separate calculation.

## Limitations
The result covers only dicyclic groups with cyclic index-two subgroup. It does not assert graph recognition among arbitrary finite groups, nor does it classify all generalized dicyclic groups with noncyclic abelian kernels. The spectrum and tree formulas follow from the structural decomposition and are not separate independent structural results. A broader previous treatment of mutual normalising cyclic subgroups may implicitly contain this special case; publication priority should be checked independently.

## References
1. Surbhi and G. Venkataraman, *On the Symmetric Normaliser Graph of a Group*, arXiv:2601.19569v1 (27 January 2026), https://arxiv.org/html/2601.19569v1.
2. Surbhi and G. Venkataraman, *Non-Isomorphic Groups with Isomorphic Power and Commuting Graphs*, arXiv:2406.00710v1 (2 June 2024), https://arxiv.org/abs/2406.00710.
3. Kirchhoff's matrix-tree theorem (classical standard result).
