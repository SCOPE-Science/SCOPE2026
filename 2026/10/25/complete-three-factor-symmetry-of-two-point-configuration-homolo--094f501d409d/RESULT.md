# Complete three-factor symmetry of two-point configuration homology on complete tripartite graphs

## Finding
For integers \(p,q,r\geq3\), let \(G=K_{p,q,r}\) be the complete tripartite graph on three distinguished parts and let \(X=\operatorname{UConf}_2(|G|)\) denote the space of unordered pairs of distinct points on its geometric realization. The group \(H=S_p\times S_q\times S_r\) acts by relabeling vertices within parts. For \(i\in\{1,2,3\}\), write \(n_1=p,n_2=q,n_3=r\) and regard the following rational Specht representations of \(S_{n_i}\) as representations of the corresponding factor of \(H\):
\[
U_i=S^{(n_i-1,1)},\qquad V_i=S^{(n_i-2,2)},\qquad A_i=S^{(n_i-2,1,1)}.
\]
When \(n_i=3\), the symbol \(V_i\) means the zero representation. Tensor products between distinct factors are written by juxtaposition; direct sums are retained with their multiplicities. Then there is an isomorphism of **rational representations**
\[
\begin{aligned}
H_2(X;\mathbb Q)\cong{}&
\bigoplus_{i=1}^3(U_i\oplus A_i)
\oplus\bigoplus_{i\ne j}(U_iV_j\oplus U_iA_j\oplus V_iA_j)\\
&\oplus2\bigoplus_{i<j}U_iU_j
\oplus3U_1U_2U_3
\oplus\bigoplus_{k=1}^3 U_iU_j(V_k\oplus A_k),\quad\{i,j,k\}=\{1,2,3\}.
\end{aligned}
\]
In the final sum, \(i,j\) are the two indices other than \(k\); their order does not matter. If all three part sizes are at least four, this decomposition has 34 distinct irreducible constituents (with multiplicities as displayed). In particular, \(H_2(X;\mathbb Q)^H=0\). The natural representation in degree one is \(H_1(X;\mathbb Q)\cong H_1(G;\mathbb Q)\), with one-dimensional \(H\)-invariants.

An equivalent formula specifies the **entire character** without decomposing into Specht modules. For \(g=(g_1,g_2,g_3)\in H\), let \(f_i\) be the number of fixed vertices of \(g_i\), and let \(t_i\) be its number of two-cycles. Set \(F=f_1+f_2+f_3\) and \(E=f_1f_2+f_1f_3+f_2f_3\). Then
\[
\begin{aligned}
\operatorname{tr}(g\mid H_2(X;\mathbb Q))={}&
\binom E2-\sum_i f_i\binom{F-f_i}2
-2\sum_{i<j}t_it_j\\
&-(F-3)E+\binom F2-F+\sum_i t_i.
\end{aligned}
\]
The convention \(\binom a2=a(a-1)/2\) applies also for \(a=0,1\).

## Assumptions and scope
The graph has exactly three independently labeled parts, each of size at least three. The configuration points may lie anywhere on the geometric graph, but may not coincide. All representation isomorphisms and characters are over \(\mathbb Q\); this finding does **not** assert an integral splitting or an absence of integral torsion. The action preserves each part rather than permuting equally sized parts. The homology degree is ordinary degree two (equal to reduced homology there). Primary classification: MSC2020 55R80.

## Proof
**1. Maturity and degree one.** Call a graph mature when inclusion of the **ordered** two-point configuration space into \(|G|\times|G|\) induces an isomorphism on integral first homology. Barnett–Farber establish maturity of \(K_{3,3}\); Farber–Hanbury establish it for all \(K_{p,q}\) with \(p,q\geq3\), as well as an edge-attachment criterion: adjoining an edge with endpoints \(u,v\) to a mature graph preserves maturity if removal of these endpoints leaves the original graph connected. Subdivision preserves maturity (their subdivision argument).

For completeness, the edge criterion extends maturity inductively to \(K_{p,q,r}\). Start from \(K_{p,q}\). If the existing graph is \(K_{p,q,s}\) (including \(s=0\)), take distinct vertices \(u,v\) in the first part; deleting both leaves a connected graph because \(p,q\geq3\). Adjoin the temporary edge \(uv\), then subdivide it with a new vertex \(w\); the temporary edge is replaced by \(uw,vw\). Now adjoin each missing edge \(wx\) for \(x\) in the first or second part. At each such edge addition, deleting \(w,x\) leaves \(K_{p,q,s}\setminus\{x\}\), which is connected. Do not connect \(w\) to any previously created third-part vertex. The resulting graph is \(K_{p,q,s+1}\). This completes the induction, so \(G\) is mature.

The ordered first-homology isomorphism is equivariant for part relabelings and is compatible with exchanging the two particles. Passing to invariants under particle exchange over \(\mathbb Q\) gives \(H_1(X;\mathbb Q)\cong H_1(G;\mathbb Q)\) equivariantly. In the representation ring,
\[
[H_1(G;\mathbb Q)]=[\mathbb Q E(G)]-[\mathbb Q V(G)]+[\mathbf1].
\]
Here each graph edge has the canonical orientation from its lower-indexed part to its higher-indexed part, so this is the **unsigned** edge-permutation module. Its invariant dimension is \(3-3+1=1\), since the three edge-types, three vertex-types and connected component each contribute one invariant.

**2. Exact finite equivariant cell model.** The standard deleted-product cubical deformation retract for two particles has cells indexed as follows: unordered distinct vertex pairs in degree zero, pairs \((v,e)\) with vertex \(v\) disjoint from edge \(e\) in degree one, and unordered pairs of disjoint edges in degree two. Orient edges consistently by increasing part index; orient two-cells using an order of their two oriented edge factors. Write \(P_i\) for the vertex-permutation module of part \(i\), \(R_i\) for unordered vertex pairs in part \(i\), \(Q_i\) for ordered distinct vertex pairs in that part, and \(L_i=\bigwedge^2P_i\) for the orientation-signed pair module. The resulting exact rational cellular chain characters are
\[
\begin{aligned}
[C_0]&=\sum_i[R_i]+\sum_{i<j}[P_iP_j],\\
[C_1]&=\sum_{i<j}([Q_iP_j]+[P_iQ_j]+[P_iP_jP_k]),\quad\{i,j,k\}=\{1,2,3\},\\
[C_2]&=\sum_{i<j}([L_iR_j]+[R_iL_j])+\sum_i[Q_iP_jP_k],\quad\{i,j,k\}=\{1,2,3\}.
\end{aligned}
\]
For the last line: two disjoint edges of the same type \((i,j)\) occupy two vertices in each part and form a two-element signed matching, yielding \(L_iR_j\oplus R_iL_j\). Two edges of different types meeting only in their common part occupy an **ordered** pair of distinct common-part vertices, yielding \(Q_iP_jP_k\). This establishes the sign conventions rather than replacing signed cells by unsigned sets.

Because the cubical model is connected and two-dimensional, equivariant Euler–Poincaré yields
\[
[H_2(X;\mathbb Q)]=[C_2]-[C_1]+[C_0]-[\mathbf1]+[H_1(G;\mathbb Q)].
\]
This is an identity in the rational representation ring of \(H\).

**3. Irreducible expansion.** For every \(n_i\geq3\), the standard decompositions are
\[
P_i=\mathbf1\oplus U_i,\quad
R_i=\mathbf1\oplus U_i\oplus V_i,\quad
Q_i=\mathbf1\oplus2U_i\oplus V_i\oplus A_i,\quad
L_i=U_i\oplus A_i.
\]
The convention \(V_i=0\) when \(n_i=3\) makes these formulas uniform. Substituting them into the displayed Euler–Poincaré identity and grouping the tensor products over the three independently acting factors gives precisely the decomposition in the Finding. Each multiplicity is nonnegative; semisimplicity of rational representations of a finite group upgrades the representation-ring identity to the asserted isomorphism. Every displayed summand has a nontrivial factor, so the invariant degree-two subspace vanishes.

**4. Fixed-cell trace formula.** Under \(g\), the fixed edge count is \(E\), the fixed vertex count is \(F\), and the fixed degree-one cubical cells total \((F-2)E\). The fixed zero-cells total \(\binom F2+\sum_i t_i\). For the degree-two oriented cubical cells, the trace is
\[
\binom E2-\sum_i f_i\binom{F-f_i}2-2\sum_{i<j}t_it_j.
\]
The first two terms count disjoint pairs of individually fixed edges; the last term counts pairs of disjoint edges interchanged by the group element, which contribute orientation sign \(-1\). The first-homology trace is \(E-F+1\). Substitution in the signed Euler identity gives the character formula in the Finding. This independent cell argument agrees with the Specht decomposition for every conjugacy class.

## Verification
The included standard-library program `artifacts/verify_tripartite.py` reconstructs the full deleted-product cubical model and all degree-one/two incidences; it checks binary boundary ranks for \((3,3,3),(3,3,4),(3,4,4),(4,4,4)\) and independently compares every group-element signed Lefschetz trace with both character formulas for the first two of those tuples. The separate program `artifacts/verify_tripartite_mod3.py` computes **signed** cubical boundaries and exact ranks over \(\mathbb F_3\) for the first three tuples, obtaining the predicted rational ranks there. Their actual recorded outputs are packaged alongside the source. These computations check small parameters and signs; the preceding uniform graph-maturity and representation-ring proof establishes the infinite-family claim.

## Relationship to prior work
Barnett–Farber established the graph configuration cubical model and foundational maturity results. Farber–Hanbury established the complete-bipartite maturity theorem, the edge-attachment criterion and ordinary topological invariants; this work uses those as inputs rather than asserting them as new. Ramos–Yun studied stable homology representations for graph families and, in particular, a balanced two-large-part family with one singleton part and a **diagonal** symmetric-group action. Their hypotheses neither contain three parts of sizes at least three nor determine the independent three-factor representation here. The present calculation contributes the all-parameter complete rational \(S_p\times S_q\times S_r\)-module on \(H_2\), including its irreducible multiplicities and full character.

## Limitations
No integral representation decomposition or integral torsion assertion is made. The theorem does not determine actions that interchange equal-sized parts. It concerns unordered **two-point** configurations, not ordered or sink configuration spaces, and not higher-particle configurations. An equivalent statement outside the inspected literature and indexed research remains possible. The finite computer checks cover only the explicitly listed instances. Independent scientific audit has not been performed.

## References
1. K. Barnett and M. Farber, *Topology of configuration space of two particles on a graph, I*, arXiv:0903.2180 (first public version 12 March 2009), especially the deleted-product model and mature graph examples.
2. M. Farber and E. Hanbury, *Topology of configuration space of two particles on a graph, II*, arXiv:1005.2300 (first public version 13 May 2010), especially the mature-graph edge-attachment result and complete bipartite graphs.
3. E. Ramos and C. H. Yun, *Computing stable homology representations of graph configuration spaces*, arXiv:2606.13813 (2026), especially its distinct balanced/diagonal-action cases.
