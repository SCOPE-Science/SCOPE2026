# Perfect continuous-time random-walk search occurs exactly at cones over regular graphs
## Finding
For a connected finite simple undirected loopless graph \(G\) with at least two vertices, use the degree-reversible random-walk Laplacian and the rank-one marked-vertex oracle. Search from the normalized stationary state succeeds with probability exactly one at some positive time and positive hopping parameter **if and only if** the marked vertex \(w\) is universal and the graph obtained by deleting it is regular. Thus the successful marked graphs are exactly cones over regular graphs (the regular base may be disconnected).

If the base has \(k\) neighbors per base vertex, with integer \(k\ge0\), the unique successful hopping parameter and exact probability law are
\[
\gamma_* = \frac{k+1}{k+2},\qquad p_{\gamma_*}(t)=\frac{1}{k+2}+\frac{k+1}{k+2}\sin^2\!\left(\frac{t}{\sqrt{k+2}}\right).
\]
The complete set of nonnegative perfect times is
\[
t_j=\left(j+\frac12\right)\pi\sqrt{k+2},\qquad j=0,1,2,\ldots.
\]
In particular, among connected regular graphs, exact perfect search is possible precisely for complete graphs.

## Assumptions and scope
Let \(G=(V,E)\) be a finite connected simple undirected unweighted loopless graph, with \(N=|V|\ge2\), \(m=|E|\), vertex degrees \(d_v\ge1\), adjacency matrix \(A\), degree matrix \(D\), and transition matrix \(P=D^{-1}A\). Equip functions on \(V\) with \(\langle f,g\rangle_d=\sum_{v\in V}d_v\overline{f(v)}g(v)\), in which \(\Delta=I-P\) is self-adjoint. Fix a marked vertex \(w\) and define unit vectors
\[
e_w=\frac{\delta_w}{\sqrt{d_w}},\quad s=\frac{1}{\sqrt{2m}}\sum_{v\in V}\delta_v,\quad H_\gamma=\gamma\Delta-|e_w\rangle\langle e_w|,\quad \gamma>0.
\]
The success probability is \(p_\gamma(t)=|\langle e_w,e^{-itH_\gamma}s\rangle_d|^2\) for real \(t\). The statement concerns exact equality \(p_\gamma(t)=1\) at some finite positive time, not near-perfect success, time-dependent controls, edge weights, loops, multiple marked vertices or other Laplacian normalizations.

## Proof
**1. First two energy moments give a necessary local equality.** Put \(\pi=d_w/(2m)\), so \(0<\pi<1\) and \(\langle e_w,s\rangle_d=\sqrt\pi\). Since \(\Delta s=0\) and there are no self-loops, \(\langle e_w,P e_w\rangle_d=0\). For \(H=H_\gamma\),
\[
\langle s,Hs\rangle_d=-\pi,\qquad \langle e_w,H e_w\rangle_d=\gamma-1.
\]
If \(p_\gamma(t)=1\), equality in Cauchy–Schwarz for two unit vectors forces \(e^{-itH}s=e^{i\phi}e_w\). Unitarity and commutation of \(e^{-itH}\) with \(H\) force equality of the first and second energy moments of the two vectors. The first moment fixes
\[
\gamma=1-\pi.
\]
Next \(Hs=-\sqrt\pi\,e_w\) and \(H e_w=(\gamma-1)e_w-\gamma P e_w\). Directly from the transition matrix,
\[
\|P e_w\|_d^2=\langle e_w,P^2 e_w\rangle_d=R_w,
\qquad R_w:=\frac{1}{d_w}\sum_{v\sim w}\frac1{d_v}.
\]
The two second moments are
\[
\langle s,H^2s\rangle_d=\pi,\qquad
\langle e_w,H^2 e_w\rangle_d=(\gamma-1)^2+\gamma^2R_w.
\]
Substitution of \(\gamma=1-\pi\) therefore yields the **necessary** identity
\[
R_w=\frac{\pi}{1-\pi}=\frac{d_w}{2m-d_w}.
\]

**2. Equality in a degree inequality characterizes the graph.** Every neighbor has positive degree. Applying Cauchy–Schwarz to the \(d_w\) neighbors and then enlarging the degree sum gives
\[
R_w=\frac1{d_w}\sum_{v\sim w}\frac1{d_v}
\ \ge\ \frac{d_w}{\sum_{v\sim w}d_v}
\ \ge\ \frac{d_w}{\sum_{v\ne w}d_v}
=\frac{d_w}{2m-d_w}.
\]
Equality in the first inequality means all neighbors of \(w\) have the same degree. Equality in the second means there is **no nonneighbor**, since connectedness gives every vertex positive degree. Hence equality forces \(w\) to be universal, and every vertex of \(G-w\) has degree \(k=d_v-1\) in the induced graph, independent of \(v\). Thus \(G-w\) is \(k\)-regular. The finite graph has \(0\le k\le N-2\). This proves necessity for every graph, without a nondegeneracy assumption on any eigenvalue.

**3. Sufficiency and every successful tuning and time.** Conversely suppose \(w\) is universal and \(G-w\) is \(k\)-regular. There are \(N-1\) base vertices of degree \(k+1\) and \(w\) has degree \(N-1\), giving \(2m=(N-1)(k+2)\) and \(\pi=1/(k+2)\). Let
\[
r=\frac1{\sqrt{(N-1)(k+1)}}\sum_{v\ne w}\delta_v.
\]
The orthonormal span of \(e_w,r\) is invariant under \(\Delta\) and the oracle, and its operators are
\[
\Delta_{\rm red}=\begin{pmatrix}
1&-1/\sqrt{k+1}\\
-1/\sqrt{k+1}&1/(k+1)
\end{pmatrix},\quad
(H_{\gamma_*})_{\rm red}=\frac1{k+2}\begin{pmatrix}
-1&-\sqrt{k+1}\\
-\sqrt{k+1}&1
\end{pmatrix},
\qquad \gamma_*:=\frac{k+1}{k+2}.
\]
The reduced search Hamiltonian squares to \(I/(k+2)\). In this ordered basis the initial state is \(s=(1,\sqrt{k+1})/\sqrt{k+2}\), while \(H_{\gamma_*}s=-e_w/\sqrt{k+2}\). Exponentiating the squared-identity matrix gives
\[
\langle e_w,e^{-itH_{\gamma_*}}s\rangle_d
=\frac{\cos(t/\sqrt{k+2})}{\sqrt{k+2}}+i\sin(t/\sqrt{k+2}).
\]
The displayed probability law follows; it equals one exactly when the cosine vanishes, giving precisely the stated times. Any alternative successful \(\gamma\) must equal \(1-\pi=\gamma_*\) by Step 1. The complete-time description follows. If \(G\) is regular and has a universal vertex, its common degree is \(N-1\), so it is complete.

## Verification
The proof is analytic for all finite connected simple graphs. The standalone `verify.py` reproduces the exact rational first/second-moment identities, the degree-defect equality criterion on every connected labeled graph with \(2\le N\le6\), and the two-dimensional block-square identity for \(0\le k\le12\). Run `python3 verify.py` with the standard library; expected output is `VERIFY_OK connected_labeled_graphs=27475 orders=2..6 cone_blocks=13 exact_fractions=true`. These finite checks independently exercise boundary examples but are not used in place of the unrestricted proof.

## Relationship to prior work
Mograby, Balu, Okoudjou and Teplyaev (arXiv:2207.01686, subsequently *Quantum Information Processing* 23, article 27 (2024)) introduce the probabilistic-Laplacian oracle Hamiltonian and give an exact complete-graph probability law and approximate/numerical studies on weighted hypercubes. Their Theorem 2.3 concerns approximate spectral/overlap conditions; it does not assert the all-graph necessary-and-sufficient condition here.

Razzoli, Bordone and Paris (arXiv:2202.13824, *Journal of Physics A* 55, 265303 (2022)) show perfect search at any universal marked vertex for the **combinatorial** Laplacian \(D-A\) and an ordinary uniform initial state. This does not imply the random-walk-normalized result: for the cone over a three-vertex path, the marked apex is universal but the base is not regular, so that normalized search is not exact-perfect although combinatorial-Laplacian search is. Coutinho and Baptista (arXiv:2209.04668) and Alvir et al. (arXiv:1409.5840) analyze unperturbed normalized-Laplacian perfect transfer between two vertex states, rather than stationary-to-oracle search.

## Limitations
The sharp classification assumes one marked vertex, simple connected loopless unweighted graphs, the specific random-walk normalization, the stationary initial state and a time-independent rank-one oracle of strength one. Failure of exact finite-time probability one does **not** imply a uniform gap below one, nor does it exclude approximate success, changing the initial state or Hamiltonian, or perfect search with the combinatorial Laplacian. No assertion about quantum search complexity for unknown target locations is made. Exact novelty cannot be inferred from unsuccessful literature searches alone; an equivalent result under different terminology remains possible. Independent validation has not been performed.

## References
1. G. Mograby, R. Balu, K. A. Okoudjou, A. Teplyaev, *Quantitative approach to Grover's quantum walk on graphs*, arXiv:2207.01686 (first public version 2022-07-04); *Quantum Information Processing* 23, 27 (2024), DOI:10.1007/s11128-023-04212-w.
2. L. Razzoli, P. Bordone, M. G. A. Paris, *Universality of the fully connected vertex in Laplacian continuous-time quantum walk problems*, arXiv:2202.13824 (2022), DOI:10.1088/1751-8121/ac72d5.
3. G. Coutinho, P. F. Baptista, *Quantum Walks in the Normalized Laplacian*, arXiv:2209.04668 (2022), DOI:10.1080/03081087.2023.2236282.
4. R. Alvir et al., *Perfect State Transfer in Laplacian Quantum Walk*, arXiv:1409.5840 (2014), *Journal of Algebraic Combinatorics* 43 (2016), 801–826.
