# Three-step extinction rigidity and parity-swapped cycles on subdivided cliques

## Finding

Let \(G\) be a finite connected simple graph with at least two vertices. Replace every edge by a path of length two, with a distinct new middle vertex for each edge, to obtain its ordinary subdivision \(S(G)\). Over any finite field \(\mathbb F_q\) of characteristic two, let \(F_G\) synchronously replace each vertex state by the sum of its open neighbors' states. Then

\[
F_G^3=0\quad\Longleftrightarrow\quad G\cong K_n\text{ for an even integer }n\ge2.
\]

For every such clique the minimal extinction exponent is exactly three. On the complementary family of odd-order complete graphs, \(F_{K_n}^3=F_{K_n}\), and all periodic states form a direct product of two even-sum spaces on which one step swaps the factors. Exact finite-field orbit and attraction-basin counts follow in either case.

## Assumptions and scope

A graph is finite, simple, connected, undirected and has at least two vertices. Every edge of \(G\) contributes exactly one new degree-two vertex to \(S(G)\); no edges of \(G\) remain unsplit. Choose any finite field \(\mathbb F_q\), \(q=2^f\) with \(f\ge1\). The rule is the *unweighted, zero-diagonal, simultaneous open-neighborhood sum* (binary neighbor-XOR when \(q=2\)); no other Boolean or weighted interaction functions are considered.

Write \(n=|V(G)|\), \(m=|E(G)|\), and let \(B\in\mathbb F_q^{n\times m}\) be the unoriented vertex-edge incidence matrix with two unit entries in each edge column. In the original-vertex/new-edge-vertex ordering,

\[
F_G=\begin{pmatrix}0&B\\B^{\mathsf T}&0\end{pmatrix},\qquad
L=BB^{\mathsf T}=D_G+A_G\pmod 2.
\]

Here \(D_G\) is the diagonal degree matrix, and \(A_G\) the usual zero-diagonal adjacency matrix. For a clique put \(N=n+\binom n2\), the total number of vertices of its subdivision, and \(W=\{z\in\mathbb F_q^n:\sum_{i=1}^n z_i=0\}\).

## Proof

**Rigidity among all connected bases.** Direct multiplication gives

\[
F_G^3=\begin{pmatrix}0&LB\\B^{\mathsf T}L&0\end{pmatrix}.
\]

Because \(L\) is symmetric, \(F_G^3=0\) exactly when \(LB=0\). The column of \(B\) associated with an edge \(uv\) is \(e_u+e_v\). Thus \(LB=0\) forces columns \(u\) and \(v\) of \(L\) to coincide for each edge. Connectedness forces all columns of \(L\) to coincide. Symmetry then forces \(L=cJ_n\), with \(J_n\) the all-ones matrix and a single scalar \(c\). As the off-diagonal entry corresponding to any edge equals one, \(c=1\). Every off-diagonal entry is now one, hence \(G=K_n\). Its diagonal entries are the parity of \(n-1\), which equal one precisely for even \(n\). Conversely, on even \(K_n\), \(L=J_n\), and \(J_nB=0\) because every column of \(B\) has two unit entries. Therefore \(F_G^3=0\). Since the upper-left block of \(F_G^2\) is \(J_n\ne0\), the minimal exponent is exactly three.

**Incidence ranks.** For a connected graph the image of \(B\) is \(W\), and \(\ker B^{\mathsf T}=\langle\mathbf1\rangle\). Indeed, each edge column has coordinate sum zero; a path connects any pair and the sums of its edge columns give the corresponding two-coordinate vector. These vectors span \(W\). The kernel statement follows because \(B^{\mathsf T}z=0\) makes the endpoint values of \(z\) equal along every edge. Thus \(\operatorname{rank}B=n-1\), so \(\operatorname{rank}F_G=2(n-1)\).

**Even-order cliques.** Here \(L=J_n\), which has rank one. The restriction \(B^{\mathsf T}|_W\) has one-dimensional kernel: \(\mathbf1\in W\) because \(n\) is even. Consequently \(\operatorname{rank}(B^{\mathsf T}B)=n-2\). The block structure yields

\[
\bigl(\operatorname{rank}F_G^0,\operatorname{rank}F_G^1,
\operatorname{rank}F_G^2,\operatorname{rank}F_G^3\bigr)
=\bigl(N,2(n-1),n-1,0\bigr).
\]

The successive rank differences determine the nilpotent Jordan form uniquely:

\[
F_G\sim J_3(0)^{\oplus(n-1)}\oplus
J_1(0)^{\oplus\binom{n-2}{2}}.
\]

All states eventually become zero. Since every linear map over \(\mathbb F_q\) has \(q^{N-\operatorname{rank}}\) elements in its kernel, the exact numbers of configurations first reaching zero at times \(t=0,1,2,3\), respectively, are

\[
1,\qquad q^{N-2(n-1)}-1,\qquad
q^{N-(n-1)}-q^{N-2(n-1)},\qquad
q^N-q^{N-(n-1)}.
\]

These cases partition all \(q^N\) configurations. The positive number in the final class witnesses sharpness.

**Odd-order cliques.** Here \(L=I_n+J_n\). Again \(J_nB=0\), so \(LB=B\), implying \(F_G^3=F_G\). Now \(\mathbf1\notin W\); therefore \(B^{\mathsf T}|_W\) is injective and \(\operatorname{rank}F_G^2=2(n-1)\). Every state in \(\operatorname{im}F_G\) is periodic and, conversely, every periodic state belongs to this image: \(F_G\) is invertible on its image, with square the identity, while every state maps there after one update.

The image is exactly the \(2(n-1)\)-dimensional space

\[
\{(u,B^{\mathsf T}v):u,v\in W\}.
\]

For \(u,v\in W\), use \(BB^{\mathsf T}v=(I_n+J_n)v=v\) to obtain

\[
F_G(u,B^{\mathsf T}v)=(v,B^{\mathsf T}u).
\]

This is a swap involution. Fixed states correspond to \(u=v\), hence number \(q^{n-1}\). The remaining \(q^{2(n-1)}-q^{n-1}\) periodic states pair into primitive two-cycle orbits, giving \((q^{2(n-1)}-q^{n-1})/2\) orbits. The Jordan form is

\[
F_G\sim J_2(1)^{\oplus(n-1)}\oplus
J_1(0)^{\oplus d},\qquad d=N-2(n-1).
\]

Every periodic state has exactly \(q^d\) one-step preimages. Thus each fixed-point basin has \(q^d\) initial configurations and each primitive two-cycle basin has \(2q^d\); the periodic-entry-time counts are \(q^{2(n-1)}\) at time zero and \(q^N-q^{2(n-1)}\) at time one. The latter count is positive for \(n\ge3\), so the one-update entrance bound is sharp.

## Verification

The accompanying `check_incidence.py` computes binary matrix powers and ranks without invoking the symbolic proof; it checks the full rigidity equivalence for every labelled connected simple base graph on two through six vertices, all complete-graph iterate ranks through order fourteen, and complete state censuses through order five. The independent `check_states.cpp` implements the rule directly on labelled states and checks all \(2^{21}\) configurations on \(S(K_6)\), as well as smaller cases. Both outputs end in explicit success markers. These finite checks corroborate, but do not establish, the universally quantified statement; the graph- and field-uniform proof above establishes that statement.

## Relationship to prior work

Linear finite dynamical systems and finite-field automata are treated by Moreno, Bollman and Aviño-Díaz [1]. Gadouleau and Richard [2] study whether an interaction graph *admits some* nilpotent Boolean function, and prove an existence theorem for many graphs; that existential freedom is distinct from the present prescribed all-neighbors-sum rule. Barrett and collaborators [3] analyze minimum ranks over families of admissible symmetric matrices on subdivision graphs, rather than the fixed zero-diagonal adjacency update and its powers. Spectral constructions on subdivision-corona graphs are discussed by Lu and Miao [4], but do not give the present finite-characteristic dynamical classification. This result's claim is specifically the connected-graph rigidity and complete parity-dependent orbit/basin census under one fixed rule.

## Limitations

The rigidity statement requires connectedness and ordinary *simple* graphs; for disconnected bases, components may behave independently. All conclusions are for unweighted zero-diagonal adjacency updating over characteristic two. A weighted matrix, a self-inclusive rule, or a field of odd characteristic is outside scope. The computational checks cover only finite enumerated examples, and do not independently certify the infinite-family proof. Historical literature not indexed in accessible searches may contain an equivalent special case.

## References

[1] O. Moreno, D. Bollman, M. A. Aviño-Díaz, *Finite Dynamical Systems, Linear Automata, and Finite Fields*, arXiv:math/0604534v1 (first arXiv public release 2006-04-25), https://arxiv.org/abs/math/0604534.

[2] M. Gadouleau, A. Richard, *Simple dynamics on graphs*, arXiv:1503.04688 (first arXiv public release 2015-03-16), https://arxiv.org/abs/1503.04688.

[3] W. Barrett, R. Bowcutt, M. Cutler, S. Gibelyou, K. Owens, *Minimum Rank of Edge Subdivisions of Graphs*, Electronic Journal of Linear Algebra 18 (2009), 530–563, https://journals.uwyo.edu/index.php/ela/article/view/661.

[4] L. Lu, F. Miao, *Spectra of the subdivision-vertex and subdivision-edge coronae*, arXiv:1302.0457, https://arxiv.org/abs/1302.0457.
