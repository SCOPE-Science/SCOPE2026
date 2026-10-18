# Exact one-edge controllability ranks in primitive strongly regular networks

## Finding

Let \(G\) be any finite primitive strongly regular graph with parameters \((N,k,\lambda,\mu)\): \(G\) and its complement are both connected, every vertex has degree \(k\), every adjacent pair has \(\lambda\) common neighbors, and every nonadjacent pair has \(\mu\) common neighbors. Choose any edge \(\{u,v\}\). Assign positive conductance \(c\) to this edge and conductance one to every other edge; let \(L_c\) be the weighted Laplacian. For an actuator at vertex \(w\), define the reachable dimension
\[
R_c(w)=\operatorname{rank}\,[e_w,L_ce_w,\ldots,L_c^{N-1}e_w].
\]
Then for every \(c>0\),
\[
R_c(w)=\begin{cases}
3,&c=1,\\
5,&c\ne1\text{ and }[w\in\{u,v\}\text{ or }(A_{wu}\ne A_{wv})],\\
3,&c\ne1\text{ and }w\notin\{u,v\},\ A_{wu}=A_{wv}.
\end{cases}
\]
Here \(A\) is the original zero-diagonal adjacency matrix. Exactly \(2(k-\lambda)\) actuator vertices have rank five for every positive nonunit edge conductance. The remaining \(N-2(k-\lambda)\) have rank three, and no exceptional nonunit positive conductance occurs. Equivalently, the changed edge creates two additional actuator-visible modes precisely at its endpoints and at vertices distinguishing its endpoints by adjacency.

For a five-cycle the four rank-five positions individually control the whole network. For any primitive strongly regular graph with more than five vertices, no single vertex controls the entire network after this one-edge perturbation.

## Assumptions and scope

Graphs are undirected, simple, noncomplete, and primitive; \(N\ge5\), \(0<k<N-1\), and \(c>0\). Dynamics are \(\dot x=-L_c x+e_w f(t)\) over the real field, with a single scalar independent input at vertex \(w\). Controllability rank is the dimension of the reachable linear subspace, not a statement that the full system is controllable for all orders. The edge \(\{u,v\}\) may be arbitrarily chosen. Every quantifier ranges over all graph realizations having the stated properties, all their edges, all their actuator vertices, and every positive conductance \(c\). The case \(c=0\), imprimitive graphs, multiple perturbed edges, and multiple independent actuators are excluded.

## Proof

**Spectral preliminaries.** Write the three distinct adjacency eigenvalues as \(k>r>s\) and let \(E_0=J/N,E_r,E_s\) be the corresponding orthogonal spectral projectors. Primitivity gives \(r>0\) and \(s<-1\). Put \(a=k-r\), \(b=k-s\) and \(d=e_u-e_v\). The spectral projectors admit the explicit expressions
\[
E_r=\frac{A-sI-(k-s)J/N}{r-s},\qquad
E_s=\frac{A-rI-(k-r)J/N}{s-r}.
\]
The ordinary Laplacian is \(L_1=kI-A\), so \(L_c=L_1+(c-1)dd^T\). Since the perturbed edge is adjacent,
\[
\gamma_r=\|E_rd\|^2=\frac{2(-1-s)}{r-s}>0,
\qquad\gamma_s=\|E_sd\|^2=\frac{2(r+1)}{r-s}>0,
\qquad E_0d=0.
\]

**The two new eigenvalues.** Put \(\delta=c-1\). When \(\delta\ne0\), on the two-dimensional span of \(E_rd\) and \(E_sd\), the Laplacian has exactly two simple eigenvalues \(t_1,t_2\), the roots of
\[
1-\delta\left(\frac{\gamma_r}{t-a}+\frac{\gamma_s}{t-b}\right)=0.
\]
Both roots are distinct from \(a,b\): evaluating the cleared quadratic at \(a\) and \(b\) yields respectively nonzero multiples of \(\delta\gamma_r\) and \(\delta\gamma_s\). They are also distinct from one another since the restricted matrix is real symmetric with a nonzero off-diagonal entry \(\delta\sqrt{\gamma_r\gamma_s}\). Since all conductances remain positive, the graph is connected, so both are strictly positive and not zero. The subspaces \(E_r\mathbb R^N\cap d^\perp\) and \(E_s\mathbb R^N\cap d^\perp\) retain eigenvalues \(a,b\), respectively; both are nonzero as the primitive strongly regular nontrivial eigenvalue multiplicities are at least two. Together with the constant eigenvector at zero, the perturbed operator has exactly five distinct eigenvalues. For each new root \(t\), its eigenvector is proportional to
\[
q_t=\frac{E_rd}{t-a}+\frac{E_sd}{t-b}.
\]

**Visibility of the new eigenvalues.** If \(w\notin\{u,v\}\), then
\[
(E_rd)_w=\frac{A_{wu}-A_{wv}}{r-s},\qquad
(E_sd)_w=-\frac{A_{wu}-A_{wv}}{r-s},
\]
so
\[
(q_t)_w=\frac{A_{wu}-A_{wv}}{r-s}
\left(\frac1{t-a}-\frac1{t-b}\right).
\]
The parenthetical factor cannot vanish because \(a\ne b\), so each new eigenvalue is visible from \(w\) precisely when the two adjacencies differ. At the endpoints, the equal diagonal entries of each original spectral projector give \((E_\ell d)_u=\gamma_\ell/2\) and \((E_\ell d)_v=-\gamma_\ell/2\) for \(\ell\in\{r,s\}\). The secular equation therefore gives \((q_t)_u=1/(2\delta)\) and \((q_t)_v=-1/(2\delta)\). Both new eigenvalues are visible at both endpoints, uniformly for all nonunit \(c>0\).

**Visibility of the three original eigenvalues.** The constant eigenvector at zero is visible from every vertex. We establish that neither residual eigenspace at \(a\) or \(b\) is orthogonal to any \(e_w\). Let \(S\) be the set of vertices other than \(u,v\) adjacent to both or to neither endpoint. Its size is \(N-2(k-\lambda)>0\). If \(\lambda>0\), the common neighbors suffice. If \(\lambda=0\), the strongly regular parameter identity
\[
(N-k-1)\mu=k(k-1)
\]
and strict \(\mu<k\) (otherwise the complement is disconnected) imply \(N>2k\). Thus \(S\) is nonempty in either case. For every \(x\in S\), \((E_rd)_x=(E_sd)_x=0\). For each of \(E_r,E_s\), its off-diagonal entries are nonzero: if \(x\ne w\), these entries are a nonzero multiple of \(A_{xw}-(k-s)/N\) or \(A_{xw}-(k-r)/N\), respectively; both fractions lie strictly between zero and one. The first strict upper inequality follows from connectedness of the complement and the positive complement eigenvalue \(-1-s\), which is strictly smaller than complement valency \(N-k-1\); the second follows from \(0<r<k<N\).

If \(w\in S\), each \(E_\ell e_w\) is nonzero because every diagonal entry of a nonzero spectral idempotent of a strongly regular graph is its positive rank divided by \(N\), whereas \((E_\ell d)_w=0\). If \(w\notin S\), choose \(x\in S\): then \((E_\ell d)_x=0\), while \((E_\ell e_w)_x\ne0\). Hence \(E_\ell e_w\) is never proportional to \(E_\ell d\). Consequently its projection onto the residual eigenspace \(E_\ell\mathbb R^N\cap d^\perp\) is nonzero, and the inherited eigenvalues \(a,b\) are visible from every vertex.

**Reachability and counting.** For a real symmetric matrix and one actuator, the Krylov dimension equals the number of distinct eigenvalues whose spectral projectors do not annihilate the actuator. Hence the three inherited eigenvalues always contribute three, and the two new eigenvalues contribute either both or neither according to the preceding visibility test. At \(c=1\), the three original projectors all have positive diagonal entries, so every rank is three. For \(c\ne1\), the distinguishing outsider vertices consist of \(k-1-\lambda\) exclusive neighbors on each side; adding both endpoints gives \(2+2(k-1-\lambda)=2(k-\lambda)\) rank-five vertices, as asserted. This completes the proof.

## Verification

The accompanying self-contained Python script `verify_srg.py` performs exact rational Gaussian elimination for all single-vertex Krylov ranks, for every edge of eight representative strongly regular graphs, with conductances \(1/2,1,3/2,2\). It verifies their strongly regular parameters and the predicted rank at each vertex; all \(14846\) exact finite assertions pass. Tested graph orders range from five through sixteen and include the five-cycle, Petersen graph, rook graphs, triangular graphs, a Paley graph and the Shrikhande graph. Run using `python3 verify_srg.py`; no third-party packages are needed. These finite checks corroborate but do not establish the all-graph, all-positive-conductance theorem; the proof above does.

## Relationship to prior work

The standard symmetric-system Popov–Belevitch–Hautus/eigenvalue-support criterion supplies the link between eigenspaces and reachable rank. Notarstefano and Parlangeli (2012) study Laplacian controllability on grid graphs; Aguilar and Gharesifard (2015) study general Laplacian leader-follower controllability and observe the three-eigenvalue structure of unweighted strongly regular graphs. Godsil's *State transfer on graphs* (2012) relates a vertex's walk-matrix rank to its eigenvalue support.

Godsil, Guo, Kempton and Lippner (2017/2019) analyze adjacency matrices with an edge-plus-loop perturbation, including the corresponding special case of a weighted-Laplacian edge defect under a scalar spectral shift. In particular, their quadratic secular eigenvalue equation substantially overlaps the eigenvalue calculation above. Their results concern edge-endpoint state transfer and spectral support, and the inspected article does not give the exact **every-vertex** single-actuator reachability dichotomy or the count \(2(k-\lambda)\). Those rely additionally on evaluating both new eigenvectors at arbitrary vertices and proving the two inherited eigenspaces remain actuator-visible. The spectral perturbation and PBH methods are prior tools, not claimed discoveries. A future comparison might reveal an implicit equivalent in specialized literature.

## Limitations

The finding is a theorem about fixed single-edge conductance defects of primitive strongly regular graphs. It does not characterize control with multiple inputs, full controllability in larger graphs, uncertain conductances, weighted base graphs, disconnected complements, or perturbed edges of other kinds. No independent mathematical audit or external formal verification has been performed. The paper's 2017 secular equation is a close antecedent, and possible implicit or unindexed coverage is a residual originality risk.

## References

1. G. Notarstefano and G. Parlangeli, *Controllability and observability of grid graphs via reduction and symmetries*, arXiv:1203.0129 (first public version 2012-03-01), https://arxiv.org/abs/1203.0129.
2. C. O. Aguilar and B. Gharesifard, *Graph Controllability Classes for the Laplacian Leader-Follower Dynamics*, IEEE Transactions on Automatic Control 60 (2015), 1611–1623, DOI:10.1109/TAC.2014.2381435.
3. C. Godsil, *State transfer on graphs*, Discrete Mathematics 312 (2012), 129–147, DOI:10.1016/j.disc.2011.06.032.
4. C. Godsil, K. Guo, M. Kempton and G. Lippner, *State transfer in strongly regular graphs with an edge perturbation*, arXiv:1710.02181 (first public version 2017-10-05), DOI:10.1016/j.jcta.2019.105181.
