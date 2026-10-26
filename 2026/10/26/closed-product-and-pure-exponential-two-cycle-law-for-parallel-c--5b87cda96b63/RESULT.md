# Closed-product and pure-exponential two-cycle law for parallel chip-firing on binary trees

## Finding
Let \(T_h\) be the full rooted binary tree of height \(h\ge 1\), with \(2^{h+1}-1\) distinct vertices and ordinary open boundary (root degree two, nonroot internal vertices degree three, leaves degree one). In the parallel chip-firing rule, a vertex with at least its degree in chips sends one chip to every neighbour, simultaneously with all other firing vertices. Count primitive two-cycles of nonnegative integer configurations as **orbits**, so each pair of states is counted once; chips are indistinguishable and vertices are labelled by their positions.

Define integer sequences, for \(j\ge0\), by
\[
 a_0=0,\quad a_1=2,\qquad u_0=1,\quad u_1=5,
 \qquad z_{j+2}=3z_{j+1}+2z_j
\]
(the last recurrence applies separately to \(a\) and \(u\)). Then the **exact** number of primitive two-cycle orbits is
\[
 \boxed{N_h=a_h\prod_{j=1}^{h-1}u_j^{\,2^{h-1-j}}}. 
\]
In particular \(N_1=2\), \(N_2=30\), \(N_3=9350\), and \(N_4=859413750\). Let
\[
 s=\sum_{j=1}^{\infty}2^{-j-2}\log u_j,
 \qquad \kappa=\frac{4e^s}{19+5\sqrt{17}}.
\]
The sum converges, and there is a **pure exponential asymptotic with a nonzero finite constant**:
\[
 \boxed{N_h\sim\kappa\exp\!\big(s(2^{h+1}-1)\big)}
 \qquad (h\to\infty).
\]
Numerically, \(s\approx0.714538498704125\), \(e^s\approx2.043243505111162\), and \(\kappa\approx0.206307334690051\). These asymptotics refer to the number of vertices, not the height. An equivalent finite formula is \(a_h=2(\lambda_+^h-\lambda_-^h)/\sqrt{17}\), where \(\lambda_\pm=(3\pm\sqrt{17})/2\).

## Assumptions and scope
All trees are finite, loopless, have height exactly \(h\ge1\), and retain the two distinguishable children at each internal vertex. For a graph \(G=(V,E)\), a configuration is \(x\in\mathbb{Z}_{\ge0}^V\). Let \(d_v\) be the ordinary degree, \(f_v(x)=\mathbf1_{x_v\ge d_v}\), and define the simultaneous update \((\Phi x)_v=x_v-d_vf_v(x)+\sum_{w\sim v}f_w(x)\). The count includes every possible conserved total chip mass, but only configurations on primitive period-two orbits; no assertion is made about basin sizes, transient times, or full-state convergence from arbitrarily many chips.

## Proof
**Step 1: two-step firing phases and finite chip intervals.** Suppose \(x\ne y=\Phi x\) and \(\Phi y=x\) on any finite connected graph. Let \(t_v=f_v(x)+f_v(y)\). Two-step conservation at each vertex says the graph Laplacian of \(t\) is zero. Connectivity forces \(t_v\) to equal a common \(t\in\{0,1,2\}\). Values \(t=0\) and \(t=2\) force every vertex to have the same firing decision in both rounds, hence \(\Phi x=x\); therefore \(t=1\). Write \(p_v=f_v(x)\in\{0,1\}\) and let \(k_v=|\{w\sim v:p_w\ne p_v\}|\). Directly applying both firing thresholds yields precisely \(k_v\) legal choices for \(x_v\):
\[
 x_v\in
 \begin{cases}
 \{d_v,d_v+1,\dots,d_v+k_v-1\},&p_v=1,\\
 \{d_v-k_v,d_v-k_v+1,\dots,d_v-1\},&p_v=0.
 \end{cases}
\]
Both intervals are nonnegative because \(0\le k_v\le d_v\). In particular, \(k_v=0\) makes the proposed phase pattern impossible. Conversely, each configuration assembled from these intervals fires with phase \(p\) and its update fires with opposite phase, returning after two steps. This is checked by substituting the update rule: for \(p_v=1\), \(y_v=x_v-k_v<d_v\); for \(p_v=0\), \(y_v=x_v+k_v\ge d_v\). Thus the number of states for phase vector \(p\) equals \(\prod_vk_v\).

For a tree, the subset \(S\subseteq E\) of edges across opposite phases determines \(p\) up to global complement. The complementary phase is the second state of the same orbit, so each **primitive two-cycle orbit** is counted once by choosing \(S\) and independent chip intervals at all vertices. Therefore
\[
 N(T)=\sum_{S\subseteq E(T)}\prod_{v\in V(T)}\deg_S(v).
\]
This generic phase/cut representation is **not claimed as a new result**; its explicit evaluation and precise asymptotics for full binary trees constitute the result here.

**Step 2: exact binary-branch recursion.** For a rooted height-\(h\) branch with a formal edge to its parent, let \(F_h(\epsilon)\) be the sum of products of selected-edge degrees over all edge selections within the branch, where the formal parent edge is selected exactly if \(\epsilon\in\{0,1\}\). The degrees of all branch vertices include this parent edge where applicable. Put \(A_h=F_h(0)\), \(B_h=F_h(1)\), \(S_h=A_h+B_h\). A lone leaf gives \((A_0,B_0)=(0,1)\). When the root has two isomorphic branches, summing over the two child-edge bits \(\epsilon_1,\epsilon_2\) and multiplying the root degree \(\epsilon+\epsilon_1+\epsilon_2\) gives
\[
 A_h=2B_{h-1}S_{h-1},\qquad
 B_h=S_{h-1}(A_{h-1}+3B_{h-1}).
\]
Thus \(w_h=(A_h,B_h)^{\mathsf T}=S_{h-1}Mw_{h-1}\), with \(M=\begin{pmatrix}0&2\\1&3\end{pmatrix}\) and \(w_0=(0,1)^{\mathsf T}\). If \(M^jw_0=(a_j,b_j)^{\mathsf T}\), then \(a_0=0,a_1=2\) and \(u_j=a_j+b_j\) has \(u_0=1,u_1=5\); both satisfy the characteristic recurrence \(z_{j+2}=3z_{j+1}+2z_j\). Writing \(w_h=T_hM^hw_0\) gives \(T_0=1\) and \(T_{h+1}=T_h^2u_h\). Iterating, \(T_h=\prod_{j=1}^{h-1}u_j^{\,2^{h-1-j}}\). The unparented full tree has count \(N_h=A_h=T_ha_h\), as asserted.

**Step 3: precise asymptotic including the prefactor.** Put \(\Delta=\sqrt{17}\), \(\lambda_+=(3+\Delta)/2\), \(\lambda_-=(3-\Delta)/2\). Solving the recurrence gives \(a_h=2(\lambda_+^h-\lambda_-^h)/\Delta\) and \(u_h=C\lambda_+^h+D\lambda_-^h\), where \(C=(5-\lambda_-)/\Delta>0\) and \(D=(\lambda_+-5)/\Delta\). Since \(|\lambda_-|/\lambda_+<1\),
\[
 \log u_h=h\log\lambda_++\log C+O\!\left((|\lambda_-|/\lambda_+)^h\right).
\]
This implies absolute convergence of the displayed weighted series for \(s\). Taking logarithms in the finite product and comparing with \(2^{h+1}s\) yields
\[
 \log N_h-2^{h+1}s
 =\log a_h-\sum_{k=0}^{\infty}2^{-k-1}\log u_{h+k}
 \longrightarrow\log\frac{2}{\Delta C\lambda_+}
 =\log\frac4{19+5\Delta}.
\]
Since the vertex count equals \(2^{h+1}-1\), the asymptotic prefactor is \(e^s\cdot4/(19+5\Delta)\). No finite computation is used in proving the limiting statement.

## Verification
The accompanying `verify.py` computes the nonlinear branch recursion and separately computes the linear product formula through height four; it exhaustively enumerates all edge subsets through height three and constructs and updates each of the \(9350\) two-cycle orbit representatives at height three (plus the height-one and height-two representatives). An independent full-state enumeration through height two examines \(16\) and \(2304\) bounded chip configurations and finds exactly \(4\) and \(60\) primitive period-two states. Numerical evaluation of \(s\) and \(\kappa\) agrees with the stated constants. See `verification_output.txt`. All finite tests are corroboration, not substitutes for the proof for arbitrary height.

## Relationship to prior work
Bitar–Goles and Jiang establish general finite-graph constraints on parallel chip-firing periodicity and periods on trees; Jiang–Scully–Zhang investigate firing patterns on trees. The elementary two-step phase/cut parameterization also underlies an earlier mass-resolved enumeration for *paths*; none of that generic machinery is claimed original here. What is specifically evaluated here is the number of primitive two-cycle orbits on the complete rooted binary tree at **every** height, with its closed one-dimensional recurrence product and its exact positive asymptotic prefactor per vertex. Inagaki–Khovanova–Luo study a different model, sequential firings on an infinite binary tree with a loop at the root, and do not directly imply this synchronous finite-tree orbit law. Comparisons are bounded by inspected materials; the entire Bitar–Goles article was not available for inspection.

## Limitations
The formula does not resolve the number of initial states eventually entering a two-cycle, since the unrestricted configuration space has unbounded chip totals. It also does not count fixed configurations or mass-resolve the new binary-tree cycles. A stronger, unindexed result in the historical graph-dynamics literature could imply this precise formula; the relevant historical article was not fully accessible. The result is a self-review mathematical analysis, not an independent formal certification.

## References
1. Bitar and Goles (1992), *Parallel chip firing games on graphs*, Theoretical Computer Science 92, 291–300. DOI:10.1016/0304-3975(92)90316-8.
2. Tian-Yi Jiang (2010), *On the Period Lengths of the Parallel Chip-Firing Game*, arXiv:1003.0943v1, https://arxiv.org/abs/1003.0943.
3. Tian-Yi Jiang, Ziv Scully, Yan X Zhang (2012), *Motors and Impossible Firing Patterns in the Parallel Chip-Firing Game*, arXiv:1211.6786v1, https://arxiv.org/abs/1211.6786.
4. Ryota Inagaki, Tanya Khovanova, Austin Luo (2024), *On Chip-Firing on Undirected Binary Trees*, arXiv:2410.00039v1, https://arxiv.org/abs/2410.00039.
