# Exact adjacency inertia of all clique-inserted graphs via full edge subdivision

## Finding
Let \(G\) be any finite connected simple graph with \(n\geq2\) vertices and \(m\geq1\) edges. Subdivide each edge exactly once to form \(S(G)\), and form the line graph \(H=L(S(G))\). For its real symmetric adjacency matrix, let \(\operatorname{In}(H)=(p,z,q)\) denote the numbers of strictly positive, zero, and strictly negative eigenvalues, counted with multiplicity. Then
\[
\operatorname{In}(L(S(G)))=
\begin{cases}
(n,m-n,m), &G\text{ is nonbipartite};\\
(n-1,0,n-1), &G\text{ is a tree};\\
(n-1,2,n-1), &G\text{ is bipartite and }m=n;\\
(n,m-n+1,m-1), &G\text{ is bipartite and }m\geq n+1.
\end{cases}
\]
In particular, the complete inertia is determined solely by the order, size, and bipartiteness of the original graph, even when its degrees vary arbitrarily. The adjacency signature \(p-q\) is never positive. It vanishes exactly when \(G\) is a tree, is unicyclic, or is bipartite with \(m=n+1\) (bicyclic).

## Assumptions and scope
All graphs are finite, undirected, simple, and connected. The single-edge graph is allowed. The edge subdivision \(S(G)\) replaces every edge \(uv\) by the length-two path \(u-e_{uv}-v\), with one new vertex per original edge. The line graph has one vertex per edge of \(S(G)\), and vertices are adjacent precisely when their edges have an endpoint in common. Eigenvalue multiplicities are over the real numbers. No regularity, planarity, or girth hypothesis is imposed. \(n\) and \(m\) always denote the order and size of \(G\), not \(S(G)\).

## Proof
**1. Incidence reduction.** Let \(B\in\mathbb R^{n\times m}\) be the *unsigned* vertex-edge incidence matrix of \(G\), and let \(D\) be its diagonal degree matrix. The subdivided graph \(S(G)\) has \(n+m\) vertices and \(2m\) edges. Its signless Laplacian is
\[
Q(S(G))=\begin{pmatrix}D&B\\ B^{\mathsf T}&2I_m\end{pmatrix}.
\]
Consequently
\[
M=Q(S(G))-2I_{n+m}
=\begin{pmatrix}D-2I_n&B\\B^{\mathsf T}&0_m\end{pmatrix}.
\]

**2. Saddle-point inertia lemma.** For an arbitrary real \(n\times m\) matrix \(B\) of rank \(r\), and an arbitrary real symmetric \(C\) of order \(n\), consider \(\mathcal M=\left(\begin{smallmatrix}C&B\\B^{\mathsf T}&0\end{smallmatrix}\right)\). If \(C_0\) is the quadratic-form restriction of \(C\) to \(\ker B^{\mathsf T}\), then
\[
\operatorname{In}(\mathcal M)
=(r,0,r)+\operatorname{In}(C_0)+(0,m-r,0).
\]
To prove this, choose orthonormal bases that split the first space as \(\operatorname{im}B\oplus\ker B^{\mathsf T}\) and the second as \((\ker B)^\perp\oplus\ker B\). In these bases the off-diagonal block contains one invertible \(r\times r\) block \(R\) and otherwise zeros. The paired block \(\left(\begin{smallmatrix}C_{11}&R\\R^{\mathsf T}&0\end{smallmatrix}\right)\) is congruent to \(\left(\begin{smallmatrix}0&R\\R^{\mathsf T}&0\end{smallmatrix}\right)\): eliminate \(C_{11}\) by a triangular congruence using invertibility of \(R\). Its inertia is \((r,0,r)\). The cross term \(C_{10}\) between the paired part and \(\ker B^{\mathsf T}\) can likewise be eliminated by shifting the second member of the paired coordinates, leaving precisely the restriction \(C_0\). The \(m-r\) unpaired second coordinates contribute zeros. This is an exact congruence argument, not an eigenvalue approximation.

**3. Rank and restriction.** Because \(G\) is connected, a vector \(x\in\ker B^{\mathsf T}\) satisfies \(x_u+x_v=0\) along every edge. If \(G\) is nonbipartite, an odd cycle forces \(x=0\), so \(r=n\). If it is bipartite, \(\ker B^{\mathsf T}\) is spanned by the vector \(\sigma\) which takes value \(+1\) on one part and \(-1\) on the other; hence \(r=n-1\). With \(C=D-2I_n\), the restricted form in the bipartite case is governed by
\[
\sigma^{\mathsf T}C\sigma=\sum_{v\in V(G)}(\deg_G(v)-2)=2(m-n).
\]
The sign is negative for trees \(m=n-1\), zero for bipartite unicyclic graphs \(m=n\), and positive for bipartite graphs with \(m\ge n+1\). Substituting into the saddle-point lemma gives
\[
\operatorname{In}(M)=
\begin{cases}
(n,m-n,n), &G\text{ nonbipartite},\\
(n-1,0,n), &G\text{ bipartite},\ m=n-1,\\
(n-1,2,n-1), &G\text{ bipartite},\ m=n,\\
(n,m-n+1,n-1), &G\text{ bipartite},\ m\ge n+1.
\end{cases}
\]

**4. Transfer to the line graph.** Let \(T\in\mathbb R^{(n+m)\times 2m}\) be the unsigned vertex-edge incidence matrix of \(S(G)\). Then \(TT^{\mathsf T}=Q(S(G))\) and \(T^{\mathsf T}T=A(L(S(G)))+2I_{2m}\). The matrices have the same *positive* eigenvalues, counted with multiplicity. Since \(S(G)\) is connected and bipartite, \(\operatorname{rank}T=n+m-1\); in particular, \(Q(S(G))\) has exactly one zero eigenvalue and \(T^{\mathsf T}T\) has exactly \(2m-(n+m-1)=m-n+1\) zero eigenvalues. Subtracting two from both spectra, the positive and zero inertia counts of \(A(L(S(G)))\) agree with those of \(M\), while its negative count is the negative count of \(M\) minus one plus \(m-n+1\), namely an increment of \(m-n\). This yields each case of the claimed formula, including the tree boundary \(m=n-1\).

**5. Signature criterion.** In the four cases the signature is, respectively, \(n-m\), \(0\), \(0\), and \(n-m+1\). Connected nonbipartite graphs have \(m\ge n\), while connected bipartite graphs with \(m\ge n+1\) have nonpositive \(n-m+1\). Equality occurs as stated; \(m=n\) is unicyclic for any connected graph, and \(m=n+1\) is bicyclic.

## Verification
The standalone program `verify.py` independently builds \(L(S(G))\) from the edge sets, computes adjacency inertia by exact rational symmetric congruence (no floating-point eigenvalues), and checks all four formulas. It covers all connected labelled graphs on \(2\), \(3\), \(4\), and \(5\) vertices (counts \(1,4,38,728\)) and another \(126\) sparse, dense, and structured connected cases, \(897\) cases in total. Run `python3 verify.py`; expected stdout is embedded as `verification_output.txt`. These are finite corroborations; steps 1–5 are the proof for arbitrary order.

## Relationship to prior work
Francis and Uptain (2026) show that the signature of general connected line graphs is unbounded above, establishing the motivating contrast. Paone (2026) studies additional counterexamples and general four-subdivision transfer principles; neither inspected treatment supplies the complete one-subdivision-per-edge inertia classification for arbitrary irregular input graphs. Zhang, Chen, and Chen (2009) derive characteristic polynomials of clique-inserted **regular** graphs. Chen, Hou, and Li (2016), Section 2, likewise give a spectral formula for para-line graphs of **regular** input graphs. Therefore the regular-input specialization of the displayed inertia formula is already implied by previous full-spectrum work and is **not** claimed as a new special-case result. The claimed extension is its universality over arbitrary connected **irregular** input graphs and the resulting exact three-parameter classification. Signed/unsigned incidence spectral identities and Sylvester's law of inertia are standard ingredients and are not claimed as new lemmas.

## Limitations
No definitive priority claim is made: a differently named earlier treatment of the irregular-input case could exist. The 2009 publisher full text was not available for material inspection; its accessible abstract specifically describes regular input graphs, so it is not evidence of an irregular-input theorem. The conclusion applies only to graphs obtained by subdividing **every** original edge exactly once and then taking the line graph, not to arbitrary line graphs or selective subdivisions. Independent mathematical validation has not been performed.

## References
1. Luke Francis and Trevor Uptain, *The signature of connected line graphs is unbounded*, arXiv:2607.22874, first submitted July 24, 2026. https://arxiv.org/abs/2607.22874
2. Andrea Paone, *Unbounded Signature of Line Graphs: Counterexamples and Transfer Principles*, version 2 (July 24, 2026). https://www.researchgate.net/publication/410810290_Unbounded_Signature_of_Line_Graphs_Counterexamples_and_Transfer_Principles
3. Fuji Zhang, Yi-Chiuan Chen, and Zhibo Chen, *Clique-inserted-graphs and spectral dynamics of clique-inserting*, Journal of Mathematical Analysis and Applications 349 (2009), 211–225. https://doi.org/10.1016/j.jmaa.2008.08.036
4. Xiaodan Chen, Yaoping Hou, and Jingjian Li, *On two energy-like invariants of line graphs and related graph operations*, Journal of Inequalities and Applications 2016, article 51 (2016). https://doi.org/10.1186/s13660-016-0996-1
