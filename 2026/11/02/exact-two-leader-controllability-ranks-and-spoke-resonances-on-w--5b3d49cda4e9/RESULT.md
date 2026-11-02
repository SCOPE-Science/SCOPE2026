# Exact two-leader controllability ranks and spoke resonances on weighted wheels

## Finding
Consider the weighted wheel consisting of a ring of \(n\ge3\) vertices plus one hub. Its ring edges all have conductance \(1\), and its spokes all have conductance \(g>0\). Two independently actuated ring vertices are separated by cyclic offset \(d\in\{1,\ldots,n-1\}\). For the continuous-time consensus system \(\dot z=-Lz+Bu\), where \(L\) is its weighted Laplacian and \(B=[e_0,e_d]\), define \(r(n,d,g)\) as the Kalman controllability rank.

Put
\[
q=\begin{cases}\gcd(n,d),&n\text{ odd},\\\gcd(n/2,d),&n\text{ even},\end{cases}\qquad
r_0=\begin{cases}n+1-(q-1)/2,&n\text{ odd},\\n+2-q,&n\text{ even},\end{cases}
\]
and for \(1\le k\le\lfloor n/2\rfloor\), define
\[
\gamma_k=\frac{2-2\cos(2\pi k/n)}{n}.
\]
The \(\gamma_k\) are strictly increasing. If \(g\notin\{\gamma_k\}\), then \(r(n,d,g)=r_0\). If \(g=\gamma_k\), then
\[
r(n,d,\gamma_k)=r_0-\delta_{n,d,k},\qquad
\delta_{n,d,k}=\begin{cases}
0,&n\text{ even},\ k=n/2,\ d\text{ odd},\\
0,&n\text{ even},\ k<n/2,\ n\mid2kd,\ n\nmid kd,\\
1,&\text{otherwise}.
\end{cases}
\]
In particular, for odd \(n\), full controllability is equivalent to \(\gcd(n,d)=1\) and avoidance of *all* resonant spoke weights. For even \(n\), it is equivalent to \(\gcd(n/2,d)=1\), avoidance of \(\gamma_k\) for all \(k<n/2\), and additionally either \(d\) odd or \(g\ne4/n\). The exact dimension of the uncontrollable subspace is \(n+1-r(n,d,g)\).

An important phenomenon is that all but finitely many positive spoke weights have the same controllability rank, while a single isolated weight can reduce it by exactly one. The exceptional loss can vanish when the two ring actuators separate the hub mode from the collided ring mode; it is therefore not determined by eigenvalue multiplicity alone.

## Assumptions and scope
The vertices are indexed \(0,\ldots,n-1\) on the ring and \(n\) at the hub. Each undirected ring edge \(\{j,j+1\bmod n\}\) has weight \(1\), each spoke \(\{j,n\}\) has weight \(g>0\). For \(n=3\) the ring is the triangle. The control vector has two distinct arbitrary real-valued inputs acting additively at ring vertices \(0\) and \(d\); the hub is not directly actuated. The rank is computed from \([B,LB,\ldots,L^nB]\), which has the same rank for \(L\) and \(-L\). There is no restriction on final time beyond standard finite-dimensional controllability.

The theorem assumes an exactly identical spoke weight across all ring vertices, and an identical rim weight. It does not characterize nonuniform weighted wheels, sensor noise, optimal control energy or time-varying controls. Positive uniform rescaling of every edge leaves the rank unchanged; normalizing ring conductances to \(1\) is therefore without loss within the two-class uniform family.

## Proof
**1. Spectral splitting.** Let \(\Lambda_k=2-2\cos(2\pi k/n)\). The constant vector has Laplacian eigenvalue \(0\). The hub-versus-ring vector \(v=(1,\ldots,1,-n)^\mathsf T\) has eigenvalue \((n+1)g\). In the ring zero-sum subspace, the Fourier mode of frequency \(k\ne0\), extended by zero at the hub, has eigenvalue \(g+\Lambda_k\). Every frequency pair \(k,n-k\) with \(1\le k<n/2\) gives a real two-dimensional eigenspace spanned by cosine and sine. When \(n\) is even, the \(k=n/2\) alternating mode forms a one-dimensional eigenspace. The \(\Lambda_k\) are strictly increasing for \(1\le k\le\lfloor n/2\rfloor\), so distinct ring-frequency eigenspaces do not collide. A hub-mode/ring-mode collision occurs exactly at \((n+1)g=g+\Lambda_k\), equivalently \(g=\gamma_k\); no other collisions are possible because \(g>0\).

**2. Rank by eigenspaces.** For a real symmetric matrix \(L\) with spectral projectors \(P_\lambda\), the columns of \([B,LB,\ldots,L^nB]\) span the orthogonal direct sum of \(\mathrm{range}(P_\lambda B)\). One inclusion is immediate from the spectral decomposition; the reverse follows by Lagrange interpolation of spectral projectors as polynomials in \(L\). Thus the Kalman rank equals \(\sum_\lambda\mathrm{rank}(P_\lambda B)\). On an eigenspace this is the rank of the two point-evaluation functionals at \(0\) and \(d\).

The constant and hub-versus-ring modes each evaluate nontrivially and hence each contribute \(1\) when their eigenvalues are distinct from ring frequencies. For a paired ring frequency \(k\), the two evaluations of its cosine and sine basis have matrix
\[
\begin{pmatrix}1&0\\\cos(2\pi kd/n)&\sin(2\pi kd/n)\end{pmatrix}.
\]
It has rank \(2\) unless \(n\mid2kd\), when its rank is \(1\). The even-\(n\) alternating frequency always contributes \(1\) when nonresonant.

**3. Arithmetic count.** If \(n\) is odd, the condition \(n\mid2kd\) is equivalent to \(n\mid kd\). Writing \(q=\gcd(n,d)\), the admissible bad frequencies are the positive multiples of \(n/q\) below \(n/2\), exactly \((q-1)/2\) of them. If \(n\) is even, write \(N=n/2\) and \(q=\gcd(N,d)\). The bad paired frequencies are multiples of \(N/q\) strictly below \(N\), exactly \(q-1\) of them. Subtracting these losses from the total \(n+1\) eigenvector dimensions yields the stated \(r_0\).

**4. Collisions and exceptional cancellations.** At \(g=\gamma_k\) with \(k<n/2\), the hub-versus-ring mode and the ring \(k\)-pair have the same eigenvalue. Their observation columns are represented by
\[
\begin{pmatrix}1&1&0\\1&\cos\theta&\sin\theta\end{pmatrix},\qquad\theta=2\pi kd/n.
\]
Without a collision these two invariant subspaces would contribute \(1+\operatorname{rank}\begin{psmallmatrix}1&0\\\cos\theta&\sin\theta\end{psmallmatrix}\). If \(\sin\theta\ne0\), the merged rank is \(2\) rather than \(3\), a loss of \(1\). If \(\sin\theta=0\) and \(\cos\theta=1\), the merged rank is \(1\) rather than \(2\), again a loss of \(1\). If \(\sin\theta=0\) and \(\cos\theta=-1\), the merged rank remains \(2\) rather than \(2\), so the loss vanishes. The last case is exactly \(n\mid2kd\) and \(n\nmid kd\), possible only for even \(n\).

At even-\(n\) frequency \(k=n/2\), the merged hub-versus-ring and alternating modes evaluate as \((1,1)^\mathsf T\) and \((1,(-1)^d)^\mathsf T\). Their rank is \(2\) for odd \(d\), and \(1\) for even \(d\). This proves the complete collision formula. Because the collision weights are distinct, only one loss correction is ever applied. The asserted full-rank conditions follow by setting \(r_0=n+1\) and requiring zero collision loss. The proof covers every integer \(n\ge3\), every allowed offset and every real \(g>0\).

## Verification
The accompanying `check.py` implements the rank formula separately from direct wheel-Laplacian construction and verifies \(3,286\) rank identities. It independently compares spectral projector ranks for all \(3\le n\le26\), every ring offset and each resonant weight plus a nonresonant weight. For exact rational resonance cases at \(n=3,4,6,8,12\), and additional nonresonant weights, it computes the exact rational Kalman matrix rank with symbolic arithmetic. Both verification methods passed. The general theorem rests on the spectral and arithmetic proof above, not extrapolation from this finite test.

Reproduce with \`python check.py\` using Python 3, NumPy and SymPy. No unavailable external dataset is required.

## Relationship to prior work
Rahmani, Ji, Mesbahi and Egerstedt [1] introduced graph-theoretic and equitable-partition analyses of leader controllability. Parlangeli and Notarstefano [2] investigate exact reachability and observability for pure paths and cycles; those graphs have no hub eigenmode, so they do not directly supply the weighted-wheel collision corrections derived here. Yazicioglu, Abbas and Egerstedt [3] prove a distance-based lower bound applicable to arbitrary positive edge weights; because the lower bound is weight independent, it does not by itself determine the isolated spoke-weight losses calculated here. A later study by Liu and Ji [4] gives path/cycle controllable-subspace dimensions and discusses graphs generated from those topologies; its complete text was not accessible for an exhaustive comparison. No exact weighted-wheel rank-and-resonance classification was located in the examined sources. This is a qualified literature comparison, not a proof of historical uniqueness.

## Limitations
The assumptions of two independent ring controls and two uniform positive edge-weight classes are essential. The rank formulas do not extend automatically to inputs at the hub or to heterogeneous spokes. The finite verifier is supplementary; independent mathematical assessment and broader historical-literature inspection have not been performed. Source [4], particularly its further examples based on cycles, is a specific unresolved coverage risk.

## References
[1] A. Rahmani, M. Ji, M. Mesbahi and M. Egerstedt, *Controllability of Multi-Agent Systems from a Graph-Theoretic Perspective*, SIAM J. Control Optim. 48 (2009), 162–186, DOI: https://doi.org/10.1137/060674909. First published online 2009-02-11.

[2] G. Parlangeli and G. Notarstefano, *On the Reachability and Observability of Path and Cycle Graphs*, arXiv:1109.3556 (initial version 2011-09-16), https://arxiv.org/abs/1109.3556.

[3] A. Y. Yazicioglu, W. Abbas and M. Egerstedt, *Graph Distances and Controllability of Networks*, arXiv:1608.04309 (2016-08-15), https://arxiv.org/abs/1608.04309.

[4] X. Liu and Z. Ji, *Controllability of Multiagent Systems Based on Path and Cycle Graphs*, International Journal of Robust and Nonlinear Control 28 (2018), 296–309, DOI: https://doi.org/10.1002/rnc.3870 (first online 2017-06-30).
