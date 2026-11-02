# Quantum return halving and a localization reversal on subdivided cliques

## Finding

Let \(G\) be a finite connected simple graph on \(n\geq 2\) vertices, and let \(S(G)\) be the graph obtained by inserting exactly one new degree-two vertex into each edge. The Hamiltonians below are **ordinary adjacency matrices**. At any vertex \(x\) of a graph with real symmetric Hamiltonian \(M\), define the infinite-time average return probability
\[
\mathcal R_M(x)=\lim_{T\to\infty}\frac1T\int_0^T |\langle e_x,e^{-itM}e_x\rangle|^2\,dt.
\]
Let \(Q_G=D_G+A_G\) be the signless Laplacian of the original graph. For every original vertex \(u\), the exact identity is
\[
\boxed{\mathcal R_{A_{S(G)}}(u)=\tfrac12\mathcal R_{Q_G}(u)+\tfrac{1}{2n^2}\mathbf1_{\{G\text{ bipartite}\}}.}
\]
In particular, for a connected \(d\)-regular graph, \(Q_G=dI+A_G\), so replacing each edge by two edges exactly halves the original-vertex average return on nonbipartite regular graphs, and adds only \(1/(2n^2)\) beyond the half on bipartite regular graphs.

For the complete graph \(G=K_n\), \(n\ge3\), the subdivided graph has two vertex orbits: \(n\) original vertices and \(\binom n2\) inserted edge vertices. Their exact return probabilities are
\[
\boxed{\mathcal R_{\mathrm{original}}(n)=\frac{n^2-2n+2}{2n^2}},\qquad
\boxed{\mathcal R_{\mathrm{edge}}(n)=\frac{n^4-6n^3+11n^2-4n+4}{n^2(n-1)^2}}.
\]
Consequently,
\[
\mathcal R_{\mathrm{edge}}(n)-\mathcal R_{\mathrm{original}}(n)
=\frac{(n-3)(n^3-5n^2-2)}{2n^2(n-1)^2}.
\]
The orbits tie exactly at \(n=3\); the original vertices have larger return for \(n=4,5\); and the degree-two inserted vertices have strictly larger return for **every** \(n\ge6\). As \(n\to\infty\), original-vertex return tends to \(1/2\), whereas the inserted-vertex return tends to \(1\). This is a complete all-order localization reversal, despite the much smaller inserted-vertex degrees.

## Assumptions and scope

Graphs are finite, connected, loopless, undirected and simple, with unit adjacency hopping and no potential or disorder. Each edge is subdivided once. All time averages concern unitary continuous-time evolution and probabilities measured from a single localized vertex at time zero. No claim of pointwise long-time convergence is made. The general identity applies to all such \(G\), including bipartite and nonregular cases; the sharp ordering is proved only for the clique family \(K_n\).

## Proof

**1. Spectral return formula.** Let \(M=\sum_\theta\theta E_\theta\) denote its spectral decomposition, with each distinct eigenvalue appearing once. The return amplitude is \(\sum_\theta e^{-it\theta}(E_\theta)_{xx}\). Integrating the square in time and letting \(T\to\infty\), all unequal-frequency terms vanish, giving
\[
\mathcal R_M(x)=\sum_\theta (E_\theta)_{xx}^2.
\]
This is the standard average-mixing projector formula [1], used here with all degeneracies retained.

**2. The full subdivision via the signless Laplacian.** Index the new vertices by \(E(G)\), and form the unsigned incidence matrix \(B\in\mathbb R^{n\times |E(G)|}\), whose column for \(\{v,w\}\) has entries one at \(v,w\) and zeros elsewhere. The adjacency Hamiltonian of the subdivision and its square are
\[
H=\begin{pmatrix}0&B\\B^\top&0\end{pmatrix},\quad
H^2=\begin{pmatrix}Q_G&0\\0&B^\top B\end{pmatrix},\quad Q_G=BB^\top=D_G+A_G.
\]
Let \(F_\lambda\) be the spectral projector of \(Q_G\) for a positive eigenvalue \(\lambda\). Direct multiplication shows that the \(H\)-projectors at \(\pm\sqrt\lambda\) are
\[
P_{\pm,\lambda}=\frac12\begin{pmatrix}
F_\lambda&\pm\lambda^{-1/2}F_\lambda B\\
\pm\lambda^{-1/2}B^\top F_\lambda&\lambda^{-1}B^\top F_\lambda B
\end{pmatrix}.
\]
These are orthogonal idempotents; they are pairwise orthogonal across distinct signed square roots. The zero eigenspace of \(H\) is \(\ker B^\top\oplus\ker B\) and its projector, with \(Q_G^+\) the Moore--Penrose inverse, is
\[
P_0=\operatorname{diag}\big(F_0, I-B^\top Q_G^+B\big).
\]
On an original vertex, each \(P_{\pm,\lambda}\) has diagonal \((F_\lambda)_{uu}/2\), while \(P_0\) has diagonal \((F_0)_{uu}\). The projector return formula therefore yields
\[
\mathcal R_H(u)=\frac12\sum_{\lambda>0}(F_\lambda)_{uu}^2+(F_0)_{uu}^2
=\frac12\mathcal R_{Q_G}(u)+\frac12(F_0)_{uu}^2.
\]
For connected \(G\), the kernel of its signless Laplacian is zero unless \(G\) is bipartite. For a connected bipartite graph, its kernel is one-dimensional, spanned by the sign vector that equals \(+1\) and \(-1\) on the two sides, respectively; this vector has squared norm \(n\). Thus \((F_0)_{uu}=1/n\) for every vertex and the claimed identity follows. For a regular graph, shifting \(A_G\) by \(dI\) changes only eigenvalues, not projectors, giving the stated halving law.

**3. Both orbits of the subdivided clique.** For \(n\ge3\), \(Q_{K_n}=(n-2)I+J\), with two eigenvalues \(2(n-1)\) and \(n-2\) and respective projectors \(F_+=(1/n)J\) and \(F_-=I-(1/n)J\). Both are positive. At an original vertex, their diagonal values are \(1/n\) and \((n-1)/n\), and step 2 gives
\[
\mathcal R_{\mathrm{original}}(n)=\frac12\left[\frac{1}{n^2}+\frac{(n-1)^2}{n^2}\right]
=\frac{n^2-2n+2}{2n^2}.
\]
For an inserted edge vertex corresponding to a clique edge \(\{i,j\}\), its incidence column is \(b=e_i+e_j\). Hence
\[
b^\top F_+b=4/n,\qquad b^\top F_-b=2(n-2)/n.
\]
In the \(H\)-projectors for the two signed eigenvalue pairs, the edge diagonal is therefore, respectively, \(1/[n(n-1)]\) and \(1/n\) for *each sign*. By the zero-projector formula, its zero eigenspace diagonal is
\[
1-b^\top Q_{K_n}^{-1}b
=1-\left(\frac{2}{n(n-1)}+\frac2n\right)
=\frac{n-3}{n-1}.
\]
Squaring the five diagonal projector contributions, with zero counted only once, gives
\[
\mathcal R_{\mathrm{edge}}(n)=2\left(\frac1{n(n-1)}\right)^2
+2\left(\frac1n\right)^2
+\left(\frac{n-3}{n-1}\right)^2
=\frac{n^4-6n^3+11n^2-4n+4}{n^2(n-1)^2}.
\]
The displayed difference factorization follows by clearing positive denominators. The cubic \(f(n)=n^3-5n^2-2\) is negative at \(n=4,5\), positive at \(n=6\), and strictly increasing for all real \(n\ge4\), because \(f'(n)=n(3n-10)>0\). The factor \(n-3\) makes the difference zero at \(n=3\). This proves all signs and the limiting values. The edge-space zero-mode contribution is responsible for the limiting return of one: its rank is \(\binom n2-n\) and its diagonal tends to one at every inserted vertex.

## Verification

The provided self-contained numerical script `verify_subdivision_clique.py` (requires Python 3 and NumPy) independently diagonalizes the actual adjacency Hamiltonian of \(S(K_n)\) for each integer \(3\le n\le16\), regroups repeated eigenvalues into their *full spectral projectors*, and checks the two return expressions on every vertex. It also enumerates all 771 labeled connected simple graphs of order \(2\) through \(5\), and tests the general signless-Laplacian return identity using independent matrix diagonalization. Observed outputs: `PASS: 14 independent adjacency-matrix diagonalizations; exact spectra and all vertex return values match.` and `PASS: general subdivision identity for all 771 connected simple graphs on 2–5 vertices.` Numerical tests support the algebra but are not a proof for infinitely many graphs or clique sizes; the proof above supplies that.

## Relationship to prior work

Godsil [1] establishes the spectral-projector formula for continuous-time average mixing; it does not, in the examined spectral and examples material, evaluate it for all edge subdivisions. Godsil, Guo and Sobchuk [2] study diagonal average-mixing entries and rooted graph constructions. Their comparison and exact results are related, but the examined sections do not state a signless-Laplacian subdivision return identity or the two-orbit clique threshold. Ide [3] studies localization caused by local subgraphs, using principally Laplacian walk models and a different large-graph localization notion; those results do not imply the adjacency-Hamiltonian formulas here. The present result uses the known projector principle, and claims no novelty for that principle itself. Targeted literature and mathematical-record searches found no dominating implication; coverage by an unexamined historical equivalent remains possible.

## Limitations

The term “localization” refers solely to the infinite-time average *return to a vertex*, not a pointwise limit or a universal guarantee for arbitrary initial states. The threshold is for unweighted full subdivisions of cliques under the adjacency Hamiltonian; adding disorder, edge weights, magnetic phases, absorbers, dephasing or a different generator can change the result. The related literature inspected does not establish historical priority exhaustively; independent verification or external audit is not claimed.

## References

[1] C. Godsil, *Average mixing of continuous quantum walks*, 2011, arXiv:1103.2578, https://arxiv.org/abs/1103.2578 (first public date 2011-03-14).

[2] C. Godsil, K. Guo and M. Sobchuk, *Diagonal entries of the average mixing matrix*, arXiv:1910.02039, https://arxiv.org/abs/1910.02039; open-access manuscript https://pure.uva.nl/ws/files/179898245/ajc_v86_p373.pdf.

[3] Y. Ide, *Local subgraph structure can cause localization in continuous-time quantum walk*, arXiv:1406.0347, https://arxiv.org/abs/1406.0347.
