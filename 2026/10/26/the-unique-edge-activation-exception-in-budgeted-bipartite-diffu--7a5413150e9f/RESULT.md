# The unique edge-activation exception in budgeted bipartite diffusion

## Finding
Let \(p,q\ge 2\) be integers. Form \(G_{p,q}^{+}\) by taking the complete bipartite graph \(K_{p,q}\) and adding exactly one edge between two specified vertices in its part of size \(p\). Assign independently chosen, nonnegative, undirected edge conductances with total \(B>0\). The largest attainable second eigenvalue of the combinatorial weighted Laplacian is
\[
\max_{w\ge0,\ \sum_e w_e=B}\lambda_2(L(w))=
\begin{cases}
\displaystyle\frac{5B}{11+2\sqrt 3},&(p,q)=(3,2),\\[5pt]
\displaystyle\frac{B}{\max\{p,q\}},&\text{otherwise}.
\end{cases}
\]
Moreover, **every** optimal allocation gives the added within-part edge zero weight unless \((p,q)=(3,2)\); in that exceptional graph, **every** optimal allocation assigns it positive weight. The placement of the added edge matters: the exceptional case attaches it to the part of size three, not the part of size two.

For the exceptional graph, label the three-vertex part \(u_1,u_2,u_3\), the two-vertex part \(v_1,v_2\), and add \(u_1u_2\). Put
\[
a=\frac{3+2/\sqrt3}{10},\quad b=\frac{4+\sqrt3}{10},\quad c=\frac{1-1/\sqrt3}{5},\quad V=\frac{11+2\sqrt3}{5}.
\]
An exact optimal allocation gives each \(u_1v_j,u_2v_j\) weight \(Ba/V\), each \(u_3v_j\) weight \(Bb/V\), and \(u_1u_2\) weight \(Bc/V\). The new-edge gain relative to allocating all budget to the bipartite edges is the factor \(3/V=15/(11+2\sqrt3)>1\).

## Assumptions and scope
The graph is finite, simple and undirected; \(p,q\) are arbitrary integers at least two. The conductance budget counts each undirected edge exactly once, and zero conductance is permitted. The Laplacian is \(L=\sum_{\{i,j\}\in E}w_{ij}(e_i-e_j)(e_i-e_j)^{\mathsf T}\). The objective is the **continuous-time** spectral mixing rate \(\lambda_2\), not the second-largest *absolute* eigenvalue of a discrete-time transition matrix. No symmetry is assumed for competitors. Equal edge conductances are used only to construct a candidate attaining the unrestricted optimum in the nonexceptional cases.

## Proof
**A universal embedding bound.** Assign vectors \(z_i\in\mathbb R^d\) to the vertices, subtract their common centroid and suppose \(\|z_i-z_j\|\le1\) on every allowed edge. Set \(S=\sum_i\|z_i-\bar z\|^2\). Applying the Rayleigh inequality to each coordinate of the centered configuration gives
\[
\lambda_2(L(w))S\le\sum_{\{i,j\}\in E}w_{ij}\|z_i-z_j\|^2\le B.
\]
If an allowed edge has **strictly** shorter embedded length than one, equality with \(B/S\) is impossible whenever that edge has positive weight. This is an elementary, graph-specific upper-bound certificate; it does not rely on taking a symmetric optimizer.

**All nonexceptional sizes.** If \(q\ge p\), put all \(p\) vertices of the first part at the origin, and put the \(q\) vertices of the other part at unit vectors summing to zero (e.g., the regular \(q\)-gon). Every bipartite edge has length one; the new edge has length zero; and \(S=q\). If \(p\ge4\) and \(p>q\), put the \(q\) vertices of the second part at zero, put the first two vertices of the first part both at \(e_1\), and let \(k=p-2\). Place the other \(k\) vertices at
\[
-\frac2k e_1+\sqrt{1-\frac4{k^2}}\left(\cos\frac{2\pi j}{k}\,e_2+\sin\frac{2\pi j}{k}\,e_3\right),\qquad j=0,\ldots,k-1.
\]
Their sum is \(-2e_1\), so all points have centroid zero. Every bipartite edge has length one, the added edge has length zero, and \(S=p\). The construction also holds for \(k=2\) because the square-root term then vanishes. The only ordered pair with \(p>q\ge2\) not included in these constructions is \((p,q)=(3,2)\).

In every nonexceptional case the bound therefore gives \(\lambda_2\le B/\max\{p,q\}\). Assigning weight \(B/(pq)\) to each bipartite edge and zero to the added edge attains this: the positive eigenvalues of the weighted \(K_{p,q}\) are \(qB/(pq)\) with multiplicity \(p-1\), \(pB/(pq)\) with multiplicity \(q-1\), and \((p+q)B/(pq)\) once. As the embedding has zero length across the added edge, equality forces its weight to be zero for **every** optimizer.

**The exceptional five-vertex graph.** Use two-dimensional embedded points
\[
z_{u_1}=(\sqrt3/2,1/2),\quad z_{u_2}=(\sqrt3/2,-1/2),\quad z_{u_3}=(-1,0),\quad z_{v_1}=z_{v_2}=(0,0).
\]
All seven allowed edges have length one. Their centered variance is
\[
S=3-\frac{(\sqrt3-1)^2}{5}=\frac{11+2\sqrt3}{5}=V.
\]
Thus \(\lambda_2\le B/V\) for every allocation.

To attain this bound, first use the unscaled weights \(a,b,c\) given above, whose total is \(4a+2b+c=V\). The exchange-antisymmetric vector on \(u_1,u_2\) has eigenvalue \(2a+2c=1\). The exchange-antisymmetric vector on \(v_1,v_2\) has eigenvalue \(2a+b=1+7\sqrt3/30>1\). On the three-dimensional subspace constant on each of these exchange orbits, the Laplacian acts on the three group values through
\[
Q=\begin{pmatrix}2a&0&-2a\\0&2b&-2b\\-2a&-b&2a+b\end{pmatrix}.
\]
Its characteristic polynomial is \(t\bigl(t^2-(4a+3b)t+10ab\bigr)\). Direct substitution gives \(10ab-(4a+3b)+1=0\), so its positive eigenvalues are \(1\) and \(4a+3b-1=7/5+17\sqrt3/30>1\). Consequently the complete five-vertex Laplacian has second eigenvalue exactly one. Scaling all weights by \(B/V\) attains the bound \(B/V\). Finally \(V<3\), whereas assigning zero conductance to the added edge leaves only \(K_{3,2}\), whose best possible rate is \(B/3\) by the earlier construction. Every exceptional optimal allocation therefore has \(w(u_1,u_2)>0\).

## Verification
The accompanying `verify.py` uses only the Python standard library. It checks exact identities over \(\mathbb Q(\sqrt3)\) for the special conductances, the exceptional embedding distances and variance, and complete Laplacian spectra for 224 nonexceptional parameter pairs with \(2\le p,q\le16\), plus the exceptional complete spectrum. Execute `python3 verify.py` in the directory containing that file. These numerical finite-size checks are supplementary: all-parameter assertions follow from the embedding constructions and the displayed exact spectrum.

## Relationship to prior work
Göring, Helmberg and Wappler (public preprint September 2, 2005) establish the maximum-variance embedding formulation of absolute algebraic connectivity, while Sun, Boyd, Xiao and Diaconis (2006) explain the same duality for continuously mixing Markov processes. The present classification uses that established method but solves an **augmented biclique family** not classified in those inspected papers. In particular, the earlier example of a clique attached to three independent vertices includes a differently oriented \(K_{2,3}\) augmentation; it does not imply that the single-edge gain is positive **only** when the edge joins two vertices of the three-element part of \(K_{3,2}\). The known explicit classifications of double-broom *trees* do not apply to these graphs, which contain triangles.

## Limitations
The theorem assumes a single extra edge within one part, uniform per-edge budget cost, unrestricted nonnegative weights and the continuous-time Laplacian spectral gap. It does not classify the possibly nonunique edge allocations beyond their added-edge sign or address two or more extra edges, constrained lower weight bounds, heterogeneous edge costs, or discrete-time fastest mixing. A specialized earlier classification of this exact one-edge augmentation may exist outside the inspected literature.

## References
1. F. Göring, C. Helmberg, and M. Wappler, *Embedded in the Shadow of the Separator*, preprint dated 2005-09-02, https://optimization-online.org/2005/09/1202/ (full PDF https://optimization-online.org/wp-content/uploads/2005/09/1202.pdf).
2. J. Sun, S. Boyd, L. Xiao, and P. Diaconis, *The Fastest Mixing Markov Process on a Graph and a Connection to a Maximum Variance Unfolding Problem*, SIAM Review 48 (2006), 681–699, https://stanford.edu/~boyd/papers/pdf/fmmp.pdf, DOI 10.1137/S0036144504443821.
3. M. Fiedler, *Absolute algebraic connectivity of trees*, Linear and Multilinear Algebra 26 (1990), 85–106, DOI 10.1080/03081089008817967 (abstract and publication data inspected; complete text not obtained).
4. S. Richter and I. Rocha, *Absolute algebraic connectivity of double brooms and trees*, Discrete Applied Mathematics 201 (2016), 213–221, preprint https://www.tu-chemnitz.de/mathematik/preprint/2014/PREPRINT_10.pdf (tree-only comparison).
