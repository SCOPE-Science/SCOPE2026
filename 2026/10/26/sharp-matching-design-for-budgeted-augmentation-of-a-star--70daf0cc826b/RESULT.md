# Sharp matching design for budgeted augmentation of a star

## Finding

**Theorem (sharp budgeted star augmentation and stability).** Fix integers \(n\ge2\) and \(1\le k\le\lfloor n/2\rfloor\), and a real budget \(W>0\). Begin with the star having hub \(0\), leaves \(1,\dots,n\), and unit conductance on each spoke. Add at most \(k\) distinct undirected edges between leaves, with nonnegative conductances whose sum does not exceed \(W\). Existing spoke weights are fixed. For the weighted graph \(G\), let \(L_G\) denote its combinatorial Laplacian and set
\[
\mathcal C(G)=\operatorname{tr}(L_G^\dagger),\qquad Kf(G)=(n+1)\mathcal C(G),
\]
where \(L_G^\dagger\) is the Moore–Penrose pseudoinverse and \(Kf\) is the Kirchhoff index (sum of all unordered-pair effective resistances). Then
\[
\min_G\mathcal C(G)=n-1+\frac{1}{n+1}-\frac{2Wk}{k+2W},
\qquad
\min_G Kf(G)=n^2-\frac{2(n+1)Wk}{k+2W}.
\]
Every minimizer uses the full budget on exactly \(k\) edges that form a matching on the leaves, each of conductance \(W/k\). Conversely, all these designs attain the minimum.

More quantitatively, if exactly \(k\) distinct leaf edges \(e_1,\dots,e_k\) have positive weights \(w_1,\dots,w_k\) summing to \(W\), then
\[
\boxed{\mathcal C(G)-\mathcal C_{\min}\ge
\frac{4\sum_{i=1}^k(w_i-W/k)^2+2\sum_{1\le i<j\le k:\,e_i\cap e_j\ne\varnothing}w_iw_j}{(1+2W)^3}.}
\]
Thus both weight imbalance and overlap of newly installed links incur a strict, explicit loss.

## Assumptions and scope

The graph has \(n+1\) labeled vertices. All base spokes have conductance exactly \(1\), and only missing **leaf-to-leaf** edges are candidates for installation. Installed conductances are real and positive; allowing zero weights merely permits the same design to be described with unused candidates. Added links are simple, distinct, and undirected. The count bound \(2k\le n\) is essential to the availability of a matching of size \(k\); no claim is made when \(k>\lfloor n/2\rfloor\), for modified spoke weights, or for directed networks. The normalization \(\mathcal C=\operatorname{tr}L^\dagger\) has no extra factor of \(1/2\); noise-driven consensus coherence under other normalizations is obtained by multiplying this value by the chosen noise factor.

## Proof

**1. An invariant spectral splitting.** Write the Laplacian as \(L_G=L_*+H\), where \(L_*\) is the unit-star Laplacian and
\[
H=\sum_{e=\{u,v\}}w_e b_eb_e^{\mathsf T},\qquad b_e=\mathbf e_u-\mathbf e_v.
\]
The three mutually orthogonal invariant subspaces are the one-dimensional constants, the one-dimensional span of \((-n,1,\ldots,1)\), and the \((n-1)\)-dimensional space \(U=\{x:x_0=0,\ \sum_{j=1}^n x_j=0\}\). On these subspaces, \(L_*\) has eigenvalues \(0\), \(n+1\), and \(1\), respectively. Every \(b_e\) lies in \(U\), so \(H\) vanishes on the first two subspaces and is positive semidefinite on \(U\).

Suppose \(s\le k\) edges carry positive weights with total \(T\le W\). Let \(\mu_1,\dots,\mu_k\) be the eigenvalues of \(H|_U\), padded by zero as necessary (rank at most \(s\)); this is possible because \(k\le n-1\). They are nonnegative and
\[
\sum_{i=1}^k\mu_i=\operatorname{tr}H=2T.
\]
All the remaining \(n-1-k\) eigenvalues of \(H|_U\) vanish. Therefore, with \(f(t)=t/(1+t)\) for \(t\ge0\),
\[
\mathcal C(G)=\frac{1}{n+1}+(n-1-k)+\sum_{i=1}^k\frac{1}{1+\mu_i}
=n-1+\frac{1}{n+1}-\sum_{i=1}^k f(\mu_i).
\]

**2. Sharp global bound, including the discrete support choice.** Since \(f'(t)=(1+t)^{-2}>0\) and \(f''(t)=-2(1+t)^{-3}<0\), strict Jensen concavity and monotonicity give
\[
\sum_{i=1}^k f(\mu_i)\le kf(2T/k)\le kf(2W/k)=\frac{2Wk}{k+2W}.
\]
Equality requires \(T=W\) and all \(k\) padded eigenvalues to equal \(2W/k>0\). Thus the rank must equal \(k\) and there must be exactly \(k\) positive-weight added edges.

**3. The equality case forces a matching.** Orient the selected edges arbitrarily and form the \((n+1)\)-by-\(k\) matrix
\[
C=[\sqrt{w_1}b_{e_1}\ \cdots\ \sqrt{w_k}b_{e_k}].
\]
The nonzero eigenvalues of \(H=CC^{\mathsf T}\) are the eigenvalues of \(B=C^{\mathsf T}C\). Since all its \(k\) eigenvalues must equal \(2W/k\), symmetry gives \(B=(2W/k)I_k\). Its diagonal entries are \(B_{ii}=2w_i\), hence \(w_i=W/k\). For distinct simple leaf edges, \(b_{e_i}^{\mathsf T}b_{e_j}\) is zero exactly when the edges share no endpoint, and equals \(1\) or \(-1\) otherwise. Its off-diagonal entries \(B_{ij}=\sqrt{w_iw_j}\,b_{e_i}^{\mathsf T}b_{e_j}\) thus vanish precisely when the selected edges form a matching. Such a matching exists because \(2k\le n\), and it achieves equality, proving both optimal formulas and the classification of all minimizers.

**4. Quantitative rigidity.** Now assume \(s=k\) and \(T=W\), and write \(\bar\mu=2W/k\). All eigenvalues lie in \([0,2W]\), on which
\[
f''(t)\le-\frac{2}{(1+2W)^3}.
\]
Taylor's theorem with the global curvature bound yields
\[
kf(\bar\mu)-\sum_i f(\mu_i)\ge\frac{\sum_i(\mu_i-\bar\mu)^2}{(1+2W)^3}.
\]
The matrices \(H\) and \(B\) have the same \(k\) nonzero-or-padded spectral values, giving
\[
\sum_i(\mu_i-\bar\mu)^2=\operatorname{tr}(B^2)-\frac{4W^2}{k}.
\]
Expanding the squared Gram entries, \(B_{ii}=2w_i\) and \(B_{ij}^2=w_iw_j\) for edges sharing one endpoint and zero otherwise, gives the exact identity
\[
\operatorname{tr}(B^2)-\frac{4W^2}{k}
=4\sum_i(w_i-W/k)^2+2\sum_{i<j:\,e_i\cap e_j\ne\varnothing}w_iw_j.
\]
This proves the claimed quantitative stability bound.

## Verification

The proof applies for **all** admissible integers and positive real budgets; finite checks are supporting examples, not an exhaustive certificate. Run `python verify_star_aug.py` with Python 3 and NumPy. It computes the full weighted Laplacian eigenvalues, checks the optimum and its equality characterization, and checks the quantitative gap bound across 14,107 candidate support-and-weight allocations with \(2\le n\le7\), \(1\le k\le\min(3,\lfloor n/2\rfloor)\), and two half-integer budgets. All 13,539 tested nonoptimal allocations exhibit strict loss. For example, a six-leaf star with three additional pairwise disjoint unit-weight links has \(\mathcal C=22/7\), agreeing with the formula at \(W=3\), \(k=3\).

## Relationship to prior work

Summers, Shames, Lygeros and Dörfler (2014) study selecting edges for network coherence and formulate a general greedy edge-selection approach with fixed added weights. Ghosh, Boyd and Saberi (2008) establish a convex continuous conductance-allocation problem on fixed graph topologies and discuss the original star. Neither inspected result gives the exact global **joint discrete-support and continuous-weight** optimum above, its all-minimizer matching characterization, or the quantitative overlap penalty. Kooij and Achterberg (2023) establish NP-hardness for general unweighted-link Kirchhoff-index augmentation but do not treat this weighted star theorem. Bhoite and coauthors (2026) study the general joint-cardinality-and-budget framework using numerical relaxations and heuristics; their inspected claims likewise do not state the sharp analytic star classification. These comparisons support a specific distinction but do not prove uniqueness against every item of specialized literature.

## Limitations

The result requires an unmodified unit-conductance star, leaf-only added edges, \(k\le\lfloor n/2\rfloor\), and a single global linear conductance budget with unit cost per installed conductance. The quantitative lower bound is not claimed to be optimal as a constant. It is an analytic classification, not a general polynomial-time method for arbitrary graph augmentation. Novelty remains subject to undiscovered specialized prior treatments of the same spectral reduction.

## References

1. T. H. Summers, I. Shames, J. Lygeros and F. Dörfler, *Topology Design for Optimal Network Coherence*, preprint first posted 18 November 2014, arXiv:1411.4884. https://arxiv.org/abs/1411.4884
2. A. Ghosh, S. Boyd and A. Saberi, *Minimizing Effective Resistance of a Graph*, SIAM Review 50 (2008), 37–66. https://doi.org/10.1137/050645452 ; author-hosted copy: https://web.stanford.edu/~boyd/papers/pdf/eff_res.pdf
3. R. E. Kooij and M. A. Achterberg, *Minimizing the Effective Graph Resistance by Adding Links Is NP-hard*, Operations Research Letters 51 (2023), 601–604. https://arxiv.org/abs/2302.12628
4. O. Bhoite, V. S. Dhuli, S. Werner and K. Kansanen, *Budget-Constrained Graph Augmentation for Robust Network Design via Kirchhoff Index Minimization*, preprint (2026). https://arxiv.org/abs/2609.29790
