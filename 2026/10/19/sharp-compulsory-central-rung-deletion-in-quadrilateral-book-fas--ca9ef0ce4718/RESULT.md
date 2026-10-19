# Sharp compulsory central-rung deletion in quadrilateral-book fastest mixing

## Finding
Let \(B_m=K_{1,m}\square K_2\) for each integer \(m\ge2\), the graph of \(m\) quadrilaterals sharing one edge. For every symmetric, entrywise nonnegative, row-stochastic transition matrix \(P\) with nonzero off-diagonal entries allowed only along graph edges, define its second-largest eigenvalue modulus by
\[
\mu(P)=\left\|P-\frac{1}{2m+2}\mathbf 1\mathbf 1^{\mathsf T}\right\|_2.
\]
The exact optimum over all such matrices is
\[
\mu_m^*=\begin{cases}2-\sqrt2,&m=2,\\[2pt]1-1/m,&m\ge3.\end{cases}
\]
Write \(a\) for the central (hub-to-hub) matching-edge transition, \(b\) for each radial (hub-to-leaf) transition, and \(c\) for each peripheral (leaf-to-leaf) matching transition of an automorphism-invariant chain. The unique invariant optimum at \(m=2\) is
\[
(a,b,c)=\left(\frac{3-2\sqrt2}{2},\sqrt2-1,\frac{2-\sqrt2}{2}\right).
\]
For every \(m\ge3\), the **complete family** of invariant optima is
\[
a=0,\qquad b=\frac1m,\qquad
\frac{1}{2(m-1)}\le c\le\frac{m-1}{m}-\frac{1}{2(m-1)}.
\]
Moreover, **every global optimum**, invariant or not, has the same central-edge probability: positive and equal to \((3-2\sqrt2)/2\) at \(m=2\), and exactly zero for \(m\ge3\). In the latter regime both hub holding probabilities are also zero. Thus three pages (eight vertices) is the sharp onset of mandatory deletion of the common edge.

## Assumptions and scope
The graph has hubs \(u_0,u_1\), and paired leaves \(x_i,y_i\) for \(1\le i\le m\). Its edges are \(\{u_0,u_1\}\), \(\{u_0,x_i\}\), \(\{u_1,y_i\}\), and \(\{x_i,y_i\}\). A permissible matrix is real symmetric, nonnegative, row-stochastic, and zero at all nonedges away from the diagonal. Zero edge probabilities and nonnegative holding probabilities are permitted. The statement does not assume uniqueness among *all* nonsymmetric-under-automorphisms optimal transition matrices. It classifies all automorphism-invariant optima and the stated entries of every optimum.

## Proof
The automorphisms that permute the \(m\) pages and exchange the two star layers preserve the feasible matrices and the rank-one stationary projector. Spectral-norm convexity therefore shows that averaging any feasible \(P\) under this group cannot increase \(\mu(P)\). Hence the global minimum is attained within the invariant three-parameter family.

For such a matrix, nonnegativity and row sums are exactly
\[
a,b,c\ge0,\qquad a+mb\le1,\qquad b+c\le1.
\]
In particular, \(0\le b\le1/m\). Taking symmetric and antisymmetric combinations under layer reflection, then separating page averages from page differences, yields the full eigenvalue multiset
\[
1,\quad 1-(m+1)b,\quad
(1-b)^{[m-1]},\quad(1-b-2c)^{[m-1]},
\quad\operatorname{eig}\!\begin{pmatrix}
1-2a-mb&\sqrt m\,b\\
\sqrt m\,b&1-b-2c
\end{pmatrix}.
\]
Here an exponent in square brackets denotes multiplicity, not a numerical power. To verify the decomposition directly, use the normalized vectors \((e_{u_0}\pm e_{u_1})/\sqrt2\), the two page-average combinations \(\sum_i(e_{x_i}\pm e_{y_i})/\sqrt{2m}\), and page-difference subspaces orthogonal to these averages. The layer-symmetric average block has eigenvalues \(1\) and \(1-(m+1)b\); the layer-antisymmetric block is the displayed matrix \(H\).

For every \(m\ge2\), the page-symmetric difference eigenvalue gives
\[
\mu(P)\ge1-b.
\]
The off-diagonal entry of \(H\) independently yields \(\mu(P)\ge\sqrt m\,b\), because a matrix operator norm bounds every entry in an orthonormal basis.

At \(m=2\), minimizing the lower envelope \(\max\{1-b,\sqrt2\,b\}\) over \(0\le b\le1/2\) gives its unique minimizer \(b=\sqrt2-1\) and minimum \(2-\sqrt2\). Choosing \(a=(1-2b)/2\) and \(c=(1-b)/2\) makes both diagonal entries of \(H\) vanish, so its eigenvalues are \(\pm\sqrt2\,b\). The remaining eigenvalue \(1-3b=4-3\sqrt2\) has strictly smaller modulus. Equality in \(\|H\|_2\ge\sqrt2\,b\) forces both diagonal entries of \(H\) to vanish, since for a symmetric \(2\times2\) matrix with diagonal entries \(s,t\) and off-diagonal \(k\), its norm is \(|s+t|/2+\sqrt{k^2+(s-t)^2/4}\). Thus the invariant optimizer at \(m=2\) is unique.

For \(m\ge3\), the constraint \(b\le1/m\) gives \(\mu(P)\ge1-1/m=:T\). Choose \(a=0\), \(b=1/m\), and \(c=(m-1)/(2m)\). Then the nontrivial eigenvalues are \(-1/m\), \(T\) (with multiplicity \(m-1\)), zero (with multiplicity \(m-1\)), and \(\pm1/\sqrt m\). The inequality \(1/\sqrt m\le T\) is equivalent to \((m-1)^2\ge m\), valid for all integers \(m\ge3\). Hence the lower bound is sharp.

Equality in \(1-b\ge T\) forces \(b=1/m\) for every invariant minimizer. The hub constraint then forces \(a=0\). Set \(h=T-2c\). The remaining antisymmetric block is \(H=\begin{pmatrix}0&1/\sqrt m\\1/\sqrt m&h\end{pmatrix}\). Its norm is \(\sqrt{1/m+h^2/4}+|h|/2\), which does not exceed \(T\) exactly when \(|h|\le T-1/(mT)\). Solving for \(c\) gives precisely the closed interval in the finding; the other eigenvalues already have modulus at most \(T\). This exhausts all invariant optimizers.

Finally, the central edge \(\{u_0,u_1\}\) is preserved as a set by every page-permutation or layer-exchange automorphism, so its probability is unchanged by averaging. Thus every global optimizer has the central-edge probability found in the invariant classification. For \(m\ge3\), the average of its two nonnegative hub diagonal entries is zero at the invariant optimum, so both entries themselves vanish. A product-homogeneous transition matrix would assign the same interlayer weight to the central rung and all leaf rungs. Such a matrix is impossible at optimum for \(m\ge3\), because setting every interlayer weight to zero disconnects the two stars and forces \(\mu=1>T\). At \(m=2\), product homogeneity contradicts the unique invariant optimal probabilities \(a\ne c\). This proves all assertions.

## Verification
The accompanying `verify.py` constructs the full \((2m+2)\)-vertex matrix independently of the block decomposition, checks exact symbolic characteristic polynomials against the stated full eigenvalue multiset for \(2\le m\le9\) and several feasible parameter choices, and tests the exact two-page optimizer. It also checks endpoint and exterior cases of the invariant optimizer interval and evaluates a finite rational-grid search by full symmetric-matrix eigensolvers. Its printed run result is `PASS 3849 exact and numerical checks`. The infinite-size classification and all-optimal conclusions follow from the proof, not from numerical sampling.

## Relationship to prior work
The foundational fastest-mixing optimization and its spectral-norm formulation were established by Boyd, Diaconis, and Xiao (2004). Boyd, Diaconis, Parrilo, and Xiao (arXiv version dated 2007-09-06; published 2009) introduced automorphism reductions and graph-product spectral methods, including complete-bipartite and wheel examples. Their Cartesian-product discussion gives Laplacian spectra for product graphs, but does not give this three-edge-orbit optimization or compulsory deletion of only the central matching edge. A product-homogeneous transition would impose \(a=c\), whereas every optimizer here violates it. Jafarizadeh (2010) solved certain complete-layered multipartite FMMC topologies; those have different interlayer adjacency patterns. Later work on friendship graphs treats triangles sharing one vertex, not quadrilaterals sharing an edge. Public results concerning quadrilateral-book matching complexes or book-graph edge polytopes concern different mathematical invariants and do not entail the SLEM optimum.

## Limitations
The result is about uniform-stationary, **symmetric stochastic** discrete-time chains with permitted self-loops. It does not optimize arbitrary nonreversible chains or chains with nonuniform stationary measures. All invariant optimizers are explicit, but full classification of non-invariant optimizers is not claimed. The finite verification is supplemental, not a proof in unbounded \(m\). As with any targeted literature comparison, equivalent results outside the checked corpus could exist; no independent audit has occurred.

## References
1. S. Boyd, P. Diaconis and L. Xiao, *Fastest Mixing Markov Chain on a Graph*, SIAM Review 46 (2004), 667–689. DOI: 10.1137/S0036144503423264; authors' full text: https://web.stanford.edu/~boyd/papers/pdf/fmmc.pdf.
2. S. Boyd, P. Diaconis, P. A. Parrilo and L. Xiao, *Fastest Mixing Markov Chain on Graphs with Symmetries*, arXiv:0709.0955, first version 2007-09-06; SIAM Journal on Optimization 20 (2009), 792–819. https://arxiv.org/abs/0709.0955.
3. S. Jafarizadeh, *Fastest Mixing Markov Chain on Symmetric K-Partite Network*, arXiv:1008.2588, first version 2010-08-16. https://arxiv.org/abs/1008.2588.
4. S. Jafarizadeh, *Fastest mixing reversible Markov chain on friendship graph*, arXiv:2501.02117 (2025). https://arxiv.org/abs/2501.02117.
