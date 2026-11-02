# Rigidity and spectral freedom of all fastest-mixing chains on complete split graphs

## Finding

For integers \(p,q\ge2\), let \(G_{p,q}=K_p\vee\overline{K_q}\): a \(p\)-vertex clique \(X\) joined to \(q\) mutually nonadjacent vertices \(Y\). Among **all** real symmetric, entrywise nonnegative, row-stochastic matrices \(P\) supported on the edges and loops of \(G_{p,q}\), minimize the second-largest eigenvalue modulus \(\mu(P)=\|P-\mathbf1\mathbf1^{\mathsf T}/(p+q)\|_2\).

The complete set of global minimizers is as follows. If \(q<2p\), every optimum has precisely the same weight on **every** cross edge \(X\)--\(Y\), namely
\[
 b_* = \frac{2}{q+2p},\qquad \mu_* = \frac{q}{q+2p}.
\]
The weights \(w_{ij}=P_{ij}=P_{ji}\ge0\) on the clique edges may vary independently. Let \(L_W\) be their \(p\)-by-\(p\) weighted Laplacian and \(d_i=\sum_{j\ne i}w_{ij}\). Such a matrix is optimal **if and only if**
\[
 d_i\le \frac{2p-q}{q+2p}\quad (i\in X),
\qquad
 \frac{2(p-q)}{q+2p}\le\lambda_j(L_W)\le\frac{2p}{q+2p}\quad(j=2,\ldots,p),
\]
with eigenvalues ordered \(0=\lambda_1(L_W)\le\cdots\le\lambda_p(L_W)\). The diagonal entries are uniquely determined by row stochasticity.

If \(q\ge2p\), the **unique** global optimizer has cross weights \(b_*=1/q\), all clique weights zero, and
\[
 \mu_* = 1-\frac pq.
\]
The formulas agree at the boundary \(q=2p\). In particular, when \(p>q\), the internal clique support of **every** optimal chain is connected (its Laplacian has a strictly positive spectral gap). For \(p\le q<2p\), an empty clique support is optimal, but additional clique weights may also be optimal. For \(q\ge2p\), every optimal clique edge has weight zero. Thus **all** cross-edge weights are rigid, while the permitted clique designs undergo a connected / optional / forced-zero transition.

The optimum **value alone** is not claimed to be new: it also follows from previously published fastest-mixing formulas for a weighted star together with clique lifting. The contribution assessed here is the all-global-optimizer rigidity and necessary-and-sufficient internal spectral characterization, including its forced connectivity and deletion regimes.

## Assumptions and scope

The graph is finite, simple except for allowed holding probabilities, and contains every clique edge and all \(pq\) cross edges as *permitted* transitions; any permitted edge is allowed probability zero. Every \(P\) is real symmetric, nonnegative, stochastic, and has zero off-diagonal entries outside this support. No automorphism invariance or uniform-edge restriction is imposed. The displayed result applies to every integer \(p,q\ge2\), including all equality cases. The \(p\)-clique can have arbitrary nonuniform optimal internal weights. Statements about uniqueness of crossing edges hold over the entire unrestricted feasible set, not merely over automorphism-invariant chains.

## Proof

**1. Two universal lower bounds.** Write \(C=(P_{ij})_{i\in X,j\in Y}\), \(S=\sum_{i\in X,j\in Y}C_{ij}\). Each clique vertex has transition mass at most one, hence \(0\le S\le p\). The \(Y\)-by-\(Y\) principal block of \(P\) is diagonal with entries \(1-\sum_{i\in X}C_{ij}\). Let \(U\) be the \((q-1)\)-dimensional subspace of vectors supported on \(Y\) whose coordinates sum to zero. The trace of the compression of \(P\) to \(U\) is \((q-1)(1-S/q)\). Every vector in \(U\) is orthogonal to \(\mathbf1\), so its Rayleigh quotient is at most \(\mu(P)\). Taking the average of an orthonormal basis gives
\[
 \mu(P)\ge 1-\frac Sq. \tag{1}
\]
The vector equal to \(1/p\) on \(X\) and \(-1/q\) on \(Y\) also has zero total sum. Only cross edges contribute to its Dirichlet energy, so its Rayleigh quotient for \(P\) is exactly \(1-(p+q)S/(pq)\). Since all nonconstant eigenvalues lie in \([-\mu(P),\mu(P)]\),
\[
 \mu(P)\ge \frac{p+q}{pq}S-1. \tag{2}
\]
Consequently \(\mu(P)\) is at least the maximum of the decreasing and increasing affine functions in (1)--(2), minimized over \(0\le S\le p\). Their intersection is at \(S_*=2pq/(q+2p)\), which lies in this interval exactly when \(q\le2p\). It yields \(\mu(P)\ge q/(q+2p)\) in that range. If \(q>2p\), the minimum occurs at \(S=p\) and gives \(\mu(P)\ge1-p/q\).

**2. All optimizers have uniform cross weights.** First suppose \(q<2p\). Any optimum attaining the lower bound must have \(S=S_*\). At this point the average Rayleigh quotient on \(U\) equals \(t=q/(q+2p)\), and all Rayleigh quotients of \(P\) on \(\mathbf1^\perp\) are at most \(t\). Positivity of \(tI-P\) on \(\mathbf1^\perp\) therefore forces \(Py=ty\) for *every* \(y\in U\) (zero quadratic form of a positive semidefinite operator forces its vector into the nullspace). The \(X\)-coordinates of this identity give \(Cy=0\) for every zero-sum \(y\in\mathbb R^q\); equivalently, each row of \(C\) is constant across the \(q\) columns. Simultaneously the two-part Rayleigh quotient in (2) equals \(-t\), so its test vector is an actual eigenvector of \(P\) with eigenvalue \(-t\). In its \(X\) coordinates this requires the cross-row sums of \(C\) to be equal. Thus **all** entries of \(C\) equal \(S_*/(pq)=2/(q+2p)\).

For \(q\ge2p\), attaining the bound requires \(S=p\). Every \(X\)-row then spends its entire probability budget on cross edges, hence no clique edge or \(X\)-holding probability can be positive. In the equality case \(q=2p\), and also for \(q>2p\), the compressed trace on \(U\) equals the optimal bound \(t=1-p/q\); the same positive-semidefinite equality argument implies \(Cy=0\) for every \(y\in U\). Each row of \(C\) is consequently constant across \(Y\), and its row sum is one, giving \(C_{ij}=1/q\). This also proves uniqueness when \(q\ge2p\).

**3. All freedom in the clique.** When \(q<2p\), insert the forced \(C=b_*\mathbf1_p\mathbf1_q^{\mathsf T}\). The orthogonal decomposition into the all-ones mode, the constant-on-parts contrast, the \(Y\)-zero-sum subspace, and the \(X\)-zero-sum subspace gives the exact eigenvalue multiset
\[
 \bigl\{1,\,1-(p+q)b_*,\,(1-pb_*)^{[q-1]},\,1-qb_*-\lambda_j(L_W)\ (j=2,\ldots,p)\bigr\}.
\]
Here the bracketed superscript denotes multiplicity. The first three eigenvalue classes equal \(1,-t,t\), respectively. Thus the remaining class lies in \([-t,t]\) exactly when all nonzero-index eigenvalues of \(L_W\) lie in the displayed interval. Nonnegativity of the holding probability on \(X\) is exactly \(d_i\le1-qb_*=(2p-q)/(q+2p)\). These necessary and sufficient conditions prove the full classification.

**4. Attainment and structural phases.** If \(p\le q<2p\), choose \(W=0\); its zero Laplacian eigenvalues lie in the required interval and the degree bound holds. If \(p>q\), choose equal clique weights \(w_{ij}=2(p-q)/[p(q+2p)]\): the nonzero-index eigenvalues are exactly the positive lower endpoint, and the degree condition holds because \(p(q+2)-2q>0\). For \(q\ge2p\), the uniform cross-only allocation already satisfies both spectral bounds. Therefore all lower bounds are attained. When \(p>q\), the required positive \(\lambda_2(L_W)\) forces positive-weight clique connectivity. When \(p\le q<2p\), the zero choice and sufficiently small positive clique weights exhibit optional internal support. When \(q\ge2p\), budget saturation forces its deletion.

## Verification

The included standalone Python program `check.py` computes exact-rational full transition spectra for 70 parameter pairs \(2\le p\le8\), \(2\le q\le11\), verifies all holding probabilities, demonstrates a nonuniform optimal clique-weight example on \(G_{4,2}\), and compares the asserted optimum with 1,575 independently adjustable feasible random designs. It reports `PASS exact rational spectra: 70; nonuniform core witness: 1; independently adjustable feasible comparisons: 1575`. The all-parameter theorem, rigidity, and necessity statements follow from the proof above, **not** from this finite test suite.

## Relationship to prior work

Boyd--Diaconis--Xiao (2004) introduce convex/Semidefinite fastest-mixing Markov-chain design. Boyd--Diaconis--Parrilo--Xiao (2009, Section 5.4.2) explicitly determine optimal cross weights and rates on complete bipartite graphs, and provide symmetry-based block diagonalization. Jafarizadeh (2020, Theorem 1 and the star formulas in Section VI-E) establishes the clique-lift value correspondence; the split graph here is a clique lifting of a star, so the **optimal objective value and existence of a symmetric lifted solution are already implied by that source**. The present statement instead classifies **all** optimal matrices, including unrestricted cross-edge rigidity and the exact allowed spectrum/degree polytope of nonuniform clique designs. Those all-optimality statements do not follow from merely exhibiting a lifted optimum and were not found stated in the inspected source passages.

## Limitations

This is a mathematical statement about symmetric stochastic chains with uniform stationary law and arbitrary allowed self-loops. It does not classify general nonreversible chains, nonuniform stationary distributions, prescribed-positive-edge constraints, or nonclique internal topologies. Existing clique-lift results already cover the optimum *value*; no novelty is claimed for that sub-result. Some specialized literature might explicitly classify the full optimal face; such coverage was not identified in the examined material. No independent audit or publication-priority certification has occurred.

## References

1. S. Boyd, P. Diaconis, L. Xiao, *Fastest Mixing Markov Chain on a Graph*, SIAM Review **46** (2004), 667--689. DOI `10.1137/S0036144503423264`. Public PDF: `https://web.stanford.edu/~boyd/papers/pdf/fmmc.pdf`.
2. S. Boyd, P. Diaconis, P. Parrilo, L. Xiao, *Fastest Mixing Markov Chain on Graphs with Symmetries*, SIAM Journal on Optimization **20** (2009), 792--819. DOI `10.1137/070689413`. First arXiv version: `arXiv:0709.0955v1`, September 6, 2007. Public PDF: `https://web.stanford.edu/~boyd/papers/pdf/fast_mix_symm.pdf`.
3. S. Jafarizadeh, *Fastest Mixing Reversible Markov Chain: Clique Lifted Graphs and Subgraphs*, IEEE Transactions on Signal and Information Processing over Networks **6** (2020), 88--104. DOI `10.1109/TSIPN.2020.2964211`. Accessible author-posted full text: `https://www.researchgate.net/publication/338414306_Fastest_Mixing_Reversible_Markov_Chain_Clique_Lifted_Graphs_Subgraphs`.
