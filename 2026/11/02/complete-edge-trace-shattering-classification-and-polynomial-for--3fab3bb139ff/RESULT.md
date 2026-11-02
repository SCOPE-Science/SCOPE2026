# Complete edge-trace shattering classification and polynomial for labeled Hamiltonian cycles

## Finding
For every integer \(n\ge3\), let \(\mathcal H_n\) be the family of undirected spanning Hamiltonian cycles in the complete simple graph \(K_n\), regarded as subsets of its edges. A query asks whether an edge belongs to the unknown cycle. A support \(S\subseteq E(K_n)\) is **shattered** if for every \(P\subseteq S\) there exists \(H\in\mathcal H_n\) with \(H\cap S=P\).

**All-support classification.** Such an \(S\) is shattered if and only if one of the following holds:

1. \(S\) is a linear forest (a disjoint union of paths, counting isolated vertices) with \(|S|\le n-3\).
2. \(S\) is a linear forest with exactly two path components, of vertex orders \(a\le b\), \(a+b=n\), and either \(a=1,\ b\ge4\), or \(a\ge4\).

In the second case \(|S|=n-2\). Thus the entire family of shattered supports is characterized, rather than only its maximum cardinality. In particular, a path component of order two or three cannot occur in a maximum shattered support, although isolated vertices can.

The **shattering polynomial** \(\Phi_n(z)=\sum_{S\text{ shattered}}z^{|S|}\) is \(\Phi_3(z)=1\), \(\Phi_4(z)=1+6z\), and, for all \(n\ge5\),
\[
\Phi_n(z)=\sum_{k=0}^{n-3}F_{n,k}z^k+M_nz^{n-2},\qquad
F_{n,0}=1,\qquad
F_{n,k}=\sum_{j=1}^{\min(k,n-k)}\frac{n!}{2^j j!(n-k-j)!}\binom{k-1}{j-1}\quad (k\ge1),
\]
where
\[
M_5=60,\qquad M_6=360,\qquad
M_n=\frac{n!(n-3)}8\quad(n\ge7).
\]
An equivalent generating function for the lower-degree coefficients is \(F_{n,k}=n![x^nz^k]\exp(x+x^2z/(2(1-xz)))\). In particular the values of \(\Phi_n(z)\) through order seven are given in `verification_output.txt`.

## Assumptions and scope
Graphs are finite, simple, undirected, with labeled vertices. A path component of order one is an isolated vertex. Each Hamiltonian cycle has \(n\) edges (including the triangle for \(n=3\)), and reversal/rotation does not produce another concept. The theorem concerns membership traces on **fixed individual edges**, not vertex-subset edge detection, and concerns spanning Hamiltonian cycles, not the family of all cycles of any length. The polynomial enumerates supports as labeled subsets, not up to graph isomorphism.

## Proof
**Necessity of a linear forest and the size cutoff.** Shattering entails realizing the all-positive labeling, so \(S\subseteq H\) for a Hamiltonian cycle \(H\). Every proper subset of \(H\) is a linear forest. If \(|S|=n\), it contains an unshattered spanning path (as below), so it is not shattered. If \(|S|=n-1\), it is a spanning path. Designate one endpoint edge negative and all its other edges positive. The positive edges form one path containing \(n-1\) vertices plus one isolated vertex \(v\). Every Hamiltonian cycle containing the positive path must attach \(v\) to both endpoints of that path; one of these attachments is the designated negative edge. The labeling is impossible. Thus any shattered support has at most \(n-2\) edges and is a linear forest.

**Reduction to complementary Hamiltonian cycles on path blocks.** Given a linear forest \(S\subseteq H\) and any labeling of its edges, call \(p\) edges positive and \(t\) negative, and let \(u=n-|S|\) be the number of unqueried edges of a fixed containing Hamiltonian cycle \(H\). Collapse every maximal consecutive run of positive edges along \(H\) to a rigid path block, retaining its two possible orientations. There are \(m=n-p=t+u\) blocks. Negative edges induce a forbidden-adjacency graph \(F\) on blocks; it consists of paths, with exactly \(t\) edges and maximum degree at most two. A Hamiltonian cycle on the block vertices in \(K_m\setminus F\), whenever \(m\ge3\), can be expanded to a Hamiltonian cycle of the original vertices satisfying all positive and negative answers. Each block can be oriented arbitrarily when attaching it to its neighbors, and no forbidden block adjacency arises. The all-positive labeling is independently realized by \(H\).

**All forests through \(n-3\) edges are shattered.** Such a forest embeds into a spanning Hamiltonian cycle: orient each path, concatenate all components, and join successive endpoints cyclically (there are at least three components). Now \(u\ge3\). When \(m\ge6\), each vertex of \(K_m\setminus F\) has degree at least \(m-3\ge m/2\), so Dirac's Hamiltonian-cycle theorem applies. For \(m=3\), necessarily \(t=0\), and the cycle is immediate. For \(m=4\), \(t\le1\), and \(K_4\) minus at most one edge is Hamiltonian. For \(m=5\), \(t\le2\), and \(K_5\) minus at most two edges is Hamiltonian. Therefore every labeling is realized.

**The two-component boundary.** A linear forest with \(n-2\) edges has precisely two path components. Let their vertex orders be \(a,b\), where \(a\le b\). The reduction now has \(u=2\) and \(m=t+2\). For \(t\ge4\), Dirac again applies. For \(t=3\), the forbidden graph on five blocks is either a four-vertex path plus an isolate, or a three-vertex path plus a two-vertex path. Both complements contain a Hamiltonian five-cycle. For the first type, writing the forbidden path \(A_1A_2A_3A_4\) and isolate \(D\), a permitted cycle is \(A_1,A_3,D,A_2,A_4,A_1\); for the second type, writing the forbidden paths \(A_1A_2A_3\), \(B_1B_2\), a permitted cycle is \(A_2,B_1,A_1,A_3,B_2,A_2\). For \(t=2\) with one negative edge in each original component, the forbidden edges are disjoint on four blocks and the complement contains a four-cycle.

If \(t=1\), one original path is split into blocks \(A,B\); the other path is one block \(D\). Every cycle on these three blocks uses adjacency \(A,B\). If both blocks are singletons, the designated negative edge is unavoidable, giving an obstruction exactly when the split component has order two. Otherwise a nonsingleton block can be reversed so that the contacting endpoint is not the vertex of the forbidden edge, and the labeling is realized.

If \(t=2\) with both negatives in one original component, it is split into consecutive blocks \(A,B,C\); the other component is block \(D\). When \(A\) or \(B\) is nonsingleton, the block cycle \(A,B,D,C,A\) includes only the possibly forbidden adjacency \(A,B\), which can be avoided at the vertex level by reversing a nonsingleton endpoint block. When only \(C\) is nonsingleton, use \(A,C,B,D,A\), with its sole potentially forbidden adjacency \(B,C\), and reverse \(C\). If \(A,B,C\) are all singletons, then \(B\) is forbidden from adjoining both \(A\) and \(C\), and it can only adjoin \(D\), so a four-block cycle is impossible. This is exactly the order-three path obstruction. Consequently all labelings are possible precisely when neither component has order two or three; when one component has order one the other must have order at least four, and when neither is isolated both orders must be at least four. This completes the classification.

**Counting supports.** For \(k\le n-3\), every shattered support is a linear forest of \(k\) edges. If it has \(j\) nontrivial path components, the component edge counts are a composition of \(k\) into \(j\) positive parts, chosen in \(\binom{k-1}{j-1}\) ways. Labeling these unoriented paths and the \(n-k-j\) isolated vertices gives the stated \(F_{n,k}\); equivalently the exponential formula yields \(\exp(x+x^2z/[2(1-xz)])\). For \(k=n-2\), the allowed unordered path orders are \((1,n-1)\) and \((a,n-a)\) with \(4\le a\le n-a\). The first contributes \(n!/2\) distinct forests, each unequal order pair with both orders at least four contributes \(n!/4\), and an equal order pair contributes \(n!/8\). For \(n=5,6\), only the first case occurs, giving \(M_n=n!/2\). For \(n\ge7\), summing the remaining cases gives \(M_n=n!(n-3)/8\) (including the special equal-split correction). At orders three and four, direct classification gives the two stated small polynomials.

## Verification
The accompanying `verify_support_classification.py` independently enumerates all labeled undirected Hamiltonian cycles and every support contained in one of them for \(3\le n\le7\), computes every binary trace, and compares shattering against the structural characterization. It checks 8, 37, 218, 1,546, and 12,772 cycle-compatible supports at those respective orders. Separate representative two-component tests at orders eight and nine cover every possible pair of path orders. Reproduction: `python verify_support_classification.py`. The included `verification_output.txt` records actual program output. These computations check finite cases; the unrestricted classification and coefficients follow from the proof above, not from extrapolation.

## Relationship to prior work
Mofidi's work on the cycle and spanning-tree hypergraphs of graphs treats all cycles, including non-spanning cycles, and gives a different VC threshold and necessary support conditions for the complete graph. A query support can be shattered by arbitrary cycles without being shattered by Hamiltonian-only cycles, so those results do not provide this full support classification or the shattering polynomial. Earlier work by Kranakis and collaborators treats graph-defined VC classes and remains a relevant historical-priority comparison where accessible full text is limited. Abasi and Bshouty study graph learning with vertex-subset edge-detecting queries rather than fixed-edge membership against Hamiltonian-cycle hypotheses. Alon and collaborators study codes whose symmetric differences contain Hamilton cycles, a different combinatorial demand. The numerical VC dimension of Hamiltonian-cycle edge concepts is known in separate work; the new subject here is the **complete trace-support description and counting polynomial**, not a reassertion of that scalar dimension.

## Limitations
The theorem requires the ambient complete simple graph, individual edge-membership queries, and undirected spanning cycles. It does not characterize Littlestone dimension, arbitrary host graphs, path-hypothesis concepts, or vertex-subset query models. The historical-priority assessment is based on identified accessible primary material; older papers without accessible full text remain a residual risk. Self-review is not independent validation.

## References
1. A. Mofidi, "On the VC-dimension, covering and separating properties of the cycle and spanning tree hypergraphs of graphs," DOI: 10.22108/TOC.2021.127880.1832 (full paper examined, especially Theorem 3.3).
2. E. Kranakis, D. Krizanc, B. Ruf, J. Urrutia, and G. Woeginger, "The VC-dimension of set systems defined by graphs," Discrete Applied Mathematics, DOI: 10.1016/S0166-218X(96)00137-0 (abstract and bibliographic material accessible).
3. H. Abasi and N. H. Bshouty, "On Learning Graphs with Edge-Detecting Queries," arXiv:1803.10639, publicly posted 2018-03-28 (full manuscript examined).
4. N. Alon, A. Gujgiczer, J. Körner, A. Milojević, and G. Simonyi, "Structured Codes of Graphs," arXiv:2202.06810 (full manuscript examined).
5. G. A. Dirac, "Some Theorems on Abstract Graphs," Proceedings of the London Mathematical Society (1952), for the classical minimum-degree Hamiltonicity criterion.
