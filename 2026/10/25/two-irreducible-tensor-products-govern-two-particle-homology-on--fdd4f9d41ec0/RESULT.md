# Two irreducible tensor products govern two-particle homology on rectangular complete bipartite graphs

## Finding
For integers \(m,n\ge 4\), let \(G=K_{m,n}\) be the geometric realization of the complete bipartite graph, and let \(X_{m,n}=\operatorname{UConf}_2(G)=\{\{x,y\}\subset G:x\ne y\}\) be the unordered, collision-free configuration space. The group \(S_m\times S_n\) acts by independent permutations of the two vertex parts. Write \(S^{\lambda}_r\) for the rational Specht representation of \(S_r\) indexed by a partition \(\lambda\vdash r\). There is a natural isomorphism of rational representations
\[
H_2(X_{m,n};\mathbb Q)\ \cong\
\bigl(S_m^{(m-2,2)}\boxtimes S_n^{(n-2,1,1)}\bigr)
\oplus
\bigl(S_m^{(m-2,1,1)}\boxtimes S_n^{(n-2,2)}\bigr).
\]
Here \(\boxtimes\) denotes the external tensor product. In particular, both summands are irreducible and nonisomorphic as \(S_m\times S_n\)-representations, and each occurs with multiplicity one. The rank is
\[
\dim_{\mathbb Q}H_2(X_{m,n};\mathbb Q)=
\frac{m(m-3)(n-1)(n-2)+(m-1)(m-2)n(n-3)}4.
\]
Consequently the full vertex-part-permutation group fixes no nonzero rational class in degree two. For arbitrary permutations \(\sigma\in S_m\), \(\tau\in S_n\), the trace is the sum of products of the four Specht characters appearing in the displayed decomposition. The rank and the previously established three-vertex-part boundary case are not claimed as new.

## Assumptions and scope
The underlying graph is a one-dimensional CW complex. Particles occupy arbitrary points of its edges and vertices but cannot coincide anywhere; they are unordered. This is distinct from configurations permitting collisions at a designated set of graph vertices. Homology and equivariance in the representation theorem are taken over \(\mathbb Q\). No claim is made about splitting these modules over \(\mathbb Z\) or about configuration spaces of more than two particles. The lower bound \(m,n\ge4\) is imposed because the three-vertex-part case has a previously established stronger integral representation theorem.

## Proof
**1. Equivariant cubical model.** The standard unordered two-particle discrete configuration space has cells obtained by choosing two mutually disjoint closed vertices or open edges in the graph, with cubical orientations. Its inclusion in the ordinary configuration space is a homotopy equivalence for two particles in \(K_{m,n}\): distinct essential vertices are at distance at least one edge, and each cycle has length at least four, meeting the standard two-particle subdivision hypotheses. All these choices and deformation constructions respect the independent permutations of the two vertex parts. Call the resulting rational cellular modules \(C_i\). The space is two-dimensional.

**2. Permutation-module bookkeeping.** For a set of \(r\) vertices define the rational permutation module \(P_r=\mathbb Q^{[r]}\), the two-subset permutation module \(A_r=\mathbb Q^{\binom{[r]}2}\), the oriented two-subset module \(B_r=\bigwedge^2P_r\), and the distinct ordered-pair permutation module \(Q_r\). Then \(Q_r\cong A_r\oplus B_r\). Every graph edge is oriented from the \(m\)-vertex part toward the \(n\)-vertex part. Classifying cubical cells by the two occupied graph cells gives exact equalities of rational \(S_m\times S_n\)-modules:
\[
\begin{aligned}
C_0&=(A_m\boxtimes\mathbf1)\oplus(P_m\boxtimes P_n)\oplus(\mathbf1\boxtimes A_n),\\
C_1&=(Q_m\boxtimes P_n)\oplus(P_m\boxtimes Q_n),\\
C_2&=(A_m\boxtimes B_n)\oplus(B_m\boxtimes A_n).
\end{aligned}
\]
For \(C_2\), the two occupied edges have distinct endpoints in each vertex part. Interchanging their cubical axes reverses orientation, so the signed module is the antisymmetric square of the cross-edge permutation module restricted to disjoint edges. The usual exterior-square Cauchy decomposition, after removing same-left-endpoint and same-right-endpoint summands, yields exactly the two displayed terms \(A_m\boxtimes B_n\) and \(B_m\boxtimes A_n\). This orientation sign is essential; replacing \(C_2\) with an unsigned pair-permutation representation would not give the result.

**3. First homology.** Farber and Hanbury proved that \(K_{m,n}\) is a mature graph for \(m,n\ge3\) (Proposition 22 of the cited article). Their definition of maturity asserts that the inclusion of the ordered two-point configuration space into the product graph induces an isomorphism on first integral homology. Over \(\mathbb Q\), taking the invariants for the free transposition of the two particles identifies the first homology of the unordered space with one copy of graph first homology. Specifically, on \(H_1(G;\mathbb Q)\oplus H_1(G;\mathbb Q)\), particle interchange swaps the factors, and its invariant diagonal is canonically \(H_1(G;\mathbb Q)\). The incidence-chain computation for \(K_{m,n}\) gives
\[
H_1(X_{m,n};\mathbb Q)\cong U_m\boxtimes U_n,
\qquad U_r=S_r^{(r-1,1)}.
\]
The connected space has \(H_0(X_{m,n};\mathbb Q)=\mathbf1\boxtimes\mathbf1\).

**4. Character cancellation.** Set \(V_r=S_r^{(r-2,2)}\) and \(W_r=S_r^{(r-2,1,1)}\) for \(r\ge4\). The standard Young permutation-module identities and the exterior-square identity are
\[
P_r\cong\mathbf1\oplus U_r,\quad
A_r\cong\mathbf1\oplus U_r\oplus V_r,\quad
B_r\cong U_r\oplus W_r,\quad
Q_r\cong\mathbf1\oplus2U_r\oplus V_r\oplus W_r.
\]
By cellular Euler–Poincaré equality in the representation ring,
\[
[H_2]=[C_2]-[C_1]+[C_0]+[H_1]-[H_0].
\]
Substitute the formulas of Steps 2 and 3. The coefficients of the trivial, one-factor, \(U_m\boxtimes U_n\), and all mixed \(U,V,W\) terms cancel pairwise except
\[
[H_2]=[V_m\boxtimes W_n]+[W_m\boxtimes V_n].
\]
Because the group \(S_m\times S_n\) is finite and \(\mathbb Q\) has characteristic zero, its representations are semisimple. Hence equality in the rational representation ring gives an actual module isomorphism. The two tensor products are inequivalent and irreducible. The hook-length formulas \(\dim V_r=r(r-3)/2\) and \(\dim W_r=(r-1)(r-2)/2\) give the stated dimension. Neither tensor product has an invariant line under both symmetric factors, proving the final assertion.

## Verification
The standalone `verify_rectangular.py` constructs the unsigned-unordered deleted-product cubical complex, computes each cellular boundary rank over the prime field \(\mathbb F_{1000003}\), and independently computes signed Lefschetz traces of every pair of permutation conjugacy-class representatives. Each trace is checked against rational Specht character values computed separately using the Jacobi–Trudi alternating permutation sum and permutation character enumeration. The nine cases \((m,n)=(3,3),(3,4),(3,5),(3,6),(4,4),(4,5),(4,6),(5,5),(5,6)\) pass. The lower-bound-three cases check consistency with the known boundary specialization; the asserted new representation theorem concerns \(m,n\ge4\). In particular, \((4,4)\) gives 12 rational two-cycles and \((5,6)\) gives 104, with all tested class traces matching. These finite checks are independent corroboration, not the proof of the infinite-parameter identity. The full executed output is in `verification_output.txt`.

## Relationship to prior work
Farber and Hanbury, *Topology of configuration space of two particles on a graph, II* (initially public 2010-05-13), establish maturity of complete bipartite graphs, hence the first-homology input. They do not state the two-summand independent \(S_m\times S_n\) character formula. Earlier same-subject calculations determine integral second homology for \(K_{4,4}\) and establish a stronger integral symmetry description for \(K_{3,n}\), but neither determines the full two-parameter \(S_m\times S_n\) decomposition for \(m,n\ge4\). The 2026 Ramos–Yun study, *Computing stable homology representations of graph configuration spaces*, examines the balanced \(K_{n,n}\) family under a **simultaneous diagonal** \(S_n\)-action, whereas the present statement determines independent relabelings for all rectangular pairs. The independent-factor character is not recoverable from the diagonal restriction alone, and the unbalanced pairs are outside that study's family. Published work on vertex-sink configurations uses a different collision condition and does not directly apply.

## Limitations
The result is rational; it does not provide a canonical integral splitting or an integral lattice basis. Published and indexed sources checked do not exhaust all possible earlier equivalent formulations, especially descriptions in graph-braid-group or arrangement-theoretic language. The character cancellation invokes the established maturity theorem, rather than reproving it. The theorem is not a novelty assertion for known rank formulas, the three-vertex-part case, or diagonal balanced-group restrictions. Independent mathematical review remains to be performed.

## References
1. Michael Farber and Elizabeth Hanbury, *Topology of configuration space of two particles on a graph, II*, arXiv:1005.2300, first posted 2010-05-13; Algebraic & Geometric Topology **10** (2010), 2203–2227, Proposition 22.
2. Eric Ramos and Claudia He Yun, *Computing stable homology representations of graph configuration spaces*, arXiv:2606.13813, first posted 2026-06-11, especially the balanced complete-bipartite diagonal-action calculation in §3.3.
3. A. D. Abrams, *Configuration spaces and braid groups of graphs*, Ph.D. dissertation, University of California, Berkeley (2000), for the discretized graph configuration-space model.
